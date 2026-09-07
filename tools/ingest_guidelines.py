"""Admit the finite English P5 release baseline and derive its coverage view.

Run ``python -m tools.ingest_guidelines`` to import, or ``--check`` to reconcile
the immutable admission and current coverage without the ignored Git mirror.
The boundary and evidence limits live in knowledge/data.md and operations.md.
Use ``--refresh-coverage`` to update processing projections from tracked
admissions after distillation changes, also without ignored originals.
The existing stdlib XML converter is retained; external entities, includes,
schemas and example instructions are never executed.
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import xml.etree.ElementTree as ET
from collections import Counter
from collections.abc import Iterator
from dataclasses import replace
from io import BytesIO
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

import yaml

from tools import ingest_git_blobs as ingest
from tools.ingest_text_identity import PILOT
from tools.sitegen.documents import read_document
from tools.tei.build_atlas import NoDTDTreeBuilder, git

TEI = "{http://www.tei-c.org/ns/1.0}"
XI = "{http://www.w3.org/2001/XInclude}"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"
MASTER = "P5/Source/guidelines-en.xml"
DATE = "2026-09-07"
MANIFEST = f"sources/manifests/{DATE}-guidelines-4.12.0-admission.yaml"
COVERAGE = "corpus/projections/guidelines-4.12.0.json"
OVERVIEW = "corpus/projections/guidelines-4.12.0.md"
MEMBERS_MANIFEST = "sources/manifests/2026-09-04-tei-p5-4.12.0-release-members.yaml"
MEMBERS = "corpus/normalized/assets/tei-p5-4.12.0-release-members.json"
CONTAINERS = frozenset({
    "TEI", "teiHeader", "fileDesc", "encodingDesc", "text", "front", "body", "back",
    "div", "elementSpec", "classSpec", "macroSpec", "dataSpec", "attList", "attDef",
    "listBibl", "anthology",
})


def reference_blocks(payload: bytes) -> list[tuple[str, str]]:
    blocks = ingest.source_blocks(payload, CONTAINERS)
    if not blocks:
        blocks = [("/", "```xml\n" + payload.decode("utf-8") + "\n```\n")]
    return blocks


ingest.FORMS["guidelines-reference"] = replace(
    ingest.CHAPTER,
    converter="complete XML plus verbatim blocks of prose, specifications and support files",
    explanation=(
        "The complete XML is preserved as inert text. The source blocks repeat exact XML\n"
        "units in document order, including examples, lists, tables and constraints. The\n"
        "locator identifies each unit inside this file; the complete XML preserves its\n"
        "surrounding structure. Includes and processing instructions remain unexecuted.\n"
        "The Guidelines coverage projection locates their separate source dependencies.\n"
        "Presence of a representation establishes neither distillation nor verification.\n"
    ),
    authority="P5 4.12.0 source; normative force depends on prose, declaration, example or publication role",
    blocks=reference_blocks,
)
RUN = ingest.Run(
    run_id=f"{DATE}-guidelines-4.12.0-admission", date=DATE,
    adapter="tools.ingest_guidelines", version=1, manifest=MANIFEST,
    boundary=(
        "English master, every XML file under P5/Source/Guidelines/en, every immediate "
        "P5/Source/Specs/*.xml file, and their transitive local XML XIncludes outside examples"
    ),
    status_applies_to="the enumerated source blobs and immutable representations only",
    known_limits=(
        "No distillation, assertion review, human verification or domain completeness follows from admission.",
        "Published HTML and generated schemas are separate manifestations; render equivalence is untested.",
        "Non-XML assets and external links are inventoried dependencies, not admitted documentary evidence.",
        "Translated text in shared specifications is preserved; translated Guidelines editions are outside the boundary.",
        "Bibliographic entries do not admit the full text of the publications they describe.",
    ), admissions=(),
)


def parse_xml(payload: bytes) -> ET.Element:
    return ET.fromstring(payload, parser=ET.XMLParser(target=NoDTDTreeBuilder()))


def live_nodes(node: ET.Element) -> Iterator[ET.Element]:
    """Exclude example markup from the dependency graph, preserving it in the source."""
    if node.tag.rsplit("}", 1)[-1] == "egXML":
        return
    yield node
    for child in node:
        yield from live_nodes(child)


def baseline_paths(inventory: dict[str, str]) -> list[str]:
    return sorted(path for path in inventory if path == MASTER or (
        path.endswith(".xml") and (
            path.startswith("P5/Source/Guidelines/en/")
            or PurePosixPath(path).parent.as_posix() == "P5/Source/Specs"
        )
    ))


def local_target(source: str, href: str) -> str | None:
    url = urlsplit(href)
    if url.scheme or url.netloc or url.path.startswith("/"):
        return None
    if not url.path:
        return source
    path = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(url.path)))
    if path.startswith("../") or "\\" in path:
        raise ValueError(f"dependency escapes the source tree: {source}: {href}")
    return path


def includes(source: str, payload: bytes) -> list[dict]:
    nodes = list(live_nodes(parse_xml(payload)))
    if any("{http://www.w3.org/XML/1998/namespace}base" in node.attrib for node in nodes):
        raise ValueError(f"xml:base requires an explicit dependency resolver: {source}")
    return [{"source": source, "href": node.get("href", ""),
             "target": local_target(source, node.get("href", "")),
             "parse": node.get("parse", "xml"), "xpointer": node.get("xpointer")}
            for node in nodes if node.tag == XI + "include"]


def fetch_blobs(root: Path, inventory: dict[str, str], paths: list[str]) -> dict[str, bytes]:
    stream = BytesIO(git(root / ingest.GIT_DIR, "cat-file", "--batch",
                         payload="".join(inventory[path] + "\n" for path in paths).encode("ascii")))
    result = {}
    for path in paths:
        header = stream.readline().decode("ascii").split()
        if len(header) != 3 or header[:2] != [inventory[path], "blob"]:
            raise ValueError(f"missing or mismatched Git blob: {path}")
        payload = stream.read(int(header[2]))
        if stream.read(1) != b"\n" or ingest.blob_id(payload) != inventory[path]:
            raise ValueError(f"Git payload mismatch: {path}")
        result[path] = payload
    if stream.read():
        raise ValueError("unexpected trailing Git batch output")
    return result


def existing_admissions() -> dict[str, tuple[ingest.Run, ingest.Admission]]:
    return {entry.git_path: (run, entry) for run in (PILOT, *ingest.RUNS.values())
            for entry in run.admissions}


def admission(path: str, payload: bytes, blob: str) -> ingest.Admission:
    root = parse_xml(payload)
    heading = root.get("ident") or " ".join(root.findtext(TEI + "head", "").split())
    heading = heading or ("The TEI Guidelines" if path == MASTER else PurePosixPath(path).stem)
    stem = PurePosixPath(path).stem.lower()
    prefix = "tei-p5-" if "/Specs/" in path else "tei-p5-guidelines-"
    slug = prefix + re.sub(r"[^a-z0-9.-]+", "-", stem) + "-4.12.0"
    return ingest.Admission(path, blob, len(payload), slug, heading,
                            f"TEI P5 4.12.0 {heading}", "guidelines-reference")


def load_payloads(root: Path, inventory: dict[str, str], check: bool) -> dict[str, bytes]:
    if check:
        manifest = yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8"))
        result = {}
        for row in [*manifest["admissions"], *manifest.get("reused_admissions", [])]:
            path = row["git_path"]
            stub = ingest.Admission(path, row["git_blob_id"], row["original_bytes"],
                                    Path(row["representation_path"]).stem, "", "", "guidelines-reference")
            result[path] = ingest.embedded_source(stub, (root / row["representation_path"]).read_bytes())
        return result
    result = fetch_blobs(root, inventory, baseline_paths(inventory))
    while True:
        needed = set()
        for path, payload in result.items():
            for dep in includes(path, payload):
                target = dep["target"]
                if target is not None and dep["parse"] == "xml":
                    if target not in inventory:
                        raise ValueError(f"missing local XML include: {dep}")
                    if target not in result:
                        needed.add(target)
        if not needed:
            return result
        result.update(fetch_blobs(root, inventory, sorted(needed)))


def toc(payloads: dict[str, bytes]) -> list[dict]:
    master = parse_xml(payloads[MASTER])
    rows = [{"part": "front", "number": "", "title": "Title", "source": MASTER,
             "published_page": "TitlePageRecto.html"}]
    for part in ("front", "body", "back"):
        section = master.find(f"{TEI}text/{TEI}{part}")
        if section is None:
            raise ValueError(f"missing master section: {part}")
        for index, node in enumerate(section.findall(XI + "include"), 1):
            path = local_target(MASTER, node.attrib["href"])
            source = parse_xml(payloads[path])
            heading = " ".join(source.findtext(TEI + "head", "").split())
            ident = source.get(XML_ID, "")
            page = {"Dedication.xml": "dedication", "REF-ATTRIBUTES.xml": "REF-ATTS"}.get(
                PurePosixPath(path).name, ident or PurePosixPath(path).stem)
            rows.append({"part": part, "number": str(index), "title": heading,
                         "source": path, "published_page": page + ".html"})
    if Counter(row["part"] for row in rows) != {"front": 7, "body": 24, "back": 9}:
        raise ValueError("English release contents do not reconcile to 7 front, 24 body and 9 back entries")
    return rows


def dependencies(payloads: dict[str, bytes], inventory: dict[str, str]) -> list[dict]:
    result = []
    for path, payload in sorted(payloads.items()):
        for dep in includes(path, payload):
            target = dep["target"]
            dep["disposition"] = ("admitted-xml" if target in payloads and dep["parse"] == "xml"
                                  else "git-asset" if target in inventory else "external")
            result.append({"kind": "xinclude", **dep})
        for node in live_nodes(parse_xml(payload)):
            if node.tag == TEI + "graphic" and node.get("url"):
                href = node.attrib["url"]
                target = local_target(path, href)
                result.append({"kind": "graphic", "source": path, "href": href,
                               "target": target, "git_blob_id": inventory.get(target),
                               "disposition": "git-asset" if target in inventory else "unresolved-or-external"})
    return result


def source_sections(payload: bytes, form: ingest.Form) -> list[dict]:
    rows = []
    anchors = {locator: f"{form.id_prefix}{index}" for index, (locator, _) in enumerate(form.blocks(payload), 1)}

    def walk(node: ET.Element, locator: str) -> None:
        if node.tag.rsplit("}", 1)[-1] == "egXML":
            return
        if node.tag == TEI + "div":
            heading = " ".join(node.findtext(TEI + "head", "").split())
            if heading:
                rows.append({"xml_id": node.get(XML_ID), "heading": heading,
                             "xml_location": locator,
                             "heading_block": anchors.get(locator + "/head[1]")})
        counts: Counter = Counter()
        for child in node:
            tag = child.tag.rsplit("}", 1)[-1]
            counts[tag] += 1
            walk(child, f"{locator}/{tag}[{counts[tag]}]")

    root = parse_xml(payload)
    walk(root, "/" + root.tag.rsplit("}", 1)[-1] + "[1]")
    return rows


def published_members(root: Path, contents: list[dict], sources: list[dict]) -> dict:
    manifest = yaml.safe_load((root / MEMBERS_MANIFEST).read_text(encoding="utf-8"))
    obj = next(item for item in manifest["objects"] if item["path"] == MEMBERS)
    payload = (root / MEMBERS).read_bytes()
    if ingest.sha256(payload) != obj["sha256"]:
        raise ValueError("release ZIP member inventory checksum mismatch")
    inventory = json.loads(payload)
    lock = yaml.safe_load((root / ingest.LOCK).read_text(encoding="utf-8"))
    if inventory["archive_sha256"] != lock["hashes"]["official_release_zip_sha256"]:
        raise ValueError("published member inventory belongs to a different release ZIP")
    names = {entry["path"] for entry in inventory["entries"] if not entry["directory"]}
    for row in contents:
        member = "doc/tei-p5-doc/en/html/" + row["published_page"]
        if member not in names:
            raise ValueError(f"published contents page absent from release ZIP inventory: {member}")
        row["release_member"] = member
    by_source = {row["source"]: row["release_member"] for row in contents}
    unmatched = []
    for row in sources:
        candidate = by_source.get(row["source"])
        if "/Specs/" in row["source"]:
            candidate = "doc/tei-p5-doc/en/html/ref-" + PurePosixPath(row["source"]).stem + ".html"
        row["release_member"] = candidate if candidate in names else None
        if candidate and candidate not in names:
            unmatched.append({"source": row["source"], "expected_member": candidate})
    return {"manifest": MEMBERS_MANIFEST, "inventory": MEMBERS, "sha256": obj["sha256"],
            "contents_pages_matched": len(contents), "unmatched_specifications": unmatched,
            "scope": "Filename membership in the recorded release ZIP inventory only; no HTML/source semantic equivalence or current raw ZIP availability is claimed."}


def build(root: Path, check: bool = False) -> dict:
    inventory = ingest.pinned_inventory(root)
    payloads = load_payloads(root, inventory, check)
    required = set(baseline_paths(inventory))
    for path, payload in payloads.items():
        required.update(dep["target"] for dep in includes(path, payload)
                        if dep["target"] is not None and dep["parse"] == "xml")
    if set(payloads) != required:
        raise ValueError("admission does not exhaust the declared inventory and XML include boundary")
    old = existing_admissions()
    entries, objects, rows = [], [], []
    slugs = set()
    for path, payload in sorted(payloads.items()):
        run, item = old.get(path, (RUN, admission(path, payload, inventory[path])))
        if item.slug in slugs:
            raise ValueError(f"duplicate representation slug: {item.slug}")
        slugs.add(item.slug)
        if item.blob != inventory[path]:
            raise ValueError(f"admission differs from pinned inventory: {path}")
        output = ingest.representation(run, item, payload)
        original = root / item.original
        if original.exists() or not check:
            ingest.immutable_output(original, payload, check)
        ingest.immutable_output(root / item.rendered, output, check)
        entries.append({"source_type": "document", "git_path": path, "commit": ingest.COMMIT,
                        "original_path": item.original, "original_bytes": len(payload),
                        "original_sha256": ingest.sha256(payload), "git_blob_id": item.blob,
                        "representation_path": item.rendered, "representation_sha256": ingest.sha256(output),
                        "reused_admission": run.manifest if path in old else None,
                        "source_blocks": len(ingest.FORMS[item.form].blocks(payload)),
                        "content_authority": ingest.FORMS[item.form].authority, "instruction_trust": "none"})
        objects.append({"kind": "markdown-representation", "path": item.rendered, "sha256": ingest.sha256(output)})
        distillate = f"20_distillates/documents/{item.slug}.md"
        meta = read_document(root, distillate)[0] if (root / distillate).exists() else {}
        if meta and (meta.get("type") != "distillate" or meta.get("source-type") != "document"
                     or meta.get("representation") != f"[[{item.rendered.removesuffix('.md')}]]"):
            raise ValueError(f"distillate does not describe its corresponding source: {distillate}")
        rows.append({"source": path, "title": item.heading, "representation": item.rendered,
                     "distillate": distillate if meta else None, "distillate_status": meta.get("status"),
                     "processing": "distilled" if meta else "ingested",
                     "sections": source_sections(payload, ingest.FORMS[item.form]),
                     "section_review": "not-recorded", "instruction_trust": "none"})
    dep_rows = dependencies(payloads, inventory)
    manifest_path = root / MANIFEST
    prior = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    now = ingest._now()
    manifest = {
        "schema_version": 1, "run_id": RUN.run_id, "source_id": ingest.SOURCE_ID,
        "started_at": prior.get("started_at", now), "finished_at": prior.get("finished_at", now),
        "status": "bounded-complete", "adapter": {"name": RUN.adapter, "version": RUN.version},
        "scope": {"boundary": RUN.boundary, "status_applies_to": RUN.status_applies_to},
        "lock_file": ingest.LOCK, "upstream_inventory_sha256": ingest.INVENTORY_HASH,
        "counts": {"sources": len(entries), "reused": sum(e["reused_admission"] is not None for e in entries),
                   "original_bytes": sum(e["original_bytes"] for e in entries)},
        "objects": objects,
        "admissions": [entry for entry in entries if entry["reused_admission"] is None],
        "reused_admissions": [entry for entry in entries if entry["reused_admission"] is not None],
        "dependencies": dep_rows,
        "gaps": [], "known_limits": list(RUN.known_limits), "instruction_trust": "none",
        "rights": {"selected_license": "CC-BY-3.0", "attribution": "TEI Consortium; original paths and commit retained",
                   "license_records": ingest.LICENSES,
                   "note": "The master retains a historical GPL comment and explicit CC-BY-3.0/BSD-2 availability. "
                           "The pinned repository license and explicit availability supply this admission's license; "
                           "embedded third-party examples retain their attribution. Assets are not republished by this import."},
    }
    ingest.immutable_output(manifest_path, yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True).encode(), check)
    contents = toc(payloads)
    by_path = {row["source"]: row for row in rows}
    contents = [{**row, **{k: by_path[row["source"]][k] for k in
                          ("representation", "distillate", "processing", "distillate_status")}}
                for row in contents]
    publication = published_members(root, contents, rows)
    return {"schema_version": 1, "kind": "navigation-projection", "release": "4.12.0",
            "commit": ingest.COMMIT, "admission_manifest": MANIFEST, "boundary": RUN.boundary,
            "counts": {"sources": len(rows), "ingested": len(rows),
                       "distilled": sum(row["distillate"] is not None for row in rows),
                       "main_chapters": 24, "specifications": sum("/Specs/" in row["source"] for row in rows)},
            "limits": list(RUN.known_limits), "contents": contents, "sources": rows,
            "dependencies": dep_rows, "publication_inventory": publication}


def markdown(view: dict) -> str:
    lines = ["# TEI P5 4.12.0 Guidelines coverage", "",
             "Generated navigation only. Ground claims through the linked representations and distillates.", "",
             f"Release commit: `{view['commit']}`. [Admission manifest](../../{MANIFEST}).", "",
             f"{view['counts']['ingested']} source representations; {view['counts']['distilled']} sources with a distillate.", "",
             "A distillate's presence does not establish exhaustive section review. No section-level review has been recorded by this import.", "",
             "## Published contents", "",
             "| Part | Entry | Source representation | Processing | Distillate |",
             "|---|---|---|---|---|"]
    for row in view["contents"]:
        title = row["title"].replace("|", "\\|")
        doc = f"[Source](../../{row['representation']})"
        dist = f"[{' / '.join(filter(None, [row['processing'], row['distillate_status']]))}](../../{row['distillate']})" if row["distillate"] else "—"
        public = "https://tei-c.org/Vault/P5/4.12.0/doc/tei-p5-doc/en/html/" + row["published_page"]
        lines.append(f"| {row['part']} {row['number']} | [{title}]({public}) | {doc} | {row['processing']} | {dist} |")
    lines += ["", "## Every admitted source", "", "| Source | Representation | Processing |", "|---|---|---|"]
    for row in view["sources"]:
        lines.append(f"| `{row['source']}` | [Read](../../{row['representation']}) | {row['processing']} |")
    lines += ["", "## Dependencies and limits", "",
              f"[Machine-readable coverage](guidelines-4.12.0.json) records {len(view['dependencies'])} include and graphic dependencies, source sections and unresolved asset references.", ""]
    lines += ["All 40 contents pages match filenames in the recorded release ZIP inventory. This does not test rendering or semantic equivalence.", ""]
    for row in view["publication_inventory"]["unmatched_specifications"]:
        lines.append(f"- `{row['source']}` is admitted from Git; its expected HTML member `{row['expected_member']}` is absent from that inventory.")
    lines.append("")
    lines += [f"- {limit}" for limit in view["limits"]]
    return "\n".join(lines) + "\n"


def projection_output(path: Path, text: str, check: bool) -> None:
    payload = text.encode("utf-8")
    if check:
        if not path.exists() or path.read_bytes() != payload:
            raise ValueError(f"missing or stale coverage projection: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_bytes(payload)
        temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path())
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--refresh-coverage", action="store_true",
                      help="reconcile tracked admissions and update only the processing projections")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        view = build(root, args.check or args.refresh_coverage)
        projection_output(root / COVERAGE, json.dumps(view, ensure_ascii=False, indent=2) + "\n", args.check)
        projection_output(root / OVERVIEW, markdown(view), args.check)
    except (OSError, ValueError, KeyError, ET.ParseError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print("OK: Guidelines reference admission and coverage reconcile: " + json.dumps(view["counts"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
