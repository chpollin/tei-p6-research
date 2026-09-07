---
type: representation
source-type: document
source: '[[00_sources/tei-p5-incipit-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 incipit
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/incipit.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# incipit

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4919. Git blob: `5ad1c8dbe5335186858156252434e102e7bf15e5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="INCIPIT" ident="incipit">
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="incipit.desc">contains the <term>incipit</term> of a manuscript or similar object item, that is the opening words of the text proper, exclusive of any <term>rubric</term> which might precede it, of sufficient length to identify the work uniquely; such incipits were, in former times, frequently used a means of reference to a work, in place of a title.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 항목의 <term>incipit</term>(시작 말)을 포함한다. 선행하는 <term>rubric</term>를 제외한 텍스트의 시작 단어이며, 그 작품을 고유하게 식별할 수 있는 충분한 방식이다; 이러한 시작은 제목 대신 작품 참조의 수단으로 예전에 사용되었다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿項目中的<term>起始語</term>，即文本開端的起始語，不包括可能出現在之前的<term>按語</term>，並以充分的文字來獨家識別該作品；早期，這種起始語常用為作品的參照工具，出現在標題部份。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の<term>冒頭語句(incipit)</term>を示す。冒頭語句とは、テキ
  ストの書き出しにある語句で、これに先行してある朱書き部分を除いた、当
  該作品を特定するに充分な文量の部分である。
  冒頭語句は、タイトル部分において、作品への参照を示す手段としてよく使
  用されていた。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient l'<term>incipit</term> d'une section d'un
      manuscrit, c'est-à-dire les mots commençant le texte proprement dit, à l'exclusion de toute
        <term>rubrique</term> qui pourrait les précéder, la transcription étant de longueur
      suffisante pour permettre l'identification de l'œuvre. De tels incipit étaient autrefois
      souvent utilisés à la place du titre de l'œuvre, pour l'identifier.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el <term>incipit</term> de un manuscrito, es decir, las primeras palabras del texto propriamente dicho, a excepción de eventuales <term>títulos en rojo</term> que lo preceden; los incipit tienen una longitud a deteminar según de que obra se trate y, antiguamente, eran utilizados a menudo para referirse a las obras mismas en lugar de títulos eventuales.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene l' <term>incipit</term> di un manoscritto, cioè le prime parole del testo propriamente detto, a eccezione di eventuali <term>titoli in rosso</term> che lo precedono; gli incipit hanno una lunghezza sufficiente a deteminare di quale opera si tratti e, anticamente, erano spesso utilizzati per riferirsi alle opere stesse al posto di eventuali titoli.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.msQuoteLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="INCIPIT-egXML-dx">
      <incipit>Pater noster qui es in celis</incipit>
      <incipit defective="true">tatem dedit hominibus alleluia.</incipit>
      <incipit type="biblical">Ghif ons huden onse dagelix broet</incipit>
      <incipit>O ongehoerde gewerdighe christi</incipit>
      <incipit type="lemma">Firmiter</incipit>
      <incipit>Ideo dicit firmiter quia ordo fidei nostre probari non potest</incipit>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="INCIPIT-egXML-ym">
      <incipit>Pater noster qui es in celis</incipit>
      <incipit defective="true">tatem dedit hominibus alleluia.</incipit>
      <incipit type="biblical">Ghif ons huden onse dagelix broet</incipit>
      <incipit>O ongehoerde gewerdighe christi</incipit>
      <incipit type="lemma">Firmiter</incipit>
      <incipit>Ideo dicit firmiter quia ordo fidei nostre probari non potest</incipit>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="INCIPIT-egXML-iq">
      <incipit>大學之道在明明德</incipit>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mscoit"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="incipit.desc">contains the <term>incipit</term> of a manuscript or similar object item, that is the opening words of the text proper, exclusive of any <term>rubric</term> which might precede it, of sufficient length to identify the work uniquely; such incipits were, in former times, frequently used a means of reference to a work, in place of a title.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 항목의 <term>incipit</term>(시작 말)을 포함한다. 선행하는 <term>rubric</term>를 제외한 텍스트의 시작 단어이며, 그 작품을 고유하게 식별할 수 있는 충분한 방식이다; 이러한 시작은 제목 대신 작품 참조의 수단으로 예전에 사용되었다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿項目中的<term>起始語</term>，即文本開端的起始語，不包括可能出現在之前的<term>按語</term>，並以充分的文字來獨家識別該作品；早期，這種起始語常用為作品的參照工具，出現在標題部份。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の<term>冒頭語句(incipit)</term>を示す。冒頭語句とは、テキ
  ストの書き出しにある語句で、これに先行してある朱書き部分を除いた、当
  該作品を特定するに充分な文量の部分である。
  冒頭語句は、タイトル部分において、作品への参照を示す手段としてよく使
  用されていた。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient l'<term>incipit</term> d'une section d'un
      manuscrit, c'est-à-dire les mots commençant le texte proprement dit, à l'exclusion de toute
        <term>rubrique</term> qui pourrait les précéder, la transcription étant de longueur
      suffisante pour permettre l'identification de l'œuvre. De tels incipit étaient autrefois
      souvent utilisés à la place du titre de l'œuvre, pour l'identifier.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el <term>incipit</term> de un manuscrito, es decir, las primeras palabras del texto propriamente dicho, a excepción de eventuales <term>títulos en rojo</term> que lo preceden; los incipit tienen una longitud a deteminar según de que obra se trate y, antiguamente, eran utilizados a menudo para referirse a las obras mismas en lugar de títulos eventuales.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene l' <term>incipit</term> di un manoscritto, cioè le prime parole del testo propriamente detto, a eccezione di eventuali <term>titoli in rosso</term> che lo precedono; gli incipit hanno una lunghezza sufficiente a deteminare di quale opera si tratti e, anticamente, erano spesso utilizzati per riferirsi alle opere stesse al posto di eventuali titoli.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.msQuoteLike"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="INCIPIT-egXML-dx">
      <incipit>Pater noster qui es in celis</incipit>
      <incipit defective="true">tatem dedit hominibus alleluia.</incipit>
      <incipit type="biblical">Ghif ons huden onse dagelix broet</incipit>
      <incipit>O ongehoerde gewerdighe christi</incipit>
      <incipit type="lemma">Firmiter</incipit>
      <incipit>Ideo dicit firmiter quia ordo fidei nostre probari non potest</incipit>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="INCIPIT-egXML-ym">
      <incipit>Pater noster qui es in celis</incipit>
      <incipit defective="true">tatem dedit hominibus alleluia.</incipit>
      <incipit type="biblical">Ghif ons huden onse dagelix broet</incipit>
      <incipit>O ongehoerde gewerdighe christi</incipit>
      <incipit type="lemma">Firmiter</incipit>
      <incipit>Ideo dicit firmiter quia ordo fidei nostre probari non potest</incipit>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="INCIPIT-egXML-iq">
      <incipit>大學之道在明明德</incipit>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mscoit"/>
  </listRef>
```

^b13

