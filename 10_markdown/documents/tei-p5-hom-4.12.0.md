---
type: representation
source-type: document
source: '[[00_sources/tei-p5-hom-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 hom
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/hom.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# hom

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4074. Git blob: `45f43671678e35ca8e44764ccea3ddc809789175`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-hom" ident="hom">
  <gloss versionDate="2005-01-14" xml:lang="en">homograph</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">동형이의어</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">同形義異字</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">homographe</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">homógrafo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">omografo</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">groups information relating to one homograph within an entry.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 표제 항목 내에서 하나의 동형이의어와 관련된 정보들을 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集辭條中一個同形義異字的相關資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">項目中にあるひとつの同綴異義語に関する情報をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe les informations relatives à un
			homographe dans une entrée.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa información relativa a un homógrafo dentro de una entrada.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni attinenti a un omografo all'interno di una voce.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.entryPart"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="sense"/>
        <elementRef key="pc"/>
        <classRef key="model.entryPart.top"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hom-egXML-uv">
      <entry>
        <form>
          <orth>bray</orth>
          <pron>breI</pron>
        </form>
        <hom>
          <gramGrp>
            <pos>n</pos>
          </gramGrp>
          <def>cry of an ass; sound of a trumpet.</def>
        </hom>
        <hom>
          <gramGrp>
            <pos>vt</pos>
            <subc>VP2A</subc>
          </gramGrp>
          <def>make a cry or sound of this kind.</def>
        </hom>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hom-egXML-qd" source="#fr-ex-Grand-Robert">
      <entry>
        <form>
          <orth>canon</orth>
          <pron>[kanö] </pron>
        </form>
        <hom>
          <gramGrp>
            <pos>n</pos>
            <gen>m.</gen>
          </gramGrp>
          <def>Pièce d'artillerie servant à lancer des projectiles lourds.</def>
        </hom>
        <hom>
          <gramGrp>
            <pos>n.</pos>
            <gen>m.</gen>
          </gramGrp>
          <def>Théol. Loi ecclésiastique.</def>
        </hom>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hom-egXML-eb">
      <entry>
        <form>
          <orth>將</orth>
          <pron>jiang4</pron>
        </form>
        <hom>
          <gramGrp>
            <pos>名</pos>
          </gramGrp>
          <def>軍階名；技藝優良的人。</def>
        </hom>
        <hom>
          <gramGrp>
            <pos>動詞</pos>
            <subc>及物</subc>
          </gramGrp>
          <def>統率軍隊</def>
        </hom>
      </entry>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DIEN" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">homograph</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">동형이의어</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">同形義異字</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">homographe</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">homógrafo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">omografo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups information relating to one homograph within an entry.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 표제 항목 내에서 하나의 동형이의어와 관련된 정보들을 모아 놓는다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集辭條中一個同形義異字的相關資訊。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">項目中にあるひとつの同綴異義語に関する情報をまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe les informations relatives à un
			homographe dans une entrée.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa información relativa a un homógrafo dentro de una entrada.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni attinenti a un omografo all'interno di una voce.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.entryPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="sense"/>
        <elementRef key="pc"/>
        <classRef key="model.entryPart.top"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hom-egXML-uv">
      <entry>
        <form>
          <orth>bray</orth>
          <pron>breI</pron>
        </form>
        <hom>
          <gramGrp>
            <pos>n</pos>
          </gramGrp>
          <def>cry of an ass; sound of a trumpet.</def>
        </hom>
        <hom>
          <gramGrp>
            <pos>vt</pos>
            <subc>VP2A</subc>
          </gramGrp>
          <def>make a cry or sound of this kind.</def>
        </hom>
      </entry>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hom-egXML-qd" source="#fr-ex-Grand-Robert">
      <entry>
        <form>
          <orth>canon</orth>
          <pron>[kanö] </pron>
        </form>
        <hom>
          <gramGrp>
            <pos>n</pos>
            <gen>m.</gen>
          </gramGrp>
          <def>Pièce d'artillerie servant à lancer des projectiles lourds.</def>
        </hom>
        <hom>
          <gramGrp>
            <pos>n.</pos>
            <gen>m.</gen>
          </gramGrp>
          <def>Théol. Loi ecclésiastique.</def>
        </hom>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hom-egXML-eb">
      <entry>
        <form>
          <orth>將</orth>
          <pron>jiang4</pron>
        </form>
        <hom>
          <gramGrp>
            <pos>名</pos>
          </gramGrp>
          <def>軍階名；技藝優良的人。</def>
        </hom>
        <hom>
          <gramGrp>
            <pos>動詞</pos>
            <subc>及物</subc>
          </gramGrp>
          <def>統率軍隊</def>
        </hom>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIEN" type="div2"/>
  </listRef>
```

^b19

