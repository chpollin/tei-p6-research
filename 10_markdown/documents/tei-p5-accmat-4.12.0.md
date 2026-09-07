---
type: representation
source-type: document
source: '[[00_sources/tei-p5-accmat-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 accMat
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/accMat.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# accMat

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4074. Git blob: `20879a1bd3c904ad9292e200a5d69e98abdfbc9e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="ACCMAT" ident="accMat">
  <gloss versionDate="2005-01-14" xml:lang="en">accompanying material</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">동봉 자료</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">伴隨資料</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">matériel d'accompagnement</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">material adicional</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">materiale allegato</gloss>
  <gloss versionDate="2018-12-18" xml:lang="ja">添付資料</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">Begleitmaterial</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="accmat.desc">contains details of any significant additional
material which may be closely associated with the manuscript or object being
described, such as non-contemporaneous documents or fragments bound in
with it at some earlier historical period.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">기술하고 있는 원고와 밀접히 관련된 중요한 부가적 자료를 세밀하게 기술한다. 예를 들어, 어떤 이전 시기에 원고와 함께 제본된 비동시대의 문서  또는 문서 일부.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含可能與該手稿關係密切的重要附加資料之細節，例如非同時期的文件或是在早期與手稿裝訂一起的片段。</desc>
  <desc versionDate="2022-06-07" xml:lang="ja">当該手書き資料と密接に関連していると考えられる重要な追加資料、例えば、時代を異にする文書、歴史的に早い時期に手書き資料と合わされた断片などの詳細を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">donne des détails sur tout matériel d'accompagnement
      étroitement associé au manuscrit, tel que documents non contemporains ou fragments reliés avec
      le manuscrit à une époque antérieure.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene eventuales detalles que conciernen a materiales añadidos estrechamente relacionados con el manuscrito examinado, p.ej. documentos no actuales o fragmentos cosidos junto al manuscrito en un período histórico precedente al actual.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene eventuali dettagli riguardanti maeriale aggiuntivo strettamente collegato al manoscritto in esame, per esempio documenti non attali o frammenti rilegati insieme al manoscritto in un periodo storico precedente a quello attuale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.physDescPart"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACCMAT-egXML-ar" source="#UND">
      <accMat>A copy of a tax form from 1947 is included in the envelope
with the letter. It is not catalogued separately.</accMat>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACCMAT-egXML-fc" source="#UND">
      <accMat>A copy of a tax form from 1947 is included in the envelope with the letter. It is
          not catalogued separately.</accMat>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACCMAT-egXML-bk" source="#UND">
      <accMat>有張1947年的稅單一同與此信件放於信封裡，不單獨分類。</accMat>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msadac"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">accompanying material</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">동봉 자료</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">伴隨資料</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">matériel d'accompagnement</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">material adicional</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">materiale allegato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2018-12-18" xml:lang="ja">添付資料</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">Begleitmaterial</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="accmat.desc">contains details of any significant additional
material which may be closely associated with the manuscript or object being
described, such as non-contemporaneous documents or fragments bound in
with it at some earlier historical period.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기술하고 있는 원고와 밀접히 관련된 중요한 부가적 자료를 세밀하게 기술한다. 예를 들어, 어떤 이전 시기에 원고와 함께 제본된 비동시대의 문서  또는 문서 일부.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含可能與該手稿關係密切的重要附加資料之細節，例如非同時期的文件或是在早期與手稿裝訂一起的片段。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-06-07" xml:lang="ja">当該手書き資料と密接に関連していると考えられる重要な追加資料、例えば、時代を異にする文書、歴史的に早い時期に手書き資料と合わされた断片などの詳細を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne des détails sur tout matériel d'accompagnement
      étroitement associé au manuscrit, tel que documents non contemporains ou fragments reliés avec
      le manuscrit à une époque antérieure.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene eventuales detalles que conciernen a materiales añadidos estrechamente relacionados con el manuscrito examinado, p.ej. documentos no actuales o fragmentos cosidos junto al manuscrito en un período histórico precedente al actual.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene eventuali dettagli riguardanti maeriale aggiuntivo strettamente collegato al manoscritto in esame, per esempio documenti non attali o frammenti rilegati insieme al manoscritto in un periodo storico precedente a quello attuale.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.physDescPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACCMAT-egXML-ar" source="#UND">
      <accMat>A copy of a tax form from 1947 is included in the envelope
with the letter. It is not catalogued separately.</accMat>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACCMAT-egXML-fc" source="#UND">
      <accMat>A copy of a tax form from 1947 is included in the envelope with the letter. It is
          not catalogued separately.</accMat>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ACCMAT-egXML-bk" source="#UND">
      <accMat>有張1947年的稅單一同與此信件放於信封裡，不單獨分類。</accMat>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msadac"/>
  </listRef>
```

^b21

