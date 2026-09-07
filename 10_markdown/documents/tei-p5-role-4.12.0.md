---
type: representation
source-type: document
source: '[[00_sources/tei-p5-role-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 role
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/role.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# role

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3840. Git blob: `fce97523ddccbaa71c47e2fc91a891e25652fe2d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-role" ident="role">
  <gloss versionDate="2007-06-12" xml:lang="en">role</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">rôle</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">contains the name of a dramatic role, as given in a cast list.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">배역 목록에 제시되는 드라마 배역의 이름</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">角色名單所列的劇中角色名稱。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">el nombre de un papel dramático, según los dados en el
    reparto.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">配役リスト中にある、役名を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">le nom d'un rôle au théâtre tel qu’il est donné dans la
    distribution.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">il nome di un ruolo teatrale, secondo la lista dei
    personaggi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="model.castItemPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="gender" usage="opt">
      <desc versionDate="2023-03-11" xml:lang="en">specifies the gender of the role.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
      <remarks ident="role-attr.gender-remarks" versionDate="2023-03-11" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-role-egXML-rl" source="#JonsBart">
      <role xml:id="jt">Joan Trash</role>
      <roleDesc>A Ginger-bread-woman</roleDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-role-egXML-ke">
      <role xml:id="fr_pr">Le professeur Rubeck</role>
      <roleDesc>sculpteur</roleDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-role-egXML-zr" source="#biblzh-tw_n35-36">
      <role xml:id="zh-tw_王">鄧肯</role>
      <roleDesc>蘇格蘭國王</roleDesc>
    </egXML>
  </exemplum>
  <remarks ident="role-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>It is important to assign a meaningful ID attribute to the <gi>role</gi> element, since this
      ID is referred to by <att>who</att> attributes on many other elements.</p>
  </remarks>
  <remarks ident="role-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Il est important de fournir un identifiant signifiant pour
    l'attribut <att>xml:id</att> de l'élément <gi>role</gi> :
    l'identifiant donné sera utilisé pour renseigner l'attribut
    <att>who</att> de nombreux autres éléments, et faire ainsi
    référence à l'élément <gi>role</gi>.</p>
  </remarks>
  <remarks ident="role-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>role</gi>の属性IDに有意義な値を付与することが重要である。 この属性IDの値は、他の要素にある属性<att>who</att>から参照される。 </p>
  </remarks>
  <listRef>
    <ptr target="#DRCAST" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">role</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">rôle</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains the name of a dramatic role, as given in a cast list.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">배역 목록에 제시되는 드라마 배역의 이름</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">角色名單所列的劇中角色名稱。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">el nombre de un papel dramático, según los dados en el
    reparto.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">配役リスト中にある、役名を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">le nom d'un rôle au théâtre tel qu’il est donné dans la
    distribution.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">il nome di un ruolo teatrale, secondo la lista dei
    personaggi.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
    <memberOf key="model.castItemPart"/>
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
<desc versionDate="2023-03-11" xml:lang="en">specifies the gender of the role.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="role-attr.gender-remarks" versionDate="2023-03-11" xml:lang="en">
        <p>Values for this attribute may be locally defined by a project, or they may refer to an external standard.</p>
      </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-role-egXML-rl" source="#JonsBart">
      <role xml:id="jt">Joan Trash</role>
      <roleDesc>A Ginger-bread-woman</roleDesc>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-role-egXML-ke">
      <role xml:id="fr_pr">Le professeur Rubeck</role>
      <roleDesc>sculpteur</roleDesc>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-role-egXML-zr" source="#biblzh-tw_n35-36">
      <role xml:id="zh-tw_王">鄧肯</role>
      <roleDesc>蘇格蘭國王</roleDesc>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="role-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>It is important to assign a meaningful ID attribute to the <gi>role</gi> element, since this
      ID is referred to by <att>who</att> attributes on many other elements.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="role-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Il est important de fournir un identifiant signifiant pour
    l'attribut <att>xml:id</att> de l'élément <gi>role</gi> :
    l'identifiant donné sera utilisé pour renseigner l'attribut
    <att>who</att> de nombreux autres éléments, et faire ainsi
    référence à l'élément <gi>role</gi>.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="role-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>role</gi>の属性IDに有意義な値を付与することが重要である。 この属性IDの値は、他の要素にある属性<att>who</att>から参照される。 </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRCAST" type="div3"/>
  </listRef>
```

^b21

