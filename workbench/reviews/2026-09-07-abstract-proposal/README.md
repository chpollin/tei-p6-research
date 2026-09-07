# Modell-Proposal und Konsistenzprüfung

Diese Aufzeichnung dokumentiert eine Implementierungs- und Textprüfung. Sie
ist keine Forschungsquelle, kein Grounding-Ziel und keine unabhängige
Source-Support-Review. Der Nutzer hat die Ausarbeitung und die Modellwahl der
Subagenten ausdrücklich beauftragt. Basis und Rollen stehen im
[Brief](brief.md), SHA-256
`b54862a7eede32802e58d4a6e7d1dc145ca46174891aff03d9b7b96d15a71479`.

GPT-6 Astra prüfte Modellverträge und Implementierung sowie den Entwurf von
Kapitel 02. GPT-5.6 Sol prüfte den vorhandenen Output-Bestand. Der Integrator
schrieb den Text, übernahm die Präzisierungen und wiederholte die folgenden
Gegenproben ohne Dateiveränderung. Fachliche Nutzerabnahme bleibt offen.

## Wiederholte Gegenproben

| Eingabe und Veränderung im Speicher | Beobachtung |
|---|---|
| Im Dossier `experiments/identity_evidence/dossier.json` erhält `selection-passage-szd-work-3` die `version` und den `selector` von `selection-passage-szd-work-4`. Die IDs und Belegbodies bleiben erhalten. Snapshots stammen aus `tools.ingest_identity_evidence.snapshots`. | `validate_profile` und `check_profile_revision` geben `valid: true`. Die Belegstelle hat trotzdem den Katalogeintrag gewechselt. |
| In `experiments/entities_v02/examples/statements-and-revision.json` wird `kind` der ersten Entität zu `other` geändert. | `validate_extension` und `check_claim_revision` akzeptieren die Änderung. |
| Im gleichen Entitätenbeispiel wird das erste vorhandene Concept-Alignment unter Beibehaltung seines vollständigen Records in ein anderes Concept verschoben. | Beide Prüfungen akzeptieren die Änderung des impliziten Claim-Gegenstands. |
| Das gültige 0.1-Beispiel `competing-readings.json` erhält ein Concept `en-proper-noun` mit eigener lokaler Definition. Die Kopie erhält `model_version: 0.2` und die vier leeren Erweiterungscollections. | 0.1 validiert, 0.2 verweigert mit `E_MENTION` am neuen Concept. Universelle additive Kompatibilität ist damit widerlegt. |

Die Proposal und die verantwortlichen Knowledge Documents benennen diese
Grenzen. Die fehlenden Revisionsgarantien sind als offener fachlich-technischer
Punkt in `knowledge/handoff.md` aufgenommen. Die bestehenden Modellregeln
wurden in dieser Ausarbeitung nicht geändert.

Die Textprüfung präzisierte außerdem den ausführbaren Umfang des Reanchorings
auf 0.1, die sechs reservierten Berichtstypen des Quellenprofils, dessen
certainty-Verbot für Berichte und Belege sowie die Teilnehmerrollen einer
Werkzuordnung. Der alte Pilot-Audit bleibt auf seine bisherigen Quellen und
Aussagen begrenzt. Seine neun unveränderten Review-Paare werden weiterhin
gegen ihre gespeicherten Urteile geprüft. Sie verifizieren das ausgebaute
Kapitel nicht.

Die aktuellen technischen Abschlussprüfungen und ihr Geltungsumfang stehen
in `knowledge/state.md`.
