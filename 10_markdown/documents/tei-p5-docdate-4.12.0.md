---
type: representation
source-type: document
source: '[[00_sources/tei-p5-docdate-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 docDate
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/docDate.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# docDate

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4981. Git blob: `bfa5a85fe60e75ad7da395be1ab7fa6ee6df7cd1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="textstructure" xml:id="gi-docDate" ident="docDate">
  <gloss versionDate="2005-01-14" xml:lang="en">document date</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문서 날짜</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文件日期</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">date du document</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Datierung des Dokuments</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">fecha del documento</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">data del documento</gloss>
  <desc versionDate="2013-11-12" xml:lang="en">contains the date of a document, as given on a title page or in a dateline.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">대개 제목 페이지에 제시되는 문서의 날짜를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件日期， 同於 (通常) 在題名頁上顯示的日期。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">文書の日付を示す。一般にはタイトルページに書かれている。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la date d’un document telle qu’elle est (généralement ) donnée sur une page de titre.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält die Datierung des Dokuments, wie auf der Titelseite oder in einer Datumszeile angegeben.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la fecha del documento, tal y como, normalmente, aparece en el frontispicio.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la data del documento così come riportata di norma nel frontespizio.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.calendarSystem"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docDate-egXML-nd">
      <docImprint>Oxford, Clarendon Press, <docDate>1987</docDate>
         </docImprint>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docDate-egXML-ho">
      <docImprint>Lettres Modernes Minard, <pubPlace>PARIS-CAEN</pubPlace>
            <docDate>2003</docDate>
        </docImprint>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docDate-egXML-af">
      <docImprint>上海：中華書局，<docDate>2001</docDate>年。
      </docImprint>
    </egXML>
  </exemplum>
  <remarks ident="docDate-remarks" versionDate="2013-11-12" xml:lang="en">
    <p>Cf. the general <gi>date</gi> element in the core tag set.
      This specialized element is provided for convenience in marking
      and processing the date of the documents, since it is likely to
      require specialized handling for many applications. It should be
      used only for the date of the entire document, not for any subset
      or part of it.</p>
  </remarks>
  <remarks ident="docDate-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Voir l'élément générique <gi>date</gi> dans le module <term>core</term>. L'élément
      spécifique <gi>docDate</gi> est fourni à toutes fins utiles pour encoder et traiter
      la date des documents, puisque celle-ci requiert une gestion particulière pour de
      nombreux besoins.</p>
  </remarks>
  <remarks ident="docDate-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>date</gi>は、コアタグ集合で定義されている。
    当該要素は、当該文書の日付を記述・処理するためのものである。多くの
    ソフトウェアは独自の扱いをするだろう。
    </p>
  </remarks>
  <remarks ident="docDate-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Vgl. das allgemeine <gi>date</gi>-Element im core-Modul. Dieses
      spezialisierte Element erleichtert die Kodierung und Verarbeitung der Datierung eines Dokuments,
      die vermutlich in vielen Anwendungsszenarien gesondert behandelt wird. Es sollte nur für das
      Datum des gesamten Dokuments verwendet werden, nicht für Datierungen von Abschnitten oder
      Teilen.</p>
  </remarks>
  <listRef>
    <ptr target="#DSTITL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">document date</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문서 날짜</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文件日期</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">date du document</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Datierung des Dokuments</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">fecha del documento</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">data del documento</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-11-12" xml:lang="en">contains the date of a document, as given on a title page or in a dateline.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">대개 제목 페이지에 제시되는 문서의 날짜를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件日期， 同於 (通常) 在題名頁上顯示的日期。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">文書の日付を示す。一般にはタイトルページに書かれている。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la date d’un document telle qu’elle est (généralement ) donnée sur une page de titre.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält die Datierung des Dokuments, wie auf der Titelseite oder in einer Datumszeile angegeben.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la fecha del documento, tal y como, normalmente, aparece en el frontispicio.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la data del documento così come riportata di norma nel frontespizio.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.calendarSystem"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docDate-egXML-nd">
      <docImprint>Oxford, Clarendon Press, <docDate>1987</docDate>
         </docImprint>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docDate-egXML-ho">
      <docImprint>Lettres Modernes Minard, <pubPlace>PARIS-CAEN</pubPlace>
            <docDate>2003</docDate>
        </docImprint>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-docDate-egXML-af">
      <docImprint>上海：中華書局，<docDate>2001</docDate>年。
      </docImprint>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="docDate-remarks" versionDate="2013-11-12" xml:lang="en">
    <p>Cf. the general <gi>date</gi> element in the core tag set.
      This specialized element is provided for convenience in marking
      and processing the date of the documents, since it is likely to
      require specialized handling for many applications. It should be
      used only for the date of the entire document, not for any subset
      or part of it.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="docDate-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Voir l'élément générique <gi>date</gi> dans le module <term>core</term>. L'élément
      spécifique <gi>docDate</gi> est fourni à toutes fins utiles pour encoder et traiter
      la date des documents, puisque celle-ci requiert une gestion particulière pour de
      nombreux besoins.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="docDate-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>date</gi>は、コアタグ集合で定義されている。
    当該要素は、当該文書の日付を記述・処理するためのものである。多くの
    ソフトウェアは独自の扱いをするだろう。
    </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="docDate-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Vgl. das allgemeine <gi>date</gi>-Element im core-Modul. Dieses
      spezialisierte Element erleichtert die Kodierung und Verarbeitung der Datierung eines Dokuments,
      die vermutlich in vielen Anwendungsszenarien gesondert behandelt wird. Es sollte nur für das
      Datum des gesamten Dokuments verwendet werden, nicht für Datierungen von Abschnitten oder
      Teilen.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b25

