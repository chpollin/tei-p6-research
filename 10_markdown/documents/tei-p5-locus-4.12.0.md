---
type: representation
source-type: document
source: '[[00_sources/tei-p5-locus-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 locus
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/locus.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# locus

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11250. Git blob: `a3db3507c232b2088021f56145c317c75f245699`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="LOCUS" ident="locus">
  <gloss versionDate="2007-06-12" xml:lang="en">locus</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">locus</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="locus.desc">defines a location within a manuscript, manuscript part, or other object typically 
    as a (possibly discontinuous) sequence of folio references.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고의 일부 내에서 위치를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義一個手稿或手稿部分裡的位置，通常是用一系列的 (可能不連續的) 頁面參照。</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">手書き資料中の場所を定義する。一般には、(多くの場合不連続の)一連の折 丁参照による。</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">définit un emplacement au sein d'un manuscrit ou d'une
    partie de manuscrit, souvent une séquence, éventuellement discontinue, de références de
    feuillets.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una posición al interno de un manuscrito o de una
    de sus partes, generalmente como secuencia (no necesariamete contínua) de referencias de
    folios.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce una posizione all'interno di un manoscritto o
    di una sua parte, generalmente come sequenza (non necessariamete continua) di riferimenti di
    fogli</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
   <alternate minOccurs="0" maxOccurs="unbounded">
    <textNode/>
    <classRef key="model.gLike"/>
    <elementRef key="hi"/>
    <elementRef key="locus"/>
   </alternate>
  </content>
  <attList>
    <attDef ident="scheme">
      <gloss versionDate="2007-06-12" xml:lang="en">scheme</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">système</gloss>
      <desc versionDate="2013-12-21" xml:lang="en">identifies the foliation scheme in terms of which the location is being
        specified by pointing to some <gi>foliation</gi> element
	defining it, or to some other equivalent resource.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">명시된 위치를 정해 주는 책의 장 수 매김 방식을 규정한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明所指出位置的編頁架構。</desc>
      <desc versionDate="2008-04-06" xml:lang="ja">当該場所を指定するための折丁スキームを特定する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">désigne le système de foliotation utilisé pour
        localiser la subdivision du manuscrit qui est en cours de description.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica la foliación en base a la posición
        especificada.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica la foliazione in base alla posizione
        specificata</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="from">
      <gloss versionDate="2007-06-12" xml:lang="en">from</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">depuis</gloss>
      <desc versionDate="2013-12-21" xml:lang="en">specifies the
      starting point of the location in a normalized form, typically a
      page number.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">표준화된 형식의 위치에서 시작 지점을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用正規格式指明該位置的起始點。</desc>
      <desc versionDate="2008-04-06" xml:lang="ja">正規化された形で、当該場所の始点を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie, sous une forme normalisée, le point de
        départ de la localisation.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el punto de inicio de una localización en una
        forma estándard.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica l'inizio della posizione in forma
        normalizzata</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
    <attDef ident="to">
      <gloss versionDate="2007-06-12" xml:lang="en">to</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">jusqu'à</gloss>
      <desc versionDate="2013-12-21" xml:lang="en">specifies the
      end-point of the location in a normalized form, typically as a
      page number.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">표준화된 형식으로 종료 지점을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用正規格式指明該位置的結束點。</desc>
      <desc versionDate="2008-04-06" xml:lang="ja">正規化された形で、当該場所の終点を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie, sous une forme normalisée, la borne de fin
        pour la localisation.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el punto final de una localización en una
        forma estándard.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il termine della posizione in forma
        normalizzata</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-ne">
      <!-- within ms description -->
      <msItem n="1">
        <locus target="#F1r #F1v #F2r" from="1r" to="2r">ff. 1r-2r</locus>
        <author>Ben Jonson</author>
        <title>Ode to himself</title>
        <rubric rend="italics"> An Ode<lb/> to him selfe.</rubric>
        <incipit>Com leaue the loathed stage</incipit>
        <explicit>And see his chariot triumph ore his wayne.</explicit>
        <bibl><name>Beal</name>, <title>Index 1450-1625</title>, JnB 380</bibl>
      </msItem>
      <!-- within transcription ... -->
      <pb xml:id="F1r"/>
      <!-- ... -->
      <pb xml:id="F1v"/>
      <!-- ... -->
      <pb xml:id="F2r"/>
      <!-- ... -->
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-xz">
      <msItem n="1">
        <locus target="#fr_F1r #fr_F1v #fr_F2r">ff. 1r-2r</locus>
        <author>Ben Jonson</author>
        <title>Ode to himself</title>
        <rubric rend="italics"> An Ode<lb/> to him selfe.</rubric>
        <incipit>Com leaue the loathed stage</incipit>
        <explicit>And see his chariot triumph ore his wayne.</explicit>
        <bibl><name>Beal</name>, <title>Index 1450-1625</title>, JnB 380</bibl>
      </msItem>
      <pb xml:id="fr_F1r"/>
      <pb xml:id="fr_F1v"/>
      <pb xml:id="fr_F2r"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">The <att>facs</att> attribute is available globally when the <ident type="module">transcr</ident> module is included in a schema. It may be used to point directly to an
        image file, as in the following example: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-om">
      <msItem>
        <locus facs="images/08v.jpg images/09r.jpg images/09v.jpg images/10r.jpg images/10v.jpg">fols. 8v-10v</locus>
        <title>Birds Praise of Love</title>
        <bibl>
          <title>IMEV</title>
          <biblScope>1506</biblScope>
        </bibl>
      </msItem>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-yk">
      <locus target="#zh-tw_P12 #zh-tw_P13 #zh-tw_P14 #zh-tw_P16">fols 12-14, 16r</locus>
      <!-- ... -->
      <pb xml:id="zh-tw_P12"/>
      <pb xml:id="zh-tw_P13"/>
      <pb xml:id="zh-tw_P14"/>
      <pb xml:id="zh-tw_P15"/>
      <pb xml:id="zh-tw_P16"/>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>The <att>facs</att> attribute is available globally when the <ident type="module">transcr</ident> module is included in a schema. It may be used to point directly to an
      image file, as in the following example: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-yp">
      <msItem>
        <locus facs="images/08v.jpg images/09r.jpg images/09v.jpg images/10r.jpg images/10v.jpg">fols. 8v-10v</locus>
        <title>Birds Praise of Love</title>
        <bibl>
          <title>IMEV</title>
          <biblScope>1506</biblScope>
        </bibl>
      </msItem>
    </egXML>
  </exemplum>
  <remarks ident="locus-remarks" versionDate="2021-03-24" xml:lang="en">
    <p>The <att>target</att> attribute should only be used to point to
    elements that contain or indicate a transcription of the locus
    being described, as in the <q>Ben Jonson</q> example.</p>
    <p>To associate a <gi>locus</gi> element with a page image or
    other comparable representation, the global <att>facs</att>
    attribute should be used, as shown in the <q>Birds Praise of
    Love</q> example. The <att>facs</att> attribute may be used to
    indicate one or more image files, as in that example, or
    alternatively it may point to one or more appropriate XML
    elements, such as the <gi>surface</gi>, <gi>zone</gi>,
    <gi>graphic</gi>, or <gi>binaryObject</gi> elements.</p>
    <p>When a single page is being cited, use the <att>from</att> and
    <att>to</att> attributes with an identical value. When no clear
    endpoint is provided, the <att>from</att> attribute may be used
    without <att>to</att>; for example a citation such as <q>p.
    3ff</q> might be encoded <code>&lt;locus from="3"&gt;p.
    3ff&lt;/locus&gt;</code>.</p>
  </remarks>
  <remarks ident="locus-remarks" versionDate="2009-04-17" xml:lang="fr">
    <p>L'attribut <att>target</att> doit être utilisé uniquement pour pointer vers des éléments contenant ou référençant une transcription de la partie du manuscrit ainsi localisée, comme dans le premier exemple ci-dessus. Pour associer un élément <gi>locus</gi> avec l'image d'une page ou avec une autre représentation similaire, on doit utiliser l'attribut global <att>facs</att>, comme le montre le deuxième exemple. L'attribut <att>target</att> est déprécié pour établir un lien vers une image. On utilise l'attribut <att>facs</att>, soit pour établir un lien vers un ou plusieurs fichiers image, comme ci-dessus, soit pour pointer vers un ou plusieurs éléments dédiés, tels que
      <gi>surface</gi>, <gi>zone</gi>, <gi>graphic</gi> ou <gi>binaryObject</gi>.</p>
  </remarks>
  <listRef>
    <ptr target="#msloc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">locus</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">locus</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="locus.desc">defines a location within a manuscript, manuscript part, or other object typically 
    as a (possibly discontinuous) sequence of folio references.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고의 일부 내에서 위치를 정의한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義一個手稿或手稿部分裡的位置，通常是用一系列的 (可能不連續的) 頁面參照。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">手書き資料中の場所を定義する。一般には、(多くの場合不連続の)一連の折 丁参照による。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">définit un emplacement au sein d'un manuscrit ou d'une
    partie de manuscrit, souvent une séquence, éventuellement discontinue, de références de
    feuillets.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una posición al interno de un manuscrito o de una
    de sus partes, generalmente como secuencia (no necesariamete contínua) de referencias de
    folios.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce una posizione all'interno di un manoscritto o
    di una sua parte, generalmente come sequenza (non necessariamete continua) di riferimenti di
    fogli</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
   <alternate minOccurs="0" maxOccurs="unbounded">
    <textNode/>
    <classRef key="model.gLike"/>
    <elementRef key="hi"/>
    <elementRef key="locus"/>
   </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">scheme</gloss>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">système</gloss>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">identifies the foliation scheme in terms of which the location is being
        specified by pointing to some <gi>foliation</gi> element
	defining it, or to some other equivalent resource.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">명시된 위치를 정해 주는 책의 장 수 매김 방식을 규정한다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明所指出位置的編頁架構。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">当該場所を指定するための折丁スキームを特定する。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">désigne le système de foliotation utilisé pour
        localiser la subdivision du manuscrit qui est en cours de description.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica la foliación en base a la posición
        especificada.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica la foliazione in base alla posizione
        specificata</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">from</gloss>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">depuis</gloss>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">specifies the
      starting point of the location in a normalized form, typically a
      page number.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준화된 형식의 위치에서 시작 지점을 명시한다.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用正規格式指明該位置的起始點。</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">正規化された形で、当該場所の始点を示す。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie, sous une forme normalisée, le point de
        départ de la localisation.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el punto de inicio de una localización en una
        forma estándard.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica l'inizio della posizione in forma
        normalizzata</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">to</gloss>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">jusqu'à</gloss>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">specifies the
      end-point of the location in a normalized form, typically as a
      page number.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준화된 형식으로 종료 지점을 명시한다.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用正規格式指明該位置的結束點。</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">正規化された形で、当該場所の終点を示す。</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie, sous une forme normalisée, la borne de fin
        pour la localisation.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el punto final de una localización en una
        forma estándard.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il termine della posizione in forma
        normalizzata</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b41

### Block 42

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-ne">
      <!-- within ms description -->
      <msItem n="1">
        <locus target="#F1r #F1v #F2r" from="1r" to="2r">ff. 1r-2r</locus>
        <author>Ben Jonson</author>
        <title>Ode to himself</title>
        <rubric rend="italics"> An Ode<lb/> to him selfe.</rubric>
        <incipit>Com leaue the loathed stage</incipit>
        <explicit>And see his chariot triumph ore his wayne.</explicit>
        <bibl><name>Beal</name>, <title>Index 1450-1625</title>, JnB 380</bibl>
      </msItem>
      <!-- within transcription ... -->
      <pb xml:id="F1r"/>
      <!-- ... -->
      <pb xml:id="F1v"/>
      <!-- ... -->
      <pb xml:id="F2r"/>
      <!-- ... -->
    </egXML>
  </exemplum>
```

^b42

### Block 43

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-xz">
      <msItem n="1">
        <locus target="#fr_F1r #fr_F1v #fr_F2r">ff. 1r-2r</locus>
        <author>Ben Jonson</author>
        <title>Ode to himself</title>
        <rubric rend="italics"> An Ode<lb/> to him selfe.</rubric>
        <incipit>Com leaue the loathed stage</incipit>
        <explicit>And see his chariot triumph ore his wayne.</explicit>
        <bibl><name>Beal</name>, <title>Index 1450-1625</title>, JnB 380</bibl>
      </msItem>
      <pb xml:id="fr_F1r"/>
      <pb xml:id="fr_F1v"/>
      <pb xml:id="fr_F2r"/>
    </egXML>
  </exemplum>
```

^b43

### Block 44

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">The <att>facs</att> attribute is available globally when the <ident type="module">transcr</ident> module is included in a schema. It may be used to point directly to an
        image file, as in the following example: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-om">
      <msItem>
        <locus facs="images/08v.jpg images/09r.jpg images/09v.jpg images/10r.jpg images/10v.jpg">fols. 8v-10v</locus>
        <title>Birds Praise of Love</title>
        <bibl>
          <title>IMEV</title>
          <biblScope>1506</biblScope>
        </bibl>
      </msItem>
    </egXML>
  </exemplum>
```

^b44

### Block 45

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-yk">
      <locus target="#zh-tw_P12 #zh-tw_P13 #zh-tw_P14 #zh-tw_P16">fols 12-14, 16r</locus>
      <!-- ... -->
      <pb xml:id="zh-tw_P12"/>
      <pb xml:id="zh-tw_P13"/>
      <pb xml:id="zh-tw_P14"/>
      <pb xml:id="zh-tw_P15"/>
      <pb xml:id="zh-tw_P16"/>
    </egXML>
  </exemplum>
```

^b45

### Block 46

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <p>The <att>facs</att> attribute is available globally when the <ident type="module">transcr</ident> module is included in a schema. It may be used to point directly to an
      image file, as in the following example: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCUS-egXML-yp">
      <msItem>
        <locus facs="images/08v.jpg images/09r.jpg images/09v.jpg images/10r.jpg images/10v.jpg">fols. 8v-10v</locus>
        <title>Birds Praise of Love</title>
        <bibl>
          <title>IMEV</title>
          <biblScope>1506</biblScope>
        </bibl>
      </msItem>
    </egXML>
  </exemplum>
```

^b46

### Block 47

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="locus-remarks" versionDate="2021-03-24" xml:lang="en">
    <p>The <att>target</att> attribute should only be used to point to
    elements that contain or indicate a transcription of the locus
    being described, as in the <q>Ben Jonson</q> example.</p>
    <p>To associate a <gi>locus</gi> element with a page image or
    other comparable representation, the global <att>facs</att>
    attribute should be used, as shown in the <q>Birds Praise of
    Love</q> example. The <att>facs</att> attribute may be used to
    indicate one or more image files, as in that example, or
    alternatively it may point to one or more appropriate XML
    elements, such as the <gi>surface</gi>, <gi>zone</gi>,
    <gi>graphic</gi>, or <gi>binaryObject</gi> elements.</p>
    <p>When a single page is being cited, use the <att>from</att> and
    <att>to</att> attributes with an identical value. When no clear
    endpoint is provided, the <att>from</att> attribute may be used
    without <att>to</att>; for example a citation such as <q>p.
    3ff</q> might be encoded <code>&lt;locus from="3"&gt;p.
    3ff&lt;/locus&gt;</code>.</p>
  </remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="locus-remarks" versionDate="2009-04-17" xml:lang="fr">
    <p>L'attribut <att>target</att> doit être utilisé uniquement pour pointer vers des éléments contenant ou référençant une transcription de la partie du manuscrit ainsi localisée, comme dans le premier exemple ci-dessus. Pour associer un élément <gi>locus</gi> avec l'image d'une page ou avec une autre représentation similaire, on doit utiliser l'attribut global <att>facs</att>, comme le montre le deuxième exemple. L'attribut <att>target</att> est déprécié pour établir un lien vers une image. On utilise l'attribut <att>facs</att>, soit pour établir un lien vers un ou plusieurs fichiers image, comme ci-dessus, soit pour pointer vers un ou plusieurs éléments dédiés, tels que
      <gi>surface</gi>, <gi>zone</gi>, <gi>graphic</gi> ou <gi>binaryObject</gi>.</p>
  </remarks>
```

^b48

### Block 49

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msloc"/>
  </listRef>
```

^b49

