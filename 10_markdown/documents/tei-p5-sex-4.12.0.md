---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sex-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sex
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sex.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sex

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3842. Git blob: `0ec937e5c25d84245e409b44dd24197fce4f3c9f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-sex" ident="sex">
  <gloss versionDate="2009-03-19" xml:lang="en">sex</gloss>
  <gloss versionDate="2009-03-19" xml:lang="fr">sexe</gloss>
  <desc versionDate="2022-05-10" xml:lang="en">specifies the sex of an organism.</desc>
  <desc versionDate="2022-05-10" xml:lang="fr">précise le sexe d'un organisme.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 성을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指明個人性別。</desc>
  <desc versionDate="2021-09-21" xml:lang="ja">生物学的性別を示す。</desc>
  <desc versionDate="2022-05-10" xml:lang="es">especifica el sexo de un organismo.</desc>
  <desc versionDate="2022-05-10" xml:lang="it">specifica il sesso di un organismo.</desc>
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
      <desc versionDate="2012-10-07" xml:lang="en">supplies a coded value for sex.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.sex"/>
      </datatype>
      <remarks ident="sex-attr.value-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
      <remarks ident="sex-attr.value-remarks" versionDate="2022-05-03" xml:lang="fr">
        <p>Les valeurs de cet attribut peuvent être définies localement par un projet ou peuvent faire référence à un standard externe.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-yk">
      <sex value="F">female</sex>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-wc">
      <sex value="I">Intersex</sex>
    </egXML>
  </exemplum>
  <exemplum versionDate="2022-05-31" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-tl">
      <sex value="TG F">Female (TransWoman)</sex>
    </egXML>
  </exemplum>
  <exemplum versionDate="2022-05-31" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-kc">
      <sex value="F">féminin</sex>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW" versionDate="2022-05-31">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-zm">
      <sex value="F">女性</sex>
    </egXML>
  </exemplum>
  <remarks ident="sex-remarks" versionDate="2022-05-03" xml:lang="en">
    <p>As with other culturally-constructed traits such as age and gender, the way in which this
      concept is described in different cultural contexts varies. The normalizing attributes are
      provided only as an optional means of simplifying that variety for purposes of
      interoperability or project-internal taxonomies for consistency, and should not be used where
      that is inappropriate or unhelpful. The content of the element may be used to describe the
      intended concept in more detail.</p>
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
<gloss versionDate="2009-03-19" xml:lang="en">sex</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="fr">sexe</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2022-05-10" xml:lang="en">specifies the sex of an organism.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2022-05-10" xml:lang="fr">précise le sexe d'un organisme.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 성을 명시한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明個人性別。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2021-09-21" xml:lang="ja">生物学的性別を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-05-10" xml:lang="es">especifica el sexo de un organismo.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2022-05-10" xml:lang="it">specifica il sesso di un organismo.</desc>
```

^b9

### Block 10

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

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-10-07" xml:lang="en">supplies a coded value for sex.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.sex"/>
      </datatype>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="sex-attr.value-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="sex-attr.value-remarks" versionDate="2022-05-03" xml:lang="fr">
        <p>Les valeurs de cet attribut peuvent être définies localement par un projet ou peuvent faire référence à un standard externe.</p>
      </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-yk">
      <sex value="F">female</sex>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-wc">
      <sex value="I">Intersex</sex>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2022-05-31" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-tl">
      <sex value="TG F">Female (TransWoman)</sex>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2022-05-31" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-kc">
      <sex value="F">féminin</sex>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW" versionDate="2022-05-31">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sex-egXML-zm">
      <sex value="F">女性</sex>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="sex-remarks" versionDate="2022-05-03" xml:lang="en">
    <p>As with other culturally-constructed traits such as age and gender, the way in which this
      concept is described in different cultural contexts varies. The normalizing attributes are
      provided only as an optional means of simplifying that variety for purposes of
      interoperability or project-internal taxonomies for consistency, and should not be used where
      that is inappropriate or unhelpful. The content of the element may be used to describe the
      intended concept in more detail.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
```

^b22

