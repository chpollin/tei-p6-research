---
type: representation
source-type: document
source: '[[00_sources/tei-p5-msname-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 msName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/msName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# msName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3551. Git blob: `36af13d65c786f3081db1550c0fba834130d38ef`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="MSNAME" ident="msName">
  <gloss versionDate="2024-12-23" xml:lang="en">manuscript name</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">이명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">替換名稱</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">autre nom</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nombre alternativo.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nome alternativo</gloss>
  <gloss versionDate="2024-12-23" xml:lang="de">Manuskriptname</gloss>
  <desc versionDate="2024-12-23" xml:lang="en">contains a proper noun or noun phrase used for a manuscript, or other object, as opposed to a formal identification number or classmark.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><soCalled>ocellus nominum</soCalled> 또는 별명처럼 원고에 사용된 어떤 형식의 구조화되지 않은 이명(대체명)을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿無特定結構的任何形式替換名稱，像是<soCalled>ocellus nominum</soCalled>或是暱稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料を示す構造化されていない別名の形式を示す。例えば、
  <soCalled>ocellus nominum</soCalled>などの愛称など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un autre nom, dans une forme libre, utilisé pour désigner le manuscrit, tel qu'un surnom ou un <soCalled>ocellus nominum</soCalled>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier forma de nombre alternativo no estructurado usado para un manuscrito, como por ejemplo <soCalled>ocellus nominum</soCalled>, o sobranombre.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi nome alternativo non strutturato utilizzato per un manoscritto, per esempio <soCalled>ocellus
nominum</soCalled>, o soprannome</desc>
  <desc versionDate="2024-12-23" xml:lang="de">enthält einen Eigennamen in Form eines Nomens oder einer Nominalphrase, der für ein Manuskript oder anderes Objekt verwendet wird, anstatt einer formalen Identifikationsnummer oder Signatur.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <elementRef key="rs"/>
      <elementRef key="name"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSNAME-egXML-yq">
      <msName>The Vercelli Book</msName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSNAME-egXML-ub">
      <msName>The Vercelli Book</msName>
      <!--NOTE : LA TRADUCTION DE MSNAME EST A REPRENDRE-->
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSNAME-egXML-uw">
      <msName>心經</msName>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msid"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2024-12-23" xml:lang="en">manuscript name</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">이명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">替換名稱</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">autre nom</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nombre alternativo.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">nome alternativo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-12-23" xml:lang="de">Manuskriptname</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2024-12-23" xml:lang="en">contains a proper noun or noun phrase used for a manuscript, or other object, as opposed to a formal identification number or classmark.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><soCalled>ocellus nominum</soCalled> 또는 별명처럼 원고에 사용된 어떤 형식의 구조화되지 않은 이명(대체명)을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿無特定結構的任何形式替換名稱，像是<soCalled>ocellus nominum</soCalled>或是暱稱。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料を示す構造化されていない別名の形式を示す。例えば、
  <soCalled>ocellus nominum</soCalled>などの愛称など。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un autre nom, dans une forme libre, utilisé pour désigner le manuscrit, tel qu'un surnom ou un <soCalled>ocellus nominum</soCalled>.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier forma de nombre alternativo no estructurado usado para un manuscrito, como por ejemplo <soCalled>ocellus nominum</soCalled>, o sobranombre.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi nome alternativo non strutturato utilizzato per un manoscritto, per esempio <soCalled>ocellus
nominum</soCalled>, o soprannome</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2024-12-23" xml:lang="de">enthält einen Eigennamen in Form eines Nomens oder einer Nominalphrase, der für ein Manuskript oder anderes Objekt verwendet wird, anstatt einer formalen Identifikationsnummer oder Signatur.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <elementRef key="rs"/>
      <elementRef key="name"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSNAME-egXML-yq">
      <msName>The Vercelli Book</msName>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSNAME-egXML-ub">
      <msName>The Vercelli Book</msName>
      <!--NOTE : LA TRADUCTION DE MSNAME EST A REPRENDRE-->
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSNAME-egXML-uw">
      <msName>心經</msName>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msid"/>
  </listRef>
```

^b21

