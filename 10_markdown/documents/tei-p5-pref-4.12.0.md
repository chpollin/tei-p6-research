---
type: representation
source-type: document
source: '[[00_sources/tei-p5-pref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 pRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/pRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# pRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2997. Git blob: `e48b3ad20881972ac26f63910c4fd7b38e2154d9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-pRef" ident="pRef">
  <gloss versionDate="2005-01-14" xml:lang="en">pronunciation reference</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">발음 참조</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">發音參照</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">référence à une prononciation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">referencia a la pronunciación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">riferimento per la pronuncia</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">in a dictionary example, indicates a reference to the pronunciation(s) of the headword.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전의 예에서 표제어의 발음에 대한 참조를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在字典範例中，參照出標題字的發音形式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書の用例中で、見出し語の発音への参照を示す。</desc>
  <desc versionDate="2009-04-08" xml:lang="fr">dans un exemple de dictionnaire, indique une référence à
    la/aux prononciation(s) du mot-vedette</desc>
  <desc versionDate="2007-05-04" xml:lang="es">en un diccionario, indica la pronunciación de un lema.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">in un esempio in un dizionario, indica un riferimento
    alla pronuncia del lemma</desc>
  <classes>
      <memberOf key="att.global"/>
      <memberOf key="att.lexicographic"/>
     <memberOf key="att.notated"/>
      <memberOf key="att.pointing"/>
      <memberOf key="model.ptrLike.form"/>
  </classes>
  <content>
     <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <elementRef key="pRef"/>
     </alternate>
  </content>
  <exemplum xml:lang="de">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pRef-egXML-sh">
         <entry>
            <form>
               <orth>umfahren</orth>
               <pron xml:id="umfahren1">umf'ahren</pron>
               <pron xml:id="umfahren2">'umfahren</pron>
            </form>
            <cit>
               <quote>Paul musste die Pfütze <pRef target="#umfahren1"/>, wenn er nicht nass werden wollte.</quote>
            </cit>
            <cit>
               <quote>Paul wollte das Schild nicht absichtlich <pRef target="#umfahren2"/> und beschädigen.</quote>
            </cit>
         </entry>
      </egXML>
   </exemplum>
  <listRef>
      <ptr target="#DIHW"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">pronunciation reference</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">발음 참조</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">發音參照</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">référence à une prononciation</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">referencia a la pronunciación</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">riferimento per la pronuncia</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">in a dictionary example, indicates a reference to the pronunciation(s) of the headword.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전의 예에서 표제어의 발음에 대한 참조를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在字典範例中，參照出標題字的發音形式。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書の用例中で、見出し語の発音への参照を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-08" xml:lang="fr">dans un exemple de dictionnaire, indique une référence à
    la/aux prononciation(s) du mot-vedette</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">en un diccionario, indica la pronunciación de un lema.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">in un esempio in un dizionario, indica un riferimento
    alla pronuncia del lemma</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
      <memberOf key="att.global"/>
      <memberOf key="att.lexicographic"/>
     <memberOf key="att.notated"/>
      <memberOf key="att.pointing"/>
      <memberOf key="model.ptrLike.form"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
     <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <elementRef key="pRef"/>
     </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="de">
      <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-pRef-egXML-sh">
         <entry>
            <form>
               <orth>umfahren</orth>
               <pron xml:id="umfahren1">umf'ahren</pron>
               <pron xml:id="umfahren2">'umfahren</pron>
            </form>
            <cit>
               <quote>Paul musste die Pfütze <pRef target="#umfahren1"/>, wenn er nicht nass werden wollte.</quote>
            </cit>
            <cit>
               <quote>Paul wollte das Schild nicht absichtlich <pRef target="#umfahren2"/> und beschädigen.</quote>
            </cit>
         </entry>
      </egXML>
   </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
      <ptr target="#DIHW"/>
  </listRef>
```

^b17

