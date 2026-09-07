# Modellwissen und Beispiele konsolidieren

Der Lauf integriert die Nutzerdiskussion in die bestehenden Wissensdokumente.
Er ist eine Dokumentations- und Konsistenzprüfung. Er vergibt keinen
Forschungsstatus und liefert keine unabhängige Quellenprüfung.

## Auftrag und Zuständigkeiten

Basis ist Commit `32e9c43f9fe09314447f4d6f73aca4033b8875b8` mit bereits
vorhandenen gestagten und ungestagten Änderungen. Der unveränderte
[Brief](brief.md) hat SHA-256
`1eaa034cb2314d6d1e1404b999f995d0754ade9a81301e4f940400c997cb626e`.

GPT-6 Astra konsolidierte das Modellkonzept. GPT-5.6 Sol bearbeitete die
P5-Kriterien; ein weiterer Sol-Agent prüfte die Dokumentation read-only.
Der Integrator bearbeitete die übrigen Dateien und wiederholte die Prüfungen.
Nach dem Brief ergänzte der Nutzer die Anforderung, alle Beispiele in XML,
JSON und RDF mitzudenken. Ein Folgeauftrag erweiterte die Schreibzuständigkeit
des Modellagenten auf `knowledge/model-examples.md`. Die Aufteilung nach
Aufgabenschwere folgt der ausdrücklichen Modellwahl des Nutzers.

## Integration

- `knowledge/model-design.md` übernimmt die vorgeschlagenen Begriffe und
  die dauerhaften Anforderungen der früheren Abschnitte 10 und 11 des
  Textmodells. Modellierungsebenen, primitive Konstrukte, Reihenfolge,
  gemischter Inhalt, Hierarchien, Selektionen, Referenzen, Eigenschaften,
  Normalisierung und Constraints bleiben erhalten. Die alten Abschnittsziele
  leiten auf die kanonischen Orte weiter.
- `knowledge/model-examples.md` enthält vier vollständige illustrative Fälle
  mit Ressourcen, Definitionen und Aussagen in den drei Syntaxen. Die
  Briefinterpretation bleibt ausdrücklich ein konstruiertes Beispiel.
- Kapitel 02 ergänzt fünf Posits zu anwendungsübergreifendem Text,
  eigenständigen Namen, offenen Klassifikationen, kontextgebundenen Referenten
  und P5-Erhaltung. Die neun bereits zugelassenen Prämissen bleiben erhalten.
- README, Adapter, Index, Architektur, Spezifikation, Bewertung, Experimente
  und Arbeitswege verweisen auf dieselben Begriffe und Zuständigkeiten.
- Die Codeprüfung widerlegte die frühere Dokumentationsbehauptung über
  XML/JSON/YAML-Codecs für 0.2. Ein gültiges 0.2-Referenzbeispiel wird von
  `encode_model` in allen drei Syntaxen abgewiesen. Die Dokumentation und
  `experiments/entities_v02/spec.json` nennen jetzt den tatsächlich
  implementierten Umfang. Kein Codec wurde erweitert.

## Prüfung am 2026-09-07

Der Integrator parste die vier XML-, JSON- und Turtle-Blöcke. XML-Attribute
wurden nach den dokumentierten Literal- und Referenzregeln in dieselben
Records überführt. Aus JSON wurde der vollständige erwartete RDF-Graph
rekonstruiert und mit dem geparsten Turtle-Graph als Menge verglichen.
Alle IDs und Referenzen lösen auf, alle sechs Unicode-Ausschnitte stimmen,
und direkte unqualifizierte Welttripel der Claim-Inhalte fehlen.

| Fall | Ressourcen | Claims | RDF-Tripel |
|---|---:|---:|---:|
| Briefsatz | 29 | 12 | 251 |
| Organisation | 11 | 4 | 79 |
| Olympus | 9 | 2 | 60 |
| Atlantis | 11 | 3 | 75 |

Die abschließende Sol-Durchsicht fand keine materiellen Widersprüche in den
beiden neuen Dokumenten. Die 1.463 geprüften lokalen Dokumentverweise und
20 Markdown-Abschnittsverweise lösen auf. Acht vorhandene Workbench-Routen
mit `#example=` sind Anwendungszustände und keine Markdown-Überschriften.

`git diff --check`, Ruff, Vollvalidierung und beide Kapitelvalidierungen
bestehen ohne Fehler oder Warnungen. Quellen-Control-Plane, Modellberichte
0.1/0.2, Textidentität, Quellenprofil, Editorial-Fälle und Guidelines-Navigation
reproduzieren. Der bestehende Wave-one-Audit bestätigt seine acht Verdicts.
Der vollständige Testlauf besteht mit 1.441 erfolgreichen Tests und einem
plattformabhängigen Symlink-Skip. Nach Rückschreibung des aktuellen Stands
wurden die betroffenen Seiten erneut erzeugt. Die sechs Tests in
`tests/test_build_pages_reproduce.py` bestehen und bestätigen die Reproduktion
aller fünf Seiten. Abschließende Vollvalidierung und `git diff --check` bestehen.

## Geltungsgrenze

Die Syntaxbeispiele sind prüfbare Entwürfe eines eigenen illustrativen
Formats. Die ausführbaren Modelle behalten ihre bisherigen Regeln. Neu
vorgeschlagene Namen und Ortskontexte sind keine implementierte Version 0.3.
Ontologieverweise bleiben Rechercheeinstiege. Vollständige P5-Abdeckung,
repräsentative Migration, 0.2-Roundtrips und fachliche Nutzerabnahme bleiben
offen. Der Lauf übernimmt keine neuen Quellen in die Evidenzkette und
verändert keine bestehenden Forschungsstatus. Es wird weder committet noch
gepusht oder veröffentlicht.
