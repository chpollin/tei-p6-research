---
type: representation
source-type: document
source: '[[00_sources/tei-p5-rhyme-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 rhyme
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/rhyme.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# rhyme

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7344. Git blob: `e5d75bec4d784a94e93afb1df5b82aa747ebf867`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="verse" xml:id="gi-rhyme" ident="rhyme">
  <desc versionDate="2005-11-10" xml:lang="en">marks the rhyming part of a metrical line.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">운율 행의 운 부분을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記韻律詩行的押韻部分。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">韻文行の押韻部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">marque la partie rimante d'une ligne métrique.</desc>
  <desc versionDate="2022-06-30" xml:lang="es">marca una parte del esquema métrico de un verso</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segnala la stringa in rima all'interno di un verso.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.lPart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="label" usage="rec">
      <desc versionDate="2013-12-20" xml:lang="en">provides a label
      (usually a single letter) to identify which part of a rhyme scheme this rhyming string
        instantiates.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">운 문자열이 예시된 운 스키마 부분을 식별하는 표지를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個標籤，識別此韻腳為押韻組合的哪一部份。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該押韻が起こる韻スキーム部分を特定するラベルを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne une étiquette pour identifier à quelle shéma
        métrique correspond cette alternance de rimes.</desc>
      <desc versionDate="2022-06-30" xml:lang="es">proporciona una etiqueta (normalmente una sola letra) que identifica qué parte del esquema métrico ejemplifica esta cadena de caracteres en cuestión.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un'etichetta che identifica quale parte
        dello schema rimico è rappresentata dalla stringa in questione</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
      <remarks ident="rhyme-attr.label-remarks" versionDate="2005-11-10" xml:lang="en">
        <p>Within a particular scope, all <gi>rhyme</gi> elements with the same value for their
            <att>label</att> attribute are assumed to rhyme with each other. The scope is defined by
          the nearest ancestor element for which the <att>rhyme</att> attribute has been
        supplied.</p>
      </remarks>
      <remarks ident="rhyme-attr.label-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Dans un cadre délimité, tous les éléments <gi>rhyme</gi> avec la même valeur pour leur
          attribut <att>label</att> sont présumés rimer l'un avec l'autre. Ce cadre est défini par
          l'élément ancêtre le plus proche pour lequel l'attribut <att>rhyme</att> a été fourni.
        </p>
      </remarks>
      <remarks ident="rhyme-attr.label-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 特定範囲中で、属性<att>label</att>に同じ属性値を持つ要素 <gi>rhyme</gi>全てが、互いに韻を踏んでいるとされる。この範囲は、
            当該属性<att>rhyme</att>が付与されているものから直近の先行要素 により定義される。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-tn" source="#VESTR-eg-5">
      <lg rhyme="abababcc">
        <l>'Tis pity learned virgins ever <rhyme label="a">wed</rhyme>
            </l>
        <l>With persons of no sort of edu<rhyme label="b">cation</rhyme>,</l>
        <l>Or gentlemen, who, though well born and <rhyme label="a">bred</rhyme>,</l>
        <l>Grow tired of scientific conver<rhyme label="b">sation</rhyme>:</l>
        <l>I don't choose to say much on this <rhyme label="a">head</rhyme>,</l>
        <l>I'm a plain man, and in a single <rhyme label="b">station</rhyme>,</l>
        <l>But — Oh! ye lords of ladies inte<rhyme label="c">llectual</rhyme>,</l>
        <l>Inform us truly, have they not hen-<rhyme label="c">peck'd you all</rhyme>?</l>
      </lg>
    </egXML>
    <!-- Byron, Don Juan I.xxii -->
  </exemplum>
  
<exemplum xml:lang="en">
   <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-vl" source="#en-blake-tyger">
     <lg>
       <l>Tyger! Tyger! burning <rhyme label="a">bright</rhyme></l>
       <l>In the forests of the <rhyme label="a">night</rhyme>,</l> 
       <l>What immortal hand or <rhyme label="b">eye</rhyme></l>
       <l>Could frame thy fearful <rhyme label="b" type="eye-rhyme">symmetry</rhyme>?</l> 
     </lg>
   </egXML>
 </exemplum>

 <exemplum xml:lang="en">
   <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-ss" source="#eg-rhyme-dutt">
     <lg>
       <l>"Hark! Lakshman! Hark, again that <rhyme label="a">cry</rhyme>!</l>
       <l>It is, — it is my husband's <rhyme label="b">voice</rhyme>!</l>
       <l>hasten, to his succour <rhyme label="a">fly</rhyme>,</l>
       <l>No more hast thou, dear friend, a <rhyme label="b">choice</rhyme>.</l>
       <l>He calls on thee, perhaps his <rhyme label="c">foes</rhyme></l>
       <l>Environ him on all sides <rhyme label="d">round</rhyme>,</l>
       <l>That wail, — it means death's final <rhyme label="c">throes</rhyme>!</l>
       <l>Why standest thou, as magic-<rhyme label="d">bound</rhyme>?</l>
     </lg>
   </egXML>
  </exemplum>
  
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-cl" source="#fr-ex-Hugo-Fen">
      <lg type="quatrain" rhyme="aabccb">
        <l> Les étoiles, points d'or, percent les branches n<rhyme label="a">oires</rhyme> ; </l>
        <l> Le flot huileux et lourd décompose ses m<rhyme label="a">oires</rhyme>
            </l>
        <l> Sur l'océan blê<rhyme label="b">mi</rhyme> ;</l>
        <l>Les nuages ont l'air d'oiseaux prenant la f<rhyme label="c">uite</rhyme>,</l>
        <l>Par moments le vent parle, et dit des mots sans s<rhyme label="c">uite</rhyme>
            </l>
        <l> Comme un homme endor<rhyme label="b">mi</rhyme>.</l>
      </lg>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-sc" source="#biblzh-tw_n65">
      <lg rhyme="ou">
        <l>故人西辭黃鶴 <rhyme label="lou2">樓</rhyme>，</l>
        <l>煙花三月下揚<rhyme label="jou">州</rhyme>；</l>
        <l>孤帆遠影碧山<rhyme label="jin4">盡</rhyme>，</l>
        <l>唯見長江天際流<rhyme label="liou2">sation</rhyme>。</l>
      </lg>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#VERH"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-11-10" xml:lang="en">marks the rhyming part of a metrical line.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">운율 행의 운 부분을 표시한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記韻律詩行的押韻部分。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">韻文行の押韻部分を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">marque la partie rimante d'une ligne métrique.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-06-30" xml:lang="es">marca una parte del esquema métrico de un verso</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segnala la stringa in rima all'interno di un verso.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.lPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-20" xml:lang="en">provides a label
      (usually a single letter) to identify which part of a rhyme scheme this rhyming string
        instantiates.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">운 문자열이 예시된 운 스키마 부분을 식별하는 표지를 제시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個標籤，識別此韻腳為押韻組合的哪一部份。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該押韻が起こる韻スキーム部分を特定するラベルを示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne une étiquette pour identifier à quelle shéma
        métrique correspond cette alternance de rimes.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2022-06-30" xml:lang="es">proporciona una etiqueta (normalmente una sola letra) que identifica qué parte del esquema métrico ejemplifica esta cadena de caracteres en cuestión.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un'etichetta che identifica quale parte
        dello schema rimico è rappresentata dalla stringa in questione</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="rhyme-attr.label-remarks" versionDate="2005-11-10" xml:lang="en">
        <p>Within a particular scope, all <gi>rhyme</gi> elements with the same value for their
            <att>label</att> attribute are assumed to rhyme with each other. The scope is defined by
          the nearest ancestor element for which the <att>rhyme</att> attribute has been
        supplied.</p>
      </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="rhyme-attr.label-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Dans un cadre délimité, tous les éléments <gi>rhyme</gi> avec la même valeur pour leur
          attribut <att>label</att> sont présumés rimer l'un avec l'autre. Ce cadre est défini par
          l'élément ancêtre le plus proche pour lequel l'attribut <att>rhyme</att> a été fourni.
        </p>
      </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="rhyme-attr.label-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 特定範囲中で、属性<att>label</att>に同じ属性値を持つ要素 <gi>rhyme</gi>全てが、互いに韻を踏んでいるとされる。この範囲は、
            当該属性<att>rhyme</att>が付与されているものから直近の先行要素 により定義される。 </p>
      </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-tn" source="#VESTR-eg-5">
      <lg rhyme="abababcc">
        <l>'Tis pity learned virgins ever <rhyme label="a">wed</rhyme>
            </l>
        <l>With persons of no sort of edu<rhyme label="b">cation</rhyme>,</l>
        <l>Or gentlemen, who, though well born and <rhyme label="a">bred</rhyme>,</l>
        <l>Grow tired of scientific conver<rhyme label="b">sation</rhyme>:</l>
        <l>I don't choose to say much on this <rhyme label="a">head</rhyme>,</l>
        <l>I'm a plain man, and in a single <rhyme label="b">station</rhyme>,</l>
        <l>But — Oh! ye lords of ladies inte<rhyme label="c">llectual</rhyme>,</l>
        <l>Inform us truly, have they not hen-<rhyme label="c">peck'd you all</rhyme>?</l>
      </lg>
    </egXML>
    <!-- Byron, Don Juan I.xxii -->
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
   <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-vl" source="#en-blake-tyger">
     <lg>
       <l>Tyger! Tyger! burning <rhyme label="a">bright</rhyme></l>
       <l>In the forests of the <rhyme label="a">night</rhyme>,</l> 
       <l>What immortal hand or <rhyme label="b">eye</rhyme></l>
       <l>Could frame thy fearful <rhyme label="b" type="eye-rhyme">symmetry</rhyme>?</l> 
     </lg>
   </egXML>
 </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
   <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-ss" source="#eg-rhyme-dutt">
     <lg>
       <l>"Hark! Lakshman! Hark, again that <rhyme label="a">cry</rhyme>!</l>
       <l>It is, — it is my husband's <rhyme label="b">voice</rhyme>!</l>
       <l>hasten, to his succour <rhyme label="a">fly</rhyme>,</l>
       <l>No more hast thou, dear friend, a <rhyme label="b">choice</rhyme>.</l>
       <l>He calls on thee, perhaps his <rhyme label="c">foes</rhyme></l>
       <l>Environ him on all sides <rhyme label="d">round</rhyme>,</l>
       <l>That wail, — it means death's final <rhyme label="c">throes</rhyme>!</l>
       <l>Why standest thou, as magic-<rhyme label="d">bound</rhyme>?</l>
     </lg>
   </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-cl" source="#fr-ex-Hugo-Fen">
      <lg type="quatrain" rhyme="aabccb">
        <l> Les étoiles, points d'or, percent les branches n<rhyme label="a">oires</rhyme> ; </l>
        <l> Le flot huileux et lourd décompose ses m<rhyme label="a">oires</rhyme>
            </l>
        <l> Sur l'océan blê<rhyme label="b">mi</rhyme> ;</l>
        <l>Les nuages ont l'air d'oiseaux prenant la f<rhyme label="c">uite</rhyme>,</l>
        <l>Par moments le vent parle, et dit des mots sans s<rhyme label="c">uite</rhyme>
            </l>
        <l> Comme un homme endor<rhyme label="b">mi</rhyme>.</l>
      </lg>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-rhyme-egXML-sc" source="#biblzh-tw_n65">
      <lg rhyme="ou">
        <l>故人西辭黃鶴 <rhyme label="lou2">樓</rhyme>，</l>
        <l>煙花三月下揚<rhyme label="jou">州</rhyme>；</l>
        <l>孤帆遠影碧山<rhyme label="jin4">盡</rhyme>，</l>
        <l>唯見長江天際流<rhyme label="liou2">sation</rhyme>。</l>
      </lg>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#VERH"/>
  </listRef>
```

^b26

