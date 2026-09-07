---
type: representation
source-type: document
source: '[[00_sources/tei-p5-surplus-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 surplus
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/surplus.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# surplus

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2395. Git blob: `98591c1f55c745924483e7a5cfd20d29e30dacef`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-surplus" ident="surplus">
  <gloss versionDate="2007-06-12" xml:lang="en">surplus</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">Texte superflu</gloss>
  <desc versionDate="2009-11-06" xml:lang="en">marks text present in the source which the editor believes to be superfluous or redundant.</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">permet d'encoder une partie de texte présente dans la source lorsque l'éditeur la considère superflue ou redondante.</desc>
  <desc versionDate="2024-09-05" xml:lang="ja">編集者が無駄、もしくは、冗長だと考える原資料にあるテクストをマークする。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="reason" usage="opt">
      <desc versionDate="2013-12-06" xml:lang="en">one or more words indicating why this text is believed to be superfluous, e.g.
      <mentioned>repeated</mentioned>,
      <mentioned>interpolated</mentioned> etc.</desc>
      <desc versionDate="2009-11-16" xml:lang="fr">indique les raisons pour lesquelles on considère cette partie de texte comme superflue.</desc>
      <desc versionDate="2024-09-05" xml:lang="ja">このテキストが余分なものであると考えられる理由を示す1つ以上の単語。例えば<mentioned>repeated</mentioned>〔繰返し〕、<mentioned>interpolated</mentioned>〔衍字〕など。</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surplus-egXML-wv">I am dr Sr yrs
    <surplus reason="repeated">yrs</surplus>
    Sydney Smith</egXML>
  </exemplum>
  <listRef>
    <ptr target="#PHDA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">surplus</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">Texte superflu</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2009-11-06" xml:lang="en">marks text present in the source which the editor believes to be superfluous or redundant.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">permet d'encoder une partie de texte présente dans la source lorsque l'éditeur la considère superflue ou redondante.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2024-09-05" xml:lang="ja">編集者が無駄、もしくは、冗長だと考える原資料にあるテクストをマークする。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b6

### Block 7

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-06" xml:lang="en">one or more words indicating why this text is believed to be superfluous, e.g.
      <mentioned>repeated</mentioned>,
      <mentioned>interpolated</mentioned> etc.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">indique les raisons pour lesquelles on considère cette partie de texte comme superflue.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2024-09-05" xml:lang="ja">このテキストが余分なものであると考えられる理由を示す1つ以上の単語。例えば<mentioned>repeated</mentioned>〔繰返し〕、<mentioned>interpolated</mentioned>〔衍字〕など。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-surplus-egXML-wv">I am dr Sr yrs
    <surplus reason="repeated">yrs</surplus>
    Sydney Smith</egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHDA"/>
  </listRef>
```

^b13

