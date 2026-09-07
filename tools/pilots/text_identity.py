"""Compare two version-bound selectors on synthetic finite Unicode strings.

This is an independent modeling hypothesis, not a TEI converter or ontology.
All public operations return fresh JSON-compatible results and never mutate
their inputs. No Unicode normalization or interpretation transfer is inferred.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
INPUTS = (
    "knowledge/experiments.md",
    "experiments/text_identity/spec.json",
    "experiments/text_identity/cases.json",
    "tools/__init__.py",
    "tools/pilots/__init__.py",
    "tools/pilots/text_identity.py",
)
REPORT = "experiments/text_identity/report.json"
CONTRACT_HEADING = "## Text identity and annotation pilot"
DIAGNOSTICS = {
    "E_SHAPE", "E_ID", "E_DUPLICATE_ID", "E_REFERENCE", "E_OWNERSHIP",
    "E_HASH", "E_CYCLE", "E_SELECTOR", "E_BOUNDS", "E_QUOTE",
    "E_NO_MATCH", "E_AMBIGUOUS", "E_REANCHOR",
}


def text_hash(content: str) -> str:
    """Hash exact UTF-8 bytes; reject lone surrogates through model validation."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _string(value: Any) -> bool:
    return _unicode(value) and bool(value)


def _unicode(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        value.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def _finish(errors: list[dict[str, str]], resolutions: dict) -> dict:
    return {
        "diagnostics": sorted(errors, key=lambda row: (row["path"], row["code"])),
        "resolutions": resolutions,
    }


def quote_candidates(content: str, quote: str, prefix: str = "", suffix: str = "") -> list[dict[str, int]]:
    """Find every literal match, including overlapping occurrences."""
    if not quote:
        return []
    candidates = []
    offset = 0
    while (start := content.find(quote, offset)) >= 0:
        end = start + len(quote)
        if content[:start].endswith(prefix) and content[end:].startswith(suffix):
            candidates.append({"start": start, "end": end})
        offset = start + 1
    return candidates


def validate_model(model: Any) -> dict:
    """Validate identity/references first, then resolve independently per region.

    Structural errors suppress all resolution. Selector failures suppress only
    that region. Diagnostics carry stable codes and object paths.
    """
    errors: list[dict[str, str]] = []

    def error(code: str, path: str) -> None:
        errors.append({"code": code, "path": path})

    kinds = ("texts", "versions", "regions", "annotations")
    if not isinstance(model, dict) or set(model) != set(kinds):
        return _finish([{"code": "E_SHAPE", "path": "model"}], {})
    indexes: dict[str, dict[str, dict]] = {kind: {} for kind in kinds}
    seen: set[str] = set()
    for kind in kinds:
        if not isinstance(model[kind], list):
            error("E_SHAPE", kind)
            continue
        for number, item in enumerate(model[kind]):
            path = f"{kind}[{number}]"
            if not isinstance(item, dict):
                error("E_SHAPE", path)
                continue
            identifier = item.get("id")
            if not _string(identifier):
                error("E_ID", path)
                continue
            if identifier in seen:
                error("E_DUPLICATE_ID", path)
                continue
            seen.add(identifier)
            indexes[kind][identifier] = item
    if errors:
        return _finish(errors, {})

    texts, versions, regions, annotations = (indexes[kind] for kind in kinds)

    def reference(value: Any, target: dict, path: str) -> bool:
        if not _string(value) or value not in target:
            error("E_REFERENCE", path)
            return False
        return True

    for identifier, item in texts.items():
        if set(item) != {"id"}:
            error("E_SHAPE", f"texts/{identifier}")
    for identifier, item in versions.items():
        path = f"versions/{identifier}"
        if not {"id", "text", "content", "sha256"} <= set(item) or set(item) - {"id", "text", "content", "sha256", "parent"}:
            error("E_SHAPE", path)
        reference(item.get("text"), texts, path + "/text")
        if not _unicode(item.get("content")):
            error("E_SHAPE", path + "/content")
        elif item.get("sha256") != text_hash(item["content"]):
            error("E_HASH", path + "/sha256")
        if ("parent" in item and reference(item["parent"], versions, path + "/parent")
                and versions[item["parent"]].get("text") != item.get("text")):
            error("E_OWNERSHIP", path + "/parent")
    for identifier, item in regions.items():
        path = f"regions/{identifier}"
        if set(item) != {"id", "version", "selector"}:
            error("E_SHAPE", path)
        reference(item.get("version"), versions, path + "/version")
    for identifier, item in annotations.items():
        path = f"annotations/{identifier}"
        if set(item) != {"id", "region", "body"} or not _string(item.get("body")) or not _unicode(item.get("body")):
            error("E_SHAPE", path)
        reference(item.get("region"), regions, path + "/region")
    if errors:
        return _finish(errors, {})

    # Iterative ancestry traversal avoids recursion limits on finite chains.
    finished: set[str] = set()
    for identifier in versions:
        current = identifier
        chain: set[str] = set()
        while current not in finished:
            if current in chain:
                error("E_CYCLE", f"versions/{current}/parent")
                break
            chain.add(current)
            parent = versions[current].get("parent")
            if parent is None:
                break
            current = parent
        finished.update(chain)
    if errors:
        return _finish(errors, {})

    resolutions = {}
    for identifier, item in regions.items():
        path = f"regions/{identifier}/selector"
        selector = item["selector"]
        if not isinstance(selector, dict):
            error("E_SELECTOR", path)
            continue
        kind = selector.get("kind")
        quote = selector.get("quote")
        if not _string(quote) or not _unicode(quote):
            error("E_SELECTOR", path)
            continue
        content = versions[item["version"]]["content"]
        if kind == "A":
            if set(selector) != {"kind", "start", "end", "quote"}:
                error("E_SELECTOR", path)
                continue
            start, end = selector["start"], selector["end"]
            if type(start) is not int or type(end) is not int or not 0 <= start < end <= len(content):
                error("E_BOUNDS", path)
                continue
            if content[start:end] != quote:
                error("E_QUOTE", path)
                continue
        elif kind == "B":
            if set(selector) - {"kind", "quote", "prefix", "suffix"} or not all(_unicode(selector.get(key, "")) for key in ("prefix", "suffix")):
                error("E_SELECTOR", path)
                continue
            matches = quote_candidates(content, quote, selector.get("prefix", ""), selector.get("suffix", ""))
            if len(matches) != 1:
                error("E_NO_MATCH" if not matches else "E_AMBIGUOUS", path)
                continue
            start, end = matches[0]["start"], matches[0]["end"]
        else:
            error("E_SELECTOR", path)
            continue
        resolutions[identifier] = {"version": item["version"], "start": start, "end": end, "quote": quote}
    return _finish(errors, resolutions)


def propose_reanchor(model: Any, request: Any) -> dict:
    """Return candidates in a chosen version, never an accepted annotation.

    A retains its quote; B retains its quote and literal context. Same-text
    ownership is required, but the target need not be a direct descendant.
    """
    invalid = {"diagnostics": ["E_REANCHOR"], "proposal": None}
    if not isinstance(request, dict) or set(request) != {"region", "target_version"}:
        return invalid
    if not all(_string(request[key]) for key in request):
        return invalid
    validated = validate_model(model)
    if validated["diagnostics"] or request["region"] not in validated["resolutions"]:
        return invalid
    versions = {item["id"]: item for item in model["versions"]}
    if request["target_version"] not in versions:
        return invalid
    region = next(item for item in model["regions"] if item["id"] == request["region"])
    source, target = versions[region["version"]], versions[request["target_version"]]
    if source["text"] != target["text"]:
        return invalid
    selector = region["selector"]
    matches = quote_candidates(target["content"], selector["quote"], selector.get("prefix", ""), selector.get("suffix", ""))
    return {
        "diagnostics": [],
        "proposal": {
            "region": region["id"], "source_version": region["version"],
            "target_version": target["id"], "candidates": matches,
            "status": "absent" if not matches else "unique" if len(matches) == 1 else "ambiguous",
            "accepted": False,
        },
    }


def evaluate_case(case: dict) -> dict:
    result = validate_model(case.get("model"))
    actual = {
        "diagnostics": sorted({row["code"] for row in result["diagnostics"]}),
        "resolutions": result["resolutions"],
    }
    if "reanchor" in case:
        actual["reanchor"] = propose_reanchor(case.get("model"), case["reanchor"])
    # JSON distinguishes booleans from numbers, unlike Python equality.
    # Canonical serialization also makes object-key ordering irrelevant.
    passed = json.dumps(actual, sort_keys=True, ensure_ascii=True) == json.dumps(
        case.get("expected"), sort_keys=True, ensure_ascii=True
    )
    return {"id": case["id"], "passed": passed, "actual": actual, "details": result["diagnostics"]}


def input_fingerprints(root: Path) -> dict[str, str]:
    fingerprints = {}
    for name in INPUTS:
        content = (root / name).read_bytes()
        if name == "knowledge/experiments.md":
            text = content.decode("utf-8").replace("\r\n", "\n")
            marker = "\n" + CONTRACT_HEADING + "\n"
            if text.count(marker) != 1:
                raise ValueError("text identity contract heading missing or ambiguous")
            section = text.split(marker, 1)[1].split("\n## ", 1)[0]
            content = (CONTRACT_HEADING + "\n" + section.rstrip() + "\n").encode("utf-8")
        fingerprints[name] = hashlib.sha256(content).hexdigest()
    return fingerprints


def build_report(root: Path = ROOT) -> dict:
    spec = json.loads((root / INPUTS[1]).read_text(encoding="utf-8"))
    cases = json.loads((root / INPUTS[2]).read_text(encoding="utf-8"))
    if not isinstance(spec, dict) or type(spec.get("format_version")) is not int or spec.get("format_version") != 1 or not isinstance(spec.get("diagnostics"), dict) or set(spec["diagnostics"]) != DIAGNOSTICS:
        raise ValueError("specification version or diagnostic vocabulary mismatch")
    if not isinstance(cases, dict) or type(cases.get("format_version")) is not int or cases.get("format_version") != 1 or not isinstance(cases.get("cases"), list) or not cases["cases"]:
        raise ValueError("expected a nonempty version-1 case suite")
    identifiers = set()
    for case in cases["cases"]:
        if not isinstance(case, dict) or not _string(case.get("id")) or case["id"] in identifiers or not isinstance(case.get("expected"), dict):
            raise ValueError("malformed case or duplicate case identity")
        identifiers.add(case["id"])
    results = [evaluate_case(case) for case in cases["cases"]]
    return {
        "format_version": 1,
        "scope": "Synthetic finite modeling experiment; not P5 conversion or ontological evidence.",
        "inputs": input_fingerprints(root),
        "input_scopes": {"knowledge/experiments.md": CONTRACT_HEADING},
        "summary": {"cases": len(results), "passed": sum(row["passed"] for row in results)},
        "cases": results,
    }


def report_bytes(report: dict) -> bytes:
    return (json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated report differs from checked-in bytes")
    args = parser.parse_args()
    try:
        report = build_report()
        content = report_bytes(report)
        path = ROOT / REPORT
        if report["summary"]["passed"] != report["summary"]["cases"]:
            failures = [case["id"] for case in report["cases"] if not case["passed"]]
            print("FAIL: case expectation mismatch: " + ", ".join(failures))
            return 1
        if args.check:
            if not path.exists() or path.read_bytes() != content:
                print("FAIL: report drift; run python -m tools.pilots.text_identity")
                return 1
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        print(f"OK: {report['summary']['cases']} synthetic cases; report {'matches' if args.check else 'generated'}")
        return 0
    except (OSError, ValueError, TypeError, RecursionError) as error:
        print(f"FAIL: invalid experiment inputs: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
