---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.editlike-4.12.0.xml]]'
converter: tools.ingest_git_blobs v2; complete XML plus XML itertext English reading
  blocks with whitespace normalized and identified locators
channel: collection
metadata:
  title: TEI P5 4.12.0 att.editLike specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.editLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# att.editLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.
A locator names an element that carries an `ident` attribute by that ident, so the
reading block of an attribute definition states which attribute it describes.

Source byte length: 8092. Git blob: `125dd51d6ec3328982d02edc0740d71638ccfa2e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" ident="att.editLike">
  <desc versionDate="2012-02-14" xml:lang="en">provides attributes describing the nature of an encoded scholarly intervention or
    interpretation of any kind.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 유형의 부호화된 학문적 간섭 또는 해석의 특성을 기술하는 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供屬性，描述任何已標記的學者更正或詮釋的性質。</desc>
  <desc versionDate="2019-05-20" xml:lang="ja">学術的調整・解釈の性質を表す属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs décrivant la nature d'une
    intervention savante encodée ou de tout autre interprétation.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos que describen la naturaleza de una
    intervención crítica codificada o una interpretación de cualquier tipo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi che descrivono il carattere di un
    intervento critico codificato o interpretazione di altro tipo</desc>
  <attList>
    <attDef ident="evidence" usage="opt">
      <desc versionDate="2005-12-13" xml:lang="en">indicates the nature of the evidence supporting the reliability or accuracy of the
        intervention or interpretation.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">간섭 또는 해석의 신뢰성 또는 정확성을 지지하는 증거의 특성을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出支持該更動或詮釋可信度或正確性的證明</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該解釈や調整の信頼度や正確さを判断する証拠を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique la nature de la preuve attestant la fiabilité
        ou la justesse de l'intervention ou de l'interprétation.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la naturaleza de las pruebas que sostienen la
        fiabilidad o precisión de la intervención o interpretación.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il carattere delle prove a sostegno
        dell'affidabilità o accuratezza dell'intervento o interpretazione</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="internal">
          <desc versionDate="2007-04-15" xml:lang="en">there is internal evidence to support the intervention.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">간섭을 지지하는 내부 증거가 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">有內部證明得以支持</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該調整を判断する内部証拠を示す。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'intervention est justifiée par une preuve
            interne</desc>
          <desc versionDate="2007-05-04" xml:lang="es">existen pruebas internas que sostienen la
            intervención.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">esistono prove interne a sostegno
          dell'intervento</desc>
        </valItem>
        <valItem ident="external">
          <desc versionDate="2007-04-15" xml:lang="en">there is external evidence to support the intervention.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">간섭을 지지하는 외부 증거가 있다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">有外部證明得以支持</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該調整を判断する外部証拠を示す。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'intervention est justifiée par une preuve
            externe</desc>
          <desc versionDate="2007-05-04" xml:lang="es">existen pruebas externas que sostienen la
            intervención.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">esistono prove interne a sostegno
          dell'intervento</desc>
        </valItem>
        <valItem ident="conjecture">
          <desc versionDate="2007-04-15" xml:lang="en">the intervention or interpretation has been made by the editor, cataloguer, or
            scholar on the basis of their expertise.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">간섭 또는 해석이 편집자, 또는 전문성에 근거한 학자에 의해 수행되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">編輯、編目者或學者根據自身的專業來執行該更動或詮釋。</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">編集者、カタログ作成者、研究者による解釈や調整。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'intervention ou l'interprétation a été faite
            par le rédacteur, le catalogueur, ou le chercheur sur la base de leur expertise.</desc>
          <desc versionDate="2007-05-04" xml:lang="es">la intervención o interpretación ha sido hecho
            por el editor, catalogador o crítico en base a su experiencia.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'intervento o interpretazione è stata effettuata
            dal curatore, catalogatore o critico in base alla loro esperienza</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="instant">
      <desc versionDate="2012-12-27" xml:lang="en">indicates whether this is an instant revision or not.</desc>
      <desc versionDate="2019-05-20" xml:lang="ja">これがにわか仕込みの修正か否かを示す。</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <defaultVal>false</defaultVal>
    </attDef>
  </attList>
  <remarks ident="att.editLike-remarks" versionDate="2019-09-15" xml:lang="en">
    <p>The members of this attribute class are typically used to represent any kind of editorial
      intervention in a text, for example a correction or interpretation, or to date or localize
      manuscripts etc.</p>
    <p>Each pointer on the <att>source</att> (if present)
      corresponding to a witness or witness group should reference a bibliographic citation such as a <gi>witness</gi>, <gi>msDesc</gi>, or <gi>bibl</gi> element, or another external bibliographic citation, documenting the source concerned.</p>
  </remarks>
  <remarks ident="att.editLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les membres de cette classe d'attributs sont couramment employés pour représenter tout type
      d'intervention éditoriale dans un texte, par exemple une correction ou une interprétation, ou
      bien une datation ou une localisation de manuscrit, etc. </p>
  </remarks>
  <remarks ident="att.editLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>los miembros de esta clase de atributo se usan normalmente para representar cualquier tipo de
      intervención editorial en un texto, por ejemplo una corrección, una interpretación, la fecha o
      incluso la signatura de los manuscritos etc.</p>
  </remarks>
  <remarks ident="att.editLike-remarks" versionDate="2019-05-20" xml:lang="ja"><p>当該クラスは、あらゆる編集上の調整、例えば、原稿に対する修正や解釈、日時や場所の特定などを示すために、一般には使用される。</p></remarks>
  <listRef>
<ptr target="#COED"/>
<ptr target="#msdates"/>
<ptr target="#NDPERSE"/>
<ptr target="#PHCO"/>
  </listRef>
</classSpec>
```

## English reading blocks

### Reading 1

XML location: `/classSpec[@ident='att.editLike']/desc[1]`.

provides attributes describing the nature of an encoded scholarly intervention or interpretation of any kind. ^r1

### Reading 2

XML location: `/classSpec[@ident='att.editLike']/attList[1]/attDef[@ident='evidence']/desc[1]`.

indicates the nature of the evidence supporting the reliability or accuracy of the intervention or interpretation. ^r2

### Reading 3

XML location: `/classSpec[@ident='att.editLike']/attList[1]/attDef[@ident='evidence']/valList[1]/valItem[@ident='internal']/desc[1]`.

there is internal evidence to support the intervention. ^r3

### Reading 4

XML location: `/classSpec[@ident='att.editLike']/attList[1]/attDef[@ident='evidence']/valList[1]/valItem[@ident='external']/desc[1]`.

there is external evidence to support the intervention. ^r4

### Reading 5

XML location: `/classSpec[@ident='att.editLike']/attList[1]/attDef[@ident='evidence']/valList[1]/valItem[@ident='conjecture']/desc[1]`.

the intervention or interpretation has been made by the editor, cataloguer, or scholar on the basis of their expertise. ^r5

### Reading 6

XML location: `/classSpec[@ident='att.editLike']/attList[1]/attDef[@ident='instant']/desc[1]`.

indicates whether this is an instant revision or not. ^r6

### Reading 7

XML location: `/classSpec[@ident='att.editLike']/remarks[@ident='att.editLike-remarks']/p[1]`.

The members of this attribute class are typically used to represent any kind of editorial intervention in a text, for example a correction or interpretation, or to date or localize manuscripts etc. ^r7

### Reading 8

XML location: `/classSpec[@ident='att.editLike']/remarks[@ident='att.editLike-remarks']/p[2]`.

Each pointer on the source (if present) corresponding to a witness or witness group should reference a bibliographic citation such as a witness, msDesc, or bibl element, or another external bibliographic citation, documenting the source concerned. ^r8

