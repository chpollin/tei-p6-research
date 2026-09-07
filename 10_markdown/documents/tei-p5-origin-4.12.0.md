---
type: representation
source-type: document
source: '[[00_sources/tei-p5-origin-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 origin
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/origin.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# origin

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3138. Git blob: `679192d49e9bb984cd5356267a4c479443c35195`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="ORIGIN" ident="origin">
  <gloss versionDate="2007-06-12" xml:lang="en">origin</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">origine</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="origin.desc">contains any descriptive or other information concerning the origin of  a manuscript, manuscript part, or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고 일부의 기원에 관한 기술적 또는 그 외의 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含關於手稿或手稿部分的來源之任何描述性或其他資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の出自に関する解説や情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur l'origine du manuscrit ou de la partie de manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene informaciones relativas al orígen de un manuscrito o de una de sus partes.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative all'origine di un manoscritto o di una sua parte.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGIN-egXML-tm">
      <origin notBefore="1802" notAfter="1845" evidence="internal" resp="#AMH">
Copied in <name type="origPlace">Derby</name>, probably from an
old Flemish original, between 1802 and 1845, according to <persName xml:id="AMH">Anne-Mette Hansen</persName>.
</origin>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGIN-egXML-tp">
      <origin notBefore="1802" notAfter="1845" evidence="internal" resp="#fr_AMH"> Copied in <name type="origPlace">Derby</name>, probably from an old Flemish original, between 1802 and
          1845, according to <persName xml:id="fr_AMH">Anne-Mette Hansen</persName>.</origin>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGIN-egXML-iy">
      <origin notBefore="1802" notAfter="1845" evidence="internal" resp="#zh-tw_HDM">抄寫於 <name type="origPlace">印度</name>，可能源自巴利文，時間介於1802至1845年間，由<persName xml:id="zh-tw_HDM">黃大鳴</persName>提供。</origin>
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
<gloss versionDate="2007-06-12" xml:lang="en">origin</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">origine</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="origin.desc">contains any descriptive or other information concerning the origin of  a manuscript, manuscript part, or other object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고 일부의 기원에 관한 기술적 또는 그 외의 정보를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含關於手稿或手稿部分的來源之任何描述性或其他資訊。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の出自に関する解説や情報を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur l'origine du manuscrit ou de la partie de manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene informaciones relativas al orígen de un manuscrito o de una de sus partes.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative all'origine di un manoscritto o di una sua parte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGIN-egXML-tm">
      <origin notBefore="1802" notAfter="1845" evidence="internal" resp="#AMH">
Copied in <name type="origPlace">Derby</name>, probably from an
old Flemish original, between 1802 and 1845, according to <persName xml:id="AMH">Anne-Mette Hansen</persName>.
</origin>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGIN-egXML-tp">
      <origin notBefore="1802" notAfter="1845" evidence="internal" resp="#fr_AMH"> Copied in <name type="origPlace">Derby</name>, probably from an old Flemish original, between 1802 and
          1845, according to <persName xml:id="fr_AMH">Anne-Mette Hansen</persName>.</origin>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ORIGIN-egXML-iy">
      <origin notBefore="1802" notAfter="1845" evidence="internal" resp="#zh-tw_HDM">抄寫於 <name type="origPlace">印度</name>，可能源自巴利文，時間介於1802至1845年間，由<persName xml:id="zh-tw_HDM">黃大鳴</persName>提供。</origin>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mshy"/>
  </listRef>
```

^b15

