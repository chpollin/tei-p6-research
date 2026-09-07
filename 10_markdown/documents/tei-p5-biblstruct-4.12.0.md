---
type: representation
source-type: document
source: '[[00_sources/tei-p5-biblstruct-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 biblStruct
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/biblStruct.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# biblStruct

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6704. Git blob: `797303df20e3eda1bd032aaa808e8b8b0c414c73`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-biblStruct" ident="biblStruct">
  <gloss versionDate="2005-04-15" xml:lang="en">structured bibliographic citation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">구조화된 서지 인용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">結構次要書目</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">référence bibliographique structurée</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">cita bibliográfica estructurada.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">citazione bibliografica strutturata</gloss>
  <gloss versionDate="2023-09-21" xml:lang="ja">構造的な典拠情報</gloss>
  <desc versionDate="2008-01-13" xml:lang="en">contains a structured bibliographic citation, in which only bibliographic sub-elements
    appear and in a specified order.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">서지의 하위 요소만이 나타나는, 명시적 순서로 구성되는 구조화된 서지 인용을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含僅出現子節點的結構書目資料，並以特定順序呈現。</desc>
  <desc versionDate="2023-09-21" xml:lang="ja">構造を持った典拠情報を示す。下位要素として、典拠情報を示す要素のみが、決められた順番で出現する。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une référence bibliographique dans laquelle
    seuls des sous-éléments bibliographiques apparaissent et cela, selon un ordre déterminé.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una cita bibliográfica estructurada, en la cual
    sólo aparecen los subelementos bibliográficos y en un orden especificado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una citazione bibliografica strutturata che può
    contenere solo altri elemento nell'ordine specificato.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.docStatus"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblLike"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="analytic" minOccurs="0" maxOccurs="unbounded"/>      
      <sequence minOccurs="1" maxOccurs="unbounded">
        <elementRef key="monogr"/>
        <elementRef key="series" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="relatedItem"/>
        <elementRef key="citedRange"/>
      </alternate>
    </sequence>
  </content>
  <constraintSpec ident="biblStruct-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:biblStruct"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblStruct-egXML-fg">
      <biblStruct>
        <monogr>
          <author>Blain, Virginia</author>
          <author>Clements, Patricia</author>
          <author>Grundy, Isobel</author>
          <title>The Feminist Companion to Literature in English: women writers from the middle ages
            to the present</title>
          <edition>first edition</edition>
          <imprint>
            <publisher>Yale University Press</publisher>
            <pubPlace>New Haven and London</pubPlace>
            <date>1990</date>
          </imprint>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
  <exemplum versionDate="2023-02-20" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblStruct-egXML-pd">
      <biblStruct type="newspaper">
        <analytic>
          <author>
            <forename>David</forename>
            <surname>Barstow</surname>
          </author>
          <author>
            <forename>Susanne</forename>
            <surname>Craig</surname>
          </author>
          <author>
            <forename>Russ</forename>
            <surname>Buettner</surname>
          </author>
          <title type="main">Trump Took Part in Suspect Schemes to Evade Tax Bills</title>
          <title type="sub">Behind the Myth of a Self-Made Billionaire, a Vast Inheritance From His Father</title>
        </analytic>
        <monogr>
          <title level="j">The New York Times</title>
          <imprint>
            <pubPlace>New York</pubPlace>
            <publisher>A. G. Sulzberger</publisher>
            <date when="2018-10-03">Wednesday, October 3, 2018</date>
          </imprint>
          <biblScope unit="volume">CLXVIII</biblScope>
          <biblScope unit="issue">58,104</biblScope>
          <biblScope unit="page">1</biblScope>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblStruct-egXML-wd">
      <biblStruct>
        <monogr>
          <author>Anouilh, Jean</author>
          <title>Antigone</title>
          <edition>première édition</edition>
          <imprint>
            <publisher>in Nouvelles pièces noires, La Table ronde</publisher>
            <pubPlace>Paris</pubPlace>
            <date>1955</date>
          </imprint>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblStruct-egXML-cv">
      <biblStruct>
        <monogr>
          <author>王大明</author>
          <author>文天行</author>
          <author>廖全京</author>
          <title>抗戰文藝報刊編目彙編</title>
          <edition>初版</edition>
          <imprint>
            <publisher>四川省社會科學院</publisher>
            <pubPlace>成都</pubPlace>
            <date>1984</date>
          </imprint>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COBITY"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-04-15" xml:lang="en">structured bibliographic citation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">구조화된 서지 인용</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">結構次要書目</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">référence bibliographique structurée</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">cita bibliográfica estructurada.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">citazione bibliografica strutturata</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2023-09-21" xml:lang="ja">構造的な典拠情報</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-01-13" xml:lang="en">contains a structured bibliographic citation, in which only bibliographic sub-elements
    appear and in a specified order.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">서지의 하위 요소만이 나타나는, 명시적 순서로 구성되는 구조화된 서지 인용을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含僅出現子節點的結構書目資料，並以特定順序呈現。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-09-21" xml:lang="ja">構造を持った典拠情報を示す。下位要素として、典拠情報を示す要素のみが、決められた順番で出現する。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une référence bibliographique dans laquelle
    seuls des sous-éléments bibliographiques apparaissent et cela, selon un ordre déterminé.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una cita bibliográfica estructurada, en la cual
    sólo aparecen los subelementos bibliográficos y en un orden especificado.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una citazione bibliografica strutturata che può
    contenere solo altri elemento nell'ordine specificato.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.docStatus"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblLike"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="analytic" minOccurs="0" maxOccurs="unbounded"/>      
      <sequence minOccurs="1" maxOccurs="unbounded">
        <elementRef key="monogr"/>
        <elementRef key="series" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.noteLike"/>
        <classRef key="model.ptrLike"/>
        <elementRef key="relatedItem"/>
        <elementRef key="citedRange"/>
      </alternate>
    </sequence>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="biblStruct-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:biblStruct"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblStruct-egXML-fg">
      <biblStruct>
        <monogr>
          <author>Blain, Virginia</author>
          <author>Clements, Patricia</author>
          <author>Grundy, Isobel</author>
          <title>The Feminist Companion to Literature in English: women writers from the middle ages
            to the present</title>
          <edition>first edition</edition>
          <imprint>
            <publisher>Yale University Press</publisher>
            <pubPlace>New Haven and London</pubPlace>
            <date>1990</date>
          </imprint>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2023-02-20" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblStruct-egXML-pd">
      <biblStruct type="newspaper">
        <analytic>
          <author>
            <forename>David</forename>
            <surname>Barstow</surname>
          </author>
          <author>
            <forename>Susanne</forename>
            <surname>Craig</surname>
          </author>
          <author>
            <forename>Russ</forename>
            <surname>Buettner</surname>
          </author>
          <title type="main">Trump Took Part in Suspect Schemes to Evade Tax Bills</title>
          <title type="sub">Behind the Myth of a Self-Made Billionaire, a Vast Inheritance From His Father</title>
        </analytic>
        <monogr>
          <title level="j">The New York Times</title>
          <imprint>
            <pubPlace>New York</pubPlace>
            <publisher>A. G. Sulzberger</publisher>
            <date when="2018-10-03">Wednesday, October 3, 2018</date>
          </imprint>
          <biblScope unit="volume">CLXVIII</biblScope>
          <biblScope unit="issue">58,104</biblScope>
          <biblScope unit="page">1</biblScope>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblStruct-egXML-wd">
      <biblStruct>
        <monogr>
          <author>Anouilh, Jean</author>
          <title>Antigone</title>
          <edition>première édition</edition>
          <imprint>
            <publisher>in Nouvelles pièces noires, La Table ronde</publisher>
            <pubPlace>Paris</pubPlace>
            <date>1955</date>
          </imprint>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-biblStruct-egXML-cv">
      <biblStruct>
        <monogr>
          <author>王大明</author>
          <author>文天行</author>
          <author>廖全京</author>
          <title>抗戰文藝報刊編目彙編</title>
          <edition>初版</edition>
          <imprint>
            <publisher>四川省社會科學院</publisher>
            <pubPlace>成都</pubPlace>
            <date>1984</date>
          </imprint>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBITY"/>
    <ptr target="#HD3"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b22

