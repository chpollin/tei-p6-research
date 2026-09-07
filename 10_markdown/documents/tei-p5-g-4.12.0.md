---
type: representation
source-type: document
source: '[[00_sources/tei-p5-g-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 g
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/g.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# g

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5188. Git blob: `fba591d514280b5865700e646ba875afc0f32df0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="gaiji" ident="g" xml:id="G">
  <gloss versionDate="2005-01-14" xml:lang="en">character or glyph</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문자 또는 그림문자</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文字或字體</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">caractère ou glyphe</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">carácter o pictograma</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">carattere o glifo</gloss>
  <desc versionDate="2012-09-22" xml:lang="en">represents a glyph, or a non-standard character.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">비표준 문자 또는 그림문자를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">非標準的文字或字體。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">非標準的な文字やグリフを示す。</desc>
  <desc versionDate="2009-05-27" xml:lang="fr">représente un glyphe,
  ou un caractère non standard.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa un carácter no estándard o un pictograma.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rapperesenta un carattere o glifo non standard.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.gLike"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <attList>
    <attDef ident="ref">
      <desc versionDate="2005-01-14" xml:lang="en">points to a description of the character or glyph intended.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到該文字或字體的描述。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該文字やグリフの解説を参照する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers la description du caractère ou du glyphe
        visé</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la descripción del carácter o pictograma dado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">punta a una descrizione del carattere o glifo.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-xb">
      <g ref="#ctlig">ct</g>
    </egXML>
    <p>This example points to a <gi>glyph</gi> element with the identifier <code>ctlig</code> like
      the following: <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-vh" source="#UND"><glyph xml:id="ctlig"><!-- here we describe the particular ct-ligature intended --></glyph></egXML>
      </p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-yb">
      <g ref="#fr_flig">fl</g>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cet exemple pointe vers un élément<gi>glyph</gi>à l'aide du code
        identifiant<code>flig</code> comme dans l'exemple suivant :<egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-jt" source="#UND"><glyph xml:id="flig"/></egXML>
      </p>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-aw">
      <g ref="#zh-tw_flig">fl</g>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-gf" source="#UND">
      <glyph xml:id="zh-tw_flig">
        <!--...-->
      </glyph>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-oe">
      <g ref="#per-glyph">per</g>
    </egXML>
    <p>The medieval brevigraph per could similarly be considered as an individual glyph, defined in
      a <gi>glyph</gi> element with the identifier <code>per-glyph</code> as follows: <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-od" source="#UND"><glyph xml:id="per-glyph"><!-- ... --></glyph></egXML>
      </p>
  </exemplum>
  <remarks ident="g-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The name <ident>g</ident> is short for <term>gaiji</term>, which is the Japanese term for a
      non-standardized character or glyph.</p>
  </remarks>
  <remarks ident="g-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le nom <ident>g</ident> de cet élément est une abréviation pour <term>gaiji</term>, qui
      désigne en Japonais un caractère ou un glyphe non standard.</p>
  </remarks>
  <remarks ident="g-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<ident>g</ident>の要素名は、日本語の「外字」を語源とする <term>gaiji</term>の頭文字である。 </p>
  </remarks>
  <listRef>
    <ptr target="#WD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">character or glyph</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문자 또는 그림문자</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文字或字體</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">caractère ou glyphe</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">carácter o pictograma</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">carattere o glifo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-09-22" xml:lang="en">represents a glyph, or a non-standard character.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">비표준 문자 또는 그림문자를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">非標準的文字或字體。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">非標準的な文字やグリフを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">représente un glyphe,
  ou un caractère non standard.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa un carácter no estándard o un pictograma.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rapperesenta un carattere o glifo non standard.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.gLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">points to a description of the character or glyph intended.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">連結到該文字或字體的描述。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該文字やグリフの解説を参照する。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers la description du caractère ou du glyphe
        visé</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la descripción del carácter o pictograma dado.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">punta a una descrizione del carattere o glifo.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-xb">
      <g ref="#ctlig">ct</g>
    </egXML>
    <p>This example points to a <gi>glyph</gi> element with the identifier <code>ctlig</code> like
      the following: <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-vh" source="#UND"><glyph xml:id="ctlig"><!-- here we describe the particular ct-ligature intended --></glyph></egXML>
      </p>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-yb">
      <g ref="#fr_flig">fl</g>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cet exemple pointe vers un élément<gi>glyph</gi>à l'aide du code
        identifiant<code>flig</code> comme dans l'exemple suivant :<egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-jt" source="#UND"><glyph xml:id="flig"/></egXML>
      </p>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-aw">
      <g ref="#zh-tw_flig">fl</g>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-gf" source="#UND">
      <glyph xml:id="zh-tw_flig">
        <!--...-->
      </glyph>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-oe">
      <g ref="#per-glyph">per</g>
    </egXML>
    <p>The medieval brevigraph per could similarly be considered as an individual glyph, defined in
      a <gi>glyph</gi> element with the identifier <code>per-glyph</code> as follows: <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="G-egXML-od" source="#UND"><glyph xml:id="per-glyph"><!-- ... --></glyph></egXML>
      </p>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="g-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The name <ident>g</ident> is short for <term>gaiji</term>, which is the Japanese term for a
      non-standardized character or glyph.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="g-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le nom <ident>g</ident> de cet élément est une abréviation pour <term>gaiji</term>, qui
      désigne en Japonais un caractère ou un glyphe non standard.</p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="g-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<ident>g</ident>の要素名は、日本語の「外字」を語源とする <term>gaiji</term>の頭文字である。 </p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#WD"/>
  </listRef>
```

^b31

