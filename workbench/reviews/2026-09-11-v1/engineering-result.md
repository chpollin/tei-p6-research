# V1-Prüfinstrument: Engineering-Ergebnis

## Integrator-Abgleich zur Fassung v1.7

Der unten dokumentierte unabhängige Engineering-Stand ist historisch. Seine
Fehlerkorrekturen und die anschließenden Kontextkorrekturen bestehen jetzt
161 gezielte Tests für Instrument, Siegel, klassischen Cutter und
XML-Kontext. Die CLI-Antwortform wurde mit einem isolierten echten
Opus-Aufruf bestätigt; die aufgelöste Modellkennung lautet `claude-opus-5`.
Die alten Vorläufe bleiben erhalten und gelten nicht als aktueller Gesamt-Pass.

V1.7 liefert die Quellenidentität auch in Gesamttextprüfungen. Die Auswahl
einzelner Kernaussagen darf selektiv bleiben; der Gesamttextcheck prüft
zusätzliche Tatsachen, Einschränkungen und irreführende Auslassungen.
Weitere 16 Tests prüfen die Aufnahme der neun Praxisquellen.

- N1: Der gelieferte Großkontext und seine Grenze stehen im Prompt und im
  Siegel. Explizite Belege außerhalb der Core statements werden einbezogen.
  Ein Quellen-Support-Pass bezieht sich auf die geprüften Aussagen innerhalb
  dieses Kontexts. Er behauptet keine Lektüre unzugelieferter Buchteile.
- N2: UUID-Suffixe verhindern das Überschreiben gleichzeitiger Fehlversuche.
- N4: Jedes Urteil enthält angefordertes und aufgelöstes Modell; übernommene
  Pakete tragen ein Herkunftsprotokoll und benötigen exakte Gleichheit der
  vollständigen Prompts, Materialhashes, Schema- und Ausführungsgrenze.
- N5: Originalantworten tragen eine überprüfte SHA-256-Bindung. Ein öffentliches
  Siegel bleibt ein prüfbarer Record des vertrauenswürdigen Kontrollbereichs;
  es ist keine unabhängige Signatur des Modellanbieters.
- XML-Identität, Provenienz, vollständige Praxisdateien und Zitatlocator werden
  nach dem Journalbeschluss geliefert. Assertion-Reviews erhalten keine
  Autorbegründung oder zusätzliche Originalquote als Beleg.
- B7: Für Mehrfachdokumente fordert das Prompt konkrete Anker oder genaue
  beanstandete Klauseln. Deren Auswertung bleibt inhaltliche Nacharbeit.
- B8: Eine unteilbare große Einheit läuft allein und wird ausdrücklich als
  solche gemeldet. Das Zeichenbudget ist keine behauptete harte Kontextgrenze.

Der zusätzliche Gesamtcheck hat elf gezielte Tests für vollständigen Umfang,
die vorab erklärte Zweitstichprobe, separate Antworten und Modellbindung.
Er ist erst bestanden, wenn die aktuellen Erst- und Zweitsiegel vorliegen
und alle Bedingungen erfüllen.

Stand: 2026-09-11. Die Kontextform im folgenden Abschnitt ist verbindlich. Den geprüften Code-Stand, die Tests und die offenen Befunde enthält „Stand der Offline-Prüfung“.

## Frühe Notiz für Root: Kontextdatei der Publikationen

`python tools/full_review.py emit . --publication-context <datei.json> --out <dir>` liest genau eine JSON-Datei. Der Schlüssel ist die `reference`-ID des Destillats. Jede Passage deckt eine oder mehrere Statement-IDs dieser Referenz ab. Bei Threads mit weit auseinanderliegenden Kommentaren gibt es mehrere Passagen.

```json
{
  "teic-tei-issue-1400": {
    "source_url": "https://github.com/TEIC/TEI/issues/1400",
    "version": "issue thread at the 2026-09-06 snapshot",
    "retrieved": "2026-09-11",
    "storage": "local-only",
    "passages": [
      {
        "statements": ["s1"],
        "locator": "issue description, 2015-11-10",
        "context": "<vollständiger Originalwortlaut des umgebenden Abschnitts>",
        "context_sha256": "<SHA-256 der UTF-8-Bytes von context>"
      },
      {
        "statements": ["s2"],
        "locator": "comment 4, 2015-11-10",
        "context": "…",
        "context_sha256": "…"
      }
    ]
  }
}
```

Regeln, die `emit` hart prüft:

- Alle Felder sind Pflicht. `storage` ist `public` oder `local-only`. Private Thread- und Kommentarkörper sind `local-only`. Einheiten mit solchem Kontext dürfen nur in ein git-ignoriertes Verzeichnis oder außerhalb des Repositorys geschrieben werden, sonst bricht `emit` bzw. `run` ab.
- `context_sha256` muss exakt dem Text entsprechen. Eine unbekannte Referenz-ID, eine unbekannte oder doppelt abgedeckte Statement-ID ist ein Fehler.
- Das bei der Aufnahme gespeicherte Zitat, also der Text zwischen den Anführungszeichen vor der Klammer, muss nach Zusammenfassung von Leerraum wörtlich im `context` stehen. Sonst entsteht für dieses Statement die Lücke `quote-not-in-context`.
- Eine fehlende Referenz oder ein nicht abgedecktes Statement führt zur Lücke `no-original-context`. `check` meldet sie getrennt und gibt dafür keinen Pass.

## Stand der Offline-Prüfung (Worker, 2026-09-11)

Geprüfter Code, jeweils SHA-256: `tools/full_review.py` `dad4946fbaa7ca8f2eeb0b74c6b400c08a227e00f7f78b973e4da8dfdd831a0a`, `tools/review_execution.py` `ebf0615ba14fa14009482699f3d99fb87a6533ebfd034f8a3c6f7f58e83a630e`, `tools/review.py` `401192a6c29d133229a0e42654fcfc799c44d204d534720ec5810618870716ea`. Root hat `full_review.py` während dieser Arbeit dreimal geändert. Die Ergebnisse gelten nur für diesen Stand.

Lauf: `.venv/Scripts/python.exe -m pytest tests/test_full_review.py tests/test_review.py -q` ergibt **137 passed, 2 xfailed (strict)**. Es gab keinen Live-LLM-Aufruf und keinen Smoke-Test. Die Stringsuche im Binary der installierten CLI 2.1.263 findet `structured_output`, `modelUsage` und `outputTokens`. Die von `parse_response` erwartete Antwortform ist damit plausibel, aber nicht live belegt.

Geänderte Dateien:

- `tests/test_full_review.py` (neu, 93 Testfälle einschließlich Parametrisierung) prüft auf Kopien von `tests/fixtures/minimal`. Den Claude-Prozess ersetzt ein Fake mit CLI-Ergebnisform. Die Isolation aus `review_execution` läuft dabei echt. Die Fake-Grenze prüft bei jedem Aufruf ein leeres cwd, eine leere MCP-Konfiguration und dass kein Prompt in argv steht.
- `tests/test_review.py` patcht jetzt `tools.review.resolve_claude` statt `shutil.which`. Der Test prüft zusätzlich die Isolationsflags, das leere externe cwd, dessen Entfernung und den `isolation`-Record.

Abgedeckt:

- Emission: Ebenen, stabile IDs und Hashes, reproduzierbares `units.json`, Manifest.
- Assertion-Einheiten: vollständiger Statement-Abschnitt ohne Support, Lücke bei fehlendem Statement.
- Kontext: Dokumentfenster ±2 Blöcke ungekürzt; Publikation ohne Kontext (Lücke plus Zitat); Kontextbindung; Zitat nicht im Kontext; neun defekte Kontextdateien; Datenlücke.
- Gesamttext: Destillat mit Appraisal, Übergröße, assertion-complete, Kapitel samt fehlender Assertion, contested mit beiden Positionen ohne Support, unaufgelöstes contested-Ziel.
- Scope-Auswahl und -Ablehnung.
- Privatgrenze: git-ignoriert, extern oder öffentlich; verschobene Runde; Seal mit gehashten privaten Begründungen.
- Antworten: 16 defekte Formen.
- Isolation: Flags, cmd-Shim, natives Binary, cwd leer/extern/entfernt, Datei im cwd, cwd im Repo, keine Env-Werte oder Temp-Pfade im Record, Timeout, acht fehlende Isolationsnachweise, schreibender Reviewer.
- Ausführung: Batches je Ebene, Ablehnung eines Scopes mit Lücken, Resume ohne neue Aufrufe, Wechsel der Settings, `reuse` nur bei identischen Paketen, anderes Instrument, stale Batch, manipulierte Prompts, defekte Antwort als Failed-Batch, `--retry-failed`.
- `check`: Lücken, Abweichungen, fehlende Urteile, Exitcodes, kein Schreibzugriff auf den Vault; stale Material, Kontext, fehlender Kontext, geändertes Instrument; manipulierte und überlappende Batches.
- Zweitstichprobe nach `protocol.json`.

### Status der Erstmeldungen

| Befund | Stand dad4946f |
|---|---|
| B1 | Behoben: Positionen mit H1 + Statement, beschriftete Belege, kein Support (Test). |
| B2 | Behoben: „Citation-only excerpt“, die Lücke bleibt; `run` verweigert jeden Scope mit Lücken. |
| B3 | Behoben über `--retry-failed` (verschiebt nach `failed-attempts/`); Rest siehe N2. |
| B4 | Behoben: stale IDs werden gelistet, fehlender `--publication-context` hat eine eigene Meldung. `check` bricht weiterhin ab statt teilweise zu berichten. |
| B5 | **Verschärft:** `instrument_files` bindet zusätzlich `tools/review.py`, `tools/validate.py` und `tools/vault_documents.py`. Jede Änderung dieser gemeinsamen Werkzeuge, auch aus anderen Paketen, macht Runden unprüfbar und sperrt `reuse`. |
| B6 | Behoben (Test). |
| B7 | Teilweise: SYSTEM verlangt Anker oder Zitat im `reason`, es gibt aber kein Schemafeld und damit keine maschinelle Auswertung. |
| B8 | Teilweise: Hinweis bei Übergröße. `tei-p5-guidelines-nd-4.12.0` bleibt ein Aufruf mit 292 727 Zeichen, weil die zitierten Fenster allein 255 773 Zeichen haben. |
| B9 | Aktualisiert: 17 Referenzen mit 109 Statements, dazu 17 `distillate-complete`-Einheiten ergeben 126 Lücken. 756 Einheiten, davon 630 lauffähig. Neu sind `p6-v1-council-2025-10-07` und `p6-v1-council-2026-04-24`. |
| B10 | Behoben: Der Seal ersetzt Begründungen von local-only-Einheiten durch einen Hash (Test mit zitiertem Kontext). |
| B11 | Behoben: Abbruch „unresolved contested target“. |

### Neue Befunde

- **N1 Begrenzter Großkontext ohne Lücke (strict xfail):** Übersteigt eine Repräsentation 240 000 Zeichen, bekommt `distillate-complete` nur Vorspann und zitierte Fenster, aber keinen Eintrag in `gaps`. `check` kann dann `all_support: true` melden, obwohl Terms und Appraisal nie gegen den Volltext geprüft wurden. Real betroffen sind `szd-werke-2026-09-07` (Körper 1 647 466 Zeichen, geliefert 12 178) und `tei-p5-guidelines-nd-4.12.0` (428 758 Zeichen, geliefert 255 773). Vorschlag: eine eigene Einschränkung, die `all_support` verhindert. Ob `run` diese Einheiten trotzdem ausführt, entscheidet Root.
- **N2 Retry überschreibt Fehlversuch (strict xfail):** Das Versuchsverzeichnis ist ein Sekunden-Zeitstempel. Zwei Retries in derselben Sekunde, etwa bei sofortigem Auth- oder Parsefehler in einer Skriptschleife, überschreiben per `Path.replace` den früheren Fehlrecord desselben Pakets. Vorschlag: Zählersuffix oder Abbruch, wenn das Ziel existiert.
- **N3 Hinweis (fail-closed, getestet):** Ein fremder oder stale Batch im Rundenverzeichnis lässt `run` und `check` mit „package hash does not bind“ abbrechen. Die einzige Übernahmeform ist deshalb `reuse`.
- **N4 Hinweis:** `reuse` prüft `requested_model` der Vorrunde nicht. Das reale Modell steht zwar in jedem Urteil, aber `run-settings.json` der neuen Runde zeigt die Übernahme nicht.
- **N5 Hinweis:** Maßgeblich ist die ungehashte Rohantwort `outcome.stdout`. Ein lokal umgeschriebenes Verdict innerhalb des Vokabulars bleibt unentdeckt. Die Ablage muss vertrauenswürdig sein.

### Vor dem Volllauf

1. `full_review.py`, `review_execution.py`, `review.py`, `validate.py` und `vault_documents.py` einfrieren (B5).
2. Die Kontextdatei deckt alle 17 Referenzen ab, oder die Runde wird per `--ids` ohne Lückeneinheiten emittiert, weil `run` Lücken verweigert.
3. Ausgabe in ein git-ignoriertes Verzeichnis oder außerhalb des Repositorys schreiben.
4. Eine Runde mit einer Einheit ausführen, um die reale Antwortform (`structured_output`, `modelUsage`) live zu bestätigen. Diese Offline-Tests belegen sie nicht.
5. N1 entscheiden, bevor ein `all_support` für nd und szd-werke gilt.

## Erstmeldung (Stand c9ff585…, überholt; Status in der Tabelle oben)

Geprüfter Stand: `tools/full_review.py` VERSION `v1.1`, `tools/review_execution.py`, 2026-09-11. Die Emission lief nur mit `emit_units` im Speicher gegen das echte Repository, ohne Schreibzugriff und ohne Kontextdatei. Ergebnis: 720 Einheiten (source 444, assertion 112, distillate-complete 50, assertion-complete 107, chapter-complete 4, contested 3), 556 Originalpaare, keine doppelten IDs, 115 Lücken `no-original-context`.

- **B1 Anchoring in contested:** `contested::…`-Einheiten enthalten `docs[t].body` beider Assertions samt `## Support`. Das trifft alle drei realen Einheiten. Laut verification.md gehört Produzenten-Support nur in den gesonderten Konsistenzdurchgang (assertion-complete). Außerdem sind die Belege nicht nach Position beschriftet: `"\n\n".join(evidence)` ohne Assertion-Namen, das Modell kann Belege nicht zuordnen. Vorschlag: pro Position H1 + Statement-Abschnitt + beschriftete Belege.
- **B2 Publikation ohne Kontext verliert das Zitat:** `publication_context` liefert ohne Mapping nur `"Original publication context unavailable."`. Das gespeicherte Zitat (`pair.location`) fehlt dann ganz im Prompt. Ein Lauf erzeugt so für 100 Einheiten wertlose Urteile (erwartbar „not in the text“), die als Maschinenurteil gespeichert würden. Vorschlag: Einheiten mit `no-original-context` nicht an `run` geben oder das Zitat ausdrücklich als „nur Zitat, kein Kontext“ mitgeben.
- **B3 Resume blockiert nach einem Fehler:** Ein nicht akzeptierter Batch (Timeout, Parsefehler) liegt als `batches/<hash>.json`. Jeder weitere `run` bricht dann mit „existing nonaccepted batch requires a new attempt directory“ ab. `emit` verweigert ein vorhandenes `units.json`, und die akzeptierten Batches werden nicht übernommen. Ein einziger transienter Fehler im Volllauf erzwingt so Handarbeit oder einen vollständigen Neulauf. Vorschlag: den Fehlversuch nach `batches/failed/<hash>-<n>.json` verschieben, damit er sichtbar bleibt, und einen neuen Versuch erlauben.
- **B4 `check` meldet stale nur global:** Bei Material- oder Promptänderung bricht `check` mit einer einzigen `ValueError` ab, ohne Liste der betroffenen Einheiten. Wer `--publication-context` vergisst, sieht dieselbe irreführende Meldung „review scope or prompts are stale“, obwohl `manifest.context_sha256` einen gezielten Hinweis erlaubte.
- **B5 Instrumenthash deckt den gesamten Code:** `instrument_files` bindet `full_review.py` und `review_execution.py` vollständig. Schon eine spätere Korrektur an `check`/`seal` macht alle Urteile einer Runde unprüfbar. Der Code muss also vor dem Volllauf eingefroren sein.
- **B6 Unerwartete Antwortform bricht den Thread:** Ist `stdout` gültiges JSON, aber kein Objekt (oder ist ein `modelUsage`-Wert kein Objekt), wirft `parse_response` `AttributeError`. `run_batch` fängt nur `ValueError/TypeError/KeyError`, deshalb wird kein Batchrecord geschrieben und die Rohantwort geht verloren.
- **B7 Keine Claim-ID im Schema:** Das Schema erlaubt genau `id/verdict/reason`. Der Auftrag verlangt „ggf. konkret beanstandete Claim-ID“, was für Gesamttext- und Kapitel-Einheiten nötig ist.
- **B8 `--max-batch-chars` ist keine harte Grenze:** `distillate-complete::20_distillates/documents/tei-p5-guidelines-nd-4.12.0` hat 292 727 Zeichen und läuft allein, ohne Kürzung und ohne Warnung. Die nächstgrößeren Einheiten haben 201 572, 175 112 und 142 133 Zeichen.
- **B9 Umfang der Publikationskontexte:** Es gibt 15 Publikationsreferenzen, nicht neun. Zusätzlich zu Threads/Issues/Artikeln gehören dazu sechs `p6-v1-*` (Council-Protokolle, Folien). Die Kontextdatei muss alle 15 abdecken, sonst bleiben 115 Lücken.
- **B10 Seal und Privatgrenze:** `seal` übernimmt `reason` wörtlich. Reviewer-Begründungen zu `local-only`-Einheiten können private Thread-Körper zitieren, deshalb ist das öffentliche Siegel nicht garantiert frei von Privatkontext.
- **B11 Stilles Auslassen:** Ein `contested-with`-Ziel, das nicht auflöst, wird ohne Lücke übersprungen (`continue`).
