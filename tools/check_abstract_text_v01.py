"""Reproduce independently authored v0.1 cases, or validate a local model JSON."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

if __package__ in (None, ""):  # run as a script, so the package root is not on the path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.models import abstract_text as model

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("experiments/abstract_text_v01")
REPORT = BASE / "report.json"
OPERATIONS = {"validate", "equivalent", "revision", "reanchor"}
INPUT_FIELDS = {
    "validate": {"model"}, "equivalent": {"left", "right"},
    "revision": {"before", "after"},
    "reanchor": {"model", "selection", "target_version", "continuity"},
}


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode("utf-8")


def text_sha256(path: Path) -> str:
    """The input fingerprint of a text file, one policy for every check script.

    SHA-256 of UTF-8 text with checkout CRLF/CR normalized to LF, so a report
    reproduces on Windows and Linux alike. The content itself stays unchanged.
    """
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def _object(pairs: list[tuple]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _constant(value: str):
    raise ValueError(f"non-JSON numeric constant: {value}")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_object,
                      parse_constant=_constant)


def _codes(result: dict) -> list[str]:
    return sorted({item["code"] for item in result["diagnostics"]})


def execute(case: dict, packages: dict) -> dict:
    args, operation = case["input"], case["operation"]
    if operation == "validate":
        result = model.validate_model(packages[args["model"]])
        return {key: result[key] for key in
                ("valid", "all_selections_resolved", "resolutions")} | {"codes": _codes(result)}
    if operation == "equivalent":
        left, right = packages[args["left"]], packages[args["right"]]
        equal = model.equivalent(left, right)
        if equal != (model.canonical_bytes(left) == model.canonical_bytes(right)):
            raise ValueError("equivalence disagrees with canonical comparison")
        return {"equivalent": equal}
    if operation == "revision":
        result = model.check_revision(packages[args["before"]], packages[args["after"]])
        return {"valid": result["valid"], "codes": _codes(result)}
    if operation == "reanchor":
        result = model.propose_reanchor(packages[args["model"]], args["selection"],
                                        args["target_version"], args["continuity"])
        return {"codes": _codes(result), "proposal": result["proposal"]}
    raise ValueError(f"unknown operation: {operation}")


def validate_suite(suite: dict, spec: dict) -> None:
    if (type(suite) is not dict or set(suite) != {"format_version", "model_version", "models", "cases"}
            or type(suite["format_version"]) is not int or suite["format_version"] != 1
            or suite["model_version"] != spec["model_version"]):
        raise ValueError("invalid case-suite envelope")
    packages, cases = suite["models"], suite["cases"]
    if type(packages) is not dict or not packages or type(cases) is not list or not cases:
        raise ValueError("nonempty models and cases are required")
    seen, rules, operations = set(), set(), set()
    for case in cases:
        if type(case) is not dict or set(case) != {"id", "description", "rules", "operation", "input", "expected"}:
            raise ValueError("invalid case record")
        if type(case["id"]) is not str or not case["id"] or case["id"] in seen:
            raise ValueError("case IDs must be unique nonempty strings")
        seen.add(case["id"])
        if type(case["description"]) is not str or not case["description"]:
            raise ValueError("case description required")
        labels = case["rules"]
        if (type(labels) is not list or not labels or any(type(rule) is not str for rule in labels)
                or len(labels) != len(set(labels)) or not set(labels) <= set(spec["rules"])):
            raise ValueError("invalid case rule coverage")
        rules.update(labels)
        operation, args = case["operation"], case["input"]
        if type(operation) is not str or operation not in OPERATIONS:
            raise ValueError("unknown case operation")
        operations.add(operation)
        if (type(args) is not dict or set(args) != INPUT_FIELDS[operation]
                or any(type(value) is not str or not value for value in args.values())):
            raise ValueError("invalid operation arguments")
        for key in set(args) & {"model", "left", "right", "before", "after"}:
            if args[key] not in packages:
                raise ValueError("case references an unknown model")
        expected = case["expected"]
        fields = {"validate": {"valid", "all_selections_resolved", "codes", "resolutions"},
                  "equivalent": {"equivalent"}, "revision": {"valid", "codes"},
                  "reanchor": {"codes", "proposal"}}[operation]
        if type(expected) is not dict or set(expected) != fields:
            raise ValueError("invalid expected outcome shape")
        for key in fields & {"valid", "all_selections_resolved", "equivalent"}:
            if type(expected[key]) is not bool:
                raise ValueError("expected booleans must not be numeric")
        if "codes" in fields:
            codes = expected["codes"]
            if (type(codes) is not list or any(type(code) is not str for code in codes)
                    or codes != sorted(set(codes)) or not set(codes) <= set(spec["diagnostics"])):
                raise ValueError("unknown, duplicated, or unordered expected diagnostics")
    if rules != set(spec["rules"]) or operations != OPERATIONS:
        raise ValueError("suite must cover every declared rule and public operation family")


def build_report(root: Path = ROOT) -> dict:
    spec = read_json(root / BASE / "spec.json")
    suite = read_json(root / BASE / "cases.json")
    validate_suite(suite, spec)
    results = []
    for case in suite["cases"]:
        packages = copy.deepcopy(suite["models"])
        before = json_bytes(packages)
        try:
            actual = execute(case, packages)
            unchanged = before == json_bytes(packages)
            passed = unchanged and json_bytes(actual) == json_bytes(case["expected"])
            result = {"actual": actual, "nonmutating": unchanged, "passed": passed}
        except Exception as exc:  # A case crash is a report failure, never a missing row.
            result = {"error": f"{type(exc).__name__}: {exc}", "passed": False}
        results.append({"id": case["id"], "description": case["description"],
                        "operation": case["operation"], "rules": case["rules"],
                        "expected": case["expected"], **result})

    canonical_checks = []
    for name, package in suite["models"].items():
        before = json_bytes(package)
        validation = model.validate_model(package)
        if not validation["valid"]:
            continue
        try:
            encoded = model.canonical_bytes(package)
            roundtrip = json.loads(encoded)
            passed = (encoded == model.canonical_bytes(package)
                      and encoded == model.canonical_bytes(roundtrip)
                      and model.equivalent(package, roundtrip)
                      and before == json_bytes(package))
            canonical_checks.append({"model": name, "passed": passed,
                                     "sha256": hashlib.sha256(encoded).hexdigest()})
        except Exception as exc:
            canonical_checks.append({"model": name, "passed": False,
                                     "error": f"{type(exc).__name__}: {exc}"})

    example_checks = []
    example_paths = sorted((root / BASE / "examples").glob("*.json"))
    required_examples = {"competing-readings.json": "competing_readings",
                         "identity-and-reanchoring.json": "identity_and_reanchoring"}
    if not set(required_examples) <= {path.name for path in example_paths}:
        raise ValueError("standalone example missing")
    for path in example_paths:
        package = read_json(path)
        validation = model.validate_model(package)
        matches = path.name not in required_examples or (
            json_bytes(package) == json_bytes(suite["models"][required_examples[path.name]]))
        example_checks.append({"path": path.relative_to(root).as_posix(),
                               "valid": validation["valid"], "matches_case_model": matches,
                               "passed": validation["valid"] and matches})

    # Contract/code/example changes invalidate the recorded report.
    paths = [BASE / "spec.json", BASE / "cases.json",
             Path("knowledge/text-model.md"),
             Path("tools/check_abstract_text_v01.py"),
             *[path.relative_to(root) for path in sorted((root / "tools/models").glob("*.py"))],
             *[path.relative_to(root) for path in example_paths]]
    fingerprints = {path.as_posix(): text_sha256(root / path) for path in paths}
    passed = all(item["passed"] for item in results + canonical_checks + example_checks)
    return {
        "format_version": 1, "model_version": spec["model_version"],
        "authority": "Synthetic experimental observations; not a Vault grounding source or human acceptance.",
        "fingerprint_policy": "SHA-256 of UTF-8 text with checkout CRLF/CR normalized to LF; model content is unchanged.",
        "inputs": fingerprints,
        "coverage": {rule: [case["id"] for case in suite["cases"] if rule in case["rules"]]
                     for rule in spec["rules"]},
        "summary": {"passed": passed, "models": len(suite["models"]), "cases": len(results),
                    "case_passes": sum(item["passed"] for item in results),
                    "canonical_checks": len(canonical_checks), "example_checks": len(example_checks)},
        "cases": results, "canonical_checks": canonical_checks, "examples": example_checks,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="reproduce without rewriting the recorded report")
    group.add_argument("--validate", type=Path, metavar="MODEL.json", help="validate one local package")
    args = parser.parse_args(argv)
    try:
        if args.validate is not None:
            result = model.validate_model(read_json(args.validate))
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
        failures = [case["id"] for case in report["cases"] if not case["passed"]]
        if failures:
            print("Failed cases: " + ", ".join(failures))
        return 0 if report["summary"]["passed"] else 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Abstract Text Model 0.1 check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
