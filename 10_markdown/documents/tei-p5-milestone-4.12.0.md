---
type: representation
source-type: document
source: '[[00_sources/tei-p5-milestone-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 milestone
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/milestone.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# milestone

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6793. Git blob: `0f15e8a6a28b41ce606dd1420ec99c1a918df1d0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-milestone" ident="milestone">
  <gloss versionDate="2009-01-06" xml:lang="en">milestone</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">borne</gloss>
  <gloss versionDate="2016-11-29" xml:lang="de">Grenzpunkt</gloss>
  <desc versionDate="2008-06-21" xml:lang="en">marks a boundary point separating any kind of section of a text, typically but not
    necessarily indicating a point at which some part of a standard reference system changes, where
    the change is not represented by a structural element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 절을 분할하는 경계점을 표지한다. 이는 표준 참조 시스템에서의 변화로 표시되며, 구조적 요소에
    의해서는 표시되지 않는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明文本中由標準參照系統變更所指示的任何區塊分界點，並且該章節未以任何結構性元素標記。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該セクションが、構造要素により表現することができない場合に、標準的
    な参照機能により、テキストの各種セクション間にある境界点を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">marque un point
  permettant de délimiter les sections d'un
    texte selon un autre systeme que les éléments de structure ; une
    balise de ce type marque une frontière.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">marca un punto de frontera que separa cada tipo de
    sección de un texto, indicado por cambios en el sistema de referencia estándard, donde la
    sección no es representada por un elemento estructural.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segnala il limite che separa ogni tipo di sezione di un
    testo, come indicato da cambiamenti nel sistema di riferimento standard, qualora la sezione non
    sia rappresentata da un elemento strutturale.</desc>
  <desc versionDate="2016-11-29" xml:lang="de">markiert einen Grenzpunkt, der Abschnitte eines Textes trennen kann, 
    typischerweise (aber nicht notwendigerweise) den Wechsel eines Bezugssystems, 
    der nicht durch ein strukturelles Markup beschrieben werden kann.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.breaking"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.milestoneUnit"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
  <content><empty/></content>
  <!-- MDH 2012-07-15: Attribute @unit moved to att.milestoneUnit; milestone and refState are now members of 
     that attribute class. This centralizes the definition of the attribute and its suggested values. 
     SF ticket http://purl.org/tei/bugs/3537452. -->
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-milestone-egXML-yc"><milestone n="23" ed="La" unit="Dreissiger"/>
      ... <milestone n="24" ed="AV" unit="verse"/> ...</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-milestone-egXML-eh"><milestone n="23" ed="La" unit="Dreissiger"/> ... <milestone n="24" ed="AV" unit="verse"/>
        ...</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-milestone-egXML-yn"><milestone n="23" ed="拉丁文版本" unit="三十"/> ...
        <milestone n="24" ed="聖經欽定版本" unit="韻文"/> ...</egXML>
  </exemplum>
  <remarks ident="milestone-remarks" versionDate="2016-11-04" xml:lang="en">
    <p>For this element, the global <att>n</att> attribute indicates the new number or other value
      for the unit which changes at this milestone. The special value
      <mentioned>unnumbered</mentioned> should be used in passages which fall outside the normal
      numbering scheme, such as chapter or other headings, poem numbers or titles, etc.</p>
    <p>The order in which <gi>milestone</gi> elements are given at a given point is not normally significant.
      <!--Milestones for page and column should precede
milestones for line numbers. -->
    </p>
  </remarks>
  <remarks ident="milestone-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Pour cet élément, l'attribut global <att>n</att> affecte un nouveau numéro ou une autre
      valeur à l'unité qui change à partir de l'élément <gi>milestone</gi>. La valeur
        <mentioned>unnumbered</mentioned> doit être utilisée pour les passages qui sortent du
      système normal de numérotation (par ex. titres de chapitres, numéros ou titres de poèmes, ou
      noms des personnages qui prennent la parole dans une pièce de théâtre).</p>
    <p>L'ordre dans lequel apparaissent les éléments <gi>milestone</gi> à un endroit donné n'est en
      principe pas signifiant.</p>
  </remarks>
  <remarks ident="milestone-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素にあるグローバル属性<att>n</att>は、当該標石要素が示す変化 の単位の、他の値を示す。特別な値<mentioned>unnumbered</mentioned>
      は、一般的な番号付けスキームから外れている一節中で使用されるべきで ある(例えば、章見出し、詩の番号やタイトル、詩劇における話し手の属 性など)。 </p>
    <p> 標石要素の順番は、一般には重要ではない。
      <!--Milestones for page and column should precede milestones for
    line numbers. -->
    </p>
  </remarks>
  <remarks ident="milestone-remarks" versionDate="2016-11-29" xml:lang="de">
    <p>Das globale <att>n</att>-Attribut gibt für dieses Element die neue Zahl 
      (oder einen anderen Wert) der Einheit an, die an diesem Grenzpunkt wechselt. 
      Der besondere Wert <val>unnumbered</val> (ungezählt) sollte für Abschnitte gewählt werden, 
      die außerhalb des normalen Zählsystems fallen, wie beispielsweise Kapitel- 
      oder andere Überschriften, Gedichtnummern oder -titel etc.</p>
    <p>Die Reihenfolge des Auftretens von mehreren <gi>milestone</gi>-Elementen 
      an einem gegebenen Punkt ist normalerweise nicht signifikant.</p>
  </remarks>
  <listRef>
    <ptr target="#CORS5" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="en">milestone</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">borne</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-29" xml:lang="de">Grenzpunkt</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-06-21" xml:lang="en">marks a boundary point separating any kind of section of a text, typically but not
    necessarily indicating a point at which some part of a standard reference system changes, where
    the change is not represented by a structural element.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 절을 분할하는 경계점을 표지한다. 이는 표준 참조 시스템에서의 변화로 표시되며, 구조적 요소에
    의해서는 표시되지 않는다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明文本中由標準參照系統變更所指示的任何區塊分界點，並且該章節未以任何結構性元素標記。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該セクションが、構造要素により表現することができない場合に、標準的
    な参照機能により、テキストの各種セクション間にある境界点を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">marque un point
  permettant de délimiter les sections d'un
    texte selon un autre systeme que les éléments de structure ; une
    balise de ce type marque une frontière.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">marca un punto de frontera que separa cada tipo de
    sección de un texto, indicado por cambios en el sistema de referencia estándard, donde la
    sección no es representada por un elemento estructural.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segnala il limite che separa ogni tipo di sezione di un
    testo, come indicato da cambiamenti nel sistema di riferimento standard, qualora la sezione non
    sia rappresentata da un elemento strutturale.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-29" xml:lang="de">markiert einen Grenzpunkt, der Abschnitte eines Textes trennen kann, 
    typischerweise (aber nicht notwendigerweise) den Wechsel eines Bezugssystems, 
    der nicht durch ein strukturelles Markup beschrieben werden kann.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.breaking"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.milestoneUnit"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-milestone-egXML-yc"><milestone n="23" ed="La" unit="Dreissiger"/>
      ... <milestone n="24" ed="AV" unit="verse"/> ...</egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-milestone-egXML-eh"><milestone n="23" ed="La" unit="Dreissiger"/> ... <milestone n="24" ed="AV" unit="verse"/>
        ...</egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-milestone-egXML-yn"><milestone n="23" ed="拉丁文版本" unit="三十"/> ...
        <milestone n="24" ed="聖經欽定版本" unit="韻文"/> ...</egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="milestone-remarks" versionDate="2016-11-04" xml:lang="en">
    <p>For this element, the global <att>n</att> attribute indicates the new number or other value
      for the unit which changes at this milestone. The special value
      <mentioned>unnumbered</mentioned> should be used in passages which fall outside the normal
      numbering scheme, such as chapter or other headings, poem numbers or titles, etc.</p>
    <p>The order in which <gi>milestone</gi> elements are given at a given point is not normally significant.
      <!--Milestones for page and column should precede
milestones for line numbers. -->
    </p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="milestone-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Pour cet élément, l'attribut global <att>n</att> affecte un nouveau numéro ou une autre
      valeur à l'unité qui change à partir de l'élément <gi>milestone</gi>. La valeur
        <mentioned>unnumbered</mentioned> doit être utilisée pour les passages qui sortent du
      système normal de numérotation (par ex. titres de chapitres, numéros ou titres de poèmes, ou
      noms des personnages qui prennent la parole dans une pièce de théâtre).</p>
    <p>L'ordre dans lequel apparaissent les éléments <gi>milestone</gi> à un endroit donné n'est en
      principe pas signifiant.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="milestone-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素にあるグローバル属性<att>n</att>は、当該標石要素が示す変化 の単位の、他の値を示す。特別な値<mentioned>unnumbered</mentioned>
      は、一般的な番号付けスキームから外れている一節中で使用されるべきで ある(例えば、章見出し、詩の番号やタイトル、詩劇における話し手の属 性など)。 </p>
    <p> 標石要素の順番は、一般には重要ではない。
      <!--Milestones for page and column should precede milestones for
    line numbers. -->
    </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="milestone-remarks" versionDate="2016-11-29" xml:lang="de">
    <p>Das globale <att>n</att>-Attribut gibt für dieses Element die neue Zahl 
      (oder einen anderen Wert) der Einheit an, die an diesem Grenzpunkt wechselt. 
      Der besondere Wert <val>unnumbered</val> (ungezählt) sollte für Abschnitte gewählt werden, 
      die außerhalb des normalen Zählsystems fallen, wie beispielsweise Kapitel- 
      oder andere Überschriften, Gedichtnummern oder -titel etc.</p>
    <p>Die Reihenfolge des Auftretens von mehreren <gi>milestone</gi>-Elementen 
      an einem gegebenen Punkt ist normalerweise nicht signifikant.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CORS5" type="div3"/>
  </listRef>
```

^b21

