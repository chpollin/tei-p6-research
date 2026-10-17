---
title: State
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: de
created: "2026-09-04"
updated: "2026-10-17"
related: [INDEX, plan, handoff, operations, journal]
---

# State

Das Repository enthält einen ausführbaren Forschungsbestand mit vier quellengebundenen Ausgabekapiteln. Der Produktionskorpus und die menschliche Fachprüfung sind unvollständig. Die aktuelle agentische Vollprüfung V1 einschließlich der vorab bestimmten blinden Zweitstichprobe ist am 17.10.2026 abgeschlossen. Der [Fortsetzungsbericht](../workbench/reviews/2026-10-17-v1-continuation/) beschreibt Quellenkorrekturen, Reviewgrenzen und die gesonderte Klärung des älteren Auszug-Checks. Die veröffentlichte Baseline `v0.1.0` und ihre Grenzen stehen in [[knowledge/releases]]. Der September-Arbeitsstand ist mit `749c7b1` auf `main` gesichert. Die mit `1110961` lokal gesicherte Übergabebaseline vom 17.10.2026 enthält die Folgekorrekturen, aktuellen öffentlichen Reviewsiegel und integrierten Ansichten. Vollständige Reviewkontexte und Originalantworten bleiben außerhalb Git. Es erfolgte keine Veröffentlichung.

## Current checkpoint

| Bereich | Aktueller Stand | Evidenz und Grenze |
|---|---|---|
| Quellenreferenz | 903 unveränderliche Repräsentationen, davon 888 Quellen der englischen P5-Guidelines 4.12.0 und neun neue Praxisquellen | [Aufnahme und Abdeckung](../corpus/projections/guidelines-4.12.0.md). Alle 24 Hauptkapitel und 846 Spezifikationen sind aufgenommen. XML-Includes und Grafikverweise sind begrenzt abgeglichen; zwei erwartete HTML-Ziele bleiben Ausnahmen. Aufnahme ist keine vollständige Destillation. |
| Wissensproduktion | 61 Destillate, 120 Assertions und vier Kapitel | Der [Ausgangsaudit](../workbench/reviews/2026-09-11-data-and-verification/) hält die früheren 44 Destillate und 107 Assertions fest. Hinzu kommen acht P6- und neun Praxisdestillate sowie 13 Assertions. Geänderte Aussagen erhalten bis zum Abschluss ihrer erneuten Prüfung keine maschinelle Freigabe. Das [generierte Inventar](../corpus/projections/source-inventory.md) führt die konkreten Pfade. Kein Artefakt trägt menschlich vergebenes `verified`. |
| Vollprüfung V1 | Aktueller Erststand und vorab festgelegte blinde Zweitstichprobe vollständig geprüft | [Erstsiegel](../workbench/reviews/2026-09-11-v1/primary-seal.json) und [Zweitsiegel](../workbench/reviews/2026-09-11-v1/second-seal.json) binden 836 aktuelle Erstprüfungen und die separat ausgeführten 89 Stichprobeneinheiten ohne offene Abweichung oder Kontextlücke. Lokal liegen die Pakete unter `corpus/raw/review-contexts/2026-10-17/primary-v17-r11/` und `second-v17-r2/`. Eine redundante Grounding-Beziehung entfiel, Quellen und Artefakte blieben erhalten. Die Fortsetzung nutzte den nachgewiesenen Reviewer `claude-opus-5-5`; historische unveränderte Pakete behalten ihre frühere Modellkennung. Die drei großen begrenzten Kontexte, fehlende Unabhängigkeit der Modellfamilie und menschliche Verifikation bleiben ausdrücklich getrennt. |
| Text- und Dokumentstrukturen | Aktuelle Destillate und Assertions in V1 geprüft; menschliche Fachprüfung offen | Die aktuellen Artefakte gehören zum vollständigen V1-Erststand. Die älteren Quellen- und Assertionspaare in [der Prüfablage](../workbench/reviews/2026-09-07-text-structures-run1/) bleiben historische Vorbereitungen. Der dortige Kapitelentwurf liegt weiterhin außerhalb von `40_output/` und erhält durch V1 keine übertragene Abnahme. |
| Modell 0.1 und 0.2 | Ausführbare, begrenzte Verträge; menschliche Abnahme offen | [[knowledge/text-model]] und [[knowledge/text-model-bindings]]. 0.1: JSON/XML/YAML-Rundläufe. 0.2: JSON und gerichteter RDF-Export. Allgemeine P5-Migration und 0.2-Rundläufe über alle Bindungen sind offen. |
| Design, Ontologie und HSA | Vorschlagsdokumente, dokumentarische Ontologie und separat gebundener HSA-Einzelfall vorhanden | [[knowledge/model-design]], [[knowledge/model-examples]], [[knowledge/ontology]], [[knowledge/hsa-profile]]. Illustrative Syntaxansichten erweitern den produktiven 0.1/0.2-Vertrag nicht. Der HSA-Fall belegt keine allgemeine Editionskonversion. |
| Identität und Belege | Quellenprofil auf 0.2 mit zwei XML-Snapshots und einem reproduzierbaren Katalogdossier | [[knowledge/identity-evidence]]. Die aktuellen Destillate und Assertions sind in V1 geprüft und behalten ihren ausgewiesenen Status. Menschliche Domänenabnahme, Unabhängigkeit der Modellfamilie und vollständige Editionsmigration bleiben offen. |
| Revisionsschutz | Die drei bekannten Gegenfälle werden zurückgewiesen; gezielte Prüfungen bestanden | Entity-kind, Alignment-Träger und referenzierte Selektionen sind durch [[knowledge/text-model]] 14.4 geschützt. Nach Regeneration bestanden 209 gezielte Modell- und Reproduktionstests. Labels und nicht reservierte Konzeptdefinitionen bleiben ausdrücklich veränderlich. |
| Vergleichsgrundlage | Synthetische Piloten und drei Fragmente eines Humboldt-Tagebuchs ausgeführt | [[knowledge/experiments]]. Der eingefrorene Kandidat verweigert den Seiten-/Foliierungs-Gegenfall; auch die Baseline verfehlt dessen gefordertes Prosaergebnis. Repräsentative Editions-, Korpus- und Katalogfälle sowie Domänenprüfung fehlen. |
| Navigation | Lokale Suche und deklarierte Quellenauswahl ausführbar; Websuche nach Relevanz und Prüfstatus filterbar | Exakte Quellenkennungen, Versionsgrenzen, Gegenpositionen und leere Treffer sind geprüft. Kuratierte Themen bleiben von Vorschlägen getrennt. Der Atlas bildet direkte Deklarationen ab; 57 benannte Datentypreferenzen und effektive ODD-Vererbung bleiben offen. Navigation begründet keine Forschungsbehauptung. |
| Technische Prüfung | V1-Reviews, beide Legacy-Checks und technischer Gesamtlauf bestanden | Die beiden Standardchecker zeigen auf die tatsächlich erneuerten Legacy-Records. Der Wave-1-Check besteht mit erneut geprüftem kurzen Originalkontext zur Publikationsaussage. Das frühere Auszug-Urteil bleibt erhalten. Strukturprüfung und Linter bestehen; der Gesamtlauf und die bestandene gezielte Nachprüfung sind im [Fortsetzungsbericht](../workbench/reviews/2026-10-17-v1-continuation/) protokolliert. Die vorhandenen HTML-Änderungen reproduzieren den bisherigen Quellenstand. Die Quellenkorrekturen sind durch die bestehenden Generatoren integriert, alle Seitenreproduktionen und der technische Gesamtlauf bestehen. Der [September-Prüfbericht](../workbench/reviews/2026-09-11-v1/technical-checkpoint.md) bleibt ein historischer Stand. |

## Quellenbereiche und offene Grenzen

| Bereich | Status | Was vorhanden ist und was fehlt |
|---|---|---|
| P5 4.12.0 | `partial` | Releasecommit, Git-Baum, Release-ZIP und rekonstruierbare XML-Referenz vorhanden; veröffentlichte HTML-Grenze noch gegen das ZIP abzugleichen. |
| Organisationszensus und öffentliche TEIC-Git-Repositories | `observable-complete` | Zwei Familien: 41 beim Organisationszensus sichtbare Repositories und ihre Git-Beobachtungen mit vollen HEAD-Commits inventarisiert. Dies beschreibt den damaligen Zensus. Unter `corpus/raw/git/` liegt heute nur der TEIC/TEI-Spiegel; die anderen 40 fehlen in diesem Checkout. |
| GitHub-Arbeitspakete | `partial` | REST- und GraphQL-Läufe vom 2026-09-06 vorhanden. Die spätere Relationsstufe erfasst alle 2.931 Work Items ohne eigenen Gap. Der ältere REST-Lauf enthält weiterhin seinen damaligen Relations-Gap. Eine übergreifende Abgleichung muss diese historischen Aussagen erhalten; ein neuer REST-Abruf ist dafür nicht automatisch erforderlich. |
| TEI-L | `partial` | Penn State Dezember 2025 bis September 2026: 267 Nachrichten. Brown/Wayback: 432 Monate gemessen, 368 mit Capture, 64 ohne. Januar 2000 ist mit allen 19 gelisteten Nachrichtenseiten aufgenommen; die Wiederaufnahme reproduziert die Metadaten bytegleich. Ein produktiv gefundener Parserfehler bei alten Abstandszellen ist korrigiert und durch 52 Tests abgesichert. Die übrigen 367 gemessen erfassten Monate bleiben offen. Nachrichtentexte und Absenderidentität bleiben im lokalen Rohbereich. |
| Website, Council und Board | `partial` | Drei Familien: Website-Gitbestand sowie 206 Council-Seiten und 225 Board-Ziele beobachtet; Snapshot-Abgrenzung, historische Linklücken und externe Dokumente offen. |
| Council-Arbeitsdokumente | `observable-complete` | Git-Beobachtung mit 16 Baumeinträgen und 322 Commits dokumentiert; der lokale Spiegel fehlt. Dies ist keine vollständige Sammlung aller Council-Protokolle. |
| P5-Releasehistorie | `partial` | 50 Versionsverzeichnisse und 53 Indexantworten erfasst. Einzelne historische Releases sind noch nicht mit eigenen Versions-Locks aufgenommen. |
| Historisches TEI-Archiv | `partial` | 394 Index-/Seitenantworten aufgenommen; 363 verlinkte Nicht-HTML-Artefakte und 424 Links an der Abruf-Tiefengrenze bleiben abzugleichen. |
| SourceForge | `partial` | Die Tracker-API-Grenze ist `observable-complete`: 1.349 Tickets und 8.880 Diskussionseinträge abgeglichen. Der r4-Lauf ist im Familien-Lock ergänzt; seine Wiederverwendung früherer Ticketdaten bleibt ausgewiesen. Release-Dateien und alte Versionsverwaltung bleiben offen; frühere Rohantworten fehlen im Checkout. |
| Stylesheets und Tooling | `partial` | Zwei Familien mit Git-Inventaren für Stylesheets und sechs Werkzeuge. Lokale Spiegel fehlen; die Locks halten offene Work-Item-Zugänge fest. Die jetzige Erreichbarkeit wurde hier nicht neu geprüft. |
| Community/SIG | `partial` | Drei Indexseiten mit 101 Links erfasst. Arbeitsgruppen und Jahrestagungen sind damit nicht inhaltlich aufgenommen; TEI-L hat eine eigene Grenze. |
| Reale Anpassungen und Praxisfälle | `partial` | Zusätzlich zu Humboldt, HSA und SZD sind drei reale ODDs aus DraCor, EpiDoc und CMIF, drei Verarbeitungskontexte und drei reale Eingabedateien aufgenommen. Das [Auswahlprotokoll](../workbench/selections/2026-09-11-odd-practice.md) begründet die Kontraste. 17 weitere Kontextbeobachtungen sind im Aufnahmemanifest gebucht. ODD-Kompilation, effektive Schema-/Schematronprüfung, ein externer Katalog-ODD-Fall und fachliche Repräsentativität bleiben offen. |
| Literatur | `partial` | Vier Kandidaten: zwei Aufsätze und ein technischer Vergleichsstandard zitationsbasiert aufgenommen, eine OHCO-Autorfassung wegen HTTP 403 nicht verfügbar. Breitere Literaturseeds bleiben offen. Der [Eignungsaudit](../workbench/reviews/2026-09-11-data-and-verification/) empfiehlt gezielte Nutzung; eine breite Erweiterung ist fachlich noch nicht begründet. |
| Offizieller P6-Prozess | `partial` | Sieben ausgewählte Council-Seiten und die gepinnte Foliendatei einer Council-Session sind mit 42 Zitaten und sechs Assertions aufgenommen. Das README-Original wurde hashgleich wiederhergestellt. [Auswahl und Grenzen](../workbench/selections/2026-09-11-p6-process.md) bleiben explizit: weitere Council-Seiten, Vancouver-Ergebnisse und eine öffentliche Sandbox-Aufnahme fehlen. Der erneute HTTP-404-Befund beweist weder Nichtexistenz noch Privatstatus. Aussagen über Diskussion, Beschluss und spätere Umsetzung bleiben getrennt. |

Die konkreten Identitäten, Beobachtungsdaten, Prüfsummen und Lücken stehen in `sources/locks/` und den abgeschlossenen Manifesten. Die Tabelle behauptet keinen neuen Netzabruf.

## Source inventory

[[corpus/projections/source-inventory|Vollständiges generiertes Quelleninventar]]

`python tools/inventory.py . --write` aktualisiert das Inventar sowie die erzeugten Navigationsregionen. `--check` vergleicht sie mit den vorhandenen Dateien. Verarbeitungsstand und wissenschaftlicher Prüfstatus bleiben getrennte Felder.

## Chapter register

The register lists existing chapters and reserved topic routes. Writing status
mirrors each existing chapter's frontmatter. Planned topic routes become
standalone chapters when their evidence and reader-facing function justify
the split, under [[knowledge/p6-architecture]].

| Chapter | File | Status | Notes |
|---|---|---|---|
| P5 Architecture | `40_output/01-p5-architecture.md` | planned | Scope topic: P5 Architecture. |
| Abstract Model | `40_output/02-abstract-model.md` | grounded | Standalone definition and rationale for 0.1, entity extension 0.2 and the optional source-attribution profile, with explicitly proposed extensions for edition, corpus and catalogue tasks. Nine source premises and twenty-five posits. Documentary hierarchy, proposition/stance separation and critical GPT-6 review integrated; current V1 chapter review passes, while human acceptance remains open. |
| ODD and Customization | `40_output/03-odd-and-customization.md` | planned | Scope topic: ODD and Customization. |
| Elements and Classes | `40_output/04-elements-and-classes.md` | planned | Scope topic: Elements and Classes. |
| Text and Document Structures | `40_output/05-text-and-document-structures.md` | planned | Scope topic: Text and Document Structures. |
| Annotation and Overlap | `40_output/06-annotation-and-overlap.md` | grounded | First synthesis: five grounded premises and four explicit proposed tests; source-support review and owner review remain distinct. |
| Critical Apparatus | `40_output/07-critical-apparatus.md` | planned | Scope topic: Critical Apparatus. |
| Metadata and Entities | `40_output/08-metadata-and-entities.md` | grounded | Rewritten after the second topic run on sixty-six assertions over twenty-one entity sources, three contested pairs cited on both sides; eleven explicit posits connect the findings to the record kinds of the claim pattern; human verification and encoded practice beyond the release's test document remain open. |
| History and Governance | `40_output/09-history-and-governance.md` | planned | Scope topic: History and Governance. |
| Issues and Decisions | `40_output/10-issues-and-decisions.md` | planned | Scope topic: Issues and Decisions. |
| Interoperability and Processing | `40_output/11-interoperability-and-processing.md` | planned | Scope topic: Interoperability and Processing. |
| P6 Design | `40_output/12-p6-design.md` | grounded | Architecture argument with nine source premises, thirteen posits and comparisons retaining their 0.1 scope. Chapter 02 supplies the broader model definition. Architecture and adoption verdicts remain open. |

## Open work

- Den technisch geprüften integrierten lokalen Stand fachlich beurteilen. Die menschliche Verifikation bleibt offen. Projektcommits unterliegen der spezifischen Regel in AGENTS.md, Push und Veröffentlichung sind nicht beauftragt.
- Die aus der abgeschlossenen [Einzelprüfung der 32 Wontfix-Fälle](../workbench/selections/2026-09-11-wontfix-context.md) empfohlenen Fälle 542, 1485 und 2247 bei passenden Themenläufen gesondert aufnehmen. Die Auswahlsichtung von 32 Beschreibungen und 262 Kommentaren ist abgeschlossen; sie verleiht den drei Kandidaten keinen Belegstatus.
- Die fachliche und menschliche Prüfung der Textstruktur- und Identitäts-/Beleg-Assertions bleibt offen. Die ausgeführte V1-Prüfung mit derselben Reviewer-Modellfamilie ersetzt sie nicht.
- Die offenen Entitätenfragen aus [[30_assertions/MOC-Metadata and Entities]] bearbeiten: Vererbung der Klassenbemerkungen, Träger globaler Verantwortungsattribute, Koexistenz von `key` und `ref` sowie die dort begründet vertagten Quellen.
- Den erfolgreichen Brown-Monatsabruf auf weitere deklarierte Monate ausweiten. Januar 2000 und die Checkpoint-Wiederaufnahme sind abgeschlossen; 367 weitere Monate mit gemessenen Captures und 64 ohne Capture bleiben getrennte Lücken. Eine Anfrage an das Konsortium setzt einen ausdrücklichen Versandauftrag voraus.
- Quellenbereiche anhand ihrer vorhandenen Läufe abgleichen: GitHub-Stufen, HTML- und Website-Grenzen, Archivartefakte, SourceForge-Nebenschnittstellen und Literaturseeds.
- Auswahl und Umfang der menschlichen Stichprobe bestimmen. Die Entitätenläufe umfassen 21 Destillate und 66 Assertions; die drei umstrittenen Paare benötigen beide Positionen. Der Projekteigentümer ist nach [[knowledge/governance]] bereits zur Verifikation berechtigt.
- Repräsentative Editions-, Korpus- und Katalogfälle für die Vergleichsaufgaben in [[knowledge/plan]] auswählen und fachlich begründen.
- Modellabnahmepunkte aus [[knowledge/text-model]] und [[knowledge/experiments]] sowie Architekturkriterien aus [[knowledge/p6-evaluation]] fachlich entscheiden. Die vorliegenden Tests tragen keine bevorzugte Architektur oder allgemeine P5-Migration.
