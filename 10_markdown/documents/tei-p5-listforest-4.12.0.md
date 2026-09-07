---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listforest-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listForest
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listForest.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listForest

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3049. Git blob: `323a86ca338b04a60df7d3b19c9a067dff8b3db0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-listForest" ident="listForest">
  <desc versionDate="2011-12-02" xml:lang="en">provides for lists of forests.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="forest" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2011-12-02" xml:lang="en">identifies the type of the forest group.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">수형도군의 유형을 식별한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明森林群組的類型。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該森集合の種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise le type du groupe de forêts.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica el tipo de grupo de bosque</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica il tipo di gruppo di foresta.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listForest-egXML-hs" source="#UND">
      <listForest>
        <forest type="derivation-syntactic">
          <tree ord="true">
            <root children="#fgex1 #fgex2"/>
            <!-- ... -->
          </tree>
          <!-- ... -->
        </forest>
        <forest type="derivation-prosodic">
          <tree ord="true">
            <root children="#fgex3 #fgex4"/>
            <!-- ... -->
          </tree>
          <!-- ... -->
        </forest>
      </listForest>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listForest-egXML-if" source="#UND"> </egXML>
  </exemplum>
  <remarks ident="listForest-remarks" versionDate="2011-12-02" xml:lang="en">
    <p rend="dataDesc">One or more forests representing the same object.</p>
  </remarks>
  <remarks ident="listForest-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Une ou plusieurs forêts.</p>
  </remarks>
  <remarks ident="listForest-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    ひとつ以上の森。
    </p>
  </remarks>
  <listRef>
    <ptr target="#GDAT" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-12-02" xml:lang="en">provides for lists of forests.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
```

^b2

### Block 3

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="forest" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b3

### Block 4

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-12-02" xml:lang="en">identifies the type of the forest group.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수형도군의 유형을 식별한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明森林群組的類型。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該森集合の種類を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise le type du groupe de forêts.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica el tipo de grupo de bosque</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica il tipo di gruppo di foresta.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listForest-egXML-hs" source="#UND">
      <listForest>
        <forest type="derivation-syntactic">
          <tree ord="true">
            <root children="#fgex1 #fgex2"/>
            <!-- ... -->
          </tree>
          <!-- ... -->
        </forest>
        <forest type="derivation-prosodic">
          <tree ord="true">
            <root children="#fgex3 #fgex4"/>
            <!-- ... -->
          </tree>
          <!-- ... -->
        </forest>
      </listForest>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listForest-egXML-if" source="#UND"> </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listForest-remarks" versionDate="2011-12-02" xml:lang="en">
    <p rend="dataDesc">One or more forests representing the same object.</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="listForest-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Une ou plusieurs forêts.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="listForest-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    ひとつ以上の森。
    </p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDAT" type="div2"/>
  </listRef>
```

^b17

