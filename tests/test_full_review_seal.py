"""Public review seals detect stale material without redistributing source context."""

import copy
import json
import shutil
from pathlib import Path

import pytest

from tools import full_review


@pytest.fixture
def sealed(tmp_path):
    root = tmp_path / "vault"
    shutil.copytree(Path(__file__).parent / "fixtures/minimal", root)
    units, _ = full_review.emit_units(root, {})
    ids = [u["id"] for u in units if u["document"] == "20_distillates/documents/report-garden-water-2026"]
    out = tmp_path / "review"
    meta = full_review.emit(root, None, out, ids)
    record = {key: value for key, value in meta.items() if key != "root"}
    record["verdicts"] = [{
        "id": identifier, "prompt_sha256": hashed, "verdict": "fully supports",
        "model": "claude-opus-5", "reviewer": "Offline test fixture",
        "requested_model": "opus", "outcome_sha256": "c" * 64,
        "checked_at": "2026-09-11", "package_sha256": "a" * 64,
        "reason": "Fixture judgment; no model was called.",
    } for identifier, hashed in record["unit_hashes"].items()]
    path = tmp_path / "seal.json"
    full_review.write_json(path, record)
    return root, out, path, record


def test_public_seal_checks_current_material_without_original_context(sealed):
    root, _, path, _ = sealed
    result = full_review.check_seal(path, root)
    assert result["all_support"]
    assert not result["human_verified"]
    assert "Private prompts" in result["boundary"]


def test_source_text_change_invalidates_the_public_seal(sealed):
    root, _, path, _ = sealed
    source = root / "10_markdown/documents/report-garden-water-2026.md"
    source.write_text(source.read_text(encoding="utf-8") + "\nChanged source passage.\n", encoding="utf-8")
    with pytest.raises(ValueError, match="sealed review material changed"):
        full_review.check_seal(path, root)


@pytest.mark.parametrize("change", ["hash", "duplicate", "instrument", "missing"])
def test_public_seal_refuses_invalid_or_incomplete_bindings(sealed, change):
    root, _, path, original = sealed
    record = copy.deepcopy(original)
    if change == "hash":
        record["verdicts"][0]["prompt_sha256"] = "b" * 64
    elif change == "duplicate":
        record["verdicts"].append(record["verdicts"][0])
    elif change == "instrument":
        record["instrument_files"]["tools/full_review.py"] = "b" * 64
    else:
        record["verdicts"].pop()
    full_review.write_json(path, record)
    if change == "missing":
        result = full_review.check_seal(path, root)
        assert result["missing"] and not result["all_support"]
    else:
        with pytest.raises(ValueError):
            full_review.check_seal(path, root)


def test_emission_metadata_cannot_silently_change_privacy_or_evidence(sealed):
    _, out, _, _ = sealed
    units = full_review.read_json(out / "units.json")
    units[0]["storage"] = "local-only"
    full_review.write_json(out / "units.json", units)
    with pytest.raises(ValueError, match="unit metadata changed"):
        full_review.collect(out)


def test_seal_omits_private_reviewer_reason(sealed, monkeypatch, tmp_path):
    _, out, _, record = sealed
    units = full_review.read_json(out / "units.json")
    units[0]["storage"] = "local-only"
    full_review.write_json(out / "units.json", units)
    verdicts = {v["id"]: dict(v) for v in record["verdicts"]}
    secret = "A private source sentence quoted by the reviewer."
    verdicts[units[0]["id"]]["reason"] = secret
    monkeypatch.setattr(full_review, "collect", lambda _: verdicts)
    path = tmp_path / "public.json"
    full_review.seal(out, path)
    text = path.read_text(encoding="utf-8")
    assert secret not in text
    assert full_review.digest(secret) in text
    assert "document_independence" in json.loads(text)
