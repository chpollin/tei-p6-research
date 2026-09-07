"""Build or reproduce the bounded catalogue/correspondence attribution experiment.

Run `python -m tools.check_identity_evidence`, then `--check`. The mapper is
deliberately restricted to protocol.json; it is not a general TEI converter.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path

from tools.check_abstract_text_v01 import json_bytes, text_sha256
from tools.ingest_identity_evidence import BASE, ROOT, digest, snapshots
from tools.models import identity_evidence as profile
from tools.models.abstract_text import COLLECTIONS, validate_model
from tools.models.entities import NEW_COLLECTIONS


def _span(content: str, tag: str) -> tuple[int, int]:
    matches = list(re.finditer(r"<" + tag + r"\b[^>]*>[\s\S]*?</" + tag + ">", content))
    if len(matches) != 1:
        raise ValueError(f"expected one {tag}")
    return matches[0].span()


def build_dossier(intake: dict) -> dict:
    package = {key: [] for key in (*COLLECTIONS, *NEW_COLLECTIONS)}
    package.update({"model_version": "0.2", "concepts": copy.deepcopy(list(profile.RESERVED_CONCEPTS)),
                    "agents": [{"id": "ie-importer", "label": "GPT-6 source import; no individual source authorship inferred"}]})
    dossier = {"profile": profile.PROFILE, "package": package, "sources": []}
    instant = intake["finished_at"]
    for source in intake["sources"]:
        for fragment in source["fragments"]:
            version = fragment["id"]
            package["versions"].append({"id": version, "content": fragment["xml"],
                                         "sha256": fragment["sha256"], "parents": []})
            dossier["sources"].append({"version": version, "snapshot": source["id"],
                                       "uri": source["url"], "sha256": source["sha256"],
                                       "start_byte": fragment["start_byte"], "end_byte": fragment["end_byte"],
                                       "xpath": fragment["xpath"]})
    package["entities"] = [
        {"id": "artifact-w21", "kind": "object", "label": "SZ-AAP/W2.1"},
        {"id": "artifact-w22", "kind": "object", "label": "SZ-AAP/W2.2"},
        {"id": "work-szdwrk2", "kind": "other", "label": "Catalogue work reference #SZDWRK.2"},
        {"id": "person-lotte", "kind": "person", "label": "Lotte Zweig, as named in the selected record"},
        {"id": "hsa-letter", "kind": "object", "label": "HSA letter 4493"},
    ]
    versions = {item["id"]: item["content"] for item in package["versions"]}

    def annotation(identifier: str, version: str, start: int, end: int, concept: str) -> str:
        body = versions[version][start:end]
        selection = "selection-" + identifier
        package["selections"].append({"id": selection, "version": version,
                                      "selector": {"kind": "ranges", "segments": [{"start": start, "end": end, "quote": body}]}})
        package["annotations"].append({"id": identifier, "agent": "ie-importer", "created": instant,
                                       "status": "asserted", "selection": selection, "body": body, "concept": concept})
        return identifier

    def report(identifier: str, concept: str, version: str, span: tuple[int, int],
               participants: list[tuple[str, str]], value: str) -> None:
        package["statements"].append({"id": identifier, "agent": "ie-importer", "created": instant,
                                      "status": "asserted", "kind": "relation", "type": concept,
                                      "participants": [{"entity": entity, "role": role} for entity, role in participants],
                                      "value": value})
        passage = annotation("passage-" + identifier, version, *span, profile.PASSAGE)
        package["relations"].append({"id": "support-" + identifier, "agent": "ie-importer",
                                     "created": instant, "status": "asserted", "type": profile.SUPPORT,
                                     "source": identifier, "target": passage})

    for number, artifact in ((3, "artifact-w21"), (4, "artifact-w22")):
        version = f"szd-record-{number}"
        content = versions[version]
        matches = list(re.finditer(r'<term\b[^>]*type="work"[^>]*>[\s\S]*?</term>', content))
        if len(matches) != 1 or 'ref="#SZDWRK.2"' not in matches[0].group():
            raise ValueError("selected work reference changed")
        report(f"szd-work-{number}", profile.WORK, version, matches[0].span(),
               [(artifact, "artifact"), ("work-szdwrk2", "work")], "#SZDWRK.2")
    hand_span = _span(versions["szd-record-3"], "handDesc")
    report("szd-hand", profile.HAND, "szd-record-3", hand_span,
           [("artifact-w21", "artifact"), ("person-lotte", "attributed-person")], "Lotte Zweig (?)")
    report("szd-contributor", profile.CONTRIBUTOR, "szd-record-3", _span(versions["szd-record-3"], "editor"),
           [("artifact-w21", "artifact"), ("person-lotte", "contributor")], "contributor")
    position = versions["szd-record-3"].index("(?)", hand_span[0], hand_span[1])
    qualifier = annotation("qualification-hand", "szd-record-3", position, position + 3, profile.QUALIFICATION)
    package["relations"].append({"id": "qualifies-hand", "agent": "ie-importer", "created": instant,
                                 "status": "asserted", "type": profile.QUALIFIES,
                                 "source": "szd-hand", "target": qualifier})
    report("hsa-origin", profile.ORIGIN, "hsa-source-description",
           _span(versions["hsa-source-description"], "origDate"), [("hsa-letter", "letter")], "1878-04-17")
    report("hsa-sent", profile.SENT, "hsa-correspondence",
           _span(versions["hsa-correspondence"], "date"), [("hsa-letter", "letter")], "1878-04-17")
    report("hsa-dateline-report", profile.DATELINE, "hsa-dateline", (0, len(versions["hsa-dateline"])),
           [("hsa-letter", "letter")], "Graz 17. 4. 78.")
    return dossier


def synthetic_identity_cases() -> list[dict]:
    """Declared policies over invented strings; none describes an acquired witness."""
    cases = []
    for identifier, strings, grouped, criterion in (
        ("corrected-transcription", ("Wortlaut A", "Wortlaut B"), True,
         "Same selected editorial unit and witness; a documented transcription correction."),
        ("diplomatic-and-normalized", ("daß", "dass"), True,
         "Same selected editorial unit and witness under two declared rendering policies."),
        ("equal-content-distinct-witnesses", ("gleiche Zeichen", "gleiche Zeichen"), False, ""),
        ("draft-and-sent-not-automatically-grouped", ("Entwurf", "Ausfertigung"), False, ""),
    ):
        package = {key: [] for key in COLLECTIONS}
        package.update({"model_version": "0.1", "agents": [{"id": "editor", "label": "Synthetic editor"}]})
        package["versions"] = [{"id": f"v{index}", "content": content, "sha256": digest(content.encode("utf-8")),
                                 "parents": []} for index, content in enumerate(strings)]
        if grouped:
            package["texts"] = [{"id": "text", "label": "Declared editorial unit"}]
            package["continuities"] = [{"id": "continuity", "text": "text", "versions": ["v0", "v1"],
                                         "agent": "editor", "criterion": criterion}]
        outcome = validate_model(package)
        cases.append({"id": identifier, "synthetic": True, "package": package,
                      "expected_grouped": grouped, "passed": outcome["valid"]
                      and bool(package["continuities"]) == grouped
                      and len({item["id"] for item in package["versions"]}) == 2})
    return cases


def outputs(root: Path = ROOT) -> dict[Path, bytes]:
    intake, source_bytes = snapshots(root)
    dossier = build_dossier(intake)
    validation = profile.validate_profile(dossier, source_bytes)
    if not validation["valid"]:
        raise ValueError(validation["diagnostics"])
    views = {item["id"]: profile.inspect_claim(dossier, item["id"], source_bytes)
             for item in dossier["package"]["statements"]}
    synthetic = synthetic_identity_cases()
    reports = {item["id"]: item for item in dossier["package"]["statements"]}
    observations = {
        "distinct_artifacts_share_only_a_reported_work":
            reports["szd-work-3"]["participants"][0] != reports["szd-work-4"]["participants"][0]
            and reports["szd-work-3"]["participants"][1] == reports["szd-work-4"]["participants"][1]
            and not dossier["package"]["continuities"],
        "hand_question_mark_preserved_without_importer_certainty":
            views["szd-hand"]["qualifications"][0]["annotation"]["body"] == "(?)"
            and "certainty" not in reports["szd-hand"],
        "contribution_and_hand_have_separate_claims_and_passages":
            views["szd-hand"]["passages"] != views["szd-contributor"]["passages"],
        "dateline_origin_and_sent_have_separate_contexts":
            len({views[item]["passages"][0]["origin"]["xpath"]
                 for item in ("hsa-origin", "hsa-sent", "hsa-dateline-report")}) == 3,
        "dates_are_present_in_their_own_source_passages":
            all(reports[item]["value"] in views[item]["passages"][0]["annotation"]["body"]
                for item in ("hsa-origin", "hsa-sent", "hsa-dateline-report")),
    }
    false_claim = copy.deepcopy(dossier)
    false_claim["package"]["statements"][2]["value"] = "This unsupported historical conclusion remains structurally valid."
    observations["structural_validity_does_not_detect_false_interpretation"] = profile.validate_profile(false_claim, source_bytes)["valid"]
    fingerprints = (BASE / "protocol.json", Path("knowledge/identity-evidence.md"),
                    Path("tools/models/identity_evidence.py"), Path("tools/check_identity_evidence.py"),
                    Path("tools/ingest_identity_evidence.py"))
    report = {"profile": profile.PROFILE, "authority": "Source fidelity and contract execution; no independent source-support review or human verification.",
              "inputs": {path.as_posix(): text_sha256(root / path) for path in fingerprints},
              "source_snapshots": {source["id"]: source["sha256"] for source in intake["sources"]},
              "observations": observations, "claims": views,
              "synthetic_identity_cases": [{key: value for key, value in case.items() if key != "package"} for case in synthetic],
              "passed": all(observations.values()) and all(case["passed"] for case in synthetic),
              "limits": json.loads((root / BASE / "protocol.json").read_text(encoding="utf-8"))["limits"]}
    return {BASE / "dossier.json": json_bytes(dossier), BASE / "identity-cases.json": json_bytes(synthetic),
            BASE / "report.json": json_bytes(report)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated = outputs()
    for path, payload in generated.items():
        destination = ROOT / path
        if args.check:
            if not destination.exists() or destination.read_bytes() != payload:
                raise ValueError(f"experiment does not reproduce: {path}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
    report = json.loads(generated[BASE / "report.json"])
    print(json.dumps({"passed": report["passed"], "source_reports": len(report["claims"]),
                      "observations": len(report["observations"]), "synthetic_identity_cases": 4}))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
