---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.creferencing-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.cReferencing
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.cReferencing.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.cReferencing

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4818. Git blob: `3c8d3f1ac336356b61b8089fe8c01914452d96c3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.cReferencing">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes that may be used to supply a
  <term>canonical reference</term> as a means of identifying the
  target of a pointer.</desc>
  <desc versionDate="2018-12-31" xml:lang="ja">ポインタのターゲットを識別する手段として<term>canonical reference</term>を提供するために使用される属性を提供する。</desc>
  <attList>
    <attDef ident="cRef">
      <gloss versionDate="2012-09-23" xml:lang="en">canonical reference</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">표준 참조</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">referencia canónica</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">référence canonique</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">riferimento canonico</gloss>
      <gloss versionDate="2022-08-26" xml:lang="ja">基準的形式の参照</gloss>
      <desc versionDate="2013-11-22" xml:lang="en">specifies the destination of the pointer by supplying a canonical reference expressed using the
        scheme defined in a <gi>refsDecl</gi> element in the TEI header.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">TEI 헤더의 <gi>refsDecl</gi> 요소에서 정의된 체계의 표준 참조를 이용하여
        포인터의 목적지를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用元素<gi>refsDecl</gi>在TEI標頭內所定義的標準參照來說明指標所指位置。</desc>
      <desc versionDate="2022-08-26" xml:lang="ja">TEIヘダー内の要素<gi>refsDecl</gi>で定義されているスキームにある、基準的参照形式により、当該ポインタの参照場所を示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">précise la cible du pointeur en fournissant une
        référence canonique issue d'un modèle défini par un élément <gi>refsDecl</gi>dans l'En-tête
        TEI.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la destinación de un señalizador
        proporcionando una referencia canónica de un esquema definido en un elemento
        <gi>refsDecl</gi> en el encabezado TEI.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica la destinazione di un puntatore usando un
        riferimento canonico a partire da uno schema definito in un elemento <gi>refsDecl</gi>
        nell'intestazione TEI</desc>
      <datatype maxOccurs="1"><dataRef key="teidata.text"/></datatype>
          <remarks ident="att.cReferencing-attr.cRef-remarks" versionDate="2012-09-23" xml:lang="en">
        <p>The value of <att>cRef</att> should be constructed so
      that when the algorithm for the resolution of canonical
      references (described in section <ptr target="#SACR"/>) is
      applied to it the result is a valid URI reference to the
      intended target.</p>
<p>The <gi>refsDecl</gi> to use may be indicated with the <att>decls</att> attribute.</p>
        <p>Currently these Guidelines only provide for a single canonical reference to be encoded on
          any given <gi>ptr</gi> element.</p>
      </remarks>
      <remarks ident="att.cReferencing-attr.cRef-remarks" versionDate="2007-06-12" xml:lang="fr">
<p>Le résultat de l’application de l'algorithme pour la résolution des
        références canoniques (décrit à la section <ptr target="#SACR"/>). Ce sera une référence URI
        valide pour la cible prévue.</p>        <p>La <gi>refsDecl</gi> à utiliser peut être indiquée à l'aide
        de l'attribut <att>decls</att>.  Actuellement ces Principes
        directeurs ne permettent que l'encodage d'une unique référence
        canonique pour tout élément <gi>ptr</gi> donné.</p>
      </remarks>

      <remarks ident="att.cReferencing-attr.cRef-remarks" versionDate="2018-12-31" xml:lang="ja"><p><ptr target="#SACR"/> 節での正規化参照を解決するためのアルゴリズムが適用される時にその結果が対象への正しいURI参照となるように、 <att>cRef</att> の値は作られるべきである</p> <p> <gi>refsDecl</gi> は <att>decls</att> 属性とともに示されてもよい。現行のガイドラインが <gi>ptr</gi> 要素に渡すのは、単一の符号化された正規化参照のみである。</p></remarks>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes that may be used to supply a
  <term>canonical reference</term> as a means of identifying the
  target of a pointer.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2018-12-31" xml:lang="ja">ポインタのターゲットを識別する手段として<term>canonical reference</term>を提供するために使用される属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2012-09-23" xml:lang="en">canonical reference</gloss>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">표준 참조</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">referencia canónica</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">référence canonique</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">riferimento canonico</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2022-08-26" xml:lang="ja">基準的形式の参照</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-11-22" xml:lang="en">specifies the destination of the pointer by supplying a canonical reference expressed using the
        scheme defined in a <gi>refsDecl</gi> element in the TEI header.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">TEI 헤더의 <gi>refsDecl</gi> 요소에서 정의된 체계의 표준 참조를 이용하여
        포인터의 목적지를 명시한다.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用元素<gi>refsDecl</gi>在TEI標頭內所定義的標準參照來說明指標所指位置。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2022-08-26" xml:lang="ja">TEIヘダー内の要素<gi>refsDecl</gi>で定義されているスキームにある、基準的参照形式により、当該ポインタの参照場所を示す。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">précise la cible du pointeur en fournissant une
        référence canonique issue d'un modèle défini par un élément <gi>refsDecl</gi>dans l'En-tête
        TEI.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la destinación de un señalizador
        proporcionando una referencia canónica de un esquema definido en un elemento
        <gi>refsDecl</gi> en el encabezado TEI.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica la destinazione di un puntatore usando un
        riferimento canonico a partire da uno schema definito in un elemento <gi>refsDecl</gi>
        nell'intestazione TEI</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="1"><dataRef key="teidata.text"/></datatype>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.cReferencing-attr.cRef-remarks" versionDate="2012-09-23" xml:lang="en">
        <p>The value of <att>cRef</att> should be constructed so
      that when the algorithm for the resolution of canonical
      references (described in section <ptr target="#SACR"/>) is
      applied to it the result is a valid URI reference to the
      intended target.</p>
<p>The <gi>refsDecl</gi> to use may be indicated with the <att>decls</att> attribute.</p>
        <p>Currently these Guidelines only provide for a single canonical reference to be encoded on
          any given <gi>ptr</gi> element.</p>
      </remarks>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.cReferencing-attr.cRef-remarks" versionDate="2007-06-12" xml:lang="fr">
<p>Le résultat de l’application de l'algorithme pour la résolution des
        références canoniques (décrit à la section <ptr target="#SACR"/>). Ce sera une référence URI
        valide pour la cible prévue.</p>        <p>La <gi>refsDecl</gi> à utiliser peut être indiquée à l'aide
        de l'attribut <att>decls</att>.  Actuellement ces Principes
        directeurs ne permettent que l'encodage d'une unique référence
        canonique pour tout élément <gi>ptr</gi> donné.</p>
      </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.cReferencing-attr.cRef-remarks" versionDate="2018-12-31" xml:lang="ja"><p><ptr target="#SACR"/> 節での正規化参照を解決するためのアルゴリズムが適用される時にその結果が対象への正しいURI参照となるように、 <att>cRef</att> の値は作られるべきである</p> <p> <gi>refsDecl</gi> は <att>decls</att> 属性とともに示されてもよい。現行のガイドラインが <gi>ptr</gi> 要素に渡すのは、単一の符号化された正規化参照のみである。</p></remarks>
```

^b19

