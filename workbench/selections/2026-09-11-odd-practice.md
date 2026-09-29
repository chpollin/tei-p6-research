# Auswahlprotokoll: ODD- und Verarbeitungspraxis, Kontraststichprobe V1

Dieses Protokoll hält die Auswahl vom 2026-09-11 fest. Es wurde geschrieben,
bevor die Quellen aufgenommen und destilliert wurden. Es ist ein Protokoll und
eine Navigationshilfe, keine Quelle und kein Grounding-Ziel. Die Aufnahme selbst
dokumentiert `sources/manifests/2026-09-11-practice-v1-admission.yaml`.

## Anlass und Lücke

Der Lock `sources/locks/real-world-customizations.yaml` (Stand 2026-09-07)
enthält für die Familie `tei-real-world-customizations` zwei Stichproben. Die
erste sind drei Fragmente eines Humboldt-Tagebuchs mit dem generierten
Projekt-RNG; eine effektive ODD wurde dort nicht ausgewertet. Die zweite sind zwei
Katalog- und Brief-XML-Quellen der Identitätsstudie. Keine Stichprobe verbindet
eine tatsächliche externe ODD mit ihrem dokumentierten Verarbeitungspfad und
einem realen Eingabedokument. Das Familienprotokoll bleibt offen
(`sampling-protocol-not-yet-approved`); dieser Lauf schließt die Familie nicht.

## Fragen, vor der Detailauswertung geschlossen

| ID | Art | Frage |
|---|---|---|
| P1 | Abdeckung | Mit welchem Mechanismus wählt die ODD P5-Module und -Elemente aus (`moduleRef` mit `include` oder `except`, Löschung)? |
| P2 | Abdeckung | Welche Änderungen erklärt die ODD tatsächlich (`elementSpec`/`classSpec` mit `mode`, geschlossene Wertlisten, Inhaltsmodelle, Datentypen)? |
| P3 | Abdeckung | Wo stehen Zusatzbedingungen: eingebettetes Schematron in der ODD, separate Schematron-Datei oder keine? |
| P4 | Abdeckung | Gegen welche TEI-Quelle wird die ODD kompiliert (`schemaSpec/@source` oder nicht angegeben)? |
| P5 | Abdeckung | Welcher dokumentierte oder konfigurierte Prozessorpfad erzeugt Schemata, und welcher prüft Eingabedokumente? |
| P6 | Abdeckung | Wie verknüpft ein reales Eingabedokument sich mit einem Schema (Verarbeitungsanweisung, Version)? |

Der Lauf formuliert keine Problembehauptung über einen P5-Mangel. Er prüft
weder Migrations- noch Nutzbarkeitserfolg und misst keine Verbreitung.

## Kriterien

Einschluss eines Falls:

1. Offizielles, öffentliches Projekt-Repository; Datei an einem vollständigen
   Commit-SHA gepinnt.
2. Die als ODD bezeichnete Datei ist ein TEI-Dokument mit genau einem
   `schemaSpec`. Die Erkundung sah das nur per Textsuche; das Aufnahmewerkzeug
   prüft es durch XML-Parsing, bevor die Datei als ODD geführt wird.
3. Ein dokumentierter oder konfigurierter Verarbeitungspfad im Projekt-Repository
   oder in einem ausdrücklich verbundenen Dienst.
4. Ein reales, vom Projekt oder vom verarbeitenden Dienst veröffentlichtes
   Eingabedokument, kein Tutorial- oder Vorlagenbeispiel.
5. Eine Lizenzdatei oder eine Lizenzangabe im Dokument selbst erlaubt die
   Weitergabe. Dateien ohne geklärte Rechte bleiben lokale Kontextbeobachtung.

Kontrastdimensionen: Dokumentdomäne, Anpassungsstrategie, Ort der
Zusatzbedingungen, Prozessorpfad und Schemaverknüpfung der Eingabe. Als
Fallobergrenze galten drei Projekte mit je drei aufgenommenen Dateien, also neun
Quellen innerhalb des Budgets von zwölf.

## Kandidaten und Dispositionen

Erkundung am 2026-09-11 über die GitHub-API (Repository-Metadaten, Bäume,
Dateiinhalte an festen Commits) und die GitHub-Codesuche nach
`cmi-customization.rng`.

| Kandidat | Repository und Commit | Disposition | Grund |
|---|---|---|---|
| DraCor: Schema-ODD und Build | `dracor-org/dracor-schema` @ `c2f9e8140bf413cb3bce44abc818d563ddc92d88` (5 Commits nach Release 1.6.0 = `01158c7788d9b5fdbec4d224e5d6bbf2ecf165c4`) | aufnehmen: `dracor.odd`, `build` | Dramenkorpus; `dracor.odd` mit `schemaSpec`; Build über das TEI-Stylesheets-Submodul `81408afc9a25c9170c49adadb0df508ead8ba959`; Repository-Lizenz CC BY 4.0 |
| DraCor: GerDraCor-Stück | `dracor-org/gerdracor` @ `43fe19012bae4784689ce7ad5855dfdd643364e5` | aufnehmen: `tei/leisewitz-die-pfandung.xml` | kleinste Datei unter 776 Stücken; Korpus laut README und Dateikopf CC0 |
| EpiDoc: Schema-ODD und Schema-README | `EpiDoc/Source` @ `e5b68eb8627ac1bc55a4f9f2bec94d8276ff74b3` (28 Commits nach Tag v9.8) | aufnehmen: `schema/tei-epidoc.xml`, `schema/README.txt` | Epigraphik; ODD im Schemaordner; README beschreibt den Erzeugungs- und Einbindungspfad; `schema/LICENSE.txt` GPL |
| EpiDoc: I.Sicily-Inschrift | `ISicily/ISicily` @ `262784ad8b4d4ee5a203abc0a772ae3eea289997` | aufnehmen: `inscriptions/ISic000156.xml` | realer EpiDoc-Korpus; Repository-Lizenz und Dateilizenz CC BY 4.0; einzige Datei mit `revisionDesc/@status="edited"` unter den ersten 40 Baumeinträgen zwischen 11.000 und 14.500 Bytes |
| CMIF: ODD | `TEI-Correspondence-SIG/CMIF` @ `d171133e2ca7a0b987ba0564577ec79077b8d908` (= Tag v1.1.0) | aufnehmen: `odd/cmi-customization.odd` | Austauschformat für Briefmetadaten; kleine ODD mit `schemaSpec`; Doppellizenz CC BY 4.0 und BSD-2-Clause |
| CMIF: Prüfdienst von correspSearch | `correspSearch/csAPI` @ `566b2d29233e3be332dc749266558cb7383cd31d` | aufnehmen: `api/v2.0/services/check/index.xql` | verbraucherseitiger Prüfpfad des Dienstes, der CMIF laut README verarbeitet; LGPL-3.0 |
| CMIF: reale Datei aus dem correspSearch-Speicher | `correspSearch/csStorage` @ `9a7ebe3b68bb464be64d6e08fe1ed8672f90c00d` | aufnehmen: `freieisen-stoeber.xml` | reale veröffentlichte CMIF-Datei mit CC-BY-4.0-Lizenzangabe im Dokument; das Repository hat keine Lizenzdatei |
| edition humboldt digital | `telota/edition-humboldt-digital` @ `f128f89b9dc101254cd311b096f7569fbc1e001e` | nicht als ODD-Fall | Wurzel und `schemata/` enthalten drei `.rng`-Dateien, keine ODD; eine RNG-Datei wird nicht als ODD geführt. Die Fragmentstudie von 2026-09-05 bleibt unberührt |
| `correspSearch/csStorage/gw9.xml` | wie oben | ablehnen, Dublette der Rolle | größer (20.747 Bytes) und mit Kontaktdaten im Kopf; es wurde nur ein Eingabedokument je Fall vorgesehen |
| `csStorage/keun-tucholsky.xml`, `bucer1-15.xml`, `Formey-Bertrand.xml` | wie oben | ablehnen, Dublette der Rolle | gesichtet, nicht gewählt |
| `ISicily/ISicily/inscriptions/ISic001906.xml` | wie oben | ablehnen | `revisionDesc/@status="stub"`, Editionstext leer |
| SigiDoc (`SigiDoc/SigiDoc`) | nicht gepinnt | zurückstellen, Budget | EpiDoc-kompatible Siegeledition; nur als Suchtreffer gesehen |
| IIP texts, EDH-Datendumps | nicht gepinnt | zurückstellen, Lead | epigraphische Daten; Lizenz und ODD nicht geprüft |
| WeGA- und HenDi-CMIF-Erzeugung (`modules/cmif.xql`) | nicht gepinnt | zurückstellen, Lead | erzeugerseitiger Pfad von Edition zu CMIF; Lizenz nicht geprüft |
| Katalogfall | keiner | Lücke | in dieser begrenzten Erkundung wurde kein Katalogprojekt mit geprüfter ODD betrachtet; CMIF gilt nicht als Katalog |

Nicht aufgenommene, aber lokal gespeicherte Kontextdateien stehen mit Hash und
Grund im Aufnahmemanifest. Das sind die CI-Workflows von GerDraCor, DraCor
und EpiDoc/Source, Lizenz- und README-Dateien sowie die Schema- und
Schematron-Kopien von CMIF, csAPI, EpiDoc und I.Sicily.

## Bekannte Verzerrungen

- Alle drei Fälle sind gemeinschaftlich veröffentlichte Profile, die viele
  Projekte nachnutzen. Sie sind keine lokale ODD eines einzelnen Projekts und
  sagen nichts über unveröffentlichte lokale Anpassungen.
- Alle Repositories liegen auf GitHub und sind gut dokumentiert. Zwei Fälle
  kommen aus dem deutschsprachigen Raum, einer ist britisch-international
  (EpiDoc, I.Sicily). TEI-nahe Infrastrukturprojekte sind überrepräsentiert.
- Kleine Dateien wurden bevorzugt. Die CMIF-Eingabe wurde nach Sichtung von vier
  kleinen Dateien gewählt; dass sie ein von CMIF 1.1 eingeschränktes Attribut
  verwendet, war bei der Wahl sichtbar.
- Gepinnt sind Entwicklungsstände (`HEAD` am 2026-09-11), nicht die jeweils
  letzte Veröffentlichung, außer bei CMIF (Tag v1.1.0).
- Die Auswahl stammt von einem einzelnen Agenten mit Vorwissen über diese
  Projekte. Statistische Repräsentativität wird nicht beansprucht.

## Notwendige fachliche Abnahme

Die Wahl der Eingabedokumente und jede Deutung ihrer Kodierung braucht eine
menschliche Domänenabnahme: Dramenkodierung (DraCor), epigraphische Edition
und Leidener Konventionen (EpiDoc, I.Sicily) sowie Briefmetadaten (CMIF,
correspSearch).
