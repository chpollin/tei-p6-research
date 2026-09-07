---
type: representation
source-type: document
source: '[[00_sources/tei-p5-flib-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fLib
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fLib.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fLib

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3886. Git blob: `ed4b44f35d372a9ec9f51c89cfff12ceef97b73d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fLib" ident="fLib">
  <gloss versionDate="2007-07-04" xml:lang="en">feature library</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질 라이브러리</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能存庫</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">bibliothèque de traits</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">biblioteca de rasgos</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">biblioteca dei tratti</gloss>
  <desc versionDate="2017-06-14" xml:lang="en">assembles a library of <gi>f</gi> (feature) elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">자질 요소를 하나의 라이브러리에 모아놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">功能元素的集合存庫。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性に関する要素のライブラリをまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">rassemble une bibliothèque de traits.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa una biblioteca de elementos de rasgo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raccoglie una bilbioteca degli elementi dei tratti.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.fsdDeclPart"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    
      <elementRef key="f" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fLib-egXML-pb" source="#UND">
      <fLib n="agreement features">
        <f xml:id="pers1" name="person">
          <symbol value="first"/>
        </f>
        <f xml:id="pers2" name="person">
          <symbol value="second"/>
        </f>
        <!-- ... -->
        <f xml:id="nums" name="number">
          <symbol value="singular"/>
        </f>
        <f xml:id="nump" name="number">
          <symbol value="plural"/>
        </f>
        <!-- ... -->
      </fLib>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fLib-egXML-rs" source="#UND">
      <fLib n="agreement features">
        <f xml:id="fr_pers1" name="person">
          <symbol value="first"/>
        </f>
        <f xml:id="fr_pers2" name="person">
          <symbol value="second"/>
        </f>
        <f xml:id="fr_nums" name="number">
          <symbol value="singular"/>
        </f>
        <f xml:id="fr_nump" name="number">
          <symbol value="plural"/>
        </f>
      </fLib>
    </egXML>
  </exemplum>
  <remarks ident="fLib-remarks" versionDate="2012-03-14" xml:lang="en">
    <p>The global <att>n</att> attribute may be used to supply an informal
name to categorize the library's contents.</p>
  </remarks>
  <remarks ident="fLib-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut global <att>n</att> peut être utilisé pour fournir un nom informel afin de
                catégoriser les contenus de la bibliothèque.</p>
  </remarks>
  <remarks ident="fLib-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    グローバル属性<att>n</att>が、当該ライブラリの内容を分類する、非公
    式の名前を示すために使われるかもしれない。
    </p>
  </remarks>
  <listRef>
    <ptr target="#FSFL" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">feature library</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질 라이브러리</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能存庫</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">bibliothèque de traits</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">biblioteca de rasgos</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">biblioteca dei tratti</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-06-14" xml:lang="en">assembles a library of <gi>f</gi> (feature) elements.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질 요소를 하나의 라이브러리에 모아놓는다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">功能元素的集合存庫。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性に関する要素のライブラリをまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">rassemble une bibliothèque de traits.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa una biblioteca de elementos de rasgo.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raccoglie una bilbioteca degli elementi dei tratti.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.fsdDeclPart"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <elementRef key="f" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fLib-egXML-pb" source="#UND">
      <fLib n="agreement features">
        <f xml:id="pers1" name="person">
          <symbol value="first"/>
        </f>
        <f xml:id="pers2" name="person">
          <symbol value="second"/>
        </f>
        <!-- ... -->
        <f xml:id="nums" name="number">
          <symbol value="singular"/>
        </f>
        <f xml:id="nump" name="number">
          <symbol value="plural"/>
        </f>
        <!-- ... -->
      </fLib>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fLib-egXML-rs" source="#UND">
      <fLib n="agreement features">
        <f xml:id="fr_pers1" name="person">
          <symbol value="first"/>
        </f>
        <f xml:id="fr_pers2" name="person">
          <symbol value="second"/>
        </f>
        <f xml:id="fr_nums" name="number">
          <symbol value="singular"/>
        </f>
        <f xml:id="fr_nump" name="number">
          <symbol value="plural"/>
        </f>
      </fLib>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="fLib-remarks" versionDate="2012-03-14" xml:lang="en">
    <p>The global <att>n</att> attribute may be used to supply an informal
name to categorize the library's contents.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="fLib-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut global <att>n</att> peut être utilisé pour fournir un nom informel afin de
                catégoriser les contenus de la bibliothèque.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="fLib-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    グローバル属性<att>n</att>が、当該ライブラリの内容を分類する、非公
    式の名前を示すために使われるかもしれない。
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSFL" type="div3"/>
  </listRef>
```

^b21

