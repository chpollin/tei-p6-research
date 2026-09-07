---
type: representation
source-type: document
source: '[[00_sources/tei-p5-acquisition-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 acquisition
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/acquisition.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# acquisition

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3277. Git blob: `8926dcc167bcbd36ab9562ac02754cef51925ade`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="ACQUISITION" ident="acquisition">
  <gloss versionDate="2007-06-12" xml:lang="en">acquisition</gloss>
  <gloss versionDate="2022-06-16" xml:lang="es">adquisición</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">acquisition</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">Akquise</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="acquisn.desc">contains any descriptive or other information
concerning the process by which a manuscript or manuscript part or other object entered the holding
institution.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 그 일부가 현 보유 기관에 입수된 과정에 관련한 기술적 또는 기타 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何描述性或其他資訊，關於手稿或手稿部分進入保管機構的過程。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料が入手された経緯についての情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur les modalités et
      circonstances de l'entrée du manuscrit ou de la partie du manuscrit dans l'institution qui le
      détient.</desc>
  <desc versionDate="2022-06-16" xml:lang="es">contiene cualquier descripción u otra información concerniente al proceso de adquisición del manuscrito o de una de sus partes o cualquier otro objeto que haya ingresado en la institución</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative al processo di acquisizione di un manoscritto o di una sua parte.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACQUISITION-egXML-my" source="#UND">
      <acquisition>Left to the <name type="place">Bodleian</name> by 
<name type="person">Richard Rawlinson</name> in 1755.
</acquisition>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACQUISITION-egXML-xp" source="#UND">
      <acquisition>Left to the <name type="place">Bodleian</name> by<name type="person">Richard
            Rawlinson</name> in 1755.</acquisition>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACQUISITION-egXML-mc" source="#UND">
      <acquisition>1998年9 月30 日，<name type="institution">CBETA</name> 與<name type="institution">日本大藏出版株式會社</name>簽約授權使用。</acquisition>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mshy"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">acquisition</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2022-06-16" xml:lang="es">adquisición</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">acquisition</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">Akquise</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="acquisn.desc">contains any descriptive or other information
concerning the process by which a manuscript or manuscript part or other object entered the holding
institution.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 그 일부가 현 보유 기관에 입수된 과정에 관련한 기술적 또는 기타 정보를 포함한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何描述性或其他資訊，關於手稿或手稿部分進入保管機構的過程。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料が入手された経緯についての情報を示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur les modalités et
      circonstances de l'entrée du manuscrit ou de la partie du manuscrit dans l'institution qui le
      détient.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-06-16" xml:lang="es">contiene cualquier descripción u otra información concerniente al proceso de adquisición del manuscrito o de una de sus partes o cualquier otro objeto que haya ingresado en la institución</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative al processo di acquisizione di un manoscritto o di una sua parte.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACQUISITION-egXML-my" source="#UND">
      <acquisition>Left to the <name type="place">Bodleian</name> by 
<name type="person">Richard Rawlinson</name> in 1755.
</acquisition>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACQUISITION-egXML-xp" source="#UND">
      <acquisition>Left to the <name type="place">Bodleian</name> by<name type="person">Richard
            Rawlinson</name> in 1755.</acquisition>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACQUISITION-egXML-mc" source="#UND">
      <acquisition>1998年9 月30 日，<name type="institution">CBETA</name> 與<name type="institution">日本大藏出版株式會社</name>簽約授權使用。</acquisition>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mshy"/>
  </listRef>
```

^b17

