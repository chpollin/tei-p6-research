---
type: representation
source-type: document
source: '[[00_sources/tei-p5-mentioned-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 mentioned
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/mentioned.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# mentioned

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3095. Git blob: `c4710d0e979d14edb504256dc81aa5b9c0708a01`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-mentioned" ident="mentioned">
  <gloss versionDate="2005-01-14" xml:lang="en"/>
  <gloss versionDate="2009-01-06" xml:lang="fr">mentionné</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">指涉</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">marks words or phrases mentioned, not used.</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">marque des mots ou des expressions employés métalinguistiquement.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">marca palabras o locuciones mencionadas, no usadas.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標誌被提到的但意義上不被使用的字句。</desc>
  <desc versionDate="2007-01-21" xml:lang="it">codifica parole o sintagmi citati o riportati, non
        usati.</desc>
  <desc versionDate="2006-10-28" xml:lang="ja">言及された語句を示す。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.emphLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-mentioned-egXML-vb" source="#COHTG-eg-44">There is thus a
            striking accentual difference between a verbal form like <mentioned xml:id="X234" xml:lang="el">eluthemen</mentioned>
            <gloss target="#X234">we were released,</gloss> accented on the second syllable of the
            word, and its participial derivative <mentioned xml:id="X235" xml:lang="el">lutheis</mentioned>
            <gloss target="#X235">released,</gloss> accented on the last.</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-mentioned-egXML-ev" source="#fr-ex-simjar">Aucune ville ne répond mieux à
    l'expressioin <mentioned>sortie de terre</mentioned> que New York
    (ou faudrait-il plutôt dire  <mentioned>jaillie</mentioned>) :</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-mentioned-egXML-tn" source="#fr-ex-Manu_Shan"> L’harmonisation
        vocalique régressive empêche que <mentioned>agwêdê</mentioned> puisse être interprété comme
        un dérivé de <mentioned>gwada</mentioned>, qui pourtant est de même racine.</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-mentioned-egXML-pg"><mentioned xml:id="zh-tw_X234" xml:lang="zh-TW">憂鬱</mentioned>的鬱字很難寫。</egXML>
  </exemplum>
  <listRef>
    <ptr target="#COHQQ"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en"/>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">mentionné</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">指涉</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks words or phrases mentioned, not used.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">marque des mots ou des expressions employés métalinguistiquement.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">marca palabras o locuciones mencionadas, no usadas.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標誌被提到的但意義上不被使用的字句。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">codifica parole o sintagmi citati o riportati, non
        usati.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-28" xml:lang="ja">言及された語句を示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.emphLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-mentioned-egXML-vb" source="#COHTG-eg-44">There is thus a
            striking accentual difference between a verbal form like <mentioned xml:id="X234" xml:lang="el">eluthemen</mentioned>
            <gloss target="#X234">we were released,</gloss> accented on the second syllable of the
            word, and its participial derivative <mentioned xml:id="X235" xml:lang="el">lutheis</mentioned>
            <gloss target="#X235">released,</gloss> accented on the last.</egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-mentioned-egXML-ev" source="#fr-ex-simjar">Aucune ville ne répond mieux à
    l'expressioin <mentioned>sortie de terre</mentioned> que New York
    (ou faudrait-il plutôt dire  <mentioned>jaillie</mentioned>) :</egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-mentioned-egXML-tn" source="#fr-ex-Manu_Shan"> L’harmonisation
        vocalique régressive empêche que <mentioned>agwêdê</mentioned> puisse être interprété comme
        un dérivé de <mentioned>gwada</mentioned>, qui pourtant est de même racine.</egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-mentioned-egXML-pg"><mentioned xml:id="zh-tw_X234" xml:lang="zh-TW">憂鬱</mentioned>的鬱字很難寫。</egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQQ"/>
  </listRef>
```

^b16

