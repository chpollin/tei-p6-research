---
type: representation
source-type: document
source: '[[00_sources/tei-p5-catdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 catDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/catDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# catDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5821. Git blob: `7d0652d34b2eb7030c02b0ea2b2a37af38d7ec8c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-catDesc" ident="catDesc">
  <gloss versionDate="2005-01-14" xml:lang="en">category description</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">Description de la catégorie</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">범주 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">類目描述</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Beschreibung der Kategorie</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción de una categoría</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione della categoria</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">分類の記述</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes some category within a taxonomy or text typology, either in the form of a brief
    prose description or in terms of the situational parameters used by the TEI formal <gi>textDesc</gi>.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit une catégorie particulière à l’intérieur d’une
    taxinomie ou d’une typologie de texte, sous forme d’un court texte descriptif suivi ou dans les
    termes des paramètres contextuels utilisés dans l’élément Description du texte
    <gi>textDesc</gi>.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">간단한 산문체 기술 형식 또는 TEI의 형식적 텍스트 기술에 의해 사용된 상황 매개변수를 통해 분류법
    또는 텍스트 유형 내에서 어떤 범주를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述分類法中或文件類型學中的某些類目，可用短文描述的型式，或是用TEI正式元素<gi>textDesc</gi>所使用的狀況參數。</desc>
  <desc versionDate="2023-10-02" xml:lang="ja">テキスト分類や分類法における分類項目を示す。簡単な散文形式またはTEIの<gi>textDesc</gi>で使用される形式化された状況パラメータで示される。</desc>
  <desc versionDate="2016-11-25" xml:lang="de">beschreibt eine Kategorie innerhalb einer Taxonomie oder Texttypologie, 
    entweder als einfacher Fließtext oder über kontextbezogene Parameter, mittels des strukturierten <gi>textDesc</gi>-Elements.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe alguna categoría dentro de una taxonomía o
    tipología textual, a través de una breve e descripción en prosa o en términos de parámetros
    situacionales usados por el <gi>textDesc</gi> formal de TEI.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive una categoria all'interno di una tassonomia o
    tipologia di testo, sotto forma di una breve descrizione in prosa o secondo i parametri
    situazionali usati in modo formale dall'elemento TEI <gi>textDesc</gi>.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.limitedPhrase"/>
        <classRef key="model.catDescPart"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-uc">
      <catDesc>Prose reportage</catDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-pq">
      <catDesc>Texte documentaire</catDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-we">
      <category>
        <catDesc>genre</catDesc>
        <category>
          <catDesc>Géneral</catDesc>
        </category>
        <category>
          <catDesc>Journal</catDesc>
        </category>
        <category>
          <catDesc>Manuel technique</catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-uy">
      <catDesc>報導文學</catDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-yc">
      <catDesc>
        <textDesc n="novel">
          <channel mode="w">出版品；專輯</channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepared"/>
          <purpose type="entertain" degree="high"/>
          <purpose type="inform" degree="medium"/>
        </textDesc>
      </catDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-bz">
      <catDesc>
        <textDesc n="novel">
          <channel mode="w">print; part issues</channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepared"/>
          <purpose type="entertain" degree="high"/>
          <purpose type="inform" degree="medium"/>
        </textDesc>
      </catDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD55"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">category description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">Description de la catégorie</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">범주 기술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">類目描述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Beschreibung der Kategorie</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción de una categoría</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione della categoria</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">分類の記述</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes some category within a taxonomy or text typology, either in the form of a brief
    prose description or in terms of the situational parameters used by the TEI formal <gi>textDesc</gi>.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit une catégorie particulière à l’intérieur d’une
    taxinomie ou d’une typologie de texte, sous forme d’un court texte descriptif suivi ou dans les
    termes des paramètres contextuels utilisés dans l’élément Description du texte
    <gi>textDesc</gi>.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">간단한 산문체 기술 형식 또는 TEI의 형식적 텍스트 기술에 의해 사용된 상황 매개변수를 통해 분류법
    또는 텍스트 유형 내에서 어떤 범주를 기술한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述分類法中或文件類型學中的某些類目，可用短文描述的型式，或是用TEI正式元素<gi>textDesc</gi>所使用的狀況參數。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2023-10-02" xml:lang="ja">テキスト分類や分類法における分類項目を示す。簡単な散文形式またはTEIの<gi>textDesc</gi>で使用される形式化された状況パラメータで示される。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">beschreibt eine Kategorie innerhalb einer Taxonomie oder Texttypologie, 
    entweder als einfacher Fließtext oder über kontextbezogene Parameter, mittels des strukturierten <gi>textDesc</gi>-Elements.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe alguna categoría dentro de una taxonomía o
    tipología textual, a través de una breve e descripción en prosa o en términos de parámetros
    situacionales usados por el <gi>textDesc</gi> formal de TEI.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive una categoria all'interno di una tassonomia o
    tipologia di testo, sotto forma di una breve descrizione in prosa o secondo i parametri
    situazionali usati in modo formale dall'elemento TEI <gi>textDesc</gi>.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.limitedPhrase"/>
        <classRef key="model.catDescPart"/>
      </alternate>
    
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-uc">
      <catDesc>Prose reportage</catDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-pq">
      <catDesc>Texte documentaire</catDesc>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-we">
      <category>
        <catDesc>genre</catDesc>
        <category>
          <catDesc>Géneral</catDesc>
        </category>
        <category>
          <catDesc>Journal</catDesc>
        </category>
        <category>
          <catDesc>Manuel technique</catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-uy">
      <catDesc>報導文學</catDesc>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-yc">
      <catDesc>
        <textDesc n="novel">
          <channel mode="w">出版品；專輯</channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepared"/>
          <purpose type="entertain" degree="high"/>
          <purpose type="inform" degree="medium"/>
        </textDesc>
      </catDesc>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-catDesc-egXML-bz">
      <catDesc>
        <textDesc n="novel">
          <channel mode="w">print; part issues</channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepared"/>
          <purpose type="entertain" degree="high"/>
          <purpose type="inform" degree="medium"/>
        </textDesc>
      </catDesc>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD55"/>
  </listRef>
```

^b25

