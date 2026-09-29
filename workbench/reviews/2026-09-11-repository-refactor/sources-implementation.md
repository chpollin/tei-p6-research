# Umsetzungsbericht: Quellenkontrolle und Wayback-Wiederaufnahme

- Datum: 2026-09-11
- Basis: `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0`
- Auftrag: `sources-brief-v1.md` in diesem Verzeichnis
- Rolle: Worker. Keine Commits, kein Staging, kein Netzwerkzugriff, keine Statushebung. Dieser Bericht ist eine Selbstauskunft und keine Quellenevidenz.

## Geaenderte Dateien

- `tools/corpus/manifest.py`: `lock_manifest_references` zaehlt `manifest`, `manifests` und `records[].manifest` in Reihenfolge ohne Dubletten auf; fehlerhafte Eintraege werfen `ValueError` statt still uebersprungen zu werden. `repository_path` erzwingt relative POSIX-Verweise ohne `..`, Backslash oder Laufwerk, optional unter einem Praefix, und prueft, dass der aufgeloeste Pfad unter der Wurzel bleibt. Konstanten `LOCK_DIRECTORY`, `MANIFEST_DIRECTORY`.
- `tools/corpus/validate_control_plane.py`: nutzt beide Helfer. Neu geprueft werden `retrieval_status` zwischen Registry und Lock, Pfadgrenzen fuer Lock-, Manifest- und Objektverweise, fehlende `records[].manifest`, eine `no-retrieval-run-yet`-Luecke gegen benannte Laeufe derselben Quelle mit einem Status ausser `planned`, sowie ein vollstaendiger Lock, der noch eine `blocks-*`-Luecke traegt. Laufstatus hebt nie den Lockstatus.
- `tools/sitegen/source_data.py`: eigene Aufzaehlung entfernt; gemeinsame Aufzaehlung und Pfadgrenze fuer Manifeste.
- `tools/corpus/listserv_snapshot.py`: `wayback-fetch` arbeitet monatsweise mit versiegelten Checkpoints, `--checkpoint` und `--resume-from`; CDX-Antworten werden je Monat journalisiert. `HttpStore` ist unveraendert.
- `sources/locks/tei-l-archive.yaml`: Stand der Teile und Luecken, siehe unten.
- `corpus/normalized/README.md`: an die tatsaechlich geschriebenen Stroeme angeglichen (Identitaet und Art je Strom, Provenienz ueber benannte unveraenderliche Ausgabe, Manifest und Rohantwort, Rechteregel).
- Tests: `tests/corpus/test_listserv_snapshot.py` erweitert; neu `tests/corpus/test_control_reconciliation.py`, weil das vorhandene Kontrollmodul `test_control_plane.py` heisst; neu `tests/test_source_data.py`.

## Pruefungen (offline)

- `.venv/Scripts/python.exe -m pytest tests/corpus/test_control_plane.py tests/corpus/test_control_reconciliation.py tests/corpus/test_manifest.py tests/corpus/test_listserv_snapshot.py -q -p no:cacheprovider`: 115 passed.
- `.venv/Scripts/python.exe -m pytest tests/test_source_data.py tests/test_build_corpus_overview.py -q -p no:cacheprovider`: 37 passed.
- `.venv/Scripts/python.exe -m ruff check` auf den sieben geaenderten Python-Dateien: All checks passed.
- `.venv/Scripts/python.exe -m tools.corpus.validate_control_plane .`: OK.
- `git diff --check` auf den eigenen Dateien, fuer die neuen Tests `git diff --no-index --check`: ohne Befund.
- Nicht ausgefuehrt: volle Suite, `tools/validate.py`, Seitenregeneration. Das bleibt beim Integrator.

## CLI und Checkpoint-Form

`python -m tools.corpus.listserv_snapshot wayback-fetch --coverage-input corpus/normalized/mail/tei-l-wayback-coverage.jsonl --normalized-output corpus/normalized/mail/tei-l-wayback.jsonl --manifest-output sources/manifests/YYYY-MM-DD-tei-l-wayback.yaml [--delay-seconds 0.5] [--checkpoint DIR] [--resume-from DIR]`

- Standardverzeichnis `<raw-root>/checkpoints/<manifest stem>/`, lokal und durch `corpus/raw/.gitignore` ignoriert. Ein neuer Lauf bricht ab, wenn das Verzeichnis nicht leer ist. `--resume-from DIR` setzt fort; nennen `--checkpoint` und `--resume-from` verschiedene Verzeichnisse, bricht der Lauf ab.
- `checkpoint.json`: `checkpoint_kind: tei-l-wayback-fetch-checkpoint`, `schema_version: 1`, `source_id`, `adapter`, `started_at` des ersten Aufrufs, `invocations` und `identity` (SHA-256 der Coverage-Datei, sortierter Monatsfilter, `max_messages`, CDX-Endpunkt, Wayback-Praefix, ausgewaehlte Monate mit Capture-Zeitstempel und Original-URL). Verzoegerung und Ausgabepfade gehoeren nicht zur Identitaet.
- `months/<yymm>.json` je abgeschlossenem Monat: `budget_before`, Zaehler, `responses` (Records von Monatsindex und Nachrichtenseiten mit URL, Status, Bytezahl, SHA-256, `raw_path`), `cdx_responses`, `index_gaps`, `message_gaps`, die normalisierten `records` und `block_sha256` ueber die kanonische JSON-Form. Jede Datei wird atomar geschrieben, sobald der Monat fertig ist.
- Vor jeder Wiederverwendung werden Art, Quelle und Identitaet, das Siegel, die Monatszugehoerigkeit und der Abschluss des Monats geprueft, ausserdem jede Rohdatei (Pfadform, Groesse, SHA-256) und dass jede Zeile von einer Antwort ihres Monats getragen wird. Jede Abweichung verwirft die ganze Wiederaufnahme mit `ValueError`, vor jeder HTTP-Anfrage. Ein Monat wird nur wiederverwendet, wenn das Nachrichtenbudget vor ihm gleich ist.
- Nicht versiegelt und daher erneut abgefragt: fehlgeschlagener Monatsindex, fehlgeschlagener Nachrichtenabruf, CDX-Fehler ohne gefundenen Capture. Eine gemessene Abwesenheit (leere CDX-Liste, Wayback-Platzhalterseite, `wayback-index`-Zeile) ist ein abgeschlossenes Ergebnis.
- Ausgabe und Manifest entstehen wie bisher einmal am Ende; Zeilen, Luecken, Zaehler und `bounded_status` ergeben sich aus wiederverwendeten und neuen Monaten gemeinsam. Neu im Manifest: `requests.checkpoint`, `requests.resume_from` und bei Wiederaufnahme `resume` mit `invocations` und `months_reused`. Getestet: unterbrochener und fortgesetzter Lauf gegen ununterbrochenen Lauf, byteidentische JSONL-Ausgabe und gleiche Provenienz bis auf Lauf-ID, Pfade und `resume`, mit und ohne Nachrichtenbudget.

## Statusbereiche TEI-L

- Familie `tei-l-archive`: `partial` in Registry und Lock.
- `psu_archive`: `bounded-complete` fuer die Monate 2512 bis 2609 im Lauf `2026-09-06-tei-l-psu` (10 Monate indexiert, 267 Nachrichten, keine Luecke).
- `wayback_brown_archive`: `partial`. Die Capture-Messung 9001 bis 2512 ist `bounded-complete` (432 gemessen, 368 mit Capture, 64 ohne); kein Abruf ist erfasst.
- `consortium_export`: `planned`.
- Luecken: `wayback-captured-months-not-fetched` (blocks-bounded-complete), `wayback-months-without-capture` (open), `psu-months-before-2512-not-requested` (open), `consortium-export-not-requested` (open, unveraendert). `no-retrieval-run-yet` entfaellt, weil zwei erfasste Laeufe es widerlegen; die messbar ueberholte Brown-Luecke ist durch das Messergebnis ersetzt.

## Offene Punkte fuer den Integrator

- Materialseite: Die Seitenpruefung ist unten nachgetragen. Die neuen Lueckencodes und Zaehler haben in `tools/sitegen/materials_view.py` keine eigenen Labels.
- Knowledge-Dokumente: `knowledge/testing.md` (Umfang des Validators), `knowledge/state.md` und `knowledge/handoff.md` (TEI-L). Der abgebrochene Lauf vom 2026-09-06 hatte keinen Checkpoint; seine Rohseiten werden nicht wiederverwendet, sondern neu abgefragt und im Rohspeicher dedupliziert.
- Akquisition bleibt offen: Wayback-Abruf der 368 Monate, Messung der Penn-State-Monate vor 2512, Konsortiumsexport. `wayback-coverage` und `psu` haben keine Wiederaufnahme.
- Entscheidung offen: ob `consortium-export-not-requested` die Familie blockieren soll.
- Arbeitsweg: `apply_patch` lief ueber das Codex-Binary per Python-Subprozess mit dem Patch als einzigem Argument. Lange Shell-Kommandos scheiterten an einer Laengengrenze, doppelte Backslashes wurden bei der Uebergabe halbiert. Deshalb bauen die Tests Windows-Pfade ueber `PureWindowsPath`.

## Seitenpruefung

- `docs/corpus.html` wurde mit `tools.build_corpus_overview.build_page` aus seinem Footer-Datum 2026-09-07 im Speicher neu gebaut und verglichen, ohne die Datei zu schreiben: 4 geaenderte Zeilen, alle in der TEI-L-Zeile (Such- und Filterattribute, Kennzahlen aus den neuen Lock-Zaehlern, "4 open items", Lueckenliste). Bis der Integrator die Seite regeneriert, schlaegt `tests/test_build_pages_reproduce.py` fuer `corpus.html` notwendig fehl, weil der Test genau diesen Build mit der committeten Datei vergleicht. Der Test selbst wurde nicht ausgefuehrt.
