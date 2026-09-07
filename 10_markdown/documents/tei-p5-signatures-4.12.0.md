---
type: representation
source-type: document
source: '[[00_sources/tei-p5-signatures-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 signatures
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/signatures.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# signatures

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4269. Git blob: `e8203033464debaa631d617f7a092a2a2b1d059d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="SIGNATURES" ident="signatures">
  <gloss versionDate="2007-06-12" xml:lang="en">signatures</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">signatures</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="signatures.desc">contains discussion of the leaf or quire signatures found within a codex or similar object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">미제본 원고 내의 장 또는 절 표시를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手抄本中一張或一疊書頁內簽名的敘述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">冊子における葉または折丁の記号に関する情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une étude des signatures trouvées sur un feuillet ou sur un cahier dans un manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el registro de las signaturas del folio o del cuaderno pertenecientes al códex.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il registro delle segnature del foglio o del quaderno appartenenti al codice.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <constraintSpec ident="signatures_in_msDesc" scheme="schematron" xml:lang="en">
    <!-- 
         The <egXML> referred to in the constraint below is, of
         course, in the teix: namespace, not the tei: namespace.
         However, at the point in the processing pipeline when we want
         to test this the content of <egXML>s have been extracted and
         put in the TEI namespace for testing.
         At least, that's what I think is going on. —Syd, 2018-10-01
      -->
    <constraint>
      <sch:rule context="tei:signatures">
        <sch:assert test="ancestor::tei:msDesc or ancestor::tei:egXML">The &lt;<sch:name/>> element should not be used outside of &lt;msDesc>.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SIGNATURES-egXML-eq">
      <signatures>Quire and leaf signatures in letters, [b]-v, and roman
numerals; those in quires 10 (1) and 17 (s) in red ink and different
from others; every third quire also signed with red crayon in arabic
numerals in the center lower margin of the first leaf recto: "2" for
quire 4 (f. 19), "3" for quire 7 (f. 43); "4," barely visible, for
quire 10 (f.  65), "5," in a later hand, for quire 13 (f. 89), "6," in
a later hand, for quire 16 (f. 113).</signatures>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SIGNATURES-egXML-ak">
      <signatures>Quire and leaf signatures in letters, [b]-v, and roman numerals; those in quires
          10 (1) and 17 (s) in red ink and different from others; every third quire also signed with
          red crayon in arabic numerals in the center lower margin of the first leaf recto: "2" for
          quire 4 (f. 19), "3" for quire 7 (f. 43); "4," barely visible, for quire 10 (f. 65), "5,"
          in a later hand, for quire 13 (f. 89), "6," in a later hand, for quire 16 (f.
        113).</signatures>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SIGNATURES-egXML-oj" source="#biblzh-tw_n48">
      <signatures>正文前有朱紅藏印: 「武陵人」朱文橢圓印、「國立中央圖/書館收藏」朱文長方印、「奕/修」朱文方印、「約/齋」朱文雙{234245}方印。</signatures>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msmisc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">signatures</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">signatures</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="signatures.desc">contains discussion of the leaf or quire signatures found within a codex or similar object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">미제본 원고 내의 장 또는 절 표시를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手抄本中一張或一疊書頁內簽名的敘述。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">冊子における葉または折丁の記号に関する情報を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une étude des signatures trouvées sur un feuillet ou sur un cahier dans un manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el registro de las signaturas del folio o del cuaderno pertenecientes al códex.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il registro delle segnature del foglio o del quaderno appartenenti al codice.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.pPart.msdesc"/>
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

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="signatures_in_msDesc" scheme="schematron" xml:lang="en">
    <!-- 
         The <egXML> referred to in the constraint below is, of
         course, in the teix: namespace, not the tei: namespace.
         However, at the point in the processing pipeline when we want
         to test this the content of <egXML>s have been extracted and
         put in the TEI namespace for testing.
         At least, that's what I think is going on. —Syd, 2018-10-01
      -->
    <constraint>
      <sch:rule context="tei:signatures">
        <sch:assert test="ancestor::tei:msDesc or ancestor::tei:egXML">The &lt;<sch:name/>> element should not be used outside of &lt;msDesc>.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SIGNATURES-egXML-eq">
      <signatures>Quire and leaf signatures in letters, [b]-v, and roman
numerals; those in quires 10 (1) and 17 (s) in red ink and different
from others; every third quire also signed with red crayon in arabic
numerals in the center lower margin of the first leaf recto: "2" for
quire 4 (f. 19), "3" for quire 7 (f. 43); "4," barely visible, for
quire 10 (f.  65), "5," in a later hand, for quire 13 (f. 89), "6," in
a later hand, for quire 16 (f. 113).</signatures>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SIGNATURES-egXML-ak">
      <signatures>Quire and leaf signatures in letters, [b]-v, and roman numerals; those in quires
          10 (1) and 17 (s) in red ink and different from others; every third quire also signed with
          red crayon in arabic numerals in the center lower margin of the first leaf recto: "2" for
          quire 4 (f. 19), "3" for quire 7 (f. 43); "4," barely visible, for quire 10 (f. 65), "5,"
          in a later hand, for quire 13 (f. 89), "6," in a later hand, for quire 16 (f.
        113).</signatures>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SIGNATURES-egXML-oj" source="#biblzh-tw_n48">
      <signatures>正文前有朱紅藏印: 「武陵人」朱文橢圓印、「國立中央圖/書館收藏」朱文長方印、「奕/修」朱文方印、「約/齋」朱文雙{234245}方印。</signatures>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msmisc"/>
  </listRef>
```

^b16

