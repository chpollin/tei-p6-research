---
type: representation
source-type: document
source: '[[00_sources/tei-p5-forest-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 forest
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/forest.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# forest

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3796. Git blob: `f443856f1b1ce328b631ea77836e2be8ebc2dff8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="nets" xml:id="gi-forest" ident="forest">
  <gloss versionDate="2007-06-12" xml:lang="en">forest</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">forêt</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides for groups of rooted trees.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">뿌리가 있는 수형도군을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集具根節點的樹狀結構群組。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">根付き木のの集合を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">permet d'encoder des groupes d'arbres à racine.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define grupos de árboles enraizados.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce gruppi di alberi radicati.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <elementRef key="tree"/>
      <elementRef key="eTree"/>
      <elementRef key="triangle"/>
    </alternate>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-forest-egXML-nt">
      <forest n="ex5" type="derivation-syntactic">
        <eTree n="Stage 1" xml:id="s1SBAR">
          <label>S'</label>
          <eTree xml:id="s1S">
            <label>S</label>
            <eTree xml:id="s1NP1">
              <label>NP</label>
              <eLeaf>
                <label>you</label>
              </eLeaf>
            </eTree>
            <eTree xml:id="s1VP">
              <label>VP</label>
              <eTree xml:id="s1V">
                <label>V</label>
                <eLeaf>
                  <label>do</label>
                </eLeaf>
              </eTree>
            </eTree>
          </eTree>
        </eTree>
        <eTree n="Stage 2" xml:id="s2SBAR" corresp="#s1SBAR">
          <label>S'</label>
          <eTree xml:id="s2S" corresp="#s1S">
            <label>S</label>
            <eTree xml:id="s2NP1" copyOf="#s1NP1">
              <label>NP</label>
            </eTree>
            <eTree xml:id="s2VP" corresp="#s1VP">
              <label>VP</label>
              <eTree xml:id="s2V" copyOf="#s1V">
                <label>V</label>
              </eTree>
              <eTree xml:id="s2NP2" corresp="#s1NP2">
                <label>NP</label>
                <eLeaf corresp="#s1WH">
                  <label>t</label>
                </eLeaf>
              </eTree>
            </eTree>
          </eTree>
        </eTree>
      </forest>
    </egXML>
  </exemplum>
  <remarks ident="forest-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">One or more trees, embedding trees, or underspecified embedding
trees (triangles).</p>
  </remarks>
  <remarks ident="forest-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Un ou plusieurs arbres, des arbres englobants ou des arbres englobants sommaires (triangles).</p>
  </remarks>
  <remarks ident="forest-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    ひとつ以上の木、部分木、省略部分木。
    </p>
  </remarks>
  <listRef>
    <ptr target="#GDAT" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">forest</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">forêt</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides for groups of rooted trees.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">뿌리가 있는 수형도군을 제공한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集具根節點的樹狀結構群組。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">根付き木のの集合を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">permet d'encoder des groupes d'arbres à racine.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define grupos de árboles enraizados.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce gruppi di alberi radicati.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.standOffPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <elementRef key="tree"/>
      <elementRef key="eTree"/>
      <elementRef key="triangle"/>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-forest-egXML-nt">
      <forest n="ex5" type="derivation-syntactic">
        <eTree n="Stage 1" xml:id="s1SBAR">
          <label>S'</label>
          <eTree xml:id="s1S">
            <label>S</label>
            <eTree xml:id="s1NP1">
              <label>NP</label>
              <eLeaf>
                <label>you</label>
              </eLeaf>
            </eTree>
            <eTree xml:id="s1VP">
              <label>VP</label>
              <eTree xml:id="s1V">
                <label>V</label>
                <eLeaf>
                  <label>do</label>
                </eLeaf>
              </eTree>
            </eTree>
          </eTree>
        </eTree>
        <eTree n="Stage 2" xml:id="s2SBAR" corresp="#s1SBAR">
          <label>S'</label>
          <eTree xml:id="s2S" corresp="#s1S">
            <label>S</label>
            <eTree xml:id="s2NP1" copyOf="#s1NP1">
              <label>NP</label>
            </eTree>
            <eTree xml:id="s2VP" corresp="#s1VP">
              <label>VP</label>
              <eTree xml:id="s2V" copyOf="#s1V">
                <label>V</label>
              </eTree>
              <eTree xml:id="s2NP2" corresp="#s1NP2">
                <label>NP</label>
                <eLeaf corresp="#s1WH">
                  <label>t</label>
                </eLeaf>
              </eTree>
            </eTree>
          </eTree>
        </eTree>
      </forest>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="forest-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">One or more trees, embedding trees, or underspecified embedding
trees (triangles).</p>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="forest-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Un ou plusieurs arbres, des arbres englobants ou des arbres englobants sommaires (triangles).</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="forest-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    ひとつ以上の木、部分木、省略部分木。
    </p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#GDAT" type="div2"/>
  </listRef>
```

^b16

