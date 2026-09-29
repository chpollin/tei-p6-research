---
type: representation
source-type: document
source: '[[00_sources/documents/practice-v1-cmif-freieisen-stoeber-9a7ebe3b.xml]]'
converter: tools.ingest_practice_v1 v1; complete original plus JSON-escaped exact
  source fragments
channel: collection
metadata:
  title: CMIF file in correspSearch storage (freieisen-stoeber.xml)
  creator: correspSearch storage; publisher named in the source header
  date: '2026-03-10'
  format: application/xml
  identifier: https://github.com/correspSearch/csStorage/blob/9a7ebe3b68bb464be64d6e08fe1ed8672f90c00d/freieisen-stoeber.xml
  license: CC-BY-4.0
  confidential: false
created: '2026-09-11'
updated: '2026-09-11'
---

# CMIF file in correspSearch storage (freieisen-stoeber.xml)

Source: `freieisen-stoeber.xml` in `correspSearch/csStorage` at commit `9a7ebe3b68bb464be64d6e08fe1ed8672f90c00d`.
Source SHA-256: `bba0af2b8befbb89494bcb836f05a481d4901ea3a2dc0683ff999d29d58bfdef`, 2305 bytes.
Rights: CC-BY-4.0. CMIF file freieisen-stoeber.xml, correspSearch storage, CC BY 4.0; publisher and cited print source are named in the source header.
License evidence: publicationStmt/availability/licence in the file; the repository has no license file.

The complete original is inert source text and is never executed. The
separator newline before its closing fence is not part of the original.
Reading blocks are exact source byte intervals encoded as JSON strings;
their line and byte locators refer to the original.

## Complete original

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
    <teiHeader>
        <fileDesc>
            <titleStmt>
                <title>Brief Johann Christoph Freieisen an August Stoeber</title>
                <editor>Ariane Martin<email>a.martin@uni-mainz.de</email>
                </editor>
            </titleStmt>
            <publicationStmt>
                <publisher>
                    <ref target="https://www.martin.germanistik.uni-mainz.de/">Ariane Martin</ref>
                </publisher>
                <availability>
                    <licence target="https://creativecommons.org/licenses/by/4.0/">CC-BY
                        4.0</licence>
                </availability>
                <idno type="url">https://correspsearch.net/storage/freieisen-stoeber.xml</idno>
                <date when="2026-03-09T14:53:52.197-01:00"/>
            </publicationStmt>
            <sourceDesc>
                <bibl type="print" xml:id="q968f389-b31d-431c-adc6-e01d1af01da1">Ariane Martin:
                    Johann Christoph Freieisens Brief an August Stoeber vom 8. März 1839. Spuren
                    eines Romans über J. M. R. Lenz in einem Dokument der Lenz-Rezeption im Umkreis
                    Georg Büchners. In: Lenz-Jahrbuch. Literatur – Kultur – Medien 1750−1800, Jg. 27
                    (2020), S. 87-97.</bibl>
            </sourceDesc>
        </fileDesc>
        <profileDesc>
            <correspDesc source="#q968f389-b31d-431c-adc6-e01d1af01da1">
                <correspAction type="sent">
                    <persName ref="https://d-nb.info/gnd/104260084">Johann Christoph
                        Freieisen</persName>
                    <placeName ref="http://www.geonames.org/2661552">Bern</placeName>
                    <date when="1839-03-08"/>
                </correspAction>
                <correspAction type="received">
                    <persName ref="https://d-nb.info/gnd/119059010">August Stoeber</persName>
                    <placeName ref="http://www.geonames.org/2973783">Straßburg</placeName>
                    <date evidence="conjecture" when="1839-03-12"/>
                </correspAction>
            </correspDesc>
        </profileDesc>
    </teiHeader>
    <text>
        <body>
            <p/>
        </body>
    </text>
</TEI>

```

## Selected source reading blocks

### r1 document start

Locator: lines 1-1, bytes 0-41, start-tag, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<TEI xmlns=\"http://www.tei-c.org/ns/1.0\">" ^r1

### r2 file licence

Locator: lines 13-16, bytes 510-683, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<availability>\n                    <licence target=\"https://creativecommons.org/licenses/by/4.0/\">CC-BY\n                        4.0</licence>\n                </availability>" ^r2

### r3 correspondence description

Locator: lines 29-41, bytes 1425-2186, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<correspDesc source=\"#q968f389-b31d-431c-adc6-e01d1af01da1\">\n                <correspAction type=\"sent\">\n                    <persName ref=\"https://d-nb.info/gnd/104260084\">Johann Christoph\n                        Freieisen</persName>\n                    <placeName ref=\"http://www.geonames.org/2661552\">Bern</placeName>\n                    <date when=\"1839-03-08\"/>\n                </correspAction>\n                <correspAction type=\"received\">\n                    <persName ref=\"https://d-nb.info/gnd/119059010\">August Stoeber</persName>\n                    <placeName ref=\"http://www.geonames.org/2973783\">Straßburg</placeName>\n                    <date evidence=\"conjecture\" when=\"1839-03-12\"/>\n                </correspAction>\n            </correspDesc>" ^r3

