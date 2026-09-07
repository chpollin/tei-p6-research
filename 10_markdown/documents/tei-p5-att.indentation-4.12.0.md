---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.indentation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.indentation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.indentation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.indentation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2531. Git blob: `08f8fb55c685dec4ffffa21640b19e6e9b126c86`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-indentation" ident="att.indentation">
  <desc versionDate="2024-05-17" xml:lang="en">provides attributes for describing the indentation of a textual element on the source page or object.</desc>
  <desc versionDate="2024-05-17" xml:lang="es">proporciona atributos para describir el sangrado de un elemento textual en la página fuente o en un objeto.</desc>
  <desc versionDate="2024-05-17" xml:lang="de">stellt Attribute zur Beschreibung der Einrückung eines Textelements in der Quelle oder im Objekt bereit.</desc>
  <attList>
    <attDef ident="indentLevel" usage="rec">
      <desc versionDate="2024-05-17" xml:lang="en">specifies the level of indentation of an item using a numeric value.</desc>
      <datatype maxOccurs="1">
        <dataRef name="integer"/>
      </datatype>
      <exemplum xml:lang="de">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-indentation-egXML-gi">
          <post type="standard" generatedBy="human" indentLevel="3" synch="#t02622878" who="#WU00018921">
            <p> Wie du siehst hab ich die Lemma geändert, danke für den Hinweis, ich war nämlich selbst auch etwas unsicher bei der ganzen Sache und bin jetzt damit auch viel glücklicher!--</p>
            <signed rend="inline" generatedBy="template"><gap reason="signatureContent"/>
            <time generatedBy="template">12:01, 12. Jun. 2009 (CEST)</time>
            </signed>
          </post>
        </egXML>
      </exemplum>
      <remarks ident="att.indentation-attr.indentLevel-remarks" versionDate="2024-05-17" xml:lang="en">
        <p>This attribute can be used to mark the level of indentation
        of a post in a thread-like structure (as defined by its author
        and in relation to the standard level of indentation which
        should be encoded with <val>0</val>). This is commonly used
        for Wiki talk pages, but should also be used for genres such
        as webblog comments when the source was HTML.</p>
      </remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#CMCcmcpostatts"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2024-05-17" xml:lang="en">provides attributes for describing the indentation of a textual element on the source page or object.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-05-17" xml:lang="es">proporciona atributos para describir el sangrado de un elemento textual en la página fuente o en un objeto.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2024-05-17" xml:lang="de">stellt Attribute zur Beschreibung der Einrückung eines Textelements in der Quelle oder im Objekt bereit.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2024-05-17" xml:lang="en">specifies the level of indentation of an item using a numeric value.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="1">
        <dataRef name="integer"/>
      </datatype>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="de">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-indentation-egXML-gi">
          <post type="standard" generatedBy="human" indentLevel="3" synch="#t02622878" who="#WU00018921">
            <p> Wie du siehst hab ich die Lemma geändert, danke für den Hinweis, ich war nämlich selbst auch etwas unsicher bei der ganzen Sache und bin jetzt damit auch viel glücklicher!--</p>
            <signed rend="inline" generatedBy="template"><gap reason="signatureContent"/>
            <time generatedBy="template">12:01, 12. Jun. 2009 (CEST)</time>
            </signed>
          </post>
        </egXML>
      </exemplum>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.indentation-attr.indentLevel-remarks" versionDate="2024-05-17" xml:lang="en">
        <p>This attribute can be used to mark the level of indentation
        of a post in a thread-like structure (as defined by its author
        and in relation to the standard level of indentation which
        should be encoded with <val>0</val>). This is commonly used
        for Wiki talk pages, but should also be used for genres such
        as webblog comments when the source was HTML.</p>
      </remarks>
```

^b7

### Block 8

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CMCcmcpostatts"/>
  </listRef>
```

^b8

