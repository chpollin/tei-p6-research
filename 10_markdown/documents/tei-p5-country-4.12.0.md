---
type: representation
source-type: document
source: '[[00_sources/tei-p5-country-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 country
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/country.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# country

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3881. Git blob: `ef023c09d8dd57076ac0b7ccbd50b926f0bf55cd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-country" ident="country">
  <gloss versionDate="2008-12-09" xml:lang="en">country</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">pays</gloss>
  <desc versionDate="2006-01-22" xml:lang="en">contains the name of a geo-political unit, such as a nation, country, colony, or commonwealth, larger than or administratively superior to a region and smaller than a bloc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 블록보다 큰 국가, 지역, 식민지, 또는 공화국, 또는 하나의 블록보다 작은 지역의 상급 행정기관과 같은, 지리-정치 단위명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個地理政治區域名稱，例如民族、國家、殖民地、或聯邦區域，範圍大於一般地區或行政地位較高，但小於國家聯盟性的地理政治區。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene el nombre de una unidad geopolítica, como una nación, país, colonia, etc. más grande o administrativamente superior que una región y más pequeño que un bloque.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">1つの国家に相当する地政学的な単位名を示す。国家、植民地、共同体・連 邦を含む。これは、行政単位上の地域よりも大きい単位で、連合より小さな 単位である。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient le nom d'une unité géo-politique, comme une nation, un pays, une colonie ou une communauté, plus grande ou administrativement supérieure à une région et plus petite qu'un bloc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un'unità geopolitica, come una nazione, un paese, una colonia, o un'unione di stati, che sia più ampia o amministrativamente superiore rispetto a una regione ma di dimensioni inferiori rispetto a un blocco.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeNamePart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-country-egXML-fk">
      <country key="DK">Denmark</country>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-country-egXML-di">
      <country key="DK">Danemark</country>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-country-egXML-mq">
      <country key="DK">丹麥</country>
    </egXML>
  </exemplum>
  <remarks ident="country-remarks" versionDate="2007-06-28" xml:lang="en">
    <p>The recommended source for codes to represent coded country names is ISO 3166.</p>
  </remarks>
  <remarks ident="country-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p>La source recommandée des codes pour représenter les noms de pays est ISO 3166.</p>
  </remarks>
  <remarks ident="country-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該国家相当地域を示すコードは、ISO3166にあるコードを使うことが推 奨される。 </p>
  </remarks>
  <listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">country</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">pays</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-22" xml:lang="en">contains the name of a geo-political unit, such as a nation, country, colony, or commonwealth, larger than or administratively superior to a region and smaller than a bloc.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 블록보다 큰 국가, 지역, 식민지, 또는 공화국, 또는 하나의 블록보다 작은 지역의 상급 행정기관과 같은, 지리-정치 단위명을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個地理政治區域名稱，例如民族、國家、殖民地、或聯邦區域，範圍大於一般地區或行政地位較高，但小於國家聯盟性的地理政治區。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene el nombre de una unidad geopolítica, como una nación, país, colonia, etc. más grande o administrativamente superior que una región y más pequeño que un bloque.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">1つの国家に相当する地政学的な単位名を示す。国家、植民地、共同体・連 邦を含む。これは、行政単位上の地域よりも大きい単位で、連合より小さな 単位である。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient le nom d'une unité géo-politique, comme une nation, un pays, une colonie ou une communauté, plus grande ou administrativement supérieure à une région et plus petite qu'un bloc.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un'unità geopolitica, come una nazione, un paese, una colonia, o un'unione di stati, che sia più ampia o amministrativamente superiore rispetto a una regione ma di dimensioni inferiori rispetto a un blocco.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeNamePart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-country-egXML-fk">
      <country key="DK">Denmark</country>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-country-egXML-di">
      <country key="DK">Danemark</country>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-country-egXML-mq">
      <country key="DK">丹麥</country>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="country-remarks" versionDate="2007-06-28" xml:lang="en">
    <p>The recommended source for codes to represent coded country names is ISO 3166.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="country-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p>La source recommandée des codes pour représenter les noms de pays est ISO 3166.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="country-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該国家相当地域を示すコードは、ISO3166にあるコードを使うことが推 奨される。 </p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
```

^b18

