# Technischer Prüfstand vom 11. September 2026

Der gemeinsame Abschlussgate ist offen. Der integrierte Gesamtlauf ergab
1.917 bestandene und drei fehlgeschlagene Tests, einen Plattform-Skip und
zehn bekannte RDFLib-Deprecation-Warnungen. Die drei Fehler betreffen zwei
Textidentitäts-Pilotchecks mit veralteten Prompts und den V1-Check mit
fehlenden Abschlusssiegeln. Der gesonderte Wave-1-Checker weist ebenfalls
seine inzwischen geänderten Prompts zurück. Diese Fehler werden erst durch
neue tatsächliche Reviews behoben.

Der erste diagnostische Gesamtlauf hatte 22 Fehler. Zwei Integrationsfehler
bei neuen Quellen wurden korrigiert: quellenweise Rechteangaben in Manifesten
werden der jeweiligen Repräsentation zugeordnet, und lokale Originale
erscheinen in der Materialübersicht ohne öffentlichen Dateilink. Veraltete
Projektionen und Seiten wurden regeneriert; der Test der TEI-L-Läufe wurde
um die zwei dokumentierten Vorläufe und den abgeschlossenen Monatsabruf mit
Wiederaufnahme ergänzt. Der anschließende Gesamtlauf lässt ausschließlich
die oben genannten drei Reviewfehler offen.

Eine danach geprüfte Korrektur übernimmt den gepinnten Commit einer
ausdrücklich als Git-Blob aufgenommenen Publikation aus ihrem Quelleneintrag.
Der Commit der letzten Änderung wird davon unterschieden. 24 gezielte Tests
für Suche und Quellenmetadaten bestehen. Eine tatsächliche Suche nach
`blueprints` mit dem vollständigen Commit `eb924226d12d22599bae9dad4fc53bc748b3f121`
liefert die zugehörigen P6-Folien. Die erneute komplette Abschlussprüfung
folgt nach den ausstehenden semantischen Reviews.

Weitere ausgeführte Prüfungen:

- Schema, Inventar und alle vier Kapitel: keine Fehler oder Warnungen.
- Ruff und Diffprüfung: bestanden.
- Quellensteuerung sowie Guidelines-, Textstruktur-, Praxis-, Identitäts-
  und Editionsaufnahme: abgeglichen.
- Alle 888 Guidelines-XML-Dateien exportiert und bytegenau verifiziert.
- Modelle 0.1 und 0.2, Identitätsprofil, redaktionelle Fälle, HSA-Fall und
  dokumentarische Ontologie reproduzieren ihre begrenzten Berichte.
- Alle fünf Seiten neu erzeugt und lokal mit HTTP 200 ausgeliefert.
  Die abschließende Seitenreproduktion bestand sechs Tests.
  Kein geprüfter Link verweist auf lokale Originale oder den Rohdatenbereich.
  Eine erneute visuelle Browserprüfung war mangels verfügbarem Browser
  nicht möglich.
- Der lokale V1-Check und das öffentliche Zwischensiegel bestätigen dieselben
  397 aktuellen Urteile bei 837 Einheiten, ohne fehlende Quellenkontexte.
  Sie weisen 440 ausstehende Urteile aus und melden keinen Gesamt-Pass.

Es wurde weder ein wissenschaftliches `verified` vergeben noch committed,
gepusht oder veröffentlicht. Die Projekt- und Übergabedokumente halten den
ausführbaren Wiedereinstieg fest. Vollständige Testausgaben und rohe
Modellantworten bleiben lokal.
