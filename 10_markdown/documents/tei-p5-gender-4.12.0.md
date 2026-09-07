---
type: representation
source-type: document
source: '[[00_sources/tei-p5-gender-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 gender
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/gender.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# gender

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3515. Git blob: `8ca096444c7c97493af52f2cc7949c0beae5a0c8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-gender" ident="gender">
  <gloss versionDate="2022-05-03" xml:lang="en">gender</gloss>
  <desc versionDate="2022-05-17" xml:lang="en">specifies the gender identity of a person, persona, or character.</desc>
  <desc versionDate="2022-05-03" xml:lang="es">especifica la identidad de género de una persona.</desc>
  <desc versionDate="2022-05-03" xml:lang="it">specifica l'identità di genere di una persona.</desc>
  <desc versionDate="2022-09-21" xml:lang="ja">人、ペルソナ、あるいはキャラクターのジェンダーを示す。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="value" usage="opt">
      <desc versionDate="2022-05-03" xml:lang="en">supplies a coded value for gender identity.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
      <remarks ident="gender-attr.value-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gender-egXML-tt" source="#NONE">
      <gender value="W">woman</gender>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gender-egXML-xf" source="#NONE">
      <gender value="NB">non-binary</gender>
    </egXML>
  </exemplum>
  <remarks ident="gender-remarks" versionDate="2022-05-03" xml:lang="en">
    <p>As with other culturally-constructed traits such as
    age and sex, the way in which this concept is described in different
    cultural contexts varies. The normalizing attributes are
    provided only as an optional means of simplifying that variety for purposes of interoperability
    or project-internal taxonomies for consistency, and should not be used where that is
    inappropriate or unhelpful. The content of the element may be used to describe
    the intended concept in more detail.</p>
  </remarks>
  <remarks ident="gender-remarks" versionDate="2022-09-21" xml:lang="ja">
    <p>年齢や性別など他の文化的特質と同様に、この概念が異なる文化的文脈で記述される方法は様々である。
      属性の正規化は、相互運用性あるいはプロジェクト内部の分類法の一貫性のために、その多様性を単純化する付随的な手段としてのみ提供されるものであり、それが不適切であったり有用でない場合には、使用されるべきではない。
      要素の内容は、意図する概念をより詳細に記述するために利用できる。</p>
  </remarks>
  <listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2022-05-03" xml:lang="en">gender</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2022-05-17" xml:lang="en">specifies the gender identity of a person, persona, or character.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2022-05-03" xml:lang="es">especifica la identidad de género de una persona.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2022-05-03" xml:lang="it">specifica l'identità di genere di una persona.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-09-21" xml:lang="ja">人、ペルソナ、あるいはキャラクターのジェンダーを示す。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
```

^b6

### Block 7

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2022-05-03" xml:lang="en">supplies a coded value for gender identity.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="gender-attr.value-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gender-egXML-tt" source="#NONE">
      <gender value="W">woman</gender>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gender-egXML-xf" source="#NONE">
      <gender value="NB">non-binary</gender>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="gender-remarks" versionDate="2022-05-03" xml:lang="en">
    <p>As with other culturally-constructed traits such as
    age and sex, the way in which this concept is described in different
    cultural contexts varies. The normalizing attributes are
    provided only as an optional means of simplifying that variety for purposes of interoperability
    or project-internal taxonomies for consistency, and should not be used where that is
    inappropriate or unhelpful. The content of the element may be used to describe
    the intended concept in more detail.</p>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="gender-remarks" versionDate="2022-09-21" xml:lang="ja">
    <p>年齢や性別など他の文化的特質と同様に、この概念が異なる文化的文脈で記述される方法は様々である。
      属性の正規化は、相互運用性あるいはプロジェクト内部の分類法の一貫性のために、その多様性を単純化する付随的な手段としてのみ提供されるものであり、それが不適切であったり有用でない場合には、使用されるべきではない。
      要素の内容は、意図する概念をより詳細に記述するために利用できる。</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
```

^b15

