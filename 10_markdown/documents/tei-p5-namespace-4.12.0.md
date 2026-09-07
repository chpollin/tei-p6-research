---
type: representation
source-type: document
source: '[[00_sources/tei-p5-namespace-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 namespace
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/namespace.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# namespace

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4092. Git blob: `abc2e1c10f9e85fd29ab8595e8c8f9e2a350f995`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-namespace" ident="namespace">
  <gloss versionDate="2009-01-05" xml:lang="en">namespace</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">espace de noms</gloss>
  <desc versionDate="2006-02-07" xml:lang="en">supplies the formal name of the namespace to which the elements documented by its children
    belong.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">fournit le nom formel de l'espace de noms auquel
    appartiennent les éléments documentés par ses éléments fils.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">그 자식이 기술한 요소가 속하는 네임스페이스의 공식적 이름을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供其子元素所描述的元素所屬的名稱空間之正式名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該要素が属する名前空間の形式名を示す。</desc>
  <desc versionDate="2018-07-18" xml:lang="de"> liefert die formale Bezeichnung des Namensraums, zu
    dem die Elemente als Kind-Elemente gehören.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre formal del namespace al cual
    pertenecen los elementos documentados por sus hijos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome formale del namespace a cui appartengono
    gli elementi documentati dai suoi figli.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <elementRef key="tagUsage" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <attList>
    <attDef ident="name" usage="req">
      <desc versionDate="2012-12-27" xml:lang="en">specifies the full formal name of the namespace concerned.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">le nom formel complet de l'espace de noms concerné.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">관련된 네임스페이스의 공식적 전체 이름</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">名稱空間的正式完整名稱。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">名前空間の全形式名。</desc>
      <desc versionDate="2018-07-18" xml:lang="de">gibt die vollständige formale Bezeichnung des betreffenden
        Namensraums an.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">el nombre formal completo del namespace concerniente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">l'intero nome formale del namespace in questione.</desc>
      <datatype minOccurs="0" maxOccurs="1"><dataRef key="teidata.namespace"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-namespace-egXML-fa">
      <namespace name="http://www.tei-c.org/ns/1.0">
        <tagUsage gi="hi" occurs="28" withId="2"> Used only to mark English words
          italicized in the copy text </tagUsage>
      </namespace>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-namespace-egXML-ez">
      <namespace name="http://www.tei-c.org/ns/1.0">
        <tagUsage gi="foreign">Employé pour marquer des mots non-français dans le
            texte.</tagUsage>
      </namespace>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-namespace-egXML-ah">
      <namespace name="http://www.tei-c.org/ns/1.0">
        <tagUsage gi="hi" occurs="28" withId="2"> 僅用於標示副本上的斜體英文字</tagUsage>
      </namespace>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD57"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="en">namespace</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">espace de noms</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-02-07" xml:lang="en">supplies the formal name of the namespace to which the elements documented by its children
    belong.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">fournit le nom formel de l'espace de noms auquel
    appartiennent les éléments documentés par ses éléments fils.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">그 자식이 기술한 요소가 속하는 네임스페이스의 공식적 이름을 제공한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供其子元素所描述的元素所屬的名稱空間之正式名稱。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素が属する名前空間の形式名を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de"> liefert die formale Bezeichnung des Namensraums, zu
    dem die Elemente als Kind-Elemente gehören.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre formal del namespace al cual
    pertenecen los elementos documentados por sus hijos.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome formale del namespace a cui appartengono
    gli elementi documentati dai suoi figli.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <elementRef key="tagUsage" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">specifies the full formal name of the namespace concerned.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">le nom formel complet de l'espace de noms concerné.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">관련된 네임스페이스의 공식적 전체 이름</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">名稱空間的正式完整名稱。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">名前空間の全形式名。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">gibt die vollständige formale Bezeichnung des betreffenden
        Namensraums an.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">el nombre formal completo del namespace concerniente.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">l'intero nome formale del namespace in questione.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="1"><dataRef key="teidata.namespace"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-namespace-egXML-fa">
      <namespace name="http://www.tei-c.org/ns/1.0">
        <tagUsage gi="hi" occurs="28" withId="2"> Used only to mark English words
          italicized in the copy text </tagUsage>
      </namespace>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-namespace-egXML-ez">
      <namespace name="http://www.tei-c.org/ns/1.0">
        <tagUsage gi="foreign">Employé pour marquer des mots non-français dans le
            texte.</tagUsage>
      </namespace>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-namespace-egXML-ah">
      <namespace name="http://www.tei-c.org/ns/1.0">
        <tagUsage gi="hi" occurs="28" withId="2"> 僅用於標示副本上的斜體英文字</tagUsage>
      </namespace>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD57"/>
  </listRef>
```

^b25

