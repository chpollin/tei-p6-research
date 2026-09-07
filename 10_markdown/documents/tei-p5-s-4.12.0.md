---
type: representation
source-type: document
source: '[[00_sources/tei-p5-s-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 s
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/s.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# s

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5493. Git blob: `844484d77c31129208843250c8f2fe75b4f20b36`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="analysis" xml:id="gi-s" ident="s">
  <gloss versionDate="2005-01-14" xml:lang="en">s-unit</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">s-단위</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">句子單元</gloss>
  <gloss versionDate="2009-02-13" xml:lang="fr">phrase</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">oración</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">unità s</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Satzeinheit</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a sentence-like division of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 문장에 해당하는 부분을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文字中一個句子組成的區段。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">文に相当するテキスト単位を示す。</desc>
  <desc versionDate="2009-02-13" xml:lang="fr">contient une division textuelle de type phrase.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una oración del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la divisione del testo del tipo proposizione.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält einen satzähnlichen Textabschnitt.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.segLike"/>
  </classes>
  <content>
    <!-- NOTE: MDH reversing horrible change to content model mandated
         by Council in https://sourceforge.net/p/tei/bugs/578/ ==
         https://github.com/TEIC/TEI/issues/1193, and replacing
         original macro.phraseSet content model. -->
    <macroRef key="macro.phraseSeq"/> 
  </content>
  <constraintSpec ident="noNestedS" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:s">
        <sch:report test="tei:s">You may not nest one &lt;s&gt; element within another: use &lt;seg&gt; instead.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-s-egXML-dy">
      <head>
        <s>A short affair</s>
      </head>
      <s>When are you leaving?</s>
      <s>Tomorrow.</s>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-s-egXML-dq">
      <s><w>Quand</w><w>partez</w><w>-</w><w>vous</w><w> ?</w></s>
      <s><w>Demain</w><w>.</w></s>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-s-egXML-jd" source="#biblzh-tw_n1">
      <s>士何事？”</s>
      <s>尚志。 </s>
    </egXML>
  </exemplum>
  <remarks ident="s-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>The <gi>s</gi> element may be used to mark orthographic sentences, or any other segmentation
      of a text, provided that the segmentation is end-to-end, complete, and non-nesting. For
      segmentation which is partial or recursive, the <gi>seg</gi> should be used instead. </p>
    <p>The <att>type</att> attribute may be used to indicate the type of segmentation intended,
      according to any convenient typology.</p>
  </remarks>
  <remarks ident="s-remarks" versionDate="2009-02-13" xml:lang="fr">
    <p>L'élément <gi>s</gi> peut être utilisé pour marquer les phrases ou toute autre segmentation
      existant dans un texte, pourvu que cette segmentation soit présente du début à la fin du
      texte, complète et sans imbrication. Dans le cas d'une segmentation partielle ou récursive,
      l'élément <gi>seg</gi> doit remplacer l'élément <gi>s</gi>.</p>
    <p>L'attribut <att>type</att> peut être utilisé pour indiquer le type de segmentation prévue, selon une typologie appropriée.</p>
  </remarks>
  <remarks ident="s-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> テキストや句レベルの要素が混在する。また、当該要素自身も含むかもし れない。 </p>
    <p> 要素<gi>s</gi>が、ある単位の全体を完全に、入れ子なく示す場合には、 正書形の文や、他のテキスト部分を示すために使われるかもしれない。 </p>
  </remarks>
  <remarks ident="s-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Das <gi>s</gi>-Element wird verwendet um orthographische Sätze oder andere Textsegmente zu
      kodieren, vorausgesetzt das Segment ist lückenlos, vollständig und nicht verschachtelt. Für
      unvollständige oder rekursive Segmente soll stattdessen das <gi>seg</gi>-Element verwendet
      werden.</p>
    <p>Das <att>type</att>-Attribut wird verwendet, um den Segmenttyp entsprechend einer geeigneten
      Typologie anzugeben.</p>
  </remarks>
  <listRef>
    <ptr target="#AILC"/>
    <ptr target="#TSSASE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">s-unit</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">s-단위</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">句子單元</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-02-13" xml:lang="fr">phrase</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">oración</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">unità s</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Satzeinheit</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a sentence-like division of a text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 문장에 해당하는 부분을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文字中一個句子組成的區段。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">文に相当するテキスト単位を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-02-13" xml:lang="fr">contient une division textuelle de type phrase.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una oración del texto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la divisione del testo del tipo proposizione.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält einen satzähnlichen Textabschnitt.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.segLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!-- NOTE: MDH reversing horrible change to content model mandated
         by Council in https://sourceforge.net/p/tei/bugs/578/ ==
         https://github.com/TEIC/TEI/issues/1193, and replacing
         original macro.phraseSet content model. -->
    <macroRef key="macro.phraseSeq"/> 
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="noNestedS" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:s">
        <sch:report test="tei:s">You may not nest one &lt;s&gt; element within another: use &lt;seg&gt; instead.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-s-egXML-dy">
      <head>
        <s>A short affair</s>
      </head>
      <s>When are you leaving?</s>
      <s>Tomorrow.</s>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-s-egXML-dq">
      <s><w>Quand</w><w>partez</w><w>-</w><w>vous</w><w> ?</w></s>
      <s><w>Demain</w><w>.</w></s>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-s-egXML-jd" source="#biblzh-tw_n1">
      <s>士何事？”</s>
      <s>尚志。 </s>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="s-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>The <gi>s</gi> element may be used to mark orthographic sentences, or any other segmentation
      of a text, provided that the segmentation is end-to-end, complete, and non-nesting. For
      segmentation which is partial or recursive, the <gi>seg</gi> should be used instead. </p>
    <p>The <att>type</att> attribute may be used to indicate the type of segmentation intended,
      according to any convenient typology.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="s-remarks" versionDate="2009-02-13" xml:lang="fr">
    <p>L'élément <gi>s</gi> peut être utilisé pour marquer les phrases ou toute autre segmentation
      existant dans un texte, pourvu que cette segmentation soit présente du début à la fin du
      texte, complète et sans imbrication. Dans le cas d'une segmentation partielle ou récursive,
      l'élément <gi>seg</gi> doit remplacer l'élément <gi>s</gi>.</p>
    <p>L'attribut <att>type</att> peut être utilisé pour indiquer le type de segmentation prévue, selon une typologie appropriée.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="s-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> テキストや句レベルの要素が混在する。また、当該要素自身も含むかもし れない。 </p>
    <p> 要素<gi>s</gi>が、ある単位の全体を完全に、入れ子なく示す場合には、 正書形の文や、他のテキスト部分を示すために使われるかもしれない。 </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="s-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Das <gi>s</gi>-Element wird verwendet um orthographische Sätze oder andere Textsegmente zu
      kodieren, vorausgesetzt das Segment ist lückenlos, vollständig und nicht verschachtelt. Für
      unvollständige oder rekursive Segmente soll stattdessen das <gi>seg</gi>-Element verwendet
      werden.</p>
    <p>Das <att>type</att>-Attribut wird verwendet, um den Segmenttyp entsprechend einer geeigneten
      Typologie anzugeben.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AILC"/>
    <ptr target="#TSSASE"/>
  </listRef>
```

^b26

