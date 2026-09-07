---
type: representation
source-type: document
source: '[[00_sources/tei-p5-ab-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 ab
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/ab.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# ab

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5501. Git blob: `9b1cb990126bd47a976a30efde78fbc95ab20709`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="linking" xml:id="gi-ab" ident="ab">
  <gloss versionDate="2005-01-14" xml:lang="en">anonymous block</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">익명 구역</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">匿名區塊</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">bloc anonyme</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">bloque anónimo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">blocco anonimo</gloss>
  <gloss versionDate="2018-12-18" xml:lang="ja">無名ブロック</gloss>
  <desc versionDate="2022-08-11" xml:lang="en">contains any component-level unit of text, acting as a container for phrase or inter level elements analogous to, but without the same constraints as, a paragraph.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">의미적 부담 없이, 문단과 유사한 구 또는 상호층위 요소에 대한 익명 전달체로 기능하는 임의적 성분-층위 단위를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件中任何隨機組合性層次的單元，匿名收容類似一個段落、但不包含段落語義的字詞或中間層元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">任意の部分的テキスト単位を示す。特定の意味はなくとも、段落に相当する、 句レベル・挿入レベルの単位として無名単位になる。</desc>
  <desc versionDate="2009-10-05" xml:lang="fr">contient une unité de texte quelconque, de niveau <q>composant</q>, faisant office de contenant anonyme pour une expression ou des éléments de niveau intermédiaire, analogue à un paragraphe mais sans sa portée sémantique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier unidad textual a nivel de componente que actua como un contenedor anónimo de sintagmas o de elementos de internivel similares al párrafo pero sin la carga semántica de este último.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una qualsiasi unità testuale a livello di componente che funge da contenitore anonimo di sintagmi o elementi interlivello simili al paragrafo ma senza il bagaglio semantico di quest'ultimo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.fragmentable"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.pLike"/>
  </classes>
  <content>
    <macroRef key="macro.abContent"/>
  </content>
  <constraintSpec ident="abstractModel-structure-ab-in-l" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:l//tei:ab">
        <sch:assert test="ancestor::tei:floatingText | parent::tei:figure | parent::tei:note">
          Abstract model violation: Metrical lines (&lt;l> elements) may not contain higher-level divisions such as &lt;p> or &lt;ab>, unless &lt;ab> is a child of &lt;figure> or &lt;note>, or is a descendant of &lt;floatingText>.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ab-egXML-zb" source="#SASE-eg-40">
      <div type="book" n="Genesis">
        <div type="chapter" n="1">
          <ab>In the beginning God created the heaven and the earth.</ab>
          <ab>And the earth was without form, and void; and 
               darkness was upon the face of the deep. And the 
               spirit of God moved upon the face of the waters.</ab>
          <ab>And God said, Let there be light: and there was light.</ab>
          <!-- ...-->
        </div>
      </div>
    </egXML>
  </exemplum>
  <remarks ident="ab-remarks" versionDate="2022-08-11" xml:lang="en">
    <p>The <gi>ab</gi> element may be used at the encoder's discretion to mark any component-level elements in a text for which no other more specific appropriate markup is defined. Unlike paragraphs, <gi>ab</gi> may nest and may use the <att>type</att> and <att>subtype</att> attributes.</p>
  </remarks>
  <remarks ident="ab-remarks" versionDate="2022-05-02" xml:lang="es"><p>El elemento <gi>ab</gi> se puede utilizar a discreción del codificador para marcar cualquier elemento a nivel de componente en un texto para el que no se haya definido ningún otro marcado apropiado más específico.</p></remarks>
  <remarks ident="ab-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p>L'élément <gi>ab</gi> peut être utilisé à la discrétion de l'encodeur pour marquer dans un texte tout élément de niveau composant pour lequel aucune méthode appropriée de balisage plus spécifique n'est définie.</p>
  </remarks>
  <remarks ident="ab-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>ab</gi>は、符号化する人が望むあらゆる単位レベルで、適切な 要素が規定されていない場合に、自由に使用することが出来る。 </p>
  </remarks>
  <listRef>
    <ptr target="#SASE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">anonymous block</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">익명 구역</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">匿名區塊</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">bloc anonyme</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">bloque anónimo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">blocco anonimo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2018-12-18" xml:lang="ja">無名ブロック</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2022-08-11" xml:lang="en">contains any component-level unit of text, acting as a container for phrase or inter level elements analogous to, but without the same constraints as, a paragraph.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">의미적 부담 없이, 문단과 유사한 구 또는 상호층위 요소에 대한 익명 전달체로 기능하는 임의적 성분-층위 단위를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件中任何隨機組合性層次的單元，匿名收容類似一個段落、但不包含段落語義的字詞或中間層元素。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">任意の部分的テキスト単位を示す。特定の意味はなくとも、段落に相当する、 句レベル・挿入レベルの単位として無名単位になる。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-10-05" xml:lang="fr">contient une unité de texte quelconque, de niveau <q>composant</q>, faisant office de contenant anonyme pour une expression ou des éléments de niveau intermédiaire, analogue à un paragraphe mais sans sa portée sémantique.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier unidad textual a nivel de componente que actua como un contenedor anónimo de sintagmas o de elementos de internivel similares al párrafo pero sin la carga semántica de este último.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una qualsiasi unità testuale a livello di componente che funge da contenitore anonimo di sintagmi o elementi interlivello simili al paragrafo ma senza il bagaglio semantico di quest'ultimo.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.fragmentable"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.pLike"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.abContent"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="abstractModel-structure-ab-in-l" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:l//tei:ab">
        <sch:assert test="ancestor::tei:floatingText | parent::tei:figure | parent::tei:note">
          Abstract model violation: Metrical lines (&lt;l> elements) may not contain higher-level divisions such as &lt;p> or &lt;ab>, unless &lt;ab> is a child of &lt;figure> or &lt;note>, or is a descendant of &lt;floatingText>.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ab-egXML-zb" source="#SASE-eg-40">
      <div type="book" n="Genesis">
        <div type="chapter" n="1">
          <ab>In the beginning God created the heaven and the earth.</ab>
          <ab>And the earth was without form, and void; and 
               darkness was upon the face of the deep. And the 
               spirit of God moved upon the face of the waters.</ab>
          <ab>And God said, Let there be light: and there was light.</ab>
          <!-- ...-->
        </div>
      </div>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="ab-remarks" versionDate="2022-08-11" xml:lang="en">
    <p>The <gi>ab</gi> element may be used at the encoder's discretion to mark any component-level elements in a text for which no other more specific appropriate markup is defined. Unlike paragraphs, <gi>ab</gi> may nest and may use the <att>type</att> and <att>subtype</att> attributes.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="ab-remarks" versionDate="2022-05-02" xml:lang="es"><p>El elemento <gi>ab</gi> se puede utilizar a discreción del codificador para marcar cualquier elemento a nivel de componente en un texto para el que no se haya definido ningún otro marcado apropiado más específico.</p></remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="ab-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p>L'élément <gi>ab</gi> peut être utilisé à la discrétion de l'encodeur pour marquer dans un texte tout élément de niveau composant pour lequel aucune méthode appropriée de balisage plus spécifique n'est définie.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="ab-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>ab</gi>は、符号化する人が望むあらゆる単位レベルで、適切な 要素が規定されていない場合に、自由に使用することが出来る。 </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SASE"/>
  </listRef>
```

^b23

