---
type: representation
source-type: document
source: '[[00_sources/tei-p5-source-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 source
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/source.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# source

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2368. Git blob: `ee69041885a7da0c320cb13d074508c21a153c7a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="SOURCE" ident="source">
  <gloss versionDate="2007-06-12" xml:lang="en">source</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">source</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="source.desc">describes the original source for the information contained with a manuscript or object description.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 기술에 포함된 정보에 대한 최초 원본을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述關於手稿說明資訊的原始出處。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料にある、元資料に関する情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit la source des informations contenues dans la
      description du manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe la fuente original que contiene las informaciones sobre la descripción del manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive la fonte delle informazioni contenute nella descrizione del manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SOURCE-egXML-ik">
      <source>Derived from <ref>Stanley (1960)</ref>
         </source>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SOURCE-egXML-sw">
      <source>Derived from <ref>Stanley (1960)</ref>
        </source>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SOURCE-egXML-wl">
      <source>來自 <ref>Stanley (1960)</ref>
         </source>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msrh"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">source</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">source</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="source.desc">describes the original source for the information contained with a manuscript or object description.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 기술에 포함된 정보에 대한 최초 원본을 기술한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述關於手稿說明資訊的原始出處。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料にある、元資料に関する情報を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit la source des informations contenues dans la
      description du manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe la fuente original que contiene las informaciones sobre la descripción del manuscrito.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive la fonte delle informazioni contenute nella descrizione del manoscritto.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SOURCE-egXML-ik">
      <source>Derived from <ref>Stanley (1960)</ref>
         </source>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SOURCE-egXML-sw">
      <source>Derived from <ref>Stanley (1960)</ref>
        </source>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SOURCE-egXML-wl">
      <source>來自 <ref>Stanley (1960)</ref>
         </source>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msrh"/>
  </listRef>
```

^b15

