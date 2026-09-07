---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.textcritical-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.textCritical
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.textCritical.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.textCritical

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11355. Git blob: `ee1f7028c82282c1f837109b5d5571ae424fecc1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="READINGS" type="atts" ident="att.textCritical">
  <desc versionDate="2005-10-10" xml:lang="en">defines a set of attributes common to all elements representing variant readings in text critical work.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 비평 작품에서 이문 독법을 나타내는 모든 요소에 공통된 속성 집합을 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義在文件評論作品中，所有標記變異對應本的元素可用的一套屬性。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">校勘資料における解釈を示す要素全てに付与される属性を定義する。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">définit un ensemble d'attributs communs à tous les éléments présentant différentes leçons dans l'analyse critique d'un texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define un conjunto de atributos comunes a todos los elementos que presentan lecturas de variantes en la lectura crítica de una obra</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un insieme di attributi comuni a tutti gli elementi che rappresentano letture di varianti nella lettura critica di un'opera.</desc>
  <classes>
    <memberOf key="att.written"/>
  </classes>
  <!-- Seems we can't just use:
  <classes>
    <memberOf key="att.typed"/>
  </classes>
  and then modify @type with <attDef>, below, as the Stylesheets
  generate RELAX NG with 2 @types defined. See Stylesheets ticket
  #370. Note that same problems is present in att.entryLike.
  Also see TEI ticket #1867. -->
  <attList>
    <attRef class="att.typed" key="subtype"/>
    <attDef ident="type" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">classifies the reading according to some useful typology.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">유용한 유형에 따라 독법을 분류한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用合宜的分類法將對應本分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該解釈の分類を示す。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">établit une classification de la leçon selon une typologie utile.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">clasifica la lectura según alguna tipología funcional.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica la lettura secondo una tipologia funzionale.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="substantive">
          <gloss versionDate="2009-05-28" xml:lang="en">substantive</gloss>
          <gloss versionDate="2009-05-28" xml:lang="fr">substantif</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the reading offers a substantive variant.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">독법은 내용적 이문을 제공한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">對應本提供一個獨立變異。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la lectura ofrece una variante substancial.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該解釈は、実質的な異形を示す。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">la leçon offre une variante nominale.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la lettura offre una variante sostanziale.</desc>
        </valItem>
        <valItem ident="orthographic">
          <gloss versionDate="2009-05-28" xml:lang="en">orthographic</gloss>
          <gloss versionDate="2009-05-28" xml:lang="fr">orthographique</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the reading differs only orthographically, not in substance,
from other readings.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">독법은 다른 독법과 내용이 아니라, 철자상 차이가 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該對應本僅於拼字法上與其他對應本不同，大致上維持不變。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la lectura difiere de otras lecturas sólo ortograficamente, no de forma substancial.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該解釈は、実質的なものではないが、他の解釈の正書法と異なる。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">la leçon ne diffère que par l'orthographe, mais non en substance, des autres leçons.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la lettura differisce solo in senso ortografico, e non in modo sostanziale, rispetto ad altre letture.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="cause" usage="opt">
      <desc versionDate="2005-10-10" xml:lang="en">classifies the cause for the variant reading, according to any appropriate typology of possible origins.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">가능한 원본의 적절한 유형에 따라 이문 독본의 이유를 분류한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">利用可能來源的任何適當分類法，將變異對應本的產生原因分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">解釈が異なる原因を分類する。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">établit une classification de la cause d'une variante de leçon, selon une typologie appropriée aux origines possibles de cette variation.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">clasifica la causa de una lectura alternativa según cualquier tipología adecuada de posibles orígenes.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica le ragioni di una lettura alternativa secondo una qualsiasi tipologia adeguata di origini possibili.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="homeoteleuton"/>
        <valItem ident="homeoarchy"/>
        <valItem ident="paleographicConfusion"/>
        <valItem ident="haplography"/>
        <valItem ident="dittography"/>
        <valItem ident="falseEmendation"/>
      </valList>
    </attDef>
    <attDef ident="varSeq" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">variant sequence</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">이문 연쇄</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">secuencia variable</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">position de la variante dans une séquence</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">sequenza variante</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">provides a number indicating the position of this reading in a sequence, when there is reason to presume a sequence to the variants. <!--on any one lemma.--></desc>
      <desc versionDate="2007-12-20" xml:lang="ko">어떤 연쇄를 임의의 레마에 관한 이문으로 추정하는 이유가 있을 때, 어떤 연쇄에서 이 독본의 위치를 나타내는 수를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">當有理由假設任一主題的一系列變異對應本時，則提供一個數字，指出此對應本於連續系列中的位置。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">1つの対象語に対する一連の異形を想定する理由がある場合、当該解釈 がある場所を番号で示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit un nombre indiquant la position de la leçon dans une séquence, lorsqu'on peut supposer un ordre pour les variantes de chaque lemme.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un número que indica la posición de tal lectura dentro de una secuencia, cuando se de el caso de suponer una secuencia respecto a las variantes de un lema dado</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un numero che indica la posizione di tale lettura all'interno di una sequenza, qualora ci sia motivo di supporre una sequenza rispetto alle varianti per un dato lemma.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <remarks ident="att.textCritical-attr.varSeq-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>Different variant sequences could be coded with distinct
        number trails: 1-2-3 for one sequence, 5-6-7 for another.
        More complex variant sequences, with (for example) multiple
        branchings from single readings, may be expressed through the
        <gi>join</gi> element.</p>
      </remarks>
      <remarks ident="att.textCritical-attr.varSeq-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>On peut coder différentes séquences de variantes avec des
        séries de numéros distincts : 1-2-3 pour une séquence, 5-6-7
        pour une autre. On peut exprimer des séquences de variantes
        plus complexes (par exemple comportant de multiples
        ramifications à partir de leçons uniques) par l'élément
        <gi>join</gi>.</p>
      </remarks>
      <remarks ident="att.textCritical-attr.varSeq-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        異形列は、異なる番号の列として記すことになろう。例えば、1-2-3
        となり、これとは別の列には5-6-7となる。1つの解釈から複数の分岐
        を作る複雑な異形列の場合には、共通識別子<gi>join</gi>を使い示
        されるかもしれない。
        </p>
      </remarks>
    </attDef>
    <attDef ident="require" usage="opt">
      <desc versionDate="2016-08-19" xml:lang="en">points to other readings that are required when adopting the current reading or lemma.</desc>
      <desc versionDate="2016-08-19" xml:lang="it">punta ad altre letture che vanno obbligatoriamente considerate insieme all'elemento corrente.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <remarks ident="att.textCritical-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>This element class defines attributes inherited by
    <gi>rdg</gi>, <gi>lem</gi>, and <gi>rdgGrp</gi>.</p>
  </remarks>
  <remarks ident="att.textCritical-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe d'éléments définit les attributs hérités par les éléments <gi>rdg</gi>, <gi>lem</gi> et <gi>rdgGrp</gi>.</p>
  </remarks>
  <remarks ident="att.textCritical-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      当該要素クラスは、共通識別子<gi>rdg</gi>、<gi>lem</gi>、<gi>rdgGrp</gi>が継承する属性を定義している。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">defines a set of attributes common to all elements representing variant readings in text critical work.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 비평 작품에서 이문 독법을 나타내는 모든 요소에 공통된 속성 집합을 정의한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義在文件評論作品中，所有標記變異對應本的元素可用的一套屬性。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">校勘資料における解釈を示す要素全てに付与される属性を定義する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">définit un ensemble d'attributs communs à tous les éléments présentant différentes leçons dans l'analyse critique d'un texte.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define un conjunto de atributos comunes a todos los elementos que presentan lecturas de variantes en la lectura crítica de una obra</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un insieme di attributi comuni a tutti gli elementi che rappresentano letture di varianti nella lettura critica di un'opera.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.written"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attRef[1]`.

```xml
<attRef class="att.typed" key="subtype"/>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">classifies the reading according to some useful typology.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">유용한 유형에 따라 독법을 분류한다.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用合宜的分類法將對應本分類。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該解釈の分類を示す。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">établit une classification de la leçon selon une typologie utile.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clasifica la lectura según alguna tipología funcional.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica la lettura secondo una tipologia funzionale.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="substantive">
          <gloss versionDate="2009-05-28" xml:lang="en">substantive</gloss>
          <gloss versionDate="2009-05-28" xml:lang="fr">substantif</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the reading offers a substantive variant.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">독법은 내용적 이문을 제공한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">對應本提供一個獨立變異。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la lectura ofrece una variante substancial.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該解釈は、実質的な異形を示す。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">la leçon offre une variante nominale.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la lettura offre una variante sostanziale.</desc>
        </valItem>
        <valItem ident="orthographic">
          <gloss versionDate="2009-05-28" xml:lang="en">orthographic</gloss>
          <gloss versionDate="2009-05-28" xml:lang="fr">orthographique</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the reading differs only orthographically, not in substance,
from other readings.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">독법은 다른 독법과 내용이 아니라, 철자상 차이가 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該對應本僅於拼字法上與其他對應本不同，大致上維持不變。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la lectura difiere de otras lecturas sólo ortograficamente, no de forma substancial.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該解釈は、実質的なものではないが、他の解釈の正書法と異なる。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">la leçon ne diffère que par l'orthographe, mais non en substance, des autres leçons.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la lettura differisce solo in senso ortografico, e non in modo sostanziale, rispetto ad altre letture.</desc>
        </valItem>
      </valList>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">classifies the cause for the variant reading, according to any appropriate typology of possible origins.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">가능한 원본의 적절한 유형에 따라 이문 독본의 이유를 분류한다.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">利用可能來源的任何適當分類法，將變異對應本的產生原因分類。</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">解釈が異なる原因を分類する。</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">établit une classification de la cause d'une variante de leçon, selon une typologie appropriée aux origines possibles de cette variation.</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clasifica la causa de una lectura alternativa según cualquier tipología adecuada de posibles orígenes.</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica le ragioni di una lettura alternativa secondo una qualsiasi tipologia adeguata di origini possibili.</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="homeoteleuton"/>
        <valItem ident="homeoarchy"/>
        <valItem ident="paleographicConfusion"/>
        <valItem ident="haplography"/>
        <valItem ident="dittography"/>
        <valItem ident="falseEmendation"/>
      </valList>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">variant sequence</gloss>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">이문 연쇄</gloss>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">secuencia variable</gloss>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">position de la variante dans une séquence</gloss>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">sequenza variante</gloss>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">provides a number indicating the position of this reading in a sequence, when there is reason to presume a sequence to the variants. <!--on any one lemma.--></desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 연쇄를 임의의 레마에 관한 이문으로 추정하는 이유가 있을 때, 어떤 연쇄에서 이 독본의 위치를 나타내는 수를 제공한다.</desc>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">當有理由假設任一主題的一系列變異對應本時，則提供一個數字，指出此對應本於連續系列中的位置。</desc>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">1つの対象語に対する一連の異形を想定する理由がある場合、当該解釈 がある場所を番号で示す。</desc>
```

^b36

### Block 37

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit un nombre indiquant la position de la leçon dans une séquence, lorsqu'on peut supposer un ordre pour les variantes de chaque lemme.</desc>
```

^b37

### Block 38

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un número que indica la posición de tal lectura dentro de una secuencia, cuando se de el caso de suponer una secuencia respecto a las variantes de un lema dado</desc>
```

^b38

### Block 39

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un numero che indica la posizione di tale lettura all'interno di una sequenza, qualora ci sia motivo di supporre una sequenza rispetto alle varianti per un dato lemma.</desc>
```

^b39

### Block 40

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b40

### Block 41

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="att.textCritical-attr.varSeq-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>Different variant sequences could be coded with distinct
        number trails: 1-2-3 for one sequence, 5-6-7 for another.
        More complex variant sequences, with (for example) multiple
        branchings from single readings, may be expressed through the
        <gi>join</gi> element.</p>
      </remarks>
```

^b41

### Block 42

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="att.textCritical-attr.varSeq-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>On peut coder différentes séquences de variantes avec des
        séries de numéros distincts : 1-2-3 pour une séquence, 5-6-7
        pour une autre. On peut exprimer des séquences de variantes
        plus complexes (par exemple comportant de multiples
        ramifications à partir de leçons uniques) par l'élément
        <gi>join</gi>.</p>
      </remarks>
```

^b42

### Block 43

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="att.textCritical-attr.varSeq-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        異形列は、異なる番号の列として記すことになろう。例えば、1-2-3
        となり、これとは別の列には5-6-7となる。1つの解釈から複数の分岐
        を作る複雑な異形列の場合には、共通識別子<gi>join</gi>を使い示
        されるかもしれない。
        </p>
      </remarks>
```

^b43

### Block 44

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2016-08-19" xml:lang="en">points to other readings that are required when adopting the current reading or lemma.</desc>
```

^b44

### Block 45

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2016-08-19" xml:lang="it">punta ad altre letture che vanno obbligatoriamente considerate insieme all'elemento corrente.</desc>
```

^b45

### Block 46

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b46

### Block 47

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.textCritical-remarks" versionDate="2005-10-10" xml:lang="en">
    <p>This element class defines attributes inherited by
    <gi>rdg</gi>, <gi>lem</gi>, and <gi>rdgGrp</gi>.</p>
  </remarks>
```

^b47

### Block 48

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.textCritical-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe d'éléments définit les attributs hérités par les éléments <gi>rdg</gi>, <gi>lem</gi> et <gi>rdgGrp</gi>.</p>
  </remarks>
```

^b48

### Block 49

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.textCritical-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      当該要素クラスは、共通識別子<gi>rdg</gi>、<gi>lem</gi>、<gi>rdgGrp</gi>が継承する属性を定義している。
    </p>
  </remarks>
```

^b49

### Block 50

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b50

