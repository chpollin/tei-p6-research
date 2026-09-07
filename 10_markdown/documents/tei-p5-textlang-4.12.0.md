---
type: representation
source-type: document
source: '[[00_sources/tei-p5-textlang-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 textLang
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/textLang.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# textLang

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7223. Git blob: `53a4cc90b8eb5ab2899bb3d2cc7bb165799dfa67`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="TEXTLANG" ident="textLang">
  <gloss versionDate="2007-07-04" xml:lang="en">text language</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 언어</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">lengua del texto</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">langues du texte</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">lingua del testo</gloss>
  <desc versionDate="2011-12-07" xml:lang="en" xml:id="textlang.desc">describes the languages and writing systems identified within the bibliographic work  
  being described, rather than its description.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">(<gi>langUsage</gi>에 기술된 기술과 반대로) 원고에서 사용된 언어와 글 체계를
    기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述手稿中所使用的語言和書寫系統 (相對於其描述時使用的<gi>語言使用</gi>元素) 。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料中の言語や書記システムを示す。(要素<gi>langUsage</gi>にあ る情報と対位する)</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit les langues et systèmes d'écriture utilisés dans
    un manuscrit (et non dans la description du manuscrit, dont les langues et systèmes d'écriture
    sont décrits dans l'élément <gi>langUsage</gi>).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe las lenguas y los sistemas de escritura usados
    en un manuscrito (no se ha de confundir con la descripción contenida en el elemento
      <gi>langUsage</gi>. ****</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive le lingue e i sistemi di scrittura usati da un
    manoscritto (da non confondere con la descrizione contenuta nell'elemento <gi>langUsage</gi></desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.msItemPart"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <attList>
    <attDef ident="mainLang">
      <gloss versionDate="2007-07-04" xml:lang="en">main language</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">주요 언어</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
      <gloss versionDate="2008-04-06" xml:lang="es">lengua principal</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">langue principale</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">lingua principale</gloss>
      <desc versionDate="2011-12-05" xml:lang="en">supplies a code which identifies the chief language used in the bibliographic work.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">원고에 사용된 주요 언어를 식별하는 부호를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一代碼，識別手稿中使用的主要語言。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料中で主に使用される言語を特定するコードを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">contient un code identifiant la langue principale du
        manuscrit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un código que identifica la lengua
        principal utilizada en el manuscrito.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un codice che identifica la lingua principale
        utilizzata nel manoscritto</desc>
      <datatype><dataRef key="teidata.language"/></datatype>
    </attDef>
    <attDef ident="otherLangs">
      <gloss versionDate="2007-07-04" xml:lang="en">other languages</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">다른 언어</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
      <gloss versionDate="2008-04-06" xml:lang="es">otras lenguas</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">autres langues</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">altre lingue</gloss>
      <desc versionDate="2011-12-05" xml:lang="en">one or more codes identifying any other languages used in the bibliographic work.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">원고에 사용된 다른 언어를 식별하는 하나 이상의 부호</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">一個或多個代碼識別手稿中使用的任何其他語言。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料中で使用されている他の言語を特定する、ひとつ以上の コード。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">contient un ou plusieurs codes identifiant toute
        autre langue utilisée dans le manuscrit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">uno o más códigos que identifican otras eventuales
        lenguas utilizadas en el manuscrito.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">uno o più codici che identificano eventuali altre
        lingue utilizzate nel manoscritto</desc>
      <datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.language"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="TEXTLANG-egXML-rt">
      <textLang mainLang="en" otherLangs="la"> Predominantly in English with Latin
      glosses</textLang>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="TEXTLANG-egXML-zi">
      <textLang mainLang="en" otherLangs="la"> En français essentiellement, avec des gloses en
          latin.</textLang>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="TEXTLANG-egXML-nu">
      <textLang mainLang="en" otherLangs="la"> 主要為英文，摻以拉丁字彙。</textLang>
    </egXML>
  </exemplum>
  <remarks ident="textLang-remarks" versionDate="2013-11-20" xml:lang="en">
    <p>This element should not be used to document the
languages or writing systems used for the bibliographic or manuscript description itself: as for
all other TEI elements, such information should be provided by means of the
global <att>xml:lang</att> attribute attached to the element
containing the description. </p>
<p>In all cases, languages should be identified by means of a standardized
<soCalled>language tag</soCalled> generated according to <ref target="https://tools.ietf.org/html/bcp47">BCP 47</ref>. Additional
documentation for the language may be provided by a <gi>language</gi>
element in the TEI header.
</p>
  </remarks>
  <listRef>
    <ptr target="#COBICOI"/>
    <ptr target="#mslangs"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">text language</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">텍스트 언어</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">lengua del texto</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">langues du texte</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">lingua del testo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-12-07" xml:lang="en" xml:id="textlang.desc">describes the languages and writing systems identified within the bibliographic work  
  being described, rather than its description.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">(<gi>langUsage</gi>에 기술된 기술과 반대로) 원고에서 사용된 언어와 글 체계를
    기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述手稿中所使用的語言和書寫系統 (相對於其描述時使用的<gi>語言使用</gi>元素) 。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料中の言語や書記システムを示す。(要素<gi>langUsage</gi>にあ る情報と対位する)</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit les langues et systèmes d'écriture utilisés dans
    un manuscrit (et non dans la description du manuscrit, dont les langues et systèmes d'écriture
    sont décrits dans l'élément <gi>langUsage</gi>).</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe las lenguas y los sistemas de escritura usados
    en un manuscrito (no se ha de confundir con la descripción contenida en el elemento
      <gi>langUsage</gi>. ****</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive le lingue e i sistemi di scrittura usati da un
    manoscritto (da non confondere con la descrizione contenuta nell'elemento <gi>langUsage</gi></desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.msItemPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">main language</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">주요 언어</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">lengua principal</gloss>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">langue principale</gloss>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">lingua principale</gloss>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-12-05" xml:lang="en">supplies a code which identifies the chief language used in the bibliographic work.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고에 사용된 주요 언어를 식별하는 부호를 제공한다.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一代碼，識別手稿中使用的主要語言。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料中で主に使用される言語を特定するコードを示す。</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un code identifiant la langue principale du
        manuscrit.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un código que identifica la lengua
        principal utilizada en el manuscrito.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un codice che identifica la lingua principale
        utilizzata nel manoscritto</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.language"/></datatype>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">other languages</gloss>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">다른 언어</gloss>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">otras lenguas</gloss>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">autres langues</gloss>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">altre lingue</gloss>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2011-12-05" xml:lang="en">one or more codes identifying any other languages used in the bibliographic work.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고에 사용된 다른 언어를 식별하는 하나 이상의 부호</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">一個或多個代碼識別手稿中使用的任何其他語言。</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料中で使用されている他の言語を特定する、ひとつ以上の コード。</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un ou plusieurs codes identifiant toute
        autre langue utilisée dans le manuscrit.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">uno o más códigos que identifican otras eventuales
        lenguas utilizadas en el manuscrito.</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">uno o più codici che identificano eventuali altre
        lingue utilizzate nel manoscritto</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.language"/></datatype>
```

^b43

### Block 44

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="TEXTLANG-egXML-rt">
      <textLang mainLang="en" otherLangs="la"> Predominantly in English with Latin
      glosses</textLang>
    </egXML>
  </exemplum>
```

^b44

### Block 45

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="TEXTLANG-egXML-zi">
      <textLang mainLang="en" otherLangs="la"> En français essentiellement, avec des gloses en
          latin.</textLang>
    </egXML>
  </exemplum>
```

^b45

### Block 46

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="TEXTLANG-egXML-nu">
      <textLang mainLang="en" otherLangs="la"> 主要為英文，摻以拉丁字彙。</textLang>
    </egXML>
  </exemplum>
```

^b46

### Block 47

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="textLang-remarks" versionDate="2013-11-20" xml:lang="en">
    <p>This element should not be used to document the
languages or writing systems used for the bibliographic or manuscript description itself: as for
all other TEI elements, such information should be provided by means of the
global <att>xml:lang</att> attribute attached to the element
containing the description. </p>
<p>In all cases, languages should be identified by means of a standardized
<soCalled>language tag</soCalled> generated according to <ref target="https://tools.ietf.org/html/bcp47">BCP 47</ref>. Additional
documentation for the language may be provided by a <gi>language</gi>
element in the TEI header.
</p>
  </remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOI"/>
    <ptr target="#mslangs"/>
  </listRef>
```

^b48

