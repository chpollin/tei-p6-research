---
type: representation
source-type: document
source: '[[00_sources/tei-p5-wit-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 wit
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/wit.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# wit

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3798. Git blob: `70ccda1038763fc168fdbe2b735352dedbaea2d6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-wit" ident="wit">
  <gloss versionDate="2007-06-12" xml:lang="en">wit</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">témoin</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a list of one or more sigla of witnesses attesting a
given reading, in a textual variation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형에서 주어진 독법을 입증하는 비교 대상 텍스트에 대한 하나 이상의 기호일람표 목록을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">原文變異中，表明已知對應本版本的一個或多個印記的列表。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">読みの元となる文献を表すひとつ以上の文献記号のリストを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une liste d'une ou plusieurs
			abréviation(s) désignant des témoins attestant d'une leçon donnée, pour une version du
			texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una lista de una o más siglas de testimonios que atestiguan una lectura dada de una variante textual.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una lista di una o più sigle di testimoni che attestano una data lettura di una variante testuale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.rdgPart"/>
    <memberOf key="model.rdgPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-wit-egXML-pj">
      <rdg wit="#El #Hg">Experience</rdg>
      <wit>Ellesmere,  Hengwryt</wit>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-wit-egXML-ct">
      <rdg wit="#fr_El #fr_Hg">Experience</rdg>
      <wit>Ellesmere, Hengwryt</wit>
      <!-- EX. A TROUVER A VALIDER  A COMPLETER-->
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-wit-egXML-sz">
      <rdg wit="#El #Hg">經驗</rdg>
      <wit>郝仁</wit>
    </egXML>
  </exemplum>
  <remarks ident="wit-remarks" versionDate="2006-06-11" xml:lang="en">
    <p>This element represents the same  information as that provided by the
<att>wit</att> attribute of the reading; it may be used to record the
exact form of the sigla given in the source edition, when that is of
interest.</p>
  </remarks>
  <remarks ident="wit-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément représente la même information que celle fournie par l'attribut
                <att>wit</att> de la leçon ; on peut l'utiliser pour noter la forme exacte des
                abréviations de témoins données dans l'édition source, lorsque cela présente un
                intérêt.</p>
  </remarks>
  <remarks ident="wit-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、解釈を表す要素<gi>rdg</gi>にある属性<att>wit</att>と、
    同じ情報を示すことになる。元資料にある文献記号の正確な形式に関心が
    ある場合に、それを記録するため使われるかもしれない。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLW"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">wit</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">témoin</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a list of one or more sigla of witnesses attesting a
given reading, in a textual variation.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 변이형에서 주어진 독법을 입증하는 비교 대상 텍스트에 대한 하나 이상의 기호일람표 목록을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">原文變異中，表明已知對應本版本的一個或多個印記的列表。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">読みの元となる文献を表すひとつ以上の文献記号のリストを示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une liste d'une ou plusieurs
			abréviation(s) désignant des témoins attestant d'une leçon donnée, pour une version du
			texte.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una lista de una o más siglas de testimonios que atestiguan una lectura dada de una variante textual.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una lista di una o più sigle di testimoni che attestano una data lettura di una variante testuale.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.rdgPart"/>
    <memberOf key="model.rdgPart"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-wit-egXML-pj">
      <rdg wit="#El #Hg">Experience</rdg>
      <wit>Ellesmere,  Hengwryt</wit>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-wit-egXML-ct">
      <rdg wit="#fr_El #fr_Hg">Experience</rdg>
      <wit>Ellesmere, Hengwryt</wit>
      <!-- EX. A TROUVER A VALIDER  A COMPLETER-->
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-wit-egXML-sz">
      <rdg wit="#El #Hg">經驗</rdg>
      <wit>郝仁</wit>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="wit-remarks" versionDate="2006-06-11" xml:lang="en">
    <p>This element represents the same  information as that provided by the
<att>wit</att> attribute of the reading; it may be used to record the
exact form of the sigla given in the source edition, when that is of
interest.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="wit-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément représente la même information que celle fournie par l'attribut
                <att>wit</att> de la leçon ; on peut l'utiliser pour noter la forme exacte des
                abréviations de témoins données dans l'édition source, lorsque cela présente un
                intérêt.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="wit-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、解釈を表す要素<gi>rdg</gi>にある属性<att>wit</att>と、
    同じ情報を示すことになる。元資料にある文献記号の正確な形式に関心が
    ある場合に、それを記録するため使われるかもしれない。
    </p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLW"/>
  </listRef>
```

^b18

