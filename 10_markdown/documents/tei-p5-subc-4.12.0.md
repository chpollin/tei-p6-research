---
type: representation
source-type: document
source: '[[00_sources/tei-p5-subc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 subc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/subc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# subc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3190. Git blob: `d2623d7ce8128aa27cd4cc5f07f1408265664470`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-subc" ident="subc">
  <gloss versionDate="2005-01-14" xml:lang="en">subcategorization</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">하위범주화</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">次要分類</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">sous-catégorisation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">subcategorización</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">sottocategorizzazione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains subcategorization information (transitive/intransitive, countable/non-countable, etc.)</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하위범주화 정보를 포함한다(타동사/자동사, 가산/불가산, 등).</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含次要分類資訊 (及物 / 不及物、可數 / 不可數等)</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">下位範疇情報を示す。例えば、自動詞・他動詞、可算・非可算など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient des informations de sous-catégorie (transitif/intransitif, dénombrable/indénombrable, etc.)</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene información sobre la subcategorización (transitivo/intransitivo, contable/no contable, etc.)</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni circa la sottocategorizzazione (transitivo/intransitivo, numerabile/non numerabile, ecc.)</desc>
  <classes>
    <memberOf key="att.global"/>
    
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.lexicalRefinement"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subc-egXML-ux">
      <entry>
        <form>
          <orth>médire</orth>
        </form>
        <gramGrp>
          <subc>t ind</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subc-egXML-bj">
      <entry>
        <form>
          <orth>médire</orth>
        </form>
        <gramGrp>
          <subc>trans. ind.</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subc-egXML-sb">
      <entry>
        <form>
          <orth>cloth（布料）</orth>
        </form>
        <gramGrp>
          <subc>不可數</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DITPGR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">subcategorization</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">하위범주화</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">次要分類</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">sous-catégorisation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">subcategorización</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">sottocategorizzazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains subcategorization information (transitive/intransitive, countable/non-countable, etc.)</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하위범주화 정보를 포함한다(타동사/자동사, 가산/불가산, 등).</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含次要分類資訊 (及物 / 不及物、可數 / 不可數等)</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">下位範疇情報を示す。例えば、自動詞・他動詞、可算・非可算など。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient des informations de sous-catégorie (transitif/intransitif, dénombrable/indénombrable, etc.)</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene información sobre la subcategorización (transitivo/intransitivo, contable/no contable, etc.)</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni circa la sottocategorizzazione (transitivo/intransitivo, numerabile/non numerabile, ecc.)</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.lexicalRefinement"/>
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
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subc-egXML-ux">
      <entry>
        <form>
          <orth>médire</orth>
        </form>
        <gramGrp>
          <subc>t ind</subc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subc-egXML-bj">
      <entry>
        <form>
          <orth>médire</orth>
        </form>
        <gramGrp>
          <subc>trans. ind.</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subc-egXML-sb">
      <entry>
        <form>
          <orth>cloth（布料）</orth>
        </form>
        <gramGrp>
          <subc>不可數</subc>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPGR"/>
  </listRef>
```

^b19

