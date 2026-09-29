# V1-Arbeitspaket Assertion-Korrekturen: Ergebnis

Stand 2026-09-11. Basis `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0` mit dem uncommitteten Arbeitsstand. Umfang sind die vor diesem Lauf vorhandenen Dateien in `30_assertions/` ohne MOCs, `p6-v1-*`, `practice-v1-*` und `w3c-quote-selection-can-match-multiple-sequences.md`. Destillate, Repräsentationen, Kapitel, Code, Manifeste und Wissensdokumente blieben unverändert. Quelltexte und Reviewerurteile wurden als Daten behandelt.

## Grundlage

- Die Nicht-Pass-Urteile stammen aus `corpus/raw/review-contexts/2026-09-11/v12-latest-findings.json` und wurden am Ende mit `tools.full_review.collect` aus `primary-v12-1` und `primary-v12-2` nachgelesen. Alle 180 Assertion-Einheiten des Umfangs sind beurteilt. 42 Urteile sind nicht bestanden, sie betreffen 39 Assertions.
- Geänderte Core statements wurden als Differenz der Statement-Zeilen gegen `HEAD` ermittelt und mit `source-corrections-result.md` abgeglichen. Sieben Assertions des Umfangs gründen auf geänderten Statements, fünf davon ohne eigenes Nicht-Pass-Urteil.
- Jeder Befund wurde gegen das zitierte Core statement geprüft, in Zweifelsfällen zusätzlich gegen den Originalblock der Repräsentation oder den Publikationskontext.
- Bearbeiter und Reviewer gehören zur Familie Opus. Die Einschränkung gleicher Modellfamilie gilt auch für diese Nacharbeit.

## Status und Buchungen

Alle 41 geänderten Assertions tragen `checked: {}` und `updated: 2026-09-11`. Nicht kontestierte stehen auf `grounded`. Die vier kontestierten Assertions bleiben `contested`, ihre `contested-with`-Einträge und Gegenlinks sind erhalten. Die früheren `machine-review`- und `validation`-Daten wurden entfernt, weil sie den alten Inhalt betrafen. Keine Datei wurde umbenannt und kein Anker entfernt. Drei vorhandene Destillat-Anker wurden ergänzt, die Begründung steht in der Tabelle.

## Änderungen aus Reviewer-Befunden

| Assertion | Eigentlicher Fehler | Beleg | Korrektur | Kapitel |
|---|---|---|---|---|
| `p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur` | Zusatz „on the same element“. Die H1 machte die Klasse zum Urheber statt der Remarks, „English“ fehlte. Support behauptete eine Kapitelaussage zu `ref`. | att.canonical ^s10, Original r7 ohne Elementbedingung | H1 und Statement nach ^s10, Support auf ^s10 begrenzt | 08 [^noprecedence] |
| `p5-guidelines-let-an-encoder-regard-a-city-and-its-predecessor-as-one-place` | Support nannte das Beispiel „one example for a place record“ und behauptete „no criterion for the decision“. Das Original begründet die Identität mit der Überlappung („therefore“). | ND ^s43, Original b144 | Einzigkeit, „record“ und Kriteriumslosigkeit aus Support entfernt | 08 [^entity] |
| `p5-guidelines-state-that-interchange-is-improved-by-tag-uris-in-ref-instead-of-key` | Support verlor die Bedingung der Tag-URIs („preference between the two attributes“) und behauptete eine Position im Kapitel. | ND ^s5 | Verbesserung an Tag-URIs in `ref` gebunden, Position entfernt | keine |
| `p5-guidelines-use-generic-state-trait-and-event-customized-through-type-for-information-about-a-place` | Support behauptete „statement elements introduced for persons“ und „section on places“. | ND ^s49, Original b171 | Support gibt Empfehlung und ergänzende Elemente wieder | 08 [^extension] |
| `p5-idno-supplies-any-form-of-identifier-used-to-identify-some-object-in-a-standardized-way` | Support verschob „in a standardized way“ auf den Identifikator und nannte Beispiele, die ^s1 nicht enthält. | idno ^s1 | „standardized“ der Identifikation zugeordnet, Beispielbezug entfernt | 08 [^idnoread], [^alignment] |
| `p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value` | Support verengte „externally-defined means“ auf „defined outside the document“. | att.canonical ^s2 | Support ohne Bezugsrahmen des Externen | keine |
| `p5-key-remarks-propose-no-particular-syntax-because-its-form-depends-on-project-practice` (contested) | Support behauptete „no deprecation and no move towards a URI syntax“ und begründete damit den Konflikt. | att.canonical ^s4 | Begründungsüberhang entfernt, neutraler Verweis auf die Gegenposition | keine |
| `p5-key-serves-cases-where-no-direct-link-is-required` | Support behauptete eine Arbeitsteilung zwischen `key` und `ref`, ^s4 nennt `ref` nicht. | ND ^s4 | Support auf die zwei Fälle für `key` begrenzt | keine |
| `p5-namesdates-represents-the-referent-and-the-name-independently` | H1 verlor „information about“ und „is understood to refer“. Support verwies auf einen späteren Kapitelabschnitt. | ND ^s2 | H1 nach ^s2, Abschnittsbezug entfernt | keine |
| `p5-core-elements-state-the-kind-of-referent-only-through-type` | H1 machte aus „let an encoder“ eine Eigenschaft der Elemente und verlor „or referred to“. Das Statement nannte das Modul `namesdates`, das ^s1 nicht nennt. | ND ^s1 (Modulname erst in ^s59) | H1 und Statement mit „let an encoder“ und „the module of this chapter“ | 08 [^type] |
| `p5-rs-contains-a-general-purpose-name-or-referring-string` | „core element“, ^s1 trägt keine Modulzugehörigkeit. | rs ^s1 | „core“ entfernt | keine |
| `teic-tei-issue-1414-author-proposes-ref-and-key-on-person-and-place` | Support deutete `ref` und `key` als „identification attributes of the mention“. | 1414 ^s3 | Deutung entfernt, Position und Datum aus der Zitatangabe von ^s3 beibehalten | keine |
| `teic-tei-issue-1414-author-proposes-that-a-record-entry-refer-through-ref-or-key-to-further-information-about-the-same-entity` | Dieselbe Deutung. | 1414 ^s1 | wie oben | keine |
| `teic-tei-issue-1414-commenter-summarizes-idno-as-a-first-child-of-the-record-elements-as-the-short-term-solution` | Support behauptete eine Wende der Diskussion von Attributen zum Kindelement, die erst aus ^s3 und ^s14 zusammen folgt. | 1414 ^s14 | Wende entfernt, Kommentarnummer und Datum aus der Zitatangabe | keine |
| `teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical` | Support behauptete den Bezug auf den `dev`-Branch und XML-Inhalte der Klassenspezifikationen. ^s4 trägt beides nicht. | 2739 ^s4, dazu ^s5 („as can be seen from their spec files“) und ^s6 (URL auf `dev`) aus demselben Kommentar | ^s5 und ^s6 ergänzt, H1 und Statement nennen den Verweis auf die Spec-Datei, XML-Behauptung entfernt | 08 [^2739chain] ist damit über die Assertion gedeckt |
| `teic-tei-issue-337-author-announces-an-interim-guidelines-change-telling-people-to-switch-to-ref` | Support führte eine Kapitelpräferenz als „release fact“ an. | 337 ^s5 | Kapitelbezug entfernt | keine |
| `teic-tei-issue-337-author-reports-a-wish-to-deprecate-key-held-back-by-its-wide-use` (contested) | Support schrieb den Wunsch „the discussion“ zu und behauptete den Release-Zustand von att.canonical. | 337 ^s4 | „a wish the issue author reports“, Release-Behauptung entfernt, neutraler Verweis auf die Gegenposition | keine |
| `teic-tei-issue-337-commenter-excepts-values-that-already-refer-to-an-external-vocabulary` | Support stützte den Bezug der Ausnahme auf „neighbouring statements“. H1 und Statement ließen offen, wovon ausgenommen wird. | 337 ^s20 (vom Quellen-Worker um Format und Ausnahme erweitert), ^s21 | ^s20 ergänzt, Statement nennt die angekündigte Änderung der `key`-Beispiele samt Ausnahme | 08 [^337except] |
| `hsa-dateline-retains-short-year` | Support nannte die Datumszeile „ediert“, ^s1 sagt „im Brieftext“. | HSA ^s1 | „Datumszeile im Brieftext“ | keine |
| `p5-att-canonical-associates-a-name-with-canonical-information-about-its-object` | H1 verlor „provides attributes that can be used to“. Support behauptete „identifying attributes attach to the representation“. | att.canonical ^s1 | Modalität in der H1, Support nach ^s1 | 08 [^canonical] |
| `p5-att-datable-provides-attributes-for-normalization-of-elements-that-contain-dates-times-or-datable-events` | Support behauptete eine Kapitelrolle der Klasse als Quelle der Zeitbegrenzung. | att.datable ^s1 | Kapitelbezug entfernt | keine |
| `p5-att-global-responsibility-indicates-the-agent-responsible-for-something-asserted-by-the-markup` | Support sprach von „the agent the class names“ und schloss auf den gesamten englischen Klassentext. | att.global.responsibility ^s1 | Support auf die Beschreibung begrenzt | keine |
| `p5-att-naming-describes-nymref-through-the-object-named` (contested) | Der Satz „states nothing about whether the canonical form belongs to the name or to the object“ widerspricht ^s3 („canonical form … of the names“). | att.naming ^s3 | Satz entfernt, neutraler Verweis auf die Gegenposition | keine |
| `p5-nested-description-elements-inherit-type-and-responsibility-and-may-date-more-precisely` | Support behauptete „section on places“, die H1 verlor „understood as“. | ND ^s50 | Abschnittsbezug entfernt, „understood as“ in der H1 | keine |
| `p5-place-contains-data-about-a-geographic-location` | Support behauptete „the one reading block of its specification“. | place ^s1 | entfernt | keine |
| `p5-prosopography-records-refer-to-external-authorities-through-idno` | Support grenzte gegen `key` und `ref` ab und sprach von „external authority“, ^s25 spricht von „other resources“. | ND ^s25 | Support nach ^s25, die Einschränkung zur bloßen Nebeneinanderstellung bleibt | keine |
| `p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link` | Das Statement verallgemeinerte die Bedingung des Beispiels `ref="#DPB1"` (^s3 inzwischen korrigiert). Support behauptete, ^s3 sei die einzige verankerbare Evidenz. | ND ^s3 in neuer Fassung | Statement nach ^s3, H1 mit „should be used“, Evidenzbehauptung entfernt | 08 [^inherit] |
| `p5-att-personal-provides-common-attributes-for-elements-forming-part-of-a-name` | Support schloss von der Klassenbeschreibung auf den gesamten englischen Klassentext. | att.personal ^s1 | Schluss entfernt | 08 [^inheritance] (Posit) |
| `p5-guidelines-detach-the-nymref-association-from-the-entity-named` (contested) | Das Statement ersetzte das Beispiel durch „full name form“ und „familiar short form“. Support behauptete „section on nyms“. | ND ^s56, Original b206 | Beispiel im Wortlaut von ^s56, neutraler Verweis auf die Gegenposition | 08 [^nymrefchapter], [^name] |
| `p5-state-describes-a-status-or-quality-attributed-to-a-person-place-or-organization` | Support unterstellte Attribute, mit denen `state` auf sein Subjekt zeigt. | state ^s2, Original r1 | Support nach ^s2 | keine |
| `p5-testnames-change-of-place-is-a-sequence-of-dated-residence-states-without-an-event` | Support behauptete „rather than by attributes on the state element“. | testnames ^s12 | Kontrast entfernt | keine |
| `p5-testnames-name-of-type-person-in-a-note-carries-a-key-and-no-ref` | Support nannte ein „core name element“. | testnames ^s6 | „core“ entfernt | keine |
| `p5-testnames-person-name-form-and-place-carry-three-separate-identifying-values` | Support verortete den Ortsnamen „inside a statement“. | testnames ^s14 | „place name of the birthplace“ | keine |
| `structure-p5-note-responsibility-code-needs-definition` | „English“ fehlte in H1 und Statement, Support war eine Formel. | note ^s5, Original b12 | englisches Beispiel benannt, Support konkret | keine |
| `structure-p5-stand-off-discontinuous-annotation` | „can combine discontinuous text segments in one annotation“ trägt ^s27 nicht. | NH ^s27, Original b43 | Statement nach ^s27 | keine |
| `structure-p5-join-combines-virtual-elements` | Generalisierung über die Bedingung „With scope root“ und über das Beispiel virtueller Sätze. | NH ^s23, join ^s5 | beide Befunde getrennt zugeschrieben, Bedingung erhalten | keine |

## Nachzug geänderter Core statements

| Assertion | Eigentlicher Fehler | Beleg | Korrektur | Kapitel |
|---|---|---|---|---|
| `p5-each-statement-about-a-life-must-be-documentable-and-time-framed` | H1 und Statement verengten den Schluss mit „because“ auf die Quellenabhängigkeit. | ND ^s24 neu, Original b87 („Taking all this into account“) | H1 und Statement nach ^s24 | 02 [^documentablesource], 08 [^documentable], [^extension] |
| `p5-guidelines-distinguish-names-for-places-from-other-data-about-places-as-they-do-for-people` | „may be useful“ war zu „useful for“ geworden, „associated with a particular text or set of texts“ und „any form of“ fehlten. Support behauptete die Position am Abschnittsbeginn. | ND ^s42 neu | H1, Statement und Support nach ^s42 | 08 [^placerecord] |
| `structure-p5-divgen-processing-is-application-defined` | „when … rendered“ und „some information about the kind“ fehlten. | DS ^s39 neu | Statement nach ^s39 | keine |
| `structure-p5-floatingtext-interrupts-resumable-text` | „should be used“ und „interrupts … at any point“ fehlten. | DS ^s30 neu | H1 und Statement nach ^s30 | keine |
| `structure-p5-pb-number-and-sequence` | Sprachgrenze der englischen Remarks, „normally … printed on it“ und die Begründung fehlten. | pb ^s6 neu | H1 und Statement nach ^s6 | keine |

## Instrumentbedingte Fehlalarme

- Dokumentidentität aus dem Destillattitel, die v1.2 nicht lieferte: „Schuchardt-Brief 4493“ in `hsa-origin-and-sent-dates-have-distinct-contexts` und `hsa-dateline-retains-short-year`, „TEIC/TEI“ in `structure-issue1505-recommendation-self-report`, „P5 4.12.0“ in `structure-p5-boundary-range-validation`, das Kapitel in `p5-namesdates-represents-the-referent-and-the-name-independently` und att.canonical in `p5-key-remarks-propose-no-particular-syntax-because-its-form-depends-on-project-practice`. Aus diesem Grund wurde nichts geändert. `hsa-origin-and-sent-dates-have-distinct-contexts`, `structure-issue1505-recommendation-self-report` und `structure-p5-boundary-range-validation` blieben ganz unverändert, die übrigen drei wurden nur wegen der in der Tabelle genannten Fehler bearbeitet.
- Datum, Kommentarnummer und Position in den Issue-Assertions zu 1414, 2739 und 337 stehen in der Zitatangabe des jeweiligen Core statements und bleiben erhalten. `review._source_pairs` übergibt als Claim nur die Aufzählungszeile, und `full_review.ground_identity` baut den Assertion-Beleg aus diesem Claim. Auch v1.4 zeigt die Zitatzeile daher nicht, und die Blindprüfung wird diese Angaben ohne Instrumentergänzung erneut beanstanden.
- Für `teic-tei-issue-337-author-reports-a-wish-to-deprecate-key-held-back-by-its-wide-use` meinte der Reviewer, die Quelle schreibe den Wunsch dem Issue-Autor zu. Das gilt nur für ^s4. Das Original spricht von „Council's vision“. Die Korrektur folgt ^s4 ohne eigene Zuschreibung.

## Offene Punkte

1. Destillate außerhalb dieses Pakets:
   - 337 ^s4 und ^s5 verlieren die Zuschreibung an den Council („Per discussion at TEI Council meeting in Paris“, „Council's vision“, „we will modify“).
   - ND ^s43 verliert „therefore“ und damit die Überlappung als Grund für die Identität von Lyon und Lugdunum.
   - NH ^s27 verdichtet b43 und verliert „mentioned in the literature“ sowie „combined in a single annotation“. Nach einer Erweiterung könnte die Stand-off-Assertion diesen Inhalt wieder tragen.
   - att.global.responsibility ^s1 zitiert die Klassenbeschreibung ohne „and the degree of certainty associated with it“ und kennzeichnet die Auslassung nicht.
   - 337 ^s21 wiederholt seit der Erweiterung von ^s20 dessen Ausnahme.
2. Bestandene Assertions mit demselben Support-Muster blieben unverändert. Positionsangaben oder Abwesenheitsschlüsse über den ganzen Klassentext stehen in `p5-guidelines-distinguish-resolving-a-name-from-treating-it-as-an-object`, `p5-guidelines-group-information-about-a-person-as-distinct-from-references-to-a-person-within-person`, `p5-guidelines-separate-the-entity-record-from-references-to-the-entity`, `p5-rolename-excludes-the-role-a-person-has-in-a-context` und `p5-source-specifies-the-source-from-which-some-aspect-of-an-element-is-drawn`. 18 `structure-*`-Assertions tragen weiterhin die Formel „The assertion retains its stated source and scope“, die ein Reviewer als unzutreffende Selbstauskunft beanstandet hat. Ob dies als systematischer Befund eine Vollprüfung des Aussagentyps auslöst, entscheidet der Integrator.
3. Kapitel 08 wird parallel bearbeitet (`W-STALE`). Beim Abschluss dieses Pakets wichen noch folgende Stellen von den korrigierten Assertions ab:
   - [^type] „as marking“ ohne „let an encoder“
   - [^placerecord] „as a structured record of data about any place“
   - [^idnoread] und [^alignment] „standardized identifier of some object“
   - [^entity] und der Absatz davor „without a stated criterion“, was b144 widerspricht
   - [^337except] ohne die Änderung, von der ausgenommen wird
   - [^extension] „the place section prescribes“ und „require“
   Kapitel 02 [^documentablesource] sowie 08 [^documentable], [^inherit], [^nymrefchapter] und [^noprecedence] sind gegen die neuen Statements gegenzulesen.
4. `python tools/inventory.py . --write` steht aus. Geänderte H1 und neue Anker betreffen die MOCs Abstract Model, Elements and Classes, Metadata and Entities und Text and Document Structures sowie die Glossareinträge entity-identification, entity-record, mention-of-an-entity, name-as-an-object, responsibility-for-a-statement und statement-about-an-entity.
5. Alle 41 geänderten Assertions brauchen neue Paare und Blindurteile.

## Ausgeführte Prüfungen

| Prüfung | Ergebnis |
|---|---|
| `git diff --check` für die 41 geänderten Assertions | ohne Befund |
| `review.cut_pairs(root, problems)` | 649 Paare, 0 Probleme |
| `python tools/validate.py .` | 42 Fehler, 1 Warnung, kein Befund an einer Datei dieses Pakets |
| `full_review.collect` für `primary-v12-1` und `primary-v12-2`, nur lesend | 180 von 180 Assertion-Einheiten des Umfangs beurteilt |

Tests wurden nicht ausgeführt, weil kein Code geändert wurde.

### Integrationsfehler außerhalb dieses Pakets

- 28 × `E-LADDER` an unveränderten `validated`-Assertions über inzwischen `grounded` gesetzten Destillaten, Behandlung durch Root.
- 14 × `E-GENERATED` in acht MOCs und sechs Glossareinträgen, siehe offener Punkt 4.
- 1 × `W-STALE` für `40_output/08-metadata-and-entities`.

## Geänderte Dateien

Die 41 in den beiden Tabellen genannten Dateien unter `30_assertions/` und neu dieser Bericht.
