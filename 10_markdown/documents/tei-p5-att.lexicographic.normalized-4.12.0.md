---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.lexicographic.normalized-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.lexicographic.normalized
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.lexicographic.normalized.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.lexicographic.normalized

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8351. Git blob: `3f9b1149961b8cb53ba8b92a105476c15e8b0c4e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="analysis" xml:id="ATTNORM" type="atts" ident="att.lexicographic.normalized">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes for usage within word-level elements in the analysis module and within lexicographic microstructure in the dictionaries module.</desc>
  <classes/>
  <attList>
    <attDef ident="norm" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">normalized</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko"> 표준화</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">normalizado</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">normalisé</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">normalizzato</gloss>
      
      <desc versionDate="2018-03-17" xml:lang="en">provides the normalized/standardized form of information present in the source text in a non-normalized form.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">비표준형으로 원본 텍스트에서 제시된 정보의 표준형을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一規格化形式的資訊，其來源文件為非規格化形式</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該テキストを、正規形を示す。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">donne une forme normalisée de l'information fournie par le texte source sous une forme non normalisée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proprorciona de manera normalizada información dada en el texto fuente de manera no normalizada</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce la forma normalizzata delle informazioni contenute nel testo di origine in forma non normalizzata.</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
      <exemplum xml:lang="en">
        <p>Normalization of part-of-speech information within a dictionary entry.</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-gi">
          <gramGrp>
            <pos norm="noun">n</pos>
          </gramGrp>
        </egXML>
      </exemplum>
      <exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-lk" source="#fr-ex-Grand-Robert">
          <gramGrp>
            <pos norm="nom">n.</pos>
          </gramGrp>
        </egXML>
      </exemplum>
      <exemplum xml:lang="en">
        <p>Normalization of a source form in a tokenized historical corpus.</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-pk">
          <s xmlns="">
            <w>for</w>
            <w norm="virtue's">vertues</w>
          <w>sake</w></s>
        </egXML>
      </exemplum>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-wd">
          <s xmlns="">
            <w norm="persuasion">perswasion</w>
            <w>of</w>
            <w norm="Unity">Vnitie</w>
          </s>
        </egXML>
      </exemplum>

      <exemplum xml:lang="en">
        <p>Example of normalization from <ref target="http://www.deutschestextarchiv.de/anonym_aviso_1609/258">Aviso. Relation oder Zeitung. Wolfenbüttel, 1609. In: Deutsches Textarchiv</ref>.</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-xl">
          <s xmlns="">
            <w norm="freiwillig">freywillig</w>
            <pc norm="," join="left">/</pc>
            <w norm="unbedrängt">vnbedraͤngt</w>
            <w norm="und">vnd</w>
            <w norm="unverhindert">vnuerhindert</w>
          </s>
        </egXML>
      </exemplum>

      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-xv">
          <w xmlns="" norm="Teil">Theyll</w>
        </egXML>
      </exemplum>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-le">
          <w xmlns="" norm="Freude">Frewde</w>
        </egXML>
      </exemplum>
    </attDef>
    
    <attDef ident="orig" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">original</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">원본</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">originale</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">gives the original string or is the empty string when the element does not appear in the source text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">원본 문자열을 제시하거나 요소가 원본텍스트에 나타나지 않을 때는 공백 문자열을 제시한다.</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">indique la chaîne originale ou contient une chaîne vide si l'élément n'apparaît pas dans le texte source.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">當該元素未出現於來源文件中，提供其原文字串或空白字串。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">元の文字列を示す。当該要素が元資料に無い場合には空になる。</desc>
      <desc versionDate="2007-05-04" xml:lang="es">da la serie original o la serie vacía cuando el elemento no aparece en el texto fuente</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce la stringa originale o la srtinga vuota quando l'elemento non compare nel testo di origine.</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
      
      <exemplum xml:lang="en">
        <p>Example from a language documentation project of the Mixtepec-Mixtec language (ISO 639-3:
        'mix'). This is a use case where speakers spell something incorrectly but we would
        like to preserve it for any number of reasons, the use of <att>orig</att> is essential and could
        have uses for both the speaker to see past mistakes, researchers to get insight into how
        untrained speakers write their language instinctually (in contrast to prescribed
        convention), etc.:</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-qs">
          <w orig="ntsa sia'i">ntsasia'i</w>
        </egXML>
      </exemplum>
      <exemplum xml:lang="en">
        <p>Example from the <ref target="https://earlyprint.org">EarlyPrint</ref> project. Fragment
        of text where obvious errors have been corrected but the original forms remain
        recorded:</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-ah">
          <w lemma="he" pos="pns" xml:id="b1afj-003-a-0950">he</w>
          <w lemma="have" pos="vvz" xml:id="b1afj-003-a-0960">hath</w>
          <w lemma="bring" pos="vvn" xml:id="b1afj-003-a-0970">brought</w>
          <w lemma="forth" pos="av" xml:id="b1afj-003-a-0980" orig="sorth">forth</w>
        </egXML>
      </exemplum>
      <exemplum xml:lang="en">
        <p>An example from the EarlyPrint project showing the use of both <att>norm</att> and <att>orig</att>. The <att>orig</att> attribute preserves the original version (sometimes with spelling errors, often with printer abbreviations), the element content resolves printer abbreviations but retains the original orthography, and the <att>norm</att> attribute holds normalized values:</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-sb">
          <w lemma="commandment" pos="n1" norm="commandment" xml:id="b9avr-018-a-7720" orig="commandemēt">commandement</w>
        </egXML>
      </exemplum>
    </attDef>

  </attList>
  <remarks ident="att.lexicographic.normalized-remarks" versionDate="2020-02-12" xml:lang="en">
    <p>It needs to be stressed that the two attributes in this class are meant for strictly
    lexicographic and linguistic uses, and not for editorial interventions. For the latter, the
    mechanism based on <gi>choice</gi>, <gi>orig</gi>, and <gi>reg</gi> needs to be employed.</p>
  </remarks>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes for usage within word-level elements in the analysis module and within lexicographic microstructure in the dictionaries module.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes/>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">normalized</gloss>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko"> 표준화</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">normalizado</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">normalisé</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">normalizzato</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2018-03-17" xml:lang="en">provides the normalized/standardized form of information present in the source text in a non-normalized form.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">비표준형으로 원본 텍스트에서 제시된 정보의 표준형을 제시한다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一規格化形式的資訊，其來源文件為非規格化形式</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストを、正規形を示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">donne une forme normalisée de l'information fournie par le texte source sous une forme non normalisée.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proprorciona de manera normalizada información dada en el texto fuente de manera no normalizada</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce la forma normalizzata delle informazioni contenute nel testo di origine in forma non normalizzata.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <p>Normalization of part-of-speech information within a dictionary entry.</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-gi">
          <gramGrp>
            <pos norm="noun">n</pos>
          </gramGrp>
        </egXML>
      </exemplum>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-lk" source="#fr-ex-Grand-Robert">
          <gramGrp>
            <pos norm="nom">n.</pos>
          </gramGrp>
        </egXML>
      </exemplum>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
        <p>Normalization of a source form in a tokenized historical corpus.</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-pk">
          <s xmlns="">
            <w>for</w>
            <w norm="virtue's">vertues</w>
          <w>sake</w></s>
        </egXML>
      </exemplum>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-wd">
          <s xmlns="">
            <w norm="persuasion">perswasion</w>
            <w>of</w>
            <w norm="Unity">Vnitie</w>
          </s>
        </egXML>
      </exemplum>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
        <p>Example of normalization from <ref target="http://www.deutschestextarchiv.de/anonym_aviso_1609/258">Aviso. Relation oder Zeitung. Wolfenbüttel, 1609. In: Deutsches Textarchiv</ref>.</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-xl">
          <s xmlns="">
            <w norm="freiwillig">freywillig</w>
            <pc norm="," join="left">/</pc>
            <w norm="unbedrängt">vnbedraͤngt</w>
            <w norm="und">vnd</w>
            <w norm="unverhindert">vnuerhindert</w>
          </s>
        </egXML>
      </exemplum>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-xv">
          <w xmlns="" norm="Teil">Theyll</w>
        </egXML>
      </exemplum>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-le">
          <w xmlns="" norm="Freude">Frewde</w>
        </egXML>
      </exemplum>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">original</gloss>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">원본</gloss>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">originale</gloss>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">gives the original string or is the empty string when the element does not appear in the source text.</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원본 문자열을 제시하거나 요소가 원본텍스트에 나타나지 않을 때는 공백 문자열을 제시한다.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">indique la chaîne originale ou contient une chaîne vide si l'élément n'apparaît pas dans le texte source.</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">當該元素未出現於來源文件中，提供其原文字串或空白字串。</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">元の文字列を示す。当該要素が元資料に無い場合には空になる。</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">da la serie original o la serie vacía cuando el elemento no aparece en el texto fuente</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce la stringa originale o la srtinga vuota quando l'elemento non compare nel testo di origine.</desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[2]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <p>Example from a language documentation project of the Mixtepec-Mixtec language (ISO 639-3:
        'mix'). This is a use case where speakers spell something incorrectly but we would
        like to preserve it for any number of reasons, the use of <att>orig</att> is essential and could
        have uses for both the speaker to see past mistakes, researchers to get insight into how
        untrained speakers write their language instinctually (in contrast to prescribed
        convention), etc.:</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-qs">
          <w orig="ntsa sia'i">ntsasia'i</w>
        </egXML>
      </exemplum>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[2]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
        <p>Example from the <ref target="https://earlyprint.org">EarlyPrint</ref> project. Fragment
        of text where obvious errors have been corrected but the original forms remain
        recorded:</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-ah">
          <w lemma="he" pos="pns" xml:id="b1afj-003-a-0950">he</w>
          <w lemma="have" pos="vvz" xml:id="b1afj-003-a-0960">hath</w>
          <w lemma="bring" pos="vvn" xml:id="b1afj-003-a-0970">brought</w>
          <w lemma="forth" pos="av" xml:id="b1afj-003-a-0980" orig="sorth">forth</w>
        </egXML>
      </exemplum>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[2]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
        <p>An example from the EarlyPrint project showing the use of both <att>norm</att> and <att>orig</att>. The <att>orig</att> attribute preserves the original version (sometimes with spelling errors, often with printer abbreviations), the element content resolves printer abbreviations but retains the original orthography, and the <att>norm</att> attribute holds normalized values:</p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATTNORM-egXML-sb">
          <w lemma="commandment" pos="n1" norm="commandment" xml:id="b9avr-018-a-7720" orig="commandemēt">commandement</w>
        </egXML>
      </exemplum>
```

^b36

### Block 37

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.lexicographic.normalized-remarks" versionDate="2020-02-12" xml:lang="en">
    <p>It needs to be stressed that the two attributes in this class are meant for strictly
    lexicographic and linguistic uses, and not for editorial interventions. For the latter, the
    mechanism based on <gi>choice</gi>, <gi>orig</gi>, and <gi>reg</gi> needs to be employed.</p>
  </remarks>
```

^b37

