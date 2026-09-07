---
type: representation
source-type: document
source: '[[00_sources/tei-p5-iff-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 iff
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/iff.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# iff

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2883. Git blob: `4277ef831974f1683d78e381545c152b99b143a7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-iff" ident="iff">
  <gloss versionDate="2007-07-04" xml:lang="en">if and only if</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">필요충분조건</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">si y solamente si</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">si et seulement si</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">se e solo se</gloss>
  <desc versionDate="2017-02-07" xml:lang="en">separates the condition from the consequence in a <gi>bicond</gi> element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">이중 조건 요소에서 결론과 조건을 분리한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">區分條件和元素<gi>bicond</gi> 裡的結果。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">必要十分条件における前提部と帰結部の区切を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">sépare la condition de la conséquence dans un élément bicond.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">separa la condicion de la consecuencia en un elemento bicond.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">separa la condizione dal successivo in un elemento bicond.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content><empty/></content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iff-egXML-tm" source="#UND">
      <bicond>
        <fs>
          <f name="FOO">
            <symbol value="42"/>
          </f>
        </fs>
        <iff/>
        <fs>
          <f name="BAR">
            <binary value="true"/>
          </f>
        </fs>
      </bicond>
    </egXML>
  </exemplum>
  <remarks ident="iff-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element is provided primarily to enhance the
human readability of the feature-system declaration.</p>
  </remarks>
  <remarks ident="iff-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est fourni essentiellement pour rendre plus lisible par l'homme une
                déclaration d'un système de traits.</p>
  </remarks>
  <remarks ident="iff-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、素性システム宣言を、人に読みやすくするためのものである。
    </p>
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
<gloss versionDate="2007-07-04" xml:lang="en">if and only if</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">필요충분조건</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">si y solamente si</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">si et seulement si</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">se e solo se</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">separates the condition from the consequence in a <gi>bicond</gi> element.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이중 조건 요소에서 결론과 조건을 분리한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">區分條件和元素<gi>bicond</gi> 裡的結果。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">必要十分条件における前提部と帰結部の区切を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">sépare la condition de la conséquence dans un élément bicond.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">separa la condicion de la consecuencia en un elemento bicond.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">separa la condizione dal successivo in un elemento bicond.</desc>
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
<content><empty/></content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-iff-egXML-tm" source="#UND">
      <bicond>
        <fs>
          <f name="FOO">
            <symbol value="42"/>
          </f>
        </fs>
        <iff/>
        <fs>
          <f name="BAR">
            <binary value="true"/>
          </f>
        </fs>
      </bicond>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="iff-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element is provided primarily to enhance the
human readability of the feature-system declaration.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="iff-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est fourni essentiellement pour rendre plus lisible par l'homme une
                déclaration d'un système de traits.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="iff-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、素性システム宣言を、人に読みやすくするためのものである。
    </p>
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

