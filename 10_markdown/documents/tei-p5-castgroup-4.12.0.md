---
type: representation
source-type: document
source: '[[00_sources/tei-p5-castgroup-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 castGroup
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/castGroup.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# castGroup

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5654. Git blob: `fe4d19113b53d2d322b3898471200e2c0b64697e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-castGroup" ident="castGroup">
  <gloss versionDate="2007-07-04" xml:lang="en">cast list grouping</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">배역 목록 모아 놓기</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">角色群組</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">grupo de reparto</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">liste de personnages</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">raggruppamento della lista dei personaggi</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">配役リスト内グループ</gloss>
  <desc versionDate="2017-02-07" xml:lang="en">groups one or more individual <gi>castItem</gi>
elements within a cast list.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">배역 목록 내의 몇 개의 개별 castItem 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集角色清單中一個或多個角色項目元素。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">agrupa uno o más elementos individuales del reparto (castItem).</desc>
  <desc versionDate="2023-10-02" xml:lang="ja">配役リストにある、ひとつ以上の<gi>castItem</gi>要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">dans une distribution, catégorie qui rassemble un ou
      plusieurs personnages.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa uno o più elementi individuali castItem in una lista dei personaggi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <classRef key="model.headLike"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate>
          <elementRef key="castItem"/>
          <elementRef key="castGroup"/>
          <elementRef key="roleDesc"/>
        </alternate>
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
      <sequence minOccurs="0">
        <elementRef key="trailer"/>
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castGroup-egXML-mx" source="#DRCAST-eg-21">
      <castGroup rend="braced">
        <castItem>
          <role>Walter</role>
          <actor>Mr Frank Hall</actor>
        </castItem>
        <castItem>
          <role>Hans</role>
          <actor>Mr F.W. Irish</actor>
        </castItem>
        <roleDesc>friends of Mathias</roleDesc>
      </castGroup>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castGroup-egXML-dw" source="#fr-ex-Guerre-Troie">
      <castGroup>
        <head>Messagers</head>
        <castItem><actor>Jean-Claude Islert</actor>, <actor>Michel Sausin</actor>.</castItem>
      </castGroup>
      <castGroup>
        <head>Servantes troyennes</head>
        <castItem><actor>Dominique Jayr</actor>, <actor>Annie Seurat</actor>,<actor> Hélène
            Augier</actor></castItem>
      </castGroup>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castGroup-egXML-wt" source="#biblzh-tw_n30-31">
      <castGroup rend="braced">
        <castItem>
          <role>程蝶衣</role>
          <actor>張國榮</actor>
        </castItem>
        <castItem>
          <role>菊仙</role>
          <actor>鞏俐</actor>
        </castItem>
        <roleDesc>原是妓女，後嫁段小樓為妻</roleDesc>
      </castGroup>
    </egXML>
  </exemplum>
  <remarks ident="castGroup-remarks" versionDate="2008-02-01" xml:lang="en">
    <p>The <att>rend</att> attribute may be used, as here, to indicate
whether the grouping is indicated by a brace, whitespace, font change,
etc. </p>
    <p>Note that in this example the role description <q>friends of
Mathias</q> is understood to apply to both roles equally. </p>
  </remarks>
  <remarks ident="castGroup-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>rend</att> peut être utilisé comme ici pour indiquer si le
                regroupement est indiqué par une parenthèse, un espace, un changement de police de caractère,
                etc. </p>
    <p>À noter que dans cet exemple il est entendu que la description du rôle <q>friends of
                    Mathias</q> (amis de Mathias) s'applique de la même façon aux deux rôles.</p>
  </remarks>
  <remarks ident="castGroup-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>rend</att>は、当該グループが括弧、空白、字形の違いなどで
    示されていることを示す。
    </p>
    <p>
    この例では、役に関する情報<q>friends of Mathias</q>は、2つの役に同
    じく当てはまると理解される。
    </p>
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
<gloss versionDate="2007-07-04" xml:lang="en">cast list grouping</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">배역 목록 모아 놓기</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">角色群組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">grupo de reparto</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">liste de personnages</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">raggruppamento della lista dei personaggi</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">配役リスト内グループ</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">groups one or more individual <gi>castItem</gi>
elements within a cast list.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">배역 목록 내의 몇 개의 개별 castItem 요소를 모아 놓는다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集角色清單中一個或多個角色項目元素。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">agrupa uno o más elementos individuales del reparto (castItem).</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2023-10-02" xml:lang="ja">配役リストにある、ひとつ以上の<gi>castItem</gi>要素をまとめる。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">dans une distribution, catégorie qui rassemble un ou
      plusieurs personnages.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa uno o più elementi individuali castItem in una lista dei personaggi.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.performed"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <classRef key="model.headLike"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate>
          <elementRef key="castItem"/>
          <elementRef key="castGroup"/>
          <elementRef key="roleDesc"/>
        </alternate>
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
      <sequence minOccurs="0">
        <elementRef key="trailer"/>
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castGroup-egXML-mx" source="#DRCAST-eg-21">
      <castGroup rend="braced">
        <castItem>
          <role>Walter</role>
          <actor>Mr Frank Hall</actor>
        </castItem>
        <castItem>
          <role>Hans</role>
          <actor>Mr F.W. Irish</actor>
        </castItem>
        <roleDesc>friends of Mathias</roleDesc>
      </castGroup>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castGroup-egXML-dw" source="#fr-ex-Guerre-Troie">
      <castGroup>
        <head>Messagers</head>
        <castItem><actor>Jean-Claude Islert</actor>, <actor>Michel Sausin</actor>.</castItem>
      </castGroup>
      <castGroup>
        <head>Servantes troyennes</head>
        <castItem><actor>Dominique Jayr</actor>, <actor>Annie Seurat</actor>,<actor> Hélène
            Augier</actor></castItem>
      </castGroup>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-castGroup-egXML-wt" source="#biblzh-tw_n30-31">
      <castGroup rend="braced">
        <castItem>
          <role>程蝶衣</role>
          <actor>張國榮</actor>
        </castItem>
        <castItem>
          <role>菊仙</role>
          <actor>鞏俐</actor>
        </castItem>
        <roleDesc>原是妓女，後嫁段小樓為妻</roleDesc>
      </castGroup>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="castGroup-remarks" versionDate="2008-02-01" xml:lang="en">
    <p>The <att>rend</att> attribute may be used, as here, to indicate
whether the grouping is indicated by a brace, whitespace, font change,
etc. </p>
    <p>Note that in this example the role description <q>friends of
Mathias</q> is understood to apply to both roles equally. </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="castGroup-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>rend</att> peut être utilisé comme ici pour indiquer si le
                regroupement est indiqué par une parenthèse, un espace, un changement de police de caractère,
                etc. </p>
    <p>À noter que dans cet exemple il est entendu que la description du rôle <q>friends of
                    Mathias</q> (amis de Mathias) s'applique de la même façon aux deux rôles.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="castGroup-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>rend</att>は、当該グループが括弧、空白、字形の違いなどで
    示されていることを示す。
    </p>
    <p>
    この例では、役に関する情報<q>friends of Mathias</q>は、2つの役に同
    じく当てはまると理解される。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRCAST" type="div3"/>
  </listRef>
```

^b23

