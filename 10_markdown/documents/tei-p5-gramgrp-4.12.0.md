---
type: representation
source-type: document
source: '[[00_sources/tei-p5-gramgrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 gramGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/gramGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# gramGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4203. Git blob: `8aa9b85fbbd1a92c84ffd78098befb16fd06f65e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-gramGrp" ident="gramGrp">
  <gloss versionDate="2005-01-14" xml:lang="en">grammatical information group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문법 정보군</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文法資訊群</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">groupe d'informations grammaticales</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de información gramatical</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gruppo di informazioni grammaticali</gloss>
  <desc versionDate="2005-10-11" xml:lang="en">groups morpho-syntactic information about a lexical item, e.g. <gi>pos</gi>, <gi>gen</gi>, <gi>number</gi>, <gi>case</gi>, or
        <gi>iType</gi> (inflectional class).</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어휘 항목에 관한 형태-통사적 정보를 모아 놓는다. 예, <gi>pos</gi>, <gi>gen</gi>, <gi>number</gi>, <gi>case</gi>, 또는
        <gi>iType</gi> (굴절 부류)</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集文字的型態及句法資訊，例如詞性、性別、單複數、格、或屈折變化種類。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">語彙項目、の形態統語情報、例えば、<gi>gen</gi>、<gi>number</gi>、
  <gi>case</gi>、<gi>iType</gi>をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des informations morphosyntaxiques sur
			un item lexical, par exemple Partie du discours <gi>pos</gi>, Genre <gi>gen</gi>, Nombre
				<gi>number</gi>, Cas <gi>case</gi>, ou Classe flexionnelle <gi>iType</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa la información morfosintáctica sobre un elemento léxico, p.ej. <gi>pos</gi>,
            <gi>gen</gi>, <gi>number</gi>, <gi>case</gi>, o <gi>iType</gi> (categoría no flexiva).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni morfo-sintattiche di un'unità lessicale, ad esempio <gi>pos</gi>,
            <gi>gen</gi>, <gi>number</gi>, <gi>case</gi>, or <gi>iType</gi> (tipologie flessive).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
    <memberOf key="model.lexicalRefinement"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <classRef key="model.inter"/>
        <classRef key="model.gramPart"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gramGrp-egXML-ee">
      <entry>
        <form>
          <orth>luire</orth>
        </form>
        <gramGrp>
          <pos>verb</pos>
          <subc>intransitive</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gramGrp-egXML-oz">
      <entry>
        <form>
          <orth>luire</orth>
        </form>
        <gramGrp>
          <pos>verbe</pos>
          <subc>intransitif</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gramGrp-egXML-uc">
      <entry>
        <form>
          <orth>luire</orth>
        </form>
        <gramGrp>
          <pos>動詞</pos>
          <subc>不及物的</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DITPGR" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">grammatical information group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문법 정보군</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文法資訊群</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">groupe d'informations grammaticales</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de información gramatical</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gruppo di informazioni grammaticali</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-10-11" xml:lang="en">groups morpho-syntactic information about a lexical item, e.g. <gi>pos</gi>, <gi>gen</gi>, <gi>number</gi>, <gi>case</gi>, or
        <gi>iType</gi> (inflectional class).</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어휘 항목에 관한 형태-통사적 정보를 모아 놓는다. 예, <gi>pos</gi>, <gi>gen</gi>, <gi>number</gi>, <gi>case</gi>, 또는
        <gi>iType</gi> (굴절 부류)</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集文字的型態及句法資訊，例如詞性、性別、單複數、格、或屈折變化種類。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">語彙項目、の形態統語情報、例えば、<gi>gen</gi>、<gi>number</gi>、
  <gi>case</gi>、<gi>iType</gi>をまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des informations morphosyntaxiques sur
			un item lexical, par exemple Partie du discours <gi>pos</gi>, Genre <gi>gen</gi>, Nombre
				<gi>number</gi>, Cas <gi>case</gi>, ou Classe flexionnelle <gi>iType</gi>.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa la información morfosintáctica sobre un elemento léxico, p.ej. <gi>pos</gi>,
            <gi>gen</gi>, <gi>number</gi>, <gi>case</gi>, o <gi>iType</gi> (categoría no flexiva).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni morfo-sintattiche di un'unità lessicale, ad esempio <gi>pos</gi>,
            <gi>gen</gi>, <gi>number</gi>, <gi>case</gi>, or <gi>iType</gi> (tipologie flessive).</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
    <memberOf key="model.lexicalRefinement"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <classRef key="model.inter"/>
        <classRef key="model.gramPart"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gramGrp-egXML-ee">
      <entry>
        <form>
          <orth>luire</orth>
        </form>
        <gramGrp>
          <pos>verb</pos>
          <subc>intransitive</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gramGrp-egXML-oz">
      <entry>
        <form>
          <orth>luire</orth>
        </form>
        <gramGrp>
          <pos>verbe</pos>
          <subc>intransitif</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gramGrp-egXML-uc">
      <entry>
        <form>
          <orth>luire</orth>
        </form>
        <gramGrp>
          <pos>動詞</pos>
          <subc>不及物的</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPGR" type="div2"/>
  </listRef>
```

^b19

