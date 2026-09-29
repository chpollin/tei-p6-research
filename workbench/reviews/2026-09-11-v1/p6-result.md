# V1-Arbeitspaket P6: Ergebnis

Stand 2026-09-11. Basis `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0` mit dem uncommitteten Arbeitsstand. Brief: [briefs/p6.md](briefs/p6.md). Keine Statusanhebung; alle neuen Destillate und Assertions stehen auf `grounded`, die Destillate zusätzlich mit `checked.quote: 2026-09-11`. Quelltexte wurden nur als Daten behandelt.

## Dateien dieses Pakets

| Pfad | Art |
|---|---|
| `workbench/selections/2026-09-11-p6-process.md` | Auswahlprotokoll mit Grenze, Abfragen, 23 Seitendispositionen, Repositorien und Gegenbelegen |
| `sources/manifests/2026-09-11-p6-time-for-p6-git.yaml` | Git-Beobachtung `TEIC/timeForP6` (aus dem abgebrochenen Lauf, unverändert) |
| `sources/manifests/2026-09-11-p6-council-citations.yaml` | Aufnahmemanifest, `bounded-complete`, 8 Aufnahmen, 8 Rohantworten, 42 Zitate; SHA-256 `b02fcbc9342fb11d1c8275ad9776bf4dba1d9dcd8637202339fa7ec609f7d345` |
| `sources/manifests/2026-09-11-p6-time-for-p6-readme-provenance.yaml` | Provenienznachweis README, `partial` wegen offener Lücke; SHA-256 `0a55c82c02ecaf3d67a477ebc5eb5d9fc5ba9c47a638429c6ca8d8747aa4e56a` |
| `corpus/normalized/p6-v1/fetch-2026-09-11.json`, `fetch-git-2026-09-11.json`, `teic-time-for-p6-2026-09-11.json` | Beobachtungsrecords mit Rohhashes (aus dem abgebrochenen Lauf, unverändert) |
| `references/p6-v1.json` | 8 CSL-Datensätze; SHA-256 `2bcbdd6e909996d11cad51680f5a3d14b3b08f5745d8b85c97207af6e8779f36` |
| `20_distillates/publications/p6-v1-*.md` | 8 Destillate, 42 Statements; 2 neu, 6 aus dem abgebrochenen Lauf ergänzt oder berichtigt |
| `30_assertions/p6-v1-*.md` | 6 Assertions |
| `corpus/raw/review-contexts/2026-09-11/p6-contexts.json` | lokale, git-ignorierte V1-Kontexte, `storage: local-only`; SHA-256 `644f42b997248db64a56274c6d11db5b19abd7d0cd9bba7187b01903c0505bac` |

Änderungen an Dateien des abgebrochenen Laufs: Das Würzburg-Destillat erhielt korrigierte Abschnittslocatoren für s2 bis s8, den exakten Seitentitel und das neue Statement s9. Das Kraków-Destillat erhielt Seitentitel und Überschrift in exakter Schreibung. In der Einschätzung des Destillats 2026-04-10 ist die Zuschreibung von s3 präzisiert. Eine in diesem Lauf angelegte Assertion zum Beschluss vom 2025-10-07 wurde wieder entfernt, weil ihr Anker vollständig in der P5-Feature-Assertion enthalten war (`W-DUPLICATE-GROUNDING`). Das Aufnahmeskript lag außerhalb des Repositorys unter `C:/tmp/p6_v1_intake.py`. Reproduzierbar im Repository ist der Zitatabgleich mit dem unten genannten Werkzeug.

## Aufgenommene Quellen

Alle Council-Seiten wurden am 2026-09-11 mit HTTP 200 beobachtet und sind byteidentisch mit dem Zensus vom 2026-09-04. Die Rechte erlauben nur Zitate: Seitentext und Teilnehmernamen bleiben im Rohspeicher.

| Referenz | Quelle und Version | Roh-SHA-256 | Was die Passagen belegen |
|---|---|---|---|
| `p6-v1-council-f2f-2025-09-krakow` | Council F2F Kraków, 14–16.09.2025 | `163811297f646604aa722470f9a20125d350335f98327aef00d378cdaa489e13` | Absicht und Planung, keine Beschlussmarke |
| `p6-v1-council-2025-10-07` | Teleconference 2025-10-07 | `3ff668cc05bc74a9ef582b638f50a09cd92de2101e68b696beaf60c41bcb3ced` | ausdrücklicher Council-Beschluss zu P5-Feature-Requests; Planungsdiskussion |
| `p6-v1-council-f2f-2026-03-wurzburg` | Council F2F Würzburg, 10–13.03.2026 | `0baa751e656b773808115c29c427787e352d65dafb41c83f36633d552fac8e11` | ein Beschluss (Repositorium vorerst privat), Pläne, festgehaltene Positionen |
| `p6-v1-council-2026-04-10` | Teleconference 2026-04-10 | `010e4a4a85be0e106f5bb76059d5a1f0d86e72d284b58d83192d96a09df0919e` | Vereinbarung zur Planung abwechselnder Sitzungen; Übereinstimmung zu einem Begriff; Vorschlag |
| `p6-v1-council-2026-04-24` | Teleconference 2026-04-24 | `4dd80d8287b51b3fe94321f104d388f034f4093352bd661fa427e556534555d8` | vom Protokoll erklärter Beginn der abwechselnden Agenda; Arbeitsort; offene Frage |
| `p6-v1-council-p6-2026-05-20` | P6 Teleconference 2026-05-20 | `3fa84af579066aea42788c70cf731773730ff35395f496873048df695db1706c` | Diskussionsergebnis „vorerst privat“; Absicht der Veröffentlichung |
| `p6-v1-council-p6-2026-07-16` | P6 Teleconference 2026-07-16 | `9983a27ccd01472252fc98f7f31ac94f3729832d2a7bbcfdd5dbea780a4fb553` | Diskussionsstand (Übereinstimmungs- und Dissensliste eines Teilnehmers); Repositorium für Folien angelegt |
| `p6-v1-time-for-p6-slides-eb924226` | `TEIC/timeForP6` `index.html`, Commit `eb924226d12d22599bae9dad4fc53bc748b3f121`, Blob `09dfa583120a80d5ccf071d75386cd437528ae44` | `d0382f5a749119cfa993a45562a20547adb9dcf82a588d5a5239276d6fea9a8c` | präsentierte Positionen und offene Fragen; `LICENSE` AGPL-3.0 gegen `package.json` ISC, deshalb nur Zitate |

Keine Quelle belegt eine P6-Spezifikation, Implementierung oder Releasewirkung.

## Assertions

| Assertion | Grounding | Belegart |
|---|---|---|
| `p6-v1-alternating-p5-p6-meetings-planned-and-initiated-2026` | Würzburg s9, 2026-04-10 s1, 2026-04-24 s1 | Plan, Vereinbarung, vom Protokoll erklärter Beginn |
| `p6-v1-p6-sandbox-repository-kept-private-2026` | Würzburg s5, 2026-05-20 s2 | Beschluss und Diskussionsergebnis zum jeweiligen Datum |
| `p6-v1-p6-work-located-in-teic-p6-sandbox-2026` | Würzburg s4, 2026-04-24 s3 | geplanter Schritt und angegebener Arbeitsort |
| `p6-v1-official-records-state-p6-continues-with-xml` | Kraków s4, Würzburg s2, 2026-07-16 s2, Folien s2 | festgehaltene und präsentierte Position |
| `p6-v1-recorded-positions-on-new-p5-features-differ-2025-2026` | Kraków s2, 2025-10-07 s4, Würzburg s8, 2026-04-10 s2, 2026-07-16 s7, Folien s5 | datierte, voneinander abweichende Positionen verschiedener Art |
| `p6-v1-layered-blueprint-architecture-agreement-so-far-and-possible-path` | 2026-07-16 s3, Folien s3 | Diskussionsstand und präsentierter möglicher Weg |

Die Gegenbelegabfragen C1 bis C4 im Auswahlprotokoll fanden im Rahmen keinen Widerspruch. Eine Assertion ist nicht `contested`. Die P5-Feature-Assertion beschreibt Positionen, die sich im Zeitverlauf unterscheiden, ohne sie als unvereinbar zu werten.

## Provenienz der README-Repräsentation

`10_markdown/documents/tei-time-for-p6-readme-2026-07-16.md` (SHA-256 `55440fd25a84e1c2bb92c305de3a3278f205feed1ecd372b15affb34bcff9ee1`) stammt aus `README.md` bei `eb924226`, Blob `bd4ad0759be99e8f8d8f8281ece6749c09dde9ab`.

- Die Rohantwort `ea5e6c104132575686320e7f731b9f0433915ec76062769c1b84005c357193ed` (3736 Bytes) ergibt mit `git hash-object` genau diesen Blob.
- Ohne die fünf Anker `^p6r1` bis `^p6r5` besteht der Körper aus einem führenden Zeilenumbruch, den exakten Rohbytes und zwei abschließenden Zeilenumbrüchen.
- Das Datum 2026-07-16 entspricht dem letzten README-Commit `320aaf8a51f60450b5cf856a94a05973c726e5e1`.
- Die Lizenzangabe AGPL-3.0-only entspricht `LICENSE`; `package.json` erklärt dagegen ISC.

Offen: Das deklarierte Original `00_sources/tei-time-for-p6-readme-2026-07-16.md` fehlt im Checkout. Die Wiederherstellung liegt außerhalb dieses Pakets, die Bytes sind lokal vorhanden:

```powershell
Copy-Item corpus/raw/sha256/ea/5e6c104132575686320e7f731b9f0433915ec76062769c1b84005c357193ed 00_sources/tei-time-for-p6-readme-2026-07-16.md
```

Den vorhandenen Prüfstatus des README-Destillats habe ich nicht verändert.

## P6-Sandbox

Am 2026-09-11T11:36:25Z lieferten `https://api.github.com/repos/TEIC/p6-sandbox` und `https://github.com/TEIC/p6-sandbox` unauthentifiziert HTTP 404 (Rohhashes im Aufnahmemanifest unter `p6_sandbox_observation`). Das beweist weder Existenz noch Nichtexistenz. Offizielle Protokolle verlinken in das Repositorium und halten fest, es vorerst privat zu halten.

## Ausgeführte Prüfungen

| Prüfung | Ergebnis |
|---|---|
| `python tools/check_wave1_sources.py --manifest sources/manifests/2026-09-11-p6-council-citations.yaml --references references/p6-v1.json` | `OK: 42 quotations match 8 local publication sources and distillates.` |
| `full_review.checked_contexts` mit `p6-contexts.json` gegen `review.cut_pairs` | bestanden; 42 Quellen-Pairs, alle `local-only`, keine Lücke `quote-not-in-context` oder `no-original-context`; 20 Assertion-Pairs vor Entfernung der redundanten Assertion |
| `python -m tools.corpus.validate_control_plane .` | `OK: source control plane is internally consistent` |
| `python tools/validate.py .` | 11 Fehler, 0 Warnungen: 6× `E-ORPHAN` für die neuen Assertions, 5× `E-GENERATED` für `MOC-P6 Design`, `MOC-History and Governance` und `corpus/projections/source-inventory.md`. Beides verschwindet erst nach Root-Integration über `tools/inventory.py . --write`. |

Tests wurden nicht ausgeführt, weil dieses Paket keinen Code geändert hat. Eine V1-Review der neuen Pairs wurde nicht ausgeführt.

## Für Root

1. `python tools/inventory.py . --write`, danach Validator. Die Assertions tragen bereits `topics` für `P6 Design` und `History and Governance`; die generierten MOC-Regionen nehmen sie auf.
2. Lock `sources/locks/tei-p6-process.yaml`:
   - `manifests` um `2026-09-11-p6-time-for-p6-git.yaml`, `2026-09-11-p6-council-citations.yaml` und `2026-09-11-p6-time-for-p6-readme-provenance.yaml` ergänzen.
   - Die Lücke `p6-specific-council-records-not-yet-projected` ist für 2025-01-01 bis 2026-09-04 als begrenzte Auswahl bearbeitet; die Statusentscheidung liegt bei Root.
   - Die Lücke `reported-p6-sandbox-not-publicly-observable` bleibt offen und kann die Beobachtung vom 2026-09-11 aufnehmen.
3. Die README-Originaldatei nach `00_sources/` materialisieren (Befehl oben) und das Provenienzmanifest in den Fünf-Review-Abgleich einbeziehen.
4. V1-Vollprüfung mit `--publication-context corpus/raw/review-contexts/2026-09-11/p6-contexts.json` für 42 Quellen-Pairs und die Assertion-Pairs der 6 Assertions. Ausgaben mit lokalem Kontext gehören in ein ignoriertes Verzeichnis.
5. Registry, Knowledge (`state.md`, `handoff.md`) und Kapitel nach eigener Integration; ein Journaleintrag zur kuratierten Aufnahme ohne Repository-Werkzeug, wie in operations § Acquire vorgesehen.

## Offene inhaltliche Grenzen

- Die Protokolle des Vancouver-F2F und der Annual Members' Meeting 2026 waren im beobachteten Index nicht verlinkt. Die Entscheidung über die Sandbox in Vancouver und die geplante Ankündigung zum Stopp neuer P5-Features sind öffentlich nicht belegt.
- Sieben Council-Seiten mit P6-Treffern sind aus Budgetgründen zurückgestellt: 2025-11-11, 2025-12-18, 2026-02-09, 2026-05-06, 2026-06-22, 2026-06-24 und 2026-07-14.
- Nicht untersucht: der PDF-Export in `TEIC/timeForP6`, `TEIC/Documentation`, Board-Aufzeichnungen, die Konferenzseite und TEI-L.
- Ob die Foliensource bei `eb924226` dem gezeigten Vortrag entspricht, ist offen; die letzte Änderung an `index.html` datiert vom 2026-08-13.
- Die Abfragen des Auswahlprotokolls standen nicht vor der Lektüre des abgebrochenen Laufs fest. Sie wurden nachträglich vollständig über die Grenze ausgeführt, was das Protokoll offenlegt.
