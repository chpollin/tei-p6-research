---
type: representation
source-type: document
source: '[[00_sources/tei-p5-superentry-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 superEntry
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/superEntry.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# superEntry

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4890. Git blob: `bc911d43bed2cc8b77c8bd98f8579b4cb8820321`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" ident="superEntry" xml:id="gi-superEntry" validUntil="2027-03-07">
  <desc xml:lang="en" type="deprecationInfo" versionDate="2024-03-07">Because an <gi>entry</gi> can now occur inside an <gi>entry</gi>, the <gi>superEntry</gi> element is no longer needed. For instances where the <gi>superEntry</gi> element was used to group multiple <gi>entry</gi> elements, these Guidelines recommend using instead an outer <gi>entry</gi> element, perhaps with a <att>type</att> attribute.</desc>
  <gloss versionDate="2020-12-20" xml:lang="en">super entry</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">groupe d'entrées</gloss>
  <desc versionDate="2011-04-29" xml:lang="en">groups a sequence of entries within any kind of lexical resource, such as a dictionary or lexicon which function as a single unit, for example a set of homographs.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">동형이의어 집합의 연속된 표제 항목을 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集一組同形異義字的連續辭條。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">同形異義語の集合にある、一連の項目をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des entrées successives pour un ensemble d'homographes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa las entradas sucesivas para una serie de homógrafos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa voci successive per una serie di omografi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.entryLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.entryLike"/>
    <memberOf key="model.entryPart"/>
  </classes>
  <content>
    <alternate>
      <sequence>
        <elementRef key="form" minOccurs="0"/>
        <elementRef key="entry" minOccurs="1" maxOccurs="unbounded"/>
      </sequence>
      <elementRef key="dictScrap"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-superEntry-egXML-kf">
      <superEntry>
        <form>
          <orth>abandon</orth>
          <hyph>a|ban|don</hyph>
          <pron>@"band@n</pron>
        </form>
        <entry n="1">
          <gramGrp>
            <pos>v</pos>
            <subc>T1</subc>
          </gramGrp>
          <sense n="1">
            <def>to leave completely and for ever ... </def>
          </sense>
          <sense n="2"/>
        </entry>
        <entry n="2">
          <gramGrp>
            <pos>n</pos>
            <subc>U</subc>
          </gramGrp>
          <def>the state when one's feelings and actions are uncontrolled; freedom from
                        control</def>
        </entry>
      </superEntry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-superEntry-egXML-gv" source="#fr-ex-Grand-Robert">
      <superEntry>
        <form>
          <orth>homme</orth>
          <hyph>hom|me</hyph>
          <pron>óm</pron>
        </form>
        <entry n="1">
          <gramGrp>
            <pos>n.</pos>
          </gramGrp>
          <sense n="1">
            <def>Etre appartenant à l'espèce animale la plus évoluée de la Terre</def>
          </sense>
          <sense n="2"/>
        </entry>
        <entry n="2">
          <gramGrp>
            <pos>n.</pos>
          </gramGrp>
          <def>Etre humain mâle et (le plus souvent) adulte.</def>
        </entry>
      </superEntry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-superEntry-egXML-ql">
      <superEntry>
        <form>
          <orth>弼</orth>
          <hyph> (因漢字無法以連字符號拆解，故不提供範例。)</hyph>
          <pron>bi4</pron>
        </form>
        <entry n="1">
          <gramGrp>
            <pos>動詞</pos>
            <subc>及物</subc>
          </gramGrp>
          <sense n="1">
            <def>輔助；矯正過失</def>
          </sense>
          <sense n="2"/>
        </entry>
        <entry n="2">
          <gramGrp>
            <pos>名詞</pos>
            <subc>可數</subc>
          </gramGrp>
          <def>古時矯正弓的器具</def>
        </entry>
      </superEntry>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DIBO"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc xml:lang="en" type="deprecationInfo" versionDate="2024-03-07">Because an <gi>entry</gi> can now occur inside an <gi>entry</gi>, the <gi>superEntry</gi> element is no longer needed. For instances where the <gi>superEntry</gi> element was used to group multiple <gi>entry</gi> elements, these Guidelines recommend using instead an outer <gi>entry</gi> element, perhaps with a <att>type</att> attribute.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">super entry</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">groupe d'entrées</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2011-04-29" xml:lang="en">groups a sequence of entries within any kind of lexical resource, such as a dictionary or lexicon which function as a single unit, for example a set of homographs.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">동형이의어 집합의 연속된 표제 항목을 모아 놓는다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集一組同形異義字的連續辭條。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">同形異義語の集合にある、一連の項目をまとめる。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des entrées successives pour un ensemble d'homographes.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa las entradas sucesivas para una serie de homógrafos.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa voci successive per una serie di omografi.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.entryLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.entryLike"/>
    <memberOf key="model.entryPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <sequence>
        <elementRef key="form" minOccurs="0"/>
        <elementRef key="entry" minOccurs="1" maxOccurs="unbounded"/>
      </sequence>
      <elementRef key="dictScrap"/>
    </alternate>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-superEntry-egXML-kf">
      <superEntry>
        <form>
          <orth>abandon</orth>
          <hyph>a|ban|don</hyph>
          <pron>@"band@n</pron>
        </form>
        <entry n="1">
          <gramGrp>
            <pos>v</pos>
            <subc>T1</subc>
          </gramGrp>
          <sense n="1">
            <def>to leave completely and for ever ... </def>
          </sense>
          <sense n="2"/>
        </entry>
        <entry n="2">
          <gramGrp>
            <pos>n</pos>
            <subc>U</subc>
          </gramGrp>
          <def>the state when one's feelings and actions are uncontrolled; freedom from
                        control</def>
        </entry>
      </superEntry>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-superEntry-egXML-gv" source="#fr-ex-Grand-Robert">
      <superEntry>
        <form>
          <orth>homme</orth>
          <hyph>hom|me</hyph>
          <pron>óm</pron>
        </form>
        <entry n="1">
          <gramGrp>
            <pos>n.</pos>
          </gramGrp>
          <sense n="1">
            <def>Etre appartenant à l'espèce animale la plus évoluée de la Terre</def>
          </sense>
          <sense n="2"/>
        </entry>
        <entry n="2">
          <gramGrp>
            <pos>n.</pos>
          </gramGrp>
          <def>Etre humain mâle et (le plus souvent) adulte.</def>
        </entry>
      </superEntry>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-superEntry-egXML-ql">
      <superEntry>
        <form>
          <orth>弼</orth>
          <hyph> (因漢字無法以連字符號拆解，故不提供範例。)</hyph>
          <pron>bi4</pron>
        </form>
        <entry n="1">
          <gramGrp>
            <pos>動詞</pos>
            <subc>及物</subc>
          </gramGrp>
          <sense n="1">
            <def>輔助；矯正過失</def>
          </sense>
          <sense n="2"/>
        </entry>
        <entry n="2">
          <gramGrp>
            <pos>名詞</pos>
            <subc>可數</subc>
          </gramGrp>
          <def>古時矯正弓的器具</def>
        </entry>
      </superEntry>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIBO"/>
  </listRef>
```

^b16

