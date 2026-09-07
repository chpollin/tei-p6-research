---
type: representation
source-type: document
source: '[[00_sources/tei-p5-opener-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 opener
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/opener.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# opener

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5161. Git blob: `9629d92476ba0d79a9c10aaa7c9a013d3d5dd132`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-opener" ident="opener">
  <gloss versionDate="2007-06-12" xml:lang="en">opener</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">formule de début</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">groups together dateline, byline, salutation, and similar phrases appearing as a preliminary
    group at the start of a division, especially of a letter.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구역, 특히 편지의 시작부에 서문군으로 나타나는 날짜 표시란, 필자명 행, 인사말, 그리고 유사 구를
    합하여 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集日期地點、署名、稱呼語及其他在區段開端出現的類似措辭，尤指信件開頭。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト部分の始まりに、日付欄、署名欄、挨拶文言など、前置き的な部分
    としてあるものをまとめる。典型例は、手紙の場合である。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe la date, la mention de responsabilité, la
    formule de politesse et d'autres expressions de ce type dans un groupe préliminaire au début
    d’une division, en particulier au commencement d’une lettre.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">fasst Datumszeile, Verfasserangabe, Anredeformel und ähnliche Phrasen zusammen, die einleitend zu
    Beginn eines Abschnitts stehen, vor allem bei einem Brief.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa la fecha, autoria, fórmula introductiva o de
    saludo o expresiones similares utilizades al inicio de una división textual, especialmente en
    una carta.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa dateline, byline, formule introduttive o di
    saluto ed espressioni simili utilizzate all'inizio di una partizione testuale, soprattutto in
    una lettera</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divTopPart"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <!-- shd be class ref -->
        <elementRef key="argument"/>
        <elementRef key="byline"/>
        <elementRef key="dateline"/>
        <elementRef key="epigraph"/>
        <elementRef key="salute"/>
        <elementRef key="signed"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-nl" source="#harveyFour">
      <opener>
        <dateline>Walden, this 29. of August 1592</dateline>
      </opener>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-xd">
      <opener>
        <dateline>Avignon, le 11 février.</dateline>
      </opener>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-fc" source="#fr-ex-Diderot-Corresp_SV">
      <opener>
        <dateline><name type="place"> à Paris </name>, <date>le 2 septembre 1769</date></dateline>
      </opener>
      <p>Mais non, ma bonne amie, vous n' aviez pas raison de vous plaindre... </p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-la">
      <opener>
        <dateline>1983年7月3日</dateline>
      </opener>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-uh">
      <opener>
        <dateline>
          <name type="place">杭州西湖</name>
          <date>2008年4月1日</date>
        </dateline>
        <salute>親愛的小張：</salute>
      </opener>
      <p>很抱歉，我今天有事無法赴約，希望您能諒解...</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-lz" source="#DSCO-eg-51">
      <opener>
        <dateline>
          <name type="place">Great Marlborough Street</name>
          <date>November 11, 1848</date>
        </dateline>
        <salute>My dear Sir,</salute>
      </opener>
      <p>I am sorry to say that absence from town and other circumstances have prevented me from
        earlier enquiring...</p>
    </egXML>
    <!-- Trollope Autobiog, p 77 -->
  </exemplum>
  <listRef>
    <ptr target="#DSDTB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">opener</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">formule de début</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups together dateline, byline, salutation, and similar phrases appearing as a preliminary
    group at the start of a division, especially of a letter.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구역, 특히 편지의 시작부에 서문군으로 나타나는 날짜 표시란, 필자명 행, 인사말, 그리고 유사 구를
    합하여 모아 놓는다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集日期地點、署名、稱呼語及其他在區段開端出現的類似措辭，尤指信件開頭。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト部分の始まりに、日付欄、署名欄、挨拶文言など、前置き的な部分
    としてあるものをまとめる。典型例は、手紙の場合である。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe la date, la mention de responsabilité, la
    formule de politesse et d'autres expressions de ce type dans un groupe préliminaire au début
    d’une division, en particulier au commencement d’une lettre.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">fasst Datumszeile, Verfasserangabe, Anredeformel und ähnliche Phrasen zusammen, die einleitend zu
    Beginn eines Abschnitts stehen, vor allem bei einem Brief.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa la fecha, autoria, fórmula introductiva o de
    saludo o expresiones similares utilizades al inicio de una división textual, especialmente en
    una carta.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa dateline, byline, formule introduttive o di
    saluto ed espressioni simili utilizzate all'inizio di una partizione testuale, soprattutto in
    una lettera</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divTopPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <!-- shd be class ref -->
        <elementRef key="argument"/>
        <elementRef key="byline"/>
        <elementRef key="dateline"/>
        <elementRef key="epigraph"/>
        <elementRef key="salute"/>
        <elementRef key="signed"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-nl" source="#harveyFour">
      <opener>
        <dateline>Walden, this 29. of August 1592</dateline>
      </opener>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-xd">
      <opener>
        <dateline>Avignon, le 11 février.</dateline>
      </opener>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-fc" source="#fr-ex-Diderot-Corresp_SV">
      <opener>
        <dateline><name type="place"> à Paris </name>, <date>le 2 septembre 1769</date></dateline>
      </opener>
      <p>Mais non, ma bonne amie, vous n' aviez pas raison de vous plaindre... </p>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-la">
      <opener>
        <dateline>1983年7月3日</dateline>
      </opener>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-uh">
      <opener>
        <dateline>
          <name type="place">杭州西湖</name>
          <date>2008年4月1日</date>
        </dateline>
        <salute>親愛的小張：</salute>
      </opener>
      <p>很抱歉，我今天有事無法赴約，希望您能諒解...</p>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-opener-egXML-lz" source="#DSCO-eg-51">
      <opener>
        <dateline>
          <name type="place">Great Marlborough Street</name>
          <date>November 11, 1848</date>
        </dateline>
        <salute>My dear Sir,</salute>
      </opener>
      <p>I am sorry to say that absence from town and other circumstances have prevented me from
        earlier enquiring...</p>
    </egXML>
    <!-- Trollope Autobiog, p 77 -->
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSDTB"/>
  </listRef>
```

^b19

