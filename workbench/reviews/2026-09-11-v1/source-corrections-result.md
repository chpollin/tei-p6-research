# V1-Arbeitspaket Quellenkorrekturen: Ergebnis

Integrator-Nachtrag aus der neuen Blindprüfung: ND ^s42 bewahrt jetzt auch
„in much the same way“ (b141); die nachgelagerte Assertion
`p5-guidelines-distinguish-names-for-places-from-other-data-about-places-as-they-do-for-people`
und Kapitel 08 müssen dieses „much“ ebenfalls erhalten. NH ^s20 bewahrt
„sometimes called chaining“ (b34). Keine Assertion gründet auf NH ^s20.
Diese beiden Änderungen folgen dem ursprünglichen Paketbericht und erhalten
erneute Prüfungen im finalen Lauf.

Stand 2026-09-11. Basis `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0` mit dem uncommitteten Arbeitsstand. Umfang: vorhandene `20_distillates/documents/tei-p5-*.md` und `20_distillates/publications/teic-tei-issue-*.md`. Quelltexte und Reviewerbegründungen wurden als Daten behandelt. Code, Repräsentationen, Assertions, Kapitel, Manifeste und Wissensdokumente blieben unverändert.

## Grundlage

- Befundliste `corpus/raw/review-contexts/2026-09-11/v12-current-findings.json`: 38 Nicht-Pass-Urteile im Umfang.
- Erneutes Einlesen beider Teilrunden mit `tools.full_review.collect` (nur lesend), zuletzt nach allen Änderungen: 544 von 595 Einheiten beurteilt, alle 361 Einheiten des Umfangs beurteilt. Hinzu kamen 20 Nicht-Pass-Urteile aus `distillate-complete`-Einheiten. Insgesamt wurden 58 Urteile geprüft.
- Jedes Urteil wurde gegen das eingebettete XML der Repräsentation beziehungsweise gegen den Publikationskontext aus `all-publication-contexts.json` geprüft. Die Prompts stammen aus `primary-v12-1/units.json` und `primary-v12-2/units.json`.
- Die Reviewer der Urteile gehören zur Familie Opus, ebenso dieser Bearbeiter. Die Einschränkung gleicher Modellfamilie gilt daher auch für diese Nacharbeit.

## Status und Prüfbuchungen

Jedes inhaltlich geänderte Destillat steht jetzt auf `grounded`. Frühere `machine-review`- und `validation`-Daten wurden entfernt, weil sie den alten Inhalt betrafen. Ein neues Validierungsdatum wurde nicht gebucht. `updated` steht auf 2026-09-11.

Für die vier geänderten Publikationsdestillate steht `checked.quote: 2026-09-11`. Die Prüfung lief tatsächlich, und zwar nach der letzten Zitatänderung:

- `check_wave1_sources` mit beiden Aufnahmemanifesten gegen den lokalen Rohspeicher;
- `full_review.publication_context` gegen die wiederhergestellten Originalkontexte, mit normalisierten Leerräumen.

Zitate wurden ausschließlich wörtlich erweitert, und zwar ohne Personennamen. Deshalb bleiben einige Erweiterungen kürzer als der Satz im Original.

| Datei | Vorher | Nachher |
|---|---|---|
| anchor, att.canonical, att.datable, att.global.responsibility, att.global.source, att.personal, guidelines-nd, person, place, rs, span, state, test-testnames | `validated` | `grounded`, `checked: {}` |
| teic-tei-issue-337, -1414, -2739 | `validated` | `grounded`, `checked.quote: 2026-09-11` |
| teic-tei-issue-1400 | `grounded`, quote 2026-09-07 | `grounded`, `checked.quote: 2026-09-11` |
| att.fragmentable, att.global.linking, div, guidelines-ds, guidelines-nh, pb, test-testoverlap | `grounded` | `grounded` (nur `updated`) |

`att.editlike` und `annotation` blieben unverändert. Ihre einzigen Befunde sind Instrumentbefunde (siehe unten).

## Tatsächliche Änderungen

Locatoren von Dokumentquellen verweisen auf Blöcke der unveränderten Repräsentation `10_markdown/documents/<slug>`. Locatoren von Publikationen verweisen auf GitHub-Records aus dem Kontext. Die Spalte „Folgen“ nennt Assertions, die auf dem Statement gründen.

### Guidelines ND (`tei-p5-guidelines-nd-4.12.0`)

| Claim | Fehler | Locator | Korrektur | Folgen |
|---|---|---|---|---|
| ^s3 | Bedingung des einzelnen Beispiels `ref="#DPB1"` zu einer allgemeinen Voraussetzung von `ref` verallgemeinert; `role` leicht umformuliert | `#^b8`, `/div[1]/div[1]/div[1]/p[1]` | Die Existenzbedingung gilt jetzt nur für die Beispielkodierung mit `DPB1`; die Alternative eines anderen Dokuments per URI steht dabei; `role` folgt dem Wortlaut („minimal information about the person name“) | `p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link`: das Statement enthält die Verallgemeinerung und muss nachgezogen werden |
| ^s10 | Beispiel („e.g.“) zur Bedingung gemacht | `#^b35`, `/div[1]/div[2]/div[1]/p[10]` | „when it is used as a surname, for example by …“ | keine |
| ^s17 | „may itself be regarded“ zur Feststellung gemacht; „simply“ fehlte | `#^b53`, `/div[1]/div[2]/div[3]/p[2]` | Modalität und Wortlaut wiederhergestellt | keine |
| ^s24 | Schluss aus „all this“ auf die Quellenabhängigkeit allein verengt | `#^b87`, `/div[1]/div[3]/div[1]/p[4]` | Alle drei Prämissen (Datierung, Wechselwirkung mit Merkmalen, Quellen) und „taking all this into account“ | `p5-each-statement-about-a-life-must-be-documentable-and-time-framed`: H1 und Statement tragen das falsche „because“ |
| ^s34 | Begründung „since“ eingefügt; „may be grouped“ zu „grouped by“ gemacht | `#^b122`, `/div[1]/div[3]/div[2]/div[2]/p[2]` | Aussagen nebeneinander, Gruppierung als Möglichkeit | keine |
| ^s42 | „may be useful“ zu „useful for“ gemacht | `#^b141`, `/div[1]/div[3]/div[4]/p[1]` | Modalität und vollständige Aufzählung | `p5-guidelines-distinguish-names-for-places-from-other-data-about-places-as-they-do-for-people` prüfen |
| ^s54 | „This may be useful“ zu „which serves“ gemacht | `#^b184`, `/div[1]/div[3]/div[5]/p[3]` | Modalität wiederhergestellt | keine |
| Term *referring string* | Definition, die die Quelle nicht gibt | `#^b46` | Als Markierung mit `rs` im Unterschied zu `name` beschrieben | – |
| Offene Fragen 1, 3, 5 | Falsche Prämissen („only“; `person` neben `relation`; „only through listPerson“) | b55-Fußnote; b124, b207; b95, b108, b193 | Prämissen quellengetreu | – |

### Guidelines DS (`tei-p5-guidelines-ds-defaulttextstructure-4.12.0`)

| Claim | Fehler | Locator | Korrektur | Folgen |
|---|---|---|---|---|
| ^s23 | „explicitly extends“ statt „no implication that … apply only to newspaper texts“ | `#^b52`, `/div[1]/div[2]/div[2]/p[2]` | Wortlaut der Verneinung | keine |
| ^s28 | Garantie der Core-Elemente „in all cases“ ausgelassen | `#^b61`, `/div[1]/div[2]/div[4]/p[1]` | Garantie aufgenommen | keine |
| ^s29 | „same module“ zu „different modules“ gemacht; „may appear at any point“ fehlte | `#^b62`, `/div[1]/div[2]/div[4]/p[2]` | Wortlaut | keine |
| ^s30 | „or other purposes“ ausgelassen; „should be used“ fehlte | `#^b65`, `/div[1]/div[3]/p[1]` | Beide Hälften vollständig | `structure-p5-floatingtext-interrupts-resumable-text` erneut prüfen (Inhalt bleibt gedeckt) |
| ^s33 | „anthologies of short extracts such as commonplace books“ und „may often be preferable“ verloren | `#^b77`, `/div[1]/div[3]/div[1]/p[11]` | Geltungsbereich und Modalität | keine |
| ^s39 | „some information about the kind“ zu voller Identifikation gemacht; „when … rendered“ fehlte | `#^b89`, `/div[1]/div[4]/p[3]` | Wortlaut | `structure-p5-divgen-processing-is-application-defined`: H1 und Statement übernehmen „what kind“ und müssen nachgezogen werden |
| ^s48 | Unbelegtes Ziel „infrastructure discussion“ | `#^b115`, `/div[1]/div[8]/p[1]` | „the section it points to as STIN“ | keine |
| Appraisal | „normative source“ vom Kapitel nicht selbst behauptet | ganze Quelle | Guidelines-Prosa am Release, Empfehlung und Erlaubnis | – |

### Guidelines NH (`tei-p5-guidelines-nh-non-hierarchical-4.12.0`)

| Claim | Fehler | Locator | Korrektur | Folgen |
|---|---|---|---|---|
| ^s30 | Rahmung „beyond ordinary XML processing“ statt „non-XML methods“; Datenmodelle fehlten | `#^b48` mit b46/b47 | Rahmung aus dem Abschnitt; Concurrent-Markup-Eintrag genannt | keine |
| ^s31 | Grund „since TEI is currently based on XML“, „certainly“ und die Kennzeichnung der Ansätze fehlten (gleiche Passage, Versionsgrenze) | `#^b49`, `/div[1]/div[5]/p[2]` | Wortlaut | keine |
| Appraisal | wie DS | – | wie DS | – |

### Spezifikationen

| Datei, Claim | Fehler | Locator | Korrektur | Folgen |
|---|---|---|---|---|
| pb ^s7 | Sprachgrenze: nur die englischen Remarks bevorzugen `break`/`ed`/`edRef`; die französischen Remarks weisen die Wortbrechung `type` zu | `#^b22` (`remarks[1]`, en); b23 (fr) | „The English pb remarks …“ mit „may“/„should be preferred“ | keine |
| pb ^s5, ^s6 | Gleiche Sprachgrenze; die japanischen Remarks verlangen stattdessen eine konsistente Zählpolitik | `#^b22`; b24 (ja) | Auf englische Remarks begrenzt, Wortlaut | `structure-p5-pb-number-and-sequence` (^s6) prüfen |
| pb Appraisal | „distinguishes … observed processor behavior“ ohne beobachtetes Verhalten | – | „records no processor behavior“ | – |
| att.fragmentable ^s2 | „specifies whether or not its parent element is fragmented“ zu „describes fragmentation“ verkürzt; „two or more“ fehlte | `#^b3`, `/classSpec[1]/attList[1]/attDef[1]/desc[1]` | Wortlaut | keine |
| att.fragmentable ^s6 | `should` zu `require` gemacht | `#^b8`, `…/remarks[1]` | „The English remarks state that … should be used only where …“ | keine |
| att.fragmentable Lead, Appraisal, offene Frage | „selected examples“ und „Examples establish“ ohne `exemplum`; „referenced classes“ ohne Klassenmitgliedschaft | XML der Quelle | Lead und Appraisal berichtigt; offene Frage zum Default N und zum XML-Kommentar über dessen Deprecation ergänzt | – |
| att.global.linking ^s3 | Vergleich „slightly looser relationship than … the preceding example“ ausgelassen | `#^b26`, `…/attDef[1]/exemplum[2]` | Vergleich und Korrespondenz aufgenommen | keine |
| att.global.linking ^s7, ^s14 | `should` zu Verarbeitungsanweisung beziehungsweise Empfehlung gemacht; Sprachgrenze (fr: „doit“) | `#^b61`, `#^b113` | „The English … remarks state that … should …“ | keine |
| att.global.linking Lead, Appraisal | „local declarations“ ohne entsprechende Statements; Appraisal-Floskel wie pb | – | Lead auf Beschreibungen, Remarks und ein Beispiel begrenzt | – |
| div ^s6 | Zentrale Alternation des Inhaltsmodells ausgelassen | `#^b17`, `/elementSpec[1]/content[1]` | Vollständige Struktur des Inhaltsmodells | keine |
| div Appraisal | Floskel wie pb | – | wie pb | – |
| anchor ^s2 | Wertbedingungen (eindeutig im Dokument, syntaktisch gültiger Name) ausgelassen | `#^r2`, `/elementSpec[1]/remarks[1]/p[1]` | Wortlaut mit Bedingungen | keine |
| att.canonical Term, 2 offene Fragen | „specification that provides“ statt Klasse; unterstellte Eindeutigkeitspflicht von `key`; unterstellte Textgeschichte des XML-Kommentars | `#^r1`, `#^r3`, Kommentar in `remarks` | Neutral formuliert | keine |
| att.datable Appraisal, offene Frage | „normalizes temporal information“ statt „provides attributes … to provide normalized values“; Beispiel `calendar` von außen | `#^r3` | Wortlaut; Beispiel entfernt | keine |
| att.global.responsibility Term, Appraisal | Parenthese „(person or org)“ als Definition; Wertbereiche und Träger angeblich in XML-Deklarationen dieser Quelle festgelegt, obwohl `classes` leer ist und die Datentypen anderswo definiert sind | `#^r4`; XML | Term als Glosse; Appraisal nennt leere Mitgliedschaft und fremd definierte Datentypen | keine |
| att.global.source Term, Appraisal | „specification“ statt Klasse; drei Überdehnungen (Elementliste in r3, Datentyp im XML, japanische Remarks zur Kombination) | `#^r1`, `#^r3`; XML | Auf englischen Text begrenzt, Elementliste genannt | keine |
| att.personal Appraisal, 2 offene Fragen | „two attributes“ gegen eigene Frage; „name component“ nicht in r1; englische Glossen übersehen | `#^r1`–`#^r6`; XML-Glossen | Berichtigt | keine |
| rs 2 offene Fragen, Appraisal | `att.canonical` als Mitgliedschaft unterstellt; Klassenmitgliedschaft angeblich nur aus Klassenspezifikationen | XML `classes` | Deklarierte Klassen genannt; Mitgliedschaft als XML-Deklaration dieser Quelle | keine |
| span Appraisal | „release-specific annotation mechanism“ vermischt Zeit und Version | – | „descriptions … the specification carries at the pinned release“ | keine |
| state Term *trait*, Appraisal, offene Frage | Bedingung „If you wish to distinguish“ verloren; „twice over“; Kriterium Volition ausgelassen; Attribute angeblich im XML deklariert; zh-TW-Beschreibung übersehen | `#^r1`, `#^r2`; XML | Berichtigt | keine |
| person 2 offene Fragen, Appraisal | Hedge „presumably declared“ verloren; `xml:id` angeblich nur in Beispielen; Container angeblich in XML-Deklarationen | XML-Exempla, `classes` | Berichtigt | keine |
| place Appraisal | Unbelegtes Ziel „geographic names chapter“ | Pointer `#NDGEOG` | Pointer statt Kapitelname | keine |
| test-testnames ^s1 | Interpretation „a generic phrase standing where a name … would stand“ | `#^b1` | Nur der Befund „reads "The title"“ | keine |
| test-testnames ^s5 | `rend="nolist"` als Präsentationsanweisung gedeutet | `#^b34` | „a `rend` value is attached“ | keine |
| test-testnames Lead, Appraisal | Zweckzuschreibung „for names and dates“; „which attribute carries the identifier“; allgemeine Prämisse über Testdateien | – | Neutral und quellengebunden | – |
| test-testoverlap Appraisal | „placeholder metadata“ unverankert; nur Seitenmarken in Absätzen genannt | `#^b1`–`#^b6` | pb-Verteilung vollständig; Headerangabe als ausgeklammert markiert | – |

### Publikationen

| Datei, Claim | Fehler | Locator | Korrektur | Folgen |
|---|---|---|---|---|
| 1400 ^s1 | Bedingung „Unless it has some semantic value that I am missing“ und Gegenstand verloren | Record 116172534, Issue-Beschreibung 2015-11-10 | Bedingung im Statement und im Zitat; „the option for numbered divisions“ | keine |
| 1400 ^s2 | Subjekt und Grundlage (ausschließliche Nutzung nummerierter Divs) verloren | Record 155582272, `#issuecomment-155582272` | Zitat um „We of course use numbered divs exclusively.“ erweitert | keine |
| 1414 ^s6 | Bedingung „But then“ (Antwort auf den Vorschlag aus Kommentar 2) verloren | Record 165053676 | Bezug auf den Vorschlag von Kommentar 2 im Statement; Zitat unverändert, weil die Erweiterung einen Namen enthielte | keine |
| 2739 ^s8 | Fragezeichen verloren; zweite Satzhälfte fehlte | Record 3158291195 | „in a sentence ending with a question mark“; ganzer Satz zitiert, Schreibung „att naming“ erhalten | keine |
| 2739 ^s9 | Bedingung „if either of those hierarchies were real … then“ verloren | Record 3158291195 | Bedingung, Vergleich `att.global.analytic` und Frage im Statement und Zitat | keine |
| 2739 ^s14 | Hedge „i suspect … so“ verloren | Record 3158532441 | Vermutung und Folgerung in einem Statement und einem Zitat | keine |
| 337 ^s8 | Weitergabe aus zweiter Hand und die Gruppe „computer sciency types“ verloren | Record 145099874 (Kommentar 7) | Weitergegebener Bericht an tei-council vom 2011-11-13 mit Gruppe; Zitat ohne Namen erweitert | keine |
| 337 ^s10 | Frage einem Kommentator statt einer weitergegebenen E-Mail eines externen Experten zugeschrieben | Record 145099876 (Kommentar 9) | E-Mail mit „former colleagues at W3C would all say“; Zitat ohne Namen erweitert | keine |
| 337 ^s11 | Status „proposed“ des Unterausschusses verloren | Record 145099877 (Kommentar 10) | „the subcommittee that another participant proposed in a SourceForge tracker item and on tei-council“; Zitat bis „proposed by“ | keine |
| 337 ^s14 | Grundlage „Per discussion in Ann Arbor“, handelnde Person, Begründung und Review verloren | Record 145099879 (Kommentar 12) | Alles im Statement nach Rolle; Zitat bis „regardless of the outcome of“ (Name folgt) | keine |
| 337 ^s16 | Geltungsbereich (Registrierung von URI-Schemata bei der IANA nach RFC 4395) verloren | Record 145099880 (Kommentar 13) | Geltungsbereich im Statement und Zitat | keine |
| 337 ^s20 | Ausnahme für externe Vokabulare wie `<country key="FR"/>` ausgelassen; Format unbenannt | Record 145099880 (Kommentar 13) | Format `ref="tag:example.org,2012:foo"` und Ausnahme im Statement und Zitat. ^s21 bleibt als Anker bestehen | `teic-tei-issue-337-commenter-excepts-values-that-already-refer-to-an-external-vocabulary` (^s21) unverändert gedeckt |

## Instrumentbefunde (keine Änderung)

| Befund | Prüfung am Original | Einordnung |
|---|---|---|
| span ^s2 `@from`, join ^s3 `result`, join ^s4 `scope`, att.global.linking ^s2 `corresp`, att.fragmentable ^s2 `part` | Das eingebettete XML trägt `attDef ident="from"`/`"to"`, `"result"`/`"scope"`, `"corresp"` an erster Stelle, `"part"` | Fehlender XML-Vorfahrenkontext in Instrument v1.2. Die Aussagen sind wahr und bleiben unverändert (bei att.fragmentable ^s2 wurde nur der sachliche Teil korrigiert). |
| Release-Label „TEI P5 4.12.0“ in anchor, annotation, att.canonical, att.datable, att.editlike, att.fragmentable, ND-Lead | `sources/locks/tei-p5-4.12.0.yaml` bindet `release_tag: P5_Release_4.12.0` an `113e933e21f016e2655518321e9d10214b8d9fcb`; Repräsentationsmetadaten nennen Titel und Commit | Der Prompt enthielt die Quellenidentität ohne Lock. Kein Destillatfehler. |
| 1400 ^s3 Snapshot 2026-09-06 | `sources/manifests/2026-09-07-text-structures-citations.yaml`: `observed_at: 2026-09-06T09:49:41Z`, Label `Status: Reconsider for P6`; Wiederherstellung 2026-09-11 mit `byte_identity: true` | Der Kontext zeigte nur das Reproduktionsdatum. Die Aussage ist wahr. |
| ND Term *persona* (b108 nicht im Kontext) | b108 enthält die Definition wörtlich | Auswahlgrenze der Gesamttextprüfung bei über 240.000 Zeichen |
| „The section audit records the examined units and exclusions“ (Appraisal) | Audit vorhanden in `workbench/reviews/2026-09-07-text-structures-run1/README.md` | Projektseitiger Verweis in einer Appraisal, kein Quellenanspruch |

## Verworfene oder nur teilweise übernommene Befunde

- span, fehlende Aussage zu `@to` (r3): Der Lead begrenzt den Umfang ausdrücklich auf Definition und `from`. Eine Auslassung ist keine Falschaussage.
- div, übrige nicht berichtete Mitgliedschaften, Glosse und `listRef`: ^s2 sagt „include“ und bleibt wahr. Übernommen wurde nur die Inhaltsmodell-Alternation in ^s6.
- att.global.linking, ausgelassenes erstes `corresp`-Beispiel und fehlende Deklarationen: Statt neuer Statements wurde der Lead begrenzt.
- att.fragmentable ^s5, Deprecation-Kommentar: Der Kommentar liegt in keinem Block. Er steht deshalb als offene Frage und nicht als Core statement.
- ND Term *relative place name* ohne Core statement: Die Definition ist durch b65 gedeckt. Terms verlangen kein Core statement.

## Offene Punkte

1. **Zitatreichweite.** Bei 1414 ^s6, 337 ^s11 und 337 ^s14 geht das Statement über das Zitat hinaus: Bezug auf Kommentar 2, Status „proposed“ mit SourceForge und tei-council, Grundlage „Ann Arbor“. Die fehlenden Teile stehen in Originalsätzen mit Personennamen. V1-Einheiten liefern den vollständigen Kontext. Ein reines Zitatpaar des historischen Cutters zeigt diese Teile nicht.
2. **Assertion-Befunde für Root, Destillate wahr und unverändert.**
   - `p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur`: Zusatz „on the same element“, H1 schreibt die Aussage der Klasse statt den Remarks zu, „English“ fehlt.
   - `p5-namesdates-represents-the-referent-and-the-name-independently`: „in the chapter on names, dates, people and places“ ist durch ND ^s2 nicht gedeckt.
   - `p5-core-elements-state-the-kind-of-referent-only-through-type`: „namesdates module“ nicht durch ND ^s1 gedeckt (Modulname stünde in ND ^s59).
   - `p5-rs-contains-a-general-purpose-name-or-referring-string`: „core element“ durch rs ^s1 nicht gedeckt.
   - `structure-p5-join-combines-virtual-elements`: Bedingung „With scope root“ von join ^s5 verloren.
3. **Nachzuziehende Assertions wegen geänderter Statements:** siehe Spalte „Folgen“, insbesondere `p5-each-statement-about-a-life-must-be-documentable-and-time-framed`, `structure-p5-divgen-processing-is-application-defined` und `p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link`.
4. **Statusfolgen.** 57 `validated`-Assertions stehen jetzt über `grounded`-Ankern (`E-LADDER`):
   - 24 auf guidelines-nd;
   - 7 auf att.canonical;
   - 6 auf test-testnames;
   - 4 auf teic-tei-issue-1414;
   - je 2 auf att.global.responsibility, span, state und teic-tei-issue-337;
   - je 1 auf anchor, att.datable, att.personal, att.global.source, person, place, rs und teic-tei-issue-2739.

   Root setzt sie herab oder lässt sie neu prüfen. Kapitel mit diesen Assertions sind entsprechend betroffen.
5. **Blindprüfung.** Alle 24 geänderten Destillate brauchen neue Paare und Urteile. Unveränderte Destillate des Umfangs wurden nicht angefasst.

## Ausgeführte Prüfungen

| Prüfung | Ergebnis |
|---|---|
| `python tools/check_wave1_sources.py --manifest sources/manifests/2026-09-06-entities-run2-citations.yaml --references references/entities-run2.json` | `OK: 58 quotations match 3 local publication sources and distillates.` |
| `python tools/check_wave1_sources.py --manifest sources/manifests/2026-09-07-text-structures-citations.yaml --references references/text-structures-run1.json` | `OK: 5 quotations match 2 local publication sources and distillates.` |
| `review.cut_pairs(root, problems)` | 646 Paare, 0 Probleme. Ein früherer Zwischenlauf hatte die Problemliste nicht übergeben; das hier genannte Ergebnis stammt aus dem korrekten Lauf. |
| `full_review.publication_context` gegen `all-publication-contexts.json` | 63 Publikations-Quellenpaare des Umfangs, keine Lücke `quote-not-in-context` oder `no-original-context` |
| `python tools/validate.py .` | 61 Fehler, 0 Warnungen; kein Fehler an einer Datei dieses Pakets |
| `git diff --check -- 20_distillates/documents/tei-p5-*.md 20_distillates/publications/teic-tei-issue-*.md` | ohne Befund |

Tests wurden nicht ausgeführt, weil kein Code geändert wurde.

### Integrationsfehler außerhalb dieses Pakets

- 57 × `E-LADDER` in `30_assertions/`: direkte Folge der vorgeschriebenen Herabstufung, Behandlung durch Root (siehe Offene Punkte 4).
- 4 × `E-GENERATED`: generierte Regionen in `MOC-History and Governance`, `MOC-Interoperability and Processing`, `MOC-ODD and Customization` und `MOC-P6 Design` sind veraltet (`tools/inventory.py . --write`). Diese Fehler stehen nicht mit diesem Paket in Zusammenhang.

## Geänderte Dateien

`20_distillates/documents/` (jeweils `tei-p5-<name>-4.12.0.md`), 20 Dateien: `anchor`, `att.canonical`, `att.datable`, `att.fragmentable`, `att.global.linking`, `att.global.responsibility`, `att.global.source`, `att.personal`, `div`, `guidelines-ds-defaulttextstructure`, `guidelines-nd`, `guidelines-nh-non-hierarchical`, `pb`, `person`, `place`, `rs`, `span`, `state`, `test-testnames`, `test-testoverlap`.

`20_distillates/publications/`: `teic-tei-issue-337.md`, `-1400.md`, `-1414.md`, `-2739.md`.

Neu: `workbench/reviews/2026-09-11-v1/source-corrections-result.md`.
