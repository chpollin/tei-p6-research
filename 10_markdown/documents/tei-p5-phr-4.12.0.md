---
type: representation
source-type: document
source: '[[00_sources/tei-p5-phr-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 phr
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/phr.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# phr

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3442. Git blob: `8001f1b2539a95ab65220c63ff29a27f17406616`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="analysis" xml:id="gi-phr" ident="phr">
  <gloss versionDate="2005-01-14" xml:lang="en">phrase</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">구</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">片語</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">syntagme</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">sintagma</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">sintagma</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents a grammatical phrase.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문법적 구를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個文法上的片語。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">文法上の句を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente un syntagme grammatical.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa un sintagma gramatical.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta il sintagma grammaticale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.segLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-phr-egXML-rr">
      <phr type="verb" function="extraposted_modifier">To talk 
        <phr type="preposition" function="complement">of 
          <phr type="noun" function="object">many things</phr>
            </phr>
         </phr>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-phr-egXML-vk">
      <phr type="verb" function="extraposted_modifier">To talk 
        <phr type="preposition" function="complement">of 
          <phr type="noun" function="object">many things</phr>
            </phr>
         </phr>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-phr-egXML-ey">
      <phr type="動詞" function="extraposted_modifier">談 <phr type="介係詞" function="補語">及<phr type="名詞" function="受詞">許多事物</phr>
            </phr>
         </phr>
    </egXML>
  </exemplum>
  <remarks ident="phr-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>The <att>type</att> attribute may be used to indicate the type of phrase, taking values such
      as <val>noun</val>, <val>verb</val>, <val>preposition</val>, etc. as appropriate.</p>
  </remarks>
  <remarks ident="phr-remarks" versionDate="2009-02-13" xml:lang="fr">
    <p>L'attribut <att>type</att> peut être utilisé pour indiquer le type de syntagme grammatical,
      avec des valeurs telles que <val>nom</val>, <val>verbe</val>, <val>préposition</val>, etc. selon le cas.</p>
  </remarks>
  <listRef>
    <ptr target="#AILC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">phrase</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">구</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">片語</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">syntagme</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">sintagma</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">sintagma</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents a grammatical phrase.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문법적 구를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個文法上的片語。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">文法上の句を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente un syntagme grammatical.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa un sintagma gramatical.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta il sintagma grammaticale.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.segLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.segLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-phr-egXML-rr">
      <phr type="verb" function="extraposted_modifier">To talk 
        <phr type="preposition" function="complement">of 
          <phr type="noun" function="object">many things</phr>
            </phr>
         </phr>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-phr-egXML-vk">
      <phr type="verb" function="extraposted_modifier">To talk 
        <phr type="preposition" function="complement">of 
          <phr type="noun" function="object">many things</phr>
            </phr>
         </phr>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-phr-egXML-ey">
      <phr type="動詞" function="extraposted_modifier">談 <phr type="介係詞" function="補語">及<phr type="名詞" function="受詞">許多事物</phr>
            </phr>
         </phr>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="phr-remarks" versionDate="2008-10-25" xml:lang="en">
    <p>The <att>type</att> attribute may be used to indicate the type of phrase, taking values such
      as <val>noun</val>, <val>verb</val>, <val>preposition</val>, etc. as appropriate.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="phr-remarks" versionDate="2009-02-13" xml:lang="fr">
    <p>L'attribut <att>type</att> peut être utilisé pour indiquer le type de syntagme grammatical,
      avec des valeurs telles que <val>nom</val>, <val>verbe</val>, <val>préposition</val>, etc. selon le cas.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#AILC"/>
  </listRef>
```

^b21

