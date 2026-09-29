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
updated: "2026-09-11"
related: [INDEX, state, plan]
---

# Handoff

## Wiederaufnahme: Vollprüfung V1 und gezielte Quellenaufnahme

- Received: 2026-09-11
- Source: Der Nutzer hat nach dem kontrollierten Abschluss die vollständige Umsetzung der benannten Nacharbeiten beauftragt: „mach das alles!“.
- Target: [[knowledge/state]], [[knowledge/plan]] § Meilenstein V1 und [eingefrorener Prüfbestand](../workbench/reviews/2026-09-11-data-and-verification/).
- Context: Die Refaktorierung und der Daten-/Eignungsaudit sind lokal abgeschlossen. Der gesamte Änderungsstand liegt auf `main` über `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0` uncommittet, einschließlich neuer Werkzeuge, Tests, Inventar- und Prüfdateien. Es gibt keinen Stash und keinen neuen Commit, Push oder Deployment. Vor einer weiteren Änderung `git status` prüfen und auch ungetrackte Dateien erhalten. Der [Refaktorierungsbericht](../workbench/reviews/2026-09-11-repository-refactor/) und der [Daten-/Prüfbericht](../workbench/reviews/2026-09-11-data-and-verification/) tragen Ergebnisse, Belege und Grenzen; die vollständige semantische Prüfung ist weiterhin offen.
- Decisions: Bestehende Quellen bleiben erhalten. Literatur wird nach konkreter Forschungsfrage, Vergleichswert und Gegenbeleg ausgewählt. V1 umfasst die bestehenden Destillate und Assertions samt Kapitelverwendung und die neu aufgenommenen P6- und Praxisquellen. Alte Pass-Urteile ersetzen den ergänzten vollständigen Durchgang nicht. Die historische Ausgangsemission bleibt unverändert nachvollziehbar.
- Next action: Den [ausführbaren Wiedereinstieg in V1](../workbench/reviews/2026-09-11-v1/#ausführbarer-wiedereinstieg) verwenden. Die aktuelle vollständige Emission heißt `primary-final-v17-r3`, der lokale Kontext `all-publication-contexts-v17.json`. 397 Urteile sind aktuell, 440 Einheiten und die blinde Zweitstichprobe offen. Das Opus-Sitzungslimit unterbrach die Prüfung; laut Anbieter wird es am 11. September um 19 Uhr Europe/Vienna zurückgesetzt. Es läuft kein weiterer Agent und keine automatische Wiederaufnahme. Vor jedem neuen Lauf die Material- und Instrumenthashes prüfen. Die sieben geänderten älteren Prompts benötigen eigene neue Urteile. Danach technische Regeneration und Abschlussgate sowie die bereits beauftragte Veröffentlichung durchführen; hierfür ist keine erneute Autorisierung einzuholen. Vollständige Originalkontexte und Prompts bleiben im ignorierten Rohbereich.
- Evidence: Der [aktuelle technische Prüflauf](../workbench/reviews/2026-09-11-v1/technical-checkpoint.md) endete mit 1.917 bestandenen und drei wegen fehlender aktueller Reviews fehlgeschlagenen Tests, einem Plattform-Skip und zehn bekannten RDFLib-Warnungen. Die nachfolgende Versionskorrektur bestand 24 gezielte Tests. Quellensteuerung, Reproduktionen, XML-Export und strukturelle Kapitelprüfungen bestehen. Der frühere Refaktorierungsabschluss mit 1.780 Tests und die damalige ACTIVE-WORK-Rückschreibung bleiben historische Befunde. ACTIVE-WORK, Project Overview, Repo-Verzeichnis, Projects MOC und Erledigt-Log wurden damals durch eine echte Vault-Opus-Session nachgezogen. Die jetzige V1-Fortsetzung ist dort noch nicht zurückgeschrieben. Diese Rückschreibung aus einer echten Vault-Session gehört zur nächsten Fortsetzung; der Repository-Wiedereinstieg ist vollständig gesichert.

## Brown-TEI-L: begrenzter Produktionsabruf und Wiederaufnahme

- Received: 2026-09-06
- Source: background run started from the session of 2026-09-06 at 14:38 local time over all 368 captured months, with `--delay-seconds 0.5`; the exact command was `python -m tools.corpus.listserv_snapshot wayback-fetch --coverage-input corpus/normalized/mail/tei-l-wayback-coverage.jsonl --delay-seconds 0.5 --normalized-output corpus/normalized/mail/tei-l-wayback.jsonl --manifest-output sources/manifests/2026-09-06-tei-l-wayback.yaml`
- Target: `corpus/normalized/mail/tei-l-wayback.jsonl` and `sources/manifests/2026-09-06-tei-l-wayback.yaml`, then the TEI-L rows of [[knowledge/state]] and the lock `sources/locks/tei-l-archive.yaml`
- Context: Der damalige Lauf endete ohne normalisierte Ausgabe und Manifest. Er läuft nicht weiter; einzelne Antworten können im lokalen Rohdatenspeicher liegen. Seit 2026-09-11 besitzt `wayback-fetch` eine offline geprüfte Wiederaufnahme mit monatsweisen Checkpoints und Prüfung ihrer Rohdateien. Der frühere Abruf hatte keine Checkpoints und kann daraus keinen abgeschlossenen Monat rekonstruieren. Index-only-Einträge bleiben von aufgenommenen Nachrichtentexten getrennt.
- Result: Januar 2000 ist im Lauf `2026-09-11-tei-l-wayback-0001-v2` mit 19 Nachrichtenseiten und ohne Abruflücken innerhalb dieser Monatsgrenze abgeschlossen. `2026-09-11-tei-l-wayback-0001-v2-resumed` reproduziert die Metadaten bytegleich aus Checkpointversion 2. Beide Manifeste und der Familien-Lock sind abgeglichen. Die zwei vorherigen Pilotmanifeste dokumentieren die ursprüngliche Fehlklassifikation leerer LISTSERV-Abstandszellen; sie bleiben erhalten und werden nicht zur Abdeckung addiert.
- Next action: Bei inhaltlichem Bedarf weitere benannte Monate mit eigenen Ausgabepfaden aufnehmen. 367 Monate mit gemessenen Captures und 64 ohne Capture bleiben getrennte Lücken. Der begrenzte Produktionsabruf und der Wiederaufnahmetest sind abgeschlossen.
