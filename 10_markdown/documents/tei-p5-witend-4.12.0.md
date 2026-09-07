---
type: representation
source-type: document
source: '[[00_sources/tei-p5-witend-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 witEnd
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/witEnd.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# witEnd

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2342. Git blob: `ad135d53db5179176bacc0e5f13b3ad4535c4282`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-witEnd" ident="witEnd">
  <gloss versionDate="2007-07-04" xml:lang="en">fragmented witness end</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">파편화된 비교 대상 텍스트의 종료부</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">fin del testimonio fragmentado</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">fin d'un témoin fragmentaire</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">fine di testimone frammentario</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates the end, or suspension, of the text of a fragmentary
witness.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">파편화된 비교 대상 텍스트의 종료부 또는 중지부를 나타낸다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指明零散版本文字的結尾或中止。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">断片的な文献のテキストの終わりまたは停止点を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indique la fin ou l'arrêt du texte d'un témoin fragmentaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el inicio o la continuación del texto de un testimonio fragmentario</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica la fine o l'interruzione del testo di un testimone frammentario.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.rdgPart"/>
    <memberOf key="model.rdgPart"/>
  </classes>
  <content><empty/></content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-witEnd-egXML-fi">
      <app>
        <lem wit="#El #Hg">Experience</lem>
        <rdg wit="#Ha4">Ex<g ref="#per"/>
               <witEnd/>
            </rdg>
      </app>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TCAPMI"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">fragmented witness end</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">파편화된 비교 대상 텍스트의 종료부</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">fin del testimonio fragmentado</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">fin d'un témoin fragmentaire</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">fine di testimone frammentario</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the end, or suspension, of the text of a fragmentary
witness.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">파편화된 비교 대상 텍스트의 종료부 또는 중지부를 나타낸다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明零散版本文字的結尾或中止。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">断片的な文献のテキストの終わりまたは停止点を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique la fin ou l'arrêt du texte d'un témoin fragmentaire.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el inicio o la continuación del texto de un testimonio fragmentario</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la fine o l'interruzione del testo di un testimone frammentario.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.rdgPart"/>
    <memberOf key="model.rdgPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-witEnd-egXML-fi">
      <app>
        <lem wit="#El #Hg">Experience</lem>
        <rdg wit="#Ha4">Ex<g ref="#per"/>
               <witEnd/>
            </rdg>
      </app>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPMI"/>
  </listRef>
```

^b17

