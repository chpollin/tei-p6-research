# Datenbestand, Quelleneignung und Vollprüfung

Stand: 2026-09-11. Basis: `7d7b7e47ce3eacf605a19ca4dd711d016c2655a0` mit den lokalen Änderungen. Dieser Bericht dokumentiert eine Bestandsprüfung und die Vorbereitung des Meilensteins V1. Er enthält keine neuen fachlichen Freigaben. Prüfberichte und Suchprojektionen sind keine Grounding-Ziele.

Der Referenzbestand ist breit, die wissenschaftliche Auswertung konzentriert sich auf wenige Themen. Die wichtigste Lücke liegt in der Prüfung und gezielten Auswertung bereits vorhandener Quellen. Bei Literatur sind bisher zwei Aufsätze und ein technischer Standard aufgenommen. Eine breite Erweiterung um weitere Publikationen ist für die nächste Forschungsarbeit nicht begründet.

## Was tatsächlich vorhanden ist

Das [Quellenregister](../../../sources/registry.yaml) enthält 18 Quellenfamilien. Drei tragen für ihre damalige Beobachtungsgrenze `observable-complete`, 15 bleiben `partial`. Ein Inventar mit Kennungen und Verweisen ist von einem lokal verfügbaren Volltext zu unterscheiden. Auch ein historisch abgeschlossener Abruf garantiert keine heutige Verfügbarkeit seiner ignorierten Rohdateien in diesem Checkout.

| Quellenfamilie | Vorhandener Bestand | Grenze und geeignete Verwendung |
|---|---|---|
| P5 4.12.0 | Releasebindung, Git-Spiegel, Release-ZIP; 888 unveränderliche Guidelines-Repräsentationen mit allen 24 Hauptkapiteln und 846 Spezifikationen. 29 Guidelines-Destillate sowie zwei Destillate zu zusätzlichen P5-Testdateien. | Normative Referenz dieses Releases. Die Aufnahme ist wesentlich breiter als die Auswertung. HTML-/ZIP-Abgleich und effektive ODD-Vererbung bleiben offen. |
| GitHub TEIC/TEI | 2.476 Issues, 455 Pull Requests, 19.565 Issue-Kommentare, 74.981 Timeline-Ereignisse; zusätzlicher Lauf mit 16.003 Relationen und 674 Review-Threads. Fünf Thread-Destillate. | Metadaten und Relationsläufe sind erfasst; die Vollständigkeit lokaler Rohtexte wurde hier nicht global geprüft. Diskussion, Beschluss, Merge und Release müssen einzeln belegt werden. |
| TEIC-Organisationszensus | 41 öffentliche Repositories im damaligen Zensus. | Vollständig innerhalb dieser beobachteten Grenze; keine aktuelle Aussage über sämtliche TEI-Projekte. |
| Öffentliche TEIC-Git-Bestände | Für 41 Repositories protokollierte Beobachtungen und normalisierte Bauminventare; zusammen 25.415 Baumeinträge und 40.957 gezählte Commits. | Lokal liegt unter `corpus/raw/git/` nur `TEIC-TEI.git`. Die anderen 40 Spiegel fehlen hier; daraus folgt nicht, dass ihre protokollierten Abrufe nie stattgefunden haben. Repositories nach konkreter Frage auswählen. |
| Council-Protokolle | 206 Seitenantworten und 2.473 externe Links; von zehn Binärzielen wurde eines abgerufen. | Zentrale Governance-Quelle. Anhänge und externe Arbeitspapiere bleiben lückenhaft; keine entsprechende Destillation vorhanden. |
| Council-Arbeitsdokumente | Git-Inventar mit 16 Baumeinträgen und 322 Commits. | Historisch begrenzt `observable-complete`; lokaler Spiegel fehlt. Dokumenttyp und Entscheidungsstatus pro Text feststellen. |
| Offizieller P6-Prozess | Inventar von `timeForP6` mit 21 Baumeinträgen und 53 Commits; eine README-Repräsentation mit Destillat. | Das README beschreibt Präsentationsinfrastruktur. Es trägt keinen technischen P6-Konsens. Die P6-spezifische Auswahl aus Council-Protokollen ist offen; `p6-sandbox` war beim protokollierten Zugriff nicht öffentlich verfügbar. |
| P5-Releasehistorie | 50 Versionsverzeichnisse und 53 Indexantworten. | Einzelne Releasebestände sind noch nicht durch eigene Versions-Locks aufgenommen. Nur für konkret untersuchte Änderungen erweitern. |
| Board | 225 Antworten: 197 erfolgreich, 28 fehlgeschlagen; 358 externe Links. | Für institutionelle und strategische Entscheidungen relevant. Keine allgemeine Voraussetzung für eine technische P5-Analyse. |
| Historisches TEI-Archiv | 394 Seiten-/Indexantworten und 221 externe Links. | 363 Nicht-HTML-Artefakte und 424 Links an der Abruf-Tiefengrenze sind offen. Historische Fragen benötigen eine gezielte Auswahl. |
| SourceForge | 1.349 Tickets und 8.880 Diskussionseinträge inventarisiert; ein Ticket-Destillat. | Der r4-Lauf verwendete alle Tickets aus dem Vorlauf. Frühere Rohantworten fehlen lokal; Release-Dateien und alte Versionsverwaltung sind offen. r4 ist bisher nicht im Familien-Lock aufgeführt. |
| TEI Stylesheets | Git-Inventar mit 986 Baumeinträgen und 7.449 Commits. | Für tatsächliche Verarbeitung und Transformationskosten wichtig. Lokaler Spiegel fehlt; Work-Item-Zugang ist im Lock als damalige Lücke erfasst. |
| TEI-Werkzeuge | Sechs Werkzeug-Repositories mit zusammen 1.023 Baumeinträgen und 1.513 Commits inventarisiert. | Roma, Validierung und Konversion nach Vergleichsaufgabe untersuchen. Git-Inventare allein belegen kein Werkzeugverhalten. |
| TEI-Website | Git-Inventar mit 851 Baumeinträgen und 560 Commits. | Publikations- und Policy-Kontext. Lokaler Spiegel und Abgrenzung der Seitensnapshots bleiben offen. |
| Community/SIG | Drei Indexseiten mit 101 Links. | Arbeitsgruppen und Jahrestagungen sind damit nicht inhaltlich erfasst. Gezielte Praxis- oder Prozessfragen begründen weitere Aufnahmen. |
| Reale Anpassungen und Praxisfälle | Anpassungsindex mit zwei erfolgreichen Seiten und 122 externen Artefaktverweisen. Aufgenommen sind drei Humboldt-Tagebuchfragmente, ein HSA-Brief und SZD-Katalogdaten; das Humboldt-Paket enthält auch ein RNG-Schema. | Es fehlt eine begründete Stichprobe externer ODD-Anpassungen mit ihren Prozessoren und erwarteten Ergebnissen. Die vorhandenen Einzelfälle tragen keine allgemeine Migrationsbewertung. |
| Literatur und Vergleichsstandard | Vier Kandidaten: W3C Web Annotation, Piez 2014, Renear/Wickett 2010 aufgenommen; OHCO-Autorfassung 1993 wegen HTTP 403 nicht verfügbar. | Drei Destillate mit jeweils einem Zitat. Kein systematischer Literaturüberblick. Die historische Auswahl hatte konkrete Suchanfragen; ein übergreifendes Such- und Auswahlprotokoll fehlt. |
| TEI-L | Penn State: zehn Monate Dezember 2025 bis September 2026, 267 Nachrichten mit lokal vorhandenen Rohdateien. Wayback: 432 Monate auf Verfügbarkeit untersucht, davon 368 mit Capture und 64 ohne. | Für Wayback fehlt ein abgeschlossener Volltext-Abruf mit Ergebnismanifest. Ein Capture-Nachweis ist kein Nachrichtenbestand. Keine TEI-L-Destillate vorhanden. |

Die Mengen beziehen sich auf dokumentierte Läufe Anfang September 2026. Dieser Audit ist kein erneuter Vollabruf. Die Familien überschneiden sich: Die 41 Git-Repositories enthalten beispielsweise Stylesheets, Website und `timeForP6`. Ihre Zahlen dürfen nicht zu einem vermeintlichen Gesamtvolumen addiert werden.

Über alle Familien hinweg liegen **894 Repräsentationen, 44 Destillate, 107 Assertions und vier Ausgabekapitel** vor. Der Ordner `publications` enthält neun Destillate: zwei Aufsätze, einen W3C-Standard, fünf GitHub-Threads und ein SourceForge-Ticket. Der Ordnertyp allein ist deshalb kein Literaturfilter. Die vollständige Zuordnung liefert das [generierte Inventar](../../../corpus/projections/source-inventory.md).

## Quellenauswahl und Literatur

Für weitere Forschung empfehle ich als Kern die P5-Releasequellen, konkrete Entwicklungsentscheidungen, offizielle P6-Prozessdokumente sowie reale Anpassungs- und Verarbeitungsfälle. Die offenen Council-/P6-Dokumente und repräsentativen ODD-Fälle sind fachlich bedeutsamer als ein pauschaler Ausbau der Literaturmenge. Die [32 ergänzend gefundenen Wontfix-Kandidaten](../../selections/2026-09-11-counterevidence-reconciliation.md) benötigen eine inhaltliche Sichtung als mögliche Gegenbelege.

| Werk | Empfohlene Verwendung | Grund und Grenze |
|---|---|---|
| [W3C Web Annotation Data Model, Recommendation 2017](https://www.w3.org/TR/2017/REC-annotation-model-20170223/) | Gezielter Kernvergleich für Selektoren und die verwendete RDF-Abbildung. | Ein technischer Vergleichsstandard mit prüfbaren Regeln. Die Bedeutung von Präfix, Suchtext und Suffix muss erhalten bleiben. Keine TEI-Normativität. |
| [Piez 2014: Hierarchies within range space](https://www.balisage.net/Proceedings/vol13/html/Piez01/BalisageVol13-Piez01.html) | Bei einer konkreten Gegenüberstellung mit LMNL und Range-Modellen lesen. | Das Argument über optionale Hierarchien begründet ein mögliches Untersuchungsmodell. Daraus folgt kein empirischer Vorteil einer P6-Architektur. |
| [Renear/Wickett 2010: There are No Documents](https://www.balisage.net/Proceedings/vol5/html/Renear01/BalisageVol5-Renear01.html) | Für die konkrete Unterscheidung von Stringtransformation und fortbestehender Identität verwenden. | Die veröffentlichte Seite bezeichnet den Text als vorläufige Konferenzfassung. Seine philosophischen Positionen müssen den Autoren zugeschrieben bleiben. |
| OHCO-Autorfassung 1993 | Bis zu einer konkreten Frage nach historischen Hierarchieannahmen vertagen. | Volltext bislang nicht aufgenommen. Die Autorfassung und die Publikation von 1996 sind unterschiedliche Quellenfassungen. Es hängt kein bestehender Claim an diesem Kandidaten. |

Diese Empfehlungen entfernen keine Quelle und ändern keine bestehende Aufnahmeentscheidung. Jede zusätzliche Publikation sollte eine benannte Frage beantworten, einen notwendigen Begriff präzisieren, einen Vergleich ermöglichen oder einen möglichen Gegenbeleg liefern. Vor der Suche werden Frage, Quellenrolle, Suchwege und Ausschlussgründe festgehalten. Weder Bekanntheit eines Textes noch seine Passung zur eigenen Modellidee genügt als Auswahlgrund.

Eine spätere breite JTEI-, Zotero-, Archiv- oder Mailinglisten-Auswertung braucht eine eigene Forschungsfrage. Die derzeit als offen registrierten Sammlungsziele erzwingen keine wahllose Aufnahme ihrer Inhalte. Ob wir diese Grenzen dauerhaft enger ziehen, bleibt eine fachliche Entscheidung.

## Prüfstand und konkrete Befunde

Die aktuelle Statuszählung lautet: 30 Destillate `validated`, 14 `grounded`; 71 Assertions `validated`, 30 `grounded`, sechs `contested`. Kein Artefakt trägt menschliches `verified`.

Der bestehende Cutter erzeugt **523 Belegpaare**: 411 zwischen Quelle und Destillat sowie 112 zwischen Destillat und Assertion. Das sind mehr Beziehungen als Dokumente, weil Dokumente mehrere Aussagen und Assertions mehrere Belege enthalten können. Der [eingefrorene Umfang](scope.json) und die [Abdeckung historischer Reviews](review-coverage.json) machen diese Zählung nachvollziehbar.

| Historischer Nachweis | Paare | Bedeutung |
|---|---:|---|
| Passendes früheres `fully supports` mit gleicher ID und gleichem Prompthash | 327 | 249 Quellenpaare und 78 Assertion-Paare. Keine erneute fachliche Prüfung; Reviewer-Unabhängigkeit ist damit nicht bestätigt. |
| Sonderprompts des Identitätspiloten | 5 | Drei Destillate; durch den eigenen Pilotchecker geprüft. Die damaligen erweiterten Prompts sind vom generischen Cutter verschieden. |
| Noch `grounded`, ohne passenden bestandenen Review | 186 | 152 Quellenpaare und 34 Assertion-Paare. Betroffen sind die 14 noch ungeprüften Destillate und 30 Assertions. |
| Bereits `validated`, passendes Reviewprotokoll nicht gefunden | 5 | Die fünf Aussagen des P6-README-Destillats. Dessen Status ist damit im Repository derzeit nicht hinreichend durch auffindbare Prüfprotokolle belegt. |

Bei der Integration wurden folgende materielle Grenzen bestätigt:

1. **W3C-Kontext:** Das bisherige Zitat setzt erst nach einer Bedingung des Originalsatzes ein. §4.2.4 verlangt die Auswertung von Präfix, exaktem Suchtext und Suffix, bevor verbleibende Mehrfachtreffer gemeinsam behandelt werden. Die bedingte Aussage muss im Destillat, im vollständigen Assertion-Text und in den Kapiteln 06 und 12 nachvollzogen werden. Das ist ein bestätigter Kontext- und Präzisierungsbedarf; dieser Audit setzt noch kein neues hashgebundenes Verdict.
2. **P6-README:** Für den vorhandenen Status `validated` wurden die fünf erforderlichen Reviewprotokolle nicht gefunden. Die Aufnahmeprovenienz ist zusätzlich gegen die Git-Beobachtung nachzuvollziehen. Das README belegt keinen Beschluss über eine P6-Architektur.
3. **Prüfumfang:** Der aktuelle Cutter prüft bei Assertions nur die H1. Der vollständige Statement-Abschnitt und Tatsachenbehauptungen in Terms, Appraisal, Support und Kapitelprosa sind dadurch nicht vollständig erfasst. Auch die fünf Assertions mit mehreren Belegen benötigen eine Prüfung des gemeinsamen Schlusses.
4. **Blindprüfung:** Ein frischer Aufruf in `run_claude` sperrt weder Werkzeuge noch den übrigen Projektbestand. Damit ist die verlangte Abschirmung gegen Produzentenbegründungen nicht technisch garantiert. Dies ist kein Nachweis, dass frühere Reviewer solche Begründungen tatsächlich gelesen haben.
5. **Quellenzugang:** Fehlende lokale Rohtexte begrenzen eine Wiederholung der Zitattreueprüfung. Normalisierte Metadaten und gespeicherte Kurzbelege ersetzen den nötigen Originalkontext nicht. Die drei Literatur-Primärseiten wurden für diesen Audit online gelesen; damit sind die damaligen Rohdateien noch nicht wiederhergestellt oder ihre historischen Hashes bestätigt.

Alle sechs `contested` Assertions besitzen passende frühere Einzelpaar-Urteile. Ein gestütztes Zitat auf jeder Seite löst ihren Konflikt nicht auf. Die Vollprüfung muss Zeitstand, Begriffe und Reichweite beider Positionen vergleichen.

## Meilenstein V1

Der [Meilenstein](../../../knowledge/plan.md) und seine [verbindliche Prüfmethode](../../../knowledge/verification.md) sind angelegt. Sein Ausgangsbestand umfasst alle 44 Destillate und 107 Assertions einschließlich ihrer bisher als geprüft markierten Teile. Die vier Ausgabekapitel werden auf die korrekte Weiterverwendung der Prämissen geprüft. Die Dateien und Ausgangsprompts sind mit Prüfsummen bezeichnet.

Für den Durchgang werden Original- und Kontextprüfung, Destillatprüfung, vollständige Assertion-Prüfung sowie Konflikt- und Kapitelprüfung auf mehrere Reviewer verteilt. Ein zusätzlicher Reviewer kontrolliert Abweichungen und eine vorab bestimmte Stichprobe bestandener Urteile. Die Opus-Vorgabe gilt weiterhin; familiengleiche Fehler müssen als Grenze dokumentiert werden. Menschliche Verifikation bleibt eine gesonderte Abnahme.

**Abgeschlossen sind Bestandsaudit, Quelleneignungsbewertung und Vorbereitung.** Der vollständige neue semantische Durchgang ist offen. Vor seiner Ausführung sind die Abschirmung des Reviewrunners und ergänzende Kontext-/Gesamttextpaare erforderlich. Ein Abschluss setzt vollständige Abdeckung, nachvollziehbare Urteile und behandelte Abweichungen voraus. Ungeklärte Aussagen dürfen keine freigegebenen Tatsachenprämissen tragen. Absolut fehlerfreie Forschung wird damit nicht zugesichert.

## Durchführung und Nachweise

Drei getrennte Opus-Subagents bearbeiteten [Bestand](holdings-brief-v1.md), [Literatureignung](literature-brief-v1.md) und [Verifikationsumfang](verification-brief-v1.md) lesend. [Laufmetadaten](audit-workers.json) halten Modellangabe, erfolgreiche Antworten und Antwortprüfsummen fest. Dies waren Repository-Audits mit Dateizugriff und keine abgeschirmten Urteile über alle 523 Paare.

Der Integrator prüfte wesentliche Mengen, Statuswerte und auffällige Aussagen gegen Dateien und Originalseiten. Dabei wurden unter anderem die 894 Repräsentationen korrekt auf mehrere Familien verteilt, das vorhandene Humboldt-Schema berücksichtigt und die 191 offenen generischen Paarzuordnungen in 186 `grounded`-Paare und fünf unbelegte P6-Statuszuordnungen getrennt. Aus fehlenden Lock-Verweisen wurde keine allgemeine Regel abgeleitet, nach der jedes historische oder aufnahmespezifische Manifest zwingend im Familien-Lock stehen müsse.

Der Integrator hat folgende laufbezogenen Prüfungen am lokalen Stand ausgeführt:

- `tools/review.py emit`: 523 Ausgangspaare ohne Cutterfehler; anschließend alle 151 Dokumenthashes und 523 aktuellen Prompthashes abgeglichen. Die vier Kapitel sind zusätzlich durch Dateihashes bezeichnet.
- `tools/check_wave1_sources.py . --review-only`: acht passende historische Pass-Urteile. Die damaligen Rohdateien fehlen lokal; ihre Zitattreue wurde damit nicht erneut geprüft.
- `tools/check_text_identity_pilot.py`: Aufnahme, neun historische Piloturteile und 38 reproduzierte synthetische Fälle bestanden.
- `tools/validate.py .`: null Fehler und null Warnungen; `tools/inventory.py . --check`: keine veraltete Inventarregion.
- `ruff check .` und `git diff --check`: bestanden.
- `tools/build_docs.py --date 2026-09-11`: Projektseite regeneriert; `tests/test_build_pages_reproduce.py` und `tests/test_knowledge_routes.py`: 13 Tests bestanden.

Diese Prüfungen bestätigen Struktur, Konsistenz und Reproduktion. Die 523 Paare erhalten dadurch kein neues fachliches Pass. Es wurden keine Quellen entfernt, keine Wissensstatus angehoben und kein Commit, Push oder Deployment ausgeführt. Die kanonische Rückschreibung erfolgte in den Repository-Wissensdokumenten; der persönliche Obsidian-Vault blieb unverändert.
