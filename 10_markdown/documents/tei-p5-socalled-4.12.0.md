---
type: representation
source-type: document
source: '[[00_sources/tei-p5-socalled-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 soCalled
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/soCalled.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# soCalled

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3947. Git blob: `7f57f5d044507f308544c6140958d2ee462fa0ec`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-soCalled" ident="soCalled">
  <gloss versionDate="2020-12-20" xml:lang="en">so called</gloss>
  <gloss versionDate="2026-03-26" xml:lang="de">sogenannt</gloss>
  <gloss versionDate="2026-03-26" xml:lang="it">cosiddetto</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a word or phrase for which the author or narrator indicates a disclaiming of
    responsibility, for example by the use of scare quotes or italics.</desc>
  <desc versionDate="2026-03-26" xml:lang="de">enthält ein Wort oder eine Phrase, für die der Autor oder Erzähler einen Haftungsausschluss anzeigt,
    zum Beispiel durch den Einsatz von Anführungszeichen oder Kursivschrift.</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une expression ou un mot pour lesquels l'auteur
    ou le narrateur renonce à toute responsabilité, par exemple en utilisant de l'italique ou des
    guillemets.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una palabra o frase de la que el autor o
    narrador declina la responsabilidad, p.ej. mediante el uso de comillas o cursiva.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">作者或敘述者使用的字句在意義上另有所指的表現，例如：諷刺所使用的引號或斜體標示。</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una parola o sintagma per cui l'autore o il
    narratore non assume la responsabilità intelletuale, segnalati ad esempio tramite l'uso di
    virgolette o corsivi.</desc>
  <desc versionDate="2006-10-28" xml:lang="ja">著者や語り手が、責任を持ちたくない語句を示す。例えば、英語
    文化圏では、引用符号で囲んだり、イタリック体で示される部分。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.emphLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-soCalled-egXML-kb" source="#COHQHE-eg-14">To edge his way along
      the crowded paths of life, warning all human sympathy to keep its distance, was what the
      knowing ones call <soCalled>nuts</soCalled> to Scrooge.</egXML>
    <!-- C.Dickens, Xmas Carol, 1843, p5 -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-soCalled-egXML-vm" source="#fr-ex-Pennac_Marchande">- On ne
        bouge pas, on ne touche à rien, il faut que je prévienne <soCalled>la Maison</soCalled>.
        C'est ainsi qu'il appelait le Quai des Orfèvres. </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-soCalled-egXML-jb" source="#fr-ex-Hugo-miserables">
      <p> Mais, après tout, les propos auxquels on mêlait son nom n'étaient que des propos ; du
          bruit, des mots, des paroles, moins que des paroles, des<soCalled>palabres</soCalled>,
          comme dit l'énergique langue du midi.</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-soCalled-egXML-lq" source="#biblzh-tw_n22">
        眾猴听說，即拱伏無違。一個個序齒排班，朝上禮拜，都稱千歲大王。自此，石猴高登王位，將石字儿隱了，遂稱<soCalled>美猴王</soCalled>。</egXML>
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
<gloss versionDate="2020-12-20" xml:lang="en">so called</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2026-03-26" xml:lang="de">sogenannt</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2026-03-26" xml:lang="it">cosiddetto</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a word or phrase for which the author or narrator indicates a disclaiming of
    responsibility, for example by the use of scare quotes or italics.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2026-03-26" xml:lang="de">enthält ein Wort oder eine Phrase, für die der Autor oder Erzähler einen Haftungsausschluss anzeigt,
    zum Beispiel durch den Einsatz von Anführungszeichen oder Kursivschrift.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une expression ou un mot pour lesquels l'auteur
    ou le narrateur renonce à toute responsabilité, par exemple en utilisant de l'italique ou des
    guillemets.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una palabra o frase de la que el autor o
    narrador declina la responsabilidad, p.ej. mediante el uso de comillas o cursiva.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">作者或敘述者使用的字句在意義上另有所指的表現，例如：諷刺所使用的引號或斜體標示。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una parola o sintagma per cui l'autore o il
    narratore non assume la responsabilità intelletuale, segnalati ad esempio tramite l'uso di
    virgolette o corsivi.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2006-10-28" xml:lang="ja">著者や語り手が、責任を持ちたくない語句を示す。例えば、英語
    文化圏では、引用符号で囲んだり、イタリック体で示される部分。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.emphLike"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-soCalled-egXML-kb" source="#COHQHE-eg-14">To edge his way along
      the crowded paths of life, warning all human sympathy to keep its distance, was what the
      knowing ones call <soCalled>nuts</soCalled> to Scrooge.</egXML>
    <!-- C.Dickens, Xmas Carol, 1843, p5 -->
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-soCalled-egXML-vm" source="#fr-ex-Pennac_Marchande">- On ne
        bouge pas, on ne touche à rien, il faut que je prévienne <soCalled>la Maison</soCalled>.
        C'est ainsi qu'il appelait le Quai des Orfèvres. </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-soCalled-egXML-jb" source="#fr-ex-Hugo-miserables">
      <p> Mais, après tout, les propos auxquels on mêlait son nom n'étaient que des propos ; du
          bruit, des mots, des paroles, moins que des paroles, des<soCalled>palabres</soCalled>,
          comme dit l'énergique langue du midi.</p>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-soCalled-egXML-lq" source="#biblzh-tw_n22">
        眾猴听說，即拱伏無違。一個個序齒排班，朝上禮拜，都稱千歲大王。自此，石猴高登王位，將石字儿隱了，遂稱<soCalled>美猴王</soCalled>。</egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQQ"/>
  </listRef>
```

^b17

