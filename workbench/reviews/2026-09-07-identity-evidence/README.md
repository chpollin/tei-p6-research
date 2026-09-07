# Prüfvorbereitung: Identität und Quellenbezug

Die Auswahl umfasst zwei Quellen, neun Destillataussagen und sechs Assertions.
Die Quelldokumente und ihre ausgewählten Ausschnitte stehen unveränderlich in
den zugehörigen Repräsentationen. Die Paar-Dateien werden mit `tools/review.py
emit` aus dem tatsächlichen Stand erzeugt und enthalten dessen unveränderte
Prüfprompts. Es entstehen neun Quellenpaare und neun Assertion-Anker-Paare.

Bei den drei Vergleichen über mehrere Destillataussagen schneidet das
allgemeine Werkzeug ein Paar pro Anker. Ein einzelner Anker trägt jeweils
nur seinen Anteil am Vergleich. Die spätere Prüfung muss zusätzlich den
gemeinsamen Schluss aus allen angegebenen Prämissen beurteilen; ein
isoliertes Teilpaar darf dafür kein Vollunterstützungsurteil erhalten.
Diese Grenze der vorhandenen Paarzerlegung bleibt ausdrücklich offen.

Eine unabhängige Quellenprüfung wurde in dieser Ausarbeitung nicht ausgeführt.
Es liegen keine Verdicts vor. Die Artefakte behalten `grounded`; die formale
Validierung verleiht ihnen keinen höheren Forschungsstatus. Erzeugung der
Prüfpaare, technische Quellenprüfung und fachliche Quellenunterstützung sind
separate Vorgänge.

Autor und Implementierer arbeiten im selben GPT-6-Kontext. Die echten Beispiele
waren vor der Implementierung bekannt. Die vier synthetischen Identitätsfälle
und die synthetische Zweitbewertung sind als solche benannt. Sie ergänzen keine
historischen Tatsachen über die ausgewählten Katalogobjekte oder den Brief.
