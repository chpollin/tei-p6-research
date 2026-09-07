---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.styledef-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.styleDef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.styleDef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.styleDef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5339. Git blob: `bad7d8e85800a276ee6c3470c0723a55a73c1b8d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tei" type="atts" ident="att.styleDef">
  <desc versionDate="2015-02-15" xml:lang="en">provides attributes to specify the name of a formal definition language used to provide formatting or rendition information.</desc>
  <attList>
    <attDef ident="scheme">
      <desc versionDate="2012-10-06" xml:lang="en">identifies the language used to describe the rendition.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">모양을 기술하는 언어를 식별한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">identifica el lenguaje usado para describir la interpretación.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該描出を解説する言語を特定する。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">identifie la langue employée pour décrire le rendu.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">identifica la lingua utilizzata per descrivere la resa</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="css">
          <desc versionDate="2012-10-06" xml:lang="en">Cascading Stylesheet Language</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">연속식 스타일시트 언어</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Lenguaje de CSS</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">CSS</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">langage CSS (Cascading Stylesheet )</desc>
          <desc versionDate="2007-11-06" xml:lang="it">linguaggio CSS.</desc>
        </valItem>
        <valItem ident="xslfo">
          <desc versionDate="2012-10-06" xml:lang="en">Extensible Stylesheet Language Formatting Objects</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">확장가능 스타일시트 언어</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Objetos extensibles del formato del lenguaje de Stylesheet</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">XSL-FO</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">langage XSL (Extensible Stylesheet )Formatting Objects</desc>
          <desc versionDate="2007-11-06" xml:lang="it">linguaggio XSL-FO.</desc>
        </valItem>
        <valItem ident="free">
          <desc versionDate="2012-10-06" xml:lang="en">Informal free text description</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">격식이 자유로운 텍스트 기술</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Descripción informal y libre del texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">自由記述。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">description en texte libre non structuré.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">descrizione informale testo libero.</desc>
        </valItem>
        <valItem ident="other">
          <desc versionDate="2012-10-06" xml:lang="en">A user-defined rendition description language</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">사용자 정의 해석 기술 언어</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Un idioma descriptivo de interpretación definido por el usario.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">利用者が決めた、描出記述言語。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">langue de description de l'interprétation définie par l'utilisateur</desc>
          <desc versionDate="2007-11-06" xml:lang="it">linguaggio di descrizione della resa definito dall'utente</desc>
        </valItem>
      </valList>
      <remarks ident="att.styleDef-attr.scheme-remarks" versionDate="2013-04-11" xml:lang="en">
        <p>If no value for the @scheme attribute is provided, then the default assumption should be that CSS is in use.</p>
      </remarks>
    </attDef>
    <attDef ident="schemeVersion" usage="opt">
      <desc versionDate="2013-04-12" xml:lang="en">supplies a version number for the style language provided in <att>scheme</att>.</desc>
      <datatype><dataRef key="teidata.versionNumber"/></datatype>
      <constraintSpec ident="schemeVersionRequiresScheme" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@schemeVersion]">
            <sch:assert test="@scheme and not(@scheme eq 'free')">
              @schemeVersion can only be used if @scheme is specified.
            </sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <remarks ident="att.styleDef-attr.schemeVersion-remarks" versionDate="2013-04-12" xml:lang="en">
        <p>If <att>schemeVersion</att> is used, then <att>scheme</att> should also appear, with a value
          other than <val>free</val>.</p>
      </remarks>
    </attDef>
  </attList>
</classSpec>

```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2015-02-15" xml:lang="en">provides attributes to specify the name of a formal definition language used to provide formatting or rendition information.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-10-06" xml:lang="en">identifies the language used to describe the rendition.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">모양을 기술하는 언어를 식별한다.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">identifica el lenguaje usado para describir la interpretación.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該描出を解説する言語を特定する。</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">identifie la langue employée pour décrire le rendu.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">identifica la lingua utilizzata per descrivere la resa</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="css">
          <desc versionDate="2012-10-06" xml:lang="en">Cascading Stylesheet Language</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">연속식 스타일시트 언어</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Lenguaje de CSS</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">CSS</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">langage CSS (Cascading Stylesheet )</desc>
          <desc versionDate="2007-11-06" xml:lang="it">linguaggio CSS.</desc>
        </valItem>
        <valItem ident="xslfo">
          <desc versionDate="2012-10-06" xml:lang="en">Extensible Stylesheet Language Formatting Objects</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">확장가능 스타일시트 언어</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Objetos extensibles del formato del lenguaje de Stylesheet</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">XSL-FO</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">langage XSL (Extensible Stylesheet )Formatting Objects</desc>
          <desc versionDate="2007-11-06" xml:lang="it">linguaggio XSL-FO.</desc>
        </valItem>
        <valItem ident="free">
          <desc versionDate="2012-10-06" xml:lang="en">Informal free text description</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">격식이 자유로운 텍스트 기술</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Descripción informal y libre del texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">自由記述。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">description en texte libre non structuré.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">descrizione informale testo libero.</desc>
        </valItem>
        <valItem ident="other">
          <desc versionDate="2012-10-06" xml:lang="en">A user-defined rendition description language</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">사용자 정의 해석 기술 언어</desc>
          <desc versionDate="2008-04-06" xml:lang="es">Un idioma descriptivo de interpretación definido por el usario.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">利用者が決めた、描出記述言語。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">langue de description de l'interprétation définie par l'utilisateur</desc>
          <desc versionDate="2007-11-06" xml:lang="it">linguaggio di descrizione della resa definito dall'utente</desc>
        </valItem>
      </valList>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.styleDef-attr.scheme-remarks" versionDate="2013-04-11" xml:lang="en">
        <p>If no value for the @scheme attribute is provided, then the default assumption should be that CSS is in use.</p>
      </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-04-12" xml:lang="en">supplies a version number for the style language provided in <att>scheme</att>.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.versionNumber"/></datatype>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[2]/constraintSpec[1]`.

```xml
<constraintSpec ident="schemeVersionRequiresScheme" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:*[@schemeVersion]">
            <sch:assert test="@scheme and not(@scheme eq 'free')">
              @schemeVersion can only be used if @scheme is specified.
            </sch:assert>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="att.styleDef-attr.schemeVersion-remarks" versionDate="2013-04-12" xml:lang="en">
        <p>If <att>schemeVersion</att> is used, then <att>scheme</att> should also appear, with a value
          other than <val>free</val>.</p>
      </remarks>
```

^b14

