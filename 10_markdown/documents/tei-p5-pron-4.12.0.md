---
type: representation
source-type: document
source: '[[00_sources/tei-p5-pron-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 pron
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/pron.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# pron

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3624. Git blob: `c8bb1c4d02d1ce183b60994676e175386f119c45`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-pron" ident="pron">
  <gloss versionDate="2005-01-14" xml:lang="en">pronunciation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">발음</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">發音</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">prononciation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">pronunciación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">pronuncia</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the pronunciation(s) of the word.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">단어의 발음을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含該字的一種或多種發音方法。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該語の発音を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la/les prononciation(s) du mot.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la pronunciación de la palabra.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la pronuncia (le pronunicie) di una parola.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.partials"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.formPart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
 
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pron-egXML-tk">
      <entry>
        <form><orth>obverse</orth><pron>'äb-`ərs</pron>, 
<pron extent="pref">äb-`</pron>, <pron extent="pref">əb-`</pron></form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pron-egXML-os">
      <entry>
        <form>
          <orth>amygdale</orth>
          <pron extent="full">[ami(g)dal]</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pron-egXML-gk">
      <entry>
        <form>
          <orth>transcription</orth>
          <pron notation="IPA">trænskrɪpʃən</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pron-egXML-sx">
      <entry>
        <form>
          <orth>將</orth>
          <pron>jiang4</pron>
        </form>
        <gramGrp>
          <pos>名詞</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
<remarks ident="pron-remarks" versionDate="2013-12-09" xml:lang="en"><p>The values used to
specify the notation may be taken from any appropriate project-defined
list of values. Typical values might be <mentioned>IPA</mentioned>,
<mentioned>Murray</mentioned>, for example.</p></remarks>

  <listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">pronunciation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">발음</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">發音</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">prononciation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">pronunciación</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">pronuncia</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the pronunciation(s) of the word.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">단어의 발음을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含該字的一種或多種發音方法。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該語の発音を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la/les prononciation(s) du mot.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la pronunciación de la palabra.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la pronuncia (le pronunicie) di una parola.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.partials"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.formPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pron-egXML-tk">
      <entry>
        <form><orth>obverse</orth><pron>'äb-`ərs</pron>, 
<pron extent="pref">äb-`</pron>, <pron extent="pref">əb-`</pron></form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pron-egXML-os">
      <entry>
        <form>
          <orth>amygdale</orth>
          <pron extent="full">[ami(g)dal]</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pron-egXML-gk">
      <entry>
        <form>
          <orth>transcription</orth>
          <pron notation="IPA">trænskrɪpʃən</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pron-egXML-sx">
      <entry>
        <form>
          <orth>將</orth>
          <pron>jiang4</pron>
        </form>
        <gramGrp>
          <pos>名詞</pos>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="pron-remarks" versionDate="2013-12-09" xml:lang="en"><p>The values used to
specify the notation may be taken from any appropriate project-defined
list of values. Typical values might be <mentioned>IPA</mentioned>,
<mentioned>Murray</mentioned>, for example.</p></remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
```

^b21

