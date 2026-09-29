"""Check complete current V1 coverage and its separately executed blind sample.

Public seals bind material and recorded judgments. Rechecking private prompts
and original model responses requires tools.full_review check in the local vault.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path

from tools.full_review import check_seal, digest, read_json

DIRECTORY = Path("workbench/reviews/2026-09-11-v1")
PRIMARY = DIRECTORY / "primary-seal.json"
SECOND = DIRECTORY / "second-seal.json"


def sample_ids(primary: dict) -> set[str]:
    selected = {v["id"] for v in primary["verdicts"] if v["verdict"] != "fully supports"}
    groups: dict[str, list[str]] = {}
    for verdict in primary["verdicts"]:
        if verdict["verdict"] == "fully supports":
            groups.setdefault(verdict["id"].split("::", 1)[0], []).append(verdict["id"])
    for ids in groups.values():
        ids.sort(key=lambda identifier: digest("20260911-v1-second-review\n" + identifier))
        selected.update(ids[:max(2, math.ceil(len(ids) / 10))])
    return selected


def check(root: Path, primary_path: Path = PRIMARY, second_path: Path = SECOND) -> dict:
    primary_path, second_path = root / primary_path, root / second_path
    primary, second = read_json(primary_path), read_json(second_path)
    if primary.get("scope_ids") is not None:
        raise ValueError("primary review must cover all current scholarly documents")
    first_check = check_seal(primary_path, root)
    second_check = check_seal(second_path, root)
    if not first_check["all_support"] or not second_check["all_support"]:
        raise ValueError("current review has missing, nonpassing or context-gap units")
    if set(second.get("scope_ids") or []) != sample_ids(primary):
        raise ValueError("second review does not match the prospectively declared sample")
    if second.get("reused_packages"):
        raise ValueError("blind second review may not reuse earlier judgments")
    if second["instrument_files"] != primary["instrument_files"]:
        raise ValueError("first and second reviews use different instruments")
    first = {v["id"]: v for v in primary["verdicts"]}
    for verdict in second["verdicts"]:
        identifier = verdict["id"]
        if second["unit_hashes"][identifier] != primary["unit_hashes"][identifier]:
            raise ValueError("blind review prompt differs from the primary prompt")
        if verdict["outcome_sha256"] == first[identifier]["outcome_sha256"]:
            raise ValueError("second review repeats the primary model response")
    for record in (primary, second):
        if record.get("human_verified") is not False:
            raise ValueError("machine review cannot declare human verification")
        if any(v["requested_model"] != "opus" or "opus" not in v["model"].lower()
               for v in record["verdicts"]):
            raise ValueError("review does not conform to the explicit Opus model policy")
    return {"primary_units": first_check["units"], "second_units": second_check["units"],
            "counts": dict(Counter(identifier.split("::", 1)[0] for identifier in first)),
            "all_support": True, "human_verified": False,
            "bounded_contexts": first_check["bounded_contexts"],
            "boundary": first_check["boundary"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path.cwd())
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.root)))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("FAIL:", error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
