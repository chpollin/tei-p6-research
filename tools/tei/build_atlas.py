"""Build deterministic navigation over pinned P5/Source/Specs/*.xml declarations.

This is a declaration inventory, not an ODD processor or an effective model.
Run from the repository root with ``py -3 -m tools.tei.build_atlas --output PATH``.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha1, sha256
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import xml.etree.ElementTree as ET

import yaml

from tools.corpus.git_snapshot import parse_tree

TEI = "http://www.tei-c.org/ns/1.0"
RNG = "http://relaxng.org/ns/structure/1.0"
SCH = "http://purl.oclc.org/dsdl/schematron"
NS = {"tei": TEI}
CATEGORIES = {"elementSpec", "classSpec", "macroSpec", "dataSpec"}
REFS = {
    f"{{{TEI}}}memberOf": ("key", "classSpec"),
    f"{{{TEI}}}elementRef": ("key", "elementSpec"),
    f"{{{TEI}}}classRef": ("key", "classSpec"),
    f"{{{TEI}}}macroRef": ("key", "macroSpec"),
    f"{{{TEI}}}dataRef": ("key", "dataSpec"),
    f"{{{TEI}}}attRef": ("class", "classSpec"),
    f"{{{RNG}}}ref": ("name", None),
}
EXCLUDED = [
    "Files outside the immediate P5/Source/Specs/*.xml boundary, including moduleSpec declarations.",
    "Inherited attributes, transitive class membership, effective content models and ODD customization/compilation.",
    "Examples, prose, translations, processing models and documentation cross-references.",
    "Constraint execution, XPath namespace resolution, semantic equivalence and compatibility judgments.",
    "Published HTML/schema reconciliation and release-family completeness.",
]


class NoDTDTreeBuilder(ET.TreeBuilder):
    def doctype(self, name: str, pubid: str | None, system: str | None) -> None:
        raise ValueError("DTD/entity declarations excluded")


def git(git_dir: Path, *args: str, payload: bytes | None = None) -> bytes:
    # Disable replacement objects: locators must designate the actual pinned objects.
    return subprocess.run(
        ["git", "--no-replace-objects", "--git-dir", str(git_dir), *args],
        input=payload, capture_output=True, check=True,
    ).stdout


def qname(tag: str) -> str:
    return tag.removeprefix(f"{{{TEI}}}")


def tree(node: ET.Element) -> dict:
    """A namespace-preserving lexical tree, without inferred semantics."""
    result = {"name": node.tag, "attributes": dict(sorted(node.attrib.items()))}
    if node.text and node.text.strip():
        result["text"] = node.text.strip()
    children = [tree(child) for child in node]
    if children:
        result["children"] = children
    return result


def positions(root: ET.Element) -> dict[ET.Element, str]:
    result: dict[ET.Element, str] = {}

    def visit(node: ET.Element, path: str) -> None:
        result[node] = path
        counts: Counter = Counter()
        for child in node:
            counts[child.tag] += 1
            visit(child, f"{path}/{child.tag}[{counts[child.tag]}]")

    visit(root, f"/{root.tag}[1]")
    return result


def parse_spec(payload: bytes, path: str, blob: str, commit: str) -> dict:
    # No DTD/entity evaluation or external document loading is part of navigation.
    root = ET.fromstring(payload, parser=ET.XMLParser(target=NoDTDTreeBuilder()))
    category = qname(root.tag)
    if category not in CATEGORIES or root.tag != f"{{{TEI}}}{category}":
        raise ValueError(f"unsupported specification root: {path}: {root.tag}")
    ident = root.get("ident")
    if not ident:
        raise ValueError(f"missing specification identity: {path}")
    locators = positions(root)
    local_atts = []
    structural = list(root.findall("tei:content", NS))
    structural += list(root.findall("tei:classes", NS))
    structural += list(root.findall("tei:attList", NS))
    constraints = list(root.findall("tei:constraintSpec", NS))
    for att_list in root.findall("tei:attList", NS):
        # Only nested attList containers are traversed, never examples/descriptions.
        pending = list(att_list)
        while pending:
            att = pending.pop(0)
            if att.tag == f"{{{TEI}}}attList":
                pending[0:0] = list(att)
            elif att.tag == f"{{{TEI}}}attDef":
                if not att.get("ident") or any(a["ident"] == att.get("ident") for a in local_atts):
                    raise ValueError(f"missing/duplicate local attribute identity: {path}")
                local_atts.append({
                    "ident": att.get("ident"), "attributes": dict(sorted(att.attrib.items())),
                    "locator": locators[att],
                    "datatype": [tree(n) for n in att.findall("tei:datatype", NS)],
                    "default_values": ["".join(n.itertext()).strip() for n in att.findall("tei:defaultVal", NS)],
                    "value_lists": [{"attributes": dict(sorted(n.attrib.items())),
                                     "items": [dict(sorted(v.attrib.items())) for v in n.findall("tei:valItem", NS)]}
                                    for n in att.findall("tei:valList", NS)],
                })
                constraints.extend(att.findall("tei:constraintSpec", NS))
    references = []
    # Avoid prose/example references anywhere below selected attList containers.
    skipped = {f"{{{TEI}}}{n}" for n in ("desc", "gloss", "remarks", "exemplum", "listRef")}

    def scan(node: ET.Element) -> None:
        if node.tag in skipped:
            return
        if node.tag in REFS:
            attribute, target_kind = REFS[node.tag]
            references.append({"name": node.tag, "attributes": dict(sorted(node.attrib.items())),
                               "target": node.get(attribute), "expected_category": target_kind,
                               "locator": locators[node]})
        for child in node:
            scan(child)

    for node in structural:
        scan(node)
    return {
        "ident": ident, "category": category, "attributes": dict(sorted(root.attrib.items())),
        "module_declared": root.get("module"),
        "classes_declared": [dict(sorted(n.attrib.items())) for n in root.findall("tei:classes/tei:memberOf", NS)],
        "source": {"commit": commit, "path": path, "blob": blob,
                   "sha256": sha256(payload).hexdigest(), "bytes": len(payload), "locator": locators[root]},
        "local_attributes": local_atts,
        "content_declared": [tree(n) for n in root.findall("tei:content", NS)],
        "constraints_declared": [{"attributes": dict(sorted(n.attrib.items())), "locator": locators[n],
                                  "nodes": [{"name": c.tag, "attributes": dict(sorted(c.attrib.items())),
                                             "locator": locators[c]} for c in n.iter()
                                            if c.tag.startswith(f"{{{SCH}}}")]}
                                 for n in constraints],
        "references": references,
    }


def build_atlas(root: Path, git_dir: Path, lock_path: str = "sources/locks/tei-p5-4.12.0.yaml",
                expected_version: str = "4.12.0") -> dict:
    if not (git_dir / "HEAD").is_file():
        raise ValueError(f"local Git mirror absent: {git_dir}")
    lock_bytes = (root / lock_path).read_bytes()
    lock = yaml.safe_load(lock_bytes)
    release = lock["release"]
    commit = release["resolved_full_commit_sha"]
    if release["version"] != expected_version or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("source version/full commit mismatch")
    if commit != lock["hashes"]["git_commit"]:
        raise ValueError("source commit mismatch in lock")
    manifests = [(p, yaml.safe_load((root / p).read_bytes())) for p in lock["manifests"]]
    candidates = [(p, m, obj) for p, m in manifests for obj in m.get("objects", [])
                  if obj.get("kind") == "git-tree-inventory"]
    if len(candidates) != 1:
        raise ValueError("expected exactly one Git inventory manifest")
    manifest_path, manifest, inventory_object = candidates[0]
    if (manifest.get("status") != "observable-complete" or not manifest.get("finished_at")
            or manifest.get("gaps") or manifest["source_id"] != lock["source_id"]):
        raise ValueError("Git manifest is incomplete or source identity differs")
    if not any(r.get("resolved_commit") == commit for r in manifest.get("requests", [])):
        raise ValueError("manifest commit mismatch")
    inventory_bytes = (root / inventory_object["path"]).read_bytes()
    if sha256(inventory_bytes).hexdigest() != inventory_object["sha256"]:
        raise ValueError("inventory hash mismatch")
    inventory = json.loads(inventory_bytes)
    actual_commit = git(git_dir, "rev-parse", f"{commit}^{{commit}}").decode().strip()
    actual_tree = git(git_dir, "rev-parse", f"{commit}^{{tree}}").decode().strip()
    if (actual_commit != commit or inventory["resolved_commit"] != commit
            or inventory["source_id"] != lock["source_id"]
            or inventory["repository"] != lock["origins"]["git_repository"]
            or any(actual_tree != t for t in (inventory["root_tree"], inventory_object["root_tree"],
                                               lock["hashes"]["git_root_tree"]))):
        raise ValueError("source commit/tree/origin mismatch")
    entries = parse_tree(git(git_dir, "ls-tree", "-r", "-z", "--full-tree", commit).decode("utf-8"))
    if entries != sorted(inventory["entries"], key=lambda e: e["path"]):
        raise ValueError("inventory path/blob mismatch with pinned Git tree")
    selected = [e for e in entries if PurePosixPath(e["path"]).parent.as_posix() == "P5/Source/Specs"
                and e["path"].endswith(".xml")]
    if not selected or any(e["object_type"] != "blob" or e["mode"] not in {"100644", "100755"} for e in selected):
        raise ValueError("expected nonempty regular specification blobs")
    stream = BytesIO(git(git_dir, "cat-file", "--batch",
                         payload="".join(e["object_id"] + "\n" for e in selected).encode("ascii")))
    records = []
    identities = set()
    for entry in selected:
        header = stream.readline().decode("ascii").split()
        if len(header) != 3 or header[:2] != [entry["object_id"], "blob"]:
            raise ValueError("Git batch blob mismatch")
        payload = stream.read(int(header[2]))
        blob_hash = sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()
        if stream.read(1) != b"\n" or blob_hash != entry["object_id"]:
            raise ValueError("source blob payload mismatch")
        record = parse_spec(payload, entry["path"], entry["object_id"], commit)
        if record["ident"] in identities:
            raise ValueError(f"duplicate specification identity: {record['ident']}")
        identities.add(record["ident"])
        records.append(record)
    by_ident = {r["ident"]: r for r in records}
    unresolved = []
    for record in records:
        for ref in record["references"]:
            target = by_ident.get(ref["target"])
            ref["resolution"] = ("declaration-present" if target and
                                  ref["expected_category"] == target["category"] else "unresolved")
            if ref["resolution"] == "unresolved":
                ref["reason"] = ("no-declaration-key; named/external datatype is not resolved"
                                 if ref["target"] is None else
                                 "RNG pattern expansion is excluded" if ref["expected_category"] is None else
                                 "declaration category mismatch" if target else "declaration absent in boundary")
                unresolved.append({"ident": record["ident"], **ref})
    registry = yaml.safe_load((root / "sources/registry.yaml").read_bytes())
    source = next(s for s in registry["sources"] if s["source_id"] == lock["source_id"])
    if not source.get("rights") or not source.get("authority"):
        raise ValueError("source rights and authority required")
    return {
        "schema_version": 1, "artifact": "p5-spec-navigation", "use": "navigation-only; never grounding",
        "generated": True, "generator": {"name": "tools.tei.build_atlas", "version": 1},
        "instruction_trust": "none",
        "source": {"source_id": lock["source_id"], "version": expected_version, "commit": commit,
                   "root_tree": actual_tree, "repository": inventory["repository"],
                   "lock": lock_path, "lock_sha256": sha256(lock_bytes).hexdigest(),
                   "manifest": manifest_path, "finished_at": manifest["finished_at"],
                   "manifest_sha256": sha256((root / manifest_path).read_bytes()).hexdigest(),
                   "registry": "sources/registry.yaml",
                   "registry_sha256": sha256((root / "sources/registry.yaml").read_bytes()).hexdigest(),
                   "inventory": inventory_object["path"], "inventory_sha256": inventory_object["sha256"],
                   "authority": source["authority"], "rights": source["rights"]},
        "scope": {"included": "Immediate P5/Source/Specs/*.xml root declarations at the pinned commit",
                  "locator_syntax": "Expanded-QName child paths with one-based same-name sibling positions",
                  "reference_resolution": "Exact declared identity/category lookup only; no expansion or validity claim",
                  "excluded": EXCLUDED},
        "statistics": {"files": len(selected), "input_bytes": sum(r["source"]["bytes"] for r in records),
                       "categories": dict(sorted(Counter(r["category"] for r in records).items())),
                       "declared_modules": dict(sorted(Counter(r["module_declared"] for r in records if r["module_declared"]).items())),
                       "local_attributes": sum(len(r["local_attributes"]) for r in records),
                       "constraints": sum(len(r["constraints_declared"]) for r in records),
                       "references": sum(len(r["references"]) for r in records),
                       "unresolved_references": len(unresolved)},
        "records": records, "unresolved_references": unresolved,
    }


def encoded(atlas: dict) -> bytes:
    return (json.dumps(atlas, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--git-dir", type=Path, default=Path("corpus/raw/git/TEIC-TEI.git"))
    parser.add_argument("--lock", default="sources/locks/tei-p5-4.12.0.yaml")
    parser.add_argument("--expected-version", default="4.12.0")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--check", action="store_true", help="Compare existing output bytes without writing")
    args = parser.parse_args()
    try:
        atlas = build_atlas(args.root, args.root / args.git_dir, args.lock, args.expected_version)
        payload = encoded(atlas)
        if args.check:
            if not args.output.is_file() or args.output.read_bytes() != payload:
                raise ValueError(f"generated navigation differs: {args.output}")
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(payload)
    except (ValueError, OSError, KeyError, StopIteration, ET.ParseError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(json.dumps(atlas["statistics"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
