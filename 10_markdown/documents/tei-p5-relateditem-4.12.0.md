---
type: representation
source-type: document
source: '[[00_sources/tei-p5-relateditem-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 relatedItem
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/relatedItem.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# relatedItem

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5383. Git blob: `3da21ac8dcdff4dffea4798cd4e3b333d360f59b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" ident="relatedItem" xml:id="gi-relatedItem" module="core">
  <desc versionDate="2007-03-19" xml:lang="en">contains or references some other bibliographic item which is related to the present one in some specified manner, for example as a constituent or alternative version of it.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구성물이나 대체 버전과 같이 현 항목과 특정 방식으로 관련된 다른 서지 항목을 명시적 방식에 따라 포함하거나 지시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含或參照到其他書目項目，該些項目與目前的書目項目在某種程度上相關，例如作為其組成或者替代項目。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該内容と関連する書誌情報項目を示す、または参照する。例えば、構成要 素または他の版など。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient ou référe à un autre élément bibliographique ayant une relation quelconque avec l'objet décrit, par exemple comme faisant partie d'une version alternative de celui-ci, ou bien en étant une version alternative.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene o si riferisce ad altra entità bibliografica legata alla presente tramite una relazione specificata quale, per esempio, versione costitutiva o alternativa.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene o refiere algún otro elemento bibliográfico que se relaciona con el actual de alguna manera, por ejemplo como un versión complementaria o alternativa de este.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält oder verweist auf ein anderes bibliografisches Objekt, welches zu dem aktuellen in einer bestimmten Beziehung steht, z. B. als Bestandteil oder Alternativfassung.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
  </classes>
  <content>
    <alternate minOccurs="0">
      <classRef key="model.biblLike"/>
      <classRef key="model.ptrLike"/>
    </alternate>
  </content>
  <constraintSpec ident="targetorcontent1" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:relatedItem">
        <sch:report test="@target and count( child::* ) &gt; 0">If the @target attribute on <sch:name/> is used, the relatedItem element must be empty.</sch:report>
        <sch:assert test="@target or child::*">A relatedItem element should have either a @target attribute or a child element to indicate the related bibliographic item.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="target" usage="opt">
      <desc versionDate="2009-11-06" xml:lang="en">points to the related bibliographic element by means of an
      absolute or relative URI reference.</desc>
      <desc versionDate="2017-06-13" xml:lang="de">zeigt auf das in Beziehung stehende bibliografische Objekt durch eine absolute oder relative URI.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-relatedItem-egXML-lo">
      <biblStruct>
        <monogr>
          <author>Shirley, James</author>
          <title type="main">The gentlemen of Venice</title>
          <imprint>
            <pubPlace>New York</pubPlace>
            <publisher>Readex Microprint</publisher>
            <date>1953</date>
          </imprint>
          <extent>1 microprint card, 23 x 15 cm.</extent>
        </monogr>
        <series>
          <title>Three centuries of drama: English, 1642–1700</title>
        </series>
        <relatedItem type="otherForm">
          <biblStruct>
            <monogr>
              <author>Shirley, James</author>
              <title type="main">The gentlemen of Venice</title>
              <title type="sub">a tragi-comedie presented at the private house in Salisbury
                Court by Her Majesties servants</title>
              <imprint>
                <pubPlace>London</pubPlace>
                <publisher>H. Moseley</publisher>
                <date>1655</date>
              </imprint>
              <extent>78 p.</extent>
            </monogr>
          </biblStruct>
        </relatedItem>
      </biblStruct>
    </egXML>
  </exemplum>
  <remarks ident="relatedItem-remarks" versionDate="2017-06-25" xml:lang="en">
    <p>If the <att>target</att> attribute is used to reference
  the related bibliographic item, the element must be
  empty.</p>
  </remarks>
  <remarks ident="relatedItem-remarks" versionDate="2017-06-25" xml:lang="de">
    <p>Wenn das <att>target</att>-Attribut verwendet wird, um auf das in Beziehung stehende Objekt zu
      verweisen, muss das Element leer bleiben.</p>
  </remarks>
  <listRef>
    <ptr target="#COBIRI"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-03-19" xml:lang="en">contains or references some other bibliographic item which is related to the present one in some specified manner, for example as a constituent or alternative version of it.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구성물이나 대체 버전과 같이 현 항목과 특정 방식으로 관련된 다른 서지 항목을 명시적 방식에 따라 포함하거나 지시한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含或參照到其他書目項目，該些項目與目前的書目項目在某種程度上相關，例如作為其組成或者替代項目。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該内容と関連する書誌情報項目を示す、または参照する。例えば、構成要 素または他の版など。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient ou référe à un autre élément bibliographique ayant une relation quelconque avec l'objet décrit, par exemple comme faisant partie d'une version alternative de celui-ci, ou bien en étant une version alternative.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene o si riferisce ad altra entità bibliografica legata alla presente tramite una relazione specificata quale, per esempio, versione costitutiva o alternativa.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene o refiere algún otro elemento bibliográfico que se relaciona con el actual de alguna manera, por ejemplo como un versión complementaria o alternativa de este.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält oder verweist auf ein anderes bibliografisches Objekt, welches zu dem aktuellen in einer bestimmten Beziehung steht, z. B. als Bestandteil oder Alternativfassung.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
  </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0">
      <classRef key="model.biblLike"/>
      <classRef key="model.ptrLike"/>
    </alternate>
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="targetorcontent1" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:relatedItem">
        <sch:report test="@target and count( child::* ) &gt; 0">If the @target attribute on <sch:name/> is used, the relatedItem element must be empty.</sch:report>
        <sch:assert test="@target or child::*">A relatedItem element should have either a @target attribute or a child element to indicate the related bibliographic item.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2009-11-06" xml:lang="en">points to the related bibliographic element by means of an
      absolute or relative URI reference.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">zeigt auf das in Beziehung stehende bibliografische Objekt durch eine absolute oder relative URI.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-relatedItem-egXML-lo">
      <biblStruct>
        <monogr>
          <author>Shirley, James</author>
          <title type="main">The gentlemen of Venice</title>
          <imprint>
            <pubPlace>New York</pubPlace>
            <publisher>Readex Microprint</publisher>
            <date>1953</date>
          </imprint>
          <extent>1 microprint card, 23 x 15 cm.</extent>
        </monogr>
        <series>
          <title>Three centuries of drama: English, 1642–1700</title>
        </series>
        <relatedItem type="otherForm">
          <biblStruct>
            <monogr>
              <author>Shirley, James</author>
              <title type="main">The gentlemen of Venice</title>
              <title type="sub">a tragi-comedie presented at the private house in Salisbury
                Court by Her Majesties servants</title>
              <imprint>
                <pubPlace>London</pubPlace>
                <publisher>H. Moseley</publisher>
                <date>1655</date>
              </imprint>
              <extent>78 p.</extent>
            </monogr>
          </biblStruct>
        </relatedItem>
      </biblStruct>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="relatedItem-remarks" versionDate="2017-06-25" xml:lang="en">
    <p>If the <att>target</att> attribute is used to reference
  the related bibliographic item, the element must be
  empty.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="relatedItem-remarks" versionDate="2017-06-25" xml:lang="de">
    <p>Wenn das <att>target</att>-Attribut verwendet wird, um auf das in Beziehung stehende Objekt zu
      verweisen, muss das Element leer bleiben.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBIRI"/>
  </listRef>
```

^b18

