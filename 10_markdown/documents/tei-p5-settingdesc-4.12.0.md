---
type: representation
source-type: document
source: '[[00_sources/tei-p5-settingdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 settingDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/settingDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# settingDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4903. Git blob: `643d67b44482d70ed95194984df667066f14bfd1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="corpus" xml:id="gi-settingDesc" ident="settingDesc">
  <gloss versionDate="2005-01-14" xml:lang="en">setting description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">무대 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">背景描述</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description du contexte</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción de realización</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione dello scenario</gloss>
  <desc versionDate="2014-01-06" xml:lang="en">describes the setting or settings within which a
    language interaction takes place, or other places otherwise referred to in a text, edition,
    or metadata.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">언어적 상호작용이 발생하는 무대 또는 배경을 산문적 기술로서 또는 일련의 무대 요소로서
    기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述語言互動所發生的一個或多個背景，可用一段散文描述或是一系列的背景元素來表達。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">言語交流が行われた状況設定を、散文または一連の要素<gi>setting</gi>に
    より示す。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">décrit le(s) contexte(s) dans lesquels se situe une
    interaction linguistique, soit sous la forme d'une description en prose, soit sous celle
    d'une série d'éléments décrivant le contexte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe en prosa, o mediante una serie de
    elementos de realización, la realización o realizaciones dentro de las cuales una
    interacción lingüística tiene lugar.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive lo scenario o gli scenari nei quali si
    svolge l'interazione linuistica, sia in forma di prosa descrittiva sia con elementi di
    scenario.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="setting"/>
        <classRef key="model.placeLike"/>
        <elementRef key="listPlace"/>
      </alternate>
    </alternate>
  </content>
  <constraintSpec ident="settingDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:settingDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settingDesc-egXML-ok"> <settingDesc> <p>Texts recorded in the
    Canadian Parliament building in Ottawa, between April and November 1988 </p>
    </settingDesc> </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settingDesc-egXML-tn"> <settingDesc> <p>Pierre Mendès France,
    Entretiens avec Jean Lacouture (1980-1981 )</p> </settingDesc> </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settingDesc-egXML-wq"> <settingDesc>
    <p>文本錄於渥太華的加拿大國會大廈，介於1988年4月至11月間</p> </settingDesc> </egXML>
  </exemplum>
  <remarks ident="settingDesc-remarks" versionDate="2019-12-25" xml:lang="en">
    <p rend="dataDesc">May contain a prose description organized as paragraphs, or a series of
    <gi>setting</gi> elements. If used to record not settings of language interactions, but
    other places mentioned in the text, then <gi>place</gi> optionally grouped by
    <gi>listPlace</gi> inside <gi>standOff</gi> should be preferred.</p>
  </remarks>
  <remarks ident="settingDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir un texte organisé en paragraphes ou une série d'éléments
    <gi>setting</gi>.</p>
  </remarks>
  <remarks ident="settingDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落レベルの散文、または一連の要素<gi>setting</gi>を含むかもしれない。 </p>
  </remarks>
  <listRef>
    <ptr target="#CCAH"/>
    <ptr target="#HD4"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">setting description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">무대 기술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">背景描述</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description du contexte</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción de realización</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione dello scenario</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2014-01-06" xml:lang="en">describes the setting or settings within which a
    language interaction takes place, or other places otherwise referred to in a text, edition,
    or metadata.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">언어적 상호작용이 발생하는 무대 또는 배경을 산문적 기술로서 또는 일련의 무대 요소로서
    기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述語言互動所發生的一個或多個背景，可用一段散文描述或是一系列的背景元素來表達。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">言語交流が行われた状況設定を、散文または一連の要素<gi>setting</gi>に
    より示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">décrit le(s) contexte(s) dans lesquels se situe une
    interaction linguistique, soit sous la forme d'une description en prose, soit sous celle
    d'une série d'éléments décrivant le contexte.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe en prosa, o mediante una serie de
    elementos de realización, la realización o realizaciones dentro de las cuales una
    interacción lingüística tiene lugar.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive lo scenario o gli scenari nei quali si
    svolge l'interazione linuistica, sia in forma di prosa descrittiva sia con elementi di
    scenario.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <elementRef key="setting"/>
        <classRef key="model.placeLike"/>
        <elementRef key="listPlace"/>
      </alternate>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="settingDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:settingDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settingDesc-egXML-ok"> <settingDesc> <p>Texts recorded in the
    Canadian Parliament building in Ottawa, between April and November 1988 </p>
    </settingDesc> </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settingDesc-egXML-tn"> <settingDesc> <p>Pierre Mendès France,
    Entretiens avec Jean Lacouture (1980-1981 )</p> </settingDesc> </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-settingDesc-egXML-wq"> <settingDesc>
    <p>文本錄於渥太華的加拿大國會大廈，介於1988年4月至11月間</p> </settingDesc> </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="settingDesc-remarks" versionDate="2019-12-25" xml:lang="en">
    <p rend="dataDesc">May contain a prose description organized as paragraphs, or a series of
    <gi>setting</gi> elements. If used to record not settings of language interactions, but
    other places mentioned in the text, then <gi>place</gi> optionally grouped by
    <gi>listPlace</gi> inside <gi>standOff</gi> should be preferred.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="settingDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir un texte organisé en paragraphes ou une série d'éléments
    <gi>setting</gi>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="settingDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落レベルの散文、または一連の要素<gi>setting</gi>を含むかもしれない。 </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAH"/>
    <ptr target="#HD4"/>
  </listRef>
```

^b23

