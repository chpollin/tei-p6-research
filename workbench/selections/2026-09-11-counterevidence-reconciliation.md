# Abgleich der Gegenbelegsuche

Am 2026-09-11 wurde die deklarierte GitHub-Auswahl der beiden Themenläufe vom 2026-09-06 gegen den vorhandenen Snapshot geprüft. Dieser Record ergänzt die historischen Auswahlrecords. Er ändert keine Quelle, Assertion oder damalige Disposition und dient ausschließlich der Auswahlkontrolle.

Die Prozedur in `knowledge/operations.md` unter Select verlangt in jedem Themenlauf sowohl `Status: Reconsider for P6` als auch `Status: Wontfix`. Die Records [Metadata and Entities](2026-09-06-metadata-and-entities-run2.md) und [Text and Document Structures](2026-09-06-text-and-document-structures-run1.md) enthalten die erste Labelabfrage. Eine explizite zweite Abfrage fehlt. Die bereits genannten abgelehnten Einzelvorgänge ersetzen den Nachweis der vollständigen Labelabfrage nicht.

## Prüfgrenze

Eingabe ist `corpus/normalized/github/teic-tei-work-items.jsonl`, zugeordnet zu `sources/manifests/2026-09-06-github-teic-tei-work-items.yaml`. Es werden ausschließlich `kind: issue` und `kind: pull-request` ausgewählt. Detail-, Kommentar- und Timeline-Zeilen mit derselben Vorgangsnummer sind andere Recordarten und zählen nicht als zusätzliche Treffer.

Die SHA-256 des Streams lautet `4b85f84c34010d8d3ed35fac86f13fc7ee1fcdcffd155fd76160cd2383a5bba3` und entspricht dem im Manifest benannten Objekt.

| Abfrage | Reproduzierte Treffer | Ergebnis |
|---|---:|---|
| Textstruktur B2, unveränderter Ausdruck des Auswahlrecords | 29 | Anzahl reproduziert |
| Textstruktur B6, unveränderter Ausdruck des Auswahlrecords | 50 | Anzahl reproduziert |
| Exaktes Label `Status: Reconsider for P6` | 17 | Anzahl reproduziert |
| Exaktes Label `Status: Wontfix` | 32 | Fehlender expliziter Suchnachweis erkannt |

## Disposition der ergänzenden Treffer

Die Einteilung beruht auf Titeln und Recordart im Snapshot. Sie bestimmt den nächsten Leseweg. Sie enthält keine Aussage über die Begründung einer Ablehnung oder eine veröffentlichte P5-Wirkung. Jede der 32 Nummern erhält genau eine Disposition für diesen ergänzenden Abgleich.

| Vorgänge | Disposition | Begründung |
|---|---|---|
| Issues 542, 1631, 1676 | `defer`, `lead` | Titel betreffen Entitäten, Verantwortungsattribute oder Referenzpflichten. Die Diskussionen sind gegen die Entitätenfragen zu lesen. |
| Issues 1049, 1430, 1485, 1660, 1712, 1880, 2247, 2570; PRs 2643, 2767 | `defer`, `lead` | Titel betreffen Strukturen, Annotation, Platzierung oder Bildverweise. Vor einer Verwendung als Gegenbeleg fehlen Threadlektüre und Prüfung der damaligen Deklaration bzw. Releasewirkung. Einige Vorgänge sind im alten Strukturrecord bereits unter anderen Abfragen erfasst; die damalige Disposition bleibt dort erhalten. |
| Issues 550, 1276, 1323, 1375, 1787, 1889, 2444, 2684 | `defer`, `another topic's run` | Titel weisen auf Normalisierung, ODD, Anpassung oder Schemakonformität. Sie werden bei diesen Themen erneut nach deren Fragen geprüft. |
| Issues 547, 559, 566, 568, 576, 1348, 1396, 1426, 1429, 1636, 2622 | `defer`, `lead` | Die Titel allein erlauben keine belastbare Aussonderung von Modell-, Beispiel-, Sprach- oder Werkzeugfragen. Eine Ablehnung als fachlich ungeeignet wäre damit unbegründet. |

Die fehlende Labelabfrage ist jetzt als begrenzter Suchbefund sichtbar. Die fachliche Gegenbelegarbeit der Themen ist weiterhin offen. Aus diesem Abgleich folgt keine nachträgliche globale oder thematische Vollständigkeit.

## Konsequenz für die Quellennutzung

Die versionierte P5-Referenz bleibt der Ausgangspunkt für Aussagen über die dokumentierte Releasefähigkeit. GitHub und SourceForge liefern Diskussion und Umsetzungsspuren; ein geschlossenes Ticket belegt keine Annahme und kein Release. TEI-L-Titel bleiben Suchhinweise, bis ein zitierfähiger Thread mit geklärter Aufnahmegrenze vorliegt. Literatur wird anhand einer konkreten Begriffs- oder Vergleichsfrage aufgenommen. Die Projektmodelle und ihre Beispiele beschreiben unabhängige Vorschläge und dürfen keine offizielle TEI-Position ersetzen.

Herkunftsvarianten werden über ihre Identitäten und explizite Beziehungen verbunden. Eine identische Nummer in unterschiedlichen Recordarten oder eine Migration von SourceForge nach GitHub begründet keine Löschung. Der vollständige Referenzbestand bleibt für spätere Fragen erreichbar; die begründete Auswahl begrenzt den jeweiligen Forschungslauf.
