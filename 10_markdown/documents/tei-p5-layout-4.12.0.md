---
type: representation
source-type: document
source: '[[00_sources/tei-p5-layout-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 layout
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/layout.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# layout

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10429. Git blob: `65ed9a4e7b29b35ff46ab68e7d948fc9c08fbb40`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="LAYOUT" ident="layout">
  <gloss versionDate="2007-06-12" xml:lang="en">layout</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">mise en page</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="layout.desc">describes how text is laid out on the
  page or surface of the object, including information about any ruling, pricking, or other evidence of page-preparation techniques.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">괘선, 윤곽 또는 페이지 준비 기술의 다른 증거에 관한 정보를 포함하여 텍스트의 페이지 레이아웃 방식을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述文字在頁面上的編排，包括任何橫隔線、刺痕、或其他的頁面準備技術的資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該ページ上でテキストがどのようにレイアウトされているかを示す。例え
  ば、罫線、穴、などの書記支度技法。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit comment le texte est disposé sur la page, ce
      qui inclut les informations sur d'éventuels systèmes de réglure, de piqûre ou d'autres
      techniques de préparation de la page.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe la disposición del texto en la página, comprendiendo eventuales informaciones sobre la lineación***, indicaciones de agujereado***, u otras señales de técnicas de preparación de la página utilizadas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive la disposizione del testo sulla pagina, ivi comprese eventuali informazioni su rigatura, applicazione di indicazioni per foratura, o altri segni di tecniche di preparazione della pagina.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <attList>
    <attDef ident="columns">
      <gloss versionDate="2007-06-12" xml:lang="en">columns</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">colonnes</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">specifies the number of columns per page.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">페이지 당 열의 수를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明每頁的欄數</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">ページ中の段数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie le nombre de colonnes présentes sur une page.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el número de columnas por página.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il numero di colonne per pagina.</desc>
      <datatype minOccurs="1" maxOccurs="2"><dataRef key="teidata.count"/></datatype>
      <remarks ident="layout-attr.columns-remarks" versionDate="2017-07-09" xml:lang="en"><p>If a single number is given, all pages referenced have this number of columns. If two numbers are given, the number of columns per page varies between the values supplied. Where <att>columns</att> is omitted the number is assumed to be <val>1</val>.</p>
      <p>Columns may be independent of page orientation or reading direction, and a single textual <att>stream</att> may have one or more columns.</p>
    </remarks>
    </attDef>
    <attDef ident="streams">
    	<gloss versionDate="2018-07-12" xml:lang="en">textual streams</gloss>
      <desc versionDate="2018-07-12" xml:lang="en">indicates the number of streams per page, each of which contains an independent textual stream.</desc>
      <datatype minOccurs="1" maxOccurs="2"><dataRef key="teidata.count"/></datatype>
      <remarks ident="layout-attr.streams-remarks" versionDate="2018-07-09" xml:lang="en"><p>If a single number is given, all pages referenced  have this number of textual streams. If two numbers are given, the number of textual streams per page varies between the values supplied. Where <att>streams</att> is omitted the number is assumed to be <val>1</val> and unless specified elsewhere the script orientation of the source is identical to that used in the TEI document.</p> 
</remarks>
    </attDef>
    <attDef ident="ruledLines">
      <gloss versionDate="2020-12-20" xml:lang="en">ruled lines</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">lignes de réglure</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">specifies the number of ruled lines per column.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">열 당 줄친 행의 수를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明每欄的橫隔線數</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">1段中の罫の数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie le nombre de lignes de réglure présentes
          par colonne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el número de líneas delineadas por columna.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il numero di righe per colonna.</desc>
      <datatype minOccurs="1" maxOccurs="2"><dataRef key="teidata.count"/></datatype>
      <remarks ident="layout-attr.ruledLines-remarks" versionDate="2013-12-21" xml:lang="en"><p>If a single
      number is given, all columns have this number of ruled lines. If two
      numbers are given, the number of ruled lines per column varies between
      the values supplied.</p></remarks>
    </attDef>
    <attDef ident="writtenLines">
      <gloss versionDate="2020-12-20" xml:lang="en">written lines</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">lignes d'écriture</gloss>
      <desc versionDate="2009-07-11" xml:lang="en">specifies the number of written lines per column.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">열 당 쓰인 행의 수를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明每欄的書寫行數</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">1段中の行数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie le nombre de lignes écrites par colonne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el número de líneas escritas por columna.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il numero di righe scritte per colonna.</desc>
      <datatype minOccurs="1" maxOccurs="2"><dataRef key="teidata.count"/></datatype>
      <remarks ident="layout-attr.writtenLines-remarks" versionDate="2013-12-21" xml:lang="en"><p>If a single
      number is given, all columns have this number of written lines. If two
      numbers are given, the number of written lines per column varies between
      the values supplied.</p></remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-kd">
      <layout columns="1" ruledLines="25 32">
Most pages have between 25 and 32 long lines ruled in lead.</layout>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-ys">
      <layout columns="1" ruledLines="25 32"> Most pages have between 25 and 32 long lines ruled
          in lead.</layout>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-ke">
      <layout columns="2" ruledLines="42">
        <p>2 columns of 42 lines ruled in ink, with central rule between the columns.</p>
      </layout>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-gs">
      <layout columns="1 2" writtenLines="40 50">
        <p>Some pages have 2 columns, with central rule between the columns; each column with
            between 40 and 50 lines of writing.</p>
      </layout>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-gr">
      <layout columns="1" ruledLines="25 32">頁面大多有25到32行的鉛字橫線。</layout>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-mi">
      <layout columns="2" ruledLines="42">
        <p>兩欄共42行油墨橫線，欄間有直線分隔。</p>
      </layout>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-mb">
      <layout columns="1 2" writtenLines="40 50">
        <p>有些頁面有兩欄，欄間有直線分隔；每欄有40至50行的字。</p>
      </layout>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-tj">
      <layout columns="2" ruledLines="42">
        <p>2 columns of 42 lines ruled in ink, with central rule 
between the columns.</p>
      </layout>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-mg">
      <layout columns="1 2" writtenLines="40 50">
        <p>Some pages have 2 columns, with central rule 
between the columns; each column with between 40 and 50 lines of writing.</p>
      </layout>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-yh">
       <layout streams="3" columns="3"/>
       <!-- Further down in document body -->
       <div type="page">
        <ab><pb/>
         一二三<cb type="top-stream"/>
         一二三<cb type="mid-stream"/>
         一二三<cb type="bottom-stream"/> <!-- cb here for demo purposes -->
        </ab>
       </div>
      </egXML>
    </exemplum>
  <listRef>
    <ptr target="#msph2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">layout</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">mise en page</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="layout.desc">describes how text is laid out on the
  page or surface of the object, including information about any ruling, pricking, or other evidence of page-preparation techniques.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">괘선, 윤곽 또는 페이지 준비 기술의 다른 증거에 관한 정보를 포함하여 텍스트의 페이지 레이아웃 방식을 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述文字在頁面上的編排，包括任何橫隔線、刺痕、或其他的頁面準備技術的資訊。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該ページ上でテキストがどのようにレイアウトされているかを示す。例え
  ば、罫線、穴、などの書記支度技法。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit comment le texte est disposé sur la page, ce
      qui inclut les informations sur d'éventuels systèmes de réglure, de piqûre ou d'autres
      techniques de préparation de la page.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la disposición del texto en la página, comprendiendo eventuales informaciones sobre la lineación***, indicaciones de agujereado***, u otras señales de técnicas de preparación de la página utilizadas.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive la disposizione del testo sulla pagina, ivi comprese eventuali informazioni su rigatura, applicazione di indicazioni per foratura, o altri segni di tecniche di preparazione della pagina.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">columns</gloss>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">colonnes</gloss>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the number of columns per page.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">페이지 당 열의 수를 명시한다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明每頁的欄數</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ページ中の段数を示す。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie le nombre de colonnes présentes sur une page.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el número de columnas por página.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il numero di colonne per pagina.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="2"><dataRef key="teidata.count"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="layout-attr.columns-remarks" versionDate="2017-07-09" xml:lang="en"><p>If a single number is given, all pages referenced have this number of columns. If two numbers are given, the number of columns per page varies between the values supplied. Where <att>columns</att> is omitted the number is assumed to be <val>1</val>.</p>
      <p>Columns may be independent of page orientation or reading direction, and a single textual <att>stream</att> may have one or more columns.</p>
    </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2018-07-12" xml:lang="en">textual streams</gloss>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2018-07-12" xml:lang="en">indicates the number of streams per page, each of which contains an independent textual stream.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="2"><dataRef key="teidata.count"/></datatype>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="layout-attr.streams-remarks" versionDate="2018-07-09" xml:lang="en"><p>If a single number is given, all pages referenced  have this number of textual streams. If two numbers are given, the number of textual streams per page varies between the values supplied. Where <att>streams</att> is omitted the number is assumed to be <val>1</val> and unless specified elsewhere the script orientation of the source is identical to that used in the TEI document.</p> 
</remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">ruled lines</gloss>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">lignes de réglure</gloss>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the number of ruled lines per column.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">열 당 줄친 행의 수를 명시한다.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明每欄的橫隔線數</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">1段中の罫の数を示す。</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie le nombre de lignes de réglure présentes
          par colonne.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el número de líneas delineadas por columna.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il numero di righe per colonna.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="2"><dataRef key="teidata.count"/></datatype>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="layout-attr.ruledLines-remarks" versionDate="2013-12-21" xml:lang="en"><p>If a single
      number is given, all columns have this number of ruled lines. If two
      numbers are given, the number of ruled lines per column varies between
      the values supplied.</p></remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">written lines</gloss>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">lignes d'écriture</gloss>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2009-07-11" xml:lang="en">specifies the number of written lines per column.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">열 당 쓰인 행의 수를 명시한다.</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明每欄的書寫行數</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">1段中の行数を示す。</desc>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie le nombre de lignes écrites par colonne.</desc>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el número de líneas escritas por columna.</desc>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il numero di righe scritte per colonna.</desc>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="2"><dataRef key="teidata.count"/></datatype>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[1]`.

```xml
<remarks ident="layout-attr.writtenLines-remarks" versionDate="2013-12-21" xml:lang="en"><p>If a single
      number is given, all columns have this number of written lines. If two
      numbers are given, the number of written lines per column varies between
      the values supplied.</p></remarks>
```

^b48

### Block 49

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-kd">
      <layout columns="1" ruledLines="25 32">
Most pages have between 25 and 32 long lines ruled in lead.</layout>
    </egXML>
  </exemplum>
```

^b49

### Block 50

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-ys">
      <layout columns="1" ruledLines="25 32"> Most pages have between 25 and 32 long lines ruled
          in lead.</layout>
    </egXML>
  </exemplum>
```

^b50

### Block 51

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-ke">
      <layout columns="2" ruledLines="42">
        <p>2 columns of 42 lines ruled in ink, with central rule between the columns.</p>
      </layout>
    </egXML>
  </exemplum>
```

^b51

### Block 52

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-gs">
      <layout columns="1 2" writtenLines="40 50">
        <p>Some pages have 2 columns, with central rule between the columns; each column with
            between 40 and 50 lines of writing.</p>
      </layout>
    </egXML>
  </exemplum>
```

^b52

### Block 53

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-gr">
      <layout columns="1" ruledLines="25 32">頁面大多有25到32行的鉛字橫線。</layout>
    </egXML>
  </exemplum>
```

^b53

### Block 54

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-mi">
      <layout columns="2" ruledLines="42">
        <p>兩欄共42行油墨橫線，欄間有直線分隔。</p>
      </layout>
    </egXML>
  </exemplum>
```

^b54

### Block 55

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-mb">
      <layout columns="1 2" writtenLines="40 50">
        <p>有些頁面有兩欄，欄間有直線分隔；每欄有40至50行的字。</p>
      </layout>
    </egXML>
  </exemplum>
```

^b55

### Block 56

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-tj">
      <layout columns="2" ruledLines="42">
        <p>2 columns of 42 lines ruled in ink, with central rule 
between the columns.</p>
      </layout>
    </egXML>
  </exemplum>
```

^b56

### Block 57

XML location: `/elementSpec[1]/exemplum[9]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-mg">
      <layout columns="1 2" writtenLines="40 50">
        <p>Some pages have 2 columns, with central rule 
between the columns; each column with between 40 and 50 lines of writing.</p>
      </layout>
    </egXML>
  </exemplum>
```

^b57

### Block 58

XML location: `/elementSpec[1]/exemplum[10]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LAYOUT-egXML-yh">
       <layout streams="3" columns="3"/>
       <!-- Further down in document body -->
       <div type="page">
        <ab><pb/>
         一二三<cb type="top-stream"/>
         一二三<cb type="mid-stream"/>
         一二三<cb type="bottom-stream"/> <!-- cb here for demo purposes -->
        </ab>
       </div>
      </egXML>
    </exemplum>
```

^b58

### Block 59

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph2"/>
  </listRef>
```

^b59

