# Repository-Refactoring vom 2026-09-11

Das Repository wurde lokal strukturiert, seine Suchwege wurden ausführbar
gemacht und drei belegte Fehler im Modell korrigiert. Die Evidenzkette und
die Quellenidentitäten bleiben bestehen. Der Forschungsbestand reicht
weiterhin nicht für eine allgemeine Architektur- oder Migrationsentscheidung.
Der aktuelle Prüfstand steht in [State](../../../knowledge/state.md).
Es wurde nichts committet, gepusht oder veröffentlicht.

## Umgesetzt

| Bereich | Änderung und Wirkung |
|---|---|
| Orientierung | `knowledge/INDEX.md` führt direkt zu Arbeitsaufgaben und grenzt die Modellversionen ab. State beschreibt den aktuellen Bestand; das vollständige Inventar liegt als generierte Projektion vor. |
| Verfahren | Die Quellenwahl hat ihren kanonischen Ort in `knowledge/operations.md`. Historische Fragen der Themenläufe liegen bei deren Auswahlprotokollen. Der Plan benennt Forschungsziele und überprüfbare Ergebnisse. |
| Redundanzen | Markdown-Leseregeln und Manifestauflistung sind gemeinsam implementiert. CI und Veröffentlichung verwenden denselben Prüfworkflow. Die Knowledge-Seite hält Quellenpassagen einmal statt zusätzlich im Suchattribut. |
| Agentenzugriff | Die lokale Suche liefert Pfade, Anker, Prüfstand, Versionsgrenze, Quellenrolle und Gegenpositionen. Die deklarierte Auswahl über gespeicherte Snapshots weist Treffer, Prüfsummen und Lücken aus. |
| Weboberfläche | Gewichtete Treffer, strikter Statusfilter und direkte Passagenlinks verbessern den Einstieg. Kuratierte Themen sind von automatischen Vorschlägen getrennt. Die Modellansicht benennt den Umfang von 0.1 und 0.2. |
| Quellenkontrolle | Der TEI-L-Lock beschreibt die tatsächlich abgeschlossenen Teile. Wayback-Abrufe können geprüfte Monatscheckpoints wiederverwenden; vorhandene Ergebnisdateien sind gegen Überschreiben geschützt. |
| Revisionsschutz | Bereits verwendete Entitätsarten, Claim-Träger und referenzierte Selektionen bleiben bei einer Revision gebunden. Die drei ursprünglichen Gegenfälle und zusätzliche Fehlformen sind geprüft. |

Die [Gegenbelegsuche](../../selections/2026-09-11-counterevidence-reconciliation.md)
ergänzt die fehlende Wontfix-Abfrage zweier historischer Themenläufe. Ihre
Kandidaten benötigen fachliche Einzelprüfung. Referenzquellen wurden wegen
einer geringen Trefferrelevanz nicht gelöscht: Ihre Eignung wird pro Frage
und Aussageart bewertet. Quellenfamilie, konkrete Aufnahmerolle, Version und
Belegpassage müssen zusammenpassen. Die verbindliche Rollenordnung steht in
[Data](../../../knowledge/data.md).

## Prüfung und Grenzen

Die Teilprüfungen sind in [Modell](model-implementation.md),
[Quellenkontrolle](sources-implementation.md) und
[Retrieval-Integration](retrieval-implementation.md) dokumentiert. Entscheidend
ist der gemeinsame Abschlusscheck des integrierten Repositorys: 1.780 Tests
bestanden, ein Skip wegen fehlender Symlinkberechtigung und zehn bekannte
RDFLib-Warnungen. Ruff, Schema, Inventar, Quellensteuerung, Guidelines-Navigation
und die betroffenen Modellberichte bestanden. Nach der abschließenden
Dokumentation und Seitenregeneration bestanden zusätzlich 38 Tests für
Knowledge, Arbeitswege und die Reproduktion aller fünf Seiten. Der Browserlauf prüfte
relevante Treffer, den strikten Statusfilter, kuratierte Themen, Nulltreffer
und die direkte Öffnung samt Fokus auf einer Quellenpassage; keine
JavaScript-Fehler wurden beobachtet. Die verkleinerte Knowledge-Seite enthält
weiterhin die vollständigen aufgenommenen Passagen. Der aktuelle Stand
steht in [State](../../../knowledge/state.md). Eine erzeugte Prüfdatei oder
ein Suchtreffer bestätigt keine fachliche Aussage. `verified` wurde nicht
vergeben. Die neue Wayback-Wiederaufnahme ist offline geprüft; ein neuer
Produktionsabruf gehört zur offenen Quellenarbeit.

## Inhaltlich zu besprechen

- Welche konkreten Editionen, Korpora und Kataloge sollen die repräsentativen
  Vergleichsfälle liefern? Benötigt werden Material, Aufgabe und das fachlich
  erforderliche Ergebnis einschließlich eines Gegenfalls.
- Welche Modell- und Migrationskriterien sind für diese Aufgaben verbindlich?
  P5-Reparatur, kompatible Weiterentwicklung und Ersatzarchitektur sollen an
  derselben Grundlage bewertet werden.
- Welche Stichprobe soll der menschlichen Verifikation unterzogen werden?
  Der Projekteigentümer ist bereits zur Verifikation berechtigt; die Auswahl
  und das Urteil stehen aus.

Die übrige fachliche Arbeit ist in [Plan](../../../knowledge/plan.md) und
[State](../../../knowledge/state.md) beschrieben: unabhängige Quellenreviews,
Behandlung kontroverser Befunde und die begrenzte Ergänzung fehlender
Quellenbereiche. Die technische Refaktorierung hebt diese Prüfpflichten nicht auf.
