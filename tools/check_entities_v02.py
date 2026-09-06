"""Reproduce independently authored 0.2 entity cases, or validate a local 0.2 package."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

if __package__ in (None, ""):  # run as a script, so the package root is not on the path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.check_abstract_text_v01 import json_bytes, read_json, text_sha256
from tools.models import entities as model

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("experiments/entities_v02")
REPORT = BASE / "report.json"
CASES = BASE / "cases.json"
OPERATIONS = {"denotations_of": ("mention_id", "denotations"),
              "names_of": ("entity_id", "names")}
CASE_FIELDS = ({"id", "description", "package", "expect"}, {"operations"})


def _diagnostics(items: object) -> list[dict]:
    """Sorted unique {code,path} pairs, so a recorded order never decides a case."""
    if type(items) is not list or any(
            type(item) is not dict or set(item) != {"code", "path"}
            or type(item["code"]) is not str or type(item["path"]) is not str for item in items):
        raise ValueError("diagnostics must be {code,path} objects")
    return [{"code": code, "path": path}
            for path, code in sorted({(item["path"], item["code"]) for item in items})]


def validate_suite(suite: object, spec: dict) -> list[dict]:
    """Reject a malformed suite before any case runs; return the case list."""
    if (type(suite) is not dict or set(suite) != {"format_version", "model_version", "authority", "cases"}
            or suite["format_version"] != 1 or type(suite["format_version"]) is not int
            or suite["model_version"] != spec["model_version"]
            or type(suite["authority"]) is not str or not suite["authority"]):
        raise ValueError("invalid case-suite envelope")
    cases = suite["cases"]
    if type(cases) is not list or not cases:
        raise ValueError("a nonempty case list is required")
    required, optional = CASE_FIELDS
    seen = set()
    for case in cases:
        if type(case) is not dict or not required.issubset(case) or not set(case).issubset(required | optional):
            raise ValueError("invalid case record")
        if type(case["id"]) is not str or not case["id"] or case["id"] in seen:
            raise ValueError("case IDs must be unique nonempty strings")
        seen.add(case["id"])
        if type(case["description"]) is not str or not case["description"]:
            raise ValueError(f"case description required: {case['id']}")
        expected = case["expect"]
        if type(expected) is not dict or set(expected) != {"valid", "diagnostics"} or type(expected["valid"]) is not bool:
            raise ValueError(f"invalid expected outcome: {case['id']}")
        codes = {item["code"] for item in _diagnostics(expected["diagnostics"])}
        if not codes <= set(spec["diagnostics"]):
            raise ValueError(f"unknown expected diagnostic in {case['id']}: {sorted(codes - set(spec['diagnostics']))}")
        for entry in case.get("operations", []):
            if (type(entry) is not dict or set(entry) != {"name", "arguments", "expect"}
                    or entry["name"] not in OPERATIONS or type(entry["arguments"]) is not dict
                    or type(entry["expect"]) is not dict):
                raise ValueError(f"invalid operation entry in {case['id']}")
            if set(entry["arguments"]) - {OPERATIONS[entry["name"]][0], "include_withdrawn"}:
                raise ValueError(f"unknown argument for {entry['name']} in {case['id']}")
    return cases


def run_operation(package: dict, entry: dict) -> dict:
    argument, listed = OPERATIONS[entry["name"]]
    arguments = entry["arguments"]
    operation = getattr(model, entry["name"])
    result = operation(package, arguments.get(argument),
                       include_withdrawn=arguments.get("include_withdrawn", False))
    return {"diagnostics": result["diagnostics"], listed: result[listed]}


def execute(case: dict) -> dict:
    """Run one case against the extension, reporting actual outcome and operations."""
    package = copy.deepcopy(case["package"])
    before = json_bytes(package)
    result = model.validate_extension(package)
    actual = {"valid": result["valid"], "diagnostics": result["diagnostics"]}
    expected = {"valid": case["expect"]["valid"], "diagnostics": _diagnostics(case["expect"]["diagnostics"])}
    operations = []
    for entry in case.get("operations", []):
        produced = run_operation(package, entry)
        operations.append({"name": entry["name"], "arguments": entry["arguments"],
                           "expected": entry["expect"], "actual": produced,
                           "passed": json_bytes(produced) == json_bytes(entry["expect"])})
    unchanged = before == json_bytes(package)
    return {"expected": expected, "actual": actual, "nonmutating": unchanged,
            "codes_match": {item["code"] for item in actual["diagnostics"]}
                           == {item["code"] for item in expected["diagnostics"]},
            "operations": operations,
            "passed": unchanged and json_bytes(actual) == json_bytes(expected)
                      and all(item["passed"] for item in operations)}


def canonical_check(name: str, package: dict) -> dict:
    """Canonical bytes must be stable, reproduce through JSON, and stay nonmutating."""
    before = json_bytes(package)
    try:
        encoded = model.canonical_bytes(package)
        roundtrip = json.loads(encoded)
        passed = (encoded == model.canonical_bytes(package)
                  and encoded == model.canonical_bytes(roundtrip)
                  and model.equivalent(package, roundtrip)
                  and before == json_bytes(package))
        return {"package": name, "passed": passed, "sha256": hashlib.sha256(encoded).hexdigest()}
    except (ValueError, KeyError, TypeError) as exc:
        return {"package": name, "passed": False, "error": f"{type(exc).__name__}: {exc}"}


def build_report(root: Path = ROOT) -> dict:
    spec = read_json(root / BASE / "spec.json")
    suite_path = root / CASES
    cases = validate_suite(read_json(suite_path), spec) if suite_path.exists() else []
    results = []
    for case in cases:
        try:
            outcome = execute(case)
        except Exception as exc:  # A case crash is a report failure, never a missing row.
            outcome = {"error": f"{type(exc).__name__}: {exc}", "passed": False}
        results.append({"id": case["id"], "description": case["description"], **outcome})

    canonical_checks = [canonical_check(case["id"], case["package"]) for case in cases
                        if model.validate_extension(case["package"])["valid"]]
    example_paths = sorted((root / BASE / "examples").glob("*.json"))
    examples = []
    for path in example_paths:
        package = read_json(path)
        validation = model.validate_extension(package)
        examples.append({"path": path.relative_to(root).as_posix(), "valid": validation["valid"],
                         "diagnostics": validation["diagnostics"], "passed": validation["valid"]})
        canonical_checks.append(canonical_check(path.name, package))

    # Contract, code, case and example changes invalidate the recorded report.
    paths = [BASE / "spec.json", *([CASES] if suite_path.exists() else []),
             Path("knowledge/text-model.md"), Path("tools/check_entities_v02.py"),
             *[path.relative_to(root) for path in sorted((root / "tools/models").glob("*.py"))],
             *[path.relative_to(root) for path in example_paths]]
    covered = sorted({entry["name"] for case in cases for entry in case.get("operations", [])})
    checks = [*results, *canonical_checks, *examples]
    passed = bool(cases) and covered == sorted(OPERATIONS) and all(item["passed"] for item in checks)
    return {
        "format_version": 1, "model_version": spec["model_version"],
        "authority": "Synthetic experimental observations; not a Vault grounding source or human acceptance.",
        "fingerprint_policy": "SHA-256 of UTF-8 text with checkout CRLF/CR normalized to LF; model content is unchanged.",
        "inputs": {path.as_posix(): text_sha256(root / path) for path in paths},
        "summary": {"passed": passed, "cases_present": bool(cases), "cases": len(results),
                    "case_passes": sum(item["passed"] for item in results),
                    "operations_covered": covered,
                    "canonical_checks": len(canonical_checks), "examples": len(examples)},
        "cases": results, "canonical_checks": canonical_checks, "examples": examples,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="reproduce without rewriting the recorded report")
    group.add_argument("--validate", type=Path, metavar="PACKAGE.json", help="validate one local 0.2 package")
    args = parser.parse_args(argv)
    try:
        if args.validate is not None:
            result = model.validate_extension(read_json(args.validate))
            print(json_bytes(result).decode("utf-8"), end="")
            return 0 if result["valid"] else 1
        report = build_report()
        encoded = json_bytes(report)
        if args.check:
            if not (ROOT / REPORT).exists() or (ROOT / REPORT).read_bytes() != encoded:
                raise ValueError("report missing or stale; inspect changes and regenerate intentionally")
        else:
            (ROOT / REPORT).write_bytes(encoded)
        print(json.dumps(report["summary"], sort_keys=True))
        if not report["summary"]["cases_present"]:
            print(f"No case suite: {CASES.as_posix()} is absent; the extension is unverified.", file=sys.stderr)
        failures = [case["id"] for case in report["cases"] if not case["passed"]]
        if failures:
            print("Failed cases: " + ", ".join(failures))
        return 0 if report["summary"]["passed"] else 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Entity extension 0.2 check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
