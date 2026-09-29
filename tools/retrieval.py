"""Build an offline navigation index over tracked artifacts and search it.

Run ``python -m tools.retrieval QUERY`` with optional ``--layer``, ``--status``,
``--authority``, ``--version``, ``--topic``, ``--limit``, ``--json`` and
``--index-output PATH``. The public API is ``build_index(root)`` and
``search(index, query, ...)``; the index is rebuilt per run and never required
on disk.

The index is a navigation projection (knowledge/architecture.md). It points to
stable paths and anchors and never enters grounding. It reads the Markdown
layers, glossary and knowledge documents, the registry, the locks and
admission manifests it needs, the references and the Guidelines navigation
projection. It never opens ``00_sources/`` or ``corpus/raw/`` and runs no
source command. Manifests without admissions, such as multi-megabyte stream
runs, are recognized by a byte scan and never parsed. Passages keep a short
snippet and their term set, so a serialized index holds no complete body.

Source authority comes from the registry entry of the admitting family and
from the admission record (knowledge/data.md), never from a file name. Metadata
that the control plane does not state stays ``None`` with a recorded gap.
Curated topics come from artifact frontmatter; rule-based suggestions come only
from the navigation projection and stay a separate list.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from tools.sitegen.documents import WIKI, read_document
from tools.sitegen.knowledge_view import anchored_blocks

GENERATOR = "tools.retrieval v1"
USE = "navigation-only; never grounding"
NAVIGATION = "corpus/projections/guidelines-navigation-4.12.0.json"
REGISTRY = "sources/registry.yaml"
MANIFESTS = "sources/manifests"
REFERENCES = "references"
CHAIN_FOLDERS = ("10_markdown", "20_distillates", "30_assertions", "40_output")
LAYERS = (*CHAIN_FOLDERS, "glossary", "knowledge")
CHAIN_TYPES = ("representation", "distillate", "assertion", "chapter", "moc")
EVIDENCE_KINDS = ("representation", "distillate", "assertion", "chapter")
STATUS_KINDS = ("distillate", "assertion", "chapter")
KIND_ORDER = ("assertion", "distillate", "representation", "chapter", "moc", "glossary",
              "project-contract", "project-proposal", "project-record")
STATUSES = ("grounded", "validated", "verified", "contested", "superseded")
REQUIRED_CHECKS = {"validated": ("validation", "machine-review"),
                   "verified": ("validation", "machine-review", "verification")}
# knowledge/INDEX.md: the model, architecture, evaluation and experiment documents
# record hypotheses outside the evidence chain; the others control the project.
PROPOSAL_DOCUMENTS = frozenset({"experiments", "hsa-profile", "identity-evidence", "model-design",
                                "model-examples", "ontology", "p6-architecture", "p6-evaluation",
                                "text-model", "text-model-bindings"})
CONTRACT_DOCUMENTS = frozenset({"INDEX", "architecture", "data", "design", "governance", "handoff",
                                "journal", "operations", "plan", "project", "releases", "schema",
                                "specification", "state", "testing", "verification"})
CHAIN_RELATIONS = ("distills", "grounding", "cites-assertion")
SNIPPET = 240
RESULT_PASSAGES = 3
ADMISSIONS = re.compile(rb"^(?:reused_)?admissions:", re.M)
REGION = re.compile(r"<!-- ([a-z-]+):begin -->.*?<!-- \1:end -->", re.S)
HEADING = re.compile(r"^#{1,6} +(.+?)[ \t]*$")
FENCE = re.compile(r"^[ \t]*(?:```|~~~)")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
TERM = re.compile(r"\w[\w.:-]*\w|\w")
STOPWORDS = frozenset({"a", "an", "and", "are", "as", "at", "be", "by", "do", "does", "for",
                       "from", "how", "in", "is", "it", "of", "on", "or", "that", "the", "this",
                       "to", "was", "what", "when", "where", "which", "who", "why", "with"})
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


@dataclass
class _Control:
    """Control-plane facts read once per index build."""

    root: Path
    inputs: dict = field(default_factory=dict)
    gaps: list = field(default_factory=list)
    registry: dict = field(default_factory=dict)
    admissions: dict = field(default_factory=dict)
    references: dict = field(default_factory=dict)
    navigation: dict = field(default_factory=dict)
    releases: dict = field(default_factory=dict)


def terms(text: str) -> list[str]:
    """Casefolded terms, adding the parts of dotted, colon or hyphenated idents."""
    found = set()
    for term in TERM.findall(text.casefold()):
        found.add(term)
        if any(mark in term for mark in ".:-"):
            found.update(part for part in re.split(r"[.:-]+", term) if part)
    return sorted(found)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_yaml(data: bytes):
    return yaml.load(data, Loader=LOADER)


def _plain(value):
    """JSON-safe copy in which YAML dates become ISO strings."""
    return json.loads(json.dumps(value, default=str))


def _values(value) -> list:
    if value is None or value == "":
        return []
    return list(value) if isinstance(value, list) else [value]


def _link(value) -> tuple[str, str]:
    """Repository path and block anchor of a wikilink, or two empty strings."""
    match = WIKI.fullmatch(str(value).strip())
    if not match:
        return "", ""
    path, _, anchor = match.group(1).partition("#")
    if path.split("/", 1)[0] in (*CHAIN_FOLDERS, "glossary", "knowledge") and not path.endswith(".md"):
        path += ".md"
    return path, anchor.removeprefix("^")


def _topic(value) -> str:
    path, _ = _link(value)
    return (path or str(value)).removesuffix(".md").rsplit("/", 1)[-1].removeprefix("MOC-").strip()


def _unlink(text: str) -> str:
    return WIKI.sub(lambda m: m.group(2) or m.group(1).split("#")[0].rsplit("/", 1)[-1], text)


def _snippet(text: str) -> str:
    flat = " ".join(text.split())
    return flat if len(flat) <= SNIPPET else flat[:SNIPPET - 1].rstrip() + "…"


def _clean(text: str) -> str:
    text = re.sub(r"^[ \t]*(?:```|~~~)[\w-]*[ \t]*$", "", text, flags=re.M)
    return _unlink(re.sub(r"[ \t]*\^[A-Za-z0-9-]+[ \t]*$", "", text, flags=re.M)).strip()


def _passage(locator: str, anchor: str | None, heading: str | None, text: str, cites: list[str]) -> dict:
    clean = _clean(text)
    return {"locator": locator, "anchor": anchor, "heading": heading, "snippet": _snippet(clean),
            "terms": terms(clean), "cites": cites}


def _sections(body: str) -> list[tuple[str, str]]:
    """Heading-delimited sections of an unanchored document, generated regions removed."""
    result, heading, lines, fence = [], "", [], False
    for line in REGION.sub("", body).splitlines():
        if FENCE.match(line):
            fence = not fence
        match = None if fence else HEADING.match(line)
        if match:
            if "".join(lines).strip() or heading:
                result.append((heading, "\n".join(lines)))
            heading, lines = match.group(1), []
        else:
            lines.append(line)
    if "".join(lines).strip() or heading:
        result.append((heading, "\n".join(lines)))
    return result


def _passages(path: str, kind: str, body: str) -> list[dict]:
    if kind in ("representation", "distillate"):
        result = []
        for anchor, text in anchored_blocks(body, kind).items():
            cites = []
            if kind == "distillate":
                for match in WIKI.finditer(text):
                    target, target_anchor = _link(match.group(0))
                    cites.append(f"{target}#^{target_anchor}" if target_anchor else target)
            result.append(_passage(f"{path}#^{anchor}", anchor, None, text, cites))
        return result
    return [_passage(f"{path}#{heading}" if heading else path, None, heading or None, f"{heading}\n{text}", [])
            for heading, text in _sections(body)]


def _title(meta: dict, body: str, path: str) -> str:
    metadata = meta.get("metadata") if isinstance(meta.get("metadata"), dict) else {}
    heading = re.search(r"^# (.+)$", body, re.M)
    return str(metadata.get("title") or meta.get("title") or (heading.group(1) if heading else Path(path).stem))


def _excerpt(kind: str, body: str, passages: list[dict]) -> str:
    if kind == "assertion":
        statement = re.search(r"^## Statement[ \t]*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
        if statement:
            return _snippet(_unlink(statement.group(1)))
    if kind == "representation":
        return passages[0]["snippet"] if passages else ""
    for paragraph in re.split(r"\n\s*\n", REGION.sub("", body)):
        text = paragraph.strip()
        if text and not text.startswith(("#", "<!--", "```", "~~~", "|", "- ", ">", "[^")):
            return _snippet(_unlink(text))
    return ""


def _kind(folder: str, path: str, meta: dict) -> str | None:
    if folder == "knowledge":
        stem = Path(path).stem
        if stem in PROPOSAL_DOCUMENTS:
            return "project-proposal"
        return "project-contract" if stem in CONTRACT_DOCUMENTS else "project-record"
    if folder == "glossary":
        return "glossary" if meta.get("type") == "glossary" else None
    return meta.get("type") if meta.get("type") in CHAIN_TYPES else None


def _registry(control: _Control) -> None:
    file = control.root / REGISTRY
    if not file.is_file():
        control.gaps.append({"path": REGISTRY, "reason": "Registry absent; family authority and rights are unknown."})
        return
    data = file.read_bytes()
    control.inputs[REGISTRY] = _sha256(data)
    for source in (_load_yaml(data) or {}).get("sources") or []:
        trust, rights = source.get("trust") or {}, source.get("rights") or {}
        control.registry[source.get("source_id")] = {"content_authority": trust.get("content_authority"),
                                                     "rights_status": rights.get("rights_status"),
                                                     "lock": source.get("lock")}


def _admissions(control: _Control) -> None:
    """Keep one authoritative admission per artifact together with its reuse chain."""
    found: dict[str, list[dict]] = {}
    folder = control.root / MANIFESTS
    for file in sorted(folder.glob("*.yaml")) if folder.is_dir() else []:
        data = file.read_bytes()
        if not ADMISSIONS.search(data):
            continue
        relative = file.relative_to(control.root).as_posix()
        control.inputs[relative] = _sha256(data)
        try:
            manifest = _load_yaml(data) or {}
        except yaml.YAMLError:
            control.gaps.append({"path": relative, "reason": "Unreadable admission manifest; its admissions are unknown."})
            continue
        upstream = manifest.get("upstream_manifests") or manifest.get("upstream_manifest") or []
        header = {"source_id": manifest.get("source_id"), "lock_file": manifest.get("lock_file"),
                  "content_authority": manifest.get("content_authority"),
                  "upstream_manifests": [upstream] if isinstance(upstream, str) else list(upstream)}
        for key in ("admissions", "reused_admissions"):
            for item in manifest.get(key) or []:
                artifact = item.get("representation_path") or item.get("distillate_path")
                if artifact:
                    found.setdefault(artifact, []).append({"manifest": relative, "item": item, "header": header})
    for artifact, entries in sorted(found.items()):
        originals = [entry for entry in entries if not entry["item"].get("reused_admission")]
        if len(originals) != 1:
            control.gaps.append({"path": artifact, "reason": f"{len(originals)} original admissions; provenance is left unknown."})
            continue
        original = originals[0]
        by_manifest = {entry["manifest"]: entry for entry in entries}
        chain, broken = [original["manifest"]], False
        for entry in sorted(entries, key=lambda item: item["manifest"]):
            if entry is original:
                continue
            step, seen = entry, set()
            while step is not None and step is not original and step["manifest"] not in seen:
                seen.add(step["manifest"])
                step = by_manifest.get(step["item"].get("reused_admission") or "")
            broken = broken or step is not original
            chain.append(entry["manifest"])
        if broken:
            control.gaps.append({"path": artifact, "reason": "A reused admission does not lead back to its original; provenance is left unknown."})
            continue
        control.admissions[artifact] = {**original, "chain": chain}


def _references(control: _Control) -> None:
    folder = control.root / REFERENCES
    for file in sorted(folder.glob("*.json")) if folder.is_dir() else []:
        relative = file.relative_to(control.root).as_posix()
        data = file.read_bytes()
        control.inputs[relative] = _sha256(data)
        for record in json.loads(data):
            identifier = record.get("id")
            if identifier in control.references:
                control.gaps.append({"path": relative, "reason": f"Duplicate reference id {identifier}; its citation is unknown."})
                control.references[identifier] = None
            else:
                control.references[identifier] = {"path": relative, "record": record}


def _navigation(control: _Control) -> None:
    file = control.root / NAVIGATION
    if not file.is_file():
        control.gaps.append({"path": NAVIGATION, "reason": "Guidelines navigation absent; idents, declared attributes and rule suggestions are unknown."})
        return
    data = file.read_bytes()
    control.inputs[NAVIGATION] = _sha256(data)
    projection = json.loads(data)
    if projection.get("use") != USE:
        control.gaps.append({"path": NAVIGATION, "reason": "Guidelines navigation does not declare navigation-only use; ignored."})
        return
    for row in projection.get("sources") or []:
        control.navigation[row["representation"]] = {
            "source": row.get("source"), "kind": row.get("kind"), "module": row.get("module"),
            "module_basis": row.get("module_basis"), "ident": row.get("ident"),
            "attributes": list(row.get("attributes") or []),
            "suggested": [{"topic": s["topic"], "rule": s["rule"], "projection": NAVIGATION}
                          for s in row.get("topic_suggestions") or []]}


def _release(control: _Control, lock: str | None) -> dict | None:
    """Release version and commit that a lock resolves, read once per lock."""
    if not lock:
        return None
    if lock not in control.releases:
        control.releases[lock] = None
        file = (control.root / lock).resolve()
        if file.is_relative_to(control.root.resolve()) and file.is_file():
            data = file.read_bytes()
            control.inputs[lock] = _sha256(data)
            release = (_load_yaml(data) or {}).get("release") or {}
            if release.get("resolved_full_commit_sha") and release.get("version"):
                control.releases[lock] = {"version": str(release["version"]),
                                          "commit": str(release["resolved_full_commit_sha"])}
    return control.releases[lock]


def _source(control: _Control, admission: dict, record: dict) -> dict:
    item, header = admission["item"], admission["header"]
    family = control.registry.get(header["source_id"])
    if family is None:
        record["gaps"].append({"field": "source.family_authority",
                               "reason": f"Registry names no source family {header['source_id']!r}."})
    lock = item.get("lock_file") or header["lock_file"] or (family or {}).get("lock")
    git_record = item.get("record") or {}
    if git_record.get("kind") != "git-blob":
        git_record = {}
    commit_value = item.get("commit") or git_record.get("commit")
    commit = str(commit_value) if commit_value else None
    release = _release(control, lock) if commit else None
    version = release["version"] if release and release["commit"] == commit else None
    if commit and not version:
        record["gaps"].append({"field": "source.version", "reason": "No release version is established for this admission commit."})
    elif not commit and record["kind"] == "representation":
        record["gaps"].append({"field": "source.version", "reason": "The admission records no commit; version is unknown."})
    responses = [(snapshot.get("part"), snapshot.get("response") or {}) for snapshot in item.get("snapshots") or []]
    if item.get("response"):
        responses.append((None, item["response"]))
    return _plain({
        "source_id": header["source_id"], "family_authority": (family or {}).get("content_authority"),
        "admission_authority": item.get("content_authority") or item.get("authority") or header["content_authority"],
        "rights_status": (family or {}).get("rights_status"), "instruction_trust": item.get("instruction_trust", "none"),
        "admission_manifest": admission["manifest"], "manifest_chain": admission["chain"],
        "upstream_manifests": header["upstream_manifests"], "lock": lock, "commit": commit, "version": version,
        "git_path": item.get("git_path") or git_record.get("path"),
        "git_blob_id": item.get("git_blob_id") or git_record.get("blob"),
        "original_path": item.get("original_path"), "original_sha256": item.get("original_sha256"),
        "representation_sha256": item.get("representation_sha256"), "reference_id": item.get("reference_id"),
        "work_item": item.get("work_item"),
        "snapshots": [{"part": part, "sha256": response.get("sha256"), "observed_at": response.get("observed_at")}
                      for part, response in responses],
    })


def _record(path: str, layer: str, kind: str, meta: dict, body: str, digest: str) -> dict:
    checked = meta.get("checked") if kind in STATUS_KINDS else None
    record = {
        "path": path, "layer": layer, "kind": kind, "title": _title(meta, body, path),
        "evidence_chain": kind in EVIDENCE_KINDS,
        "status": str(meta["status"]) if kind in STATUS_KINDS and meta.get("status") else None,
        "checked": {str(k): str(v) for k, v in checked.items()} if isinstance(checked, dict) else {},
        "document_status": str(meta["status"]) if kind.startswith("project-") and meta.get("status") else None,
        "file_sha256": digest, "ident": None, "attributes": [], "navigation": None,
        "topics": {"curated": [], "suggested": []}, "source": None, "authorities": [], "versions": [],
        "direct_links": [], "navigation_links": [], "contested_with": [], "superseded_by": None,
        "excerpt": "", "passages": [], "gaps": [],
    }
    if kind == "representation" and (meta.get("metadata") or {}).get("confidential"):
        record["gaps"].append({"field": "passages", "reason": "Confidential representation; its body is not indexed."})
        return record
    try:
        record["passages"] = _passages(path, kind, body)
    except ValueError as error:
        record["gaps"].append({"field": "passages", "reason": f"Passages not indexed: {error}"})
    record["excerpt"] = _excerpt(kind, body, record["passages"])
    return record


def _representation(control: _Control, record: dict, meta: dict) -> None:
    original, _ = _link(meta.get("source", ""))
    if original:
        # The local original is named as a pointer and never opened.
        record["direct_links"].append({"relation": "represents-local-original", "path": original, "anchor": None})
    admission = control.admissions.get(record["path"])
    if admission is None:
        record["gaps"].append({"field": "source", "reason": "No admission manifest names this representation; source identity, authority and version are unknown."})
    else:
        record["source"] = _source(control, admission, record)
        expected = record["source"]["representation_sha256"]
        if expected and expected != record["file_sha256"]:
            record["gaps"].append({"field": "file_sha256", "reason": "Representation bytes differ from the admission record."})
    row = control.navigation.get(record["path"])
    if row:
        record["ident"], record["attributes"] = row["ident"], row["attributes"]
        record["navigation"] = {"projection": NAVIGATION, "source": row["source"], "kind": row["kind"],
                                "module": row["module"], "module_basis": row["module_basis"]}
        record["topics"]["suggested"] = row["suggested"]


def _distillate(control: _Control, record: dict, meta: dict) -> None:
    record["topics"]["curated"] = [{"topic": _topic(value), "basis": "own-frontmatter"} for value in _values(meta.get("topics"))]
    successor, _ = _link(meta.get("superseded-by") or "")
    record["superseded_by"] = successor or None
    if meta.get("source-type") == "publication":
        reference = control.references.get(meta.get("reference"))
        record["direct_links"].append({"relation": "cites-reference", "path": reference["path"] if reference else None,
                                       "anchor": meta.get("reference")})
        if reference is None:
            record["gaps"].append({"field": "direct_links", "reason": "The cited reference id is missing or ambiguous."})
        admission = control.admissions.get(record["path"])
        if admission is None:
            record["gaps"].append({"field": "source", "reason": "No citation admission names this distillate; source authority is unknown."})
        else:
            record["source"] = _source(control, admission, record)
        return
    representation, _ = _link(meta.get("representation", ""))
    if representation:
        record["direct_links"].append({"relation": "distills", "path": representation, "anchor": None})
    else:
        record["gaps"].append({"field": "direct_links", "reason": "The distillate names no representation."})


def _assertion(record: dict, meta: dict) -> None:
    record["topics"]["curated"] = [{"topic": _topic(value), "basis": "own-frontmatter"} for value in _values(meta.get("topics"))]
    for value in _values(meta.get("grounding")):
        path, anchor = _link(value)
        record["direct_links"].append({"relation": "grounding", "path": path or str(value), "anchor": anchor or None})
    record["contested_with"] = [{"path": _link(value)[0] or str(value)} for value in _values(meta.get("contested-with"))]
    for relation, key in (("phenomenon", "phenomena"), ("related", "related")):
        for value in _values(meta.get(key)):
            record["navigation_links"].append({"relation": relation, "path": _link(value)[0] or str(value), "anchor": None})


def _connect(records: dict[str, dict]) -> None:
    """Resolve direct links, propagate curated topics and chain authorities, surface contests."""
    for record in records.values():
        for link in record["direct_links"]:
            if link["relation"] in CHAIN_RELATIONS and link["path"] not in records:
                record["gaps"].append({"field": "direct_links", "reason": f"Link target is not indexed: {link['path']}"})
        if record["kind"] == "distillate":
            for link in record["direct_links"]:
                target = records.get(link["path"]) if link["relation"] == "distills" else None
                for topic in record["topics"]["curated"] if target else []:
                    target["topics"]["curated"].append({"topic": topic["topic"], "basis": "distillate-topics",
                                                        "distillate": record["path"]})
        for counterpart in record["contested_with"]:
            target = records.get(counterpart["path"])
            counterpart.update(title=target["title"] if target else None,
                               status=target["status"] if target else None, indexed=target is not None)
        if record["status"] == "contested" and not record["contested_with"]:
            record["gaps"].append({"field": "contested_with", "reason": "Contested status names no counterpart."})
    # Authorities and versions follow the direct chain upward, one layer at a time.
    for kind in EVIDENCE_KINDS:
        for record in (r for r in records.values() if r["kind"] == kind):
            authorities, versions = set(), set()
            if record["source"]:
                authorities.add(record["source"]["family_authority"])
                versions.update((record["source"]["version"], record["source"]["commit"]))
            for link in record["direct_links"]:
                target = records.get(link["path"]) if link["relation"] in CHAIN_RELATIONS else None
                if target:
                    authorities.update(target["authorities"])
                    versions.update(target["versions"])
            record["authorities"] = sorted(a for a in authorities if a)
            record["versions"] = sorted(v for v in versions if v)


def build_index(root: Path) -> dict:
    """Index the tracked artifacts at ``root`` for navigation; see the module docstring."""
    control = _Control(Path(root))
    _registry(control)
    _admissions(control)
    _references(control)
    _navigation(control)
    records: dict[str, dict] = {}
    for folder in LAYERS:
        base = control.root / folder
        if not base.is_dir():
            control.gaps.append({"path": folder, "reason": "Folder absent; nothing is indexed from it."})
            continue
        pattern = "**/*.md" if folder in CHAIN_FOLDERS else "*.md"
        for file in sorted(base.glob(pattern), key=lambda p: p.relative_to(control.root).as_posix()):
            path = file.relative_to(control.root).as_posix()
            try:
                meta, body = read_document(control.root, path)
            except (ValueError, yaml.YAMLError) as error:
                control.gaps.append({"path": path, "reason": f"Unreadable document: {error.__class__.__name__}"})
                continue
            kind = _kind(folder, path, meta)
            if kind is None:
                control.gaps.append({"path": path, "reason": f"Unsupported artifact type {meta.get('type')!r}; not indexed."})
                continue
            record = _record(path, folder, kind, meta, body, _sha256(file.read_bytes()))
            if kind == "representation":
                _representation(control, record, meta)
            elif kind == "distillate":
                _distillate(control, record, meta)
            elif kind == "assertion":
                _assertion(record, meta)
            elif kind == "chapter":
                record["direct_links"] = [{"relation": "cites-assertion", "path": _link(v)[0] or str(v), "anchor": None}
                                          for v in _values(meta.get("assertions"))]
            elif kind == "moc" and meta.get("topic"):
                record["topics"]["curated"] = [{"topic": str(meta["topic"]), "basis": "topic-map"}]
            elif kind == "glossary":
                record["navigation_links"] = [{"relation": "related", "path": _link(v)[0] or str(v), "anchor": None}
                                              for v in _values(meta.get("related"))]
            elif kind in ("project-contract", "project-proposal"):
                record["authorities"] = [kind]
            records[path] = record
    _connect(records)
    ordered = [records[path] for path in sorted(records)]
    return {"schema_version": 1, "generator": GENERATOR, "use": USE, "instruction_trust": "none",
            "scope": {"indexed": list(LAYERS), "never_opened": ["00_sources", "corpus/raw"],
                      "control_inputs": "registry, resolving locks, admission manifests, references, Guidelines navigation"},
            "inputs": dict(sorted(control.inputs.items())),
            "counts": {kind: sum(r["kind"] == kind for r in ordered) for kind in KIND_ORDER},
            "gaps": control.gaps, "records": ordered}


def _admitted(record: dict, layer: str | None, status: str | None, authority: str | None,
              version: str | None, topic: str | None) -> bool:
    if layer is not None and layer not in (record["layer"], record["kind"]):
        return False
    if status is not None:
        if record["status"] != status:
            return False
        # A status without its recorded check dates does not pass the filter.
        if any(not ISO_DATE.fullmatch(record["checked"].get(check, "")) for check in REQUIRED_CHECKS.get(status, ())):
            return False
    if authority is not None and authority not in record["authorities"]:
        return False
    if version is not None and version not in record["versions"]:
        return False
    if topic is not None:
        names = {item["topic"].casefold() for group in record["topics"].values() for item in group}
        if _topic(topic).casefold() not in names:
            return False
    return True


def _score(record: dict, text: str, candidate: str, attribute: bool, wanted: list[str]) -> tuple | None:
    score, reasons = 0, []
    ident = record["ident"]
    if candidate and ident:
        if ident == candidate:
            score += 500 if attribute else 1000
            reasons.append(f"exact-ident:{candidate}")
        elif ident.casefold() == candidate.casefold():
            score += 400 if attribute else 900
            reasons.append(f"ident-casefold:{ident}")
    if candidate and candidate in record["attributes"]:
        score += 800 if attribute else 300
        reasons.append(f"declares-attribute:{candidate}")
    if record["title"].casefold() == text.casefold():
        score += 400
        reasons.append("exact-title")
    title_terms = set(terms(record["title"]))
    topics = [item["topic"] for group in record["topics"].values() for item in group]
    meta_terms = set(terms(" ".join([ident or "", *record["attributes"], record["path"], *topics])))
    passage_terms = [set(passage["terms"]) for passage in record["passages"]]
    matched = []
    for term in wanted:
        in_title, in_meta = term in title_terms, term in meta_terms
        count = sum(term in found for found in passage_terms)
        if not (in_title or in_meta or count):
            continue
        matched.append(term)
        score += 100 + (30 if in_title else 0) + (20 if in_meta else 0) + 2 * min(count, 5)
        reasons.append(f"term:{term} title={in_title} metadata={in_meta} passages={count}")
    if not score:
        return None
    ranked = sorted(range(len(passage_terms)), key=lambda i: (-sum(t in passage_terms[i] for t in wanted), i))
    chosen = [i for i in ranked[:RESULT_PASSAGES] if any(t in passage_terms[i] for t in wanted)]
    return score, reasons, matched, [(i, [t for t in wanted if t in passage_terms[i]]) for i in chosen]


def search(index: dict, query: str, *, layer: str | None = None, status: str | None = None,
           authority: str | None = None, version: str | None = None, topic: str | None = None,
           limit: int = 20) -> list[dict]:
    """Rank indexed records for ``query``.

    Filters are exact. ``validated`` and ``verified`` also require their recorded
    check dates. A single-token query is compared with TEI idents and, when it
    starts with ``@``, preferably with declared attributes. A query without
    any indexed term returns an empty list rather than a guess.
    """
    if limit < 1:
        raise ValueError("limit must be positive")
    if layer is not None and layer not in LAYERS and layer not in KIND_ORDER:
        raise ValueError(f"Unknown layer or kind: {layer}")
    if status is not None and status not in STATUSES:
        raise ValueError(f"Unknown status: {status}")
    text = " ".join(str(query).split())
    if not text:
        raise ValueError("Empty query")
    attribute = text.startswith("@")
    candidate = "" if " " in text else text.strip("<>/").removeprefix("@")
    wanted = [term for term in dict.fromkeys(TERM.findall(text.casefold())) if term not in STOPWORDS]
    if not wanted:
        return []
    hits = []
    for record in index["records"]:
        if _admitted(record, layer, status, authority, version, topic):
            scored = _score(record, text, candidate, attribute, wanted)
            if scored:
                hits.append((scored, record))
    hits.sort(key=lambda hit: (-hit[0][0], KIND_ORDER.index(hit[1]["kind"]), hit[1]["path"]))
    results = []
    for rank, ((score, reasons, matched, chosen), record) in enumerate(hits[:limit], 1):
        result = _plain({key: value for key, value in record.items() if key != "passages"})
        passages = [{**{k: record["passages"][i][k] for k in ("locator", "anchor", "heading", "snippet", "cites")},
                     "matched_terms": found} for i, found in chosen]
        result.update(rank=rank, score=score, reasons=reasons, matched_terms=matched,
                      missing_terms=[t for t in wanted if t not in matched], passages=_plain(passages), use=USE)
        results.append(result)
    return results


def render(results: list[dict], index: dict) -> str:
    lines = ["Navigation only: pointers to tracked artifacts, never grounding or an answer."]
    if not results:
        lines.append("No indexed artifact matches the query; nothing is inferred.")
    for result in results:
        document = result["document_status"]
        status = result["status"] or (f"document {document}" if document else "no research status")
        authorities = ", ".join(result["authorities"]) or "unknown"
        versions = ", ".join(result["versions"]) or "unknown"
        rank, path, kind, score = result["rank"], result["path"], result["kind"], result["score"]
        lines.append(f"{rank}. {path} [{kind}; {status}; score {score}]")
        lines.append("   " + result["title"])
        lines.append(f"   authority: {authorities}; version: {versions}")
        if result["missing_terms"]:
            lines.append("   partial match; missing terms: " + ", ".join(result["missing_terms"]))
        if result["contested_with"]:
            lines.append("   contested with: " + ", ".join(c["path"] for c in result["contested_with"]))
        lines.extend("   " + passage["locator"] + ": " + passage["snippet"] for passage in result["passages"])
    gaps = len(index["gaps"])
    if gaps:
        lines.append(f"Index gaps: {gaps}; use --json to inspect them.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Search tracked artifacts for navigation; results never ground a claim.")
    parser.add_argument("query")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--layer", help="layer folder or artifact kind")
    parser.add_argument("--status", choices=STATUSES)
    parser.add_argument("--authority", help="registry content authority or project-contract/project-proposal")
    parser.add_argument("--version", help="release version or full commit of the source")
    parser.add_argument("--topic")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--index-output", type=Path, help="write the derived index as JSON; it is never required")
    args = parser.parse_args(argv)
    with contextlib.suppress(AttributeError, ValueError):
        sys.stdout.reconfigure(encoding="utf-8")
    index = build_index(args.root)
    if args.index_output:
        args.index_output.write_text(json.dumps(index, ensure_ascii=False, sort_keys=True) + "\n",
                                     encoding="utf-8", newline="\n")
    filters = {"layer": args.layer, "status": args.status, "authority": args.authority,
               "version": args.version, "topic": args.topic}
    try:
        results = search(index, args.query, limit=args.limit, **filters)
    except ValueError as error:
        parser.error(str(error))
    if args.json:
        payload = {"query": args.query, "filters": filters, "limit": args.limit, "generator": GENERATOR,
                   "use": USE, "index_inputs": index["inputs"], "index_gaps": index["gaps"], "results": results}
        sys.stdout.write(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    else:
        sys.stdout.write(render(results, index))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
