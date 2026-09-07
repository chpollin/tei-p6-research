---
title: Identity and Evidence
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: de
created: "2026-09-07"
updated: "2026-09-07"
related: [text-model, model-design, model-examples, experiments, schema, verification, state]
---

# Identität und Quellenbezug

Dieses Dokument beantwortet die delegierten Fragen nach der Zusammengehörigkeit
von Fassungen und der Nachprüfbarkeit modellierter Aussagen. Es definiert das
experimentelle Profil `identity-evidence-0.1` auf dem Entitätenmodell 0.2.
Die Entscheidungen sind Projektvorschläge. Der Nutzer hat ihre Ausarbeitung
delegiert; eine fachliche Nutzerabnahme oder menschliche Verifikation folgt
daraus nicht. Die Ausführung und ihre Grenzen stehen in [[knowledge/experiments]].

Die folgenden Identitätskriterien gelten für die beschriebenen Editions- und
Katalogfälle. Die allgemeine, auch auf Sprachkorpora anwendbare Modellierung
von Textidentität und kontextgebundenen Referenten steht in
[[knowledge/model-design]]. Deren vorgeschlagene Erweiterungen verändern den
hier ausgeführten Profilvertrag nicht. Das Profil legt insbesondere keine
allgemeine Semantik für Erzählwelten oder Existenzzuschreibungen fest.

## Entscheidung über Zusammengehörigkeit

Identitätsfragen erhalten einen ausdrücklich benannten Gegenstand. Eine
Katalogbeschreibung, das beschriebene materielle Objekt, eine editorisch
konstituierte Texteinheit und ein Werk können miteinander verbunden sein und
behalten jeweils ihre eigene Identität. Das bisherige `Text` bezeichnet die
editorische Gruppierung von Versionen. Es erhält keine automatische Bedeutung
als Werk, Manuskript oder historischer Kommunikationsakt.

| Fall | Arbeitsentscheidung | Begründung und Grenze |
|---|---|---|
| Zwei Katalogeinträge verweisen auf dasselbe Werk | Getrennte Einträge und materielle Objekte erhalten; die Werkzuordnung als Quellenbericht ausdrücken. | Ein gemeinsamer Werkverweis allein begründet weder gleiche Zeichenfolgen noch ein Fassungsverhältnis. |
| Eine Transkription wird nach Korrektur eines Lesefehlers ersetzt | Neue Zeichenfolgenversion unter derselben editorischen Texteinheit; dieselbe Transkriptionsaufgabe und derselbe Textzeuge müssen begründet sein. | Frühere Lesung, Änderungsgrund und Bezugsobjekt bleiben erhalten. Bloße Gleichheit eines Dateinamens genügt nicht. |
| Diplomatische und normalisierte Wiedergabe eines Textzeugen | Bei gleicher gewählter Texteinheit in einer editorischen Gruppierung zulassen; die Wiedergabepolitik ausdrücklich dokumentieren. | Unterschiedliche Wortlaute entstehen durch unterschiedliche Regeln. Referenzauflösung und Angemessenheit einer übertragenen Annotation bleiben separat zu prüfen. |
| Entwurf und ausgefertigter Brief | Getrennte Dokumente; eine begründete Entwurfs- oder Fassungsrelation dokumentieren. | Eine gemeinsame editorische Gruppe ist unter einem angegebenen Forschungszweck möglich. Das Modell darf sie nicht allein aus Absender, Empfänger oder Datum erzeugen. |
| Zwei Zeugnisse überliefern dieselben Zeichen | Getrennte Zeugnisse und Versions-IDs zulassen. | Zeichenvergleich kann Gleichheit des Inhalts feststellen; die Überlieferungsidentität braucht andere Belege. |
| Haupttext und angefügter Nachtrag | Die gewählte editorische Texteinheit und Lesereihenfolge benennen; eine Quelle kann mehrere Projektionen tragen. | Die bloße Position im XML entscheidet keine historische Zugehörigkeit. |

Das operative Kriterium für eine positive Kontinuitätsaussage lautet, dass
ein verantwortlicher Bearbeiter die Versionen als Wiedergaben derselben
editorisch bestimmten Texteinheit unter einem benannten Zweck behandelt.
Der Datensatz hält den Grund fest. Eine erfolgreiche Gruppierung beweist
keine allgemeingültige Textontologie. Abwesenheit einer Gruppierung bleibt
ohne negative Identitätsaussage. Die synthetischen Transkriptionsfälle prüfen
diese Entscheidung unabhängig von den historischen Katalogeinträgen.

Die beiden realen Katalogeinträge sind über die Quellenkette erschlossen,
siehe [[30_assertions/szd-records-share-work-reference]] und
[[30_assertions/szd-records-have-distinct-shelfmarks]]. Ihre Textanfänge und
Beschreibungen begründen eine Untersuchungsfrage nach ihrem Zusammenhang.
Ein konkretes Fassungsverhältnis wird hier nicht behauptet.

## Entscheidung über nachprüfbare Aussagen

Jeder im Profil übernommene Quellenbericht trägt eine eigene Aussage-ID,
den betrachteten Gegenstand und seine Verantwortung für die Übernahme.
Mindestens eine exakte Belegstelle verbindet ihn mit einem festgelegten
Quellensnapshot. Die Belegstelle enthält den überlieferten Wortlaut.
Die Herkunft des Snapshots, seine Prüfsumme und der genaue Ausschnitt sind
ohne Netzwerkzugriff nachprüfbar.

Eine Unsicherheitsmarkierung der Quelle bleibt als eigener ausgewählter
Wortlaut erhalten. Das Fragezeichen einer Handschriftenbeschreibung führt
zu keiner automatischen Einstufung als `low`, `medium` oder `high`.
Eine eigene Bewertung wird als zusätzliche Annotation mit eigenem Agenten,
Begründung und gegebenenfalls eigener `certainty` angefügt. Der Quellenbericht
behält seine ursprüngliche Form. Diese Lösung verwendet die vorhandene
Adressierbarkeit von Aussagen durch Beziehungen.

Die Identität eines Importprozesses bezeichnet die Verantwortung für die
Übernahme. Sie authentifiziert keinen historischen Katalogisierer und keinen
Urheber einer Zuschreibung. Die Quelle kann allgemeine Projektverantwortliche
nennen, ohne einen einzelnen Befund einer Person zuzuschreiben. Die derzeit
betrachtete Handschriftenangabe lässt diese Einzelverantwortung offen.

Für die Handschriftenfrage stehen die getrennten Quellenbefunde in
[[30_assertions/szd-hand-attribution-retains-question-mark]] und
[[30_assertions/szd-contributor-and-hand-description-are-distinct]]. Die
Auszeichnung einer Mitwirkung und die unsichere Beschreibung einer Hand
werden als getrennte Angaben erhalten. Daraus wird kein Widerspruch und keine
Auflösung der Unsicherheit abgeleitet.

### Ausgefüllter Prüfdatensatz

| Feld | Anwendung auf den ausgewählten Katalogeintrag |
|---|---|
| Aussage-ID | `szd-hand` im experimentellen Dossier. |
| Gegenstand | Die im Eintrag zu `SZ-AAP/W2.1` beschriebene Hand. Eine konkrete Blattregion ist damit nicht identifiziert. |
| Übernommener Inhalt | Die Beschreibung enthält „Lotte Zweig (?)“. |
| Beleg | `SZDMSK.3`, vollständiges `handDesc` innerhalb des eingefrorenen Eintragsausschnitts. |
| Qualifikation | Der ausgewählte Wortlaut `(?)` bleibt mit seiner Position innerhalb des Belegs erhalten. |
| Belegart | Bericht über einen Katalogeintrag. Im Versuch wurde kein Handschriftenvergleich vorgenommen. |
| Begründung der Übernahme | Die Kopie bewahrt den Wortlaut und dessen Auszeichnungskontext; die ursprüngliche Begründung der Handzuschreibung steht in diesem Ausschnitt nicht. |
| Verantwortung | Der Importagent verantwortet die Übernahme. Die individuelle Urheberschaft dieser Katalogzuschreibung bleibt unbekannt. |
| Eigene Bewertung | Im realen Dossier ist keine eigene Handschriftenbewertung hinterlegt. Eine zusätzliche Bewertung erhält einen eigenen Agenten und eine Begründung. |
| Revisionsregel | Frühere Aussage und Beleg bleiben erhalten; eine Neubewertung wird ergänzt. |

Die damit beantwortete Nutzerfrage lautet, welche Angaben eine fachliche
Prüfung ermöglichen. Für eine übernommene Aussage sind Gegenstand,
Quellenfassung, genaue Belegstelle, Wortlaut und Übernahmeverantwortung
erforderlich. Hinzu kommen vorhandene Qualifikationen und die transparente
Angabe, was bisher geprüft wurde. Eine eigene weitergehende Interpretation
benötigt eine eigene Begründung. Fehlt der historische Nachweis, ist gerade
diese Lücke Teil des prüfbaren Ergebnisses.

## Datierung und Handlung

Datumswortlaut, normalisierte editorische Datierung, behauptetes
Entstehungsdatum und Datum einer Korrespondenzhandlung bleiben verschiedene
Aussagegegenstände. Zusätzlich datiert `created` die Anlage unseres
Aussagedatensatzes. Das Feld `valid` bezeichnet im Kernmodell die Gültigkeit
eines behaupteten Zustands; es ersetzt kein historisches Ereignisdatum.

Im Briefbeispiel sind die Datumszeile und die beiden Metadatenkontexte
separat belegt, siehe [[30_assertions/hsa-dateline-retains-short-year]] und
[[30_assertions/hsa-origin-and-sent-dates-have-distinct-contexts]]. Das Profil
berichtet, was in den jeweiligen Feldern steht. Es leitet aus der Datumszeile
weder selbständig das Jahrhundert noch einen tatsächlich erfolgten Versand
ab. Die Jahrhundertauflösung wird zunächst als Angabe der Edition übernommen.
Ein Poststempel oder eine unabhängige Versandquelle könnte eine zusätzliche
Aussage begründen; ein solcher Beleg gehört nicht zur untersuchten Auswahl.

## Ausführbarer Profilvertrag

Ein Dossier ist ein Versuchsartefakt mit `profile`, `package` und `sources`.
`package` bleibt eine gültige Instanz von Entitätenmodell 0.2. Der zusätzliche
Herkunftsteil ist ein Adapter für die festgelegten XML-Ausschnitte. Er begründet
keine neue Evidenzebene und darf nicht in `grounding` erscheinen.

Jeder Herkunftseintrag verbindet eine vorhandene Version mit `snapshot`,
`uri`, `sha256`, `start_byte`, `end_byte` und `xpath`. Der Hash bezeichnet die
vollständige empfangene XML-Antwort. Die beiden Bytepositionen grenzen einen
exakten UTF-8-Ausschnitt ab, dessen Inhalt der referenzierten Version entspricht.
Der XPath ist eine Navigationsangabe; die Bytepositionen und der Hash tragen
den Identitätscheck. Die Quelle ist eine eigene Zeichenfolge des Quelldokuments.
Sie wird dadurch zu keiner Transkription des beschriebenen Manuskripts.

Alle im Dossier verwendeten Versionen benötigen einen Herkunftseintrag.
Die festgelegten Originalbytes werden dem Validator ausdrücklich übergeben.
Fehlende Quellen, falsche Hashes, geänderte Ausschnitte oder doppelte
Herkunftseinträge sind Fehler. Das Experiment rekonstruiert die Originalbytes
aus den unveränderlichen Repräsentationen; ignorierte Dateien sind dafür
nicht erforderlich.

| Bestehender Modellbaustein | Profilbedeutung |
|---|---|
| Entität `object` | Das im ausgewählten Katalogeintrag beschriebene materielle Objekt. |
| Entität `other` | Die lokale, im Katalog angegebene Werkidentität. Eine externe Auflösung wird nicht behauptet. |
| Aussage mit reserviertem Profilkonzept | Bericht über eine Werkzuordnung, Handschriftenangabe, Mitwirkung oder ein Datumsfeld der Quelle. |
| Annotation `ie-source-passage` | Exakter Ausschnitt aus einer Quellenversion; der Body entspricht dem ausgewählten Wortlaut. |
| Annotation `ie-source-qualification` | Exakte Qualifikation aus derselben Quellenversion wie mindestens ein zugehöriger Beleg. |
| Annotation `ie-assessment` | Eigene Bewertung einer Aussage mit begründendem Body und eigenem Agenten. |
| Beziehung `ie-supported-by` | Verbindet einen Quellenbericht mit seiner Belegannotation. Der Agent entspricht dem des Quellenberichts. |
| Beziehung `ie-qualified-by` | Verbindet einen Quellenbericht mit einer überlieferten Qualifikation. Der Agent entspricht dem des Quellenberichts. |
| Beziehung `ie-assesses` | Verbindet eine Bewertungsannotation mit einer Aussage. Der Agent entspricht dem der Bewertung. |

Die reservierten Konzepte müssen ihren genauen Definitionen in
`tools/models/identity_evidence.py` entsprechen. Jeder Quellenbericht hat
mindestens einen Beleg und keine eigene `certainty`; eine eigene Bewertung
gehört in die separate Bewertungsannotation. Jeder Quellenbeleg und jede
Qualifikation muss auf genau einen nichtleeren zusammenhängenden Ausschnitt
auflösen. Alle ursprünglichen Zeichen bleiben erhalten. Eine Qualifikation
muss innerhalb eines Belegs desselben Quellenberichts liegen. Das prüft ihre
Position, ohne die Bedeutung des Fragezeichens zu automatisieren.

`validate_profile(dossier, snapshots)` prüft die Kernmodellregeln und die
beschriebenen Herkunfts- und Belegbedingungen. `inspect_claim` liefert den
Quellenbericht, seine Verantwortung, aufgelöste Belegstellen, Qualifikationen
und separate Bewertungen. `check_profile_revision` verlangt zusätzlich zur
Revisionsprüfung des Entitätenmodells die unveränderte Erhaltung älterer
Herkunftseinträge. Vorhandene Entitäts-IDs und ihre konstitutive `kind` bleiben
ebenfalls erhalten, damit unveränderte Aussagen nicht nachträglich einen
anderen Gegenstandstyp adressieren. Die Operationen verändern ihre Eingaben nicht.

Der Revisionsschutz erfasst die Selektionen und ihre Referenzauflösung bisher
nicht. Ein unveränderter Belegbody kann bei identischem Wortlaut durch eine
geänderte Selektion auf einen anderen Katalogeintrag zeigen. Der vollständige
Erhalt einer Beleggeschichte ist damit offen. Ebenso filtert `inspect_claim`
seine Belege und Bewertungen nicht automatisch nach Supersession oder
Withdrawal. Diese Grenzen sind in der
[Modell-Proposal](../40_output/02-abstract-model.md#10-revision-and-historical-integrity)
von den tatsächlich geprüften Record-Garantien getrennt.

Eine erfolgreiche Prüfung stellt keine semantische Unterstützung durch den
Beleg fest. Ein exaktes Zitat kann eine unzutreffende Behauptung begleiten.
Ein Gegenfall hält diese Grenze ausdrücklich fest. Ein zweiter Gegenfall
zeigt, dass eine räumlich passende Qualifikation keine automatische
Gewissheitsstufe erhält. Die gespeicherten Prüfberichte tragen keine
menschlichen Forschungsstatuswerte.

## Modellumfang und offene Prüfung

Das Profil ergänzt ausführbare Regeln und eine Belegansicht. Die allgemeinen
JSON-, XML- und YAML-Bindings des Kernmodells sowie der RDF-Export definieren
keinen Austausch des zusätzlichen Herkunftsteils. Dessen Verlust wäre beim
alleinigen Export von `package` offenzulegen. Das Profil beansprucht keinen
eigenen RDF-Roundtrip und keine vollständige P5-Abbildung.

Eine allgemeine Werkontologie, negative Identitätsbehauptungen,
Bildregionen, Unsicherheitslogik, historische Versandnachweise und eine
vollständige Konversion beider Editionen bleiben offen. Für die delegierten
Fragen gelten die oben formulierten Arbeitsentscheidungen. Ihre Prüfung an
weiteren Quellen und durch Editionsfachleute kann eine Revision begründen.
