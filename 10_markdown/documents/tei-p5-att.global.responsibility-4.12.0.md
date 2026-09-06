---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.global.responsibility-4.12.0.xml]]'
converter: tools.ingest_git_blobs v2; complete XML plus XML itertext English reading
  blocks with whitespace normalized and identified locators
channel: collection
metadata:
  title: TEI P5 4.12.0 att.global.responsibility specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.global.responsibility.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# att.global.responsibility

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

Source byte length: 6738. Git blob: `65688b68bc20ebdc18452ae2b285d581542e2363`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" predeclare="true" type="atts" xml:id="class-attr-global.responsibility" ident="att.global.responsibility">
  <desc versionDate="2014-12-10" xml:lang="en">provides attributes indicating the agent
    responsible for some aspect of the text, the markup or 
    something asserted by the markup, and the degree of certainty 
    associated with it.</desc>
  <desc versionDate="2022-05-09" xml:lang="ja">テキストやマークアップ、あるいはマークアップによって示されたものの何らかの側面についての責任者と、それに関する確信の度合を示す属性を提供する。</desc>
  <classes>
    
  
    
  </classes>
  <attList>
    <attDef ident="cert" usage="opt">
      <gloss versionDate="2009-11-02" xml:lang="en">certainty</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">확실성</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">certeza</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">certitude</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">certezza</gloss>
      <gloss versionDate="2022-05-09" xml:lang="ja">確信性</gloss>
      <desc versionDate="2009-11-02" xml:lang="en">signifies the degree of certainty associated with the intervention or interpretation.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">간섭 또는 해석과 연관된 확실성의 정도를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">表示該更動或詮釋的相關正確度。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne le degré de certitude associée à l'intervention
        ou à l'interprétation.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">significa el grado de certeza asociado con la
        intervención o la interpretación.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">corrisponde al grado di certezza associato
        all'intervento o interpretazione</desc>
      <desc versionDate="2019-09-16" xml:lang="ja">介入や解釈に関する確信度を示す。</desc>
      <datatype>
        <dataRef key="teidata.probCert"/>
      </datatype>
    </attDef>
    <attDef ident="resp" usage="opt">
      <gloss versionDate="2009-11-02" xml:lang="en">responsible party</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">책임 당사자</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">parte responsable</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">responsable</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">responsabile</gloss>
      <gloss versionDate="2019-09-16" xml:lang="ja">責任者</gloss>
      <desc versionDate="2009-11-02" xml:lang="en">indicates the agency responsible for the intervention or interpretation, for example an
        editor or transcriber.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">편집자 또는 전사자와 같이 또는 해석에 대한 책임이 있는 대리인을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出負責該更動或詮釋的代理者，例如編輯或轉錄者。</desc>
      <desc versionDate="2019-09-16" xml:lang="ja">介入や解釈の責任者を示す。例えば、編集者、翻刻者など。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique l'agent responsable de l'intervention ou de
        l'interprétation, par exemple un éditeur ou un transcripteur.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el agente responsable de la intervención o la
        interpretación, p.ej. un editor o un transcriptor.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il responsabile dell'intervento o
        interpretazione, per esempio un curatore o trascrittore</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.global.responsibility-attr.resp-remarks" versionDate="2014-12-10" xml:lang="en">
        <p>To reduce the ambiguity of a <att>resp</att> pointing directly to a person or 
          organization, we 
          recommend that <att>resp</att> be used to point not to an agent 
          (<gi>person</gi> or <gi>org</gi>) but to a <gi>respStmt</gi>, 
          <gi>author</gi>, <gi>editor</gi> or similar 
          element which clarifies the exact role played by the agent. 
          Pointing to multiple <gi>respStmt</gi>s allows the encoder to specify 
          clearly each of the roles played in part of a TEI file (creating, 
          transcribing, encoding, editing, proofing etc.).</p></remarks>
      <remarks ident="att.global.responsibility-attr.resp-remarks" versionDate="2019-09-16" xml:lang="ja"><p><att>resp</att> が直接個人や組織を指した場合のあいまいさを減らすため、<att>resp</att> は行為者 (<gi>person</gi> or <gi>org</gi>) ではなく <gi>respStmt</gi>、<gi>author</gi>、<gi>editor</gi> などその行為者の正確な役割を明示するエレメントを指して用いることを推奨する。エンコード者は <gi>respStmt</gi> にTEI文書内の役割分担を明確に記述できる（作成・翻刻・エンコード・編集・校正など。</p></remarks>
  </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.responsibility-egXML-zm">Blessed are the 
      <choice><sic>cheesemakers</sic><corr resp="#editor" cert="high">peacemakers</corr></choice>: for they shall be called the children of God.</egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.responsibility-egXML-zc" source="#TAYLOR">
      <!-- in the <text> ... -->
      <lg>
        <!-- ... -->
      <l>Punkes, Panders, baſe extortionizing 
        sla<choice><sic>n</sic><corr resp="#JENS1_transcriber">u</corr></choice>es,</l>
        <!-- ... -->
      </lg>
      <!-- in the <teiHeader> ... -->
      <!-- ... -->
      <respStmt xml:id="JENS1_transcriber">
        <resp when="2014">Transcriber</resp>
        <name>Janelle Jenstad</name>
      </respStmt>
    </egXML>
  </exemplum>
  
  <listRef>
    <ptr target="#STGAso"/>
    <ptr target="#COED"/>
    <ptr target="#PHHR"/>
    <ptr target="#AISP"/>
    <ptr target="#NDATTSnr"/>
  </listRef>
</classSpec>
```

## English reading blocks

### Reading 1

XML location: `/classSpec[@ident='att.global.responsibility']/desc[1]`.

provides attributes indicating the agent responsible for some aspect of the text, the markup or something asserted by the markup, and the degree of certainty associated with it. ^r1

### Reading 2

XML location: `/classSpec[@ident='att.global.responsibility']/attList[1]/attDef[@ident='cert']/desc[1]`.

signifies the degree of certainty associated with the intervention or interpretation. ^r2

### Reading 3

XML location: `/classSpec[@ident='att.global.responsibility']/attList[1]/attDef[@ident='resp']/desc[1]`.

indicates the agency responsible for the intervention or interpretation, for example an editor or transcriber. ^r3

### Reading 4

XML location: `/classSpec[@ident='att.global.responsibility']/attList[1]/attDef[@ident='resp']/remarks[@ident='att.global.responsibility-attr.resp-remarks']/p[1]`.

To reduce the ambiguity of a resp pointing directly to a person or organization, we recommend that resp be used to point not to an agent (person or org) but to a respStmt, author, editor or similar element which clarifies the exact role played by the agent. Pointing to multiple respStmts allows the encoder to specify clearly each of the roles played in part of a TEI file (creating, transcribing, encoding, editing, proofing etc.). ^r4

