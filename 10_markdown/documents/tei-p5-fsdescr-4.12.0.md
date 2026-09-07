---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fsdescr-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fsDescr
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fsDescr.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fsDescr

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3798. Git blob: `2d52adc49b6e6a47f18d959e92175702945fe838`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fsDescr" ident="fsDescr">
  <gloss versionDate="2005-01-14" xml:lang="en">feature system description (in FSD)</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질 체계 기술(FSD 에서)</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能系統描述 (在功能結構宣告中)</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description de système de traits (dans FSD)</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción de sistema de rasgo (en FSD)</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione del sistema di tratti (in FSD)</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes in prose what is represented by the type of feature
structure declared in the enclosing fsDecl.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">fsDecl에서 선언된 자질 구조 유형에 의해 표시된 정보를 산문체로 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述在功能結構宣告中宣告的功能結構類型所代表的意義。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素fsDeclで定義される素性構造の内容を、散文で示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit en texte libre ce que représente le type de
      structure de traits déclaré dans le fsDecl englobant.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe en prosa qué se representa mediante el tipo de estructura de rasgo declarado en la fsDecl.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive in prosa quello che viene rappresentato dal tipo di struttura dei tratti dichiarati nella fsDecl acclusa.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.limitedContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsDescr-egXML-yd">
      <fsDecl type="Agreement">
        <fsDescr>This type of feature structure encodes the features
              for subject-verb agreement in English</fsDescr>
        <fDecl name="PERS">
          <fDescr>person (first, second, or third)</fDescr>
          <vRange>
            <vAlt>
              <symbol value="first"/>
              <symbol value="second"/>
              <symbol value="third"/>
            </vAlt>
          </vRange>
        </fDecl>
        <fDecl name="NUM">
          <fDescr>number (singular or plural)</fDescr>
          <vRange>
            <vAlt>
              <symbol value="singular"/>
              <symbol value="plural"/>
            </vAlt>
          </vRange>
        </fDecl>
      </fsDecl>
    </egXML>
  </exemplum>
  <remarks ident="fsDescr-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data, phrase-level elements, and
inter-level elements.</p>
    <p/>
  </remarks>
  <remarks ident="fsDescr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères, des éléments de niveau expression ou de
                niveau intermédiaire.</p>
  </remarks>
  <remarks ident="fsDescr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    文字列、句レベル要素、挿入レベル要素。
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
<gloss versionDate="2005-01-14" xml:lang="en">feature system description (in FSD)</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질 체계 기술(FSD 에서)</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能系統描述 (在功能結構宣告中)</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description de système de traits (dans FSD)</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción de sistema de rasgo (en FSD)</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione del sistema di tratti (in FSD)</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes in prose what is represented by the type of feature
structure declared in the enclosing fsDecl.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">fsDecl에서 선언된 자질 구조 유형에 의해 표시된 정보를 산문체로 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述在功能結構宣告中宣告的功能結構類型所代表的意義。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素fsDeclで定義される素性構造の内容を、散文で示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit en texte libre ce que représente le type de
      structure de traits déclaré dans le fsDecl englobant.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe en prosa qué se representa mediante el tipo de estructura de rasgo declarado en la fsDecl.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive in prosa quello che viene rappresentato dal tipo di struttura dei tratti dichiarati nella fsDecl acclusa.</desc>
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
    <macroRef key="macro.limitedContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsDescr-egXML-yd">
      <fsDecl type="Agreement">
        <fsDescr>This type of feature structure encodes the features
              for subject-verb agreement in English</fsDescr>
        <fDecl name="PERS">
          <fDescr>person (first, second, or third)</fDescr>
          <vRange>
            <vAlt>
              <symbol value="first"/>
              <symbol value="second"/>
              <symbol value="third"/>
            </vAlt>
          </vRange>
        </fDecl>
        <fDecl name="NUM">
          <fDescr>number (singular or plural)</fDescr>
          <vRange>
            <vAlt>
              <symbol value="singular"/>
              <symbol value="plural"/>
            </vAlt>
          </vRange>
        </fDecl>
      </fsDecl>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="fsDescr-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data, phrase-level elements, and
inter-level elements.</p>
    <p/>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="fsDescr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères, des éléments de niveau expression ou de
                niveau intermédiaire.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="fsDescr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    文字列、句レベル要素、挿入レベル要素。
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

