---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.witnessed-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.witnessed
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.witnessed.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.witnessed

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4496. Git blob: `09c79dc9485fcf5fec3561c06d8eff27357c4574`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" type="atts" ident="att.witnessed">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes used to identify the witnesses
  supporting a particular reading in a critical apparatus.</desc>
  <classes/>
  <attList>
    <attDef ident="wit" usage="opt">
      <gloss versionDate="2012-04-18" xml:lang="en">witness or witnesses</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">testimonio o testimonios</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">témoin ou témoins</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">testimone o testimoni</gloss>
      <desc versionDate="2013-12-09" xml:lang="en">contains a space-delimited list of one or more pointers indicating the witnesses
which attest to a given reading.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">제시된 독법을 증명하는 비교 대상 텍스트를 나타내는 하나 이상의 포인터 목록을 포함한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個或多個指標的一份列表，連結到已知對應本的版本。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該解釈を証す文献を示す1つ以上のポインタのリストを示す。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">contient une liste comprenant un ou plusieurs pointeurs qui désignent
					les témoins attestant d'une leçon donnée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">contiene una lista de uno o más indicadores que muestran los testimonios que presentan una determinada lectura.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">contiene una lista di uno o più puntatori indicanti i testimoni che attestano una determinata lettura.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.witnessed-attr.wit-remarks" versionDate="2012-04-18" xml:lang="en">
        <p>If the apparatus contains readings only for a single
witness, this attribute may be consistently omitted.</p>
        <p>This attribute may occur both within an apparatus
gathering variant readings in the transcription of an individual
witness and within an apparatus gathering readings from different
witnesses.</p>
        <p>Additional descriptions or alternative versions of the sigla referenced may be
supplied as the content of a child <gi>wit</gi> element.</p>
      </remarks>
      <remarks ident="att.witnessed-attr.wit-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si l'apparat ne contient que des leçons relatives à un seul témoin, cet attribut peut être systématiquement omis. </p>
        <p>Cet attribut peut figurer à la fois dans un apparat qui réunit des variantes de leçons dans la transcription d'un témoin isolé et à l'intérieur d'un apparat qui réunit des leçons provenant de différents témoins.</p>
        <p>On peut donner des descriptions supplémentaires ou des versions alternatives d'abréviations référencées de témoins comme contenu d'un élément enfant <gi>wit</gi>.</p>
      </remarks>
      <remarks ident="att.witnessed-attr.wit-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該校勘資料中で、1つの現存資料に複数の解釈が含まれている場合、
        当該属性は常に省略されるかもしれない。
        </p>
        <p>
        当該属性は、ひとつの文献からの転記に対する各種の解釈を集めた校
        勘資料中で使用されるかもしれない。また、複数の文献中における各
        種の解釈を集めた校勘資料中でも使用されるかもしれない。
        </p>
        <p>
        当該文献記号の追加的な記述や他の版に関する情報は、子要素
        <gi>wit</gi>の内容として示されるかもしれない。
        </p>
      </remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes used to identify the witnesses
  supporting a particular reading in a critical apparatus.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes/>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2012-04-18" xml:lang="en">witness or witnesses</gloss>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">testimonio o testimonios</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">témoin ou témoins</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">testimone o testimoni</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-09" xml:lang="en">contains a space-delimited list of one or more pointers indicating the witnesses
which attest to a given reading.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">제시된 독법을 증명하는 비교 대상 텍스트를 나타내는 하나 이상의 포인터 목록을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個或多個指標的一份列表，連結到已知對應本的版本。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該解釈を証す文献を示す1つ以上のポインタのリストを示す。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">contient une liste comprenant un ou plusieurs pointeurs qui désignent
					les témoins attestant d'une leçon donnée.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una lista de uno o más indicadores que muestran los testimonios que presentan una determinada lectura.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una lista di uno o più puntatori indicanti i testimoni che attestano una determinata lettura.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.witnessed-attr.wit-remarks" versionDate="2012-04-18" xml:lang="en">
        <p>If the apparatus contains readings only for a single
witness, this attribute may be consistently omitted.</p>
        <p>This attribute may occur both within an apparatus
gathering variant readings in the transcription of an individual
witness and within an apparatus gathering readings from different
witnesses.</p>
        <p>Additional descriptions or alternative versions of the sigla referenced may be
supplied as the content of a child <gi>wit</gi> element.</p>
      </remarks>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.witnessed-attr.wit-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si l'apparat ne contient que des leçons relatives à un seul témoin, cet attribut peut être systématiquement omis. </p>
        <p>Cet attribut peut figurer à la fois dans un apparat qui réunit des variantes de leçons dans la transcription d'un témoin isolé et à l'intérieur d'un apparat qui réunit des leçons provenant de différents témoins.</p>
        <p>On peut donner des descriptions supplémentaires ou des versions alternatives d'abréviations référencées de témoins comme contenu d'un élément enfant <gi>wit</gi>.</p>
      </remarks>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.witnessed-attr.wit-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該校勘資料中で、1つの現存資料に複数の解釈が含まれている場合、
        当該属性は常に省略されるかもしれない。
        </p>
        <p>
        当該属性は、ひとつの文献からの転記に対する各種の解釈を集めた校
        勘資料中で使用されるかもしれない。また、複数の文献中における各
        種の解釈を集めた校勘資料中でも使用されるかもしれない。
        </p>
        <p>
        当該文献記号の追加的な記述や他の版に関する情報は、子要素
        <gi>wit</gi>の内容として示されるかもしれない。
        </p>
      </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b19

