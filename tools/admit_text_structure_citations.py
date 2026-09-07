"""Admit two citation-only threads from the locked local GitHub snapshot.

Raw discussion bodies stay local. The bibliography and manifest publish only
metadata and the selected short quotations, checked against exact raw hashes.
Run this module to admit, then tools/check_wave1_sources.py with the emitted
manifest and references to recheck quotations independently of generation.
"""

import argparse
import json
from pathlib import Path

import yaml

from tools.check_wave1_sources import extract_text, read_raw
from tools.ingest_git_blobs import _now, immutable_output, sha256

MANIFEST = "sources/manifests/2026-09-07-text-structures-citations.yaml"
REFERENCES = "references/text-structures-run1.json"
LOCK = "sources/locks/github-teic-tei.yaml"
UPSTREAM = "sources/manifests/2026-09-06-github-teic-tei-work-items.yaml"
SNAPSHOTS = {
    1400: (
        ("709a304213a1d99ebc2c40f0f88f12fbcf1def6c5d51bcbe864b3da391166706", 5650, "2026-09-06T09:49:41Z"),
        ("353f14b878797d99214dc96697bd164ee766c02b2274ce91ccf585b2f89becea", 43795, "2026-09-06T09:49:41Z"),
    ),
    1505: (
        ("8d022744959aa659ab5728500e55b0a758a15dc0a38d553a3167c97cf648f643", 8229, "2026-09-06T09:52:18Z"),
        ("2687ed9729186eb5de58681ddcbb283797959861e26203c1c71951b1b07a1aa2", 28589, "2026-09-06T09:52:19Z"),
    ),
}
QUOTES = {
    1400: (
        ("I propose that it be removed in the next major release.", "issue description, 2015-11-10"),
        ("Makes human editing much much easier", "comment 4, 2015-11-10, issuecomment-155582272"),
        ("Status: Reconsider for P6", "issue labels at the 2026-09-06 snapshot"),
    ),
    1505: (
        ("they must always point to elements of the same type", "comment 2, 2016-09-26, issuecomment-249580507"),
        ("Have added recommendation in the classSpec and in the text of the Guidelines.", "comment 14, 2017-05-03, issuecomment-298975299"),
    ),
}
RIGHTS = (
    "Citation and checked short quotation only. Full issue and comment bodies remain "
    "in ignored raw storage; repository licensing does not license participant discussion text."
)


def response(number: int, index: int) -> dict:
    digest, size, observed = SNAPSHOTS[number][index]
    url = f"https://api.github.com/repos/TEIC/TEI/issues/{number}"
    if index:
        url += "/comments?per_page=100"
    return {
        "requested_url": url, "canonical_url": url, "final_url": url,
        "observed_at": observed, "status": 200, "media_type": "application/json",
        "byte_count": size, "sha256": digest, "raw_path": f"sha256/{digest[:2]}/{digest[2:]}",
    }


def admit(root: Path, *, check: bool = False) -> None:
    existing_path = root / MANIFEST
    prior = yaml.safe_load(existing_path.read_text(encoding="utf-8")) if existing_path.exists() else {}
    started = prior.get("started_at") or _now()
    admissions, bibliography, requests = [], [], []
    for number in SNAPSHOTS:
        issue_response, comments_response = (response(number, index) for index in (0, 1))
        issue_bytes, comments_bytes = (read_raw(root, item) for item in (issue_response, comments_response))
        issue, comments = json.loads(issue_bytes), json.loads(comments_bytes)
        if issue["number"] != number or len(comments) != issue["comments"]:
            raise ValueError(f"thread identity or comment boundary mismatch: {number}")
        quoted_sources = [
            {"part": "issue-body", "response": issue_response, "extraction": {"kind": "json-field", "path": ["body"]}},
            {"part": "comments-page-1", "response": comments_response, "extraction": {"kind": "json-field", "path": ["*", "body"]}},
            {"part": "issue-labels", "response": issue_response, "extraction": {"kind": "json-field", "path": ["labels", "*", "name"]}},
        ]
        text = "\n\n".join(extract_text(read_raw(root, item["response"]), item["extraction"]) for item in quoted_sources)
        for quote, _ in QUOTES[number]:
            if quote not in text:
                raise ValueError(f"quotation not found in locked thread {number}: {quote}")
        reference = f"teic-tei-issue-{number}"
        bibliography.append({
            "id": reference, "type": "post", "title": issue["title"], "number": str(number),
            "container-title": "TEIC/TEI GitHub issues", "publisher": "TEI Consortium",
            "issued": {"date-parts": [[int(part) for part in issue["created_at"][:10].split("-")]]},
            "accessed": {"date-parts": [[2026, 9, 6]]}, "URL": issue["html_url"],
            "note": f"Citation-only thread admission from the locked 2026-09-06 REST snapshot; {len(comments)} comments. "
                    "Participant statements and issue labels are dated records, not evidence of adoption or released effect. " + RIGHTS,
        })
        admissions.append({
            "reference_id": reference, "source_type": "publication", "source_id": "github-teic-tei-work-items",
            "lock_file": LOCK,
            "work_item": {
                "number": number, "kind": "issue", "state": issue["state"],
                "created_at": issue["created_at"], "closed_at": issue["closed_at"],
                "comment_count": len(comments), "labels": [label["name"] for label in issue["labels"]],
                "html_url": issue["html_url"],
            },
            "snapshots": quoted_sources, "rights": RIGHTS,
            "authority": "Participant proposals and implementation self-reports; source-state labels establish only their recorded state.",
            "instruction_trust": "none",
            "quotes": [{"text": quote, "locator": locator} for quote, locator in QUOTES[number]],
            "distillate_path": f"20_distillates/publications/{reference}.md",
        })
        requests.extend((issue_response, comments_response))
    references = (json.dumps(bibliography, ensure_ascii=False, indent=2) + "\n").encode()
    manifest = {
        "schema_version": 1, "run_id": "2026-09-07-text-structures-citations",
        "source_id": "github-teic-tei-work-items", "status": "bounded-complete",
        "started_at": started, "finished_at": prior.get("finished_at") or _now(),
        "scope": {"boundary": "Issues 1400 and 1505, issue bodies, labels and their single comment pages from the locked REST snapshot.",
                  "status_applies_to": "the two selected citation-only admissions and four raw responses only"},
        "adapter": {"name": "tools.admit_text_structure_citations", "version": 1},
        "references_path": REFERENCES, "lock_file": LOCK, "upstream_manifests": [UPSTREAM],
        "objects": [{"kind": "csl-json-bibliography", "path": REFERENCES, "sha256": sha256(references)}],
        "admissions": admissions, "requests": requests,
        "counts": {"admitted_sources": 2, "raw_snapshots": 4, "checked_quotes": 5},
        "gaps": [], "rights_exceptions": [], "instruction_trust": "none",
    }
    immutable_output(root / REFERENCES, references, check)
    immutable_output(root / MANIFEST, yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True).encode(), check)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    admit(args.root, check=args.check)
    print("OK: two citation-only threads and five short quotations reconcile")


if __name__ == "__main__":
    main()
