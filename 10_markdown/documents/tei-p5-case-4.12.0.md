---
type: representation
source-type: document
source: '[[00_sources/tei-p5-case-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 case
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/case.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# case

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5561. Git blob: `f5cc61eb53106d3ebfdd6e0e8a0c8b3c57821273`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-case" ident="case">
  <gloss versionDate="2007-06-12" xml:lang="en">case</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">cas</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">Fall</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains grammatical case information given by a dictionary for a given form.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">주어진 형식에 대하여 사전에 제시된 문법적 격 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文法上格的資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書中における格情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur le cas grammatical présenté par le dictionnaire pour une forme donnée.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la información del caso gramatical.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni grammaticali sul caso fornite dal dizionario per una determinata froma.</desc>
  <desc versionDate="2024-04-11" xml:lang="de">enthält grammatikalische Kasusinformationen, die von einem Wörterbuch für eine bestimmte Form geliefert werden.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.morphLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <p>Taken from <bibl><title>Wörterbuch der Deutschen Sprache.</title><title> Veranstaltet und herausgegeben von
          Joachim Heinrich Campe. Erster Theil. A - bis - E.</title> (Braunschweig 1807. In der
        Schulbuchhandlung)</bibl>: <q rend="display">Das Evangelium, des Evangelii, ... </q>
      </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-case-egXML-ig">
      <entry>
        <form type="lemma">
          <gramGrp>
            <pos value="noun"/>
            <gen value="n"/>
          </gramGrp>
          <form type="determiner">
            <orth>Das</orth>
          </form>
          <form type="headword"><orth>Evangelium</orth>,</form>
        </form>
        <form type="inflected">
          <gramGrp>
            <case value="genitive"/>
            <number value="singular"/>
          </gramGrp>
          <form type="determiner">
            <orth>des</orth>
          </form>
          <form type="headword">
            <orth><oRef>Evangelii</oRef>,</orth>
          </form>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-case-egXML-zr" source="#fr-ex-Campe">
      <q rend="display">Das Evangelium, des Evangelii, ...</q>
      <entry>
        <form type="lemma">
          <gramGrp>
            <pos value="noun"/>
            <gen value="n"/>
          </gramGrp>
          <form type="determiner">
            <orth>Das</orth>
          </form>
          <form type="headword"><orth>Evangelium</orth>,</form>
        </form>
        <form type="inflected">
          <gramGrp>
            <case value="genitiv"/>
            <number value="singular"/>
          </gramGrp>
          <form type="determiner">
            <orth>des</orth>
          </form>
          <form type="headword">
            <orth><oRef>Evangelii</oRef>,</orth>
          </form>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-case-egXML-wf">
       因中文無「格」的現象，故不提供範例。 
    </egXML>
  </exemplum>
  <remarks ident="case-remarks" versionDate="2008-02-01" xml:lang="en">
    <p rend="dataDesc">May contain character data and phrase-level elements. Typical values will be
      of the form <mentioned>nominative</mentioned>, <mentioned>accusative</mentioned>,
        <mentioned>dative</mentioned>, <mentioned>genitive</mentioned>, etc.</p>
    <p>This element is synonymous with <tag>gram type="case"</tag>.</p>
  </remarks>
  <remarks ident="case-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères et des éléments du niveau expression.
                Les valeurs types seront <mentioned> nominative</mentioned>,
                <mentioned>accusative</mentioned>, <mentioned>dative</mentioned>,
                    <mentioned>genitive</mentioned>, etc.</p>
    <p>Cet élément est synonyme de<tag>gram type="case"</tag>
            </p>
  </remarks>
  <remarks ident="case-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    文字データまたは句レベルの要素。典型的な値は、
      <mentioned>nominative(主格)</mentioned>、<mentioned>accusative(対格)</mentioned>、<mentioned>dative(与格)</mentioned>、<mentioned>genitive(属格)
    </mentioned>など。
    </p>
    <p>
    当該要素は、要素<tag>gram type="case"</tag>と同義である。
    </p>
  </remarks>
  <listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">case</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">cas</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">Fall</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains grammatical case information given by a dictionary for a given form.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">주어진 형식에 대하여 사전에 제시된 문법적 격 정보를 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文法上格的資訊。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書中における格情報を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur le cas grammatical présenté par le dictionnaire pour une forme donnée.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la información del caso gramatical.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni grammaticali sul caso fornite dal dizionario per una determinata froma.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2024-04-11" xml:lang="de">enthält grammatikalische Kasusinformationen, die von einem Wörterbuch für eine bestimmte Form geliefert werden.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.morphLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>Taken from <bibl><title>Wörterbuch der Deutschen Sprache.</title><title> Veranstaltet und herausgegeben von
          Joachim Heinrich Campe. Erster Theil. A - bis - E.</title> (Braunschweig 1807. In der
        Schulbuchhandlung)</bibl>: <q rend="display">Das Evangelium, des Evangelii, ... </q>
      </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-case-egXML-ig">
      <entry>
        <form type="lemma">
          <gramGrp>
            <pos value="noun"/>
            <gen value="n"/>
          </gramGrp>
          <form type="determiner">
            <orth>Das</orth>
          </form>
          <form type="headword"><orth>Evangelium</orth>,</form>
        </form>
        <form type="inflected">
          <gramGrp>
            <case value="genitive"/>
            <number value="singular"/>
          </gramGrp>
          <form type="determiner">
            <orth>des</orth>
          </form>
          <form type="headword">
            <orth><oRef>Evangelii</oRef>,</orth>
          </form>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-case-egXML-zr" source="#fr-ex-Campe">
      <q rend="display">Das Evangelium, des Evangelii, ...</q>
      <entry>
        <form type="lemma">
          <gramGrp>
            <pos value="noun"/>
            <gen value="n"/>
          </gramGrp>
          <form type="determiner">
            <orth>Das</orth>
          </form>
          <form type="headword"><orth>Evangelium</orth>,</form>
        </form>
        <form type="inflected">
          <gramGrp>
            <case value="genitiv"/>
            <number value="singular"/>
          </gramGrp>
          <form type="determiner">
            <orth>des</orth>
          </form>
          <form type="headword">
            <orth><oRef>Evangelii</oRef>,</orth>
          </form>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-case-egXML-wf">
       因中文無「格」的現象，故不提供範例。 
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="case-remarks" versionDate="2008-02-01" xml:lang="en">
    <p rend="dataDesc">May contain character data and phrase-level elements. Typical values will be
      of the form <mentioned>nominative</mentioned>, <mentioned>accusative</mentioned>,
        <mentioned>dative</mentioned>, <mentioned>genitive</mentioned>, etc.</p>
    <p>This element is synonymous with <tag>gram type="case"</tag>.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="case-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères et des éléments du niveau expression.
                Les valeurs types seront <mentioned> nominative</mentioned>,
                <mentioned>accusative</mentioned>, <mentioned>dative</mentioned>,
                    <mentioned>genitive</mentioned>, etc.</p>
    <p>Cet élément est synonyme de<tag>gram type="case"</tag>
            </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="case-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    文字データまたは句レベルの要素。典型的な値は、
      <mentioned>nominative(主格)</mentioned>、<mentioned>accusative(対格)</mentioned>、<mentioned>dative(与格)</mentioned>、<mentioned>genitive(属格)
    </mentioned>など。
    </p>
    <p>
    当該要素は、要素<tag>gram type="case"</tag>と同義である。
    </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
```

^b20

