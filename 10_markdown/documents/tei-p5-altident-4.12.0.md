---
type: representation
source-type: document
source: '[[00_sources/tei-p5-altident-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 altIdent
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/altIdent.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# altIdent

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4000. Git blob: `39717250d467e517b0cd63425a0db092f8c2b8f7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="ALTIDENT" ident="altIdent">
  <gloss versionDate="2007-07-04" xml:lang="en">alternate identifier</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">교체 확인소</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">identificador alterno</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">identifiant alternatif</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">identificatore alternativo</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">代替識別子</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">supplies the recommended XML name for an element, class,
  attribute, etc. in some language.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 언어에서 요소, 부류, 속성에 대해 권고된 XML 이름을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標誌用另一種語言來表示的XML元素、元素集、屬性等的名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">特定言語において、XMLの要素、クラス、属性などで推奨される名前を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit le nom XML
  recommandé pour un élément, une classe, un attribut, etc. dans un
  langage quelconque.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre
  XML recomendado para un elemento, clase, atributo, etc. en alguna
  lengua.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome XML
  consigliato per un elemento, classe, attributo, ecc. in una
  lingua.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.identSynonyms"/>
  </classes>
  <content>
    <dataRef name="NCName"/>  <!-- key=teidata.xmlName creates bad DTD, see https://github.com/TEIC/Stylesheets/issues/569  —Syd, 2022-12-07 -->
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENT-egXML-qo" source="#NONE">
      <altIdent xml:lang="fr">balisageDoc</altIdent>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENT-egXML-fy" source="#NONE">
      <altIdent xml:lang="fr">balisageDoc</altIdent>
    </egXML>
  </exemplum>
  <remarks ident="altIdent-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>All documentation elements in ODD have a canonical name,
    supplied as the value for their <att>ident</att> attribute. The
    <gi>altIdent</gi> element is used to supply an alternative name
    for the corresponding XML object, perhaps in a different
    language.</p>
  </remarks>
  <remarks ident="altIdent-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Tous les éléments de documentation en ODD ont un nom canonique
    fourni comme valeur de leur attribut <att>ident</att>. L'élément
    <gi>altIdent</gi> est utilisé pour apporter un nom alternatif à
    l'objet XML correspondant, éventuellement dans un langage
    différent.</p>
  </remarks>
  <remarks ident="altIdent-remarks" versionDate="2018-12-28" xml:lang="ja">
    <p>ODDのすべてのドキュメント要素には、<att>ident</att>属性の値とし
    て提供される標準名がある。<gi>altIdent</gi>要素は、例えば異なる言
    語で、対応するXMLオブジェクトの代替名を提供するために使用される。
    </p>
  </remarks>
  <listRef>
    <ptr target="#COHTG"/>
    <ptr target="#TDcrystalsCEdc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">alternate identifier</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">교체 확인소</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">identificador alterno</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">identifiant alternatif</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">identificatore alternativo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">代替識別子</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies the recommended XML name for an element, class,
  attribute, etc. in some language.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 언어에서 요소, 부류, 속성에 대해 권고된 XML 이름을 제시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標誌用另一種語言來表示的XML元素、元素集、屬性等的名稱。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">特定言語において、XMLの要素、クラス、属性などで推奨される名前を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit le nom XML
  recommandé pour un élément, une classe, un attribut, etc. dans un
  langage quelconque.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre
  XML recomendado para un elemento, clase, atributo, etc. en alguna
  lengua.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome XML
  consigliato per un elemento, classe, attributo, ecc. in una
  lingua.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.identSynonyms"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <dataRef name="NCName"/>  <!-- key=teidata.xmlName creates bad DTD, see https://github.com/TEIC/Stylesheets/issues/569  —Syd, 2022-12-07 -->
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENT-egXML-qo" source="#NONE">
      <altIdent xml:lang="fr">balisageDoc</altIdent>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENT-egXML-fy" source="#NONE">
      <altIdent xml:lang="fr">balisageDoc</altIdent>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="altIdent-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>All documentation elements in ODD have a canonical name,
    supplied as the value for their <att>ident</att> attribute. The
    <gi>altIdent</gi> element is used to supply an alternative name
    for the corresponding XML object, perhaps in a different
    language.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="altIdent-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Tous les éléments de documentation en ODD ont un nom canonique
    fourni comme valeur de leur attribut <att>ident</att>. L'élément
    <gi>altIdent</gi> est utilisé pour apporter un nom alternatif à
    l'objet XML correspondant, éventuellement dans un langage
    différent.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="altIdent-remarks" versionDate="2018-12-28" xml:lang="ja">
    <p>ODDのすべてのドキュメント要素には、<att>ident</att>属性の値とし
    て提供される標準名がある。<gi>altIdent</gi>要素は、例えば異なる言
    語で、対応するXMLオブジェクトの代替名を提供するために使用される。
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHTG"/>
    <ptr target="#TDcrystalsCEdc"/>
  </listRef>
```

^b21

