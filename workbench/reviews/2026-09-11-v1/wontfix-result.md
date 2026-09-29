# V1-Arbeitspaket Wontfix: Ergebnis

Stand 2026-09-11. Basis ist `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0` mit dem uncommitteten V1-Arbeitsstand; der Auftrag steht in [briefs/wontfix.md](briefs/wontfix.md). Geschrieben wurden ausschließlich `workbench/selections/2026-09-11-wontfix-context.md` und diese Datei. Quellen, Destillate, Assertions, MOCs, Locks, Manifeste und Wissensdokumente blieben unverändert, und kein Status wurde gesetzt. Alle Thread-Inhalte wurden als Daten behandelt. Beteiligte werden nur in ihrer Rolle genannt.

## Gelesener Umfang

**Threads.** Gelesen wurden alle 32 Beschreibungen und alle 262 Issue-Kommentare aus `corpus/raw/review-contexts/2026-09-11-wontfix/review-packet.json`, vollständig und in neun Blöcken von höchstens 22 000 Zeichen. Das Hilfsskript `C:/tmp/wontfix/dump.py` liegt außerhalb des Repositorys. Drei Blöcke brachen zunächst mit einem Kodierungsfehler der Konsole ab und wurden mit UTF-8-Ausgabe vollständig wiederholt. In den übrigen Blöcken zeigte die Konsole einzelne typografische Zeichen, etwa Anführungszeichen, als Ersatzzeichen an; Wortlaut und Code blieben lesbar.

**Regeln und Records.**
- `AGENTS.md`, `knowledge/INDEX.md`, `knowledge/governance.md`
- `knowledge/operations.md` § Select und § Trace an issue or decision
- `knowledge/data.md` § Threads as citation-only sources
- `workbench/selections/README.md`, die beiden Auswahlrecords vom 2026-09-06, `2026-09-06-topic-run-context.md` und `2026-09-11-counterevidence-reconciliation.md`
- `README.md` und `source-policy.md` dieses Laufs

**Nur lesend geprüfte Deklarationen 4.12.0.** Geprüft wurden die Repräsentationen in `10_markdown/documents/` von `lb`, `author`, `body`, `figure`, `handShift`, `macro.limitedContent`, `graphic`, `att.resourced`, `front`, `back`, `listBibl`, `locus`, `choice`, `att.written`, `att.transcriptional` und `standOff`, dazu das Fehlen von `att.source`.

**Durchsuchte Claims.** `20_distillates/`, `30_assertions/`, `40_output/`, `10_markdown/`, `references/`, `glossary/`, `knowledge/` und `workbench/` wurden nach Verweisen auf die 32 Nummern durchsucht. Außerdem wurden `MOC-Text and Document Structures`, `MOC-Metadata and Entities` und drei Entitäten-Assertions eingesehen.

**Nur Snapshot-Metadaten, nicht der Thread.** Titel, Zustand und Mergedatum wurden für #374, #557, #1373, #1529, #1992, #2510, #2513, #2550, #2551 und #2665 aus dem Stream gelesen.

**Nicht gelesen.** Dazu gehören PR-Diffs, Review-Kommentare, Timelines, Commits, die SourceForge-Originale der 10 Vorgänge mit `sf-automigrated`, Stylesheets- und romajs-Issues, Council-Protokolle, Release-Notes und die Threads der verlinkten Vorgänge.

## Prüfung der 32 IDs gegen das Manifest

| Prüfung | Ergebnis |
|---|---|
| Labelabfrage `Status: Wontfix` auf `kind: issue` und `kind: pull-request` im Stream, SHA-256 `4b85f84c34010d8d3ed35fac86f13fc7ee1fcdcffd155fd76160cd2383a5bba3` | 32 Nummern; die Menge ist identisch mit dem Paket und dem Abgleich vom 2026-09-11 |
| Manifest `2026-09-11-wontfix-context.yaml` | 64 Antworten mit HTTP 200, je ein Item- und ein Kommentarendpunkt für jede der 32 Nummern; `counts` 32 und 262; `gaps: []` |
| Rohdateien `corpus/raw/<raw_path>` | alle 64 vorhanden; SHA-256 und Bytezahl stimmen mit dem Manifest überein |
| Paginierung | jede Kommentarantwort hat weniger als 100 Einträge, daher keine ungelesene Folgeseite bei `per_page=100` |
| Paket gegen Rohantworten | Kommentar-URLs, Reihenfolge, Texte und `created_at` sind identisch (262 Kommentare); Item-URL, Text, Zustand und `closed_at` sind identisch; das Feld `comments` stimmt jeweils mit der Kommentarzahl überein |
| Labels am 2026-09-11 gegen den Snapshot vom 2026-09-06 | für alle 32 identisch |
| Art | 30 Issues und 2 PRs (2643, 2767), konsistent mit `pull_request` in der Itemantwort |
| Einzeldateien `<nummer>.json` | alle 32 Prüfsummen stimmen mit `original_sha256` im Paket überein |

Geprüfte Nummern: 542, 547, 550, 559, 566, 568, 576, 1049, 1276, 1323, 1348, 1375, 1396, 1426, 1429, 1430, 1485, 1631, 1636, 1660, 1676, 1712, 1787, 1880, 1889, 2247, 2444, 2570, 2622, 2643, 2684, 2767.

## Auswahlbefunde

1. **Das Label bezeichnet sehr verschiedene Ausgänge.** Nur 13 der 32 Fälle enthalten einen Kommentar, der eine Entscheidung eines Gremiums oder einer Gruppe gegen die beantragte Änderung berichtet: 542, 550, 568, 576, 1276, 1323, 1676, 1787, 1880, 1889, 2247, 2444 und 2570. Die übrigen Fälle verteilen sich so:
   - 6 Diskussionsabschlüsse ohne berichteten Beschluss: 1396, 1429, 1430, 1485, 1631, 1636
   - 5 Verlagerungen in ein anderes Repositorium: 559, 566, 1348, 1426, 2684
   - 2 Duplikate: 547, 1375
   - 3 Erledigt-Behauptungen: 1049, 1660, 1712
   - 2 zurückgezogene PRs: 2643, 2767
   - 1 Werkzeugproblem außerhalb von TEI: 2622

   In 2684 (C2, issuecomment-2754555578) heißt es ausdrücklich, das Label sei gerade nicht als Ablehnung gesetzt worden. `knowledge/operations.md` § Select, Schritt 4, beschreibt `Wontfix`-Fälle als erwogen und abgelehnt. Diese Beschreibung trifft im gelesenen Satz höchstens auf die 13 Fälle der Art A zu, und auch dort nur als Kommentarbericht ohne geprüftes Protokoll. Ob die Regel präzisiert wird, entscheidet Root.
2. **Drei Charakterisierungen im historischen Record sind nicht haltbar.** Der Record `2026-09-06-text-and-document-structures-run1.md` schreibt in der Zeile zu B2, 1660 habe die Umbenennung von `lb` abgelehnt. Nach dem Thread war der Punkt bereits über #1529 erledigt (C1, issuecomment-311052437). Die englische Glosse von `lb` lautet in 4.12.0 „line beginning“ mit `versionDate` 2017-06-14. In der Zeile zu B4 heißt es, 1049 und 2767 seien abgelehnt worden. Tatsächlich wurde 1049 mit der Annahme geschlossen, die Fälle seien seit der XPointer-Revision entfallen (C18, issuecomment-173316942). 2767 wurde zugunsten eines PR zurückgezogen, der die Regel entfernt (C2, issuecomment-3263840676). Alle drei Fälle sind Beispiele dafür, dass „Wontfix“ nicht „abgelehnt“ heißt. Der historische Record ist write-once; ob eine Korrekturnotiz nötig ist und wo sie steht, entscheidet Root.
3. **Das Label zeigt nicht den P5-Endzustand.** 1429 wurde 2016 ohne Änderung geschlossen, doch in 4.12.0 erlaubt `locus` das Element `hi`. Umgekehrt stimmen die Deklarationen von 2247 (`handShift` nicht in `model.global`), 1485 (`figure` in `model.global`) und 2570 (`@url` verpflichtend) mit einem unveränderten Stand überein. Weil kein Releasevergleich gemacht wurde, ist in keinem Fall ein zeitlicher oder ursächlicher Zusammenhang belegt.
4. **Änderungen gegenüber dem titelbasierten Abgleich.**
   - Gruppe 542, 1631, 1676: 542 wird zur Aufnahme empfohlen. 1631 wird mit Budget für M&E Q6 zurückgestellt. 1676 wird zu ODD and Customization zurückgestellt, weil es das Element `ref` betrifft, nicht das Attribut `@ref`.
   - Strukturgruppe: 1485 und 2247 werden zur Aufnahme empfohlen. 1880, 2570 und 2643 werden mit Budget zurückgestellt, 1049 zu Annotation and Overlap. 1430, 1660, 1712 und 2767 werden ausgeschlossen.
   - Gruppe „anderes Thema“: 550, 1276, 1323, 1889 und 2444 bleiben zurückgestellt. 1787 geht an einen künftigen Header-Lauf von M&E. 1375 wird als Duplikat von #1373 ausgeschlossen, 2684 als Werkzeugproblem mit der Spur Stylesheets#730.
   - Titelgruppe: 1636 wird zu Annotation and Overlap zurückgestellt, zusammen mit #374. 547, 559, 566, 568, 576, 1348, 1396, 1426, 1429 und 2622 werden ausgeschlossen.
   - 1396 und 1712 tragen einen Ausschlussgrund außerhalb der festen Liste; das ist in der Tabelle vermerkt.
5. **Aufnahmeempfehlungen.**
   - 542 für M&E Q3 und Q7: Eine Subgruppe erklärt die Trennung von Nennung und Record als Entwurfsabsicht, ein Ablehnungsbeschluss wird berichtet.
   - 1485 für TS Q3: Die Diskussion begründet, warum `body` ein nicht globales Element verlangt und warum Projekte auf ODD-Anpassung verwiesen werden.
   - 2247 für TS Q1 und Q3: Ein Beschluss wird berichtet; der Thread unterscheidet eine Milestone-Markierung von einem umschließenden Attribut für dasselbe Phänomen.

   Alle drei würden das Budget des nächsten Laufs belasten. Sie brauchen die Aufnahme als zitationsbasierte Quelle mit Satzzitaten nach `knowledge/data.md`. Die berichteten Beschlüsse wären als berichtet zu destillieren, nicht als Gremienbeleg. Daraus folgt keine Pflicht, weitere Fälle zu destillieren.

## Mögliche Auswirkungen auf bestehende Claims

Kein Destillat, keine Assertion und kein Kapitel verweist auf einen der 32 Vorgänge. In diesem Paket wird **keine Widerspruchswirkung** gegen eine bestehende Assertion behauptet. Folgende Berührungspunkte bestehen:

| Assertion (Grounding) | Vorgang und Locator | Einschätzung |
|---|---|---|
| `p5-resp-should-point-to-an-element-that-clarifies-the-agents-role-rather-than-to-a-person-or-org` (`20_distillates/documents/tei-p5-att.global.responsibility-4.12.0#^s7`) | 1631, C3 issuecomment-296417345 | Ein Kommentar von 2017 beschreibt `@resp` auf `change` als Verweis auf die verantwortliche Person. Das ist eine Nutzungsschilderung, keine Aussage über die Bemerkungen in 4.12.0, und widerspricht der Assertion deshalb nicht. Relevant wäre sie erst, wenn ein Kapitel die Bemerkungen als tatsächliche Praxis verallgemeinert. |
| `p5-rolename-excludes-the-role-a-person-has-in-a-context`, `p5-guidelines-group-information-about-a-person-as-distinct-from-references-to-a-person-within-person` | 542, C5 issuecomment-145103053, C7 -145103056, C20 -151794157 | Die berichtete Subgruppen- und Council-Position (biografische Angaben in `person`, Verweis per `@ref`) ist mit den Assertions vereinbar. Sie ist Prozesskontext, keine Stützung der P5-Aussage selbst. |
| `structure-p5-pb-associates-page-image` | 2570, C2 issuecomment-2383901439, C4 -2397092899 | Kein Widerspruch. Die Unterscheidung zwischen `@facs` und `@url` ist eine zusätzliche Einzelstimme, der F2F-Ausgang betrifft `figure` und `graphic`. |
| Offene Frage in `MOC-Text and Document Structures` zu Konzepten, die über den XML-Baum gekoppelt bleiben | 2247, 1485 | Das ist Kandidatenmaterial, kein Befund. |

Auch Records und Regeln sind betroffen, ohne selbst Claims zu sein:
- die drei Charakterisierungen im TS-Record (Befund 2);
- die Formulierung in `knowledge/operations.md` § Select, Schritt 4 (Befund 1);
- der offene Punkt in `knowledge/state.md` zu den 32 Wontfix-Kandidaten, der mit diesem Paket inhaltlich disponiert ist. Die Aktualisierung von `knowledge/state.md` bleibt Root vorbehalten.

## Offene Grenzen

- Berichtete Beschlüsse wurden nicht gegen Council-Protokolle geprüft. Implementierungs- und Releaseangaben aus Kommentaren sind unbelegt, darunter 1660 (Commit), 1712 (Release 3.1.0), 1049 (Revision) und 2444 (PR #2513).
- Die Deklarationsbefunde 4.12.0 sind Stichproben einzelner Spezifikationen. Sie ersetzen weder einen Releasevergleich noch belegen sie einen Zusammenhang mit einem Thread.
- PR-Diffs, Reviews, Timelines, verlinkte Threads, SourceForge-Originale und externe Repositorien sind nicht erfasst. Das betrifft insbesondere #1529, #2551, #2665, #374, #1373, #1992, #2510, Stylesheets#125, Stylesheets#137, Stylesheets#138 und Stylesheets#730.
- Die Dispositionen sind Auswahlurteile eines einzelnen Reviewers (Opus 5). `knowledge/governance.md` weist Auswahlurteile der Fable-Familie zu. Eine unabhängige Zweitprüfung, ein Machine Review und die menschliche Verifikation fehlen.
- Die Auswahl ist nur für die benannte Labelmenge `bounded-complete`. Über andere Gegenbelege zu den Themenfragen sagt sie nichts.

## Abschlussprüfungen

| Prüfung | Ergebnis |
|---|---|
| Vollständigkeit der Tabelle in `workbench/selections/2026-09-11-wontfix-context.md` | 32 Fallzeilen mit 32 eindeutigen Nummern, identisch mit der Paketmenge und numerisch sortiert; jede Zeile hat 7 nicht leere Zellen; das Linkziel stimmt mit Nummer und Art (`issues` oder `pull`) überein |
| Locatoren | alle `Ck`- und `issuecomment`-Angaben in der Tabelle und in dieser Datei lösen zum angegebenen Kommentar des Pakets auf; keine Abweichung |
| Übersichtszählungen | Dispositionen 3 / 13 / 16 und Verlaufsarten 13 / 6 / 5 / 2 / 3 / 2 / 1 stimmen mit den Tabellenzeilen überein |
| Personenbezug | die Suche nach den im Paket vorkommenden Namen und Kennungen der Beteiligten liefert nur TEI-Attributnamen |
| `git diff --check -- <beide Dateien>` | Exit 0 ohne Ausgabe; beide Dateien sind untracked, deshalb prüft der Befehl sie nicht inhaltlich |
| `git diff --no-index --check /dev/null <datei>` für beide Dateien | keine Whitespace-Befunde; Exit 1 zeigt hier nur die neue Datei an |
