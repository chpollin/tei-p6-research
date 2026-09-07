---
title: Handoff
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-07"
related: [INDEX, state, plan]
---

# Handoff

## Unvollständiger Waybackabruf des Brown-TEI-L-Archivs

- Received: 2026-09-06
- Source: background run started from the session of 2026-09-06 at 14:38 local time over all 368 captured months, with `--delay-seconds 0.5`; the exact command was `python -m tools.corpus.listserv_snapshot wayback-fetch --coverage-input corpus/normalized/mail/tei-l-wayback-coverage.jsonl --delay-seconds 0.5 --normalized-output corpus/normalized/mail/tei-l-wayback.jsonl --manifest-output sources/manifests/2026-09-06-tei-l-wayback.yaml`
- Target: `corpus/normalized/mail/tei-l-wayback.jsonl` and `sources/manifests/2026-09-06-tei-l-wayback.yaml`, then the TEI-L rows of [[knowledge/state]] and the lock `sources/locks/tei-l-archive.yaml`
- Context: Der Lauf schreibt normalisierte Ausgabe und Manifest erst am Ende und besitzt keine Wiederaufnahmefunktion. Beim Abschluss am 2026-09-07 fehlen beide genannten Ergebnisdateien; ein passender lokaler Pythonprozess wurde nicht gefunden. Der damalige Abruf wird daher nicht als weiterlaufender Job übergeben. Bereits geladene Seiten können im lokalen Rohdatenspeicher liegen. Der Test eines Monats hatte index-only-Einträge ohne einzelne Nachrichtenaufnahme gezeigt.
- Next action: if the manifest exists, add it to the lock, update the state rows, run the control-plane check and commit; if it does not, give `wayback-fetch` a resume that skips months whose index and message pages are already in the raw store, test it, and re-run the command

## Revisionsabhängigkeiten des Modells 0.2

- Received: 2026-09-07
- Source: GPT-6-Modellprüfung und vom Integrator wiederholte In-Memory-Gegenproben, `workbench/reviews/2026-09-07-abstract-proposal/README.md`
- Target: `tools/models/entities.py`, `tools/models/identity_evidence.py` und ihre Verträge in `knowledge/text-model.md` und `knowledge/identity-evidence.md`
- Context: Unveränderte Claim-Records können durch geänderte Selektionen oder versetzte Alignment-Träger eine andere Bedeutung erhalten. Der allgemeine 0.2-Revisionscheck verhindert auch keine Änderung des konstitutiven Entity-kind. Das Quellenprofil schützt kind und Herkunftsdeskriptoren, jedoch keine vollständige Beleggeschichte. Kapitel 02 und die Verträge nennen diese Grenzen jetzt ausdrücklich.
- Evidence: Ein Beleg im Katalog-Dossier ließ sich auf den gleichlautenden Werkverweis des zweiten Eintrags umleiten. Beide Profilprüfungen akzeptierten die Änderung. Im Entitätenbeispiel passierten ein kind-Wechsel und der Wechsel eines Alignment-Trägers ebenfalls beide Prüfungen.
- Next action: Den Schutz unveränderter Referenzbedeutung und impliziter Claim-Gegenstände spezifizieren, dann die Gegenfälle als Regressionstests aufnehmen und die Revisionsprüfungen entsprechend erweitern. Die Ausformulierung des Proposals hat diese Modelländerung nicht vorgenommen.
