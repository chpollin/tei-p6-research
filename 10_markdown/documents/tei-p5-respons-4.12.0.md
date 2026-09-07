---
type: representation
source-type: document
source: '[[00_sources/tei-p5-respons-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 respons
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/respons.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# respons

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10289. Git blob: `9f65d67d32c6dc0b9e0878623dcd26835bae2e83`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="certainty" xml:id="gi-respons" ident="respons">
  <gloss versionDate="2005-01-14" xml:lang="en">responsibility</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">책임성</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">責任</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">Responsabilité</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">responsabilidad</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">responsabilità</gloss>
  <desc versionDate="2013-06-19" xml:lang="en">identifies the individual(s) responsible for some aspect of the content or
markup of particular element(s).</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">특정 요소의 마크업에 대한 책임이 있는 개인 또는 개인들을 지저정한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出標記一或多個特定元素某部分的負責人。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ある要素の決定に責任のある個人を特定する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">identifie le ou les personne(s) responsable(s) d'un
      aspect du balisage pour un ou plusieurs éléments particuliers.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">Identifica la responsabilidad individual/es de algún aspecto del marcaje de un elemento/s particular.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica i soggetti responsabili della codifica di determinati elementi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.scoping"/>
    <memberOf key="model.certLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="locus" usage="req">
      <desc versionDate="2013-06-19" xml:lang="en">indicates the specific aspect of the encoding (markup or
      content) for which responsibility is being assigned.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">책임성이 할당된 명시적인 마크업을 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出標記責任所屬的特定部分。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該責任を示すマークアップが何についてのものかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique l'aspect spécifique du balisage sur lequel porte la responsabilité.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el aspecto específico del marcaje por el cual la responsabilidad está siendo asignada</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'aspetto specifico della codifica per il qaule è attribuita la responsabilità.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="name">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the name of the element
          or attribute used.</desc>
        </valItem>
        <valItem ident="start">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the start of the element
          concerned.</desc>
        </valItem>
        <valItem ident="end">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the end of the element
          concerned.</desc>
        </valItem>
        <valItem ident="location">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the location of the element
          concerned.</desc>
        </valItem>
        <valItem ident="value">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the content (for an element) or
          the value (for an attribute)</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-az" source="#UND">
      <respons target="#p1" locus="name location" resp="#encoder1"/>
      <respons target="#p2" match="@rend" locus="value" resp="#encoder2"/>
      <list type="encoders">
        <item xml:id="encoder1"/>
        <item xml:id="encoder2"/>
      </list>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-jn" source="#UND">
      <respons target="#fr_p1" locus="name location" resp="#fr_encoder1"/>
      <respons target="#fr_p2" locus="value" resp="#fr_encoder2"/>
      <list type="encoders">
        <item xml:id="fr_encoder1"/>
        <item xml:id="fr_encoder2"/>
      </list>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-st" source="#UND">
      <respons target="#zh-tw_p1" locus="name location" resp="#zh-tw_encoder1"/>
      <respons target="#zh-tw_p2" match="@rend" locus="value" resp="#zh-tw_encoder2"/>
      <list type="編碼員">
        <item xml:id="zh-tw_編碼員1"/>
        <item xml:id="zh-tw_編碼員2"/>
      </list>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>In this (partially fictional) example the entire document was
    transcribed and encoded by a single encoder, except for one passage
    which was transcribed and encoded by the proofreader.</p>
    <!-- source: Michael Satlow's Inscriptions of Israel and Palestine, 'sepp0021' -->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-hp">
      <!-- in the <teiHeader>: -->
      <respStmt xml:id="enc01">
        <name>C. Colin Backslash</name>
        <resp>transcription</resp>
        <resp>encoding</resp>
      </respStmt>
      <respStmt xml:id="prf01">
        <name>Erin Spelling</name>
        <resp>proofreading</resp>
      </respStmt>
      <!-- in the <text>: -->
      <p>Θερινὴ τροπή
        <lb/>
            <foreign xml:lang="hbo" xml:id="mp0a8">
          ת
          <supplied reason="undefined">קו</supplied>
               <unclear>פ</unclear>
          ת תמוז
        </foreign>
         </p>
      <!-- elsewhere: -->
      <respons target="#mp0a8" locus="name value" resp="#prf01"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>In this (partially fictional) example an initial encoder
    (<quote>across.dta</quote>) encoded most of the document; a later
    encoder (<quote>rcapolung.ewo</quote>) encoded a particular
    passage; and a third encoder (<quote>sbauman.emt</quote>) fixed
    some of that encoding.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-pt" source="#RESPONS-eg-02">
      <!-- in the <teiHeader>: -->
      <respStmt xml:id="enc03">
        <persName ref="../contextual/persons.xml#across.dta"/>
        <resp>encoding</resp>
      </respStmt>
      <!-- in the <text>: -->
      <spGrp rend="braced(atonce1)" xml:id="sgrp05">
        <sp who="#mo">
          <speaker rend="align(left)slant(italic)"><persName>Mor</persName>.</speaker>
          <p rend="break(no)">So, so, so!</p>
        </sp>
        <sp who="#hg">
          <speaker rend="align(left)slant(italic)"><persName>Mr. H</persName>.</speaker>
          <p rend="break(no)">What, without my Leave!</p>
        </sp>
        <sp who="#la">
          <speaker rend="align(left)slant(italic)"><persName>Lady D</persName>.</speaker>
          <p rend="break(no)">Amazing!</p>
        </sp>
      </spGrp>
      <stage rend="align(right)slant(italic)" type="delivery" xml:id="atonce1">All together.</stage>
      <!-- anywhere: -->
      <respons target="#sgrp05" locus="name" resp="../contextual/persons.xml#rcapolung.ewo">
        <desc>Ashley did not know what to do with this; I have decided it
    best fits as a braced <gi>spGrp</gi></desc>
      </respons>
      <respons target="#sgrp05" match=".//@rend" locus="value" resp="../contextual/persons.xml#sbauman.emt">
        <desc>fixed <att>rend</att> attributes</desc>
      </respons>
    </egXML>
  </exemplum>
  <remarks ident="respons-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>respons</gi> element is designed for cases in which
fine-grained information about specific aspects of the markup of a text
is desirable for whatever reason.  Global responsibility for certain
aspects of markup is usually more simply indicated in the TEI header,
using the <gi>respStmt</gi> element within the title statement, edition
statement, or change log.</p>
  </remarks>
  <remarks ident="respons-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'élément <gi>respons</gi> est préconisé dans les cas où une information très fine
                sur des aspects spécifiques du balisage d'un texte est souhaitable pour une raison
                quelconque. Une responsabilité globale pour certains aspects du balisage est
                habituellement indiquée simplement au niveau de l'en-tête TEI en utilisant l'élément
                    <gi>respStmt</gi> dans la mention de titre, la mention d'édition ou le journal
                de modifications.</p>
  </remarks>
  <remarks ident="respons-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素<gi>respons</gi>は、テキスト中のある特定要素について、詳細
    な情報を示すためのものである。全体的な責任については、ヘダー中にあ
    るタイトルや版、変更履歴に関するタグの中で使われる要素
    <gi>respStmt</gi>で示されるのが一般的である。
    </p>
  </remarks>
  <listRef>
    <ptr target="#CERESP"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">responsibility</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">책임성</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">責任</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">Responsabilité</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">responsabilidad</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">responsabilità</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-06-19" xml:lang="en">identifies the individual(s) responsible for some aspect of the content or
markup of particular element(s).</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">특정 요소의 마크업에 대한 책임이 있는 개인 또는 개인들을 지저정한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出標記一或多個特定元素某部分的負責人。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ある要素の決定に責任のある個人を特定する。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">identifie le ou les personne(s) responsable(s) d'un
      aspect du balisage pour un ou plusieurs éléments particuliers.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">Identifica la responsabilidad individual/es de algún aspecto del marcaje de un elemento/s particular.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica i soggetti responsabili della codifica di determinati elementi.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.scoping"/>
    <memberOf key="model.certLike"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.descLike"/>
      <classRef key="model.certLike"/>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-06-19" xml:lang="en">indicates the specific aspect of the encoding (markup or
      content) for which responsibility is being assigned.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">책임성이 할당된 명시적인 마크업을 표시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出標記責任所屬的特定部分。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該責任を示すマークアップが何についてのものかを示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique l'aspect spécifique du balisage sur lequel porte la responsabilité.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el aspecto específico del marcaje por el cual la responsabilidad está siendo asignada</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'aspetto specifico della codifica per il qaule è attribuita la responsabilità.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="name">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the name of the element
          or attribute used.</desc>
        </valItem>
        <valItem ident="start">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the start of the element
          concerned.</desc>
        </valItem>
        <valItem ident="end">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the end of the element
          concerned.</desc>
        </valItem>
        <valItem ident="location">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the location of the element
          concerned.</desc>
        </valItem>
        <valItem ident="value">
          <desc versionDate="2009-06-07" xml:lang="en">responsibility is being assigned concerning the content (for an element) or
          the value (for an attribute)</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-az" source="#UND">
      <respons target="#p1" locus="name location" resp="#encoder1"/>
      <respons target="#p2" match="@rend" locus="value" resp="#encoder2"/>
      <list type="encoders">
        <item xml:id="encoder1"/>
        <item xml:id="encoder2"/>
      </list>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-jn" source="#UND">
      <respons target="#fr_p1" locus="name location" resp="#fr_encoder1"/>
      <respons target="#fr_p2" locus="value" resp="#fr_encoder2"/>
      <list type="encoders">
        <item xml:id="fr_encoder1"/>
        <item xml:id="fr_encoder2"/>
      </list>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-st" source="#UND">
      <respons target="#zh-tw_p1" locus="name location" resp="#zh-tw_encoder1"/>
      <respons target="#zh-tw_p2" match="@rend" locus="value" resp="#zh-tw_encoder2"/>
      <list type="編碼員">
        <item xml:id="zh-tw_編碼員1"/>
        <item xml:id="zh-tw_編碼員2"/>
      </list>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <p>In this (partially fictional) example the entire document was
    transcribed and encoded by a single encoder, except for one passage
    which was transcribed and encoded by the proofreader.</p>
    <!-- source: Michael Satlow's Inscriptions of Israel and Palestine, 'sepp0021' -->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-hp">
      <!-- in the <teiHeader>: -->
      <respStmt xml:id="enc01">
        <name>C. Colin Backslash</name>
        <resp>transcription</resp>
        <resp>encoding</resp>
      </respStmt>
      <respStmt xml:id="prf01">
        <name>Erin Spelling</name>
        <resp>proofreading</resp>
      </respStmt>
      <!-- in the <text>: -->
      <p>Θερινὴ τροπή
        <lb/>
            <foreign xml:lang="hbo" xml:id="mp0a8">
          ת
          <supplied reason="undefined">קו</supplied>
               <unclear>פ</unclear>
          ת תמוז
        </foreign>
         </p>
      <!-- elsewhere: -->
      <respons target="#mp0a8" locus="name value" resp="#prf01"/>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <p>In this (partially fictional) example an initial encoder
    (<quote>across.dta</quote>) encoded most of the document; a later
    encoder (<quote>rcapolung.ewo</quote>) encoded a particular
    passage; and a third encoder (<quote>sbauman.emt</quote>) fixed
    some of that encoding.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respons-egXML-pt" source="#RESPONS-eg-02">
      <!-- in the <teiHeader>: -->
      <respStmt xml:id="enc03">
        <persName ref="../contextual/persons.xml#across.dta"/>
        <resp>encoding</resp>
      </respStmt>
      <!-- in the <text>: -->
      <spGrp rend="braced(atonce1)" xml:id="sgrp05">
        <sp who="#mo">
          <speaker rend="align(left)slant(italic)"><persName>Mor</persName>.</speaker>
          <p rend="break(no)">So, so, so!</p>
        </sp>
        <sp who="#hg">
          <speaker rend="align(left)slant(italic)"><persName>Mr. H</persName>.</speaker>
          <p rend="break(no)">What, without my Leave!</p>
        </sp>
        <sp who="#la">
          <speaker rend="align(left)slant(italic)"><persName>Lady D</persName>.</speaker>
          <p rend="break(no)">Amazing!</p>
        </sp>
      </spGrp>
      <stage rend="align(right)slant(italic)" type="delivery" xml:id="atonce1">All together.</stage>
      <!-- anywhere: -->
      <respons target="#sgrp05" locus="name" resp="../contextual/persons.xml#rcapolung.ewo">
        <desc>Ashley did not know what to do with this; I have decided it
    best fits as a braced <gi>spGrp</gi></desc>
      </respons>
      <respons target="#sgrp05" match=".//@rend" locus="value" resp="../contextual/persons.xml#sbauman.emt">
        <desc>fixed <att>rend</att> attributes</desc>
      </respons>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="respons-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>respons</gi> element is designed for cases in which
fine-grained information about specific aspects of the markup of a text
is desirable for whatever reason.  Global responsibility for certain
aspects of markup is usually more simply indicated in the TEI header,
using the <gi>respStmt</gi> element within the title statement, edition
statement, or change log.</p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="respons-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'élément <gi>respons</gi> est préconisé dans les cas où une information très fine
                sur des aspects spécifiques du balisage d'un texte est souhaitable pour une raison
                quelconque. Une responsabilité globale pour certains aspects du balisage est
                habituellement indiquée simplement au niveau de l'en-tête TEI en utilisant l'élément
                    <gi>respStmt</gi> dans la mention de titre, la mention d'édition ou le journal
                de modifications.</p>
  </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="respons-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素<gi>respons</gi>は、テキスト中のある特定要素について、詳細
    な情報を示すためのものである。全体的な責任については、ヘダー中にあ
    るタイトルや版、変更履歴に関するタグの中で使われる要素
    <gi>respStmt</gi>で示されるのが一般的である。
    </p>
  </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CERESP"/>
  </listRef>
```

^b33

