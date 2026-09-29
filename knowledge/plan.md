---
title: Plan
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: de
created: "2026-09-06"
updated: "2026-09-11"
related: [INDEX, project, specification, state, handoff, journal, testing, verification, experiments, p6-evaluation]
---

# Plan

Das Ziel ist ein unabhängig begründetes P6-Proposal: Jede Tatsachenprämisse muss über geprüfte Assertions zu einer geeigneten Quelle führen. Modelloptionen werden an denselben Aufgaben, Gegenfällen und Migrationsanforderungen verglichen. Die verbindlichen Erfolgskriterien stehen in [[knowledge/specification]], der aktuelle Bestand und Prüfstand in [[knowledge/state]].

## Arbeitsziele

| Ziel | Prüffähiges Ergebnis | Einstieg |
|---|---|---|
| Nachvollziehbares Repository | Jede Regel hat einen kanonischen Ort. Status, historische Entscheidungen, Quelleninventar und ausführbare Verfahren bleiben unterscheidbar. | [[knowledge/INDEX]], [[knowledge/architecture]] |
| Geeignete Quellen pro Frage | Deklarierte Suche über benannte Snapshots mit Treffern, Gegenbelegen, Auswahlbegründungen und Lücken; vorhandene Referenzquellen werden wiederverwendet. | [[knowledge/operations]] § Select, [[knowledge/data]] |
| Zuverlässiger Agentenzugriff | Suche liefert überprüfbare Pfade und Passagen mit Schicht, Prüfstatus, Herkunft und Versionsgrenze. Ein fehlender Treffer bleibt eine offene Frage. | [[knowledge/operations]] § Query |
| Quellennahe Forschung | Themenläufe durchlaufen Aufnahme, Einzelquellendestillation, unabhängige Prüfung, Assertions und Kapitel. Problembehauptungen erhalten Gegenbelegsuche. | [[knowledge/operations]], [[knowledge/verification]] |
| Explizite Modellgrenzen | Ausführbare Verträge, vorgeschlagene Erweiterungen und illustrative Beispiele sind eindeutig getrennt. Revisionen bewahren die Bedeutung bestehender Claims. | [[knowledge/text-model]], [[knowledge/model-design]], [[knowledge/experiments]] |
| Vergleichbare Architekturentscheidung | P5-Reparatur, kompatible Weiterentwicklung, Ersatzarchitektur und Vertagung werden an denselben repräsentativen Aufgaben mit Erhaltung, Verlusten und Folgekosten verglichen. | [[knowledge/p6-evaluation]], [[knowledge/p6-architecture]] |
| Reproduzierbare Veröffentlichung | Quellensteuerung, Code, Modelle und erzeugte Seiten bestehen den gemeinsamen Abschlusscheck. Fachliche Abnahme wird separat dokumentiert. | [[knowledge/testing]], [[knowledge/governance]] |

## Abhängigkeiten der Forschung

Designhypothesen dürfen vor der vollständigen Evidenzprüfung ausgearbeitet werden. Eine bevorzugte Architektur setzt eine belastbare P5-Ausgangsbasis, geprüfte Problembefunde, einen Vergleich der Alternativen und Migrationsbefunde voraus. Ein bestandener synthetischer Modelltest erfüllt keine dieser fachlichen Bedingungen allein.

Die direkte Deklarationsnavigation der P5-Spezifikationen wird erst dann zu einer formalen P5-Modellbasis, wenn Vererbung, effektive ODD-Regeln, erzeugte Schemas und ihre Versionsunterschiede explizit verarbeitet und gegen Quellen geprüft werden. Offizielle Diskussion, Governance-Entscheidung, Implementierung und Releasewirkung erhalten getrennte Belege.

## Meilenstein V1: Vollprüfung des bestehenden Wissensstands

Der Nutzer beauftragt eine vollständige Prüfung der vorhandenen Destillate und Claims mit mehreren Subagents. Der Meilenstein umfasst auch bereits `validated` und `contested` markierte Artefakte. Der eingefrorene Umfang und die vorläufigen Befunde stehen in [[knowledge/state]] und im [Prüflauf](../workbench/reviews/2026-09-11-data-and-verification/). Die verbindliche Prüfmethode steht in [[knowledge/verification]] unter Vollprüfung.

Das Ergebnis besteht aus einer lückenlosen Zuordnung jedes Dokuments und jeder geprüften Aussage zu Quellenprüfung, Urteil und gegebenenfalls Nacharbeit. Es umfasst die Quellenkontexte, den vollständigen Wortlaut der Assertions, gemeinsame Schlüsse aus mehreren Belegen, die umstrittenen Paare und die Weiterverwendung in den Ausgabekapiteln. Die vorhandenen Prüfpaare bilden den Ausgangsbestand; zusätzliche Tatsachenbehauptungen in Terms, Appraisal und Support werden ausdrücklich erfasst.

Der Meilenstein ist bestanden, wenn alle Teile des eingefrorenen Umfangs geprüft sind, sämtliche Abweichungen behoben oder als begründete offene Grenzen sichtbar sind und kein unbelegter Schluss als freigegebene Tatsachenprämisse verwendet wird. Jede geänderte Aussage wird neu geprüft. Alte Freigaben zählen als Vergleichsmaterial und ersetzen keinen Durchgang der Vollprüfung. Familiengleiche Agentenurteile und fehlende Originale bleiben als Einschränkungen ausgewiesen. Menschliches `verified` und eine fachliche Modellabnahme erfordern ihre eigenen Urteile.

Eine absolute Fehlerfreiheit wird durch diesen Meilenstein nicht behauptet. Er liefert eine vollständig dokumentierte Prüfung eines benannten Stands und macht verbleibende Unsicherheit prüfbar.

## Research packages

The following bounded research packages define the remaining substantive work. Each names, before delegation,
the base commit, exclusive write paths, read-only inputs, required checks and
gaps to report under the work-package shape in [[knowledge/governance]].

- **A. Text identity requirements.** A bounded set of text-theoretical,
  annotation-model and editorial-practice sources is admitted and distilled
  separately, synthesized only through assertions, and turned into a
  requirement set that distinguishes source findings from project choices,
  with an adverse example for each requirement. Acceptance requires at least
  two conceptual alternatives facing the same independently reviewed
  observations. The executed text identity pilot compared two selectors
  inside one object model, which the acceptance criterion excludes, so the
  package stays open.
- **B. Real application cases.** Bounded case packages from edition, corpus
  and catalogue contexts cover hierarchy, overlap, and customization or
  contextual interpretation, with selection unit, inclusion and exclusion
  rules, source versions, rights, authority, ODD and tool context and known
  sampling bias recorded, required observations stated before encoding, and
  an adverse case reserved for testing after the candidates are defined.
  Acceptance requires reproduction from declared inputs, independent domain
  review of the expected distinctions and explicit coverage gaps. The
  executed editorial case study covers three fragments of one edition, so the
  package stays open.
- **C. One comparative workflow decision.** Annotation review after a text
  edit is the first decision-sized task. Repair within P5 tooling, compatible
  evolution, an alternative abstract model, and retaining or deferring the
  current behavior are compared with the editorial task and expected
  observations held fixed, with participant roles, procedure, baseline and
  acceptance criteria specified before correctness, effort, errors and
  interventions are measured, and with migration reported on separate axes
  for coverage, preservation, lexical changes, dependencies and
  reversibility. Acceptance requires technical and domain reviews of the same
  record, with costs and unknowns alongside benefits and the evidence named
  that would reverse the recommendation. No bounded execution of this package
  has occurred.

## Fachliche Entscheidungen

- Für die Modellverträge und die einzelnen Abnahmepunkte in [[knowledge/experiments]] jeweils annehmen, überarbeiten oder vertagen.
- Editionen, Korpora und Kataloge für Paket B sowie deren Auswahl- und Ausschlusskriterien bestimmen.
- Schichtung und Umfang der menschlichen Verifikationsstichprobe festlegen. Die Verifikationsrolle liegt gemäß [[knowledge/governance]] beim Projekteigentümer oder einer ausdrücklich bezeichneten TEI-Fachperson; `verified` folgt erst deren durchgeführter Prüfung.
- Architekturkriterien anhand der Vergleichsbefunde gewichten und die Empfehlung einschließlich ihrer offenen Grenzen festhalten.
- Fachliche Empfehlungen nach ihrem tatsächlichen Prüf- und Abnahmestand beurteilen. Die Veröffentlichung des in dieser Sitzung geprüften Repository-Stands ist durch den erneuten Umsetzungsauftrag autorisiert; der technische Abschlusscheck bleibt Voraussetzung.

Die Entscheidungen werden mit ihrer Begründung in [[knowledge/journal]] festgehalten. Bereits ausgeführte Abrufe benötigen keine erneute Autorisierung.

## Topic runs

Die ausführbare Auswahlprozedur steht ausschließlich in [[knowledge/operations]] unter Select. Der [historische Themenkontext](../workbench/selections/2026-09-06-topic-run-context.md) erhält die ursprünglichen Fragen und Begründungen der beiden Themenläufe. Ihre unveränderten Auswahlrecords liegen in `workbench/selections/`; die aktuellen Lücken stehen in den Themenkarten und [[knowledge/state]].

## Definition of completion

Abgeschlossen ist das Forschungsziel, wenn die deklarierten Quellenbereiche abgearbeitet oder mit begründeten Lücken dokumentiert sind, zentrale P5-Aussagen quellenprüfbar bleiben, die formale P5-Basis reproduzierbar ist und die Alternativen repräsentative sowie ungünstige Fälle bestehen. Migrationsverluste, Eingriffe und Werkzeugfolgen müssen benannt sein. Die Empfehlung benötigt deterministische Validierung, adversariale fachliche Prüfung und die bezeichnete menschliche Verifikation.
