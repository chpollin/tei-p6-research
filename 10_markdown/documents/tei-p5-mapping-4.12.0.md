---
type: representation
source-type: document
source: '[[00_sources/tei-p5-mapping-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 mapping
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/mapping.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# mapping

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4979. Git blob: `0c3f709b33be1e5e483fcc98dae0be22da751d2b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="gaiji" xml:id="MAPPING" ident="mapping">
  <gloss versionDate="2005-01-14" xml:lang="en">character mapping</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문자 사상</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文字對應</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">caractères associés</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">representación del carácter</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">mappatura di carattreri</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains one or more
	 characters which are related to the parent character or glyph
	 in some respect, as specified by the <att>type</att>
	 attribute.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><att>type</att> 상위 문자 또는 그림 문자와 관련된 하나 이상의 문자들을 포함한다. 속성으로 명시된다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含與父文字或字體在某方面有所關聯的一個或多個文字，在屬性<att>type</att>中加以說明。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">属性<att>type</att>で示される、親文字またはグリフと関連する、ひとつ
  以上の文字を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un ou plusieurs caractères reliés par
			certains aspects (spécifiés par l'attribut <att>type</att>) au glyphe ou au caractère
			défini dans l'élément parent.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene uno o más caracteres que se relacionan en algún sentido con el carácter o pictograma del padre, como se especifica por el atributo de <att>type</att>.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene uno u più caratteri in una qualche relazione con il carattere o glifo parente, come specificato dall'attributo <att>type</att>.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <macroRef key="macro.xtext"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MAPPING-egXML-tl">
      <mapping type="modern">r</mapping>
      <mapping type="standard">人</mapping>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MAPPING-egXML-hg">
      <mapping type="modern">r</mapping>
      <mapping type="standard">人</mapping>
    </egXML>
  </exemplum>
  <remarks ident="mapping-remarks" versionDate="2017-05-11" xml:lang="en">
    <p>Suggested values for the <att>type</att> attribute include
<val>exact</val> for exact equivalences, <val>uppercase</val>
for uppercase equivalences, <val>lowercase</val>   for lowercase equivalences,
and <val>simplified</val>  for simplified characters. The
	 <gi>g</gi> elements contained by this element can  point to either another
	 <gi>char</gi> or <gi>glyph</gi> element or contain a character
	 that is intended to be the target of this mapping.</p>
  </remarks>
  <remarks ident="mapping-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les valeurs conseillées de l'attribut <att>type</att> sont : <code>exact</code> pour
                une relation d'équivalence, <code>uppercase</code> pour spécifier une correspondance
                avec un caractère en majuscules, <code>lowercase</code> pour spécifier une
                correspondance avec un caractère en minuscules, et <code>simplified</code> pour
                spécifier une correspondance avec un caractère simplifié. Les éléments <gi>g</gi>
                contenus par l'élément <gi>mapping</gi> peuvent, soit pointer vers un autre élément
                    <gi>char</gi> ou <gi>glyph</gi>, soit contenir un caractère, cible de la
                relation de correspondance.</p>
  </remarks>
  <remarks ident="mapping-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>type</att>の値として、同等物の場合には<code>exact</code>
  を、大文字表記の場合には<code>uppercase</code>を、小文字表記の場合に
  は<code>lowercase</code>を、簡易表記の場合には
  <code>simplified</code>などをとる。当該要素に含まれる要素<gi>g</gi>
  は、他の要素<gi>char</gi>や<gi>glyph</gi>を参照することや、当該要素
  で対象となる文字をとることも可能である。
  </p>
  </remarks>
  <listRef>
    <ptr target="#D25-20"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">character mapping</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문자 사상</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文字對應</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">caractères associés</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">representación del carácter</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">mappatura di carattreri</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains one or more
	 characters which are related to the parent character or glyph
	 in some respect, as specified by the <att>type</att>
	 attribute.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><att>type</att> 상위 문자 또는 그림 문자와 관련된 하나 이상의 문자들을 포함한다. 속성으로 명시된다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含與父文字或字體在某方面有所關聯的一個或多個文字，在屬性<att>type</att>中加以說明。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性<att>type</att>で示される、親文字またはグリフと関連する、ひとつ
  以上の文字を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un ou plusieurs caractères reliés par
			certains aspects (spécifiés par l'attribut <att>type</att>) au glyphe ou au caractère
			défini dans l'élément parent.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene uno o más caracteres que se relacionan en algún sentido con el carácter o pictograma del padre, como se especifica por el atributo de <att>type</att>.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene uno u più caratteri in una qualche relazione con il carattere o glifo parente, come specificato dall'attributo <att>type</att>.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.xtext"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MAPPING-egXML-tl">
      <mapping type="modern">r</mapping>
      <mapping type="standard">人</mapping>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MAPPING-egXML-hg">
      <mapping type="modern">r</mapping>
      <mapping type="standard">人</mapping>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="mapping-remarks" versionDate="2017-05-11" xml:lang="en">
    <p>Suggested values for the <att>type</att> attribute include
<val>exact</val> for exact equivalences, <val>uppercase</val>
for uppercase equivalences, <val>lowercase</val>   for lowercase equivalences,
and <val>simplified</val>  for simplified characters. The
	 <gi>g</gi> elements contained by this element can  point to either another
	 <gi>char</gi> or <gi>glyph</gi> element or contain a character
	 that is intended to be the target of this mapping.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="mapping-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les valeurs conseillées de l'attribut <att>type</att> sont : <code>exact</code> pour
                une relation d'équivalence, <code>uppercase</code> pour spécifier une correspondance
                avec un caractère en majuscules, <code>lowercase</code> pour spécifier une
                correspondance avec un caractère en minuscules, et <code>simplified</code> pour
                spécifier une correspondance avec un caractère simplifié. Les éléments <gi>g</gi>
                contenus par l'élément <gi>mapping</gi> peuvent, soit pointer vers un autre élément
                    <gi>char</gi> ou <gi>glyph</gi>, soit contenir un caractère, cible de la
                relation de correspondance.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="mapping-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>type</att>の値として、同等物の場合には<code>exact</code>
  を、大文字表記の場合には<code>uppercase</code>を、小文字表記の場合に
  は<code>lowercase</code>を、簡易表記の場合には
  <code>simplified</code>などをとる。当該要素に含まれる要素<gi>g</gi>
  は、他の要素<gi>char</gi>や<gi>glyph</gi>を参照することや、当該要素
  で対象となる文字をとることも可能である。
  </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#D25-20"/>
  </listRef>
```

^b21

