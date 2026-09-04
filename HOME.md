# TEI P6 Research Vault

Dieser Vault dient der provenance-complete Analyse von TEI P5 und dem quellengebundenen Entwurf einer möglichen nächsten TEI-Generation. Zweck, Geltungsbereich und Evidenzpflicht stehen in [[knowledge/specification]]. Jede tragende Aussage des späteren Outputs muss über Assertions und Distillates bis zu einer konkreten Quellenstelle, einem überprüften Zitat oder einer reproduzierbaren Berechnung zurückverfolgbar sein.

## Die Provenienzkette

```
00_sources → 10_markdown → 20_distillates → 30_assertions → 40_output
```

`00_sources/` enthält die unveränderten Originale. `10_markdown/` enthält ihre stabil verankerten Markdown-Repräsentationen oder Datenschemata. `20_distillates/` bindet Einzelaussagen an diese Quellenstellen, `30_assertions/` synthetisiert quellengetragene Aussagen, und `40_output/` enthält die fachwissenschaftliche Synthese und Designspezifikation.

## Output lesen

- [[40_output/]] — die Kapitel; Fußnoten führen über Assertions zu den tragenden Quellenstellen.

## Wissen erschließen

- [[30_assertions/MOC-P5 Architecture]]
- [[30_assertions/MOC-Abstract Model]]
- [[30_assertions/MOC-ODD and Customization]]
- [[30_assertions/MOC-Elements and Classes]]
- [[30_assertions/MOC-Text and Document Structures]]
- [[30_assertions/MOC-Annotation and Overlap]]
- [[30_assertions/MOC-Critical Apparatus]]
- [[30_assertions/MOC-Metadata and Entities]]
- [[30_assertions/MOC-History and Governance]]
- [[30_assertions/MOC-Issues and Decisions]]
- [[30_assertions/MOC-Interoperability and Processing]]
- [[30_assertions/MOC-P6 Design]]
- [[glossary/]] — zentrale Fachbegriffe des Projekts.

## Arbeitsweise und Projektstand verstehen

- [[knowledge/index]] — Navigation und Terminologie.
- [[knowledge/state]] — Quelleninventar, Kapitelregister und offene Arbeit.
- [[knowledge/journal]] — Entscheidungen und ihre Begründungen.

## Status lesen

`grounded` bedeutet, dass die Provenienzstruktur angelegt wurde. `validated` setzt bestandene deterministische Prüfungen und ein protokolliertes adversariales Machine Review voraus. `verified` darf erst nach Bestätigung durch den Project Owner oder eine ausdrücklich benannte TEI-Fachperson gesetzt werden; derzeit ist keine Person für diese Rolle bestimmt. `contested` hält einen nicht aufgelösten Quellenkonflikt sichtbar.
