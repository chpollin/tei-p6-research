# V1-Paket Praxis: ODD- und Verarbeitungspraxis als Kontraststichprobe

Stand: 2026-09-11. Basis `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0` mit uncommittetem Refaktorierungsstand. Alle neuen Artefakte haben den Status `grounded` ohne `checked`-Einträge. Nichts wurde auf `validated` oder `verified` gehoben.

## Geschlossene Lücke

Der Lock `real-world-customizations` enthielt bisher keine externe ODD mit Verarbeitungspfad und realem Eingabedokument. Beim Humboldt-Fall lag nur ein generiertes RNG vor, keine ODD. Dieser Lauf nimmt eine begründete Kontraststichprobe aus drei Fällen auf, jeweils mit ODD, Verarbeitungskontext und echtem Eingabedokument. Kriterien, Kandidaten und Dispositionen stehen vor jedem Befund in `workbench/selections/2026-09-11-odd-practice.md`.

| Fall | Domäne | ODD | Verarbeitungskontext | Eingabe |
|---|---|---|---|---|
| DraCor | Dramenkorpus | `dracor-org/dracor-schema@c2f9e8140bf413cb3bce44abc818d563ddc92d88:dracor.odd`, CC BY 4.0 | `build` am selben Commit (teitoodd, teitorng, teitoschematron), CC BY 4.0 | `dracor-org/gerdracor@43fe19012bae4784689ce7ad5855dfdd643364e5:tei/leisewitz-die-pfandung.xml`, CC0 |
| EpiDoc | Epigraphische Edition | `EpiDoc/Source@e5b68eb8627ac1bc55a4f9f2bec94d8276ff74b3:schema/tei-epidoc.xml`, GPL (Kopf: 2.0-or-later, `LICENSE.txt`: 3.0-or-later) | `schema/README.txt` am selben Commit (OxGarage, Subset-Politik, latest vs. nummeriert), GPL-3.0-or-later | `ISicily/ISicily@262784ad8b4d4ee5a203abc0a772ae3eea289997:inscriptions/ISic000156.xml`, CC BY 4.0 |
| CMIF | Briefmetadaten-Austausch | `TEI-Correspondence-SIG/CMIF@d171133e2ca7a0b987ba0564577ec79077b8d908:odd/cmi-customization.odd` (= v1.1.0), CC BY 4.0 oder BSD-2-Clause | `correspSearch/csAPI@566b2d29233e3be332dc749266558cb7383cd31d:api/v2.0/services/check/index.xql` (jing-report und SchXslt), LGPL-3.0-or-later | `correspSearch/csStorage@9a7ebe3b68bb464be64d6e08fe1ed8672f90c00d:freieisen-stoeber.xml`, CC BY 4.0 laut Dokument |

Alle drei als ODD geführten Dateien hat das Werkzeug geprüft: Jede ist ein TEI-Dokument mit genau einem `schemaSpec`. Die Humboldt-Edition ist bewusst kein ODD-Fall, weil ihr Datensatz-Repository nur `.rng`-Dateien enthält. Ein Katalogfall wurde nicht geprüft; CMIF wird nicht als Katalog behandelt.

## Geänderte und neue Dateien (nur eigene Pfade)

- `workbench/selections/2026-09-11-odd-practice.md`: Auswahlprotokoll mit Fragen P1–P6, Kriterien, 15 Kandidatenzeilen, Verzerrungen und erforderlicher Domänenabnahme.
- `tools/ingest_practice_v1.py`, `tests/test_ingest_practice_v1.py`: reproduzierbare Aufnahme über `HttpStore` sowie `--check` (offline) und `--reproduce` (Neuabruf mit Hashvergleich).
- `sources/manifests/2026-09-11-practice-v1-admission.yaml`: `bounded-complete` für die deklarierte Anfrageliste; 26 Anfragen, 9 aufgenommene Quellen, 17 Kontextbeobachtungen, 39 Leseblöcke, `gaps: []`, 10 `known_limits`, 2 `rights_exceptions`.
- `corpus/normalized/practice-v1/admission-2026-09-11.json`: Metadaten, Hashes, Leseblock-Locators, selbst ausgeführtes Inventar und Bytevergleiche, keine Quelltexte. Das ist eine Navigationshilfe und kein Grounding.
- `00_sources/documents/practice-v1-*` (9 Originale; gitignoriert). Rohantworten liegen inhaltsadressiert unter `corpus/raw/sha256/`.
- `10_markdown/documents/practice-v1-*.md` (9 unveränderliche Repräsentationen: vollständiges Original plus JSON-kodierte exakte Byteintervalle `^r1`…, jeweils mit Zeilen- und Byte-Locator).
- `20_distillates/documents/practice-v1-*.md` (9 Destillate, 44 Aussagen).
- `30_assertions/practice-v1-*.md` (7 Assertions, 18 Grounding-Paare):
  - `practice-v1-sampled-odds-name-their-tei-source-differently`
  - `practice-v1-sampled-odds-select-modules-by-contrasting-mechanisms`
  - `practice-v1-sampled-schematron-sits-in-odds-and-in-a-service`
  - `practice-v1-sampled-inputs-associate-schemas-differently`
  - `practice-v1-epidoc-latest-guidance-and-isicily-reference`
  - `practice-v1-sampled-schema-generation-paths-differ`
  - `practice-v1-cmif-evidence-restriction-appears-in-a-real-file`

Bestehende Destillate, Claims, Locks, Registry, MOCs und Knowledge-Dokumente wurden nicht geändert. `corpus/raw/review-contexts/2026-09-11/practice-contexts.json` wurde bewusst nicht angelegt. Alle Praxisquellen sind vom Typ `document` mit Repräsentationsblöcken, und `checked_contexts` würde unbekannte Referenz-IDs zurückweisen.

## Ausgeführte Prüfungen

| Prüfung | Ergebnis |
|---|---|
| `.venv/Scripts/python.exe -m tools.ingest_practice_v1` | `OK: 26 responses; 9 sources admitted with 39 reading blocks` |
| `... --check` (offline, nach Werkzeugänderung erneut) | `OK: nine pinned practice sources, reading blocks and admission hashes reconcile` |
| `... --reproduce` (Neuabruf aller 26 Anfragen) | `OK: every recorded request refetched with identical SHA-256 and length` |
| XML-Wohlgeformtheit | Werkzeug und separater `ElementTree`-Parse: alle 6 XML-/ODD-Originale wohlgeformt, alle SHA-256 gleich Manifest. Element-Leseblöcke einzeln geparst. Keine DTD- oder Entity-Deklarationen, kein CR |
| `pytest tests/test_ingest_practice_v1.py` | 16 bestanden. Ein zunächst fehlschlagender Fall (ParseError statt ValueError bei geändertem Selektor) wurde im Werkzeug korrigiert; die Renderausgabe blieb unverändert |
| `tools.review.cut_pairs` für die neuen Dateien | 44 Quellpaare, 18 Assertion-Paare, keine Probleme, keine leeren Locations |
| `tools/validate.py .` | Exit 1, 24 Fehler, 0 Warnungen. Von diesem Paket: 7 × `E-ORPHAN` (die neuen Assertions, bis die MOCs generiert sind) und `E-GENERATED` in MOC-ODD and Customization, MOC-Interoperability and Processing, MOC-Metadata and Entities und `corpus/projections/source-inventory.md`. Keine `E-ANCHOR`, `E-LAYER`, `E-STATEMENT`, `E-FRONTMATTER` oder `E-SOURCE` an Praxisdateien. Die übrigen Fehler (6 × `E-ORPHAN` `p6-v1-*`, MOC-History and Governance, MOC-P6 Design) gehören zum P6-Paket |
| `tools/inventory.py . --check` | 11 veraltete Regionen (gemischt mit P6-Paket); nicht geschrieben |
| `python -m tools.corpus.validate_control_plane .` | `OK: source control plane is internally consistent` |

Nicht ausgeführt: ODD-Kompilierung, RELAX-NG- und Schematron-Validierung. Im Projekt-Environment fehlen TEI Stylesheets, Java, Jing, SchXslt und lxml; eine Fremdinstallation wurde nicht vorgenommen. Die Gültigkeit der drei Eingabedokumente ist deshalb unbekannt. Build-Skripte, Workflows, XQuery und XSLT aus den Quellen wurden nicht ausgeführt. Selbst ausgeführt wurden nur HTTP-Abruf, Hashing, Wohlgeformtheits-Parse, ein deterministisches Element- und Spezifikationsinventar sowie drei Bytevergleiche. Beobachtete Pipeline-Konfiguration bleibt Quelltext.

## Selbst ausgeführte Beobachtungen (Navigation, kein Grounding)

- **Inventar DraCor:** 12 `moduleRef`, 60 `elementSpec mode=change`, 1 `add`, 7 `classSpec mode=delete`, 36 `constraintSpec`, 40 `sch:rule` (29 mit Rolle `warning`), `source="tei:4.12.0"`.
- **Inventar EpiDoc:** 17 `moduleRef` (14 mit `except`), 12 `elementSpec mode=change`, 5 `sch:rule`, `source` = Vault-p5subset 4.10.2.
- **Inventar CMIF:** 5 `moduleRef` (4 mit `include`), 10 `elementSpec change`, 1 `replace`, 2 `classSpec replace`, 5 geschlossene Wertlisten, kein Schematron in der ODD, kein `@source`.
- **Bytevergleiche:** Die RNG-Kopie im csAPI-Prüfdienst hat 104.178 Bytes, die CMIF-v1.1.0-RNG 112.569; die `cmif.sch` 5.220 gegenüber 1.963 Bytes. `ircyr-checking.sch` hat bei I.Sicily 6.016 und in EpiDoc/Source 4.915 Bytes. Keine Datei ist byteidentisch. Daraus folgt kein semantischer Unterschied.

## Rechte

Aufgenommen und zur Versionierung vorgesehen sind nur Dateien mit geprüfter Lizenz (siehe Tabelle; Attribution steht in jeder Repräsentation und im Manifest `rights`). Zwei Punkte brauchen eine menschliche Rechteprüfung:

1. Die EpiDoc-ODD nennt im Dateikopf GPL-2.0-or-later, `schema/LICENSE.txt` dagegen GPL-3.0-or-later. Beide Angaben sind festgehalten, eine rechtliche Bewertung ist nicht erfolgt.
2. `csStorage` hat keine Repository-Lizenz. Die CMIF-Datei trägt eine CC-BY-4.0-Angabe auf Dateiebene; ihr Kopf enthält Personennamen und eine E-Mail-Adresse als unveränderte Quelldaten.

Nur lokal (Manifest `rights_exceptions`) bleiben `dracor-org/gerdracor/.github/workflows/validation.yml` und `EpiDoc/Source/.github/workflows/build-dev-schema.yml`, weil ihnen eine repositoryweite Lizenz fehlt.

## Benötigte Integration durch Root

1. **MOCs und Inventar:** `python tools/inventory.py . --write` erzeugt für dieses Paket:
   - MOC-ODD and Customization: +9 Destillate, +5 Assertions
   - MOC-Interoperability and Processing: +8 Destillate, +4 Assertions
   - MOC-Metadata and Entities: +2 Destillate, +1 Assertion
   - `corpus/projections/source-inventory.md`: +9 Zeilen

   Danach verschwinden die 7 `E-ORPHAN`. Vorschläge für handgeschriebene Open questions in MOC-ODD and Customization: Welche effektiven Schemata erzeugen die drei ODDs mit ihren benannten Prozessoren? Welche TEI-Quelle nutzt ein Prozessor ohne `schemaSpec/@source`? Einen Katalogfall mit ODD gibt es noch nicht.
2. **Lock** `sources/locks/real-world-customizations.yaml` (`as_of` → `2026-09-11`), neuer `records`-Eintrag:
   ```yaml
   - kind: purposive-odd-processing-contrast-sample
     manifest: sources/manifests/2026-09-11-practice-v1-admission.yaml
     selection: workbench/selections/2026-09-11-odd-practice.md
     boundary: Three community-published customizations (DraCor, EpiDoc with I.Sicily, CMIF with correspSearch), each with one ODD, one processing context and one real input document at pinned commits; seventeen local context observations; no family, corpus or catalogue coverage.
     rights: [CC-BY-4.0, CC0-1.0, GPL-2.0-or-later / GPL-3.0-or-later, CC-BY-4.0 OR BSD-2-Clause, LGPL-3.0-or-later]
   ```
   Zusätzliche offene Gaps: `odd-practice-schema-validation-not-executed` und `odd-practice-no-catalogue-case`. `retrieval_status` bleibt `partial`, der Familien-Gap `sampling-protocol-not-yet-approved` bleibt offen. Die Registry braucht keine Änderung.
3. **`.gitattributes`:** `10_markdown/documents/practice-v1-*.md -whitespace`. Fünf Repräsentationen enthalten quelltreue Leerzeichen am Zeilenende (25 Zeilen), analog zu den bestehenden Einträgen. Die Nutzlasten sind LF-only, `text=auto eol=lf` verändert sie nicht.
4. **V1-Review:** 44 Quellpaare, 18 Assertion-Paare sowie Complete-Einheiten für 9 Destillate und 7 Assertions. Kontext entsteht aus Repräsentationsblöcken, eine Publikationskontextdatei ist nicht nötig. Vorher sind keine Status-Hebungen zulässig.
5. **`knowledge/state.md` und Handoff:** Checkpoint und offene Punkte unten nachtragen.

## Konkrete Lücken und Grenzen

- **Keine Validierung:** Welche Schemata kompiliert werden und ob die drei Eingaben gültig sind, ist unbekannt. Die Schemaorte in den Eingaben (`https://dracor.org/schema.rng`, `https://epidoc.stoa.org/schema/latest/tei-epidoc.rng`) wurden nicht abgerufen. Release-Assets, Docker-Images (`dracor/validate-action:3.0.0`, `teic/teidev-docker:latest`) und das Stylesheets-Submodul `81408afc9a25c9170c49adadb0df508ead8ba959` fehlen.
- **Gegenbefund EpiDoc:** Das README nennt OxGarage, der nur lokal beobachtete Dev-Workflow ruft dagegen `teitoodd`/`teitorng` auf. Die Assertion zu Erzeugungspfaden spricht deshalb ausdrücklich nur von „dokumentiert“. Ob README-URL (`www.stoa.org/epidoc/schema/latest`) und I.Sicily-URL (`epidoc.stoa.org/schema/latest`) dieselbe Datei liefern, ist offen.
- **Gegenbefund DraCor:** Der nur lokal beobachtete GerDraCor-Workflow prüft laut Datei gegen das DraCor-Schema mit `warn-only`. Ungegroundet, weil die Rechte ungeklärt sind.
- **Offene Frage EpiDoc:** Die ODD ändert eine Klasse `att.responsibility`; ob diese in P5 4.10.2 existiert, ist ungeprüft.
- **Versionen:** DraCor ist 5 Commits nach 1.6.0 gepinnt, EpiDoc 28 nach v9.8; nur CMIF entspricht einem Tag.
- **Verzerrung:** Die drei Fälle sind geteilte Gemeinschaftsprofile, keine lokalen Einzelprojekt-ODDs. Alle liegen auf GitHub, sind gut dokumentiert und überwiegend europäisch; kleine Dateien wurden bevorzugt. Bei der CMIF-Wahl war `evidence="conjecture"` bereits sichtbar. Es gibt keine statistische Repräsentativität und keine Familien- oder Korpusvollständigkeit.
- **Nicht erfasst:** Kein Katalogfall. SigiDoc, IIP, EDH sowie die CMIF-Erzeugung bei WeGA und HenDi sind nur zurückgestellt.
- **Keine Nutzungsbelege:** Es gibt keine Belege für Migrations- oder Nutzbarkeitserfolg, und das Paket beansprucht keine.
- **Domänenabnahme ausstehend:** Dramenkodierung, Epigraphik und Leidener Konventionen sowie Briefmetadaten.
- **Review-Schnitt:** `tools/review.py` liest `#`-Kommentarzeilen im DraCor-Build-Original als Überschriften. Das betrifft nur die Pfadbeschriftung der Review-Location, nicht Anker oder Validierung.
