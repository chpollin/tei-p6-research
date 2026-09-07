---
type: representation
source-type: document
source: '[[00_sources/tei-p5-persona-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 persona
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/persona.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# persona

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6248. Git blob: `6b5f13640662502bef5ce846e8b1d293c06217b7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-persona" ident="persona">
  <desc versionDate="2016-02-16" xml:lang="en">provides information about one of the personalities identified for a given individual, where
    an individual has multiple personalities.</desc>
   <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <alternate>   
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.personPart"/>
          <classRef key="model.global"/>
        </alternate>
    </alternate>
  </content>
  <attList>
    <attDef ident="role" usage="opt">
      <desc versionDate="2005-12-14" xml:lang="en">specifies a primary role or classification for the persona.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사람에 대한 주요 역할 또는 분류를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該人物的主要角色或分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該人物の第一位の役割や分類を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise un rôle principal ou une classification principale pour cette personne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">establece el rol o la clasificación primaria de una persona.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">stabilisce il ruolo o la classificazione primaria di una persona.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
<remarks ident="persona-attr.role-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
	project, using arbitrary keywords such as <val>artist</val>,
	<val>employer</val>, <val>author</val>, <val>relative</val>, or
	<val>servant</val>, each of which should be associated with a
	definition. Such local definitions will typically be provided by a
	<gi>valList</gi> element in the project schema
specification.</p></remarks>
    </attDef>
    <attDef ident="sex" usage="opt">
      <desc versionDate="2005-12-14" xml:lang="en">specifies the sex of the persona.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사람의 성을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該人物的性別。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該人物の性別を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise le sexe de la personne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el sexo de una persona.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il sesso di una persona.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.sex"/></datatype>
      <remarks ident="persona-attr.sex-remarks" versionDate="2022-05-18" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or may refer to an external standard.</p>
      </remarks>
    </attDef>
    <attDef ident="gender" usage="opt">
      <desc versionDate="2022-05-18" xml:lang="en">specifies the gender of the persona.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
      <remarks ident="persona-attr.gender-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
    </attDef>
    <attDef ident="age" usage="opt">
      <desc versionDate="2005-12-14" xml:lang="en">specifies an age group for the persona.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사람의 연령군을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該人物所屬的年齡層。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該人物の年齢層を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise une tranche d'âge pour la personne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica un intervalo de edad para una persona.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la fascia di età di una persona.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
<remarks ident="persona-attr.age-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
	project, using arbitrary keywords such as <val>infant</val>,
	<val>child</val>, <val>teen</val>, <val>adult</val>, or
	<val>senior</val>, each of which should be associated with a
	definition. Such local definitions will typically be provided by a
	<gi>valList</gi> element in the project schema
specification.</p></remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-persona-egXML-dx">
      <person sex="M" age="adult">
        <persona sex="M">
          <persName>Dr Henry Jekyll</persName>
        </persona>
        <persona sex="M" age="youth">
          <persName>Edward Hyde</persName>
        </persona>
      </person>
    </egXML>
  </exemplum>
 
  <remarks ident="persona-remarks" versionDate="2016-02-16" xml:lang="en">
  <p>Note that a persona is not the same as a role. A role 
   may be assumed by different people on different occasions, whereas a persona is
 unique to a particular person, even though it may resemble others. Similarly, when an actor takes on or enacts the role of a historical person, they do not
 thereby acquire a new persona. </p> </remarks>
  
  <listRef>
    <ptr target="#NDPERSE"/>
   </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-02-16" xml:lang="en">provides information about one of the personalities identified for a given individual, where
    an individual has multiple personalities.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.persStateLike"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>   
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.personPart"/>
          <classRef key="model.global"/>
        </alternate>
    </alternate>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-12-14" xml:lang="en">specifies a primary role or classification for the persona.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사람에 대한 주요 역할 또는 분류를 명시한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該人物的主要角色或分類。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該人物の第一位の役割や分類を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">précise un rôle principal ou une classification principale pour cette personne.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">establece el rol o la clasificación primaria de una persona.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">stabilisce il ruolo o la classificazione primaria di una persona.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="persona-attr.role-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
	project, using arbitrary keywords such as <val>artist</val>,
	<val>employer</val>, <val>author</val>, <val>relative</val>, or
	<val>servant</val>, each of which should be associated with a
	definition. Such local definitions will typically be provided by a
	<gi>valList</gi> element in the project schema
specification.</p></remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-12-14" xml:lang="en">specifies the sex of the persona.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사람의 성을 명시한다.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該人物的性別。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該人物の性別を示す。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">précise le sexe de la personne.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el sexo de una persona.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il sesso di una persona.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.sex"/></datatype>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="persona-attr.sex-remarks" versionDate="2022-05-18" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or may refer to an external standard.</p>
      </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2022-05-18" xml:lang="en">specifies the gender of the persona.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="persona-attr.gender-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-12-14" xml:lang="en">specifies an age group for the persona.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사람의 연령군을 명시한다.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該人物所屬的年齡層。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該人物の年齢層を示す。</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">précise une tranche d'âge pour la personne.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica un intervalo de edad para una persona.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la fascia di età di una persona.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[1]`.

```xml
<remarks ident="persona-attr.age-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
	project, using arbitrary keywords such as <val>infant</val>,
	<val>child</val>, <val>teen</val>, <val>adult</val>, or
	<val>senior</val>, each of which should be associated with a
	definition. Such local definitions will typically be provided by a
	<gi>valList</gi> element in the project schema
specification.</p></remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-persona-egXML-dx">
      <person sex="M" age="adult">
        <persona sex="M">
          <persName>Dr Henry Jekyll</persName>
        </persona>
        <persona sex="M" age="youth">
          <persName>Edward Hyde</persName>
        </persona>
      </person>
    </egXML>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="persona-remarks" versionDate="2016-02-16" xml:lang="en">
  <p>Note that a persona is not the same as a role. A role 
   may be assumed by different people on different occasions, whereas a persona is
 unique to a particular person, even though it may resemble others. Similarly, when an actor takes on or enacts the role of a historical person, they do not
 thereby acquire a new persona. </p> </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSE"/>
   </listRef>
```

^b36

