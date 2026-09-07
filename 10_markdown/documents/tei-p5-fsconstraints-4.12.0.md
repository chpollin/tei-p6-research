---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fsconstraints-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fsConstraints
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fsConstraints.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fsConstraints

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3100. Git blob: `ff97e75781e6bd110b95a46bf9bec10c8ae94623`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fsConstraints" ident="fsConstraints">
  <gloss versionDate="2005-01-14" xml:lang="en">feature-structure constraints</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질-구조 제약</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能結構限制</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">contraintes de structure de traits</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">restricciones de la estructura de rasgo.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">vincoli della struttura di tratti</gloss>
  <desc versionDate="2007-07-13" xml:lang="en">specifies constraints on the content of valid feature
structures.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">유효 자질 구조 내용에 대한 제약을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出完善功能結構的內容限制。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">妥当な素性構造の内容に課す制約を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit les contraintes sur le contenu de structures
      de traits bien formées.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica restricciones para el contenido de estructuras de rasgo bien formadas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica i vincoli sul contenuto delle strutture di tratti ben formate.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="cond"/>
        <elementRef key="bicond"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsConstraints-egXML-zy" source="#UND">
      <fsConstraints>
        <cond>
          <fs>
            <!-- ...-->
          </fs>
          <then/>
          <fs>
            <!-- ... -->
          </fs>
        </cond>
      </fsConstraints>
    </egXML>
  </exemplum>
  <remarks ident="fsConstraints-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain a series of conditional or biconditional elements.</p>
    <p/>
  </remarks>
  <remarks ident="fsConstraints-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une série d'éléments conditionnels ou
            biconditionnels.</p>
  </remarks>
  <remarks ident="fsConstraints-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    一連の条件、すなわち必要十分条件を示す。
    </p>
    <p/>
  </remarks>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">feature-structure constraints</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질-구조 제약</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能結構限制</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contraintes de structure de traits</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">restricciones de la estructura de rasgo.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">vincoli della struttura di tratti</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-07-13" xml:lang="en">specifies constraints on the content of valid feature
structures.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">유효 자질 구조 내용에 대한 제약을 명시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出完善功能結構的內容限制。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">妥当な素性構造の内容に課す制約を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit les contraintes sur le contenu de structures
      de traits bien formées.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica restricciones para el contenido de estructuras de rasgo bien formadas.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica i vincoli sul contenuto delle strutture di tratti ben formate.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="cond"/>
        <elementRef key="bicond"/>
      </alternate>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsConstraints-egXML-zy" source="#UND">
      <fsConstraints>
        <cond>
          <fs>
            <!-- ...-->
          </fs>
          <then/>
          <fs>
            <!-- ... -->
          </fs>
        </cond>
      </fsConstraints>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="fsConstraints-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain a series of conditional or biconditional elements.</p>
    <p/>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="fsConstraints-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une série d'éléments conditionnels ou
            biconditionnels.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="fsConstraints-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    一連の条件、すなわち必要十分条件を示す。
    </p>
    <p/>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b20

