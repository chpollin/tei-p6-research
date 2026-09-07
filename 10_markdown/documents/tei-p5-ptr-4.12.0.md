---
type: representation
source-type: document
source: '[[00_sources/tei-p5-ptr-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 ptr
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/ptr.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# ptr

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3333. Git blob: `c5229ca388f3c3c018869c6bae3dd1c53644f08d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-ptr" ident="ptr">
  <gloss versionDate="2007-07-04" xml:lang="en">pointer</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">포인터</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">puntero</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">pointeur</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">puntatore</gloss>
  <desc versionDate="2006-01-11" xml:lang="en">defines a pointer to another location.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">다른 위치로의 포인터를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明一個與其他位置相連結的指標。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">他の場所を示すポインターを定義する。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">définit un pointeur vers un autre emplacement.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define un señalizador a otra localización.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un puntatore ad un'altra posizione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cReferencing"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.internetMedia"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.annotationPart.body"/>
    <memberOf key="model.ptrLike"/>
  </classes>
  <content><empty/></content>
  <constraintSpec scheme="schematron" ident="ptrAtts" xml:lang="en">
    <constraint>
      <sch:rule context="tei:ptr">
        <sch:report test="@target and @cRef">Only one of the attributes @target and @cRef may be supplied on &lt;<sch:name/>>.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ptr-egXML-rq" source="#UND">
      <ptr target="#p143 #p144"/>
      <ptr target="http://www.tei-c.org"/>
      <ptr cRef="1.3.4"/>
    </egXML>
  </exemplum>
  <remarks ident="ptr-remarks" versionDate="2005-10-13" xml:lang="en">
    <p>The <att>target</att> and <att>cRef</att> attributes are mutually exclusive.</p>
  </remarks>
  <remarks ident="ptr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les attributs <att>target</att> et <att>cRef</att> sont exclusifs l'un de l'autre.</p>
  </remarks>
  <remarks ident="ptr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>target</att>と<att>cRef</att>は、排他的に使用される。 </p>
  </remarks>
  <remarks ident="ptr-remarks" versionDate="2016-11-25" xml:lang="de">
    <p>Die <att>target</att> und <att>cRef</att>-Attribute schließen sich gegenseitig aus.</p>
  </remarks>
  <listRef>
    <ptr target="#COXR"/>
    <ptr target="#SAPT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">pointer</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">포인터</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">puntero</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">pointeur</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">puntatore</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-11" xml:lang="en">defines a pointer to another location.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다른 위치로의 포인터를 정의한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明一個與其他位置相連結的指標。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">他の場所を示すポインターを定義する。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">définit un pointeur vers un autre emplacement.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define un señalizador a otra localización.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un puntatore ad un'altra posizione.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cReferencing"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.internetMedia"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.annotationPart.body"/>
    <memberOf key="model.ptrLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="ptrAtts" xml:lang="en">
    <constraint>
      <sch:rule context="tei:ptr">
        <sch:report test="@target and @cRef">Only one of the attributes @target and @cRef may be supplied on &lt;<sch:name/>>.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ptr-egXML-rq" source="#UND">
      <ptr target="#p143 #p144"/>
      <ptr target="http://www.tei-c.org"/>
      <ptr cRef="1.3.4"/>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="ptr-remarks" versionDate="2005-10-13" xml:lang="en">
    <p>The <att>target</att> and <att>cRef</att> attributes are mutually exclusive.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="ptr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les attributs <att>target</att> et <att>cRef</att> sont exclusifs l'un de l'autre.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="ptr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>target</att>と<att>cRef</att>は、排他的に使用される。 </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="ptr-remarks" versionDate="2016-11-25" xml:lang="de">
    <p>Die <att>target</att> und <att>cRef</att>-Attribute schließen sich gegenseitig aus.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COXR"/>
    <ptr target="#SAPT"/>
  </listRef>
```

^b22

