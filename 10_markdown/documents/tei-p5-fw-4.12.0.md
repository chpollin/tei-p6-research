---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fw-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fw
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fw.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fw

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10910. Git blob: `d2084dd550bc6df388b2f4d1f3e5a1ec398ff771`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-fw" ident="fw">
  <gloss versionDate="2005-01-14" xml:lang="en">forme work</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">조판 작업</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">印版文字</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">élément de mise en page</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">convenciones gráficas.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">convenzioni grafiche</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a running head (e.g. a header, footer), catchword, or
  similar material appearing on the current page.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">현 페이지에 나타나는 현 표제부(예, 머리말, 꼬리말), 색인어, 또는 유사 자료를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個欄外標題 (例如頁眉、頁腳) 、標語、或出現在所標記頁面的類似文字。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">版面の周りにある柱やノンブルを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">permet d'encoder un titre courant (en haut ou en bas de la page), une réclame ou une autre information comparable, qui apparaît sur la page courante.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un encabezamiento, pie de página, reclamo o similar relativo a la página corriente</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene intestazione, piè di pagina, reclamo o simili relativi alla pagina corrente.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="rec">
      <desc versionDate="2005-01-14" xml:lang="en">classifies the material encoded according to some useful typology.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">유용한 유형에 따라 부호화된 자료를 분류한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類方法將所標記的內容分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">符号化された当該部分を分類する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">caractérise l'information encodée conformément à une typologie appropriée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">clasifica las convenciones usadas según una tipología funcional.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica le convenzioni usate secondo una tipologia funzionale.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="header">
          <desc versionDate="2007-04-02" xml:lang="en">a running title at the top of the page</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">페이지 상단의 현 제목</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面頂端的欄外標題</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">天にタイトル。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">un titre courant en haut de la page</desc>
          <desc versionDate="2007-05-04" xml:lang="es">título o asunto en el encabezamiento de la página</desc>
          <desc versionDate="2007-01-21" xml:lang="it">titolo nell'intestazione di pagina.</desc>
        </valItem>
        <valItem ident="footer">
          <desc versionDate="2007-04-02" xml:lang="en">a running title at the bottom of the page</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">페이지 하단의 제목</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面底端的欄外標題</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">地にあるタイトル。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">un titre courant en bas de la page</desc>
          <desc versionDate="2007-05-04" xml:lang="es">título o asunto a pie de página</desc>
          <desc versionDate="2007-01-21" xml:lang="it">titolo nel piè di pagina.</desc>
        </valItem>
        <valItem ident="pageNum">
          <gloss versionDate="2007-07-04" xml:lang="en">page number</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">페이지 숫자</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">página</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">numéro de page</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">numero di pagina</gloss>
          <desc versionDate="2007-04-02" xml:lang="en">a page number or foliation symbol</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">페이지 숫자 또는 페이지 기호</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">編頁數號或是編張符號</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">ノンブル。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">un numéro de page ou un symbole de foliotation</desc>
          <desc versionDate="2007-11-06" xml:lang="it">numero di pagina o simbolo di foliazione.</desc>
          <desc versionDate="2007-05-04" xml:lang="es">número de página o símbolo de la foliación</desc>
        </valItem>
        <valItem ident="lineNum">
          <gloss versionDate="2007-07-04" xml:lang="en">line number</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">행 수</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">número de línea</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">numéro de ligne</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">numero di riga</gloss>
          <desc versionDate="2007-07-04" xml:lang="en">a line number, either of prose or poetry</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">산문 또는 시에서 행 번호</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un número de línea, en prosa o verso</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">韻文・散文における行番号。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">numéro d'une ligne en prose ou en vers</desc>
          <desc versionDate="2007-11-06" xml:lang="it">numero di riga di testo in prosa o componimento poetico.</desc>
        </valItem>
        <valItem ident="sig">
          <gloss versionDate="2007-07-04" xml:lang="en">signature</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">서명</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">signatura</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">firma</gloss>
          <desc versionDate="2007-04-02" xml:lang="en">a signature or gathering symbol</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">서명 혹은 서명 기호</desc>
          <desc versionDate="2008-10-02" xml:lang="fr">signature ou marque de cahier</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">簽名或是聚集符號</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">折丁記号。</desc>
          <desc versionDate="2007-05-04" xml:lang="es">firma o símbolo común</desc>
          <desc versionDate="2007-01-21" xml:lang="it">firma o simbolo comune.</desc>
        </valItem>
        <valItem ident="catch">
          <gloss versionDate="2007-07-04" xml:lang="en">catchword</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">색인어</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">lema</gloss>
          <gloss versionDate="2009-11-16" xml:lang="fr">réclame</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">reclamo</gloss>
          <desc versionDate="2007-04-02" xml:lang="en">a catch-word</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">색인어</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標語</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">柱。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">une réclame</desc>
          <desc versionDate="2007-05-04" xml:lang="es">reclamo</desc>
          <desc versionDate="2007-01-21" xml:lang="it">reclamo.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fw-egXML-lr">
      <fw type="sig" place="bottom">C3</fw>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fw-egXML-eg">
      <fw type="sig" place="bot">C3</fw>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fw-egXML-jp">
      <fw type="sig" place="bot">徐閱</fw>
    </egXML>
  </exemplum>
  <remarks ident="fw-remarks" versionDate="2006-06-28" xml:lang="en">
    <p>Where running heads are consistent throughout a chapter or
    section, it is usually more convenient to relate them to the
    chapter or section, e.g. by use of the <att>rend</att> attribute.
    The <gi>fw</gi> element is intended for cases where the running
    head changes from page to page, or where details of page layout
    and the internal structure of the running heads are of paramount
    importance.</p>
  </remarks>
  <remarks ident="fw-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Quand le titre courant s'applique à tout un chapitre ou une section, il est habituellement plus commode de le relier au chapitre ou à la section, par exemple en utilisant l'attribut <att>rend</att>. L'élément <gi>fw</gi> est utilisé pour des cas où le titre courant change de page en page ou quand il est primordial de relever des détails de mise en page ou la structure interne des titres courants.</p>
  </remarks>
  <remarks ident="fw-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    柱に章や節が常に書かれている場合、属性<att>rend</att>を使い、
    章や節と対応した方が便利である。
    柱の内容がページごとに異なる場合、またはページのレイアウト
    や柱の内部構造が重要である場合に、当該要素<gi>fw</gi>が使用される。
    </p>
  </remarks>
  <listRef>
    <ptr target="#PHSK"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">forme work</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">조판 작업</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">印版文字</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">élément de mise en page</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">convenciones gráficas.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">convenzioni grafiche</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a running head (e.g. a header, footer), catchword, or
  similar material appearing on the current page.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 페이지에 나타나는 현 표제부(예, 머리말, 꼬리말), 색인어, 또는 유사 자료를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個欄外標題 (例如頁眉、頁腳) 、標語、或出現在所標記頁面的類似文字。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">版面の周りにある柱やノンブルを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">permet d'encoder un titre courant (en haut ou en bas de la page), une réclame ou une autre information comparable, qui apparaît sur la page courante.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un encabezamiento, pie de página, reclamo o similar relativo a la página corriente</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene intestazione, piè di pagina, reclamo o simili relativi alla pagina corrente.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">classifies the material encoded according to some useful typology.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">유용한 유형에 따라 부호화된 자료를 분류한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類方法將所標記的內容分類。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">符号化された当該部分を分類する。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">caractérise l'information encodée conformément à une typologie appropriée.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clasifica las convenciones usadas según una tipología funcional.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica le convenzioni usate secondo una tipologia funzionale.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="header">
          <desc versionDate="2007-04-02" xml:lang="en">a running title at the top of the page</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">페이지 상단의 현 제목</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面頂端的欄外標題</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">天にタイトル。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">un titre courant en haut de la page</desc>
          <desc versionDate="2007-05-04" xml:lang="es">título o asunto en el encabezamiento de la página</desc>
          <desc versionDate="2007-01-21" xml:lang="it">titolo nell'intestazione di pagina.</desc>
        </valItem>
        <valItem ident="footer">
          <desc versionDate="2007-04-02" xml:lang="en">a running title at the bottom of the page</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">페이지 하단의 제목</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">頁面底端的欄外標題</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">地にあるタイトル。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">un titre courant en bas de la page</desc>
          <desc versionDate="2007-05-04" xml:lang="es">título o asunto a pie de página</desc>
          <desc versionDate="2007-01-21" xml:lang="it">titolo nel piè di pagina.</desc>
        </valItem>
        <valItem ident="pageNum">
          <gloss versionDate="2007-07-04" xml:lang="en">page number</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">페이지 숫자</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">página</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">numéro de page</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">numero di pagina</gloss>
          <desc versionDate="2007-04-02" xml:lang="en">a page number or foliation symbol</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">페이지 숫자 또는 페이지 기호</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">編頁數號或是編張符號</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">ノンブル。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">un numéro de page ou un symbole de foliotation</desc>
          <desc versionDate="2007-11-06" xml:lang="it">numero di pagina o simbolo di foliazione.</desc>
          <desc versionDate="2007-05-04" xml:lang="es">número de página o símbolo de la foliación</desc>
        </valItem>
        <valItem ident="lineNum">
          <gloss versionDate="2007-07-04" xml:lang="en">line number</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">행 수</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">número de línea</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">numéro de ligne</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">numero di riga</gloss>
          <desc versionDate="2007-07-04" xml:lang="en">a line number, either of prose or poetry</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">산문 또는 시에서 행 번호</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un número de línea, en prosa o verso</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">韻文・散文における行番号。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">numéro d'une ligne en prose ou en vers</desc>
          <desc versionDate="2007-11-06" xml:lang="it">numero di riga di testo in prosa o componimento poetico.</desc>
        </valItem>
        <valItem ident="sig">
          <gloss versionDate="2007-07-04" xml:lang="en">signature</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">서명</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">signatura</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">firma</gloss>
          <desc versionDate="2007-04-02" xml:lang="en">a signature or gathering symbol</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">서명 혹은 서명 기호</desc>
          <desc versionDate="2008-10-02" xml:lang="fr">signature ou marque de cahier</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">簽名或是聚集符號</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">折丁記号。</desc>
          <desc versionDate="2007-05-04" xml:lang="es">firma o símbolo común</desc>
          <desc versionDate="2007-01-21" xml:lang="it">firma o simbolo comune.</desc>
        </valItem>
        <valItem ident="catch">
          <gloss versionDate="2007-07-04" xml:lang="en">catchword</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">색인어</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">lema</gloss>
          <gloss versionDate="2009-11-16" xml:lang="fr">réclame</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">reclamo</gloss>
          <desc versionDate="2007-04-02" xml:lang="en">a catch-word</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">색인어</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">標語</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">柱。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">une réclame</desc>
          <desc versionDate="2007-05-04" xml:lang="es">reclamo</desc>
          <desc versionDate="2007-01-21" xml:lang="it">reclamo.</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fw-egXML-lr">
      <fw type="sig" place="bottom">C3</fw>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fw-egXML-eg">
      <fw type="sig" place="bot">C3</fw>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fw-egXML-jp">
      <fw type="sig" place="bot">徐閱</fw>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="fw-remarks" versionDate="2006-06-28" xml:lang="en">
    <p>Where running heads are consistent throughout a chapter or
    section, it is usually more convenient to relate them to the
    chapter or section, e.g. by use of the <att>rend</att> attribute.
    The <gi>fw</gi> element is intended for cases where the running
    head changes from page to page, or where details of page layout
    and the internal structure of the running heads are of paramount
    importance.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="fw-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Quand le titre courant s'applique à tout un chapitre ou une section, il est habituellement plus commode de le relier au chapitre ou à la section, par exemple en utilisant l'attribut <att>rend</att>. L'élément <gi>fw</gi> est utilisé pour des cas où le titre courant change de page en page ou quand il est primordial de relever des détails de mise en page ou la structure interne des titres courants.</p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="fw-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    柱に章や節が常に書かれている場合、属性<att>rend</att>を使い、
    章や節と対応した方が便利である。
    柱の内容がページごとに異なる場合、またはページのレイアウト
    や柱の内部構造が重要である場合に、当該要素<gi>fw</gi>が使用される。
    </p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHSK"/>
  </listRef>
```

^b31

