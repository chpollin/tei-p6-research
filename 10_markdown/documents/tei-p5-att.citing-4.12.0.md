---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.citing-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.citing
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.citing.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.citing

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7803. Git blob: `1ce0f760f405baef8b167dfab6431e0e44dd5b84`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.citing">
  <desc versionDate="2014-01-10" xml:lang="en">provides attributes for specifying the specific part of a bibliographic item being cited.</desc>
  <desc versionDate="2019-01-04" xml:lang="ja">引用された書誌の特定箇所を指示するための属性を提供する。</desc>
  <classes/>
  <attList>
    <attDef ident="unit" usage="opt">
      <desc versionDate="2025-03-31" xml:lang="en">identifies the unit of information conveyed by the element.</desc>
      <desc versionDate="2025-03-31" xml:lang="fr">identifie le type d'information que transmet l'élément.</desc>
      <desc versionDate="2019-01-04" xml:lang="ja">当該要素が伝える情報の単位を特定する。たとえば、カラム (<val>columns</val>)、頁 (<val>pages</val>)、巻 (<val>volume</val>)、エントリ (<val>entry</val>) 等。</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
	<valItem ident="volume">
	  <gloss versionDate="2007-05-04" xml:lang="en">volume</gloss>
	  <gloss versionDate="2007-12-20" xml:lang="ko">권</gloss>
	  <gloss versionDate="2021-01-18" xml:lang="es">volumen</gloss>
	  <desc versionDate="2013-06-17" xml:lang="en">the element contains a volume number.</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">권수를 포함한다.</desc>
	  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素標記的內容為冊號。</desc>
	  <desc versionDate="2008-04-06" xml:lang="es">el elemento contiene el número de volumen.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">巻番号を含む。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément contient un numéro de volume.</desc>
	  <desc versionDate="2007-01-21" xml:lang="it">l'elemento contiene il numero del volume.</desc>
	</valItem>
	<valItem ident="issue">
	  <desc versionDate="2012-12-17" xml:lang="en">the element contains an issue number, or volume and
	  issue numbers.</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">호, 또는 권과 호를 포함한다.</desc>
	  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素標記的內容為一期刊號或冊號與期刊號。</desc>
	  <desc versionDate="2008-04-06" xml:lang="es">el elemento contiene el número de la edición, o los números del volumen y de la edición.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">号番号かまたは巻と号の番号を含む。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément contient un numéro de livraison ou bien un numéro de volume et de livraison.</desc>
	  <desc versionDate="2007-01-21" xml:lang="it">l'elemento contiene l'indicazione del numero della pubblicazione.</desc>
	</valItem>
	<valItem ident="page">
	  <gloss versionDate="2007-05-04" xml:lang="en">page</gloss>
	  <gloss versionDate="2007-12-20" xml:lang="ko">페이지</gloss>
	  <gloss versionDate="2007-11-06" xml:lang="it">pagine</gloss>
	  <gloss versionDate="2021-01-18" xml:lang="es">página</gloss>
	  <desc versionDate="2013-06-17" xml:lang="en">the element contains a page number or page range.</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">페이지 번호 또는 페이지 범위를 포함한다.</desc>
	  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素標記的內容為一頁數或頁數範圍。</desc>
	  <desc versionDate="2021-01-18" xml:lang="es">el elemento contiene un número de página o un intervalo de páginas.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">ページ番号またはページ範囲を含む。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément contient un nombre de pages ou l'étendue de sélection des pages.</desc>
	  <desc versionDate="2007-01-21" xml:lang="it">l'elemento contiene l'indicazione di pagina o pagine.</desc>
	</valItem>
	<valItem ident="line">
	  <desc versionDate="2013-06-17" xml:lang="en">the element contains a line number or line range.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">行番号か行範囲を含む。</desc>
	</valItem>
	<valItem ident="chapter">
	  <gloss versionDate="2007-11-06" xml:lang="en">chapter</gloss>
	  <gloss versionDate="2007-12-20" xml:lang="ko">장</gloss>
	  <gloss versionDate="2008-04-06" xml:lang="es">capítulo</gloss>
	  <gloss versionDate="2009-01-06" xml:lang="fr">chapitre</gloss>
	  <gloss versionDate="2007-11-06" xml:lang="it">capitolo</gloss>
	  <desc versionDate="2013-06-17" xml:lang="en">the element contains a chapter indication (number and/or title)</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">장 표시(숫자와/또는 제목)를 포함한다.</desc>
	  <desc versionDate="2008-04-06" xml:lang="es">el elemento contiene la indicación del capítulo (número y/o el título)</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">章の識別子(番号やタイトル)を含む。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément contient une indication de chapitre (le numéro et/ou le titre)</desc>
	  <desc versionDate="2007-11-06" xml:lang="it">l'elemento contiene un'indicazione di capitolo (numero e/o titolo).</desc>
	</valItem>
	<valItem ident="part">
	  <desc versionDate="2012-12-17" xml:lang="en">the element identifies a part of a book or collection.</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">책 또는 모음집의 부분을 식별한다.</desc>
	  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素標明的內容為單書或集合作品的一部份。</desc>
	  <desc versionDate="2008-04-06" xml:lang="es">el elemento identifica una parte de un libro o de una colección.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">書籍や叢書の部分を特定する。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément identifie une partie d'un livre ou une anthologie.</desc>
	  <desc versionDate="2007-01-21" xml:lang="it">l'elemento identifica una parte di un libro o di una raccolta.</desc>
	</valItem>
	<valItem ident="column">
		<desc versionDate="2013-06-17" xml:lang="en">the element identifies a column.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">一つのカラムを特定する。</desc>
	</valItem>
        <valItem ident="entry">
        	<desc versionDate="2017-10-29" xml:lang="en">the element identifies an entry number or label in a list of entries.</desc>
          <desc versionDate="2019-01-04" xml:lang="ja">エントリのリスト中の番号やラベルを特定する。</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="from">
      <desc versionDate="2013-01-08" xml:lang="en">specifies the starting point of the range of units indicated by the <att>unit</att> attribute.</desc>
      <desc versionDate="2019-01-04" xml:lang="ja"><att>unit</att>属性で指定された時間単位の幅における開始点を表す。</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
    <attDef ident="to">
      <desc versionDate="2013-01-08" xml:lang="en">specifies the end-point of the range of units indicated by the <att>unit</att> attribute.</desc>
      <desc versionDate="2019-01-04" xml:lang="ja"><att>unit</att>属性で指定された時間単位の幅における終点を表す。</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#STECAT"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2014-01-10" xml:lang="en">provides attributes for specifying the specific part of a bibliographic item being cited.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-01-04" xml:lang="ja">引用された書誌の特定箇所を指示するための属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes/>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2025-03-31" xml:lang="en">identifies the unit of information conveyed by the element.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2025-03-31" xml:lang="fr">identifie le type d'information que transmet l'élément.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2019-01-04" xml:lang="ja">当該要素が伝える情報の単位を特定する。たとえば、カラム (<val>columns</val>)、頁 (<val>pages</val>)、巻 (<val>volume</val>)、エントリ (<val>entry</val>) 等。</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
	<valItem ident="volume">
	  <gloss versionDate="2007-05-04" xml:lang="en">volume</gloss>
	  <gloss versionDate="2007-12-20" xml:lang="ko">권</gloss>
	  <gloss versionDate="2021-01-18" xml:lang="es">volumen</gloss>
	  <desc versionDate="2013-06-17" xml:lang="en">the element contains a volume number.</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">권수를 포함한다.</desc>
	  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素標記的內容為冊號。</desc>
	  <desc versionDate="2008-04-06" xml:lang="es">el elemento contiene el número de volumen.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">巻番号を含む。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément contient un numéro de volume.</desc>
	  <desc versionDate="2007-01-21" xml:lang="it">l'elemento contiene il numero del volume.</desc>
	</valItem>
	<valItem ident="issue">
	  <desc versionDate="2012-12-17" xml:lang="en">the element contains an issue number, or volume and
	  issue numbers.</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">호, 또는 권과 호를 포함한다.</desc>
	  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素標記的內容為一期刊號或冊號與期刊號。</desc>
	  <desc versionDate="2008-04-06" xml:lang="es">el elemento contiene el número de la edición, o los números del volumen y de la edición.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">号番号かまたは巻と号の番号を含む。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément contient un numéro de livraison ou bien un numéro de volume et de livraison.</desc>
	  <desc versionDate="2007-01-21" xml:lang="it">l'elemento contiene l'indicazione del numero della pubblicazione.</desc>
	</valItem>
	<valItem ident="page">
	  <gloss versionDate="2007-05-04" xml:lang="en">page</gloss>
	  <gloss versionDate="2007-12-20" xml:lang="ko">페이지</gloss>
	  <gloss versionDate="2007-11-06" xml:lang="it">pagine</gloss>
	  <gloss versionDate="2021-01-18" xml:lang="es">página</gloss>
	  <desc versionDate="2013-06-17" xml:lang="en">the element contains a page number or page range.</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">페이지 번호 또는 페이지 범위를 포함한다.</desc>
	  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素標記的內容為一頁數或頁數範圍。</desc>
	  <desc versionDate="2021-01-18" xml:lang="es">el elemento contiene un número de página o un intervalo de páginas.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">ページ番号またはページ範囲を含む。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément contient un nombre de pages ou l'étendue de sélection des pages.</desc>
	  <desc versionDate="2007-01-21" xml:lang="it">l'elemento contiene l'indicazione di pagina o pagine.</desc>
	</valItem>
	<valItem ident="line">
	  <desc versionDate="2013-06-17" xml:lang="en">the element contains a line number or line range.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">行番号か行範囲を含む。</desc>
	</valItem>
	<valItem ident="chapter">
	  <gloss versionDate="2007-11-06" xml:lang="en">chapter</gloss>
	  <gloss versionDate="2007-12-20" xml:lang="ko">장</gloss>
	  <gloss versionDate="2008-04-06" xml:lang="es">capítulo</gloss>
	  <gloss versionDate="2009-01-06" xml:lang="fr">chapitre</gloss>
	  <gloss versionDate="2007-11-06" xml:lang="it">capitolo</gloss>
	  <desc versionDate="2013-06-17" xml:lang="en">the element contains a chapter indication (number and/or title)</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">장 표시(숫자와/또는 제목)를 포함한다.</desc>
	  <desc versionDate="2008-04-06" xml:lang="es">el elemento contiene la indicación del capítulo (número y/o el título)</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">章の識別子(番号やタイトル)を含む。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément contient une indication de chapitre (le numéro et/ou le titre)</desc>
	  <desc versionDate="2007-11-06" xml:lang="it">l'elemento contiene un'indicazione di capitolo (numero e/o titolo).</desc>
	</valItem>
	<valItem ident="part">
	  <desc versionDate="2012-12-17" xml:lang="en">the element identifies a part of a book or collection.</desc>
	  <desc versionDate="2007-12-20" xml:lang="ko">책 또는 모음집의 부분을 식별한다.</desc>
	  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素標明的內容為單書或集合作品的一部份。</desc>
	  <desc versionDate="2008-04-06" xml:lang="es">el elemento identifica una parte de un libro o de una colección.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">書籍や叢書の部分を特定する。</desc>
	  <desc versionDate="2008-03-30" xml:lang="fr">l'élément identifie une partie d'un livre ou une anthologie.</desc>
	  <desc versionDate="2007-01-21" xml:lang="it">l'elemento identifica una parte di un libro o di una raccolta.</desc>
	</valItem>
	<valItem ident="column">
		<desc versionDate="2013-06-17" xml:lang="en">the element identifies a column.</desc>
	  <desc versionDate="2019-01-04" xml:lang="ja">一つのカラムを特定する。</desc>
	</valItem>
        <valItem ident="entry">
        	<desc versionDate="2017-10-29" xml:lang="en">the element identifies an entry number or label in a list of entries.</desc>
          <desc versionDate="2019-01-04" xml:lang="ja">エントリのリスト中の番号やラベルを特定する。</desc>
        </valItem>
      </valList>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-01-08" xml:lang="en">specifies the starting point of the range of units indicated by the <att>unit</att> attribute.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2019-01-04" xml:lang="ja"><att>unit</att>属性で指定された時間単位の幅における開始点を表す。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2013-01-08" xml:lang="en">specifies the end-point of the range of units indicated by the <att>unit</att> attribute.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2019-01-04" xml:lang="ja"><att>unit</att>属性で指定された時間単位の幅における終点を表す。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b14

### Block 15

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STECAT"/>
  </listRef>
```

^b15

