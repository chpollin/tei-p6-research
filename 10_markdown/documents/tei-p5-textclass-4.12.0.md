---
type: representation
source-type: document
source: '[[00_sources/tei-p5-textclass-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 textClass
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/textClass.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# textClass

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5388. Git blob: `0ced94c6ba96b253037ccf3db71bffb9eb3720bd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-textClass" ident="textClass">
  <gloss versionDate="2005-01-14" xml:lang="en">text classification</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">classification du texte</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 분류</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文件分類</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Textklassifikation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">clasificación de texto</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">classificazione del testo</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">groups information which describes the nature or topic of a text in terms of a standard
    classification scheme, thesaurus, etc.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">regroupe des informations décrivant la nature ou le sujet
    d’un texte selon des termes issus d’un système de classification standardisé, d’un thésaurus,
    etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준 분류 스키마, 시소러스 등을 통해서 텍스트의 특성 또는 주제를 기술하는 정보를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集以標準分類架構、索引典等來描述文件性質或主題的資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">標準的な分類スキーム、分類語彙などにより、テキストの性格や話題を示す 情報をまとめる。</desc>
  <desc versionDate="2016-11-24" xml:lang="de">gruppiert Informationen über Art oder Thematik eines Textes unter 
      Bezug auf ein Standard-Klassifikationsschema, einen Thesaurus o. ä.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa información que describe la naturaleza o la
    temática de un texto en términos de un esquema de clasificación estándard.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni che descrivono la natura o
    l'argomento di un testo secondo uno schema di classificazione standard, un dizionario i
    sinonimi, ecc.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="classCode"/>
      <elementRef key="catRef"/>
      <elementRef key="keywords"/>
    </alternate>
  </content>
  <constraintSpec ident="textClass-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:textClass"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textClass-egXML-fb">
      <taxonomy>
        <category xml:id="acprose">
          <catDesc>Academic prose</catDesc>
        </category>
        <!-- other categories here -->
      </taxonomy>
      <!-- ... -->
      <textClass>
        <catRef target="#acprose"/>
        <classCode scheme="http://www.udcc.org">001.9</classCode>
        <keywords scheme="http://authorities.loc.gov">
          <list>
            <item>End of the world</item>
            <item>History - philosophy</item>
          </list>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textClass-egXML-pi">
      <textClass>
        <keywords scheme="#fr_RAMEAU">
          <list>
            <item>Littérature française -- 20ème siècle -- Histoire et critique</item>
            <item>Littérature française -- Histoire et critique -- Théorie, etc.</item>
            <item>Français (langue) -- Style -- Bases de données.</item>
          </list>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textClass-egXML-fu" source="#UND">
      <textClass>
        <catRef target="#fr_forme_prose"/>
      </textClass>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textClass-egXML-xm">
      <taxonomy>
        <category xml:id="zh-tw_chineseliterature">
          <catDesc>中國文學</catDesc>
        </category>
        <!-- 其他文類 -->
      </taxonomy>
      <!-- ... -->
      <textClass>
        <catRef target="#zh-tw_chineseliterature"/>
        <classCode scheme="http://www.ncl.edu.tw/">820</classCode>
        <keywords scheme="http://authorities.loc.gov">
          <list>
            <item>傷痕文學</item>
            <item>語文類</item>
          </list>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD43"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">text classification</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">classification du texte</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">텍스트 분류</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文件分類</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Textklassifikation</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">clasificación de texto</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">classificazione del testo</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups information which describes the nature or topic of a text in terms of a standard
    classification scheme, thesaurus, etc.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">regroupe des informations décrivant la nature ou le sujet
    d’un texte selon des termes issus d’un système de classification standardisé, d’un thésaurus,
    etc.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준 분류 스키마, 시소러스 등을 통해서 텍스트의 특성 또는 주제를 기술하는 정보를 모아 놓는다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集以標準分類架構、索引典等來描述文件性質或主題的資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">標準的な分類スキーム、分類語彙などにより、テキストの性格や話題を示す 情報をまとめる。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">gruppiert Informationen über Art oder Thematik eines Textes unter 
      Bezug auf ein Standard-Klassifikationsschema, einen Thesaurus o. ä.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa información que describe la naturaleza o la
    temática de un texto en términos de un esquema de clasificación estándard.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni che descrivono la natura o
    l'argomento di un testo secondo uno schema di classificazione standard, un dizionario i
    sinonimi, ecc.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <elementRef key="classCode"/>
      <elementRef key="catRef"/>
      <elementRef key="keywords"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="textClass-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:textClass"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textClass-egXML-fb">
      <taxonomy>
        <category xml:id="acprose">
          <catDesc>Academic prose</catDesc>
        </category>
        <!-- other categories here -->
      </taxonomy>
      <!-- ... -->
      <textClass>
        <catRef target="#acprose"/>
        <classCode scheme="http://www.udcc.org">001.9</classCode>
        <keywords scheme="http://authorities.loc.gov">
          <list>
            <item>End of the world</item>
            <item>History - philosophy</item>
          </list>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textClass-egXML-pi">
      <textClass>
        <keywords scheme="#fr_RAMEAU">
          <list>
            <item>Littérature française -- 20ème siècle -- Histoire et critique</item>
            <item>Littérature française -- Histoire et critique -- Théorie, etc.</item>
            <item>Français (langue) -- Style -- Bases de données.</item>
          </list>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textClass-egXML-fu" source="#UND">
      <textClass>
        <catRef target="#fr_forme_prose"/>
      </textClass>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textClass-egXML-xm">
      <taxonomy>
        <category xml:id="zh-tw_chineseliterature">
          <catDesc>中國文學</catDesc>
        </category>
        <!-- 其他文類 -->
      </taxonomy>
      <!-- ... -->
      <textClass>
        <catRef target="#zh-tw_chineseliterature"/>
        <classCode scheme="http://www.ncl.edu.tw/">820</classCode>
        <keywords scheme="http://authorities.loc.gov">
          <list>
            <item>傷痕文學</item>
            <item>語文類</item>
          </list>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD43"/>
  </listRef>
```

^b23

