---
type: representation
source-type: document
source: '[[00_sources/tei-p5-catref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 catRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/catRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# catRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6816. Git blob: `6b238f8a90586d1b5562b0b68e3a417b4ad0c690`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-catRef" ident="catRef">
  <gloss versionDate="2005-01-14" xml:lang="en">category reference</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">référence à la catégorie</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">범주 참조</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">類目參照</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Verweis auf eine Kategorie</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">referencia de categoría</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">riferimento alla categoria</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">分類の参照</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies one or more defined categories within some taxonomy or text typology.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">spécifie une ou plusieurs catégories définies dans une
    taxinomie ou une typologie textuelle.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">분류법 또는 텍스트 유형 내에서 하나 이상의 정의된 범주를 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明在某分類法或文件類型學中，一個或多個已定義之類目。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">分類法やテキスト分類中の、ひとつ以上の分類項目を定義する。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">gibt eine oder mehrere Kategorien an, die innerhalb einer
    Taxonomie oder Texttypologie definiert sind.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica una o más categorías definidas al interno de una
    taxonomía o tipología textual.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica una o più categorie definite all'interno di una
    tassonomia o tipologia di testo</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.pointing"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="scheme" usage="opt">
      <desc versionDate="2013-12-20" xml:lang="en">identifies the classification scheme within which the set of categories concerned is
        defined, for example by a <gi>taxonomy</gi> element, or by
      some other resource.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">identifie le schéma de classification dans lequel est
        défini le jeu de catégories concerné.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">관련 범주 집합이 정의된 분류 스키마를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明該分類架構，其中相關的類目群組已被定義</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">たとえば<gi>taxonomy</gi>要素あるいはその他の資料によって、当該分類項目が定義されている分類スキームを同定する。</desc>
        <desc versionDate="2016-11-24" xml:lang="de">gibt das Klassifikationsschema an, in dem die entsprechenden Kategorien definiert sind, 
            z. B. über ein <gi>taxonomy</gi>-Element oder eine andere Ressource.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el esquema de clasificación al interno del
        cual se define una serie de categorias referidas.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica lo schema di classificazione all'interno
        del quale sono definite le categorie interessate.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum versionDate="2013-12-20" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catRef-egXML-ju">
      <catRef scheme="#myTopics" target="#news #prov #sales2"/>
      <!-- elsewhere -->
      <taxonomy xml:id="myTopics">
        <category xml:id="news">
          <catDesc>Newspapers</catDesc>
        </category>
        <category xml:id="prov">
          <catDesc>Provincial</catDesc>
        </category>
        <category xml:id="sales2">
          <catDesc>Low to average annual sales</catDesc>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
  <exemplum versionDate="2013-12-20" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catRef-egXML-gd">
      <catRef scheme="#mesTopos" target="#fr_lex #fr_dict #fr_gloss"/>
      <!-- ailleurs dans le document -->
      <taxonomy xml:id="mesTopos">
        <category xml:id="fr_lexique">
          <catDesc>Lexique</catDesc>
        </category>
        <category xml:id="fr_dict">
          <catDesc>Dictionnaire</catDesc>
        </category>
        <category xml:id="fr_gloss">
          <catDesc>Glossaire</catDesc>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catRef-egXML-me">
      <catRef target="#zh-tw_news #zh-tw_prov #zh-tw_sales2"/>
      <!-- elsewhere -->
      <taxonomy>
        <category xml:id="zh-tw_news">
          <catDesc>報紙</catDesc>
        </category>
        <category xml:id="zh-tw_prov">
          <catDesc>全省的</catDesc>
        </category>
        <category xml:id="zh-tw_sales2">
          <catDesc>低於每年平均銷售額</catDesc>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
  <remarks ident="catRef-remarks" versionDate="2016-11-04" xml:lang="en">
    <p>The <att>scheme</att> attribute needs to be supplied only if more than one
    taxonomy has been declared. </p>
  </remarks>
  <remarks ident="catRef-remarks" versionDate="2016-11-04" xml:lang="fr">
    <p>L'attribut <att>scheme</att> n'est donné que si plus d'une taxinomie a été déclarée.</p>
  </remarks>
  <remarks ident="catRef-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>El atributo del esquema necesita ser suministrado solamente si se ha declarado más de una
      taxonomía</p>
  </remarks>
  <remarks ident="catRef-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p><att>scheme</att>属性は、複数の分類法が宣言されている場合にのみ、必要となる。</p>
  </remarks>
  <remarks ident="catRef-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>Das <att>scheme</att>-Attribut muss nur dann verwendet werden, wenn mehr als eine Taxonomie deklariert ist.</p>
  </remarks>
  <listRef>
    <ptr target="#HD43"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">category reference</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">référence à la catégorie</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">범주 참조</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">類目參照</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Verweis auf eine Kategorie</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">referencia de categoría</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">riferimento alla categoria</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">分類の参照</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies one or more defined categories within some taxonomy or text typology.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">spécifie une ou plusieurs catégories définies dans une
    taxinomie ou une typologie textuelle.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">분류법 또는 텍스트 유형 내에서 하나 이상의 정의된 범주를 명시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明在某分類法或文件類型學中，一個或多個已定義之類目。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">分類法やテキスト分類中の、ひとつ以上の分類項目を定義する。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt eine oder mehrere Kategorien an, die innerhalb einer
    Taxonomie oder Texttypologie definiert sind.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica una o más categorías definidas al interno de una
    taxonomía o tipología textual.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica una o più categorie definite all'interno di una
    tassonomia o tipologia di testo</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.pointing"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-20" xml:lang="en">identifies the classification scheme within which the set of categories concerned is
        defined, for example by a <gi>taxonomy</gi> element, or by
      some other resource.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">identifie le schéma de classification dans lequel est
        défini le jeu de catégories concerné.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">관련 범주 집합이 정의된 분류 스키마를 표시한다.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明該分類架構，其中相關的類目群組已被定義</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">たとえば<gi>taxonomy</gi>要素あるいはその他の資料によって、当該分類項目が定義されている分類スキームを同定する。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">gibt das Klassifikationsschema an, in dem die entsprechenden Kategorien definiert sind, 
            z. B. über ein <gi>taxonomy</gi>-Element oder eine andere Ressource.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el esquema de clasificación al interno del
        cual se define una serie de categorias referidas.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica lo schema di classificazione all'interno
        del quale sono definite le categorie interessate.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2013-12-20" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catRef-egXML-ju">
      <catRef scheme="#myTopics" target="#news #prov #sales2"/>
      <!-- elsewhere -->
      <taxonomy xml:id="myTopics">
        <category xml:id="news">
          <catDesc>Newspapers</catDesc>
        </category>
        <category xml:id="prov">
          <catDesc>Provincial</catDesc>
        </category>
        <category xml:id="sales2">
          <catDesc>Low to average annual sales</catDesc>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2013-12-20" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catRef-egXML-gd">
      <catRef scheme="#mesTopos" target="#fr_lex #fr_dict #fr_gloss"/>
      <!-- ailleurs dans le document -->
      <taxonomy xml:id="mesTopos">
        <category xml:id="fr_lexique">
          <catDesc>Lexique</catDesc>
        </category>
        <category xml:id="fr_dict">
          <catDesc>Dictionnaire</catDesc>
        </category>
        <category xml:id="fr_gloss">
          <catDesc>Glossaire</catDesc>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catRef-egXML-me">
      <catRef target="#zh-tw_news #zh-tw_prov #zh-tw_sales2"/>
      <!-- elsewhere -->
      <taxonomy>
        <category xml:id="zh-tw_news">
          <catDesc>報紙</catDesc>
        </category>
        <category xml:id="zh-tw_prov">
          <catDesc>全省的</catDesc>
        </category>
        <category xml:id="zh-tw_sales2">
          <catDesc>低於每年平均銷售額</catDesc>
        </category>
      </taxonomy>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="catRef-remarks" versionDate="2016-11-04" xml:lang="en">
    <p>The <att>scheme</att> attribute needs to be supplied only if more than one
    taxonomy has been declared. </p>
  </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="catRef-remarks" versionDate="2016-11-04" xml:lang="fr">
    <p>L'attribut <att>scheme</att> n'est donné que si plus d'une taxinomie a été déclarée.</p>
  </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="catRef-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>El atributo del esquema necesita ser suministrado solamente si se ha declarado más de una
      taxonomía</p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="catRef-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p><att>scheme</att>属性は、複数の分類法が宣言されている場合にのみ、必要となる。</p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="catRef-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>Das <att>scheme</att>-Attribut muss nur dann verwendet werden, wenn mehr als eine Taxonomie deklariert ist.</p>
  </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD43"/>
  </listRef>
```

^b36

