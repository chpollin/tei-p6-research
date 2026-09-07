---
type: representation
source-type: document
source: '[[00_sources/tei-p5-rolename-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 roleName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/roleName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# roleName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5073. Git blob: `f49e3e9d9d9e37a28580038c485c856ec3899b95`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-roleName" ident="roleName">
  <gloss versionDate="2020-12-20" xml:lang="en">role name</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">rôle</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a name component which indicates that the referent has a particular role or position in society, such as an official title or
        rank.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">공식적 직함 또는 서열과 같이 사회에서 특별한 역할 또는 지위를 나타내는 이름 성분을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個身份名稱，代表個人在社會上所扮演的特殊角色或所處地位，例如官方頭銜或地位。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">参照されるものの、社会的な役割や地位、例えば、公式な役職名や地位など を示す、名前要素を示す</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient un composant du nom d'une personne, indiquant que celle-ci a un rôle ou une position
        particulière dans la société, comme un titre ou un rang officiel.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un componente del nombre que indica un rol o una posición específica a nivel social, como en el
        caso de títulos oficiales o de grado militar.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una componente del nome che indica un ruolo o una posizione specifici a livello sociale, come
        nel caso di titoli ufficiali o grado militare</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persNamePart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-ng">
      <persName>
        <forename>William</forename>
        <surname>Poulteny</surname>
        <roleName>Earl of Bath</roleName>
      </persName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-cp">
      <persName><forename>Joachim</forename><surname>Murat</surname>, <roleName>roi de Naples</roleName></persName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-na">
      <persName>
        <forename>溥儀</forename>
        <surname>愛新覺羅</surname>
        <roleName>滿清末代皇帝</roleName>
      </persName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2019-07-15" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-cc">
      <p>The <roleName role="solicitor_general">S.G.</roleName> is the only national public official,
      including the Supreme Court justices, required by statute to be “learned in the law.”</p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2019-07-15" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-ge">
      <p><persName ref="#NJF"><roleName role="solicitor_general">Solicitor General</roleName> Noel J. Francisco</persName>,
      representing the administration, asserted in rebuttal that there was nothing to disavow (...)
      <persName ref="#NJF">Francisco</persName> had violated the scrupulous standard of candor about the facts and
      the law that <roleName role="solicitor_general">S.G.s</roleName>, in Republican and Democratic administrations
      alike, have repeatedly said they must honor.</p>
    </egXML>
  </exemplum>
  <remarks ident="roleName-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A <gi>roleName</gi> may be distinguished from an <gi>addName</gi> by virtue of the fact that, like a title, it typically exists
            independently of its holder.</p>
  </remarks>
  <remarks ident="roleName-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p>Un élément <gi>roleName</gi> peut être distingué d'un élément <gi>addName</gi> du fait que, à l'instar d'un titre, il existe en général
            indépendamment de la personne qui le porte.</p>
  </remarks>
  <remarks ident="roleName-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>roleName</gi>は、役職名などはその当事者とは独立してあるも のであることから、要素<gi>addName</gi>とは異なっている。 </p>
  </remarks>
  <listRef>
    <ptr target="#NDPER"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">role name</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">rôle</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a name component which indicates that the referent has a particular role or position in society, such as an official title or
        rank.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">공식적 직함 또는 서열과 같이 사회에서 특별한 역할 또는 지위를 나타내는 이름 성분을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個身份名稱，代表個人在社會上所扮演的特殊角色或所處地位，例如官方頭銜或地位。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">参照されるものの、社会的な役割や地位、例えば、公式な役職名や地位など を示す、名前要素を示す</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient un composant du nom d'une personne, indiquant que celle-ci a un rôle ou une position
        particulière dans la société, comme un titre ou un rang officiel.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un componente del nombre que indica un rol o una posición específica a nivel social, como en el
        caso de títulos oficiales o de grado militar.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una componente del nome che indica un ruolo o una posizione specifici a livello sociale, come
        nel caso di titoli ufficiali o grado militare</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persNamePart"/>
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

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-ng">
      <persName>
        <forename>William</forename>
        <surname>Poulteny</surname>
        <roleName>Earl of Bath</roleName>
      </persName>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-cp">
      <persName><forename>Joachim</forename><surname>Murat</surname>, <roleName>roi de Naples</roleName></persName>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-na">
      <persName>
        <forename>溥儀</forename>
        <surname>愛新覺羅</surname>
        <roleName>滿清末代皇帝</roleName>
      </persName>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2019-07-15" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-cc">
      <p>The <roleName role="solicitor_general">S.G.</roleName> is the only national public official,
      including the Supreme Court justices, required by statute to be “learned in the law.”</p>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum versionDate="2019-07-15" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-roleName-egXML-ge">
      <p><persName ref="#NJF"><roleName role="solicitor_general">Solicitor General</roleName> Noel J. Francisco</persName>,
      representing the administration, asserted in rebuttal that there was nothing to disavow (...)
      <persName ref="#NJF">Francisco</persName> had violated the scrupulous standard of candor about the facts and
      the law that <roleName role="solicitor_general">S.G.s</roleName>, in Republican and Democratic administrations
      alike, have repeatedly said they must honor.</p>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="roleName-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A <gi>roleName</gi> may be distinguished from an <gi>addName</gi> by virtue of the fact that, like a title, it typically exists
            independently of its holder.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="roleName-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p>Un élément <gi>roleName</gi> peut être distingué d'un élément <gi>addName</gi> du fait que, à l'instar d'un titre, il existe en général
            indépendamment de la personne qui le porte.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="roleName-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>roleName</gi>は、役職名などはその当事者とは独立してあるも のであることから、要素<gi>addName</gi>とは異なっている。 </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPER"/>
  </listRef>
```

^b20

