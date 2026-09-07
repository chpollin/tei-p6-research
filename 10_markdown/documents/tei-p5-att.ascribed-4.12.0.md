---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.ascribed-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.ascribed
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.ascribed.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.ascribed

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4676. Git blob: `4e2f0b4de0b4c6703c97ef44cb5364cdf8bbe3f6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-ascribed" ident="att.ascribed">
  <desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements representing speech or action that can be ascribed to a
    specific individual.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">특정 개인의 대화 또는 행위를 표시하는 요소에 대한 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供的元素屬性代表言詞或行為，可出自某一特定個人。</desc>
  <desc versionDate="2022-05-09" xml:lang="ja">特定個人の発話や行動を示す要素に付随する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour des éléments transcrivant la
    parole ou l'action qui peuvent être attribuées à un individu en particulier.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para los elementos que representan
    palabras o acciones atribuibles a individuos determinados.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi agli elementi che rappresentano
    parole o azioni attribuibili a singoli individui</desc>
  <attList>
    <attDef ident="who">
      <desc versionDate="2005-11-05" xml:lang="en">indicates the person, or group of people, to whom the element content is ascribed.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">요소 내용이 속하는 사람 또는 사람의 그룹을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該元素內容所歸屬的個人或團體。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素の内容が示す人物を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique la personne ou le groupe de personnes à qui
        le contenu de l'élément est attribué.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la persona o grupo de personas a las que se
        refiere el contenido del elemento.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la persona o gruppo di persone alle quali
        viene attribuito il contenuto dell'elemento</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <exemplum xml:lang="en">
        <p>In the following example from Hamlet, speeches (<gi>sp</gi>) in the body of the play 
        are linked to <gi>role</gi> elements in the <gi>castList</gi> using the <att>who</att>
        attribute.</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-ascribed-egXML-jk" xml:lang="en" valid="feasible" source="#CODR-eg-293">
          <castItem type="role">
            <role xml:id="Barnardo">Bernardo</role>
          </castItem>
          <castItem type="role">
            <role xml:id="Francisco">Francisco</role>
            <roleDesc>a soldier</roleDesc>
          </castItem>
          <!-- ... -->
          <sp who="#Barnardo">
            <speaker>Bernardo</speaker>
            <l n="1">Who's there?</l>
          </sp>
          <sp who="#Francisco">
            <speaker>Francisco</speaker>
            <l n="2">Nay, answer me: stand, and unfold yourself.</l>
          </sp>
        </egXML>
      </exemplum>
      <remarks ident="att.ascribed-attr.who-remarks" versionDate="2013-11-22" xml:lang="en"><p>For transcribed speech, this will typically identify a participant or participant
        group; in other contexts, it will point to any identified <gi>person</gi> element.</p></remarks>
      <remarks ident="att.ascribed-attr.who-remarks" versionDate="2013-11-22" xml:lang="fr"><p>Pour un discours transcrit, identifiera typiquement un participant ou
        un groupe participant ; dans d'autres contextes, pointera vers n'importe quel élément
          <gi>person</gi> identifié.</p></remarks>
      <remarks ident="att.ascribed-attr.who-remarks" versionDate="2018-12-31" xml:lang="ja"><p>転記された音声の場合、これは通常、参加者または参加者グループを識別する。他のコンテキストでは、識別された<gi>person</gi>要素を指し示す。</p></remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#COHQQ"/>
    <ptr target="#TSBA"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-05" xml:lang="en">provides attributes for elements representing speech or action that can be ascribed to a
    specific individual.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">특정 개인의 대화 또는 행위를 표시하는 요소에 대한 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供的元素屬性代表言詞或行為，可出自某一特定個人。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-05-09" xml:lang="ja">特定個人の発話や行動を示す要素に付随する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour des éléments transcrivant la
    parole ou l'action qui peuvent être attribuées à un individu en particulier.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para los elementos que representan
    palabras o acciones atribuibles a individuos determinados.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi agli elementi che rappresentano
    parole o azioni attribuibili a singoli individui</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-11-05" xml:lang="en">indicates the person, or group of people, to whom the element content is ascribed.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">요소 내용이 속하는 사람 또는 사람의 그룹을 나타낸다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該元素內容所歸屬的個人或團體。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素の内容が示す人物を示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique la personne ou le groupe de personnes à qui
        le contenu de l'élément est attribué.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la persona o grupo de personas a las que se
        refiere el contenido del elemento.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la persona o gruppo di persone alle quali
        viene attribuito il contenuto dell'elemento</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <p>In the following example from Hamlet, speeches (<gi>sp</gi>) in the body of the play 
        are linked to <gi>role</gi> elements in the <gi>castList</gi> using the <att>who</att>
        attribute.</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-ascribed-egXML-jk" xml:lang="en" valid="feasible" source="#CODR-eg-293">
          <castItem type="role">
            <role xml:id="Barnardo">Bernardo</role>
          </castItem>
          <castItem type="role">
            <role xml:id="Francisco">Francisco</role>
            <roleDesc>a soldier</roleDesc>
          </castItem>
          <!-- ... -->
          <sp who="#Barnardo">
            <speaker>Bernardo</speaker>
            <l n="1">Who's there?</l>
          </sp>
          <sp who="#Francisco">
            <speaker>Francisco</speaker>
            <l n="2">Nay, answer me: stand, and unfold yourself.</l>
          </sp>
        </egXML>
      </exemplum>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.ascribed-attr.who-remarks" versionDate="2013-11-22" xml:lang="en"><p>For transcribed speech, this will typically identify a participant or participant
        group; in other contexts, it will point to any identified <gi>person</gi> element.</p></remarks>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.ascribed-attr.who-remarks" versionDate="2013-11-22" xml:lang="fr"><p>Pour un discours transcrit, identifiera typiquement un participant ou
        un groupe participant ; dans d'autres contextes, pointera vers n'importe quel élément
          <gi>person</gi> identifié.</p></remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.ascribed-attr.who-remarks" versionDate="2018-12-31" xml:lang="ja"><p>転記された音声の場合、これは通常、参加者または参加者グループを識別する。他のコンテキストでは、識別された<gi>person</gi>要素を指し示す。</p></remarks>
```

^b19

### Block 20

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQQ"/>
    <ptr target="#TSBA"/>
  </listRef>
```

^b20

