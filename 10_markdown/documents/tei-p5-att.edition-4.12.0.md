---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.edition-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.edition
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.edition.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.edition

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4825. Git blob: `871d7b20324e1b627924677b1da3bad1bd6faed3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-edition" ident="att.edition">
  <desc versionDate="2013-01-11" xml:lang="en">provides attributes identifying the source edition from which some encoded feature derives.</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">fournit des attributs identifiant l'édition source dont provient une quelconque caractéristique encodée.</desc>
  <desc versionDate="2019-05-20" xml:lang="ja">符号化された属性が派生する元のソースのエディションを特定する属性を提供する。</desc>
  <attList>
    <attDef ident="ed" usage="opt">
      <gloss versionDate="2013-01-11" xml:lang="en">edition</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">édition</gloss>
      <gloss versionDate="2019-05-20" xml:lang="ja">版</gloss>
      <desc versionDate="2013-11-22" xml:lang="en">supplies a sigil or other arbitrary identifier for the source edition in which
      the associated feature (for example, a  page, column, or line
      beginning) occurs at this point in the text.</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">fournit un identifiant arbitraire pour l'édition source dans laquelle la caractéristique associée 
        (par exemple, une page, une colonne ou un saut de ligne) apparaît à ce point du texte.</desc>
      <desc versionDate="2019-05-20" xml:lang="ja">関連する属性（ページ・段落・行の切れ目）がテキストのこの地点において発生するソースのエディションについての印やその他の任意の識別子を提供する。</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
    </attDef>
    <attDef ident="edRef" usage="opt">
      <gloss versionDate="2013-01-11" xml:lang="en">edition reference</gloss>
      <gloss versionDate="2019-05-20" xml:lang="ja">参照</gloss>
      <desc versionDate="2013-01-11" xml:lang="en">provides a pointer to the source edition in which
      the associated feature (for example, a  page, column, or line
      beginning) occurs at this point in the text.</desc>
      <desc versionDate="2019-05-20" xml:lang="ja">このポインタが示すのは、当該テキスト中に現れる（頁や段、行等の）関連する素性が生じる元の版である。</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-edition-egXML-tc">
      <l>Of Mans First Disobedience,<lb ed="1674"/> and<lb ed="1667"/> the Fruit</l>
      <l>Of that Forbidden Tree, whose<lb ed="1667 1674"/> mortal tast</l>
      <l>Brought Death into the World,<lb ed="1667"/> and all<lb ed="1674"/> our woe,</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-edition-egXML-ey">
      <listBibl>
        <bibl xml:id="stapledon1937"><author>Olaf Stapledon</author>,
	<title>Starmaker</title>, <publisher>Methuen</publisher>, <date>1937</date></bibl>
        <bibl xml:id="stapledon1968"><author>Olaf Stapledon</author>,
	<title>Starmaker</title>, <publisher>Dover</publisher>, <date>1968</date></bibl>
      </listBibl>
      <!-- ... -->
      <p>Looking into the future aeons from the supreme moment of
	  the cosmos, I saw the populations still with all their
	  strength maintaining the<pb n="411" edRef="#stapledon1968"/>essentials of their ancient culture,
	  still living their personal lives in zest and endless
	  novelty of action, … I saw myself still
	  preserving, though with increasing difficulty, my lucid
	  con<pb n="291" break="no" edRef="#stapledon1937"/>sciousness;</p>
    </egXML>
    <p>In the above example, the soft hyphen in Stapledon 1937 is omitted. Such decisions may be documented in the edition's declaration of editorial principles, e.g. with the <gi>hyphenation</gi> element in the <gi>teiHeader</gi>.</p>
  </exemplum>
  <remarks ident="att.edition-remarks" versionDate="2025-07-08" xml:lang="en">
    <p>These guidelines provide no semantic basis or suggested
      precedence when both <att>ed</att> and <att>edRef</att> are
      provided. For this reason simultaneous use of both is not
      recommended unless documentation explaining the use is provided,
      probably in an ODD customization, for interchange.</p>
  </remarks>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-01-11" xml:lang="en">provides attributes identifying the source edition from which some encoded feature derives.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">fournit des attributs identifiant l'édition source dont provient une quelconque caractéristique encodée.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2019-05-20" xml:lang="ja">符号化された属性が派生する元のソースのエディションを特定する属性を提供する。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2013-01-11" xml:lang="en">edition</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">édition</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2019-05-20" xml:lang="ja">版</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-11-22" xml:lang="en">supplies a sigil or other arbitrary identifier for the source edition in which
      the associated feature (for example, a  page, column, or line
      beginning) occurs at this point in the text.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">fournit un identifiant arbitraire pour l'édition source dans laquelle la caractéristique associée 
        (par exemple, une page, une colonne ou un saut de ligne) apparaît à ce point du texte.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2019-05-20" xml:lang="ja">関連する属性（ページ・段落・行の切れ目）がテキストのこの地点において発生するソースのエディションについての印やその他の任意の識別子を提供する。</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2013-01-11" xml:lang="en">edition reference</gloss>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2019-05-20" xml:lang="ja">参照</gloss>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-01-11" xml:lang="en">provides a pointer to the source edition in which
      the associated feature (for example, a  page, column, or line
      beginning) occurs at this point in the text.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2019-05-20" xml:lang="ja">このポインタが示すのは、当該テキスト中に現れる（頁や段、行等の）関連する素性が生じる元の版である。</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-edition-egXML-tc">
      <l>Of Mans First Disobedience,<lb ed="1674"/> and<lb ed="1667"/> the Fruit</l>
      <l>Of that Forbidden Tree, whose<lb ed="1667 1674"/> mortal tast</l>
      <l>Brought Death into the World,<lb ed="1667"/> and all<lb ed="1674"/> our woe,</l>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/classSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-edition-egXML-ey">
      <listBibl>
        <bibl xml:id="stapledon1937"><author>Olaf Stapledon</author>,
	<title>Starmaker</title>, <publisher>Methuen</publisher>, <date>1937</date></bibl>
        <bibl xml:id="stapledon1968"><author>Olaf Stapledon</author>,
	<title>Starmaker</title>, <publisher>Dover</publisher>, <date>1968</date></bibl>
      </listBibl>
      <!-- ... -->
      <p>Looking into the future aeons from the supreme moment of
	  the cosmos, I saw the populations still with all their
	  strength maintaining the<pb n="411" edRef="#stapledon1968"/>essentials of their ancient culture,
	  still living their personal lives in zest and endless
	  novelty of action, … I saw myself still
	  preserving, though with increasing difficulty, my lucid
	  con<pb n="291" break="no" edRef="#stapledon1937"/>sciousness;</p>
    </egXML>
    <p>In the above example, the soft hyphen in Stapledon 1937 is omitted. Such decisions may be documented in the edition's declaration of editorial principles, e.g. with the <gi>hyphenation</gi> element in the <gi>teiHeader</gi>.</p>
  </exemplum>
```

^b17

### Block 18

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.edition-remarks" versionDate="2025-07-08" xml:lang="en">
    <p>These guidelines provide no semantic basis or suggested
      precedence when both <att>ed</att> and <att>edRef</att> are
      provided. For this reason simultaneous use of both is not
      recommended unless documentation explaining the use is provided,
      probably in an ODD customization, for interchange.</p>
  </remarks>
```

^b18

