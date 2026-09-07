---
type: representation
source-type: document
source: '[[00_sources/tei-p5-eg-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 eg
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/eg.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# eg

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3951. Git blob: `787046604a75e2e7040d153ab8494a3563f32792`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-eg" ident="eg">
  <gloss versionDate="2007-07-04" xml:lang="en">example</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">예</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">ejemplo</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">exemple</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">esempio</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains any kind of illustrative example.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">실례적 예의 유형을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何種類的說明範例。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">例を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient toutes sortes d'exemples illustratifs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de ejemplo ilustrativo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi esempio.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.egLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eg-egXML-kl">
      <p>The
    <gi>term</gi> element is declared using the following syntax:
    <eg>&lt;![CDATA[&lt;!ELEMENT term (%phrase.content;)&gt;]]</eg>
         </p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eg-egXML-qg">
      <p>L'élément <gi>term</gi> est déclaré en utilisant la syntaxe suivante :
            <eg>&lt;![CDATA[&lt;!ELEMENT term (%phrase.content;)&gt;]]</eg>
         </p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eg-egXML-bs">
      <p><gi>術語</gi>元素用於以下語法：
        <eg>&lt;![CDATA[&lt;!ELEMENT term (%phrase.content;)&gt;]]</eg>
         </p>
    </egXML>
  </exemplum>
  <remarks ident="eg-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>If the example contains material in XML markup, either it must be
enclosed within a CDATA marked  section, or character entity
references must be used to represent the markup delimiters. If the
    example contains well-formed XML, it should be marked using the
    more specific <gi>egXML</gi> element.</p>
  </remarks>
  <remarks ident="eg-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Si le contenu de l'exemple est balisé en XML, il y a deux possibilités : soit ce
                contenu doit être mis dans une section littérale CDATA, soit des références
                d'entité de caractère doivent être utilisées pour représenter les délimiteurs de
                balisage. Si l'exemple contient du XML bien formé, il devrait être balisé en
                utilisant l'élément plus spécifique <gi>egXML</gi>.</p>
  </remarks>
  <remarks ident="eg-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該例としてXMLデータを含む場合には、その部分をCDATAセクションにす
    るか、またはタグ区切子を文字エンティティ参照で示す必要がある。
    当該例が整形式XMLである場合、例は要素<gi>egXML</gi>で示した方がよ
    い。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TDATT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">example</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">예</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">ejemplo</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">exemple</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">esempio</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains any kind of illustrative example.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">실례적 예의 유형을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何種類的說明範例。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">例を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient toutes sortes d'exemples illustratifs.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier tipo de ejemplo ilustrativo.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi esempio.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.egLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eg-egXML-kl">
      <p>The
    <gi>term</gi> element is declared using the following syntax:
    <eg>&lt;![CDATA[&lt;!ELEMENT term (%phrase.content;)&gt;]]</eg>
         </p>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eg-egXML-qg">
      <p>L'élément <gi>term</gi> est déclaré en utilisant la syntaxe suivante :
            <eg>&lt;![CDATA[&lt;!ELEMENT term (%phrase.content;)&gt;]]</eg>
         </p>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-eg-egXML-bs">
      <p><gi>術語</gi>元素用於以下語法：
        <eg>&lt;![CDATA[&lt;!ELEMENT term (%phrase.content;)&gt;]]</eg>
         </p>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="eg-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>If the example contains material in XML markup, either it must be
enclosed within a CDATA marked  section, or character entity
references must be used to represent the markup delimiters. If the
    example contains well-formed XML, it should be marked using the
    more specific <gi>egXML</gi> element.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="eg-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Si le contenu de l'exemple est balisé en XML, il y a deux possibilités : soit ce
                contenu doit être mis dans une section littérale CDATA, soit des références
                d'entité de caractère doivent être utilisées pour représenter les délimiteurs de
                balisage. Si l'exemple contient du XML bien formé, il devrait être balisé en
                utilisant l'élément plus spécifique <gi>egXML</gi>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="eg-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該例としてXMLデータを含む場合には、その部分をCDATAセクションにす
    るか、またはタグ区切子を文字エンティティ参照で示す必要がある。
    当該例が整形式XMLである場合、例は要素<gi>egXML</gi>で示した方がよ
    い。
    </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TDATT"/>
  </listRef>
```

^b22

