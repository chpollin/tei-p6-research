---
type: representation
source-type: document
source: '[[00_sources/tei-p5-index-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 index
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/index.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# index

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5348. Git blob: `bf027c2627af3a03372133f576d73eab1ac1094a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-index" ident="index">
  <gloss versionDate="2005-01-14" xml:lang="en">index entry</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">색인 표제 항목</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">索引項目</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">entrée d'index</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">entrada de un índice.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it"> voce di indice</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">marks a location to be indexed for whatever purpose.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 목적으로 사용할 수 있도록, 색인된 위치를 표지한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標誌一個因某種目的而被索引的位置。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">索引項目化されたものの場所を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">marque un emplacement à indexer dans un but quelconque.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">marca un punto para ser indexado por cualquier criterio.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segna la posizione da indicizzare per qualsiasi scopo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.spanning"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    
      <sequence minOccurs="0" maxOccurs="unbounded">
        <elementRef key="term"/>
        
          <elementRef key="index" minOccurs="0"/>
        
      </sequence>
    
  </content>
  <attList>
    <attDef ident="indexName" usage="opt">
      <desc versionDate="2012-10-10" xml:lang="en">a single word which follows the rules defining a
        legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>), supplying a name to specify which index (of several) the index entry belongs to.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">색인 표제 항목의 색인을 명시하기 위한 이름을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供該索引項目所屬索引名稱。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">索引項目となったものを特定する名前を示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">donne un nom pour préciser à quel index (parmi
        plusieurs) appartient l'entrée d'index.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un nombre para especificar a qué índice
        (de entre varios) pertence la entrada de íncide.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un nome per specificare a quale indice (o
        indici) la voce di indice appartiene.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
      <remarks ident="index-attr.indexName-remarks" versionDate="2005-06-24" xml:lang="en">
        <p>This attribute makes it possible to create multiple indexes for a text.</p>
      </remarks>
      <remarks ident="index-attr.indexName-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p> Cet attribut permet de créer plusieurs index pour un texte donné. </p>
      </remarks>
      <remarks ident="index-attr.indexName-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性は、複数の索引を作ることができる。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-index-egXML-xl">David's other principal backer, Josiah ha-Kohen
        <index indexName="NAMES"><term>Josiah ha-Kohen b. Azarya</term></index> b. Azarya, son of one of the last gaons of Sura <index indexName="PLACES"><term>Sura</term></index> was David's own first cousin.</egXML>
  </exemplum>
  <exemplum versionDate="2019-03-04" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-index-egXML-qd" source="#fr-ex-Flaubert_Tent"> Ils [les
      onagres] me venaient de mon grand-père maternel, l'empereur Saharil, fils d'Iakhschab, fils d'Iaarab, fils de Kastan <index indexName="NAMES"><term>Saharil</term></index><index indexName="NAMES"><term>Iaarab</term></index><index indexName="NAMES"><term>Kastan</term></index>
      </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-index-egXML-ha"> 道家思想的主要代表家為老子。 <index indexName="NAMES"><term>老子</term></index>姓李名耳，字伯陽，有人說又稱老聃。在傳說中，老子一生下來時，就具有白色的眉毛及鬍子，所以被後來稱為老子。相傳生活在春秋時期。<index indexName="eras"><term>春秋時期</term></index> 著有《道德經》，是中國古代著名思想家。</egXML>
  </exemplum>
  <listRef>
    <ptr target="#CONOIX"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">index entry</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">색인 표제 항목</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">索引項目</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">entrée d'index</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">entrada de un índice.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it"> voce di indice</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks a location to be indexed for whatever purpose.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 목적으로 사용할 수 있도록, 색인된 위치를 표지한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標誌一個因某種目的而被索引的位置。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">索引項目化されたものの場所を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">marque un emplacement à indexer dans un but quelconque.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">marca un punto para ser indexado por cualquier criterio.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segna la posizione da indicizzare per qualsiasi scopo.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.spanning"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <sequence minOccurs="0" maxOccurs="unbounded">
        <elementRef key="term"/>
        
          <elementRef key="index" minOccurs="0"/>
        
      </sequence>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-10-10" xml:lang="en">a single word which follows the rules defining a
        legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>), supplying a name to specify which index (of several) the index entry belongs to.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">색인 표제 항목의 색인을 명시하기 위한 이름을 제시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供該索引項目所屬索引名稱。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">索引項目となったものを特定する名前を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">donne un nom pour préciser à quel index (parmi
        plusieurs) appartient l'entrée d'index.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un nombre para especificar a qué índice
        (de entre varios) pertence la entrada de íncide.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un nome per specificare a quale indice (o
        indici) la voce di indice appartiene.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="index-attr.indexName-remarks" versionDate="2005-06-24" xml:lang="en">
        <p>This attribute makes it possible to create multiple indexes for a text.</p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="index-attr.indexName-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p> Cet attribut permet de créer plusieurs index pour un texte donné. </p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="index-attr.indexName-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性は、複数の索引を作ることができる。 </p>
      </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-index-egXML-xl">David's other principal backer, Josiah ha-Kohen
        <index indexName="NAMES"><term>Josiah ha-Kohen b. Azarya</term></index> b. Azarya, son of one of the last gaons of Sura <index indexName="PLACES"><term>Sura</term></index> was David's own first cousin.</egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2019-03-04" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-index-egXML-qd" source="#fr-ex-Flaubert_Tent"> Ils [les
      onagres] me venaient de mon grand-père maternel, l'empereur Saharil, fils d'Iakhschab, fils d'Iaarab, fils de Kastan <index indexName="NAMES"><term>Saharil</term></index><index indexName="NAMES"><term>Iaarab</term></index><index indexName="NAMES"><term>Kastan</term></index>
      </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-index-egXML-ha"> 道家思想的主要代表家為老子。 <index indexName="NAMES"><term>老子</term></index>姓李名耳，字伯陽，有人說又稱老聃。在傳說中，老子一生下來時，就具有白色的眉毛及鬍子，所以被後來稱為老子。相傳生活在春秋時期。<index indexName="eras"><term>春秋時期</term></index> 著有《道德經》，是中國古代著名思想家。</egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONOIX"/>
  </listRef>
```

^b30

