---
type: representation
source-type: document
source: '[[00_sources/tei-p5-langknown-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 langKnown
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/langKnown.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# langKnown

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6174. Git blob: `caacd2163508c2778ea40460fe7af1e714645d10`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-langKnown" ident="langKnown">
  <gloss versionDate="2007-07-04" xml:lang="en">language known</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">언어 능력</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">語言能力</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">compétence linguistique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">competencia lingüística</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">competenza linguistica</gloss>
  <desc versionDate="2007-07-04" xml:lang="en">summarizes the state of a person's linguistic competence, i.e., knowledge of a single language.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 언어 능력 상태를 요약한다. 즉, 한 언어에 대한 지식</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">個人對於某單一語言的認知狀態。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">個人の言語能力を示す。すなわち、単一言語の知識を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">synthétise l'état des connaissances d'une personne relativement à une langue particulière.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">resume la competencia de una persona en la lengua indicada.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">riassume la competenza di una persona in una determinata lingua.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="tag" usage="req">
      <desc versionDate="2006-06-21" xml:lang="en">supplies a valid language tag for the language concerned.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">관련 언어에 대한 유효한 언어 태그를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用有效的語言標籤來表示所指語言。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該言語を、言語コードで示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">fournit un code de langue valide pour la langue concernée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">asigna un marcador válido a las lengua referida.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un marcatore valido alla lingua in questione.</desc>
      <datatype><dataRef key="teidata.language"/></datatype>
      <remarks ident="langKnown-attr.tag-remarks" versionDate="2007-07-08" xml:lang="en">
        <p>The value for this attribute should be a language <soCalled>tag</soCalled> as defined in <ref target="https://tools.ietf.org/html/bcp47">BCP 47</ref>.</p>
      </remarks>
      <remarks ident="langKnown-attr.tag-remarks" versionDate="2008-12-09" xml:lang="fr">
        <p>La valeur de cet attribut doit être un <soCalled>code</soCalled> tel que défini par <ref target="https://tools.ietf.org/html/bcp47">BCP 47</ref>.</p>
      </remarks>
      <remarks ident="langKnown-attr.tag-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性値は、 <ref target="https://tools.ietf.org/html/bcp47">BCP 47</ref> で定義されている言語タグであるべきである。 </p>
      </remarks>
    </attDef>
    <attDef ident="level" usage="opt">
      <desc versionDate="2006-06-21" xml:lang="en">a code indicating the person's level of knowledge for this language.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 언어에 대한 개인의 지식 수준을 표시하는 부호</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用代號來表示個人對該語言的認知程度。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">個人レベルの知識を示す言語コード。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">un code indiquant le niveau de connaissance qu'une personne a de cette langue.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">código indicativo del nivel de competencia de una persona en una lengua.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">codice che indica il livello di competenza della persona in una determinata lingua.</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnown-egXML-go">
      <langKnown tag="en-GB" level="H">British English</langKnown>
      <langKnown tag="fr" level="M">French</langKnown>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnown-egXML-co" source="#github-mix-mix">
      <person sex="m" role="speaker collaborator">
        <!-- other details omitted -->
        <langKnowledge> 
          <langKnown tag="mix">Mixtepec-Mixtec</langKnown>
          <langKnown tag="en">English</langKnown>
          <langKnown tag="es">Spanish</langKnown>
        </langKnowledge>
      </person>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnown-egXML-lg">
      <langKnown tag="en-GB" level="H">Anglais britannique</langKnown>
      <langKnown tag="fr" level="M">Français</langKnown>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnown-egXML-ls">
      <langKnown tag="en-GB" level="H">英式英文</langKnown>
      <langKnown tag="fr" level="M">法文</langKnown>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">language known</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">언어 능력</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">語言能力</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">compétence linguistique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">competencia lingüística</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">competenza linguistica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-07-04" xml:lang="en">summarizes the state of a person's linguistic competence, i.e., knowledge of a single language.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 언어 능력 상태를 요약한다. 즉, 한 언어에 대한 지식</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">個人對於某單一語言的認知狀態。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">個人の言語能力を示す。すなわち、単一言語の知識を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">synthétise l'état des connaissances d'une personne relativement à une langue particulière.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">resume la competencia de una persona en la lengua indicada.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">riassume la competenza di una persona in una determinata lingua.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2006-06-21" xml:lang="en">supplies a valid language tag for the language concerned.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">관련 언어에 대한 유효한 언어 태그를 제공한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用有效的語言標籤來表示所指語言。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該言語を、言語コードで示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">fournit un code de langue valide pour la langue concernée.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">asigna un marcador válido a las lengua referida.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un marcatore valido alla lingua in questione.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.language"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="langKnown-attr.tag-remarks" versionDate="2007-07-08" xml:lang="en">
        <p>The value for this attribute should be a language <soCalled>tag</soCalled> as defined in <ref target="https://tools.ietf.org/html/bcp47">BCP 47</ref>.</p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="langKnown-attr.tag-remarks" versionDate="2008-12-09" xml:lang="fr">
        <p>La valeur de cet attribut doit être un <soCalled>code</soCalled> tel que défini par <ref target="https://tools.ietf.org/html/bcp47">BCP 47</ref>.</p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="langKnown-attr.tag-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性値は、 <ref target="https://tools.ietf.org/html/bcp47">BCP 47</ref> で定義されている言語タグであるべきである。 </p>
      </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2006-06-21" xml:lang="en">a code indicating the person's level of knowledge for this language.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 언어에 대한 개인의 지식 수준을 표시하는 부호</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用代號來表示個人對該語言的認知程度。</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">個人レベルの知識を示す言語コード。</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">un code indiquant le niveau de connaissance qu'une personne a de cette langue.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">código indicativo del nivel de competencia de una persona en una lengua.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">codice che indica il livello di competenza della persona in una determinata lingua.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnown-egXML-go">
      <langKnown tag="en-GB" level="H">British English</langKnown>
      <langKnown tag="fr" level="M">French</langKnown>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnown-egXML-co" source="#github-mix-mix">
      <person sex="m" role="speaker collaborator">
        <!-- other details omitted -->
        <langKnowledge> 
          <langKnown tag="mix">Mixtepec-Mixtec</langKnown>
          <langKnown tag="en">English</langKnown>
          <langKnown tag="es">Spanish</langKnown>
        </langKnowledge>
      </person>
    </egXML>
  </exemplum>
```

^b36

### Block 37

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnown-egXML-lg">
      <langKnown tag="en-GB" level="H">Anglais britannique</langKnown>
      <langKnown tag="fr" level="M">Français</langKnown>
    </egXML>
  </exemplum>
```

^b37

### Block 38

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnown-egXML-ls">
      <langKnown tag="en-GB" level="H">英式英文</langKnown>
      <langKnown tag="fr" level="M">法文</langKnown>
    </egXML>
  </exemplum>
```

^b38

### Block 39

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b39

