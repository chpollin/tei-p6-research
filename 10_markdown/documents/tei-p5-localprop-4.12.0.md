---
type: representation
source-type: document
source: '[[00_sources/tei-p5-localprop-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 localProp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/localProp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# localProp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2574. Git blob: `6fa60b947035e3a9c0f2393d3ec7759efef31ea2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="localProp" module="gaiji" xml:id="LOCALPROP">
    <gloss versionDate="2018-08-22" xml:lang="en">locally defined property</gloss>
    <desc versionDate="2020-01-28" xml:lang="en">provides a locally defined character (or glyph) property.</desc>
    <classes>
      <memberOf key="att.global"/>
      <memberOf key="att.gaijiProp"/>
    </classes>
    <content>
      <empty/>
    </content>
    <exemplum versionDate="2019-07-01" xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCALPROP-egXML-al">
            <char xml:id="daikanwaU4EBA">
                <localProp name="name" value="CIRCLED IDEOGRAPH 4EBA"/>
                <localProp name="entity" value="daikanwa"/>
                <unicodeProp name="Decomposition_Mapping" value="circle"/>
                <mapping type="standard">人</mapping>
            </char>
        </egXML>
    </exemplum>
    <remarks ident="localProp-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>No definitive list of local names is proposed. However, the name <val>entity</val> is recommended as a means of naming the property identifying the recommended
            character entity name for this character or glyph.</p>
    </remarks>
    <remarks ident="localProp-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Il n'est pas proposé de liste fermée de noms locaux de propriétés. Cependant, la dénomination <ident>entity</ident> (entité) est recommandée pour la propriété donnant le
            nom de l'entité caractère conseillée pour le caractère ou le glyphe en cours de description.</p>
    </remarks>
    <remarks ident="localProp-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> ローカル名のリストで勧告されているものはない。但し、文字やグリフを 表す文字エンティティを特定する際には、名前<ident>エンティティ </ident>を使い素性に名付けることは推奨されている。 </p>
    </remarks>
    <listRef>
        <ptr target="#ucsprops"/>
    </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2018-08-22" xml:lang="en">locally defined property</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-01-28" xml:lang="en">provides a locally defined character (or glyph) property.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
      <memberOf key="att.global"/>
      <memberOf key="att.gaijiProp"/>
    </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
      <empty/>
    </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2019-07-01" xml:lang="und">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="LOCALPROP-egXML-al">
            <char xml:id="daikanwaU4EBA">
                <localProp name="name" value="CIRCLED IDEOGRAPH 4EBA"/>
                <localProp name="entity" value="daikanwa"/>
                <unicodeProp name="Decomposition_Mapping" value="circle"/>
                <mapping type="standard">人</mapping>
            </char>
        </egXML>
    </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="localProp-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>No definitive list of local names is proposed. However, the name <val>entity</val> is recommended as a means of naming the property identifying the recommended
            character entity name for this character or glyph.</p>
    </remarks>
```

^b6

### Block 7

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="localProp-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Il n'est pas proposé de liste fermée de noms locaux de propriétés. Cependant, la dénomination <ident>entity</ident> (entité) est recommandée pour la propriété donnant le
            nom de l'entité caractère conseillée pour le caractère ou le glyphe en cours de description.</p>
    </remarks>
```

^b7

### Block 8

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="localProp-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> ローカル名のリストで勧告されているものはない。但し、文字やグリフを 表す文字エンティティを特定する際には、名前<ident>エンティティ </ident>を使い素性に名付けることは推奨されている。 </p>
    </remarks>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
        <ptr target="#ucsprops"/>
    </listRef>
```

^b9

