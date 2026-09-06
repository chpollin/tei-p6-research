"""Quotation admission fails on drift, wrong identities and missing local evidence."""

import hashlib
import json

import pytest
import yaml

from tools.check_wave1_sources import (
    REVIEW_CHAPTER,
    REVIEW_DIRECTORY,
    check,
    check_review,
    current_review_pairs,
    extract_text,
    main,
)


def fixture(root, raw=b"<p>A <em>quoted</em> passage &amp; its context.</p>"):
    quote = "A quoted passage & its context."
    (root / "corpus/raw").mkdir(parents=True)
    (root / "corpus/raw/source").write_bytes(raw)
    (root / "references").mkdir()
    (root / "references/research-wave-1.json").write_text('[{"id":"sample"}]')
    (root / "distillate.md").write_text(
        "---\ntype: distillate\nsource-type: publication\nreference: sample\n---\n"
        f'> "{quote}" (sample, section 1)\n', encoding="utf-8")
    data = {"admissions": [{
        "reference_id": "sample", "source_type": "publication",
        "response": {"sha256": hashlib.sha256(raw).hexdigest(), "byte_count": len(raw),
                     "raw_path": "source", "canonical_url": "https://example.org/source", "status": 200},
        "extraction": {"kind": "html-visible-text"},
        "quotes": [{"text": quote, "locator": "section 1"}], "distillate_path": "distillate.md",
    }]}
    write_manifest(root, data)
    return data


def write_manifest(root, data):
    (root / "manifest.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")


def test_local_html_admission_and_cli_pass(tmp_path, capsys):
    fixture(tmp_path)
    assert check(tmp_path, "manifest.yaml") == (1, 1)
    assert main([str(tmp_path), "--manifest", "manifest.yaml"]) == 0
    assert "1 quotations match 1" in capsys.readouterr().out


def test_html_joins_inline_text_and_decodes_entities_only_once():
    raw = (b"<head><title>omit</title></head><p>pre<em>fix</em> &amp;amp;\n tail</p>"
           b"<script>omit</script><style>omit</style><p>next<br>end</p>")
    assert extract_text(raw, {"kind": "html-visible-text"}) == "prefix &amp; tail next end"


@pytest.mark.parametrize("mutation, message", [
    ("byte-drift", "sha256 mismatch"), ("size-drift", "byte_count mismatch"),
    ("absent-quote", "quotation absent from extracted source"),
    ("bad-status", "status must be successful"), ("missing-raw", "local raw source unavailable"),
    ("distillate-reference", "distillate reference does not match"),
    ("distillate-type", "publication distillate"),
    ("distillate-quote", "quotation absent verbatim from distillate"),
    ("unknown-reference", "admission reference ID"),
    ("extra-reference", "bibliography and admission reference IDs"),
    ("raw-traversal", "escapes its local directory"),
])
def test_invalid_admission_fails(tmp_path, mutation, message):
    data = fixture(tmp_path)
    entry = data["admissions"][0]
    raw_path = tmp_path / "corpus/raw/source"
    distillate = tmp_path / "distillate.md"
    if mutation == "byte-drift":
        raw_path.write_bytes(raw_path.read_bytes().replace(b"passage", b"changed"))
    elif mutation == "size-drift":
        raw_path.write_bytes(raw_path.read_bytes() + b" ")
    elif mutation == "absent-quote":
        entry["quotes"][0]["text"] = "This was never in the source."
    elif mutation == "bad-status":
        entry["response"]["status"] = 403
    elif mutation == "missing-raw":
        raw_path.unlink()
    elif mutation.startswith("distillate-"):
        old, new = {
            "distillate-reference": ("reference: sample", "reference: unrelated"),
            "distillate-type": ("source-type: publication", "source-type: document"),
            "distillate-quote": ("A quoted passage", "An altered passage"),
        }[mutation]
        distillate.write_text(distillate.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
    elif mutation == "unknown-reference":
        entry["reference_id"] = "unrelated"
    elif mutation == "extra-reference":
        (tmp_path / "references/research-wave-1.json").write_text('[{"id":"sample"},{"id":"extra"}]')
    else:
        entry["response"]["raw_path"] = "../source"
    write_manifest(tmp_path, data)
    with pytest.raises(ValueError, match=message):
        check(tmp_path, "manifest.yaml")


def test_json_field_is_literal_and_path_must_resolve(tmp_path):
    text = "A quoted passage &amp; its context."
    raw = json.dumps({"ticket": {"description": text}}).encode()
    data = fixture(tmp_path, raw)
    entry = data["admissions"][0]
    entry["extraction"] = {"kind": "json-field", "path": ["ticket", "description"]}
    entry["quotes"][0]["text"] = text
    distillate = tmp_path / "distillate.md"
    distillate.write_text(distillate.read_text().replace(" & ", " &amp; "))
    write_manifest(tmp_path, data)
    assert check(tmp_path, "manifest.yaml") == (1, 1)
    entry["quotes"][0]["text"] = text.replace("&amp;", "&")
    write_manifest(tmp_path, data)
    with pytest.raises(ValueError, match="quotation absent from extracted source"):
        check(tmp_path, "manifest.yaml")
    entry["extraction"]["path"] = ["ticket", "missing"]
    write_manifest(tmp_path, data)
    with pytest.raises(ValueError, match="JSON field path does not resolve"):
        check(tmp_path, "manifest.yaml")


def test_missing_raw_cli_fails_clearly(tmp_path, capsys):
    fixture(tmp_path)
    (tmp_path / "corpus/raw/source").unlink()
    assert main([str(tmp_path), "--manifest", "manifest.yaml"]) == 1
    assert "sample: local raw source unavailable" in capsys.readouterr().err


def review_fixture(root):
    """Four canonical chains and an audit, deliberately without corpus/raw."""
    (root / "20_distillates/publications").mkdir(parents=True)
    (root / "30_assertions").mkdir()
    (root / "references").mkdir()
    admissions = []
    for index in range(4):
        reference = f"source{index}"
        path = f"20_distillates/publications/{reference}.md"
        (root / path).write_text(
            "---\ntype: distillate\nsource-type: publication\n"
            f"reference: {reference}\n---\n# Distillate {index}\n\n## Core statements\n\n"
            f'- Source {index} makes a bounded claim. ^s1\n  > "Quote {index}." (source {index})\n',
            encoding="utf-8")
        (root / f"30_assertions/claim{index}.md").write_text(
            f'---\ntype: assertion\ngrounding:\n  - "[[20_distillates/publications/{reference}#^s1]]"\n'
            f"---\n# Source {index} makes a bounded claim\n", encoding="utf-8")
        admissions.append({"reference_id": reference, "source_type": "publication", "distillate_path": path})
    write_manifest(root, {"admissions": admissions})
    (root / "references/research-wave-1.json").write_text(json.dumps([{"id": f"source{i}"} for i in range(4)]))
    (root / "40_output").mkdir()
    write_chapter(root, [f"[[30_assertions/claim{i}]]" for i in range(4)])
    pairs = current_review_pairs(root, "manifest.yaml")
    verdicts = [{"id": pair["id"], "verdict": "fully supports", "reason": "The quotation supports this attribution.",
                 "reviewer": "independent test reviewer", "prompt_sha256": pair["prompt_sha256"]} for pair in pairs]
    audit = root / REVIEW_DIRECTORY
    audit.mkdir(parents=True)
    write_audit(audit / "pairs.jsonl", pairs)
    write_audit(audit / "verdicts.jsonl", verdicts)
    return pairs, verdicts


def write_audit(path, records):
    path.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")


def write_chapter(root, assertions):
    (root / REVIEW_CHAPTER).write_text(
        "---\n" + yaml.safe_dump({"type": "chapter", "assertions": assertions})
        + "---\n# Reviewed chapter\n", encoding="utf-8")


def test_review_only_has_no_raw_prerequisite(tmp_path, capsys):
    review_fixture(tmp_path)
    assert not (tmp_path / "corpus/raw").exists()
    assert check_review(tmp_path, "manifest.yaml").pairs == 8
    assert main([str(tmp_path), "--manifest", "manifest.yaml", "--review-only"]) == 0
    assert "8 passing review verdicts" in capsys.readouterr().out


@pytest.mark.parametrize("mutation, message", [
    ("changed-claim", "stale against the current prompts"),
    ("missing-pair", "pair coverage"), ("extra-pair", "pair coverage"),
    ("stale-verdict-hash", "stale review verdict prompt hash"),
    ("nonpass", "nonpassing review verdict"),
    ("missing-verdict", "verdict coverage is incomplete"),
    ("extra-assertion", "four assertions"), ("missing-assertion", "assertion root is missing"),
    ("remove-chapter-root", "four assertions"), ("change-chapter-root", "pair coverage"),
    ("extra-source-statement", "exactly eight canonical pairs"),
])
def test_review_rejects_stale_or_incomplete_coverage(tmp_path, mutation, message):
    pairs, verdicts = review_fixture(tmp_path)
    audit = tmp_path / REVIEW_DIRECTORY
    if mutation == "changed-claim":
        path = tmp_path / "30_assertions/claim0.md"
        path.write_text(path.read_text().replace("bounded claim", "universal claim"))
    elif mutation == "missing-pair":
        write_audit(audit / "pairs.jsonl", pairs[:-1])
    elif mutation == "extra-pair":
        write_audit(audit / "pairs.jsonl", [*pairs, {**pairs[0], "id": "extra"}])
    elif mutation == "stale-verdict-hash":
        verdicts[0]["prompt_sha256"] = "0" * 64
        write_audit(audit / "verdicts.jsonl", verdicts)
    elif mutation == "nonpass":
        verdicts[0]["verdict"] = "overreaches"
        write_audit(audit / "verdicts.jsonl", verdicts)
    elif mutation == "missing-verdict":
        write_audit(audit / "verdicts.jsonl", verdicts[:-1])
    elif mutation == "extra-assertion":
        (tmp_path / "30_assertions/extra.md").write_bytes((tmp_path / "30_assertions/claim0.md").read_bytes())
        write_chapter(tmp_path, [f"[[30_assertions/claim{i}]]" for i in range(4)] + ["[[30_assertions/extra]]"])
    elif mutation == "missing-assertion":
        (tmp_path / "30_assertions/claim0.md").unlink()
    elif mutation == "remove-chapter-root":
        write_chapter(tmp_path, [f"[[30_assertions/claim{i}]]" for i in range(1, 4)])
    elif mutation == "change-chapter-root":
        (tmp_path / "30_assertions/replacement.md").write_bytes((tmp_path / "30_assertions/claim0.md").read_bytes())
        write_chapter(tmp_path, ["[[30_assertions/replacement]]"] + [f"[[30_assertions/claim{i}]]" for i in range(1, 4)])
    else:
        path = tmp_path / "20_distillates/publications/source0.md"
        path.write_text(path.read_text() + '\n- Another claim. ^s2\n  > "Another quote." (source 0)\n')
    with pytest.raises(ValueError, match=message):
        check_review(tmp_path, "manifest.yaml")


def test_unrelated_cross_source_synthesis_does_not_expand_historical_review(tmp_path):
    review_fixture(tmp_path)
    (tmp_path / "30_assertions/later-synthesis.md").write_text(
        '---\ntype: assertion\ngrounding:\n'
        '  - "[[20_distillates/publications/source0#^s1]]"\n'
        '  - "[[20_distillates/publications/source1#^s1]]"\n'
        '---\n# A later cross-source synthesis\n', encoding="utf-8")
    assert check_review(tmp_path, "manifest.yaml").pairs == 8
