# Modell 0.2: Umsetzungsbericht Revisionsprüfung

Arbeitspaket nach `model-brief-v1.md`, Basis `7d7b7e4`. Dieser Bericht ist
eine Arbeitsaufzeichnung, keine Quellenevidenz und kein Grounding-Ziel. Er
behauptet keine fachliche Abnahme und gilt bis zur Prüfung durch den
Integrator am realen Dateistand als unverifiziert.

## Geänderte Dateien

- `tools/models/entities.py`
- `tools/models/identity_evidence.py` (nur Docstring)
- `tests/models/test_entities.py`
- `tests/models/test_identity_evidence.py`
- `knowledge/text-model.md`: 14.2 Punkt 8, 14.4 Revisionsvertrag und Diagnosetabelle, `updated`
- `knowledge/identity-evidence.md`: Ausführbarer Profilvertrag, `updated`

Historische Eingaben, Fälle, Beispiele und Berichte blieben unverändert.

## Gegenproben aus `2026-09-07-abstract-proposal`

| Veränderung im Speicher | Vorher | Nachher |
|---|---|---|
| Dossier: `selection-passage-szd-work-3` erhält `version` und `selector` von `selection-passage-szd-work-4` | `valid: true` | `E_SELECTION_REWRITE` bei `/after/selections/0` |
| `statements-and-revision.json`: erste Entität erhält `kind: other` | `valid: true` | `E_ENTITY_REWRITE` bei `/after/entities/0/kind` |
| Gleiches Beispiel: Alignment `al-birth` wandert unverändert von `concepts/3` nach `concepts/4` | `valid: true` | `E_CLAIM_REWRITE` bei `/before/concepts/3/alignments/0` |

Alle drei veränderten Pakete bleiben für sich gültig; erst die
Revisionsprüfung lehnt sie ab. Die vierte Beobachtung, die Kollision eines
lokalen 0.1-Konzepts `en-proper-noun` unter 0.2, ist kein Revisionsdefekt und
blieb außerhalb des Pakets.

## Entscheidungen

1. `check_claim_revision` vergleicht jede frühere Aussage mit Collection und,
   bei Alignments, mit dem Träger als Paar aus Collection und ID. Ein
   verschobenes Alignment ändert seinen Gegenstand und bleibt deshalb
   `E_CLAIM_REWRITE` am früheren Pfad.
2. Neuer Code `E_ENTITY_REWRITE`: eine wiederverwendete Entitäts-ID mit
   anderer `kind`, auch ohne referenzierende Aussage, weil 14.1 einen
   Wechsel der Art als neue Entität definiert. Pfad ist das Feld im späteren
   Paket.
3. Neuer Code `E_SELECTION_REWRITE`: eine Selektion, auf die das frühere Paket
   verweist, ändert `version` oder `selector`, verglichen als exakter Wert
   einschließlich Selektorart und Match-Politik. Gleich aufgelöste Ziele
   genügen nicht. Der Abhängigkeitsraum ergibt sich aus Annotation,
   Lesungsknoten und Relationsendpunkt, auf die alle längeren Pfade
   zurückführen; der zyklenfähige Relationsgraph wird nicht traversiert.
4. Die `kind`- und Selektionsregel laufen nur, wenn beide Pakete gültig sind.
   Die Aussageregel liest ein ungültiges späteres Paket weiterhin defensiv.
5. Der exakte Record-Vergleich bleibt. Umordnen von Arrays innerhalb einer
   Aussage, etwa Knoten, Teilnehmer oder `supersedes`, ist ein Rewrite,
   obwohl R11 diese Reihenfolge ignoriert. Registerreihenfolge und
   Alignment-Reihenfolge im Träger bleiben frei. Ein Regressionstest
   fixiert beides.
6. Das Profil behält `E_IDENTITY_REWRITE`, das auch das Entfernen früherer
   Entitäten verbietet. Eine geänderte `kind` meldet dort bewusst beide
   Codes, damit der bestehende Profilvertrag kompatibel bleibt.
7. Drei Abstürze von `validate_extension` bei fehlerhaften Entitäten sind
   behoben: Nicht-Objekt, fehlende ID mit Alignments, unhashbare ID. Sie
   brachen auch die Revisionsprüfung.

## Prüfungen

- `.venv/Scripts/python.exe -m pytest tests/models/test_entities.py tests/models/test_identity_evidence.py -q`:
  184 bestanden, 1 fehlgeschlagen. `test_source_admission_and_generated_outputs_reproduce`
  scheitert nur an `inputs` in `experiments/identity_evidence/report.json`,
  also an Fingerprints geänderter Dateien; Dossier und Fallausgaben
  reproduzieren byte-gleich.
- `.venv/Scripts/python.exe -m ruff check` auf die vier Python-Dateien: bestanden.
- `git diff --check` auf die sechs Dateien und diesen Bericht: bestanden.
- Nur zur Abgrenzung: `tests/test_check_entities_v02.py`, `tests/models/test_rdf_binding.py`,
  `tests/models/test_editorial_profile.py`: 169 bestanden, 1 fehlgeschlagen,
  `test_spec_mirrors_the_module_constants`, erwartbar bis `spec.json` folgt.

Keine Gesamtsuite, keine Regeneration, kein Netzwerk.

## Aufgaben für den Integrator

1. `experiments/entities_v02/spec.json`: `diagnostics` gleich
   `tools.models.entities.DIAGNOSTICS` setzen; neu sind `E_ENTITY_REWRITE`
   nach `E_ENTITY_KIND` und `E_SELECTION_REWRITE` nach `E_REFERENCE`. In
   `extension_diagnostics` ergänzen:
   - `E_ENTITY_REWRITE`: "A reused entity ID changes its kind between two valid packages; check_claim_revision only"
   - `E_SELECTION_REWRITE`: "A selection referenced by the valid earlier package changes its version or selector under its ID; check_claim_revision only"
   - `E_CLAIM_REWRITE` neu: "A claim of a valid earlier package is missing, duplicated or changed in the later package, including its collection and the carrier of a nested alignment; check_claim_revision only"
   - `operations.check_claim_revision` um Trägerregel, `E_ENTITY_REWRITE` und `E_SELECTION_REWRITE` ergänzen.
2. Berichte regenerieren und prüfen: `tools/check_abstract_text_v01.py`,
   `tools/check_entities_v02.py`, `tools.check_identity_evidence`; alle
   fingerprinten `tools/models/*.py` oder die geänderten Knowledge-Dokumente.
3. Betroffene Seiten nach `knowledge/design.md` § Regeneration neu bauen.
4. Kapitel 02 § 10, `knowledge/handoff.md` und `knowledge/state.md` auf
   Aussagen prüfen, die die drei Lücken als offen führen. Maßgeblich ist
   `knowledge/text-model.md` 14.4 ab `check_claim_revision(before, after)`
   bis einschließlich Diagnosetabelle sowie 14.2 Punkt 8.

## Bewusst veränderlich

Labels von Agenten, Texten und Entitäten; Label und Definition nicht
reservierter Konzepte; Selektionen ohne Verweis im früheren Paket; eine ID,
deren früherer Record unreferenziert war und später für eine andere
Record-Kategorie verwendet wird; das Entfernen unreferenzierter Records im
Kernmodell. Eine umdefinierte Aussageart kann die Lesart einer unveränderten
Aussage verschieben; ein Einfrieren bräuchte eine eigene Entscheidung.

## Offene Lücken

- Keine allgemeine Unveränderlichkeit, kein persistenter Verlaufsdienst,
  keine menschliche Abnahme.
- `inspect_claim` filtert Supersession und Withdrawal weiterhin nicht.
- `cases.json` enthält keine Revisionsfälle, und der Runner ruft
  `check_claim_revision` nicht auf; der Nachweis liegt in den Unit-Tests.
- Der Test-Ledger in 14.6 nennt die neuen Regeln nicht als eigene Fälle.
- Die Kollision reservierter Konzept-IDs beim Übergang von 0.1 zu 0.2 bleibt
  unverändert.

## Werkzeugnotiz

`apply_patch` lief als `codex.exe --codex-run-as-apply-patch`, der Patch per
stdin an einen Python-Aufruf übergeben. Große Heredocs und einfache
Anführungszeichen im Aufruf scheiterten an der Shell-Hülle, deshalb wurden
Patches in Teilen angewendet.
