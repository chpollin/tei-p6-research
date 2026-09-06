"""Offline checks of provenance, namespace handling and declaration-only scope."""

import json
import subprocess
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from tools.corpus.git_snapshot import parse_tree
from tools.tei.build_atlas import TEI, build_atlas, encoded, parse_spec


def run_git(folder: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(folder), *args], capture_output=True,
                          check=True, encoding="utf-8").stdout.strip()


@pytest.fixture
def source(tmp_path):
    repo = tmp_path / "upstream"
    repo.mkdir()
    run_git(repo, "init")
    run_git(repo, "config", "user.email", "fixture@example.invalid")
    run_git(repo, "config", "user.name", "Fixture")
    specs = repo / "P5/Source/Specs"
    specs.mkdir(parents=True)
    (specs / "a.xml").write_text(f'''<elementSpec xmlns="{TEI}" ident="a" module="core">
      <classes><memberOf key="att.base"/></classes>
      <content><elementRef key="absent"/></content>
      </elementSpec>''', encoding="utf-8")
    (specs / "att.base.xml").write_text(f'''<classSpec xmlns="{TEI}" ident="att.base" type="atts">
      <attList><attDef ident="inherited"><datatype><dataRef name="string"/></datatype></attDef></attList>
      </classSpec>''', encoding="utf-8")
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "Add fixture")
    commit = run_git(repo, "rev-parse", "HEAD")
    root_tree = run_git(repo, "rev-parse", "HEAD^{tree}")
    entries = parse_tree(subprocess.run(["git", "-C", str(repo), "ls-tree", "-rz", "HEAD"],
                                       capture_output=True, check=True).stdout.decode())
    inventory = {"source_id": "fixture", "repository": "https://example.invalid/fixture.git",
                 "resolved_commit": commit, "root_tree": root_tree, "entries": entries}
    lock = {"source_id": "fixture", "release": {"version": "4.12.0", "resolved_full_commit_sha": commit},
            "hashes": {"git_commit": commit, "git_root_tree": root_tree},
            "origins": {"git_repository": inventory["repository"]}, "manifests": ["manifest.yaml"]}
    registry = {"sources": [{"source_id": "fixture", "authority": "synthetic-test",
                             "rights": {"license_expression": "CC0-1.0"}}]}
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources/registry.yaml").write_text(yaml.safe_dump(registry))
    (tmp_path / "lock.yaml").write_text(yaml.safe_dump(lock))
    (tmp_path / "inventory.json").write_text(json.dumps(inventory))
    manifest = {"source_id": "fixture", "status": "observable-complete", "finished_at": "2026-09-05T00:00:00Z",
                "gaps": [], "requests": [{"resolved_commit": commit}],
                "objects": [{"kind": "git-tree-inventory", "path": "inventory.json", "root_tree": root_tree,
                             "sha256": sha256((tmp_path / "inventory.json").read_bytes()).hexdigest()}]}
    (tmp_path / "manifest.yaml").write_text(yaml.safe_dump(manifest))
    return tmp_path, repo / ".git"


def mutate_yaml(root, path, mutate):
    target = root / path
    data = yaml.safe_load(target.read_bytes())
    mutate(data)
    target.write_text(yaml.safe_dump(data))


def reconcile_inventory(root):
    digest = sha256((root / "inventory.json").read_bytes()).hexdigest()
    mutate_yaml(root, "manifest.yaml", lambda m: m["objects"][0].update(sha256=digest))


def test_rebuild_is_deterministic_and_membership_does_not_inherit(source):
    root, mirror = source
    first = build_atlas(root, mirror, "lock.yaml")
    assert encoded(first) == encoded(build_atlas(root, mirror, "lock.yaml"))
    assert first["generated"] is True
    assert first["generator"] == {"name": "tools.tei.build_atlas", "version": 1}
    assert first["instruction_trust"] == "none"
    a = next(r for r in first["records"] if r["ident"] == "a")
    assert a["local_attributes"] == []
    assert a["classes_declared"] == [{"key": "att.base"}]
    assert a["references"][1]["resolution"] == "declaration-present"
    assert first["statistics"]["local_attributes"] == 1
    assert first["statistics"]["unresolved_references"] == 2
    assert "Inherited attributes" in first["scope"]["excluded"][1]


@pytest.mark.parametrize("change", ["version", "commit", "tree", "incomplete", "inventory-hash", "blob"])
def test_source_mismatch_rejected(source, change):
    root, mirror = source
    if change == "version":
        mutate_yaml(root, "lock.yaml", lambda d: d["release"].update(version="other"))
    elif change == "commit":
        mutate_yaml(root, "lock.yaml", lambda d: d["hashes"].update(git_commit="f" * 40))
    elif change == "tree":
        mutate_yaml(root, "lock.yaml", lambda d: d["hashes"].update(git_root_tree="f" * 40))
    elif change == "incomplete":
        mutate_yaml(root, "manifest.yaml", lambda d: d.update(status="partial"))
    else:
        data = json.loads((root / "inventory.json").read_bytes())
        data["entries"][0]["object_id"] = "f" * 40
        (root / "inventory.json").write_text(json.dumps(data))
        if change == "blob":
            reconcile_inventory(root)
    with pytest.raises(ValueError, match=r"mismatch|incomplete"):
        build_atlas(root, mirror, "lock.yaml")


def test_duplicate_specification_identity_rejected(source):
    root, mirror = source
    repo = mirror.parent
    spec = repo / "P5/Source/Specs/att.base.xml"
    spec.write_bytes(spec.read_bytes().replace(b'ident="att.base"', b'ident="a"'))
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "Duplicate identity")
    commit = run_git(repo, "rev-parse", "HEAD")
    tree_id = run_git(repo, "rev-parse", "HEAD^{tree}")
    mutate_yaml(root, "lock.yaml", lambda d: (d["release"].update(resolved_full_commit_sha=commit),
                                             d["hashes"].update(git_commit=commit, git_root_tree=tree_id)))
    inventory = json.loads((root / "inventory.json").read_bytes())
    entries = parse_tree(subprocess.run(["git", "-C", str(repo), "ls-tree", "-rz", "HEAD"],
                                       capture_output=True, check=True).stdout.decode())
    inventory.update(resolved_commit=commit, root_tree=tree_id, entries=entries)
    (root / "inventory.json").write_text(json.dumps(inventory))
    mutate_yaml(root, "manifest.yaml", lambda d: (d["objects"][0].update(root_tree=tree_id),
                                                d["requests"][0].update(resolved_commit=commit)))
    reconcile_inventory(root)
    with pytest.raises(ValueError, match="duplicate specification identity"):
        build_atlas(root, mirror, "lock.yaml")


def test_namespace_refs_local_attributes_constraints_and_examples():
    xml = f'''<t:elementSpec xmlns:t="{TEI}" xmlns:r="http://relaxng.org/ns/structure/1.0"
      xmlns:s="http://purl.oclc.org/dsdl/schematron" ident="a">
      <t:attList><t:attList><t:attDef ident="local" usage="req">
        <t:datatype><t:dataRef key="teidata.pointer"/></t:datatype>
        <t:valList type="closed"><t:valItem ident="yes"/></t:valList>
        <t:constraintSpec ident="valid" scheme="schematron"><t:constraint>
          <s:rule context="tei:a"><s:assert test="@local">Message</s:assert></s:rule>
        </t:constraint></t:constraintSpec>
        <t:exemplum><t:elementRef key="example-not-structural"/></t:exemplum>
      </t:attDef></t:attList></t:attList>
      <t:content><r:choice><t:elementRef key="b"/><r:ref name="legacy"/></r:choice></t:content>
      <t:exemplum><t:elementSpec ident="not-a-root"/></t:exemplum>
      </t:elementSpec>'''.encode()
    record = parse_spec(xml, "a.xml", "a" * 40, "b" * 40)
    assert record["ident"] == "a"
    assert [r["target"] for r in record["references"]] == ["b", "legacy", "teidata.pointer"]
    assert record["local_attributes"][0]["ident"] == "local"
    assert record["local_attributes"][0]["value_lists"][0]["items"] == [{"ident": "yes"}]
    assert record["content_declared"][0]["children"][0]["name"].startswith("{http://relaxng.org")
    assert record["constraints_declared"][0]["nodes"][1]["attributes"]["test"] == "@local"


def test_dtd_wrong_namespace_duplicate_attributes_and_missing_mirror_rejected(tmp_path):
    for payload, error in [
        (b'<!DOCTYPE a [<!ENTITY x "expanded">]><a/>', "DTD/entity"),
        ('<?xml version="1.0" encoding="UTF-16"?><!DOCTYPE a [<!ENTITY x "expanded">]><a/>'.encode("utf-16"), "DTD/entity"),
        (b'<elementSpec ident="a"/>', "unsupported"),
        (f'<elementSpec xmlns="{TEI}" ident="a"><attList><attDef ident="x"/><attDef ident="x"/></attList></elementSpec>'.encode(), "duplicate"),
    ]:
        with pytest.raises(ValueError, match=error):
            parse_spec(payload, "a.xml", "a" * 40, "b" * 40)
    with pytest.raises(ValueError, match="mirror absent"):
        build_atlas(tmp_path, tmp_path / "missing")
