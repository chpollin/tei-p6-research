---
type: representation
source-type: document
source: '[[00_sources/tei-p5-place-4.12.0.xml]]'
converter: tools.ingest_git_blobs v2; complete XML plus XML itertext English reading
  blocks with whitespace normalized and identified locators
channel: collection
metadata:
  title: TEI P5 4.12.0 place specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/place.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# place

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.
A locator names an element that carries an `ident` attribute by that ident, so the
reading block of an attribute definition states which attribute it describes.

Source byte length: 2848. Git blob: `04fd590ffcf6f1ecd9e40d227b78407fdc1e0774`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="place" xml:id="gi-place" module="namesdates">
  <gloss versionDate="2008-12-09" xml:lang="en">place</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">lieu</gloss>
  <desc versionDate="2007-06-14" xml:lang="en">contains data about a geographic location.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">지리적 위치에 관한 데이터를 포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene los datos sobre una localización geográfica</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">地理上の場所のデータを示す。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient des informations sur un lieu géographique.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene informazioni relative a un luogo geografico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeLike"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.labelLike"/>
          <classRef key="model.placeStateLike"/>
          <classRef key="model.eventLike"/>
          <elementRef key="name"/>
        </alternate>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.biblLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="idno"/>
        <elementRef key="linkGrp"/>
        <elementRef key="link"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.placeLike"/>
        <elementRef key="listPlace"/>
      </alternate>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-place-egXML-pa">
      <place>
        <country>Lithuania</country>
        <country xml:lang="lt">Lietuva</country>
        <place>
          <settlement>Vilnius</settlement>
        </place>
        <place>
          <settlement>Kaunas</settlement>
        </place>
      </place>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDGEOG"/>
  </listRef>
</elementSpec>
```

## English reading blocks

### Reading 1

XML location: `/elementSpec[@ident='place']/desc[1]`.

contains data about a geographic location. ^r1

