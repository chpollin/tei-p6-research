---
type: representation
source-type: document
source: '[[00_sources/tei-p5-def-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 def
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/def.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# def

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3670. Git blob: `0eb220f593a7e2ef372a2189d65a0d415a0f6dd1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-def" ident="def">
  <gloss versionDate="2005-01-14" xml:lang="en">definition</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">정의</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">定義</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">définition</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">definición</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">definizione</gloss>
  <gloss versionDate="2024-08-08" xml:lang="ja">定義</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains definition text in a dictionary entry.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전 표제 항목의 정의 텍스트를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含詞條中的定義文。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書項目における定義を示す。</desc>
  <desc versionDate="2009-02-23" xml:lang="fr">contient le texte de la définition dans une entrée de dictionnaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el texto de definición en una entrada de
    diccionario.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una definizione in una voce di dizionario.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <!-- Per issue #1800 we wanted <usg> inside <def>, but the following: -->
  <!-- <content> -->
  <!--   <alternate minOccurs="0" maxOccurs="unbounded"> -->
  <!--     <macroRef key="macro.paraContent"/> -->
  <!--     <elementRef key="usg"/> -->
  <!--   </alternate> -->
  <!-- </content> -->
  <!-- does not work due to DTD generation problems. -->
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-def-egXML-id">
      <entry>
        <form>
          <orth>competitor</orth>
          <hyph>com|peti|tor</hyph>
          <pron>k@m"petit@(r)</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
        <def>person who competes.</def>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-def-egXML-ur">
      <entry>
        <form>
          <orth>compétiteur</orth>
          <hyph>com|péti|teur</hyph>
          <pron> [köpetitœR]</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
        <def>Personne qui entre en compétition.</def>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-def-egXML-wz">
      <entry>
        <form>
          <orth>音</orth>
          <hyph>( 因漢字無法以連字符號拆解，故不提供範例。)</hyph>
          <pron>yin</pron>
        </form>
        <gramGrp>
          <pos>名詞</pos>
        </gramGrp>
        <def>物體受振動所發出的聲響；人口裡發出的聲響或腔調。</def>
      </entry>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DITPDE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">definition</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">정의</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">定義</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">définition</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">definición</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">definizione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-08-08" xml:lang="ja">定義</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains definition text in a dictionary entry.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전 표제 항목의 정의 텍스트를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含詞條中的定義文。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書項目における定義を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-02-23" xml:lang="fr">contient le texte de la définition dans une entrée de dictionnaire.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el texto de definición en una entrada de
    diccionario.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una definizione in una voce di dizionario.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-def-egXML-id">
      <entry>
        <form>
          <orth>competitor</orth>
          <hyph>com|peti|tor</hyph>
          <pron>k@m"petit@(r)</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
        <def>person who competes.</def>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-def-egXML-ur">
      <entry>
        <form>
          <orth>compétiteur</orth>
          <hyph>com|péti|teur</hyph>
          <pron> [köpetitœR]</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
        <def>Personne qui entre en compétition.</def>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-def-egXML-wz">
      <entry>
        <form>
          <orth>音</orth>
          <hyph>( 因漢字無法以連字符號拆解，故不提供範例。)</hyph>
          <pron>yin</pron>
        </form>
        <gramGrp>
          <pos>名詞</pos>
        </gramGrp>
        <def>物體受振動所發出的聲響；人口裡發出的聲響或腔調。</def>
      </entry>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPDE"/>
  </listRef>
```

^b20

