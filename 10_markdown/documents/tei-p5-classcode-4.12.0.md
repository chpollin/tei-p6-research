---
type: representation
source-type: document
source: '[[00_sources/tei-p5-classcode-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 classCode
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/classCode.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# classCode

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4230. Git blob: `91253fb87112e57bed05e9233cc73a35978efaf6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-classCode" ident="classCode">
  <gloss versionDate="2007-07-04" xml:lang="en">classification code</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">code de classification</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">분류 부호</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">código de clasificación</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Klassifikationscode</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">codice di clasificazione</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">分類コード</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the classification code used for this text in some standard classification system.</desc>
  <desc versionDate="2009-04-22" xml:lang="fr">contient le code de classification attribué à ce texte en
    référence à un système standard de classification.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준 분류 체계에서 이 텍스트에 대하여 사용된 분류 부호를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件在某標準分類系統中所屬的分類代碼。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該テキストで使用されている、ある規格に従った分類コードを示す。</desc>
    <desc versionDate="2016-11-24" xml:lang="de">enthält den für den Text verwendeten Klassifikationscode auf Basis eines normierten Klassifikationssystems.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el código de clasificación empleado para este
    texto en algún sistema de clasificación estándard.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il codice di classificazione utilizzato per
    questo testo in un sistema di calssificazione standard.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="scheme" usage="req">
      <desc versionDate="2016-11-04" xml:lang="en">identifies the
      classification system in use, as defined by, e.g. a <gi>taxonomy</gi> element, or
      some other resource.</desc>
      <desc versionDate="2009-04-22" xml:lang="fr">identifie le système de classification ou la
        taxinomie utilisée.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사용하고 있는 분류 체계 또는 분류법을 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明使用中的分類系統或分類法。</desc>
      <desc versionDate="2024-02-28" xml:lang="ja">用いられている分類体系を定義する<gi>taxonomy</gi>要素や他の資料などを指す。</desc>
        <desc versionDate="2016-11-24" xml:lang="de">benennt das verwendete Klassifikationssystem, definiert z. B. durch Verweis auf ein 
            <gi>taxonomy</gi>-Element oder eine andere Ressource.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica el sistema de clasificación o taxonomía en
        uso.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">idantifica il sistema di classificazione o la
        tassonomia utilizzati.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classCode-egXML-tg">
      <classCode scheme="http://www.udc.org">410</classCode>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classCode-egXML-yf">
      <classCode scheme="http://www.oclc.org/">801</classCode>
      <bibl>classification Dewey</bibl>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD43"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">classification code</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">code de classification</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">분류 부호</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">código de clasificación</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Klassifikationscode</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">codice di clasificazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">分類コード</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the classification code used for this text in some standard classification system.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-22" xml:lang="fr">contient le code de classification attribué à ce texte en
    référence à un système standard de classification.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준 분류 체계에서 이 텍스트에 대하여 사용된 분류 부호를 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件在某標準分類系統中所屬的分類代碼。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストで使用されている、ある規格に従った分類コードを示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">enthält den für den Text verwendeten Klassifikationscode auf Basis eines normierten Klassifikationssystems.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el código de clasificación empleado para este
    texto en algún sistema de clasificación estándard.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il codice di classificazione utilizzato per
    questo testo in un sistema di calssificazione standard.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2016-11-04" xml:lang="en">identifies the
      classification system in use, as defined by, e.g. a <gi>taxonomy</gi> element, or
      some other resource.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-04-22" xml:lang="fr">identifie le système de classification ou la
        taxinomie utilisée.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사용하고 있는 분류 체계 또는 분류법을 표시한다.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明使用中的分類系統或分類法。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">用いられている分類体系を定義する<gi>taxonomy</gi>要素や他の資料などを指す。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">benennt das verwendete Klassifikationssystem, definiert z. B. durch Verweis auf ein 
            <gi>taxonomy</gi>-Element oder eine andere Ressource.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica el sistema de clasificación o taxonomía en
        uso.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">idantifica il sistema di classificazione o la
        tassonomia utilizzati.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classCode-egXML-tg">
      <classCode scheme="http://www.udc.org">410</classCode>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classCode-egXML-yf">
      <classCode scheme="http://www.oclc.org/">801</classCode>
      <bibl>classification Dewey</bibl>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD43"/>
  </listRef>
```

^b29

