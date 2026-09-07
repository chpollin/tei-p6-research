---
type: representation
source-type: document
source: '[[00_sources/tei-p5-explicit-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 explicit
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/explicit.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# explicit

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3691. Git blob: `dcaa77d2d413282d91ec2df46848a8b0c6fc19dc`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="EXPLICIT" ident="explicit">
  <gloss versionDate="2007-06-12" xml:lang="en">explicit</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">explicit</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="explicit.desc">contains the  <term>explicit</term> of a
item, that is, the closing words of the text proper, exclusive of any rubric or colophon which might follow it.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 <term>explicit</term>(끝 말)을 포함한다, 즉, 이어 나타날 수 있는 주서 또는 판권 페이지를 제외한 텍스트의 마무리 단어</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿項目中的 <term>結尾語</term>，即文本完成時的結尾語，不包含可能出現在其後的按語或版權頁標記。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の<term>巻末語句(explicit)</term>を示す。すなわち、当該テ
  キストの終了を示す語句のことである。これは、朱書き部分(rubric)やコロ
  フォン(奥付情報)とは異なる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient l'<term>explicit</term> d'une section d'un
      manuscrit, c'est-à-dire les mots terminant le texte proprement dit, à l'exclusion de toute
      rubrique ou colophon qui pourraient le suivre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el <term>explicit</term> de un manuscrito, es decir, las palabras de clausura del texto como tal, a excepción de las eventuales rúbricas o colofón sucesivos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene l' <term>explicit</term> di un manoscritto, ovvero le parole di chiusura del testo vero e proprio, a esclusione di eventuali titoli in rosso o colophon successivi.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="EXPLICIT-egXML-cz">
      <explicit>sed libera nos a malo.</explicit>
      <rubric>Hic explicit oratio qui dicitur dominica.</rubric>
      <explicit type="defective">ex materia quasi et forma sibi 
proporti<gap/>
         </explicit>
      <explicit type="reverse">saued be shulle that doome of day the at 
</explicit>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="EXPLICIT-egXML-bh">
      <explicit>sed libera nos a malo.</explicit>
      <rubric>Hic explicit oratio qui dicitur dominica.</rubric>
      <explicit type="defective">ex materia quasi et forma sibi proporti<gap/>
         </explicit>
      <explicit type="reverse">saued be shulle that doome of day the at</explicit>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="EXPLICIT-egXML-np">
      <explicit>佛說是經已。諸比丘聞佛所說。歡喜奉行。</explicit>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mscoit"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">explicit</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">explicit</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="explicit.desc">contains the  <term>explicit</term> of a
item, that is, the closing words of the text proper, exclusive of any rubric or colophon which might follow it.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 <term>explicit</term>(끝 말)을 포함한다, 즉, 이어 나타날 수 있는 주서 또는 판권 페이지를 제외한 텍스트의 마무리 단어</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿項目中的 <term>結尾語</term>，即文本完成時的結尾語，不包含可能出現在其後的按語或版權頁標記。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の<term>巻末語句(explicit)</term>を示す。すなわち、当該テ
  キストの終了を示す語句のことである。これは、朱書き部分(rubric)やコロ
  フォン(奥付情報)とは異なる。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient l'<term>explicit</term> d'une section d'un
      manuscrit, c'est-à-dire les mots terminant le texte proprement dit, à l'exclusion de toute
      rubrique ou colophon qui pourraient le suivre.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el <term>explicit</term> de un manuscrito, es decir, las palabras de clausura del texto como tal, a excepción de las eventuales rúbricas o colofón sucesivos.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene l' <term>explicit</term> di un manoscritto, ovvero le parole di chiusura del testo vero e proprio, a esclusione di eventuali titoli in rosso o colophon successivi.</desc>
```

^b9

### Block 10

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

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="EXPLICIT-egXML-cz">
      <explicit>sed libera nos a malo.</explicit>
      <rubric>Hic explicit oratio qui dicitur dominica.</rubric>
      <explicit type="defective">ex materia quasi et forma sibi 
proporti<gap/>
         </explicit>
      <explicit type="reverse">saued be shulle that doome of day the at 
</explicit>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="EXPLICIT-egXML-bh">
      <explicit>sed libera nos a malo.</explicit>
      <rubric>Hic explicit oratio qui dicitur dominica.</rubric>
      <explicit type="defective">ex materia quasi et forma sibi proporti<gap/>
         </explicit>
      <explicit type="reverse">saued be shulle that doome of day the at</explicit>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="EXPLICIT-egXML-np">
      <explicit>佛說是經已。諸比丘聞佛所說。歡喜奉行。</explicit>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mscoit"/>
  </listRef>
```

^b15

