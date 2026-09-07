---
type: representation
source-type: document
source: '[[00_sources/tei-p5-space-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 space
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/space.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# space

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8073. Git blob: `537f1a74be477c126bce1866b1a6aa53fdbc0e08`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-space" ident="space">
  <gloss versionDate="2007-06-12" xml:lang="en">space</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">espace</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates the location of a significant space in the text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">복사본에서 중요한 공간의 위치를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出來源文件中出現大片空白的位置。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">元資料にある重要な空白の場所を示す。</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">permet de situer un espace significatif dans le texte édité.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la localización de un espacio significativo en el texto de copia.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica la posizione di uno spazio significativo nel testo copia.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
  <content>    
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="dim" usage="rec">
      <gloss versionDate="2007-07-04" xml:lang="en">dimension</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">차원</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">dimensión</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">dimensione</gloss>
      <gloss versionDate="2009-11-16" xml:lang="fr">dimension</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether the space is horizontal or vertical.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">공간의 수직 또는 수평에 대한 정보를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該空白是水平的或垂直的。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該空白は、縦長か横長かを示す。</desc>
      <desc versionDate="2009-11-16" xml:lang="fr">indique si l'espace est vertical ou horizontal.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el espacio es vertical u horizontal.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se lo spazio è orizzontale o verticale.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="horizontal">
          <desc versionDate="2007-06-27" xml:lang="en">the space is horizontal.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">공간이 수평이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">空白是水平的。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el espacio es horizontal.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該空白は、横長。</desc>
          <desc versionDate="2009-11-16" xml:lang="fr">l'espace est horizontal.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">spazio orizzontale.</desc>
        </valItem>
        <valItem ident="vertical">
          <desc versionDate="2007-06-27" xml:lang="en">the space is vertical.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">공간이 수직이다.</desc>
          <desc versionDate="2009-11-16" xml:lang="fr">l'espace est vertical.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">空白是垂直的。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el espacio es vertical.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該空白は、縦長。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">spazio verticale.</desc>
        </valItem>
      </valList>
      <remarks ident="space-attr.dim-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>For irregular shapes in two dimensions, the value for
this attribute should reflect the more important of the two dimensions.
In conventional left-right scripts, a space with both vertical and
horizontal components should be classed as <val>vertical</val>.</p>
      </remarks>
      <remarks ident="space-attr.dim-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>Pour des formes irrégulières à deux dimensions, la valeur de cet attribut doit refléter la plus importante des deux dimensions. Dans les textes
écrits conventionnellement de gauche à droite, un espace composé de parties horizontales et verticales doit être considéré comme <val>vertical</val>.</p>
      </remarks>
      <remarks ident="space-attr.dim-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        一般的でない形の場合、当該属性値は、より重要な2次元情報を反映
        すべきである。左から右に書く場合、縦長でもあり横長でもある空白
        は、属性値<val>vertical</val>で分類されるべきである。
        </p>
      </remarks>
    </attDef>
    <attDef ident="resp" mode="change">
      <desc versionDate="2013-12-10" xml:lang="en">(responsible party) indicates the individual responsible for identifying and measuring the space.</desc>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-space-egXML-np">By god if wommen had writen storyes
      As <space quantity="7" unit="minims"/> han within her oratoryes</egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-space-egXML-ha">στρατηλάτ<space quantity="1" unit="chars"/>ου</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-space-egXML-co" source="#fr-ex-Perec-vie"> Lettre à lettre,
        un texte se forme, s'affirme, s'affermit, se fixe, se fige : une ligne assez strictement
        horizontale se dépose sur la <space quantity="3" unit="lignes"/>feuille blanche.</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-space-egXML-fh" source="#biblzh-tw_n62-64">
      夕陽西下<space quantity="1" unit="minims"/>斷腸人在天涯</egXML>
  </exemplum>
  <remarks ident="space-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element should be used wherever it is desired to record
an unusual space in the source text, e.g. space left for a word to be
filled in later, for later rubrication, etc.  It is not intended to be
used to mark normal inter-word space or the like.</p>
  </remarks>
  <remarks ident="space-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Cet élément devrait être utilisé partout où l'on désire signaler un espace inhabituel dans le texte source, par exemple un espace réservé pour un mot à écrire plus tard, pour une rubrication ultérieure, etc. Il n'est pas destiné à être utilisé pour marquer l'espace normal entre des mots par exemple.</p>
  </remarks>
  <remarks ident="space-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、元テキストにある普通でない空白を記録するために使われる
    べきである。例えば、単語の後に多くある空白や、続く朱書きのためにあ
    る空白など。当該要素は、一般的な単語間や行間の空白を示すために使わ
    れるものではない。
    </p>
  </remarks>
  <listRef>
    <ptr target="#PHSP"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">space</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">espace</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the location of a significant space in the text.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">복사본에서 중요한 공간의 위치를 표시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出來源文件中出現大片空白的位置。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">元資料にある重要な空白の場所を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">permet de situer un espace significatif dans le texte édité.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la localización de un espacio significativo en el texto de copia.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la posizione di uno spazio significativo nel testo copia.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>    
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">dimension</gloss>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">차원</gloss>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">dimensión</gloss>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">dimensione</gloss>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2009-11-16" xml:lang="fr">dimension</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether the space is horizontal or vertical.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">공간의 수직 또는 수평에 대한 정보를 제시한다.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該空白是水平的或垂直的。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該空白は、縦長か横長かを示す。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">indique si l'espace est vertical ou horizontal.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el espacio es vertical u horizontal.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se lo spazio è orizzontale o verticale.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="horizontal">
          <desc versionDate="2007-06-27" xml:lang="en">the space is horizontal.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">공간이 수평이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">空白是水平的。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el espacio es horizontal.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該空白は、横長。</desc>
          <desc versionDate="2009-11-16" xml:lang="fr">l'espace est horizontal.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">spazio orizzontale.</desc>
        </valItem>
        <valItem ident="vertical">
          <desc versionDate="2007-06-27" xml:lang="en">the space is vertical.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">공간이 수직이다.</desc>
          <desc versionDate="2009-11-16" xml:lang="fr">l'espace est vertical.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">空白是垂直的。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el espacio es vertical.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該空白は、縦長。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">spazio verticale.</desc>
        </valItem>
      </valList>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="space-attr.dim-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>For irregular shapes in two dimensions, the value for
this attribute should reflect the more important of the two dimensions.
In conventional left-right scripts, a space with both vertical and
horizontal components should be classed as <val>vertical</val>.</p>
      </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="space-attr.dim-remarks" versionDate="2009-11-17" xml:lang="fr">
        <p>Pour des formes irrégulières à deux dimensions, la valeur de cet attribut doit refléter la plus importante des deux dimensions. Dans les textes
écrits conventionnellement de gauche à droite, un espace composé de parties horizontales et verticales doit être considéré comme <val>vertical</val>.</p>
      </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="space-attr.dim-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        一般的でない形の場合、当該属性値は、より重要な2次元情報を反映
        すべきである。左から右に書く場合、縦長でもあり横長でもある空白
        は、属性値<val>vertical</val>で分類されるべきである。
        </p>
      </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-12-10" xml:lang="en">(responsible party) indicates the individual responsible for identifying and measuring the space.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-space-egXML-np">By god if wommen had writen storyes
      As <space quantity="7" unit="minims"/> han within her oratoryes</egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-space-egXML-ha">στρατηλάτ<space quantity="1" unit="chars"/>ου</egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-space-egXML-co" source="#fr-ex-Perec-vie"> Lettre à lettre,
        un texte se forme, s'affirme, s'affermit, se fixe, se fige : une ligne assez strictement
        horizontale se dépose sur la <space quantity="3" unit="lignes"/>feuille blanche.</egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-space-egXML-fh" source="#biblzh-tw_n62-64">
      夕陽西下<space quantity="1" unit="minims"/>斷腸人在天涯</egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="space-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element should be used wherever it is desired to record
an unusual space in the source text, e.g. space left for a word to be
filled in later, for later rubrication, etc.  It is not intended to be
used to mark normal inter-word space or the like.</p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="space-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Cet élément devrait être utilisé partout où l'on désire signaler un espace inhabituel dans le texte source, par exemple un espace réservé pour un mot à écrire plus tard, pour une rubrication ultérieure, etc. Il n'est pas destiné à être utilisé pour marquer l'espace normal entre des mots par exemple.</p>
  </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="space-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、元テキストにある普通でない空白を記録するために使われる
    べきである。例えば、単語の後に多くある空白や、続く朱書きのためにあ
    る空白など。当該要素は、一般的な単語間や行間の空白を示すために使わ
    れるものではない。
    </p>
  </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHSP"/>
  </listRef>
```

^b37

