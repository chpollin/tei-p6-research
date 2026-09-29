# Datenbestand und Quelleneignung

Der Aufnahmebestand dieser V1-Ausführung umfasst 903 unveränderliche
Repräsentationen sowie 17 zitationsbasiert geführte Publikationsquellen.
Daraus sind 61 Destillate, 120 Assertions und vier Kapitel entstanden.
Der Begriff Publikation umfasst hier auch Standards, Tickets und
Council-Unterlagen. Zwei dieser Quellen sind wissenschaftliche Aufsätze.
Das [Inventar](../../../corpus/projections/source-inventory.md) führt die
einzelnen Dokumente; [State](../../../knowledge/state.md) führt den aktuellen
Prüfstand und die Quellenfamilien.

| Daten | Verwendungszweck | Verbleibende Grenze |
|---|---|---|
| P5 4.12.0: 888 Guidelines-Quellen und zwei zusätzliche Testdateien | Releasegebundene Definitionen, Deklarationen und konkrete Beispiele | Aufnahme deckt wesentlich mehr ab als die Destillation. Effektive ODD-Vererbung und erzeugte Schemas brauchen eigene Verarbeitung. |
| Offizieller P6-Prozess: README, sieben Council-Seiten und eine gepinnte Foliendatei | Offizielle Selbstbeschreibung, berichtete Diskussion, vorläufige Übereinstimmung und ausdrücklich protokollierte Entscheidungen | Weitere Council-Seiten, Ergebnisse aus Vancouver und zugängliche Sandbox-Inhalte fehlen. Ein HTTP 404 beantwortet deren fachlichen Inhalt nicht. |
| GitHub, SourceForge, Council, Board und öffentliche TEIC-Git-Inventare | Historische Probleme und Entscheidungswege auffinden und gezielt untersuchen | Inventarisierung belegt keine vollständige lokale Verfügbarkeit. Kommentar, Beschluss, Merge und Release erhalten eigene Belege. |
| TEI-L und Webarchive | Praxisprobleme, Gegenbeispiele und zeitgenössische Diskussionen | Zeitliche Lücken und Zugriffsgrenzen bleiben explizit. Die Speicherung einer Monatsübersicht beweist keine Aufnahme ihrer Nachrichtentexte. |
| DraCor, EpiDoc und CMIF: je eine ODD, ein Verarbeitungsdokument und eine konkrete XML-Datei | Unterschiede der Anpassung, Modulwahl, Schematron-Nutzung und Schemaverweise an echten Dateien vergleichen | Neun gepinnte Quellen bilden eine gezielte Auswahl. Die Verarbeitungsketten wurden in diesem Aufnahmeverfahren nicht ausgeführt; Repräsentativität und erwartete Ergebnisse brauchen fachliche Prüfung. |
| Humboldt-Tagebuch, Schuchardt-Brief und Stefan-Zweig-Werke | Begrenzte Editions- und Katalogbeobachtungen; Identität, Datierung und Zuschreibung | Einzelne Quellen und Fragmente tragen keine allgemeine Editionsmigration oder vollständige Katalogabdeckung. |
| W3C Web Annotation | Vergleichsstandard für Selektoren und Annotation | Seine Normativität gilt für den benannten W3C-Standard und dessen Version. |
| Piez sowie Renear/Wickett | Unterschiedliche begriffliche Argumente zu Hierarchie und Dokumentidentität | Argumente liefern keine Messung von Bedienbarkeit, Migration oder aktueller P5-Funktion. Der jeweilige Argumentationskontext gehört zur Aussage. |

Die Quellenfamilien überschneiden sich. Beispielsweise enthält der
TEIC-Organisationszensus Repositories, die zusätzlich unter P6, Website oder
Werkzeugen ausgewertet werden. Ihre Zählungen dürfen nicht addiert werden.

## Literatur und Ablenkung

Eine pauschale Entfernung der beiden Aufsätze würde begriffliche Alternativen
aus dem Vergleich nehmen. Beide bleiben mit begrenzter Funktion erhalten.
Für weitere Literatur gilt die [Aufnahmeregel](../../../knowledge/data.md):
Ein Text muss eine benannte Forschungsfrage, eine empirische Beobachtung
oder einen Gegenbeleg betreffen. Allgemeine TEI-Erwähnungen reichen nicht.
Ungeprüfte Kandidaten bleiben außerhalb des Standardkontexts einer Frage.

Die größere Verwechslungsgefahr liegt in der Gleichbehandlung verschiedenartiger
Treffer: Inventare dienen der Navigation, ein Ticket belegt zunächst eine
Äußerung, und ein Beispiel bleibt ein Beispiel. Die Suche zeigt deshalb
Schicht, Version, Herkunft und Prüfstatus; die Belegkette bleibt davon getrennt.
Die [Einzelprüfung der 32 Wontfix-Fälle](../../selections/2026-09-11-wontfix-context.md)
zeigt außerdem, warum ein Schließungslabel allein keine Ablehnungsentscheidung
beweist. Drei Fälle sind für passende Themenläufe zur Aufnahme empfohlen.

## Fachlich noch zu entscheiden

- **Decision:** Welche Editions-, Korpus- und Katalogaufgaben sollen die
  Architekturvarianten unterscheiden? Die drei neuen Projektfamilien sind
  eine belegte Ausgangsauswahl; sie ersetzen keine begründete Stichprobe.
- **Input:** Welche erwarteten Ergebnisse und Gegenfälle erkennt eine
  TEI-Fachperson in diesen Materialien als fachlich maßgeblich an?
- **Action:** Menschliche Verifikation der ausgewählten Aussagen und der
  drei Konfliktpaare durchführen. Nur die bezeichnete menschliche Rolle
  darf `verified` vergeben oder einen Konflikt auflösen.
- **Decision:** Die Architekturvarianten anhand der tatsächlichen
  Vergleichsergebnisse bewerten. Synthetische Rundläufe und bestandene
  Quellenreviews begründen für sich noch keine bevorzugte Architektur.

Die [Quellenauswahl der Praxisfälle](../../selections/2026-09-11-odd-practice.md)
und die [P6-Auswahl](../../selections/2026-09-11-p6-process.md) enthalten
Versionen, Aufnahmebelege und die konkret ausgelassenen Bereiche.
