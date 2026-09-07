---
type: representation
source-type: document
source: '[[00_sources/tei-p5-addspan-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 addSpan
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/addSpan.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# addSpan

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5381. Git blob: `20d8752f7571a2452ce47f7c73117736cfaeddb4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="transcr" xml:id="gi-addSpan" ident="addSpan">
  <gloss versionDate="2005-01-14" xml:lang="en">added span of text</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 추가 구간</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">加入的文字段</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">partie de texte ajoutée</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">fragmento de texto añadido</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">porzione di testo aggiunta</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">追加テキストの範囲</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">hinzugefügter Textabschnitt</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">marks the beginning of a longer sequence of text added by an author, scribe, annotator or corrector (see also <gi>add</gi>).</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">저자, 필기사, 주석자, 또는 교정자에 의해 추가된 긴 연쇄의 텍스트 시작부를 표시한다.(<gi>add</gi> 참조)</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記由作者、抄寫者、註解者或更正者所加入的較長連續文字之開端  (參照<gi>add</gi>) 。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">著者、筆写者、注釈者、校正者の手による長めの追加テキストを挿入する始 点を示す(<gi>add</gi>も参照のこと)。</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">marque le début d'une longue partie de texte ajoutée par un auteur, un copiste, un annotateur ou un correcteur (voir aussi <gi>add</gi>).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">señala el inicio de un fragmento largo de texto añadido por un autor, un transcriptor, un comentarista o un corrector (ver también <gi>add</gi>).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segnala l'inizio di una porzione di testo più lunga aggiunta da un autore, un trascrittore, un annotatore o un correttore (vedi anche <gi>add</gi>).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
  <content><empty/></content>
  <constraintSpec ident="addSpan-requires-spanTo" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:addSpan">
        <sch:assert test="@spanTo">The @spanTo attribute of &lt;<sch:name/>> is required.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="addSpan-requires-spanTo-fr" scheme="schematron" xml:lang="fr">
    <constraint>
      <sch:rule context="tei:addSpan">
        <sch:assert test="@spanTo">L'attribut spanTo est requis.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addSpan-egXML-pd" source="#UND">
      <handNote xml:id="HEOL" scribe="HelgiÓlafsson"/>
      <!-- ... -->
      <body>
        <div>
          <!-- text here -->
        </div>
        <addSpan n="added_gathering" hand="#HEOL" spanTo="#P025"/>
        <div>
          <!-- text of first added poem here -->
        </div>
        <div>
          <!-- text of second added poem here -->
        </div>
        <div>
          <!-- text of third added poem here -->
        </div>
        <div>
          <!-- text of fourth added poem here -->
        </div>
        <anchor xml:id="P025"/>
        <div>
          <!-- more text here -->
        </div>
      </body>
    </egXML>
  </exemplum>
  <remarks ident="addSpan-remarks" versionDate="2006-06-11" xml:lang="en">
    <p>Both the beginning and the end of the added material must be
    marked; the beginning by the <gi>addSpan</gi> element itself, the
    end by the <att>spanTo</att> attribute.</p>
  </remarks>
  <remarks ident="addSpan-remarks" versionDate="2018-09-08" xml:lang="es"><p>Tanto el inicio como el final del material que se agrego debe ser marcado; el inicio con el mismo elemento <gi>addSpan</gi>  y el final con el atributo <att>spanTo</att>.</p></remarks>
  <remarks ident="addSpan-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Le début et la fin de la partie de texte ajoutée doivent être marqués ; le début, par l'élément
                    <gi>addSpan</gi> lui-même, la fin, par l'attribut <att>spanTo</att>.</p>
  </remarks>
  <remarks ident="addSpan-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    追加する情報の始めと終わりの両方にマークアップすべきである。
    始めは、要素<gi>addSpan</gi>自身によって、終わりは属性
    <att>spanTo</att>によって示すことができる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#PHAD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">added span of text</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">텍스트 추가 구간</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">加入的文字段</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">partie de texte ajoutée</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">fragmento de texto añadido</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">porzione di testo aggiunta</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">追加テキストの範囲</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">hinzugefügter Textabschnitt</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks the beginning of a longer sequence of text added by an author, scribe, annotator or corrector (see also <gi>add</gi>).</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">저자, 필기사, 주석자, 또는 교정자에 의해 추가된 긴 연쇄의 텍스트 시작부를 표시한다.(<gi>add</gi> 참조)</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記由作者、抄寫者、註解者或更正者所加入的較長連續文字之開端  (參照<gi>add</gi>) 。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">著者、筆写者、注釈者、校正者の手による長めの追加テキストを挿入する始 点を示す(<gi>add</gi>も参照のこと)。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">marque le début d'une longue partie de texte ajoutée par un auteur, un copiste, un annotateur ou un correcteur (voir aussi <gi>add</gi>).</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">señala el inicio de un fragmento largo de texto añadido por un autor, un transcriptor, un comentarista o un corrector (ver también <gi>add</gi>).</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segnala l'inizio di una porzione di testo più lunga aggiunta da un autore, un trascrittore, un annotatore o un correttore (vedi anche <gi>add</gi>).</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="addSpan-requires-spanTo" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:addSpan">
        <sch:assert test="@spanTo">The @spanTo attribute of &lt;<sch:name/>> is required.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="addSpan-requires-spanTo-fr" scheme="schematron" xml:lang="fr">
    <constraint>
      <sch:rule context="tei:addSpan">
        <sch:assert test="@spanTo">L'attribut spanTo est requis.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addSpan-egXML-pd" source="#UND">
      <handNote xml:id="HEOL" scribe="HelgiÓlafsson"/>
      <!-- ... -->
      <body>
        <div>
          <!-- text here -->
        </div>
        <addSpan n="added_gathering" hand="#HEOL" spanTo="#P025"/>
        <div>
          <!-- text of first added poem here -->
        </div>
        <div>
          <!-- text of second added poem here -->
        </div>
        <div>
          <!-- text of third added poem here -->
        </div>
        <div>
          <!-- text of fourth added poem here -->
        </div>
        <anchor xml:id="P025"/>
        <div>
          <!-- more text here -->
        </div>
      </body>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="addSpan-remarks" versionDate="2006-06-11" xml:lang="en">
    <p>Both the beginning and the end of the added material must be
    marked; the beginning by the <gi>addSpan</gi> element itself, the
    end by the <att>spanTo</att> attribute.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="addSpan-remarks" versionDate="2018-09-08" xml:lang="es"><p>Tanto el inicio como el final del material que se agrego debe ser marcado; el inicio con el mismo elemento <gi>addSpan</gi>  y el final con el atributo <att>spanTo</att>.</p></remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="addSpan-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Le début et la fin de la partie de texte ajoutée doivent être marqués ; le début, par l'élément
                    <gi>addSpan</gi> lui-même, la fin, par l'attribut <att>spanTo</att>.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="addSpan-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    追加する情報の始めと終わりの両方にマークアップすべきである。
    始めは、要素<gi>addSpan</gi>自身によって、終わりは属性
    <att>spanTo</att>によって示すことができる。
    </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHAD"/>
  </listRef>
```

^b25

