"""Reproduce the editorial profile and real-fragment comparison, with source audit."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from itertools import pairwise
from pathlib import Path

if __package__ in (None, ""):  # run as a script, so the package root is not on the path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.check_abstract_text_v01 import json_bytes, read_json, text_sha256
from tools.ingest_editorial_cases import embedded_source
from tools.models import editorial_profile as profile
from tools.review import Pair, ReviewAudit, check_support_review, select_pairs
from tools.tei.editorial_cases import compare_fragment

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("experiments/editorial_cases")
REPORT = BASE / "report.json"
AUDIT = Path("workbench/reviews/2026-09-05-editorial-cases")
DOCUMENTS = {
    "20_distillates/documents/humboldt-h0017682-7d174637",
    "30_assertions/humboldt-diary-encodes-a-dated-nested-heading",
    "30_assertions/humboldt-diary-separates-an-unknown-hand-note-and-editorial-explanation",
    "30_assertions/humboldt-diary-encodes-a-page-pointer-and-separate-foliation",
}


def in_scope(pair: Pair) -> bool:
    return pair.document in DOCUMENTS


def current_pairs(root: Path = ROOT) -> list[dict]:
    """The six source-support pairs the editorial evidence closure cuts today."""
    pairs = [pair.to_dict() for pair in select_pairs(root, in_scope, DOCUMENTS)]
    if len(pairs) != 6 or {pair["document"] for pair in pairs} != DOCUMENTS:
        raise ValueError("editorial source-review scope is incomplete")
    return pairs


def check_review(root: Path = ROOT) -> ReviewAudit:
    """Audit the recorded editorial review against the current pairs."""
    return check_support_review(
        root, root / AUDIT, in_scope, expected=6, documents=DOCUMENTS
    )


def _codes(result: dict) -> list[str]:
    return sorted({item["code"] for item in result["diagnostics"]})


def identity_results(root: Path) -> list[dict]:
    suite = read_json(root / BASE / "identity-cases.json")
    if suite["profile_version"] != profile.PROFILE_VERSION or not suite["cases"]:
        raise ValueError("invalid independent identity suite")
    results, seen = [], set()
    for case in suite["cases"]:
        if case["id"] in seen:
            raise ValueError("duplicate identity case")
        seen.add(case["id"])
        models = copy.deepcopy(suite["models"])
        before = json_bytes(models)
        args = case["input"]
        if case["operation"] == "validate":
            result = profile.validate_profile(models[args["model"]])
            actual = {"valid": result["valid"], "codes": _codes(result)}
        elif case["operation"] == "revision":
            result = profile.check_profile_revision(models[args["before"]], models[args["after"]])
            actual = {"valid": result["valid"], "codes": _codes(result)}
        elif case["operation"] == "current":
            actual = {"claims": [claim["id"] for claim in profile.current_derivations(
                models[args["model"]], agent=args.get("agent"), subject=args.get("subject"))]}
        else:
            raise ValueError("unknown identity operation")
        results.append({"id": case["id"], "expected": case["expected"], "actual": actual,
                        "nonmutating": before == json_bytes(models),
                        "passed": before == json_bytes(models) and json_bytes(actual) == json_bytes(case["expected"])})
    return results


def _development_checks(case: dict, observed: dict) -> dict:
    """Check explicit textual and markup facts from the pre-mapping human-readable oracle."""
    checks = {"primary_text": observed["text"] == case["primary_text"]}
    elements = observed["elements"]
    if case["case_id"] == "case-1-hierarchy":
        checks["nested_element_order"] = [element["tag"] for element in elements] == ["head", "date", "hi", "hi", "placeName"]
        checks["separate_equal_extents"] = len({element["id"] for element in elements}) == 5 and len(elements) == 5 and all(element["extent"] == [0, 19] for element in elements[:3])
        checks["date_and_place_metadata"] = any(element["attributes"] == {"when": "1790-06-15", "calendar": "#gregorian"} for element in elements) and any(element["attributes"].get("ref") == "https://edition-humboldt.de/H0005512 https://www.geonames.org/11609031" for element in elements)
        checks["rendition_and_parentage"] = len(elements) == 5 and elements[2]["attributes"] == {"rendition": "#u"} and elements[3]["attributes"] == {"rendition": "#aq"} and all(child["parent"] == parent["id"] for parent, child in pairwise(elements))
    elif case["case_id"] == "case-2-interrupted-heading":
        notes = observed["notes"]
        unknown = next((note for note in notes if note["attributes"].get("hand") == "#unknown"), None)
        editorial = next((note for note in notes if note["attributes"].get("type") == "editorial"), None)
        checks["separate_note_texts"] = bool(len(notes) == 2 and unknown and editorial and unknown["own_text"] == case["unknown_hand_note_text"] and editorial["own_text"] == case["editorial_note_text"])
        checks["nested_responsibility"] = bool(unknown and editorial and editorial["parent"] == unknown["id"] and editorial["attributes"].get("resp") == "#CT #DE")
        refs = unknown["refs"] if unknown else []
        checks["reciprocal_note_references"] = bool(len(refs) == 1 and editorial and refs[0]["text"] == "6255" and refs[0]["attributes"].get("corresp") == "#" + editorial["attributes"].get("xml:id", "") and editorial["attributes"].get("corresp") == "#" + refs[0]["attributes"].get("xml:id", ""))
        checks["source_note_identifiers"] = bool(len(refs) == 1 and editorial
            and refs[0]["attributes"].get("xml:id") == "bab01c0c-9760-4703-b01c-0c9760d7037b"
            and refs[0]["attributes"].get("type") == "editorialNote"
            and editorial["attributes"].get("xml:id") == "f05a05fb-11de-42d0-9a05-fb11def2d021")
        checks["line_break_retained"] = len(observed["breaks"]) == 1 and observed["breaks"][0]["offset"] in (12, 13)
    else:
        raise ValueError("unknown development case")
    return checks


def build_report(root: Path = ROOT) -> dict:
    payload = embedded_source(root)
    cases = read_json(root / BASE / "cases.json")
    if {case["case_id"] for case in cases["cases"]} != {"case-1-hierarchy", "case-2-interrupted-heading", "case-3-holdout-media"} or len(cases["cases"]) != 3:
        raise ValueError("real-case boundary changed")
    results = []
    for case in cases["cases"]:
        fragment = payload[case["start_byte"]:case["end_byte"]]
        if hashlib.sha256(fragment).hexdigest() != case["fragment_sha256"] or fragment.decode("utf-8") != case["original_xml"]:
            raise ValueError("case fragment drift")
        compared = compare_fragment(case["original_xml"])
        if not case["holdout"]:
            baseline_checks = _development_checks(case, compared["baseline"]["observations"])
            candidate_checks = _development_checks(case, compared["candidate"]["observations"]) if compared["candidate"]["valid"] else {"candidate_valid": False}
            passed = all(baseline_checks.values()) and all(candidate_checks.values())
            results.append({"id": case["case_id"], "role": "development", "passed": passed,
                            "baseline_checks": baseline_checks, "candidate_checks": candidate_checks,
                            "observations_equal": compared["baseline"]["observations"] == compared["candidate"]["observations"],
                            "comparison": compared})
        else:
            # The held-back case can pass the evaluation gate by exposing a failure
            # to map; it must not be counted as a successful migration.
            unsupported = compared["candidate"]["unsupported"]
            refused = not compared["candidate"]["valid"] and compared["candidate"]["package"] is None and bool(unsupported)
            primary_matches = compared["baseline"]["observations"]["text"] == case["primary_text"]
            results.append({"id": case["case_id"], "role": "holdout", "passed": refused,
                            "migration_success": False, "expected_primary_text": case["primary_text"],
                            "baseline_primary_text_matches": primary_matches,
                            "outcome": "Candidate explicitly refuses unsupported source constructs; retained tree XML is not a claim of task-semantic or media preservation.",
                            "comparison": compared})
    identity = identity_results(root)
    paths = [*sorted((root / BASE).glob("*.json")),
             root / "tools/ingest_editorial_cases.py", root / "tools/check_editorial_cases.py",
             root / "tools/models/abstract_text.py", root / "tools/models/editorial_profile.py",
             root / "tools/tei/editorial_cases.py", root / "10_markdown/documents/humboldt-h0017682-7d174637.md"]
    # One fingerprint policy across the check scripts: see text_sha256.
    fingerprints = {path.relative_to(root).as_posix(): text_sha256(path)
                    for path in paths if path.relative_to(root) != REPORT}
    return {"format_version": 1, "authority": "Bounded experiment; not a Vault grounding source or domain review.",
            "license": cases["license"], "attribution": cases["attribution"], "inputs": fingerprints,
            "summary": {"passed": all(row["passed"] for row in identity + results),
                        "identity_cases": len(identity), "identity_passes": sum(row["passed"] for row in identity),
                        "real_fragments": len(results), "successful_bounded_mappings": sum(row["passed"] for row in results if row["role"] == "development"),
                        "holdout_migration_success": False},
            "identity": identity, "editorial": results,
            "limits": ["Single-document purposive sample", "No measured editor workflow or practical-adequacy verdict", "No full P5/ODD or whole-document conversion guarantee", "Tree retention, task observations, and media semantics are distinct", "Identity examples are synthetic; editorial source fragments are real"]}


def _reviewer_note(audit: ReviewAudit) -> str:
    """Attribution is recorded where it exists and named where it does not."""
    if not audit.without_reviewer:
        return ""
    return f"; {len(audit.without_reviewer)} verdict(s) name no reviewer"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true")
    group.add_argument("--emit-review", action="store_true")
    group.add_argument("--review-only", action="store_true")
    args = parser.parse_args()
    try:
        if args.emit_review:
            path = ROOT / AUDIT / "pairs.jsonl"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("".join(json.dumps(pair, ensure_ascii=False) + "\n" for pair in current_pairs()), encoding="utf-8", newline="\n")
            print("OK: six source-support pairs emitted; independent verdicts required")
            return 0
        if args.review_only:
            audit = check_review()
            print(f"OK: {audit.pairs} current editorial source-support pairs passed"
                  f"{_reviewer_note(audit)}")
            return 0
        report = build_report()
        encoded = json_bytes(report)
        if args.check:
            check_review()
            if not (ROOT / REPORT).exists() or (ROOT / REPORT).read_bytes() != encoded:
                raise ValueError("editorial report missing or stale")
        else:
            (ROOT / REPORT).write_bytes(encoded)
        print(json.dumps(report["summary"], sort_keys=True))
        return 0 if report["summary"]["passed"] else 1
    except (OSError, KeyError, ValueError, TypeError) as exc:
        print(f"Editorial case gate failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
