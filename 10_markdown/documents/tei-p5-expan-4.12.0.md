---
type: representation
source-type: document
source: '[[00_sources/tei-p5-expan-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 expan
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/expan.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# expan

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5067. Git blob: `8476a4eda1c17a134e76874ad7321c178b2b8c58`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-expan" ident="expan">
  <gloss versionDate="2005-01-14" xml:lang="en">expansion</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">확장 표기</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">縮寫還原</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">expansion</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">expansión</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">espansione</gloss>
    <gloss versionDate="2016-11-25" xml:lang="de">Abkürzungsauflösung</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the expansion of an abbreviation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">약어의 확장(비약어) 표기</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個縮寫詞的還原形式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">省略形の元の表現を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient l'expansion d'une abréviation.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la expansión de una abreviatura.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene l'esapnsione di un'abbreviazione.</desc>
    <desc versionDate="2016-11-25" xml:lang="de">enthält die aufgelöste Form einer Abkürzung.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-expan-egXML-se">The address is Southmoor 
        <choice>
            <expan>Road</expan>
            <abbr>Rd</abbr>
        </choice>
      </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-expan-egXML-yv">Il habite
        <choice>
            <expan>Avenue</expan>
            <abbr>Av.</abbr>
        </choice>de la Paix 
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-expan-egXML-dd">
      <choice>
        <expan>歐洲聯盟</expan>
        <abbr>歐盟</abbr>
      </choice>
    </egXML>
  </exemplum>
  <exemplum versionDate="2016-08-12" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-expan-egXML-or" xml:lang="la">
      <choice xml:lang="la">
        <abbr>Imp</abbr>
        <expan>Imp<ex>erator</ex></expan>
      </choice> 
    </egXML>
  </exemplum>
  <remarks ident="expan-remarks" versionDate="2017-11-17" xml:lang="en">
      <p>The content of this element should be the expanded
      abbreviation, usually (but not always) a complete word or
      phrase. The <gi>ex</gi> element provided by the <ident type="module">transcr</ident> module may be used to mark up
      sequences of letters supplied within such an expansion.</p>
    
    <p>If abbreviations are expanded silently, this practice should be
      documented in the <gi>editorialDecl</gi>, either with a
      <gi>normalization</gi> element or a <gi>p</gi>.</p>
  </remarks>
  <remarks ident="expan-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>En général, le contenu de cet élément doit être une expression ou un mot complet. L'élément
        <gi>ex</gi> fourni par le module <ident type="module">transcr</ident> peut être utilisé pour
      baliser des suites de lettres données dans une expansion de ce type.</p>
  </remarks>
  <remarks ident="expan-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素の内容は、完全な語句であるべきである。 <ident type="module">転記モジュール</ident>にある要素<gi>ex</gi>
      を使い、省略形の元の形を文字列として示すことができる。 </p>
  </remarks>
  <remarks ident="expan-remarks" versionDate="2017-11-18" xml:lang="de">
      <p>Der Inhalt dieses Elements sollte die aufgelöste Abkürzung sein, üblicherweise ein vollständiges Wort oder eine Phrase. 
          Das <gi>ex</gi>-Element aus dem Modul <ident type="module">transcr</ident> 
          kann verwendet werden, um einzelne Buchstaben innerhalb der Auflösung auszuzeichnen.  </p>
    <p>Werden Abkürzungen stillschweigend aufgelöst, 
      sollte diese Vorgehensweise im TEI-Header über das <gi>editorialDecl</gi>-Element dokumentiert werden, 
      entweder in einem <gi>normalization</gi>- oder einem <gi>p</gi>-Element.</p>
  </remarks>
  <listRef>
    <ptr target="#CONAAB" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">expansion</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">확장 표기</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">縮寫還原</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">expansion</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">expansión</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">espansione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Abkürzungsauflösung</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the expansion of an abbreviation.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">약어의 확장(비약어) 표기</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個縮寫詞的還原形式。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">省略形の元の表現を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient l'expansion d'une abréviation.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la expansión de una abreviatura.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene l'esapnsione di un'abbreviazione.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">enthält die aufgelöste Form einer Abkürzung.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-expan-egXML-se">The address is Southmoor 
        <choice>
            <expan>Road</expan>
            <abbr>Rd</abbr>
        </choice>
      </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-expan-egXML-yv">Il habite
        <choice>
            <expan>Avenue</expan>
            <abbr>Av.</abbr>
        </choice>de la Paix 
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-expan-egXML-dd">
      <choice>
        <expan>歐洲聯盟</expan>
        <abbr>歐盟</abbr>
      </choice>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2016-08-12" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-expan-egXML-or" xml:lang="la">
      <choice xml:lang="la">
        <abbr>Imp</abbr>
        <expan>Imp<ex>erator</ex></expan>
      </choice> 
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="expan-remarks" versionDate="2017-11-17" xml:lang="en">
      <p>The content of this element should be the expanded
      abbreviation, usually (but not always) a complete word or
      phrase. The <gi>ex</gi> element provided by the <ident type="module">transcr</ident> module may be used to mark up
      sequences of letters supplied within such an expansion.</p>
    
    <p>If abbreviations are expanded silently, this practice should be
      documented in the <gi>editorialDecl</gi>, either with a
      <gi>normalization</gi> element or a <gi>p</gi>.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="expan-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>En général, le contenu de cet élément doit être une expression ou un mot complet. L'élément
        <gi>ex</gi> fourni par le module <ident type="module">transcr</ident> peut être utilisé pour
      baliser des suites de lettres données dans une expansion de ce type.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="expan-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素の内容は、完全な語句であるべきである。 <ident type="module">転記モジュール</ident>にある要素<gi>ex</gi>
      を使い、省略形の元の形を文字列として示すことができる。 </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="expan-remarks" versionDate="2017-11-18" xml:lang="de">
      <p>Der Inhalt dieses Elements sollte die aufgelöste Abkürzung sein, üblicherweise ein vollständiges Wort oder eine Phrase. 
          Das <gi>ex</gi>-Element aus dem Modul <ident type="module">transcr</ident> 
          kann verwendet werden, um einzelne Buchstaben innerhalb der Auflösung auszuzeichnen.  </p>
    <p>Werden Abkürzungen stillschweigend aufgelöst, 
      sollte diese Vorgehensweise im TEI-Header über das <gi>editorialDecl</gi>-Element dokumentiert werden, 
      entweder in einem <gi>normalization</gi>- oder einem <gi>p</gi>-Element.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONAAB" type="div3"/>
  </listRef>
```

^b26

