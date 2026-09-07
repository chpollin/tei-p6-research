# Kritische Modellprüfung und Ontologieexperiment

Der Lauf prüft die bisherigen Modellentscheidungen, korrigiert konkrete
Unschärfen und legt einen begrenzten dokumentarischen Ontologiekern an.
Er vergibt keinen Forschungsstatus und ersetzt keine fachliche Nutzerabnahme.

## Auftrag und Ausführung

Basis war `32e9c43f9fe09314447f4d6f73aca4033b8875b8` mit vorhandenen gestagten
und ungestagten Änderungen. Der [Brief](brief.md) blieb unverändert, SHA-256
`30b3251e1afeb04d9bcf87f55200d73e4a7cd9d56da4072c1dc90ca07a09fc25`.
Der [Implementierungsauftrag](implementation.md) hat SHA-256
`6d23c6d2dfabca2d17cbcb084ef4bb93d0660594170902714117fa85ffecf060`.

GPT-6 Astra prüfte die Semantik und erhielt anschließend ausschließlich
`knowledge/model-design.md` zur Überarbeitung. Ein weiterer GPT-6-Agent
implementierte die sechs im Folgeauftrag benannten Ontologie-/Prüfdateien.
GPT-5.6 Sol prüfte Primärquellen zu den externen Begriffen und erhielt
anschließend ausschließlich `tests/test_model_design_examples.py`. Der
Integrator änderte Proposal, Beispiele, Mappingregister, Zuständigkeiten,
Dokumentation, Abhängigkeiten und Workflows und prüfte die integrierten Dateien.
Die Modellaufteilung folgt der ausdrücklichen Nutzeranweisung.

## Was die Prüfung ergeben hat

| Entscheidung | Bewertung und Begründung | Korrektur oder verbleibende Grenze |
|---|---|---|
| Text über Editionsarbeit hinaus | Tragfähige Anforderung. Gleicher Wortlaut kann unabhängig entstanden sein; verschiedene Transkriptionen können einem Text zugeordnet werden. | TextRecord dokumentiert sprachliche Identität. Repräsentationszuordnung, Sammlung und Austauschpaket bleiben getrennt. Kriterien brauchen fachliche Prüfung. |
| Name vom Referenten trennen | Tragfähig, aber Name und Form waren vermischt. | NameFormRecord identifiziert die dokumentierte Form. Ein weiterer Name-Gruppierungsbegriff bleibt bedarfsabhängig. |
| Personen-/Ortsname als Formklasse | Für den bisherigen Entwurf zu stark. Victoria kann in beiden Funktionen auftreten. | Verwendungskategorie an der Erwähnung oder Namenszuweisung, keine intrinsische nameType-Eigenschaft der Form. |
| Record vom beschriebenen Gegenstand trennen | Erforderlich für korrigierbare und narrative Referenz. | Prädikate geben record/referent/concept/proposition als Argumentinterpretation an. Keine Person-/Place-Vererbung auf ReferentRecord. |
| Organisationen offen klassifizieren | Für Tätigkeit, Zweck und Form begründet. | Person und Organisation bleiben mögliche Domänentypen. Verfasser, Empfänger und Mitglied sind kontextuelle Rollen. |
| Historische und erzählte Orte | Ein einzelnes fictional-Attribut und eine Koordinate reichen für die benannten Aufgaben nicht. | Zeit, Identifikation, Tradition, Erzählkontext und Bewertung bleiben getrennt. Keine automatische geografische Schlussfolgerung. |
| Ein Claim für Inhalt und Verantwortung | Für Berichten und Bestreiten desselben Inhalts unzureichend. | Proposition und Haltung werden getrennt. Rücknahme ist ein Lebenszykluszustand. Die Annotation kann einen anderen Target als die Belegstelle haben. |
| Alle Claims teilen denselben Beleg | Als pauschale Begründung unzutreffend. | evidence dokumentiert im Beispiel den Inhalt. Eigenständige Gründe für unterschiedliche Haltungen bleiben ein offenes Quellenprofil. |
| Identifikation als Vorschlagsinhalt | Die Definition „proposes that“ machte eine Verneinung mehrdeutig. | Der Inhalt benennt die mögliche Referentenidentität; assert/question/deny tragen die Haltung separat. |
| XML, JSON und RDF gleichwertig darstellen | Sinnvolle Prüfforderung, durch Parsing allein nicht erfüllt. | Vollständige Records und RDF-Tripel werden verglichen. Das beweist die begrenzte Darstellungsgleichheit, keine vollständige Bedeutungsäquivalenz. |
| Ontologien verbinden | Ein strukturierter Vergleich ist nützlich. Gleiche Klassennamen rechtfertigen keine Übernahme. | Vierzehn Kandidaten mit Begründung und Primärquellen; keine Imports, Gleichsetzungen oder fremden Klassenaxiome. |
| Bestehender 0.2-RDF-Export | Seine Strukturtests belegen keine ontologische Angemessenheit. | Beschreibung nennt jetzt mögliche Inferenzfolgen und die Record/Gegenstand- sowie Claim/Aktivität-Grenze. Der alte Bindingvertrag bleibt bestehen. |
| P5-Kompatibilität | Weiterhin ein erforderlicher Nachweis. | Die neue Hierarchie liefert keine vollständige Migration. Bestehende Revisionslücken und fehlende 0.2-Roundtrips bleiben offen. |

## Artefakte und Prüfgrenze

Der Kern enthält 21 Klassen und 28 Properties in 224 RDF-Tripeln. Turtle,
RDF/XML und JSON-LD werden als derselbe RDF-Graph geprüft. Die Record-Hierarchie
entsteht aus den deklarierten Subklassenbeziehungen. Die Domänenhierarchie in
`knowledge/model-design.md` hat eine eigene begriffliche Bedeutung.

Die sechs Beispielpakete enthalten 86 Ressourcen, 30 Propositionen, 32 Claims
und acht Selektionen. Ihre 875 RDF-Tripel stimmen mit den XML-/JSON-Records
überein. Der Namensgebrauchsfall und die drei Haltungen zu Q1 sind eigene
semantische Gegenproben. Die finalen Prädikatsdefinitionen entfernen den
Vorschlagsakt aus dem geteilten Aussageinhalt.

Der Integrator wiederholte die 30 Ontologietests, 51 Beispieltests und vier
Workflowtests. Alle bestanden. Die zehn Warnungen betreffen RDFLibs internen
veralteten `ConjunctiveGraph`-Aufruf beim JSON-LD-Parsing. Sie verändern die
geprüften Graphen nicht. Ruff und Kapitelvalidierung bestehen ohne Befund.
Der vollständige Lauf in der über `uv.lock` festgelegten Umgebung besteht mit
1.522 Tests, einem plattformabhängigen Symlink-Skip und den zehn genannten
RDFLib-Warnungen. Beide Kapitelvalidierungen und die Quellen-Control-Plane
bestehen. 1.518 lokale Dokumentverweise sowie die Abschnittsverweise von
Modellentwurf, Ontologievertrag und Proposal lösen auf. Nach der endgültigen
Rückschreibung bestanden auch die sechs Reproduktionstests für die fünf
generierten Seiten. Die abschließende Gesamtvalidierung meldete null Fehler
und null Warnungen; `git diff --check` blieb ohne Befund.

Ein unnötiger Schreibversuch auf den unveränderten 0.1-Bericht meldete unter
Windows `Invalid argument`. Der anschließende read-only Reproduktionscheck
bestand; der bereits korrekte Bericht benötigte keine Änderung.

Die Tests nutzen keinen OWL-Reasoner und liefern keine vollständige
SHACL-Validierung. Individuelle Claim-Begründungen, verschachtelte
Quellenberichte, komplexe Zeit-/Unsicherheitsmodelle, Kontextübergänge und
fachlich begründete externe Brücken bleiben offen. Die Arbeit ist lokal;
es wurde nichts gestagt, committet, gepusht oder veröffentlicht.
