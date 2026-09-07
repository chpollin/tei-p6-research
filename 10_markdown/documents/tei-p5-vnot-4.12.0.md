---
type: representation
source-type: document
source: '[[00_sources/tei-p5-vnot-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 vNot
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/vNot.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# vNot

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3098. Git blob: `d992c5b24c4b58e6cc55bb56b99ccdf31f0b424a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-vNot" ident="vNot">
  <gloss versionDate="2007-07-05" xml:lang="en">value negation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">부정 값</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">矛盾值</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">négation de valeur</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">negación de valor</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">una negazione del valore</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents a feature value which is the negation of its content.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">그 내용을 부정하는 자질 값을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">所表示的功能值和其內容互相矛盾。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該要素の内容の否定する素性値を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente une valeur de trait qui est la négation de
      son contenu.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa un valor de rasgo que es la negación de su contenido.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta un valore del tratto che è la negazione del suo contenuto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.featureVal.complex"/>
  </classes>
  <content>
    
      <classRef key="model.featureVal"/>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vNot-egXML-hs" source="#UND">
      <vNot>
        <symbol value="masculine"/>
      </vNot>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vNot-egXML-ii" source="#UND">
      <vNot>
        <symbol value="masculine"/>
      </vNot>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vNot-egXML-wm" source="#UND">
      <f name="mode">
        <vNot>
          <vAlt>
            <symbol value="infinitive"/>
            <symbol value="participle"/>
          </vAlt>
        </vNot>
      </f>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vNot-egXML-ji" source="#UND">
      <f name="mode">
        <vNot>
          <vAlt>
            <symbol value="infinitive"/>
            <symbol value="participle"/>
          </vAlt>
        </vNot>
      </f>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FVNOT" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-05" xml:lang="en">value negation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">부정 값</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">矛盾值</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">négation de valeur</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">negación de valor</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">una negazione del valore</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents a feature value which is the negation of its content.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">그 내용을 부정하는 자질 값을 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">所表示的功能值和其內容互相矛盾。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素の内容の否定する素性値を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente une valeur de trait qui est la négation de
      son contenu.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa un valor de rasgo que es la negación de su contenido.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta un valore del tratto che è la negazione del suo contenuto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.featureVal.complex"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <classRef key="model.featureVal"/>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vNot-egXML-hs" source="#UND">
      <vNot>
        <symbol value="masculine"/>
      </vNot>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vNot-egXML-ii" source="#UND">
      <vNot>
        <symbol value="masculine"/>
      </vNot>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vNot-egXML-wm" source="#UND">
      <f name="mode">
        <vNot>
          <vAlt>
            <symbol value="infinitive"/>
            <symbol value="participle"/>
          </vAlt>
        </vNot>
      </f>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vNot-egXML-ji" source="#UND">
      <f name="mode">
        <vNot>
          <vAlt>
            <symbol value="infinitive"/>
            <symbol value="participle"/>
          </vAlt>
        </vNot>
      </f>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FVNOT" type="div3"/>
  </listRef>
```

^b20

