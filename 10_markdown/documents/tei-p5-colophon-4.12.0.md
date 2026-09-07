---
type: representation
source-type: document
source: '[[00_sources/tei-p5-colophon-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 colophon
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/colophon.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# colophon

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4993. Git blob: `e76877beae5dda8926b1b50106b6eae0eea8ff29`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="COLOPHON" ident="colophon">
  <gloss versionDate="2007-06-12" xml:lang="en">colophon</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">colophon</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="colophon.desc">contains the  <term>colophon</term>
of an item: that is, a statement providing information regarding the date, place, agency, or reason for production of the manuscript or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 <term>colophon</term>(판권 표지 장)를 포함한다; 즉, 원고 생산에 대한 날짜, 장소, 대리권, 또는 이유와 관련한 정보를 제공하는 서술</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個手稿項目的 <term>版權頁標記</term>：即提供日期、地點、代理機構、或手稿產生原因等資訊的聲明。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料の<term>コロフォン(奥付情報)</term>を示す。例えば、制
  作の日時、場所、主体、制作主体、制作理由など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le <term>colophon</term> d'une section d'un
      manuscrit, c'est-à-dire la transcription des informations relatives à la date, au lieu, à
      l'organisme commanditaire ou aux raisons de la production du manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el  <term>colophon</term> de un manuscrito, es decir, una declaración que contiene informaciones relativas a fecha, lugar, agente, o finalidad de la producción del manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il  <term>colophon</term>
di un manoscritto, ovvero una dichiarazione contenente informazioni relative a data, luogo, committente, o motivo della produzione del manoscritto</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msExcerpt"/>
    <memberOf key="model.msQuoteLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-su" xml:lang="la">
      <colophon>Ricardus Franciscus Scripsit Anno Domini
 1447.</colophon>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-yy" source="#fr-ex-Pernoud-femme">
      <colophon>Orate pro scriba que scripsit hunc librum : Nomen ejus Elisabeth.</colophon>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-am">
      <colophon>Explicit expliceat/scriptor ludere eat.</colophon>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-rf">
      <colophon>Explicit venenum viciorum domini illius, qui comparavit Anno domini Millessimo
          Trecentesimo nonagesimo primo, Sabbato in festo sancte Marthe virginis gloriose. Laus tibi
          criste quia finitur libellus iste.</colophon>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-gv">
      <colophon>大明萬曆甲寅夏季月。西蜀輔慈沙門明昱書</colophon>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-ik">
      <colophon>宋咸淳五年歲在己巳八月上日。四明福泉沙門志磐寓東湖月波山。謹序。</colophon>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-ph" source="#UND">
      <!-- 已提供兩則範例，故第三則類似範例予以省略。 -->
    </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-kw" xml:lang="la">
      <colophon>Explicit expliceat/scriptor ludere eat.</colophon>
    </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-wv" xml:lang="la">
      <colophon>Explicit venenum viciorum domini illius, qui comparavit Anno
domini Millessimo Trecentesimo nonagesimo primo, Sabbato in festo
sancte Marthe virginis gloriose.  Laus tibi criste quia finitur
libellus iste.</colophon>
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
<gloss versionDate="2007-06-12" xml:lang="en">colophon</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">colophon</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="colophon.desc">contains the  <term>colophon</term>
of an item: that is, a statement providing information regarding the date, place, agency, or reason for production of the manuscript or other object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 <term>colophon</term>(판권 표지 장)를 포함한다; 즉, 원고 생산에 대한 날짜, 장소, 대리권, 또는 이유와 관련한 정보를 제공하는 서술</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個手稿項目的 <term>版權頁標記</term>：即提供日期、地點、代理機構、或手稿產生原因等資訊的聲明。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料の<term>コロフォン(奥付情報)</term>を示す。例えば、制
  作の日時、場所、主体、制作主体、制作理由など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le <term>colophon</term> d'une section d'un
      manuscrit, c'est-à-dire la transcription des informations relatives à la date, au lieu, à
      l'organisme commanditaire ou aux raisons de la production du manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el  <term>colophon</term> de un manuscrito, es decir, una declaración que contiene informaciones relativas a fecha, lugar, agente, o finalidad de la producción del manuscrito.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il  <term>colophon</term>
di un manoscritto, ovvero una dichiarazione contenente informazioni relative a data, luogo, committente, o motivo della produzione del manoscritto</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.msExcerpt"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-su" xml:lang="la">
      <colophon>Ricardus Franciscus Scripsit Anno Domini
 1447.</colophon>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-yy" source="#fr-ex-Pernoud-femme">
      <colophon>Orate pro scriba que scripsit hunc librum : Nomen ejus Elisabeth.</colophon>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-am">
      <colophon>Explicit expliceat/scriptor ludere eat.</colophon>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-rf">
      <colophon>Explicit venenum viciorum domini illius, qui comparavit Anno domini Millessimo
          Trecentesimo nonagesimo primo, Sabbato in festo sancte Marthe virginis gloriose. Laus tibi
          criste quia finitur libellus iste.</colophon>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-gv">
      <colophon>大明萬曆甲寅夏季月。西蜀輔慈沙門明昱書</colophon>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-ik">
      <colophon>宋咸淳五年歲在己巳八月上日。四明福泉沙門志磐寓東湖月波山。謹序。</colophon>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-ph" source="#UND">
      <!-- 已提供兩則範例，故第三則類似範例予以省略。 -->
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-kw" xml:lang="la">
      <colophon>Explicit expliceat/scriptor ludere eat.</colophon>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[9]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLOPHON-egXML-wv" xml:lang="la">
      <colophon>Explicit venenum viciorum domini illius, qui comparavit Anno
domini Millessimo Trecentesimo nonagesimo primo, Sabbato in festo
sancte Marthe virginis gloriose.  Laus tibi criste quia finitur
libellus iste.</colophon>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mscoit"/>
  </listRef>
```

^b21

