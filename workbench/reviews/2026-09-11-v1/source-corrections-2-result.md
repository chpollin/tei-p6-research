# V1-Arbeitspaket Quellenkorrekturen 2: Ergebnis

Stand 2026-09-11, Basis `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0` mit dem uncommitteten Arbeitsstand. Umfang sind vorhandene `20_distillates/documents/tei-p5-*.md` und `20_distillates/publications/teic-tei-issue-*.md`. Quelltexte, Kontexte und Reviewerbegründungen wurden als Daten behandelt. Repräsentationen, Assertions, Kapitel, MOCs, Manifeste, Code und Wissensdokumente blieben unverändert.

## Grundlage

- Befundliste `corpus/raw/review-contexts/2026-09-11/source-second-corrections-findings.json` mit 26 Urteilen.
- Mehrmaliges Einlesen von `primary-v14-old-sources-1` und `primary-v15-old-sources-2` mit `tools.full_review.collect`, nur lesend. Beim letzten Lauf waren alle 223 beziehungsweise 224 Einheiten beurteilt, mit 16 und 28 Nicht-Pass-Urteilen. Gegenüber der Befundliste kamen 18 Gesamttexturteile hinzu, die hier ebenfalls behandelt sind.
- Geprüft wurde gegen das eingebettete XML und die Leseblöcke der Repräsentationen sowie gegen `all-publication-contexts-v16.json`. Die Urteile beruhen auf den unveränderten v14/v15-Prompts. Mehrere Urteile beurteilen daher den Text vor den Root-Korrekturen.
- Reviewer und Bearbeiter gehören zur Familie Opus. Die Einschränkung gleicher Modellfamilie gilt auch für diese Nacharbeit.

## Status und Prüfbuchungen

- `name`, `idno`, `nym`, `persname` standen auf `validated`. Nach der inhaltlichen Änderung stehen sie auf `grounded` mit `checked: {}`. Die übrigen geänderten Destillate waren bereits `grounded`, bei `note` und `join` wurde `updated` nachgezogen.
- `checked.quote: 2026-09-11` bei 337, 1414 und 2739 bleibt gültig. Der Abgleich mit `check_wave1_sources` lief nach der letzten Zitatänderung. Bei 1400 und 1505 blieben die Zitate unverändert.
- Kein `verified`, keine Konfliktauflösung, keine neuen Anker oder Quellenzuordnungen.

## Von Root korrigierte Aussagen, erneut am Original geprüft

| Claim | Originalpassage | Ergebnis | Assertions |
|---|---|---|---|
| ND ^s42 | b141 „In much the same way … may be useful as a way of normalizing …“ | gedeckt | `p5-guidelines-distinguish-names-for-places-from-other-data-about-places-as-they-do-for-people` |
| ND ^s43 | b144 „significant areas which overlap, and we may therefore wish to regard them as the same place“ | gedeckt | `p5-guidelines-let-an-encoder-regard-a-city-and-its-predecessor-as-one-place` |
| NH ^s20 | b34 „is sometimes called chaining“ | gedeckt | keine |
| NH ^s27 | b43 „It has been noted …“, „Further advantages mentioned in the literature … combined in a single annotation“ | gedeckt | `structure-p5-stand-off-discontinuous-annotation` |
| milestone ^s1 | b4, Bedingungsstellung wie im Original | gedeckt | keine |
| 1505 ^s1 | Record 249580507 „We should introduce a constraint that they must always point to elements of the same type“, Bezug `@next`/`@prev` | gedeckt | keine |
| 337 ^s4, ^s5 | Issue-Beschreibung „Council's vision …“, „Per discussion at TEI Council meeting in Paris“ | gedeckt | `teic-tei-issue-337-author-reports-a-wish-to-deprecate-key-held-back-by-its-wide-use`, `teic-tei-issue-337-author-announces-an-interim-guidelines-change-telling-people-to-switch-to-ref` |
| 1400 ^s3 | Label `Status: Reconsider for P6` in den API-Metadaten, `observed_at 2026-09-06T09:49:41Z` im Feld version | gedeckt | `structure-p6-numbered-divisions-reconsideration-label` |

## Geänderte Core statements

Locatoren von Dokumentquellen verweisen auf Blöcke der unveränderten Repräsentation, Publikationslocatoren auf Records im v16-Kontext.

| Claim | Fehler | Originalpassage | Korrektur | Betroffene Assertions |
|---|---|---|---|---|
| ND ^s4 | Offene Beispielliste „for example because …“ zu geschlossenem „either … or“; „might maintain“ und „probably unnecessary … to expand further“ verloren | b9 | Beispielcharakter, Modalität und Hedge im Wortlaut | `p5-key-serves-cases-where-no-direct-link-is-required` (H1 und Statement tragen „because … or because“ und „as when a project maintains“) |
| ND ^s8 | Äquivalenz auf gleichen `ref` gestützt, `type="person"` der drei Nicht-persName-Beispiele verloren | b28 „synonymous with the element name type="person" … Consequently the following examples are equivalent“ | Die vier Beispielkodierungen mit `rs type="person"`, `name` in `rs type="person"`, `name type="person"` und `persName` benannt | `p5-persname-is-synonymous-with-name-of-type-person` (Statement ohne `type="person"`) |
| ND ^s48 | „This use of multiple place elements“ zu allgemeinem Kontrast verallgemeinert, „should be distinguished“ verloren | b169, vorausgehend b167 „a set of hierarchically grouped places“ | Bezug auf das vorausgehende Beispiel hierarchisch gruppierter Orte, Modalität | keine |
| ND ^s49 | „may be customized … by means of their type attribute“ in die Empfehlung „should be used“ gefaltet | b171 | Empfehlung und Erlaubnis getrennt, Wortlaut der Kategorien und „small number of predefined elements of general utility“ | `p5-guidelines-use-generic-state-trait-and-event-customized-through-type-for-information-about-a-place` (H1, Statement und Support tragen „customized through type … should be used“) |
| NH ^s11 | Konformität den Elementen statt der Methode zugeschrieben, „information or“ fehlte | b20 „this method is TEI-conformant … the method is an extension“ | Methode als Träger, beide Bedingungen im Wortlaut | keine |
| NH ^s12 | „in the markup literature under various names, including“ und „HORSE markup“ verloren, sID/eID als feste Namen, Bedingung „when the features they encode cross-hierarchical boundaries“ fehlte | b21 | Offene Liste mit Literaturzuschreibung, „in the example“, Bedingung | keine |
| NH ^s13 | Nur der nichtkonforme Fall, Deprecation den Elementen zugeschrieben | b21 „Depending on how the modifications are carried out, this method may be TEI-conformant, may represent an extension …, or may produce a non-conformant document“ | Alle drei Fälle der Methode mit ihren Bedingungen | keine |
| NH ^s24 | Zwei der drei Hauptnachteile verloren, „expose“ statt „handled explicitly“ | b39 | Hauptvorteil und alle drei Hauptnachteile mit „like most of the other methods“ und „except in the case of join“ | keine |
| note ^s7 | „it may well be considered unnecessary“ zu einer Erlaubnis gemacht | b17 (`exemplum[6]`, en) | Bedingungen und Hedge im Wortlaut | `structure-p5-note-number-omission-is-conditional` (H1 und Statement „permits omitting“) |
| milestone ^s4 | „should be used“ zu „prescribe“, Beispiele des Geltungsbereichs fehlten | b17 (`remarks[1]`, en) | „should be used … such as chapter or other headings, poem numbers or titles“ | keine |
| testnames ^s4 | Deutung „identified by a code and named … independently of it“ | b30 `<country key="D">Germany</country>` | Nur der Befund, Text „Germany“ | keine |
| 337 ^s3 | URN als allgemeine Wertform von `ref` statt als Teil der berichteten Vereinbarung für Verwendungen von `key` | Issue-Beschreibung „we agreed that uses of `@key` can all be handled by `@ref`, using ref="urn:…"“ | Statement im Rahmen der Vereinbarung, Zitat wörtlich erweitert | keine |
| 337 ^s19 | Zuschreibung der Lösung an einen anderen Teilnehmer in FR 2919640 verloren | Record 145099880 „the solution … proposed on http://purl.org/TEI/fr/2919640 -- for use of the IANA-registered "tag" URI scheme“ | Zuschreibung ohne Namen im Statement, Zitat unverändert | keine |
| 2739 ^s4 | Antwortcharakter „I think this is correct“ verloren | Record 3156043662 | Antwort und Mitgliedschaftskette, Zitat ohne Login erweitert | `teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical` erneut prüfen (Inhalt bleibt gedeckt) |
| 2739 ^s9 | „such as“ zu „as“ | Record 3158291195 | „such as“ | keine |
| 2739 ^s12 | „of their class memberships“ ohne Markierung gekürzt | Record 3158532441 | Statement und Zitat vollständig | keine |
| 1414 ^s3 | „(and I suppose `<org>`, `<bibl>`, and `<biblStruct>`, too)“ gekürzt | Record 122354402 | Statement und Zitat erweitert | `teic-tei-issue-1414-author-proposes-ref-and-key-on-person-and-place` (H1 und Statement nennen nur person und place, Geltungsbereich prüfen) |
| 1414 ^s9 | Bezug von „it“ verloren | Record 165247314 „I was about to suggest doing exactly what [ein Teilnehmer] suggests above. This seems to me to have several advantages: firstly and most obviously it allows …“ | Bezug auf den Vorschlag „above“ ohne Namen, Zitat erweitert | keine |
| 1414 ^s12 | „etc. just for this purpose“ verloren | Record 214396169 | Statement und Zitat erweitert | keine |
| 1414 ^s13 | Bezug „per #1424“ verloren | Record 214511770 | Bezug auf Issue 1424 im Statement, Zitat unverändert, weil die Erweiterung ein Namenskürzel enthielte | keine |

## Geänderte Terms, offene Fragen, Leads und Appraisals

| Datei | Fehler | Korrektur |
|---|---|---|
| ND Term *referring string* | Als Markierungsakt statt als Textsegment definiert (b2, b46) | Textsegment, das mit `rs` ausgezeichnet werden kann |
| ND offene Frage 3 | Fragmente als vollständiger Kontext gelesen, Kommentar zwischen `forename` und `person` übersehen (b207) | Prämisse auf Beispielfragmente mit Blocklinks b93, b116, b124, b125, b207 |
| ND offene Frage 5 | Objektdefinition außerhalb des begrenzten Kontexts | Belegt durch b193 „An object is any material thing whether real, in existence, fictional, missing, or purported“, jetzt mit Blocklinks b182, b193, b95, b108 verlinkt |
| NH Appraisal | „much of its guidance is worded as recommendation or permission“ unzutreffend, Leerformel zum Audit | Klassifikation als konform, Extension oder nichtkonform und Abwägung, beides dem Kapitel zugeschrieben |
| note Appraisal, offene Frage | Floskel zu Prozessorverhalten, Datentypen unterstellt | wie pb, `macro.specialPara` statt Datentypen |
| pb Lead, offene Frage | „local declarations“ bei nur einer Inhaltsdeklaration, Datentypen unterstellt | Lead nennt Inhaltsdeklaration und Remarks, Frage nennt deklarierte Klassen |
| milestone Lead, Appraisal, offene Frage | „selected examples“ ohne Beispiel-Statement, Datentypen unterstellt, Floskel | Lead und Appraisal ohne Beispiele, Klassen `att.milestoneUnit` und `att.spanning` |
| join Lead, Appraisal | „local declarations“ unvollständig, Floskel | „selected declarations“, Appraisal wie pb |
| att.fragmentable Lead | „local declarations“ ohne Datentyp und usage | Default und Werteliste von part benannt |
| span offene Frage | Beschreibung von `to` und Schematron-Constraints weder berichtet noch als ausgeklammert sichtbar | Zusätzliche offene Frage |
| name Appraisal | Totalitätsanspruch „The English text … is one description sentence and one remarks paragraph“ trotz englischer Glosse | Leseblöcke statt englischer Text, Glosse „name, proper noun“ genannt |
| persname Appraisal | Deklarationen der eigenen XML als fremd behandelt | Modul, Klassen, Inhaltsmodell und Glosse „personal name“ als XML dieser Quelle, nur deren Wirkung fremd |
| person Appraisal, offene Frage 6 | Inventar unvollständig, Identifikatorpraxis angeblich in Beispielprosa, vCard-Prosa übergangen | Leseblöcke, Glosse, Inhaltsmodell und Beispiele genannt, Identifikatoren nur im Beispiel-Markup, vCard-Prosa „fictional character“ in der Frage |
| att.global.source Appraisal | Behauptung über die japanischen Remarks außerhalb der Leseblöcke | entfernt, „the Guidelines set“ zu „its English remarks allow“ |
| att.personal Appraisal | Wirkung der Mitgliedschaft als Tatsache | Nur die Deklaration `memberOf key="att.naming"` |
| att.canonical Appraisal | „nothing about whether a key resolves outside the project“ überzogen | r6 und Beispielprosa „requires that an entire external system for key resolution be available“ |
| idno Appraisal | „establishes nothing about where idno may occur“ trotz Mitgliedschaften im XML | Leseblöcke schweigen, XML deklariert, Container anderswo spezifiziert |
| nym Appraisal | Glosse übergangen, Aussage über Listenstruktur und Kapitel ohne Beleg | Glosse genannt, `listRef` als Pointer auf `#NDNYM` ohne Inhaltsbehauptung |
| testnames offene Frage 1, Appraisal | „country code“ als Deutung, „a file the project maintains“ mehrdeutig | „one-letter value“, „two-letter value“, „a file carried by the release“ |
| 337 Appraisal, offene Frage 4 | „Two comments“ statt vier Transitionsrecords, „participant proposal“ statt Bericht einer Council-Vereinbarung, Rechtebegründung ohne Beleg, Prämisse „records no decision by any body“ | „Several comments“, Bericht von Diskussion, Vereinbarung und Vision, Rechtesatz entfernt, Prämisse mit URN-Vereinbarung und späterer Delegation |
| 2739 Appraisal, offene Frage 4 | Pinned-Commit und Manifest als Quelle des Ergebnisses, Rechtebegründung, Widerspruch zum vollständigen Zitieren, „no comment answers“ | API-Metadaten als Grundlage, Rechte- und Speichersatz entfernt, tentative Antwort des ersten Kommentars |
| 1414 Appraisal, offene Frage 3 | Falsche Zuordnung der Falschschreibung, Manifestsatz, Pinned-Commit, Rechtebegründung, vorausgesetzter Release | `</uri>` in Kommentar 6, API-Metadaten, Frage ohne Präsupposition |
| 1400 Lead, Appraisal | „dated … label“, obwohl das Label kein Datum trägt | Label beobachtet an einem datierten Snapshot |
| 1505 Appraisal | Berichtete Council-Weisung und Deprecation-Notiz unterschlagen, Speichersatz ohne Beleg | Kontext der Kommentare benannt, Speichersatz entfernt |

## Verworfene oder nur teilweise übernommene Urteile

- Versionslabel „TEI P5 4.12.0“ und „pinned release commit“ (ND-Lead, anchor, att.canonical, att.datable, att.fragmentable, att.personal, idno, join, milestone, nym, persname, person): `sources/locks/tei-p5-4.12.0.yaml` bindet `P5_Release_4.12.0` an den Commit. Den v14/v15-Prompts fehlte die dokumentierte Identität. Instrumentbefund, keine Änderung.
- relation ^s5: ^s4 berichtet ausdrücklich den nichtmutuellen Fall. Die Heraushebung des mutuellen Falls leugnet ihn nicht.
- ND Terms *persona* und *relative place name* ohne Core statement: Terms sind direkt an b108 und b65 belegt und verlangen keine Wiederholung.
- NH, fehlende Konformitätsaussagen (b4, b15, b16, b18, b36, b38, b42, b13, Term *partial elements*): Auslassungen ohne unbelegte Behauptung.
- span, Reading 3 und Schematron: Der Lead begrenzt den Umfang, die Grenze ist jetzt als offene Frage sichtbar.
- pb, note, join, person, idno, Auslassung weiterer Mitgliedschaften, Glossen, Datentypen und Inhaltsmodelle aus Core: Auslassungen. Leads und Appraisals mit unzutreffendem Umfang wurden berichtigt.
- att.fragmentable „The specification contains no examples“: am Original wahr und prüfbar, beibehalten.
- join und weitere „The section audit records …“: projektseitiger Verweis in einer Appraisal, keine Quellenbehauptung.
- testnames, faktische Prämissen in offenen Fragen: alle vom Reviewer als zutreffend bestätigt. Offene Fragen dürfen richtige Prämissen tragen.
- 2739 ^s6 nennt eine von drei URLs: Die Aussage leugnet die übrigen nicht. Die Appraisal spricht zutreffend von mehreren verlinkten Dateien.
- 2739, 1414, Schließungsdaten nur in der Appraisal: am API-Record prüfbar, beibehalten und auf die Metadaten gestützt. Der Hinweis „names no pull request“ wurde entfernt, weil `pull_request: null` nur besagt, dass der Record kein Pull Request ist.
- 1505, 337, weitere Kommentare und Revisionen außerhalb der Core statements: begrenzte Zitataufnahme ohne falsche Aussage. Die 1505-Appraisal benennt die ausgelassenen Beschlussberichte jetzt.
- 337 Lead „locked GitHub REST snapshot of 2026-09-06“: `sources/manifests/2026-09-06-entities-run2-citations.yaml` hält `observed_at: '2026-09-06T09:32:48Z'` für die Issue-Seite fest. Das Datum ist wahr, nur dem Kontext fehlt es.
- milestone ^s1, 1505 ^s1, NH ^s20, ND ^s42, 1400 ^s3: Die Urteile beziehen sich auf den Text vor den Root-Korrekturen. Die geltende Fassung ist oben geprüft.

## Meldungen an Root

1. Nachzuziehende Assertions wegen geänderter Statements: `p5-key-serves-cases-where-no-direct-link-is-required`, `p5-persname-is-synonymous-with-name-of-type-person`, `p5-guidelines-use-generic-state-trait-and-event-customized-through-type-for-information-about-a-place`, `structure-p5-note-number-omission-is-conditional`. Erneut zu prüfen: `teic-tei-issue-1414-author-proposes-ref-and-key-on-person-and-place`, `teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical`.
2. E-LADDER durch die Rückstufung: `p5-idno-serves-labels-that-identify-an-object-or-concept-in-a-cataloguing-system-or-a-distributed-system`, `p5-nym-contains-the-definition-of-a-canonical-name-or-name-component`, `p5-persname-contains-a-proper-noun-referring-to-a-person`. Auf `name` gründet keine Assertion.
3. Kontextmetadaten: Die v16-Einträge für 337, 2739 und 1414 nennen im Feld version nur die Reproduktion vom 2026-09-11, nicht das `observed_at` vom 2026-09-06 aus dem Aufnahmemanifest.
4. Zusätzliche Originalstelle: ND b193 (`/div[1]/div[3]/div[6]/p[1]`) mit der Objektdefinition. Sie ist jetzt in der offenen Frage verlinkt und gelangt so ins begrenzte Kontextfenster.
5. Befunde außerhalb des Umfangs, unbearbeitet:
   - `hsa-letter-4493-2026-09-07` und `szd-werke-2026-09-07`: Lizenzangabe der Appraisal ohne gelieferten Beleg.
   - `piez2014range`: Beteiligung am Modell ohne Anker, „publisher permission“ widerspricht „Copyright © 2014 by the author. Used with permission.“
   - `renear-wickett2010documents`: Rahmung als Wiedergabe des Arguments von 2009 verloren, Locator falsch.
   - `tei-sourceforge-fr363`: Zitatdatum 2012-05-15 im Kontext nicht belegt, Mechanismus „by adding <span> to att.pointing“ fehlt, Archiv- und Implementierungsstatus sowie Präsupposition der offenen Frage ohne Beleg, „P5“ nicht im Tickettext.
6. Wiederkehrendes Muster ohne Befund: testnames ^s6, ^s14 und ^s18 enthalten ähnliche „so …“-Deutungen wie ^s4 und haben ihre Paare bestanden. Sie blieben unverändert.

## Ausgeführte Prüfungen

| Prüfung | Ergebnis |
|---|---|
| `git diff --check -- 20_distillates/documents/tei-p5-*.md 20_distillates/publications/teic-tei-issue-*.md` | ohne Befund |
| `review.cut_pairs(root, problems)` | 649 Paare, 0 Probleme |
| `full_review.publication_context` gegen `all-publication-contexts-v16.json` | 63 Issue-Quellenpaare, keine Lücke `quote-not-in-context` oder `no-original-context` |
| `python tools/check_wave1_sources.py --manifest sources/manifests/2026-09-06-entities-run2-citations.yaml --references references/entities-run2.json` | `OK: 58 quotations match 3 local publication sources and distillates.` |
| `python tools/check_wave1_sources.py --manifest sources/manifests/2026-09-07-text-structures-citations.yaml --references references/text-structures-run1.json` | `OK: 5 quotations match 2 local publication sources and distillates.` |
| `tools.full_review.collect` beider Teilrunden, zuletzt nach allen Änderungen | 223 von 223 und 224 von 224 Einheiten beurteilt |
| `python tools/validate.py .` | 3 Fehler, 1 Warnung. Die Fehler sind die drei E-LADDER aus Meldung 2, die Warnung `W-STALE` betrifft Kapitel 08 außerhalb dieses Pakets |

Die Volltestsuite lief nicht, weil kein Code geändert wurde.

## Geänderte Dateien

`20_distillates/documents/` (jeweils `tei-p5-<name>-4.12.0.md`): `guidelines-nd`, `guidelines-nh-non-hierarchical`, `note`, `pb`, `milestone`, `span`, `name`, `att.global.source`, `test-testnames`, `att.canonical`, `att.fragmentable`, `att.personal`, `idno`, `join`, `nym`, `persname`, `person`.

`20_distillates/publications/`: `teic-tei-issue-337.md`, `-1400.md`, `-1414.md`, `-1505.md`, `-2739.md`.

Neu: `workbench/reviews/2026-09-11-v1/source-corrections-2-result.md`.
