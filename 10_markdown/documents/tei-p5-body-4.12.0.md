---
type: representation
source-type: document
source: '[[00_sources/tei-p5-body-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 body
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/body.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# body

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6369. Git blob: `14b7db642799745c59424449cc6f4787db20edf2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-body" ident="body">
  <gloss versionDate="2005-01-14" xml:lang="en">text body</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 본문</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">正文</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">corps du texte</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Textkörper</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">cuerpo del texto</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">corpo del testo</gloss>
  <gloss versionDate="2023-09-27" xml:lang="ja">テキスト本文</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the whole body of a single unitary text, excluding any front or back matter.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전면부 또는 후면부 자료를 배제한 단일 텍스트의 전체 본문을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">單篇文章的整體部分，不包含正文前及正文後資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">前付、後付を除いた、単一の作品の本文全体を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la totalité du corps d’un seul texte simple, à
  l’exclusion de toute partie pré- ou post-liminaire.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält den gesamten Textkörper eines eigenständigen Textes, außer den Vorspann (front) und Nachspann (back).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el cuerpo completo de un texto unitario,
  excluyendo los eventuales añadidos paratextuales (prólogos, dedicatorias, apéndices, etc.) al
  inicio o fin de un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene l'intero corpo di un testo unitario, esclusi
  eventuale peritesto iniziale e finale</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
  </classes>
  <content>
    <sequence>
      <!-- globals as usual -->      
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <!--possibly some divTops, interspersed with globals -->      
      <sequence minOccurs="0">
        <classRef key="model.divTop"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <classRef key="model.divTop"/>
        </alternate>          
      </sequence>
      <!-- possibly some generated divs, interspersed with globals -->      
      <sequence minOccurs="0">
        <classRef key="model.divGenLike"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <classRef key="model.divGenLike"/>
        </alternate>          
      </sequence>
      <!-- 
           now a choice between:           
           a) some divLike things, with globals and generated
              divisions after them if needed 
           b) some div1Like things, with globals
              and generated divisionss after them if needed 
           c) same again, preceded by model.common (or <schemaSpec>)
      -->
      <alternate>
        <!-- a -->          
        <sequence minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.divLike"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.global"/>
            <classRef key="model.divGenLike"/>
          </alternate>
        </sequence>
        <!-- b -->
        <sequence minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.div1Like"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.global"/>
            <classRef key="model.divGenLike"/>
          </alternate>
        </sequence>
        <!-- c -->
        <sequence>
          <sequence minOccurs="1" maxOccurs="unbounded">
            <alternate minOccurs="1" maxOccurs="1">
              <elementRef key="schemaSpec"/>
              <classRef key="model.common"/>
            </alternate>
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          </sequence>
          <alternate minOccurs="0">
            <!-- a -->
            <sequence minOccurs="1" maxOccurs="unbounded">
              <classRef key="model.divLike"/>
              <alternate minOccurs="0" maxOccurs="unbounded">
                <classRef key="model.global"/>
                <classRef key="model.divGenLike"/>
              </alternate>
            </sequence>
            <!-- b -->
            <sequence minOccurs="1" maxOccurs="unbounded">
              <classRef key="model.div1Like"/>
              <alternate minOccurs="0" maxOccurs="unbounded">
                <classRef key="model.global"/>
                <classRef key="model.divGenLike"/>
              </alternate>
            </sequence>
          </alternate>
        </sequence>
      </alternate>
      <!-- end of choice -->
      <!-- finally, some divBottoms interspersed with globals  -->
      <sequence minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.divBottom"/>
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-body-egXML-vp" source="#caedmon" xml:lang="ang">
      <body>
        <l>Nu scylun hergan hefaenricaes uard</l>
        <l>metudæs maecti end his modgidanc</l>
        <l>uerc uuldurfadur sue he uundra gihuaes</l>
        <l>eci dryctin or astelidæ</l>
        <l>he aerist scop aelda barnum</l>
        <l>heben til hrofe haleg scepen.</l>
        <l>tha middungeard moncynnæs uard</l>
        <l>eci dryctin æfter tiadæ</l>
        <l>firum foldu frea allmectig</l>
        <trailer>primo cantauit Cædmon istud carmen.</trailer>
      </body>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">text body</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">텍스트 본문</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">正文</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">corps du texte</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Textkörper</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">cuerpo del texto</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">corpo del testo</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2023-09-27" xml:lang="ja">テキスト本文</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the whole body of a single unitary text, excluding any front or back matter.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전면부 또는 후면부 자료를 배제한 단일 텍스트의 전체 본문을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">單篇文章的整體部分，不包含正文前及正文後資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">前付、後付を除いた、単一の作品の本文全体を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la totalité du corps d’un seul texte simple, à
  l’exclusion de toute partie pré- ou post-liminaire.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält den gesamten Textkörper eines eigenständigen Textes, außer den Vorspann (front) und Nachspann (back).</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el cuerpo completo de un texto unitario,
  excluyendo los eventuales añadidos paratextuales (prólogos, dedicatorias, apéndices, etc.) al
  inicio o fin de un texto.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene l'intero corpo di un testo unitario, esclusi
  eventuale peritesto iniziale e finale</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <!-- globals as usual -->      
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <!--possibly some divTops, interspersed with globals -->      
      <sequence minOccurs="0">
        <classRef key="model.divTop"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <classRef key="model.divTop"/>
        </alternate>          
      </sequence>
      <!-- possibly some generated divs, interspersed with globals -->      
      <sequence minOccurs="0">
        <classRef key="model.divGenLike"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <classRef key="model.divGenLike"/>
        </alternate>          
      </sequence>
      <!-- 
           now a choice between:           
           a) some divLike things, with globals and generated
              divisions after them if needed 
           b) some div1Like things, with globals
              and generated divisionss after them if needed 
           c) same again, preceded by model.common (or <schemaSpec>)
      -->
      <alternate>
        <!-- a -->          
        <sequence minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.divLike"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.global"/>
            <classRef key="model.divGenLike"/>
          </alternate>
        </sequence>
        <!-- b -->
        <sequence minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.div1Like"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.global"/>
            <classRef key="model.divGenLike"/>
          </alternate>
        </sequence>
        <!-- c -->
        <sequence>
          <sequence minOccurs="1" maxOccurs="unbounded">
            <alternate minOccurs="1" maxOccurs="1">
              <elementRef key="schemaSpec"/>
              <classRef key="model.common"/>
            </alternate>
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          </sequence>
          <alternate minOccurs="0">
            <!-- a -->
            <sequence minOccurs="1" maxOccurs="unbounded">
              <classRef key="model.divLike"/>
              <alternate minOccurs="0" maxOccurs="unbounded">
                <classRef key="model.global"/>
                <classRef key="model.divGenLike"/>
              </alternate>
            </sequence>
            <!-- b -->
            <sequence minOccurs="1" maxOccurs="unbounded">
              <classRef key="model.div1Like"/>
              <alternate minOccurs="0" maxOccurs="unbounded">
                <classRef key="model.global"/>
                <classRef key="model.divGenLike"/>
              </alternate>
            </sequence>
          </alternate>
        </sequence>
      </alternate>
      <!-- end of choice -->
      <!-- finally, some divBottoms interspersed with globals  -->
      <sequence minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.divBottom"/>
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-body-egXML-vp" source="#caedmon" xml:lang="ang">
      <body>
        <l>Nu scylun hergan hefaenricaes uard</l>
        <l>metudæs maecti end his modgidanc</l>
        <l>uerc uuldurfadur sue he uundra gihuaes</l>
        <l>eci dryctin or astelidæ</l>
        <l>he aerist scop aelda barnum</l>
        <l>heben til hrofe haleg scepen.</l>
        <l>tha middungeard moncynnæs uard</l>
        <l>eci dryctin æfter tiadæ</l>
        <l>firum foldu frea allmectig</l>
        <trailer>primo cantauit Cædmon istud carmen.</trailer>
      </body>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DS"/>
  </listRef>
```

^b20

