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
updated: "2026-10-17"
related: [INDEX, state, plan]
---

# Handoff

## Wiederaufnahme: Vollprüfung V1 und gezielte Quellenaufnahme

- Received: 2026-09-11
- Source: Der damalige Nutzerauftrag vom 11.09.2026 wurde am 17.10.2026 durch einen direkten Auftrag zur Fortsetzung der fehlenden V1-Prüfungen und der blinden Zweitprüfung konkretisiert. Empfang und Rückgabe stehen in der privaten TEI-P6-Operator-Datei.
- Target: [[knowledge/state]], [[knowledge/plan]] § Meilenstein V1 und [eingefrorener Prüfbestand](../workbench/reviews/2026-09-11-data-and-verification/).
- Context: Der September-Arbeitsstand ist mit `749c7b1` auf `main` gesichert. Die vorbereitete, noch uncommittete Übergabebaseline vom 17.10.2026 umfasst die geprüften Folgekorrekturen und die öffentlichen Reviewrecords. Vor jeder Fortsetzung den tatsächlichen Git-Stand prüfen. Vollständige lokale Reviewbelege gehören nicht zu einem Clone, ihre Zugangsgrenzen stehen in [[knowledge/verification#Portability of review evidence]]. Die fünf generierten HTML-Seiten waren bereits vor dieser Fortsetzung fremd geändert. Auf direkten Folgeauftrag wurden sie gesichert und vollständig aus einem temporären HEAD-Quellenstand reproduziert, bevor die unveränderten Generatoren die Quellenkorrekturen integriert haben. Der [Fortsetzungsbericht](../workbench/reviews/2026-10-17-v1-continuation/) führt die jetzigen Ergebnisse; die September-Berichte bleiben historische Belege.
- Decisions: Bestehende Quellen bleiben erhalten. Literatur wird nach konkreter Forschungsfrage, Vergleichswert und Gegenbeleg ausgewählt. V1 umfasst die bestehenden Destillate und Assertions samt Kapitelverwendung und die neu aufgenommenen P6- und Praxisquellen. Alte Pass-Urteile ersetzen den ergänzten vollständigen Durchgang nicht. Die historische Ausgangsemission bleibt unverändert nachvollziehbar.
- Result: Die aktuelle V1-Erstprüfung und die vorab festgelegte blinde Zweitstichprobe sind nach Folgekorrekturen vollständig bestanden. Lokal liegen die vollständigen Pakete unter `corpus/raw/review-contexts/2026-10-17/primary-v17-r11/` und `second-v17-r2/`; die Publikationskontexte bleiben in `corpus/raw/review-contexts/2026-09-11/all-publication-contexts-v17.json`. Die sieben geänderten Legacy-Paare sind separat ausgeführt. Beide Legacy-Checks bestehen. Der Wave-1-Prompt enthält zusätzlich kurze Originalstellen zur Rückschau auf das frühere Argument, deren Quellentreue lokal geprüft ist. Das frühere negative Urteil und die wissenschaftliche Kontextqualifikation bleiben erhalten.
- Next action: Den integrierten und technisch vollständig geprüften lokalen Stand fachlich beurteilen. Vor neuen Reviews Material-, Prompt- und Instrumenthashes erneut prüfen. Die repositoryspezifische Regel in AGENTS.md hält Projektcommits bis zu einem ausdrücklichen Auftrag zurück. Der Fortsetzungsauftrag autorisiert keinen Push, Release oder Veröffentlichung; ältere Veröffentlichungsformulierungen sind keine Freigabe innerhalb dieser Fortsetzung. Die geprüften Folgen sind im TEI-P6-Eintrag von ACTIVE-WORK, im Erledigt-Log und in der eigenen Operator-Datei zurückgeschrieben. Diese privaten Steuerdokumente sind für die Arbeit am Repository nicht erforderlich.
- Evidence: Aktuelle [Erst- und Zweitsiegel](../workbench/reviews/2026-09-11-v1/), vollständige lokale Prüfpakete und [Fortsetzungsbericht](../workbench/reviews/2026-10-17-v1-continuation/). Der Gesamtlauf und die gezielte Nachprüfung sind dort protokolliert. Historische Erstbefunde, nicht bestandene Urteile und ein zurückgewiesener fehlerhafter Antwortversuch bleiben erhalten. Kein Agent vergab `verified` oder eine fachliche Abnahme.

## Brown-TEI-L: begrenzter Produktionsabruf und Wiederaufnahme

- Received: 2026-09-06
- Source: background run started from the session of 2026-09-06 at 14:38 local time over all 368 captured months, with `--delay-seconds 0.5`; the exact command was `python -m tools.corpus.listserv_snapshot wayback-fetch --coverage-input corpus/normalized/mail/tei-l-wayback-coverage.jsonl --delay-seconds 0.5 --normalized-output corpus/normalized/mail/tei-l-wayback.jsonl --manifest-output sources/manifests/2026-09-06-tei-l-wayback.yaml`
- Target: `corpus/normalized/mail/tei-l-wayback.jsonl` and `sources/manifests/2026-09-06-tei-l-wayback.yaml`, then the TEI-L rows of [[knowledge/state]] and the lock `sources/locks/tei-l-archive.yaml`
- Context: Der damalige Lauf endete ohne normalisierte Ausgabe und Manifest. Er läuft nicht weiter; einzelne Antworten können im lokalen Rohdatenspeicher liegen. Seit 2026-09-11 besitzt `wayback-fetch` eine offline geprüfte Wiederaufnahme mit monatsweisen Checkpoints und Prüfung ihrer Rohdateien. Der frühere Abruf hatte keine Checkpoints und kann daraus keinen abgeschlossenen Monat rekonstruieren. Index-only-Einträge bleiben von aufgenommenen Nachrichtentexten getrennt.
- Result: Januar 2000 ist im Lauf `2026-09-11-tei-l-wayback-0001-v2` mit 19 Nachrichtenseiten und ohne Abruflücken innerhalb dieser Monatsgrenze abgeschlossen. `2026-09-11-tei-l-wayback-0001-v2-resumed` reproduziert die Metadaten bytegleich aus Checkpointversion 2. Beide Manifeste und der Familien-Lock sind abgeglichen. Die zwei vorherigen Pilotmanifeste dokumentieren die ursprüngliche Fehlklassifikation leerer LISTSERV-Abstandszellen; sie bleiben erhalten und werden nicht zur Abdeckung addiert.
- Next action: Bei inhaltlichem Bedarf weitere benannte Monate mit eigenen Ausgabepfaden aufnehmen. 367 Monate mit gemessenen Captures und 64 ohne Capture bleiben getrennte Lücken. Der begrenzte Produktionsabruf und der Wiederaufnahmetest sind abgeschlossen.
