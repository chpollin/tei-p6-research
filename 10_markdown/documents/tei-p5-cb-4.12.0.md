---
type: representation
source-type: document
source: '[[00_sources/tei-p5-cb-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 cb
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/cb.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# cb

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5030. Git blob: `eb96df6ceb44519a9fff889fe5d5217fac7c4423`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-cb" ident="cb">
  <gloss versionDate="2017-06-14" xml:lang="en">column beginning</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">열 바꿈</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">分段</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">段の開始</gloss>
  <gloss versionDate="2022-05-12" xml:lang="fr">début de colonne</gloss>
  <gloss versionDate="2022-05-12" xml:lang="es">inicio de columna</gloss>
  <gloss versionDate="2022-08-17" xml:lang="it">inizio di colonna</gloss>
  <desc versionDate="2013-03-31" xml:lang="en">marks the beginning of a new column of a text on a
  multi-column page.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준 참조 시스템에서 텍스트의 한 열과 다음 열 사이의 경계를 표지한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">用標準參照系統來標明文本段落之間的分界。</desc>
  <desc versionDate="2023-10-02" xml:lang="ja">複数段の頁で、テキストの新しい段の開始を示す。</desc>
  <desc versionDate="2022-05-12" xml:lang="fr">marque le
  début d'une nouvelle colonne  de texte sur une page multi-colonne.</desc>
  <desc versionDate="2022-05-12" xml:lang="es">indica el inicio de una nueva columna de texto en una página divida en columnas .</desc>
  <desc versionDate="2022-08-17" xml:lang="it">segna l'inizio di una nuova colonna di un testo in una pagina a più colonne.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.breaking"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
  <content><empty/></content>
  <exemplum xml:lang="en">
    <p>Markup of an early English dictionary printed in two columns:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cb-egXML-mv" source="#REF-cb-eg-1">
      <pb/>
      <cb n="1"/>
      <entryFree><form>Well</form>, <sense>a Pit to hold Spring-Water</sense>:
                <sense>In the Art of <hi rend="italic">War</hi>, a Depth the Miner
                    sinks into the Ground, to find out and disappoint the Enemies Mines,
                    or to prepare one</sense>.</entryFree>
      <entryFree>To <form>Welter</form>, <sense>to wallow</sense>, or
                <sense>lie groveling</sense>.</entryFree>
      <!-- remainder of column -->
      <cb n="2"/>
      <entryFree><form>Wey</form>, <sense>the greatest Measure for dry Things,
                    containing five Chaldron</sense>.</entryFree>
      <entryFree><form>Whale</form>, <sense>the greatest of
                    Sea-Fishes</sense>.</entryFree>
    </egXML>
  </exemplum>
  <remarks ident="cb-remarks" versionDate="2013-03-31" xml:lang="en">
    <p>On this element, the global <att>n</att> attribute indicates the number or other value associated with the column
            which follows the point of insertion of this <gi>cb</gi> element. Encoders should adopt a clear and consistent policy as to
            whether the numbers associated with column beginnings relate to the physical
            sequence number of the column in the whole text, or whether columns are
            numbered within the page.
            The <gi>cb</gi> element is placed at the head of the
            column to which it refers.</p>
  </remarks>
  <remarks ident="cb-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut global <att>n</att> donne un nouveau numéro ou une autre valeur à la
            colonne qui suit l'élément <gi>cb</gi>. Les encodeurs doivent faire un choix clair,
            et s'y tenir, entre l'option consistant à se fonder sur la séquence physique des
            colonnes dans le texte entier, et celle qui consiste à se fonder sur la numérotation
            des colonnes à l'intérieur de la page. L'élément <gi>cb</gi>
            apparaît en haut de la colonne à laquelle il se rapporte.</p>
  </remarks>
  <remarks ident="cb-remarks" versionDate="2023-10-02" xml:lang="ja">
    <p>
      この要素では、グローバル属性<att>n</att>はこの<gi>cb</gi>要素の直後から始まる段と関連する数値等の値を示す。テキスト全体における段の通し番号を付けるか、ページ内における番号を付けるかについて、明確で一貫した方針を採用すべきである。<gi>cb</gi>要素は指している段の冒頭に置かれる。
        </p>
  </remarks>
  <listRef>
    <ptr target="#CORS5" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2017-06-14" xml:lang="en">column beginning</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">열 바꿈</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">分段</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">段の開始</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2022-05-12" xml:lang="fr">début de colonne</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2022-05-12" xml:lang="es">inicio de columna</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2022-08-17" xml:lang="it">inizio di colonna</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-03-31" xml:lang="en">marks the beginning of a new column of a text on a
  multi-column page.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준 참조 시스템에서 텍스트의 한 열과 다음 열 사이의 경계를 표지한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用標準參照系統來標明文本段落之間的分界。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-10-02" xml:lang="ja">複数段の頁で、テキストの新しい段の開始を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2022-05-12" xml:lang="fr">marque le
  début d'une nouvelle colonne  de texte sur une page multi-colonne.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-05-12" xml:lang="es">indica el inicio de una nueva columna de texto en una página divida en columnas .</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2022-08-17" xml:lang="it">segna l'inizio di una nuova colonna di un testo in una pagina a più colonne.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.breaking"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>Markup of an early English dictionary printed in two columns:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cb-egXML-mv" source="#REF-cb-eg-1">
      <pb/>
      <cb n="1"/>
      <entryFree><form>Well</form>, <sense>a Pit to hold Spring-Water</sense>:
                <sense>In the Art of <hi rend="italic">War</hi>, a Depth the Miner
                    sinks into the Ground, to find out and disappoint the Enemies Mines,
                    or to prepare one</sense>.</entryFree>
      <entryFree>To <form>Welter</form>, <sense>to wallow</sense>, or
                <sense>lie groveling</sense>.</entryFree>
      <!-- remainder of column -->
      <cb n="2"/>
      <entryFree><form>Wey</form>, <sense>the greatest Measure for dry Things,
                    containing five Chaldron</sense>.</entryFree>
      <entryFree><form>Whale</form>, <sense>the greatest of
                    Sea-Fishes</sense>.</entryFree>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="cb-remarks" versionDate="2013-03-31" xml:lang="en">
    <p>On this element, the global <att>n</att> attribute indicates the number or other value associated with the column
            which follows the point of insertion of this <gi>cb</gi> element. Encoders should adopt a clear and consistent policy as to
            whether the numbers associated with column beginnings relate to the physical
            sequence number of the column in the whole text, or whether columns are
            numbered within the page.
            The <gi>cb</gi> element is placed at the head of the
            column to which it refers.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="cb-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut global <att>n</att> donne un nouveau numéro ou une autre valeur à la
            colonne qui suit l'élément <gi>cb</gi>. Les encodeurs doivent faire un choix clair,
            et s'y tenir, entre l'option consistant à se fonder sur la séquence physique des
            colonnes dans le texte entier, et celle qui consiste à se fonder sur la numérotation
            des colonnes à l'intérieur de la page. L'élément <gi>cb</gi>
            apparaît en haut de la colonne à laquelle il se rapporte.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="cb-remarks" versionDate="2023-10-02" xml:lang="ja">
    <p>
      この要素では、グローバル属性<att>n</att>はこの<gi>cb</gi>要素の直後から始まる段と関連する数値等の値を示す。テキスト全体における段の通し番号を付けるか、ページ内における番号を付けるかについて、明確で一貫した方針を採用すべきである。<gi>cb</gi>要素は指している段の冒頭に置かれる。
        </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CORS5" type="div3"/>
  </listRef>
```

^b21

