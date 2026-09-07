---
type: representation
source-type: document
source: '[[00_sources/tei-p5-objecttype-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 objectType
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/objectType.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# objectType

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2593. Git blob: `ccc4b0c607ab3edc0f819aeea4042b310e1fecd6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="OBJECTTYPE" ident="objectType">
  <gloss versionDate="2020-12-20" xml:lang="en">object type</gloss>
  <gloss versionDate="2011-01-10" xml:lang="fr">type d'objet</gloss>
  <desc versionDate="2013-06-22" xml:lang="en" xml:id="objectType.desc">contains a word or phrase describing the type of object being referred to.</desc>
  <desc versionDate="2011-01-10" xml:lang="fr">contient un mot ou une expression qui décrit le type de l'objet consideré.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <!--<!ELEMENT objectDesc  - -  (%phrase.seq;)>-->
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTTYPE-egXML-sk">
      <physDesc>
        <p>
      Paper and vellum <objectType>codex</objectType> in modern cloth binding.</p>
      </physDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTTYPE-egXML-ks">
      <physDesc>
        <p>Fragment of a re-used marble <objectType>funerary stele</objectType>.
    </p>
      </physDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2011-01-10" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTTYPE-egXML-tn">
      <physDesc>
        <p><objectType>Codex</objectType> avec feuilles de parchemin colorées avec la pourpre du murex.
    </p>
      </physDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2011-01-10" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTTYPE-egXML-vt">
      <physDesc>
        <p><objectType>Socle</objectType> fragmentaire d'Aphrodite Anadyomène en terre cuite.</p>
      </physDesc>
    </egXML>
  </exemplum>
  <remarks ident="objectType-remarks" versionDate="2011-01-12" xml:lang="en">
    <p>The <att>ref</att> attribute may be used to point to one
or more items within a taxonomy of types of object, defined either internally or
externally.</p>
  </remarks>
  <listRef>
    <ptr target="#msmat"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">object type</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2011-01-10" xml:lang="fr">type d'objet</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-06-22" xml:lang="en" xml:id="objectType.desc">contains a word or phrase describing the type of object being referred to.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2011-01-10" xml:lang="fr">contient un mot ou une expression qui décrit le type de l'objet consideré.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!--<!ELEMENT objectDesc  - -  (%phrase.seq;)>-->
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTTYPE-egXML-sk">
      <physDesc>
        <p>
      Paper and vellum <objectType>codex</objectType> in modern cloth binding.</p>
      </physDesc>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTTYPE-egXML-ks">
      <physDesc>
        <p>Fragment of a re-used marble <objectType>funerary stele</objectType>.
    </p>
      </physDesc>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2011-01-10" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTTYPE-egXML-tn">
      <physDesc>
        <p><objectType>Codex</objectType> avec feuilles de parchemin colorées avec la pourpre du murex.
    </p>
      </physDesc>
    </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2011-01-10" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTTYPE-egXML-vt">
      <physDesc>
        <p><objectType>Socle</objectType> fragmentaire d'Aphrodite Anadyomène en terre cuite.</p>
      </physDesc>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="objectType-remarks" versionDate="2011-01-12" xml:lang="en">
    <p>The <att>ref</att> attribute may be used to point to one
or more items within a taxonomy of types of object, defined either internally or
externally.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msmat"/>
  </listRef>
```

^b12

