---
type: representation
source-type: document
source: '[[00_sources/tei-p5-filiation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 filiation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/filiation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# filiation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6652. Git blob: `bd544f3feb9bdec2fe887e67bfce7a4557a9f1c9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="FILIATION" ident="filiation">
  <gloss versionDate="2007-06-12" xml:lang="en">filiation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">filiation</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="filiation.desc">contains information concerning the manuscript or other object's <term>filiation</term>, i.e. its relationship to other surviving manuscripts or other objects of the same text or contents, its <term>protographs</term>, <term>antigraphs</term> and <term>apographs</term>.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 <term>filiation</term>(내력)에 관한 정보를 포함한다, 즉, <term>protographs</term>, <term>antigraphs</term>, <term>apographs</term>과 같이 동일 텍스트에 대한 다른 잔존 원고의 관계.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿的<term>來歷</term>相關資訊，例如該手稿和其他相同文字內容的現存手稿之間的關係、以及該手稿的<term>原稿</term>、 <term>抄本</term>、以及<term>謄本</term>。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の<term>親子関係</term>、すなわち、同じテキストを持つ現存
  する手書き資料と、その<term>原本(protographs)</term>、
 <term>異本(antigraphs)</term>、<term>転写本(apographs)</term>との関係。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient les informations sur la
      <term>filiation</term> du manuscrit, c'est-à-dire sur ses relations avec d'autres manuscrits
      connus du même texte, ses <term>protographes</term>, <term>antigraphes</term> et
        <term>apographes</term>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene información referente a la filiación de un manuscrito, p.ej. su relación con otros manuscritos supervivientes del mismo texto, es decir, sus <term>protógrafos</term>, <term>antígrafos</term> y <term>apógrafos</term>.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative alla <term>filiazione</term> del manoscritto, cioè la sua relazione con altri manoscritti sopravvissuti per lo stesso testo, cioè i suoi <term>protografi</term>, <term>antigrafi</term> e <term>apografi</term></desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.msItemPart"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FILIATION-egXML-on">
      <msContents>
        <msItem>
          <title>Beljakovski sbornik</title>
          <filiation type="protograph">Bulgarian</filiation>
          <filiation type="antigraph">Middle Bulgarian</filiation>
          <filiation type="apograph">
            <ref target="#DN17">Dujchev N 17</ref>
          </filiation>
        </msItem>
      </msContents>
      <!-- ... -->
      <msDesc xml:id="DN17">
        <msIdentifier>
          <settlement>Faraway</settlement>
        </msIdentifier>
        <!-- ... -->
      </msDesc>
    </egXML>
    <p>In this example, the reference to <q>Dujchev N17</q> includes a
link to some other manuscript description which has the identifier <code>DN17</code>. </p>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FILIATION-egXML-sn">
      <msContents>
        <msItem>
          <title>元豐類稿</title>
          <filiation type="protograph">元大德八年丁思敬南豐刊本</filiation>
          <filiation type="antigraph">王文進《文祿堂訪書記》</filiation>
          <filiation type="apograph">清內府《天祿琳琅書目》
          <ref target="#zh-tw_DN17"/>
               </filiation>
        </msItem>
      </msContents>
      <!-- ... -->
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FILIATION-egXML-lr" source="#biblzh-tw_n41">
      <msItem>
        <title>明藏</title>
        <filiation>
          <p>明藏有四︰在南京刻的稱南藏，在北京刻的稱北藏，在浙江武林刻的稱武林藏，在徑山等處刻過的稱徑山或嘉興藏。徑山藏，是會合南北藏本而以北本為主的；日本的黃檗藏就是徑山藏的翻刻本，而卍字藏復淵源于黃檗藏，可見徑山藏給與日本的影響了。</p>
          <p>明藏因年代較近，國內外還有完整的存本；惟武林藏本，卻已全佚，其特點是始改梵夾為方冊。</p>
        </filiation>
      </msItem>
      <!--http://www.cbeta.org/data/budadata/hisutra.htm-->
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FILIATION-egXML-fr">
      <msItem>
        <title>Guan-ben</title>
        <filiation>
          <p>The "Guan-ben" was widely current among mathematicians in the
    Qing dynasty, and "Zhao Qimei version" was also read.  It is
    therefore difficult to know the correct filiation path to follow.
    The study of this era is much indebted to Li Di.  We explain the
    outline of his conclusion here.  Kong Guangsen 
    (1752-1786)(17) was from the same town as Dai Zhen, so he obtained
    "Guan-ben" from him and studied it(18).  Li Huang  (d. 1811)
    (19) took part in editing Si Ku Quan Shu, so he must have had
    "Guan-ben".  Then Zhang Dunren (1754-1834) obtained this version,
    and studied "Da Yan Zong Shu Shu" (The General Dayan
    Computation).  He wrote Jiu Yi Suan Shu (Mathematics
    Searching for One, 1803) based on this version of Shu Xue Jiu
    Zhang (20).</p>
          <p>One of the most important persons in restoring our knowledge
   concerning the filiation of these books was Li Rui (1768(21)
   -1817)(see his biography).  ... only two volumes remain of this
    manuscript, as far as chapter 6 (chapter 3 part 2) p.13, that is,
    question 2 of "Huan Tian San Ji" (square of three loops),
    which later has been lost.</p>
        </filiation>
      </msItem>
      <!--http://www2.nkfust.edu.tw/~jochi/ed1.htm-->
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mscoit"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">filiation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">filiation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="filiation.desc">contains information concerning the manuscript or other object's <term>filiation</term>, i.e. its relationship to other surviving manuscripts or other objects of the same text or contents, its <term>protographs</term>, <term>antigraphs</term> and <term>apographs</term>.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 <term>filiation</term>(내력)에 관한 정보를 포함한다, 즉, <term>protographs</term>, <term>antigraphs</term>, <term>apographs</term>과 같이 동일 텍스트에 대한 다른 잔존 원고의 관계.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿的<term>來歷</term>相關資訊，例如該手稿和其他相同文字內容的現存手稿之間的關係、以及該手稿的<term>原稿</term>、 <term>抄本</term>、以及<term>謄本</term>。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の<term>親子関係</term>、すなわち、同じテキストを持つ現存
  する手書き資料と、その<term>原本(protographs)</term>、
 <term>異本(antigraphs)</term>、<term>転写本(apographs)</term>との関係。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient les informations sur la
      <term>filiation</term> du manuscrit, c'est-à-dire sur ses relations avec d'autres manuscrits
      connus du même texte, ses <term>protographes</term>, <term>antigraphes</term> et
        <term>apographes</term>.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene información referente a la filiación de un manuscrito, p.ej. su relación con otros manuscritos supervivientes del mismo texto, es decir, sus <term>protógrafos</term>, <term>antígrafos</term> y <term>apógrafos</term>.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative alla <term>filiazione</term> del manoscritto, cioè la sua relazione con altri manoscritti sopravvissuti per lo stesso testo, cioè i suoi <term>protografi</term>, <term>antigrafi</term> e <term>apografi</term></desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.msItemPart"/>
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

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FILIATION-egXML-on">
      <msContents>
        <msItem>
          <title>Beljakovski sbornik</title>
          <filiation type="protograph">Bulgarian</filiation>
          <filiation type="antigraph">Middle Bulgarian</filiation>
          <filiation type="apograph">
            <ref target="#DN17">Dujchev N 17</ref>
          </filiation>
        </msItem>
      </msContents>
      <!-- ... -->
      <msDesc xml:id="DN17">
        <msIdentifier>
          <settlement>Faraway</settlement>
        </msIdentifier>
        <!-- ... -->
      </msDesc>
    </egXML>
    <p>In this example, the reference to <q>Dujchev N17</q> includes a
link to some other manuscript description which has the identifier <code>DN17</code>. </p>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FILIATION-egXML-sn">
      <msContents>
        <msItem>
          <title>元豐類稿</title>
          <filiation type="protograph">元大德八年丁思敬南豐刊本</filiation>
          <filiation type="antigraph">王文進《文祿堂訪書記》</filiation>
          <filiation type="apograph">清內府《天祿琳琅書目》
          <ref target="#zh-tw_DN17"/>
               </filiation>
        </msItem>
      </msContents>
      <!-- ... -->
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FILIATION-egXML-lr" source="#biblzh-tw_n41">
      <msItem>
        <title>明藏</title>
        <filiation>
          <p>明藏有四︰在南京刻的稱南藏，在北京刻的稱北藏，在浙江武林刻的稱武林藏，在徑山等處刻過的稱徑山或嘉興藏。徑山藏，是會合南北藏本而以北本為主的；日本的黃檗藏就是徑山藏的翻刻本，而卍字藏復淵源于黃檗藏，可見徑山藏給與日本的影響了。</p>
          <p>明藏因年代較近，國內外還有完整的存本；惟武林藏本，卻已全佚，其特點是始改梵夾為方冊。</p>
        </filiation>
      </msItem>
      <!--http://www.cbeta.org/data/budadata/hisutra.htm-->
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="FILIATION-egXML-fr">
      <msItem>
        <title>Guan-ben</title>
        <filiation>
          <p>The "Guan-ben" was widely current among mathematicians in the
    Qing dynasty, and "Zhao Qimei version" was also read.  It is
    therefore difficult to know the correct filiation path to follow.
    The study of this era is much indebted to Li Di.  We explain the
    outline of his conclusion here.  Kong Guangsen 
    (1752-1786)(17) was from the same town as Dai Zhen, so he obtained
    "Guan-ben" from him and studied it(18).  Li Huang  (d. 1811)
    (19) took part in editing Si Ku Quan Shu, so he must have had
    "Guan-ben".  Then Zhang Dunren (1754-1834) obtained this version,
    and studied "Da Yan Zong Shu Shu" (The General Dayan
    Computation).  He wrote Jiu Yi Suan Shu (Mathematics
    Searching for One, 1803) based on this version of Shu Xue Jiu
    Zhang (20).</p>
          <p>One of the most important persons in restoring our knowledge
   concerning the filiation of these books was Li Rui (1768(21)
   -1817)(see his biography).  ... only two volumes remain of this
    manuscript, as far as chapter 6 (chapter 3 part 2) p.13, that is,
    question 2 of "Huan Tian San Ji" (square of three loops),
    which later has been lost.</p>
        </filiation>
      </msItem>
      <!--http://www2.nkfust.edu.tw/~jochi/ed1.htm-->
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mscoit"/>
  </listRef>
```

^b16

