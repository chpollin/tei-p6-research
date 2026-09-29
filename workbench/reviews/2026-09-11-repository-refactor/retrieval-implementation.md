# Integration von Suche und Quellenauswahl

Stand: 2026-09-11. Basis: `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0`.
Dieser technische Bericht ist keine Forschungsquelle.

Der Opus-Worker lieferte `tools/retrieval.py`, `tools/select_sources.py`, die
Erweiterung der Guidelines-Navigation und zugehörige Fixtures und Tests.
Sein CLI-Lauf wurde vor einer finalen Selbstauskunft beendet. Der Integrator
hat den gelieferten Code gelesen, ausgeführt und ergänzt; ein Workerbericht
wird für diese Lieferung nicht als Prüfbeleg angesetzt.

Die Suche trennt Repräsentation, Destillat, Assertion, Kapitel und
Projektwissen. Prüfstatus und Datumsfelder, Quellenfamilie, konkrete
Aufnahmerolle, Releasecommit, Prüfsummen und direkte Belegverweise bleiben
sichtbar. Kontroverse Assertions nennen ihre Gegenposition. Quellenautorität
wird aus Aufnahmemanifest und Registry gelesen; ein Dateiname begründet sie
nicht. Themen aus Destillatmetadaten und regelbasierte Vorschläge werden
getrennt ausgewiesen. Die Suche liest keine Original- oder Rohdateien.

Die Auswahl arbeitet auf benannten, gespeicherten Streams. Sie zählt einen
GitHub-Arbeitseintrag über `work-item-detail` einmal; ergänzende Records
bestimmen Issue oder Pull Request. SourceForge-Migration und TEI-L-Threadidentität
werden aus ähnlichen Titeln nicht abgeleitet. Fehlende Streams ergeben eine
unbekannte Trefferzahl. Der Integrator vereinheitlichte die Manifestauflistung
mit der Quellensteuerung und ergänzte die Kontrolle der Streamprüfsumme gegen
das Manifest sowie sichtbare Hinweise auf lexikalische Teilergebnisse.

Die gezielte integrierte Prüfung von Suche, Auswahl, Guidelines-Navigation,
Quellensteuerung und Wiederaufnahme bestand 134 Tests. Der abschließende
Gesamtstand wird in `knowledge/state.md` und im Integrationsbericht dieses
Verzeichnisses geführt. Die Suchtests prüfen Auffindbarkeit innerhalb benannter
Treffergrenzen; sie bewerten keine wissenschaftliche Aussage.
