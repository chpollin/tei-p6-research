# Vollprüfung V1

Dieser Prüfauftrag setzt die im [Bestandsaudit](../2026-09-11-data-and-verification/) benannten Nacharbeiten um. Der aktuelle Ausführungsstand steht in [knowledge/state.md](../../../knowledge/state.md). Das [vorab festgelegte Protokoll](protocol.json) definiert die Erstprüfung, die geschichtete Zweitstichprobe und die Behandlung von Abweichungen.

Der [Datenüberblick](data-overview.md) erklärt den vorhandenen Bestand,
seine Verwendung, fehlende Evidenz und die noch erforderlichen fachlichen
Beiträge. Die Quellenaufnahme und zahlreiche Korrekturen sind ausgeführt;
V1 ist noch nicht abgeschlossen.

Der [technische Gesamtlauf](technical-checkpoint.md) enthält 1.917 bestandene
Tests und drei wegen ausstehender Reviews fehlgeschlagene Prüfchecks.
Quellensteuerung, Reproduktionen und formale Kapitelprüfung bestehen.

## Prüfstand vom 11. September 2026

Die aktuelle Emission mit Instrument V1.7 umfasst 837 Einheiten. Nach den
Korrekturen konnten 67 vollständig identische Prüfpakete mit 397 Urteilen
übernommen werden: 351 Quellenbehauptungen, 15 Assertion-Belege,
23 vollständige Destillate und acht vollständige Assertions. Alle übernommenen
Urteile lauten `fully supports`. Für 440 Einheiten steht ein aktuelles Urteil
aus. Alle vorgesehenen Originalkontexte sind vorhanden. Die getrennte
Zweitstichprobe wurde noch nicht ausgeführt.

Das [Zwischensiegel](checkpoint-seal.json) bindet diesen unvollständigen Stand
an Dokumente, Prompts, Instrument und Antwortprüfsummen. Es ist kein
Abschlusssiegel. Eine Änderung an einem Wissensdokument macht auch Prüfungen
seiner abhängigen Dokumente erneut erforderlich. Ein früherer Pass wird nur
bei identischem vollständigem Paket übernommen.

Opus lieferte am 11. September um etwa 16:39 Uhr Ortszeit HTTP 429 mit
Sitzungslimit und angekündigter Rücksetzung um 19 Uhr Europe/Vienna.
Fehlversuche und frühere Abweichungen sind lokal erhalten. Der Abschlussgate
weist die fehlenden Erst- und Zweitsiegel zurück. Auch drei geänderte
Wave-1-Prompts und vier geänderte Textidentitäts-Prompts benötigen eigene
neue Urteile in ihrem bisherigen Format.

## Ausgeführte Nacharbeiten

- Neun frühere Zitationsoriginale und das P6-README wurden anhand ihrer
  gespeicherten Prüfsummen wiederhergestellt. 109 wörtliche Belege aus
  17 Publikationsquellen wurden gegen die lokalen Originale geprüft.
- Sieben Council-Seiten und eine gepinnte P6-Foliendatei ergänzen den
  offiziellen Prozess. Neun Praxisquellen decken drei ODDs, deren
  Verarbeitungskontexte und reale Eingabedateien ab.
- Mehrere Opus-Arbeiter und isolierte Prüfkontexte fanden fehlende
  Bedingungen, verlorene Einschränkungen, unzutreffende Quellenrollen und
  unbelegte Zusätze. Die [Quellenkorrekturen](source-corrections-result.md),
  [weitere Quellenkorrekturen](source-corrections-2-result.md),
  [Assertion-Korrekturen](assertion-corrections-result.md) und
  [Kapitelkorrekturen](chapter-corrections-result.md) dokumentieren die Arbeit.
- 32 Wontfix-Fälle wurden anhand ihrer Beschreibungen und 262 Kommentare
  eingeordnet. Ein Schließungslabel begründet keine Ablehnungsentscheidung.
- Der Brown-Archivmonat Januar 2000 wurde mit allen 19 gelisteten
  Nachrichtenseiten aufgenommen. Ein real beobachteter LISTSERV-Parserfehler
  ist korrigiert; der Monatscheckpoint reproduziert die Metadaten bytegleich.

## Ausführbarer Wiedereinstieg

Im lokalen Rohbereich liegt die aktuelle vollständige Emission unter
`corpus/raw/review-contexts/2026-09-11/primary-final-v17-r3/`; der Quellenkontext
heißt `all-publication-contexts-v17.json`. Der genaue Auftrag für die 440
offenen Einheiten steht in `primary-final-v17-r3-remaining.json`.
`tools.full_review check` prüft vor der Fortsetzung die Aktualität der Eingaben.
Sein negativer Gesamtstatus ist bis zur vollständigen Prüfung zu erwarten.

Nach Freigabe des Anbieterlimits setzt folgender Aufruf ausschließlich
fehlende Pakete fort; er ist noch nicht gestartet:

```powershell
.venv/Scripts/python.exe -m tools.full_review run corpus/raw/review-contexts/2026-09-11/primary-final-v17-r3 --model opus --workers 3 --batch-size 6 --max-batch-chars 120000
```

Abweichungen werden zuerst gegen die Quelle beurteilt und korrigiert. Geänderte
Materialien erfordern eine neue Emission. Erst danach wird mit
`tools.full_review sample` die vorab definierte Zweitstichprobe erzeugt und in
frischen Kontexten ohne Übernahme früherer Urteile geprüft. Die lokalen
Antwortprüfungen müssen vor `primary-seal.json` und `second-seal.json` bestehen.
`tools.current_review` prüft beide Siegel gemeinsam. Das lokale Hilfsskript
`refresh_legacy_r2.py` bereitet die sieben geänderten älteren Prompts separat
auf; nach erfolgreichem Lauf werden die beiden Checker auf die neuen
Prüfverzeichnisse umgestellt. Historische Ergebnisse bleiben erhalten.

Danach folgen Regeneration, vollständiger Abschlussgate, die aus einer echten
Vault-Session auszuführende ACTIVE-WORK-Rückschreibung und die bereits
beauftragte Veröffentlichung des geprüften Stands. Es läuft keine automatische
Wiederaufnahme. Weder Commit noch Push oder Deployment wurden ausgeführt.

Die Prüfung umfasst Quellenbehauptungen mit Originalkontext, vollständige Assertions, Tatsachenbehauptungen in den übrigen Dokumentabschnitten, die drei dokumentierten Konfliktpaare und die Quellenverwendung der vier Kapitel. Neue P6- und Praxisquellen durchlaufen dieselben Prüfungen. Die historische Emission der 523 Belegpaare bleibt erhalten.

`tools/full_review.py` erzeugt und prüft eigene, versionierte Einheiten. Jede Prüfung bindet den tatsächlichen Prompt und die Instrumentdateien mit SHA-256. Arbeitsverzeichnis, gesperrte Werkzeuge, leere MCP-Konfiguration, konkrete Modellantwort und CLI-Version werden protokolliert. Ganze Quellenkontexte und Prompts liegen ausschließlich unter `corpus/raw/review-contexts/2026-09-11/`. Öffentliche Prüfsiegel enthalten Identitäten, Hashes und Urteile; Begründungen aus privaten Kontexten werden durch ihre Prüfsumme referenziert.

Die Aufträge liegen unter [briefs](briefs/). Ihre Arbeiter verändern getrennte Dateibereiche. Der Integrator prüft den tatsächlichen Stand, verknüpft Quellen und Wissensdokumente, behandelt fachliche Befunde und führt den gemeinsamen technischen Abschlusscheck aus. Ein Arbeiterbericht verleiht keinen Prüfstatus.

Ein V1-Abschluss bezeichnet eine dokumentierte Prüfung des ausgewiesenen Bestands. Menschliche Verifikation, fachliche Modellabnahme und eine belastbare Auswahl zwischen Architekturvorschlägen benötigen eigene Urteile. Die globale Vollständigkeit des Forschungskorpus wird damit nicht behauptet.
