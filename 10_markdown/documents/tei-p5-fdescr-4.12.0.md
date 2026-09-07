---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fdescr-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fDescr
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fDescr.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fDescr

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3143. Git blob: `ba0f64b10396d7568dfe36f3605326b2322ed043`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fDescr" ident="fDescr">
  <gloss versionDate="2005-01-14" xml:lang="en">feature description (in FSD)</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질 기술(FSD에서)</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能描述 (在功能結構宣告中)</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description de trait (dans FSD)</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción de rasgo (en FSD)</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrifine di tratto (in FSD)</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes in prose what is represented by the feature being
declared and its values.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">선언되고 있는 자질과 그 값에 의해 표시된 정보를 산문체로 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述被宣告的功能所代表的意義以及其功能值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該素性により示されるものを、散文で示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit en texte libre le trait déclaré et ses
      valeurs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe en prosa qué respresenta el rasgo que se declara y sus valores.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive in prosa ciò che è rappresentato dal tratto che si sta dichiarando e dai sui valori.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.limitedContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fDescr-egXML-hb">
      <fDecl name="INV">
        <fDescr>inverted sentence</fDescr>
        <vRange>
          <vAlt>
            <binary value="true"/>
            <binary value="false"/>
          </vAlt>
        </vRange>
        <vDefault>
          <binary value="false"/>
        </vDefault>
      </fDecl>
    </egXML>
  </exemplum>
  <remarks ident="fDescr-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data, phrase-level elements, and
inter-level elements.</p>
    <p/>
  </remarks>
  <remarks ident="fDescr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères, des éléments de niveau expression ou de
                niveau intermédiaire.</p>
  </remarks>
  <remarks ident="fDescr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    文字、句レベル要素、挿入レベル要素。
    </p>
    <p/>
  </remarks>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">feature description (in FSD)</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질 기술(FSD에서)</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能描述 (在功能結構宣告中)</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description de trait (dans FSD)</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción de rasgo (en FSD)</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrifine di tratto (in FSD)</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes in prose what is represented by the feature being
declared and its values.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">선언되고 있는 자질과 그 값에 의해 표시된 정보를 산문체로 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述被宣告的功能所代表的意義以及其功能值。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該素性により示されるものを、散文で示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit en texte libre le trait déclaré et ses
      valeurs.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe en prosa qué respresenta el rasgo que se declara y sus valores.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive in prosa ciò che è rappresentato dal tratto che si sta dichiarando e dai sui valori.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.limitedContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fDescr-egXML-hb">
      <fDecl name="INV">
        <fDescr>inverted sentence</fDescr>
        <vRange>
          <vAlt>
            <binary value="true"/>
            <binary value="false"/>
          </vAlt>
        </vRange>
        <vDefault>
          <binary value="false"/>
        </vDefault>
      </fDecl>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="fDescr-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data, phrase-level elements, and
inter-level elements.</p>
    <p/>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="fDescr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères, des éléments de niveau expression ou de
                niveau intermédiaire.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="fDescr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    文字、句レベル要素、挿入レベル要素。
    </p>
    <p/>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b20

