# Review des HSA-Falls 4493

Der Auftrag konkretisiert den P6-Entwurf an einem vollständigen, bereits
aufgenommenen P5-Brief. Der ausführbare Versuch und die erklärende
Gegenüberstellung liegen unter `experiments/hsa_letter_4493/`. Dieser
Reviewbericht ist ein Prozessartefakt außerhalb der Grounding-Kette.

Der unveränderte Arbeitsbrief `brief.md` hat SHA-256
`704e99fb988a966f14307b03c02e259c261dc9acdc7f744d12f49aa835916836`.
Der verwendete XML-Snapshot hat SHA-256
`f37ff85df57405753aa0b6d1db63f3a24fcbd33ab1ef7fb54b68844e556e2438`.
Die Ausgangsrevision war `32e9c43f9fe09314447f4d6f73aca4033b8875b8` mit
umfangreichen bereits vorhandenen Änderungen. Diese wurden erhalten.

## Rollen und Umfang

Ein GPT-6-Agent implementierte ausschließlich den Generator, sein Testmodul
und die generierten Fallartefakte. Ein weiterer GPT-6-Agent las den gesamten
Brief und prüfte anschließend den Instanzgraphen. GPT-5.6 Sol verglich die
erklärende README mit dem vollständigen Snapshot. Der Integrator schrieb
die Erklärung und Wissensintegration und wiederholte die Prüfungen am
integrierten Dateistand. Diese Maschinenprüfungen verleihen den bestehenden
Quellen und Assertions keinen höheren wissenschaftlichen Prüfstatus.

## Inhaltliche Gegenproben

| Befund | Konsequenz |
|---|---|
| Trägerherkunft steht unter `msDesc/history/origin`. | Keine automatisch datierte Schreibhandlung mit einem erschlossenen Schreiber. |
| Die XML-Publikation und die bibliografische Korrespondenzedition haben unterschiedliche Jahresangaben. | 2022 als digitaler Publikationskontext; 2016 ausdrücklich als erhaltene bibliografische Angabe. |
| Empfangsangaben nennen nur die Person. | Keine erfundenen Empfangsdaten oder Orte. |
| `Frollo` und `G.L. Frollo` liegen in unterschiedlichen Textschichten. | Getrennte Namensformen und Mention-Spans mit berichteter gleicher Quellenreferenz. |
| Diez und mehrere Hervorhebungen enthalten XML-Leerraum. | Der Versuch bewahrt die geparsten Zeichendaten und benennt seine Projektionsregel. |
| Noten 10 und 11 stehen unmittelbar vor Satzzeichen. | Nachfolgender Text bleibt im Brief; der Notenanker bezeichnet nur den Einfügepunkt. |
| PID und `div/@xml:id` weichen ab. | Beide Quellenwerte bleiben erhalten. |
| Der erste Graph verband Text und Repräsentation, aber nicht Text und Briefdokument. | Die qualifizierte Zuordnung `proposition-text-document` verbindet sie jetzt mit Quellenbezug und ausdrücklicher Importverantwortung. |
| Die Aufteilung von Brief und Träger war zunächst als Quellenbericht markiert. | Die eigene Modellentscheidung besitzt jetzt Konstruktionskontext, Begründung und `assert`-Haltung. |
| Der erste Graph klassifizierte Referenzdatensätze nur über Labels. | Revidierbare erwartete Gegenstandstypen werden über definierte ConceptRecords ausdrücklich gemacht. |
| Der P5-Ausschnitt wiederholt die geerbte Namespace-Deklaration. | Die README beschreibt diese Anpassung, statt nur veränderte Einrückung zu behaupten. |

Die Prüfung unterscheidet den Quelleninhalt von seiner vorgeschlagenen
Modellierung. Eine exakte XPath-Belegstelle begründet einen überprüfbaren
Importbericht. Sie stellt keine unabhängige historische Verifikation der
beschriebenen Ereignisse her. Die erhaltene P5-Datei beweist für sich keine
vollständige semantische Rückkonvertierung.

## Abschlussprüfung

Der Integrator wiederholte alle 24 Falltests und die Reproduktion der sieben
generierten Artefakte. Sie bestanden ohne Warnungen. Der rekonstruierte
P5-Snapshot hat die ursprüngliche Prüfsumme. Alle 81 bisherigen Ontologie-
und Beispieltests bestanden ebenfalls; die zehn Warnungen stammen aus
RDFLibs bekanntem JSON-LD-Parserpfad.

Der vollständige Testlauf meldete 1.545 bestandene Tests, einen
plattformabhängigen Skip und einen veralteten Textidentitätsbericht. Der
Vergleich zeigte ausschließlich die geänderte Prüfsumme von
`knowledge/experiments.md`; alle 38 Fallresultate waren identisch. Nach
Regeneration bestanden sämtliche 57 Tests des betroffenen Piloten und
seiner Support-Prüfung. Der anschließend durchlaufene vollständige
Support-Gate bestand mit 1.546 Tests, einem plattformabhängigen Skip und
den zehn bekannten RDFLib-Warnungen. Quellen-Control-Plane, Kapitelprüfung
und die begrenzten Pilot-Support-Verdikte bestanden ebenfalls.

Der Turtle-Ausschnitt in der Fall-README ist eine echte Teilmenge des
generierten Graphen. Ihre ausgeführte SPARQL-Abfrage liefert die beiden
getrennten Datumskontexte und jeweiligen Quellpfade. Die Konstruktionen für
Text, Dokument und Träger sowie die sieben erwarteten Gegenstandstypen
wurden am finalen Graphen nochmals nachgelesen. 118 lokale Markdown-Dateiziele
lösen auf; der Arbeitsbrief ist unverändert.

Ruff und die Gesamtvalidierung bestanden; Letztere meldete null Fehler und
null Warnungen. `git diff --check` blieb ohne Befund. Die neuen XML-/Turtle-
Artefakte enthalten ausdrücklich erhaltenen Quellenleerraum in Literalen.
Ihre eng begrenzten `.gitattributes`-Regeln behandeln diesen als Quelldaten;
die Quellkopie erhält zusätzlich keine Git-Zeilenendnormalisierung.

Alle sechs Reproduktionstests für die fünf generierten Seiten bestanden.
Nach der letzten Zustandsrückschreibung bestanden sie erneut. Auch die
abschließende Gesamtvalidierung und `git diff --check` blieben ohne Befund.
Quelle, Kapitel und bisherige Modellversionen werden durch diesen Fall
nicht wissenschaftlich neu akzeptiert. Es wurde nichts gestagt, committet,
gepusht oder veröffentlicht.
