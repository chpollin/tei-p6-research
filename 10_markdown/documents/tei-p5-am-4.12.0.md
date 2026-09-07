---
type: representation
source-type: document
source: '[[00_sources/tei-p5-am-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 am
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/am.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# am

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4048. Git blob: `4639bc52d5a1c12e96e15881ebd7416f0df10c63`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-am" ident="am">
  <gloss versionDate="2007-09-04" xml:lang="en">abbreviation marker</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">축약 표지</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">marcador de la abreviatura</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">marqueur d'abréviation</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">marcatore di abbreviazione</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">省略記号</gloss>
  <desc versionDate="2007-09-04" xml:lang="en">contains a sequence of letters or signs present in an
  abbreviation which are omitted or replaced in the expanded form of
  the abbreviation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">축약의 확장형에서 생략되거나 대체된 축약형으로, 제시된 문자열 또는 기호열을 포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene una secuencia de letras o símbolos  presentes en una abreviatura que han sido omitidos o substituidos en la forma extendida de la abreviatura.</desc>
  <desc versionDate="2022-06-07" xml:lang="ja">当該省略形が、原形を省略またはそれに代わったことを示す文字列または記号列。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">contient une succession de lettres ou de signes
  présents dans une abréviation mais omis ou remplacés dans la forme développée de l'abréviation.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene una sequenza di lettere o segni presenti in un'abbreviazione e omessi o sostituiti nella forma estesa dell'abreviazione stessa.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
  <content>
    <!--    <rng:ref name="macro.xtext"/>-->
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.pPart.transcriptional"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-am-egXML-hz" source="#pos4st">
      do you <abbr>Mr<am>.</am>
         </abbr> Jones?
    </egXML>
  </exemplum>
  <exemplum versionDate="2016-08-12" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-am-egXML-ic" xml:lang="la" source="#NONE">
      <choice>
        <abbr>Aug<am>g</am></abbr>
        <expan>Aug<ex>ustorum duo</ex></expan>
      </choice>
    </egXML>
  </exemplum>
    
  <exemplum versionDate="2016-08-12" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:lang="la" xml:id="gi-am-egXML-id" source="#UND">
        <abbr>eu<am>
            <g ref="#b-er"/>
        </am>y</abbr>
        <abbr>
            <am>
                <g ref="#b-per"/>
            </am>sone
        </abbr> ... 
    </egXML>
  </exemplum>
    
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-am-egXML-ql" source="#fr-ex-Duhamel-Pasquier">
      Le <abbr>Dr<am>.</am>
         </abbr>
      Pasquier se prit à marcher de long en large, les mains glissées dans la
      ceinture de sa blouse.
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-am-egXML-hh" source="#UND">
       因漢語無字母的縮寫，故無法提供縮寫符號的範例 
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#PHAB" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-09-04" xml:lang="en">abbreviation marker</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">축약 표지</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">marcador de la abreviatura</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">marqueur d'abréviation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">marcatore di abbreviazione</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">省略記号</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-04" xml:lang="en">contains a sequence of letters or signs present in an
  abbreviation which are omitted or replaced in the expanded form of
  the abbreviation.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">축약의 확장형에서 생략되거나 대체된 축약형으로, 제시된 문자열 또는 기호열을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene una secuencia de letras o símbolos  presentes en una abreviatura que han sido omitidos o substituidos en la forma extendida de la abreviatura.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-06-07" xml:lang="ja">当該省略形が、原形を省略またはそれに代わったことを示す文字列または記号列。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">contient une succession de lettres ou de signes
  présents dans une abréviation mais omis ou remplacés dans la forme développée de l'abréviation.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene una sequenza di lettere o segni presenti in un'abbreviazione e omessi o sostituiti nella forma estesa dell'abreviazione stessa.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!--    <rng:ref name="macro.xtext"/>-->
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.pPart.transcriptional"/>
      </alternate>
    
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-am-egXML-hz" source="#pos4st">
      do you <abbr>Mr<am>.</am>
         </abbr> Jones?
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2016-08-12" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-am-egXML-ic" xml:lang="la" source="#NONE">
      <choice>
        <abbr>Aug<am>g</am></abbr>
        <expan>Aug<ex>ustorum duo</ex></expan>
      </choice>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2016-08-12" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:lang="la" xml:id="gi-am-egXML-id" source="#UND">
        <abbr>eu<am>
            <g ref="#b-er"/>
        </am>y</abbr>
        <abbr>
            <am>
                <g ref="#b-per"/>
            </am>sone
        </abbr> ... 
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-am-egXML-ql" source="#fr-ex-Duhamel-Pasquier">
      Le <abbr>Dr<am>.</am>
         </abbr>
      Pasquier se prit à marcher de long en large, les mains glissées dans la
      ceinture de sa blouse.
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-am-egXML-hh" source="#UND">
       因漢語無字母的縮寫，故無法提供縮寫符號的範例 
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHAB" type="div3"/>
  </listRef>
```

^b20

