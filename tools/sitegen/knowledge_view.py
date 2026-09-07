"""Read the actual vault and resolve its immediate, anchored provenance edges.

This is a navigation projection, never another source of research grounding.
Original local files are named but never opened or linked for publication.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlsplit

import yaml

from tools.sitegen.documents import WIKI, read_document
from tools.sitegen.markup import doc_id, safe_url

LAYERS = {"representation": "10 · Source representation", "distillate": "20 · Distillate",
          "assertion": "30 · Assertion", "chapter": "40 · Output chapter"}
BLOCK = re.compile(r"\^([A-Za-z0-9-]+)[ \t]*$", re.M)


def block_id(path: str, anchor: str) -> str:
    return doc_id(path) + "--" + anchor.removeprefix("^")


def section(body: str, name: str) -> str:
    match = re.search(r"^## " + re.escape(name) + r"[ \t]*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return match.group(1).strip() if match else ""


def anchored_blocks(body: str, kind: str) -> dict[str, str]:
    if kind == "distillate":
        core = section(body, "Core statements")
        paragraphs = re.findall(r"^- .*?(?=^- |\Z)", core, re.M | re.S)
    else:
        paragraphs, paragraph, fence = [], [], None
        fenced, pending = [], []
        for line in body.splitlines():
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if fence:
                fenced.append(line)
                if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence):
                    fence = None
                    pending = fenced
                    fenced = []
                continue
            if marker:
                if paragraph:
                    paragraphs.append("\n".join(paragraph))
                    paragraph = []
                fence = marker.group(1)
                fenced = [line]
                pending = []
                continue
            if pending and re.fullmatch(r"\^[A-Za-z0-9-]+\s*", line):
                paragraphs.append("\n".join([*pending, "", line]))
                pending = []
                continue
            if not line.strip() or line.startswith("#"):
                if paragraph:
                    paragraphs.append("\n".join(paragraph))
                    paragraph = []
                if line.startswith("#"):
                    pending = []
            else:
                pending = []
                paragraph.append(line)
        if paragraph:
            paragraphs.append("\n".join(paragraph))
    result = {}
    for paragraph in paragraphs:
        anchors = BLOCK.findall(paragraph.splitlines()[-1]) if paragraph.lstrip().startswith(("```", "~~~")) else BLOCK.findall(paragraph)
        if len(anchors) > 1:
            raise ValueError("Multiple block anchors in one passage")
        if anchors:
            if anchors[0] in result:
                raise ValueError(f"Duplicate block anchor: {anchors[0]}")
            result[anchors[0]] = paragraph.strip()
    return result


def target(value: str) -> tuple[str, str]:
    match = WIKI.fullmatch(value)
    if not match:
        raise ValueError(f"Expected canonical wikilink: {value}")
    path, _, anchor = match.group(1).partition("#")
    if not path.endswith(".md"):
        path += ".md"
    if anchor and not re.fullmatch(r"\^[A-Za-z0-9-]+", anchor):
        raise ValueError(f"Expected exact block anchor: {value}")
    return path, anchor.removeprefix("^")


def _title(meta: dict, body: str, path: str) -> str:
    heading = re.search(r"^# (.+)$", body, re.M)
    return str(meta.get("metadata", {}).get("title") or (heading.group(1) if heading else meta.get("title") or Path(path).stem))


def _excerpt(body: str) -> str:
    paragraphs = re.split(r"\n\s*\n", body)
    return next((p for p in paragraphs if p.strip() and not p.startswith(("#", "<!--"))), "")


def _admissions(root: Path) -> dict[str, dict]:
    result = {}
    for file in sorted((root / "sources/manifests").glob("*.yaml")):
        manifest = yaml.safe_load(file.read_text(encoding="utf-8")) or {}
        for admission in manifest.get("admissions", []):
            key = admission.get("representation_path") or admission.get("distillate_path")
            if not key:
                continue
            if key in result:
                raise ValueError(f"Ambiguous source admission: {key}")
            rights = manifest.get("rights", {})
            result[key] = {"authority": admission.get("content_authority") or admission.get("authority") or manifest.get("content_authority"),
                           "version": admission.get("commit"), "observed": admission.get("response", {}).get("observed_at") or manifest.get("finished_at"),
                           "rights": admission.get("rights") or rights.get("attribution"),
                           "sha256": admission.get("original_sha256") or admission.get("response", {}).get("sha256"),
                           "manifest": file.relative_to(root).as_posix()}
    return result


def build_view(root: Path, date: str, repository_base: str | None = None) -> dict:
    root = Path(root)
    if repository_base:
        safe_url(repository_base)
        parsed = urlsplit(repository_base)
        if parsed.scheme != "https" or parsed.query or parsed.fragment:
            raise ValueError("repository_base must be an HTTPS repository path")
        repository_base = repository_base.rstrip("/") + "/"
    references = {}
    for path in sorted((root / "references").glob("*.json")):
        records = json.loads(path.read_text(encoding="utf-8"))
        for record in records:
            if record["id"] in references:
                raise ValueError("Duplicate bibliographic identifier")
            references[record["id"]] = record
    admissions = _admissions(root)
    entries, navigation = {}, []
    for directory in ("10_markdown", "20_distillates", "30_assertions", "40_output"):
        for file in sorted((root / directory).rglob("*.md")):
            path = file.relative_to(root).as_posix()
            meta, body = read_document(root, path)
            kind = meta.get("type")
            if kind not in LAYERS:
                if kind == "moc":
                    navigation.append({"path": path, "title": _title(meta, body, path), "kind": "Topic map"})
                continue
            if meta.get("metadata", {}).get("confidential"):
                raise ValueError(f"Confidential representation cannot be published: {path}")
            status = meta.get("status")
            checked = meta.get("checked", {})
            if status == "verified" and not checked.get("verification"):
                raise ValueError(f"Verified status has no human verification date: {path}")
            blocks = anchored_blocks(body, kind) if kind in ("representation", "distillate") else {}
            excerpt = section(body, "Statement") if kind == "assertion" else ("" if kind == "representation" else _excerpt(body))
            if kind == "assertion" and not excerpt:
                raise ValueError(f"Assertion has no Statement: {path}")
            entries[path] = {"path": path, "id": doc_id(path), "title": _title(meta, body, path), "kind": kind,
                             "status": status, "checked": checked, "metadata": meta, "blocks": blocks,
                             "excerpt": excerpt, "edges": [], "backlinks": [], "source": {}, "body": body}
    if len({e["id"] for e in entries.values()}) != len(entries):
        raise ValueError("Public document ID collision")

    def edge(entry: dict, value: str, expected: str, from_anchor: str = "") -> None:
        path, anchor = target(value)
        destination = entries.get(path)
        if not destination or destination["kind"] != expected:
            raise ValueError(f"Missing or wrong-layer grounding target: {value}")
        if expected in ("distillate", "representation") and not anchor:
            raise ValueError(f"Grounding requires an exact block: {value}")
        if anchor and anchor not in destination["blocks"]:
            raise ValueError(f"Missing grounding anchor: {value}")
        link = {"path": path, "anchor": anchor, "from_anchor": from_anchor,
                "href": "#" + (block_id(path, anchor) if anchor else destination["id"]), "title": destination["title"]}
        if link not in entry["edges"]:
            entry["edges"].append(link)
            destination["backlinks"].append({"path": entry["path"], "anchor": from_anchor,
                                            "target_anchor": anchor, "title": entry["title"],
                                            "href": "#" + (block_id(entry["path"], from_anchor) if from_anchor else entry["id"])})

    for path, entry in entries.items():
        meta, kind = entry["metadata"], entry["kind"]
        if kind == "chapter":
            for value in meta.get("assertions", []):
                edge(entry, value, "assertion")
            # The chapter mirror must not conceal a broken actual footnote target.
            cited = set()
            for definition in re.findall(r"^\[\^[^\]]+\]:.*?(?=^\[\^[^\]]+\]:|\Z)", entry["body"], re.M | re.S):
                for value in WIKI.finditer(definition):
                    if value.group(1).startswith("30_assertions/"):
                        cited.add(target(value.group(0))[0])
            if cited != {e["path"] for e in entry["edges"]}:
                raise ValueError(f"Chapter assertion mirror differs from footnotes: {path}")
        elif kind == "assertion":
            if not meta.get("grounding"):
                raise ValueError(f"Ungrounded assertion: {path}")
            for value in meta["grounding"]:
                edge(entry, value, "distillate")
        elif kind == "distillate":
            if not entry["blocks"]:
                raise ValueError(f"Distillate has no core statement blocks: {path}")
            if meta.get("source-type") == "publication":
                record = references.get(meta.get("reference"))
                if not record or not record.get("URL"):
                    raise ValueError(f"Missing publication citation: {path}")
                safe_url(record["URL"])
                if not meta.get("checked", {}).get("quote"):
                    raise ValueError(f"Publication quotation has no intake check: {path}")
                for block in entry["blocks"].values():
                    if not re.search(r"^\s*> ", block, re.M):
                        raise ValueError(f"Missing quotation for publication statement: {path}")
                entry["source"] = {"citation": record, **admissions.get(path, {})}
            else:
                rep_path, rep_anchor = target(meta.get("representation", ""))
                if rep_anchor or rep_path not in entries or entries[rep_path]["kind"] != "representation":
                    raise ValueError(f"Missing source representation: {path}")
                if meta.get("source-type") != "document":
                    raise ValueError(f"Data computation display requires an explicit supported renderer: {path}")
                for anchor, block in entry["blocks"].items():
                    links = list(WIKI.finditer(block))
                    if len(links) != 1 or target(links[0].group(0))[0] != rep_path:
                        raise ValueError(f"Statement must target its own source exactly once: {path}#{anchor}")
                    edge(entry, links[0].group(0), "representation", anchor)
        elif kind == "representation":
            source = {**meta.get("metadata", {}), **admissions.get(path, {})}
            if source.get("identifier"):
                safe_url(source["identifier"])
            original = meta.get("source")
            if original:
                match = WIKI.fullmatch(original)
                if not match or not match.group(1).startswith("00_sources/"):
                    raise ValueError(f"Invalid local original reference: {path}")
                source["local_original"] = match.group(1)
            if not source.get("version"):
                commit = re.search(r"/(?:blob|raw)/([0-9a-f]{40})/", source.get("identifier", ""))
                if commit:
                    source["version"] = commit.group(1)
            entry["source"] = source
    for directory, label in (("knowledge", "Project contract"), ("glossary", "Glossary")):
        for file in sorted((root / directory).glob("*.md"), key=lambda p: (p.name.casefold(), p.name)):
            path = file.relative_to(root).as_posix()
            meta, body = read_document(root, path)
            navigation.append({"path": path, "title": _title(meta, body, path), "kind": label})
    ordered = sorted(entries.values(), key=lambda e: (list(LAYERS).index(e["kind"]), e["title"].casefold(), e["path"]))
    for entry in ordered:
        entry.pop("body")
    return {"date": date, "base": repository_base, "entries": ordered, "navigation": navigation,
            "counts": {kind: sum(e["kind"] == kind for e in ordered) for kind in LAYERS}}
