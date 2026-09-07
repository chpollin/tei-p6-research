---
type: representation
source-type: document
source: '[[00_sources/tei-p5-pb-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 pb
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/pb.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# pb

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7298. Git blob: `042266e49da7c865fbdf16a953e2b51a7ccd6749`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-pb" ident="pb">
  <gloss versionDate="2017-06-14" xml:lang="en">page beginning</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">페이지 바꿈</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">分頁</gloss>
  <gloss versionDate="2022-05-12" xml:lang="fr">début de page</gloss>
  <gloss versionDate="2022-05-12" xml:lang="es">inicio de página</gloss>
  <gloss versionDate="2022-08-17" xml:lang="it">inizio di pagina</gloss>
  <gloss versionDate="2017-06-25" xml:lang="de">Seitenanfang</gloss>
  <desc versionDate="2017-06-14" xml:lang="en">marks the beginning of a new page in a paginated document.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준 참조 시스템에서 텍스트 페이지와 다음 페이지 사이의 경계를 표지한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">以標準參照系統來標記頁與頁之間的分界線。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストのページ境界を、標準的な参照システム示す。</desc>
  <desc versionDate="2022-05-12" xml:lang="fr">marque le début d'une
  page de texte dans un document paginé.</desc>
  <desc versionDate="2022-05-12" xml:lang="es">marca el inicio de una nueva página de un texto
    en un documento paginado.</desc>
  <desc versionDate="2022-08-17" xml:lang="it">segna l'inizio di una nuova pagina in un documento impaginato.</desc>
  <desc versionDate="2017-06-25" xml:lang="de">markiert den Anfang 
    einer neuen Seite in einem Dokument mit Seitenzahlen.</desc>
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
    <p>Page numbers may vary in different editions of a text.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pb-egXML-dg">
      <p> ... <pb n="145" ed="ed2"/>
            <!-- Page 145 in edition "ed2" starts here --> ... <pb n="283" ed="ed1"/>
            <!-- Page 283 in edition "ed1" starts here--> ... </p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Die Seitenzahlen können in verschiedenen Ausgaben eines Textes variieren.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pb-egXML-jl">
      <p> ... <pb n="145" ed="ed2"/>
        <!-- Seite 145 in Ausgabe "ed2" beginnt hier --> ... <pb n="283" ed="ed1"/>
        <!-- Seite 283 in Ausgabe "ed1" beginnt hier --> ... </p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>A page beginning may be associated with a facsimile image of the page it introduces by means of
      the <att>facs</att> attribute</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pb-egXML-qc" source="#UND">
      <body>
        <pb n="1" facs="page1.png"/>
        <!-- page1.png contains an image of the page;
                        the text it contains is encoded here -->
        <p>
          <!-- ... -->
        </p>
        <pb n="2" facs="page2.png"/>
        <!-- similarly, for page 2 -->
        <p>
          <!-- ... -->
        </p>
      </body>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Ein Seitenumbruch kann über das <att>facs</att>-Attribut mit einem Faksimile der Seite verknüpft
      werden.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pb-egXML-xc" source="#UND">
      <body>
        <pb n="1" facs="page1.png"/>
        <!-- page1.png enthält eine Abbildung der Seite;
                        der enthaltene Text ist hier kodiert -->
        <p>
          <!-- ... -->
        </p>
        <pb n="2" facs="page2.png"/>
        <!-- dasselbe gilt für Seite 2 -->
        <p>
          <!-- ... -->
        </p>
      </body>
    </egXML>
  </exemplum>
  <remarks ident="pb-remarks" versionDate="2016-11-29" xml:lang="en">
    <p>A <gi>pb</gi> element should appear at the start of the page
    which it identifies. The global <att>n</att> attribute indicates
    the number or other value associated with this page. This will
    normally be the page number or signature printed on it, since the
    physical sequence number is implicit in the presence of the
    <gi>pb</gi> element itself. </p>
    <p>The <att>type</att> attribute may be used to characterize 
      the page beginning in any respect. The more specialized attributes 
      <att>break</att>, <att>ed</att>, or <att>edRef</att> should be 
      preferred when the intent is to indicate whether or not the 
      page beginning is word-breaking, or to note the source from 
      which it derives.</p>
  </remarks>
  <remarks ident="pb-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un élément <gi>pb</gi> apparaît au début de la page à laquelle
    il se rapporte. L'attribut global <att>n</att> donne un numéro ou
    une autre valeur associée à cette page. Ce sera normalement le
    numéro de page ou la signature qui y est imprimée, puisque le
    numéro d'ordre matériel est implicite avec l'élément <gi>pb</gi>
    lui-même.</p>
    <p> L' attribut <att>type</att> sera employé pour indiquer toutes ses
      caractéristiques du saut de page, par exemple comme coupure de mot ou non. </p>
  </remarks>
  <remarks ident="pb-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素にあるグローバル属性<att>n</att>は、当該要素<gi>pb</gi>があ る場所に続いてあるページと関連する数値を示す。符号化する人は、改ペー
      ジと関連する数値が、物理的な一連の番号になるのか、または印刷されてい る番号になるのかについて、明確で一貫した方針を採るべきである。
      一般には、要素<gi>pb</gi>は、参照するページの始めに置かれるべきである。 </p>
  </remarks>
  <remarks ident="pb-remarks" versionDate="2016-11-29" xml:lang="de">
    <p>Ein <gi>pb</gi>-Element soll am Beginn der Seite stehen, die es kennzeichnet. 
      Das globale <att>n</att>-Attribut gibt die Zahl (oder einen anderen Wert) an, 
      der mit dieser Seite verbunden ist. Üblicherweise ist das die Seitenzahl 
      oder eine auf der Seite abgedruckte Signatur, da die Position in der 
      physikalischen Sequenz durch das <gi>pb</gi>-Element implizit ist. </p>
    <p>Das <att>type</att>-Attribut kann verwendet werden, den Seitenumbruch 
      näher zu beschreiben, wenn nicht die speziellen Attribute 
      <att>break</att> (Worttrennung), <att>ed</att> oder <att>edRef</att> 
      (Textzeuge, in dem der Seitenumbruch vorkommt) verwendet werden können.</p>
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
<gloss versionDate="2017-06-14" xml:lang="en">page beginning</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">페이지 바꿈</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">分頁</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2022-05-12" xml:lang="fr">début de page</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2022-05-12" xml:lang="es">inicio de página</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2022-08-17" xml:lang="it">inizio di pagina</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-25" xml:lang="de">Seitenanfang</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-06-14" xml:lang="en">marks the beginning of a new page in a paginated document.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준 참조 시스템에서 텍스트 페이지와 다음 페이지 사이의 경계를 표지한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">以標準參照系統來標記頁與頁之間的分界線。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストのページ境界を、標準的な参照システム示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2022-05-12" xml:lang="fr">marque le début d'une
  page de texte dans un document paginé.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-05-12" xml:lang="es">marca el inicio de una nueva página de un texto
    en un documento paginado.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2022-08-17" xml:lang="it">segna l'inizio di una nuova pagina in un documento impaginato.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-25" xml:lang="de">markiert den Anfang 
    einer neuen Seite in einem Dokument mit Seitenzahlen.</desc>
```

^b15

### Block 16

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

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>Page numbers may vary in different editions of a text.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pb-egXML-dg">
      <p> ... <pb n="145" ed="ed2"/>
            <!-- Page 145 in edition "ed2" starts here --> ... <pb n="283" ed="ed1"/>
            <!-- Page 283 in edition "ed1" starts here--> ... </p>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Die Seitenzahlen können in verschiedenen Ausgaben eines Textes variieren.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pb-egXML-jl">
      <p> ... <pb n="145" ed="ed2"/>
        <!-- Seite 145 in Ausgabe "ed2" beginnt hier --> ... <pb n="283" ed="ed1"/>
        <!-- Seite 283 in Ausgabe "ed1" beginnt hier --> ... </p>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <p>A page beginning may be associated with a facsimile image of the page it introduces by means of
      the <att>facs</att> attribute</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pb-egXML-qc" source="#UND">
      <body>
        <pb n="1" facs="page1.png"/>
        <!-- page1.png contains an image of the page;
                        the text it contains is encoded here -->
        <p>
          <!-- ... -->
        </p>
        <pb n="2" facs="page2.png"/>
        <!-- similarly, for page 2 -->
        <p>
          <!-- ... -->
        </p>
      </body>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Ein Seitenumbruch kann über das <att>facs</att>-Attribut mit einem Faksimile der Seite verknüpft
      werden.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pb-egXML-xc" source="#UND">
      <body>
        <pb n="1" facs="page1.png"/>
        <!-- page1.png enthält eine Abbildung der Seite;
                        der enthaltene Text ist hier kodiert -->
        <p>
          <!-- ... -->
        </p>
        <pb n="2" facs="page2.png"/>
        <!-- dasselbe gilt für Seite 2 -->
        <p>
          <!-- ... -->
        </p>
      </body>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="pb-remarks" versionDate="2016-11-29" xml:lang="en">
    <p>A <gi>pb</gi> element should appear at the start of the page
    which it identifies. The global <att>n</att> attribute indicates
    the number or other value associated with this page. This will
    normally be the page number or signature printed on it, since the
    physical sequence number is implicit in the presence of the
    <gi>pb</gi> element itself. </p>
    <p>The <att>type</att> attribute may be used to characterize 
      the page beginning in any respect. The more specialized attributes 
      <att>break</att>, <att>ed</att>, or <att>edRef</att> should be 
      preferred when the intent is to indicate whether or not the 
      page beginning is word-breaking, or to note the source from 
      which it derives.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="pb-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un élément <gi>pb</gi> apparaît au début de la page à laquelle
    il se rapporte. L'attribut global <att>n</att> donne un numéro ou
    une autre valeur associée à cette page. Ce sera normalement le
    numéro de page ou la signature qui y est imprimée, puisque le
    numéro d'ordre matériel est implicite avec l'élément <gi>pb</gi>
    lui-même.</p>
    <p> L' attribut <att>type</att> sera employé pour indiquer toutes ses
      caractéristiques du saut de page, par exemple comme coupure de mot ou non. </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="pb-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素にあるグローバル属性<att>n</att>は、当該要素<gi>pb</gi>があ る場所に続いてあるページと関連する数値を示す。符号化する人は、改ペー
      ジと関連する数値が、物理的な一連の番号になるのか、または印刷されてい る番号になるのかについて、明確で一貫した方針を採るべきである。
      一般には、要素<gi>pb</gi>は、参照するページの始めに置かれるべきである。 </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="pb-remarks" versionDate="2016-11-29" xml:lang="de">
    <p>Ein <gi>pb</gi>-Element soll am Beginn der Seite stehen, die es kennzeichnet. 
      Das globale <att>n</att>-Attribut gibt die Zahl (oder einen anderen Wert) an, 
      der mit dieser Seite verbunden ist. Üblicherweise ist das die Seitenzahl 
      oder eine auf der Seite abgedruckte Signatur, da die Position in der 
      physikalischen Sequenz durch das <gi>pb</gi>-Element implizit ist. </p>
    <p>Das <att>type</att>-Attribut kann verwendet werden, den Seitenumbruch 
      näher zu beschreiben, wenn nicht die speziellen Attribute 
      <att>break</att> (Worttrennung), <att>ed</att> oder <att>edRef</att> 
      (Textzeuge, in dem der Seitenumbruch vorkommt) verwendet werden können.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CORS5" type="div3"/>
  </listRef>
```

^b26

