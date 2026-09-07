---
type: representation
source-type: document
source: '[[00_sources/tei-p5-constraint-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 constraint
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/constraint.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# constraint

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1890. Git blob: `f6b2f82fd0814350bd7770a8cde8a4fb548d600d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-constraint" ident="constraint">
  <gloss versionDate="2009-06-10" xml:lang="en">constraint rules</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">制約規則</gloss>
  <desc versionDate="2009-06-10" xml:lang="en">the formal rules of a constraint</desc>
  <desc versionDate="2024-02-24" xml:lang="ja">形式的な制約規則</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <anyElement/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraint-egXML-uq">
      <constraintSpec ident="isoconstraint" scheme="schematron">
        <constraint>
          <sch:rule context="tei:constraint">
            <sch:assert test="tei:fileDesc/tei:titleStmt/tei:title[ @type eq 'main']">A main title must be supplied.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraint-egXML-mb">
      <constraintSpec ident="local" scheme="private">
        <constraint> 
(output = (ident(title) ident(author) "You must supply a title or an author"))
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDTAG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-06-10" xml:lang="en">constraint rules</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">制約規則</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2009-06-10" xml:lang="en">the formal rules of a constraint</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-02-24" xml:lang="ja">形式的な制約規則</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <anyElement/>
    </alternate>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraint-egXML-uq">
      <constraintSpec ident="isoconstraint" scheme="schematron">
        <constraint>
          <sch:rule context="tei:constraint">
            <sch:assert test="tei:fileDesc/tei:titleStmt/tei:title[ @type eq 'main']">A main title must be supplied.</sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-constraint-egXML-mb">
      <constraintSpec ident="local" scheme="private">
        <constraint> 
(output = (ident(title) ident(author) "You must supply a title or an author"))
        </constraint>
      </constraintSpec>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
  </listRef>
```

^b9

