---
type: representation
source-type: document
source: '[[00_sources/tei-p5-vlabel-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 vLabel
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/vLabel.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# vLabel

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4390. Git blob: `5cb46effe54742faded6c34d71ddfa5acb12f34b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-vLabel" ident="vLabel">
  <gloss versionDate="2005-01-14" xml:lang="en">value label</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">값 표지</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">值標籤</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">étiquette de valeur</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">etiqueta de valor</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">un'etichetta</gloss>
  <desc versionDate="2007-10-18" xml:lang="en">represents the value part of a feature-value specification
  which appears at more than one point in a feature structure.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">자질 구조에서 하나 이상의 위치에 나타나는 자질-값 명세 중 값의 부분을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，這項值部分資訊出現在功能結構中一個以上的位置。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性構造中、複数箇所に現れる、素性値規定の値の部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui apparaît en plus d’un point dans une structure de traits.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que aparece más de en un punto en una estructura de rasgo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che compare in più di un punto nella struttura dei tratti.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
  <content>
    
      <classRef key="model.featureVal" minOccurs="0"/>
    
  </content>
  <attList>
    <attDef ident="name" usage="req">
      <desc versionDate="2013-11-20" xml:lang="en">supplies a name
      identifying the sharing point.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">공유 지점의 이름을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供該共享值的名稱。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">共有ポイントの場所を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit un nom pour le point de partage.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un nombre para un punto de división.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un nome per il punto di condivisione.</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vLabel-egXML-nd" source="#UND">
      <fs>
        <f name="nominal">
          <fs>
            <f name="nm-num">
              <vLabel name="L1">
                <symbol value="singular"/>
              </vLabel>
            </f>
            <!-- other nominal features -->
          </fs>
        </f>
        <f name="verbal">
          <fs>
            <f name="vb-num">
              <vLabel name="L1"/>
            </f>
          </fs>
          <!-- other verbal features -->
        </f>
      </fs>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vLabel-egXML-ul" source="#UND">
      <fs>
        <f name="nominal">
          <fs>
            <f name="nm-num">
              <vLabel name="L1">
                <symbol value="singular"/>
              </vLabel>
            </f>
          </fs>
        </f>
        <f name="verbal">
          <fs>
            <f name="vb-num">
              <vLabel name="L1"/>
            </f>
          </fs>
        </f>
      </fs>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FSVAR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">value label</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">값 표지</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">值標籤</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">étiquette de valeur</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">etiqueta de valor</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">un'etichetta</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">represents the value part of a feature-value specification
  which appears at more than one point in a feature structure.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질 구조에서 하나 이상의 위치에 나타나는 자질-값 명세 중 값의 부분을 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示功能值細節的值部分資訊，這項值部分資訊出現在功能結構中一個以上的位置。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性構造中、複数箇所に現れる、素性値規定の値の部分を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente la partie valeur d'une spécification
      trait-valeur qui apparaît en plus d’un point dans une structure de traits.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa la parte del valor de una especificación de valor de rasgo que aparece más de en un punto en una estructura de rasgo.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta la parte di valore di una specifica del valore dei tratti che compare in più di un punto nella struttura dei tratti.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.featureVal.single"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <classRef key="model.featureVal" minOccurs="0"/>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-11-20" xml:lang="en">supplies a name
      identifying the sharing point.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">공유 지점의 이름을 제시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供該共享值的名稱。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">共有ポイントの場所を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit un nom pour le point de partage.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un nombre para un punto de división.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un nome per il punto di condivisione.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vLabel-egXML-nd" source="#UND">
      <fs>
        <f name="nominal">
          <fs>
            <f name="nm-num">
              <vLabel name="L1">
                <symbol value="singular"/>
              </vLabel>
            </f>
            <!-- other nominal features -->
          </fs>
        </f>
        <f name="verbal">
          <fs>
            <f name="vb-num">
              <vLabel name="L1"/>
            </f>
          </fs>
          <!-- other verbal features -->
        </f>
      </fs>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vLabel-egXML-ul" source="#UND">
      <fs>
        <f name="nominal">
          <fs>
            <f name="nm-num">
              <vLabel name="L1">
                <symbol value="singular"/>
              </vLabel>
            </f>
          </fs>
        </f>
        <f name="verbal">
          <fs>
            <f name="vb-num">
              <vLabel name="L1"/>
            </f>
          </fs>
        </f>
      </fs>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSVAR"/>
  </listRef>
```

^b26

