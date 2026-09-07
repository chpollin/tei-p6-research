---
type: representation
source-type: document
source: '[[00_sources/tei-p5-standoff-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 standOff
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/standOff.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# standOff

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5831. Git blob: `29c6c67319f75d668ff13472b9f83cc24ca57de2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="linking" xml:id="gi-standOff" ident="standOff">
  <desc xml:lang="en" versionDate="2018-10-31">functions as a container element for linked data, contextual information, and stand-off annotations embedded in a TEI document.</desc>
  <desc xml:lang="ja" versionDate="2023-07-29">リンクト・データや文脈情報、TEI文書に埋め込まれたスタンドオフ・アノテーションをコンテナ化する要素として機能する。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.resource"/>
  </classes>
  <content>
    <classRef key="model.standOffPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <exemplum versionDate="2019-12-25" xml:lang="en">
    <p>This example shows an encoding of morphosyntactic features similar to the encoding
    system used by <ref target="#ISO24611">ISO 24611 (MAF)</ref>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-standOff-egXML-uu" xml:lang="en" source="#MLK01" valid="feasible">
      <TEI>
        <teiHeader> <!-- ... --> </teiHeader>
        <text>
          <body>
            <!-- ... -->
            <p>
              <w xml:id="w51">I</w>
              <w xml:id="w52">wanna</w>
              <w xml:id="w53">put</w>
              <w xml:id="w54">up</w>
              <w xml:id="w55">new</w>
              <w xml:id="w56">wallpaper</w>
              <pc>.</pc>
            </p>
            <!-- ... -->
          </body>
        </text>
        <standOff type="morphosyntax">
          <spanGrp type="wordForm">
            <span target="#w51" ana="#fs01"/>
            <span target="#w52" ana="#fs02"/>
            <span target="#w52" ana="#fs03"/>
            <span target="#w53 #w54" ana="#fs04"/>
            <span target="#w55" ana="#fs05"/>
            <span target="#w56" ana="#fs06"/>
          </spanGrp>
          <fs xml:id="fs01">
            <f name="lemma"> <string>I</string> </f>
            <f name="pos"> <symbol value="PP"/> </f>
          </fs>
          <fs xml:id="fs02">
            <f name="lemma"> <string>want</string> </f>
            <f name="pos"> <symbol value="VBP"/> </f>
          </fs>
          <fs xml:id="fs03">
            <f name="lemma"> <string>to</string> </f>
            <f name="pos"> <symbol value="TO"/> </f>
          </fs>
          <fs xml:id="fs04">
            <f name="lemma"> <string>put up</string> </f>
            <f name="pos"> <symbol value="VB"/> </f>
          </fs>
          <fs xml:id="fs05">
            <f name="lemma"> <string>new</string> </f>
            <f name="pos"> <symbol value="JJ"/> </f>
          </fs>
          <fs xml:id="fs06">
            <f name="lemma"> <string>wallpaper</string> </f>
            <f name="pos"> <symbol value="NN"/> </f>
          </fs>
        </standOff>
      </TEI>
    </egXML>
  </exemplum>
  <exemplum versionDate="2019-12-28" xml:lang="en">
    <p>This example shows an encoding of contextual
    information which is referred to from the main text.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:lang="en" source="#MLK01" valid="feasible" xml:id="gi-standOff-egXML-kx">
      <TEI>
        <teiHeader> <!-- ... --> </teiHeader>
        <standOff>
          <listPlace>
            <place xml:id="LATL">
              <placeName>Atlanta</placeName>
              <location>
                <region key="US-GA">Georgia</region>
                <country key="USA">United States of America</country>
                <geo>33.755 -84.39</geo>
              </location>
              <population when="1963" type="interpolatedCensus" quantity="489359" source="https://www.biggestuscities.com/city/atlanta-georgia"/>
            </place>
            <place xml:id="LBHM">
              <placeName>Birmingham</placeName>
              <location>
                <region key="US-AL">Alabama</region>
                <country key="USA">United States of America</country>
                <geo>33.653333 -86.808889</geo>
              </location>
              <population when="1963" type="interpolatedCensus" quantity="332891" source="https://www.biggestuscities.com/city/birmingham-alabama"/>
            </place>
          </listPlace>
        </standOff>
        <text>
          <body>
            <!-- ... -->
            <p>Moreover, I am <choice><sic>congnizant</sic><corr>cognizant</corr></choice> of the interrelatedness of all communities and
            <lb/>states.  I cannot sit idly by in <placeName ref="#LATL">Atlanta</placeName> and not be concerned about what happens
            <lb/>in <placeName ref="#LBHM">Birmingham</placeName>.  <seg xml:id="FQ17">Injustice anywhere is a threat to justice everywhere.</seg>  We
            <lb/>are caught in an inescapable network of mutuality, tied in a single garment
            <lb/>of destiny.  Whatever affects one directly affects all indirectly. Never
            <lb/>again can we afford to live with the narrow, provincial <soCalled rendition="#Rqms">outside agitator</soCalled>
            <lb/>idea.  Anyone who lives inside the United States can never be considered
            <lb/>an outsider anywhere in this country.</p>
            <!-- ... -->
          </body>
        </text>
      </TEI>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#SASOstdf"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc xml:lang="en" versionDate="2018-10-31">functions as a container element for linked data, contextual information, and stand-off annotations embedded in a TEI document.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc xml:lang="ja" versionDate="2023-07-29">リンクト・データや文脈情報、TEI文書に埋め込まれたスタンドオフ・アノテーションをコンテナ化する要素として機能する。</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.resource"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.standOffPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2019-12-25" xml:lang="en">
    <p>This example shows an encoding of morphosyntactic features similar to the encoding
    system used by <ref target="#ISO24611">ISO 24611 (MAF)</ref>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-standOff-egXML-uu" xml:lang="en" source="#MLK01" valid="feasible">
      <TEI>
        <teiHeader> <!-- ... --> </teiHeader>
        <text>
          <body>
            <!-- ... -->
            <p>
              <w xml:id="w51">I</w>
              <w xml:id="w52">wanna</w>
              <w xml:id="w53">put</w>
              <w xml:id="w54">up</w>
              <w xml:id="w55">new</w>
              <w xml:id="w56">wallpaper</w>
              <pc>.</pc>
            </p>
            <!-- ... -->
          </body>
        </text>
        <standOff type="morphosyntax">
          <spanGrp type="wordForm">
            <span target="#w51" ana="#fs01"/>
            <span target="#w52" ana="#fs02"/>
            <span target="#w52" ana="#fs03"/>
            <span target="#w53 #w54" ana="#fs04"/>
            <span target="#w55" ana="#fs05"/>
            <span target="#w56" ana="#fs06"/>
          </spanGrp>
          <fs xml:id="fs01">
            <f name="lemma"> <string>I</string> </f>
            <f name="pos"> <symbol value="PP"/> </f>
          </fs>
          <fs xml:id="fs02">
            <f name="lemma"> <string>want</string> </f>
            <f name="pos"> <symbol value="VBP"/> </f>
          </fs>
          <fs xml:id="fs03">
            <f name="lemma"> <string>to</string> </f>
            <f name="pos"> <symbol value="TO"/> </f>
          </fs>
          <fs xml:id="fs04">
            <f name="lemma"> <string>put up</string> </f>
            <f name="pos"> <symbol value="VB"/> </f>
          </fs>
          <fs xml:id="fs05">
            <f name="lemma"> <string>new</string> </f>
            <f name="pos"> <symbol value="JJ"/> </f>
          </fs>
          <fs xml:id="fs06">
            <f name="lemma"> <string>wallpaper</string> </f>
            <f name="pos"> <symbol value="NN"/> </f>
          </fs>
        </standOff>
      </TEI>
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2019-12-28" xml:lang="en">
    <p>This example shows an encoding of contextual
    information which is referred to from the main text.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:lang="en" source="#MLK01" valid="feasible" xml:id="gi-standOff-egXML-kx">
      <TEI>
        <teiHeader> <!-- ... --> </teiHeader>
        <standOff>
          <listPlace>
            <place xml:id="LATL">
              <placeName>Atlanta</placeName>
              <location>
                <region key="US-GA">Georgia</region>
                <country key="USA">United States of America</country>
                <geo>33.755 -84.39</geo>
              </location>
              <population when="1963" type="interpolatedCensus" quantity="489359" source="https://www.biggestuscities.com/city/atlanta-georgia"/>
            </place>
            <place xml:id="LBHM">
              <placeName>Birmingham</placeName>
              <location>
                <region key="US-AL">Alabama</region>
                <country key="USA">United States of America</country>
                <geo>33.653333 -86.808889</geo>
              </location>
              <population when="1963" type="interpolatedCensus" quantity="332891" source="https://www.biggestuscities.com/city/birmingham-alabama"/>
            </place>
          </listPlace>
        </standOff>
        <text>
          <body>
            <!-- ... -->
            <p>Moreover, I am <choice><sic>congnizant</sic><corr>cognizant</corr></choice> of the interrelatedness of all communities and
            <lb/>states.  I cannot sit idly by in <placeName ref="#LATL">Atlanta</placeName> and not be concerned about what happens
            <lb/>in <placeName ref="#LBHM">Birmingham</placeName>.  <seg xml:id="FQ17">Injustice anywhere is a threat to justice everywhere.</seg>  We
            <lb/>are caught in an inescapable network of mutuality, tied in a single garment
            <lb/>of destiny.  Whatever affects one directly affects all indirectly. Never
            <lb/>again can we afford to live with the narrow, provincial <soCalled rendition="#Rqms">outside agitator</soCalled>
            <lb/>idea.  Anyone who lives inside the United States can never be considered
            <lb/>an outsider anywhere in this country.</p>
            <!-- ... -->
          </body>
        </text>
      </TEI>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SASOstdf"/>
  </listRef>
```

^b7

