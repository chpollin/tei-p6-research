---
title: HSA-Fallprofil
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
related: [model-design, model-examples, ontology, text-model-bindings, experiments, testing, architecture, state]
---

# HSA-Fallprofil

Dieser Vertrag definiert die ausführbare Modellierung des aufgenommenen
HSA-Briefs 4493. Er legt fest, welche Quellenangaben als Aussagen übernommen
werden, welche Zuordnungen der Importer selbst konstruiert und was lediglich
erhalten bleibt. Der [Fallvergleich](../experiments/hsa_letter_4493/README.md)
erläutert die editorischen Entscheidungen am Brief.

## Geltungsbereich und Zuständigkeit

| Artefakt | Bedeutung |
|---|---|
| [[knowledge/text-model]] und [[knowledge/text-model-bindings]] | Bestehende ausführbare Modelle 0.1 und 0.2 mit ihren eigenen Datenverträgen. |
| [[knowledge/model-design]] | Weiterführender begrifflicher Entwurf. |
| [[knowledge/model-examples]] | Sechs illustrative Fälle mit einem eigenen XML-/JSON-/RDF-Umschlag. |
| [[knowledge/ontology]] und `ontology/core.ttl` | Definition dokumentarischer Klassen und Eigenschaften. Die Ontologiesyntax ist von der Instanzsyntax zu unterscheiden. |
| Dieses Dokument | HSA-Modellprofil 1, seine Quellenzuordnungen und seine Bindings 1 und 2. |
| `tools/hsa_case/` | Ausführbare Umsetzung des Vertrags mit getrennten Quell-, Mapping-, Binding- und Prüfoperationen. |
| `workbench/reviews/2026-09-07-hsa-case/brief.md` | Unveränderlicher damaliger Arbeitsauftrag. Spätere Profiländerungen stehen hier und im Journal. |

Das Profil ist ein unabhängiger Entwurf außerhalb der Grounding-Kette.
Es führt keine Modellversion 0.3 und keine offizielle TEI-P6-Syntax ein.
Externe Ontologien werden weder importiert noch durch Äquivalenzaxiome
angebunden.

Die einzige zulässige Quelle ist der bereits aufgenommene Snapshot mit SHA-256
`f37ff85df57405753aa0b6d1db63f3a24fcbd33ab1ef7fb54b68844e556e2438`.
Seine Herkunft, Lizenz CC BY-NC 4.0 und Attribution bleiben im Paket
explizit. Ein anderer Brief erfordert ein eigenes Mapping. Die Wiedergabe
von Quellenangaben begründet keine unabhängige historische Bestätigung.

## Semantische Zuordnungen

Jede Proposition besitzt genau einen Gegenstand, ein definiertes Prädikat,
einen Kontext und entweder eine Objektreferenz oder ein typisiertes Literal.
Ihr Claim benennt dieselbe Proposition, den Importer als verantwortlichen
Agenten, seine Haltung und den Lebenszyklus `active`.

| Quellenfeld oder Konstruktion | Modellierung und begrenzte Bedeutung |
|---|---|
| Abgrenzung des Briefcontainers | Repräsentation gehört zum beschriebenen Text; Text ist Inhalt des Briefdokuments. Eigene Konstruktionen mit `assert` und `context-construction`. |
| `msDesc` | Das Briefdokument wird auf einen getrennten materiellen Träger bezogen. Eigene begründete Konstruktion. |
| `titleStmt/author/persName` | Berichtete Autorschaft des Briefdokuments. |
| `msDesc/history/origin` | Herkunftskontext des Trägers mit eigener Datums- und Ortsaussage. |
| `correspAction[@type='sent']` | Versandkontext des Briefdokuments mit Absender, Datum und Ort. |
| `correspAction[@type='received']/persName` | Berichtete Empfängerrolle im Korrespondenzkontext. Fehlende Empfangszeit und fehlender Empfangsort werden nicht ergänzt. |
| `material`, `repository`, Signaturfeld | Exakte Zeichenketten zum Träger, einschließlich des Werts `Unbekannt`. |
| `origDate/@when`, Versand-`date/@when` | Jeweils `xsd:date`, mit unterschiedlichen Ereignisgegenständen und Belegpfaden. |
| `publicationStmt/date/@when` | `xsd:gYear` der XML-Publikation. Die bibliografische Jahreszahl 2016 bleibt davon getrennt. |
| Dateline, PID, `div/@xml:id`, `geo` | Unveränderte Zeichenketten in ihren jeweiligen Kontexten. |
| Namen im Header | Exakte Namensform und berichtete Verwendung für einen ReferentRecord. Vorhandene `ref`- und `corresp`-Werte werden als `xsd:anyURI` berichtet. |
| Vier `persName`-Vorkommen im Brief und in Note 8 | Eigene MentionRecords mit exakten Bereichen und Namensformen; die kodierte Zuordnung wird als Proposition mit `report` dokumentiert. |
| Elf editorische Notes | Eigene Repräsentationen und Annotationen mit leeren Bereichen am Einfügepunkt im Brief. Ein umfassender fachlicher Zielbereich wird dadurch nicht behauptet. |

Die drei Konstruktionsclaims heißen `representation-assignment`,
`text-document` und `document-carrier`. Alle übrigen Claims sind
Quellenberichte. Eine Belegstelle verbindet den Quellenhash mit einem
absoluten, indizierten TEI-XPath und gegebenenfalls einem Attribut.
Claim und Proposition müssen auf die für ihr Mapping festgelegte Stelle
verweisen. Ein gleichlautendes Datum aus einem anderen Kontext genügt nicht.

Die vollständigen ausführbaren Zuordnungen stehen als `ClaimSpec)-Einträge
in `source_claims()` in `tools/hsa_case/mapping.py`. Der Validator liest
diese Zuordnungen, ohne den Graphgenerator aufzurufen. Er vergleicht auch
Prädikatsinterpretation und Begründung. Eigenständige Gegenproben prüfen
Vertauschungen von Personen, Datumsarten, Belegpfaden und Haltungen.
Eine gemeinsam falsche Modellentscheidung in Vertrag und Umsetzung erfordert
weiterhin fachliche Prüfung.

## Record-Anforderungen

Jeder Record besitzt genau eine explizite dokumentarische Klasse und genau
einen verantwortlichen Importer. Das Paket führt alle Records seines
Teilgraphen als Mitglieder. Referenzen im semantischen Teil müssen lokal
aufgelöst sein. Eigenschaften außerhalb des Fallprofils werden zurückgewiesen.

| Record-Klasse | Zusätzliche Anforderungen |
|---|---|
| TextRecord | Explizites Identitätskriterium. |
| ReferentRecord | Definierter lokaler ConceptRecord als revidierbare Typerwartung; Konstruktionstext zur Zuordnung. |
| RepresentationRecord | Exakter Unicode-Inhalt; Brief und Notes besitzen außerdem Projektionsregel und Quellenbezug. |
| TextRangeSelectionRecord | Repräsentation, Anfang, Ende und exaktes Zitat. Koordinaten sind nichtnegative Ganzzahlen. |
| NameFormRecord | Exakte Form und ihre Quellenstelle. |
| MentionRecord | Bereich, Namensform, Identifikationsclaim und Quellenstelle. |
| PropositionRecord | Genau ein Subjekt, Prädikat, Kontext und Objekt; der Objekttyp entspricht dem jeweiligen Mapping. |
| ClaimRecord | Aussageinhalt, Agent, Haltung und Lebenszyklus; Quelle oder ausdrücklich festgelegte Konstruktion. |
| PredicateRecord | Definition und getrennte Interpretation der Subjekt- und Objektreferenz. |
| ContextRecord und ConceptRecord | Benannter Geltungsbereich beziehungsweise definierter Begriff. |
| StructuralNodeRecord | Erhaltenes XML-Element mit Namen, Attributen, Text, Tail, Elternbezug und Position im Elternknoten. |

Das Profil verlangt Einzelwerte außer bei Paketmitgliedschaften. XML-Datentypen
werden erhalten und geprüft; ein Datum als `xsd:string` erfüllt keine
Datumsanforderung. OWL-`domain`- und `range`-Axiome allein ersetzen diese
Eingabeprüfungen nicht. Der Validator verwendet deklarierte Klassen und deren
lokale Oberklassen zur Prüfung von Referenztypen und erzeugt keine inferierten
Tripel.

## Projektion und Erhaltung

Die Projektion verwendet die von ElementTree gelieferten XML-Zeichendaten in
Dokumentreihenfolge. `note`-Unterbäume erhalten eigene Repräsentationen;
deren nachfolgender Text, der XML-Tail, bleibt im Brief. `pb` und `lb`
fügen keine Zeichen ein. Bereiche zählen Unicode-Codepoints ab null mit
exklusivem Ende. Leere Bereiche markieren Einfügepunkte.

Die erzeugten Dateien sind in zwei Komponenten gegliedert.

| Komponente | Inhalt und Zusage |
|---|---|
| `p6.json`, `p6.xml`, `p6.ttl` | Derselbe semantische Teilgraph mit vollständigem Brieftext, Notes, Claims, Namensformen, Bereichen und Quellenlokatoren. |
| `preservation.json`, `preservation.xml`, `preservation.ttl` | Ergänzender Teilgraph mit eingebettetem Quellen-XML, allen erhaltenen XML-Knoten des Bodys, deren Bereichen und den wörtlichen Werten der Quellenlokatoren. |
| `p5.xml` | Unveränderte ursprüngliche Dateibytes einschließlich vollständigem Header und Verarbeitungsanweisungen. |

Die Mengenvereinigung von semantischem Teil und Erhaltungsteil ergibt exakt
den früheren vollständigen Fallgraphen. Gemeinsame Subjekte wiederholen ihre
Typdeklaration, damit beide Bindings jeden Record typisieren können.
Der Erhaltungsteil benötigt für seine Referenzen den semantischen Teil.
Er beansprucht keine eigenständige Paketkonformität.

Der semantische Teil lässt sich mit dem festen P5-Snapshot unmittelbar prüfen.
Seine Quellenlokatoren behalten XPath und Quellenbezug; wörtliche
`sourceValue`-Kopien sind nur im Erhaltungsteil nötig. Ihre Auslagerung
entfernt keine Quellenadresse. Die komplette Graphprüfung verlangt beide
Komponenten. Nur die ursprünglichen Dateibytes begründen Byteerhaltung;
aus erhaltenen XML-Elementen folgt keine vollständige semantische
Rückkonvertierung.

## Binding 2 und Kompatibilität

Das Modellprofil bleibt
`https://example.org/tei-p6-research/profile/hsa-4493/1`.
Das aktuelle Binding heißt
`https://example.org/tei-p6-research/binding/hsa-4493/2`.
Die Präfixe sind fester Bestandteil dieses Bindings.

| Präfix | Expansion |
|---|---|
| `case:` | `https://example.org/tei-p6-research/case/hsa-4493/` |
| `p6:` | `https://example.org/tei-p6-research/ontology/` |
| `v:` | `https://example.org/tei-p6-research/case-vocabulary/hsa-4493/` |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` |
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |

JSON verwendet genau `profile`, `package`, `binding`, `component`
und `records` als Umschlagfelder. XML verwendet einen `case)-Wurzelknoten
im Binding-Namespace mit `profile`, `package` und `component`.
`component` ist `semantic`, `preservation` oder `complete`.
Diese Umschlagangabe beschreibt den Lieferumfang; sie erzeugt kein zusätzliches
RDF-Tripel. Volle IRIs sind ebenfalls zulässig. Kurzformen in XML-Attributwerten
werden nach dieser Tabelle expandiert; sie sind keine XML-Elementpräfixe.

Ein JSON-Record hat genau `id`, `type` und `properties`. Die Werte
jeder Eigenschaft bilden ein nichtleeres Array aus Referenzen mit genau
`ref` oder Literalen mit `value` und genau einem der Felder
`datatype` und `lang`. Literale bleiben Zeichenketten; Zahlen werden
nicht still konvertiert. XML bildet diese Werte durch `record`,
`property`, `ref` und `literal` ab. Literale verlangen
`xml:space="preserve"`; ihr Inhalt enthält keine Unterelemente.

Unbekannte Felder, doppelte Schlüssel, doppelte Record-IDs und doppelte
Eigenschaftswerte sind Fehler. Ebenso werden unbekannte XML-Kinder,
zusätzliche Attribute, Text außerhalb von Literalen und mehrdeutige Werte
zurückgewiesen. Sprachmarkierte Literale sind im Binding darstellbar; der
feste HSA-Fall verwendet seine ausdrücklich typisierten Quellenwerte.
Die Binding-Prüfung und die fachliche Fallprüfung sind getrennte Operationen.

Der Leser unterstützt weiterhin den vollständigen Umschlag des Bindings 1,
der volle IRIs und keinen Komponentenbezeichner enthält. Der Generator kann
mit `json_data(graph, binding=1)` und anschließend `xml_data(data)`
auch diese Schreibweise erzeugen. Die standardmäßig erzeugten `p6.*`-Dateien
enthalten seit Binding 2 den semantischen Teil. Verbraucher, die bislang die
vollständige Quellstruktur dort gelesen haben, müssen den Erhaltungsteil
hinzunehmen. Diese explizite Umstellung ist keine P5-Rückwärtskompatibilität.

## Dasselbe Aussagefragment in drei Syntaxen

Die folgenden Fragmente wählen dieselben vier Tripel aus dem Datumsrecord.
Sie sind Ausschnitte für den Syntaxvergleich. Die vollständigen Records
ergänzen Quellenlokator, Label und Verantwortung.

```json
{
  "id": "case:proposition-sending-date",
  "type": "p6:PropositionRecord",
  "properties": {
    "p6:propositionSubject": [{"ref": "case:event-sending"}],
    "p6:propositionPredicate": [{"ref": "case:predicate-date"}],
    "p6:propositionObjectLiteral": [{"value": "1878-04-17", "datatype": "xsd:date"}]
  }
}
```

```xml
<record xmlns="https://example.org/tei-p6-research/binding/hsa-4493/2"
        id="case:proposition-sending-date" type="p6:PropositionRecord">
  <property iri="p6:propositionSubject"><ref iri="case:event-sending"/></property>
  <property iri="p6:propositionPredicate"><ref iri="case:predicate-date"/></property>
  <property iri="p6:propositionObjectLiteral"><literal datatype="xsd:date" xml:space="preserve">1878-04-17</literal></property>
</record>
```

```turtle
@prefix case: <https://example.org/tei-p6-research/case/hsa-4493/> .
@prefix p6: <https://example.org/tei-p6-research/ontology/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
case:proposition-sending-date a p6:PropositionRecord ;
    p6:propositionSubject case:event-sending ;
    p6:propositionPredicate case:predicate-date ;
    p6:propositionObjectLiteral "1878-04-17"^^xsd:date .
```

## Prüfen und weiterarbeiten

`tools/build_hsa_case.py` orchestriert Lesen, Mapping, Prüfung,
Komponentenbildung und Dateierzeugung. `--check` vergleicht alle
erzeugten Dateien, ohne sie zu verändern. Änderungen erfolgen an Vertrag
und zuständiger Implementierung; die Austauschdateien werden neu erzeugt.
Der Abdeckungsbericht nennt Umfang und Dateigrößen reproduzierbar.

```powershell
python -m uv run --locked python tools/build_hsa_case.py --check
python -m uv run --locked python -m pytest tests/test_build_hsa_case.py tests/test_hsa_bindings.py -q
```

HSA-ODD-Konformität, Faksimileprüfung, externe Registerauflösung und allgemeine
P5-Migration bleiben offen. Der tatsächlich ausgeführte Abschluss steht in
[[knowledge/state]]; die fachliche Abnahme bleibt eine eigene Entscheidung.
