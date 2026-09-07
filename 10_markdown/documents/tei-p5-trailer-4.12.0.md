---
type: representation
source-type: document
source: '[[00_sources/tei-p5-trailer-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 trailer
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/trailer.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# trailer

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3572. Git blob: `ab8ffb174b9af1b64965373aac26b97fe4884fff`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-trailer" ident="trailer">
  <desc versionDate="2005-01-14" xml:lang="en">contains a closing title or footer appearing at the end of a division of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 구역의 종료부에 나타나는 마지막 제목 또는 꼬리말을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文本中一個區段結束時的結尾題名或尾錄。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト部分の最後にある、結びのタイトルや脚注を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un titre de fin ou de bas de page à la fin d’une
    division du texte.</desc>
  <desc versionDate="2017-06-25" xml:lang="de">enthält einen abschließenden Nachsatz oder eine Fußzeile am Ende eines Textabschnitts.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula de clausura o un elemento a pie de
    página que aparece al final de una sección de texto</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una formula di chiusura o un elemento a piè di
    pagina che compare alla fine di una sezione di testo</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divBottomPart"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
	<textNode/>
	<elementRef key="lg"/>
	<classRef key="model.gLike"/>
	<classRef key="model.phrase"/>
	<classRef key="model.inter"/>
	<classRef key="model.lLike"/>
	<classRef key="model.global"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-ru">
      <trailer>Explicit pars tertia</trailer>
    </egXML>
  </exemplum>
   <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-me">
      <trailer>
	<l>In stead of FINIS this advice <hi>I</hi> send,</l>
	<l>Let Rogues and Thieves beware of <lb/>
	<hi>Hamans</hi> END.</l>
      </trailer>
    </egXML>
    <p>From EEBO A87070</p>
   </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-qd">
      <trailer>Explicit pars tertia</trailer>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-yw" source="#biblzh-tw_n61">
      <trailer>畢竟董卓性命如何，且聽下文分解。</trailer>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-wv">
      <trailer>
        <l>In stead of FINIS this advice <hi>I</hi> send,</l>
        <l>Let Rogues and Thieves beware of <lb/>
          <hi>Hamans</hi> END.</l>
      </trailer>
    </egXML>
    <p>Aus EEBO A87070</p>
  </exemplum>
  <listRef>
    <ptr target="#DSCO"/>
    <ptr target="#DSDTB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a closing title or footer appearing at the end of a division of a text.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 구역의 종료부에 나타나는 마지막 제목 또는 꼬리말을 포함한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文本中一個區段結束時的結尾題名或尾錄。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト部分の最後にある、結びのタイトルや脚注を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un titre de fin ou de bas de page à la fin d’une
    division du texte.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-25" xml:lang="de">enthält einen abschließenden Nachsatz oder eine Fußzeile am Ende eines Textabschnitts.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula de clausura o un elemento a pie de
    página que aparece al final de una sección de texto</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una formula di chiusura o un elemento a piè di
    pagina che compare alla fine di una sezione di testo</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divBottomPart"/>
  </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
	<textNode/>
	<elementRef key="lg"/>
	<classRef key="model.gLike"/>
	<classRef key="model.phrase"/>
	<classRef key="model.inter"/>
	<classRef key="model.lLike"/>
	<classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-ru">
      <trailer>Explicit pars tertia</trailer>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-me">
      <trailer>
	<l>In stead of FINIS this advice <hi>I</hi> send,</l>
	<l>Let Rogues and Thieves beware of <lb/>
	<hi>Hamans</hi> END.</l>
      </trailer>
    </egXML>
    <p>From EEBO A87070</p>
   </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-qd">
      <trailer>Explicit pars tertia</trailer>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-yw" source="#biblzh-tw_n61">
      <trailer>畢竟董卓性命如何，且聽下文分解。</trailer>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-trailer-egXML-wv">
      <trailer>
        <l>In stead of FINIS this advice <hi>I</hi> send,</l>
        <l>Let Rogues and Thieves beware of <lb/>
          <hi>Hamans</hi> END.</l>
      </trailer>
    </egXML>
    <p>Aus EEBO A87070</p>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSCO"/>
    <ptr target="#DSDTB"/>
  </listRef>
```

^b16

