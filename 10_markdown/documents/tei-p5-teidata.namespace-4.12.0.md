---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.namespace-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.namespace
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.namespace.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.namespace

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3237. Git blob: `36b50158d4dd95b81696139bb0e96cec02bbf71f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.namespace">
  <desc versionDate="2007-10-14" xml:lang="en">defines the range of attribute values used to indicate XML namespaces as defined by the W3C
    <ref target="https://www.w3.org/TR/1999/REC-xml-names-19990114/">Namespaces in XML</ref>
    Technical Recommendation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">W3C <ref target="https://www.w3.org/TR/1999/REC-xml-names-19990114/">Namespaces in XML</ref> 기술적 권고안에 의해
    정의된 XML 이름공간을 나타내는 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍指出XML名稱空間，由XML technical
    recommendation中的W3C名稱空間所定義。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">W3Cの<ref target="https://www.w3.org/TR/1999/REC-xml-names-19990114/">
    XML名前空間</ref>で定義されている名前空間を示す属性値の範囲を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant une espace de noms XML tels qu'ils
  sont définis par le
      W3C.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos usados para
    indicar los nombres de los espacios en XML como establecen las recomendaciones técnicas del W3C
    para los <ptr target="https://www.w3.org/TR/1999/REC-xml-names-19990114/"/></desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per
    indicare i nomi degli spazi in XML come stabilito dalle raccomandazioni tecniche del W3C per gli
    <ref target="https://www.w3.org/TR/1999/REC-xml-names-19990114/">spazi dei nomi in XML</ref>.</desc>
  <content>
      <dataRef restriction="\S+" name="anyURI"/>
   </content>
  <remarks ident="teidata.namespace-remarks" versionDate="2008-02-08" xml:lang="en">
      <p>The range of syntactically valid values is defined by <ref target="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986 <title>Uniform Resource Identifier
          (URI): Generic Syntax</title>
         </ref>
      </p>
  </remarks>
  <remarks ident="teidata.namespace-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> 当該データ値は、<ref target="https://www.ietf.org/rfc/rfc2396.txt">RFC 2396 <title>Uniform Resource
          Identifier (URI) Reference</title>
         </ref> に定義されている。 </p>
  </remarks>
  <remarks ident="teidata.namespace-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>La gamme des valeurs  syntaxiquement valides est définie par <ref target="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986 <title>Uniform Resource Identifier
          (URI): Generic Syntax</title>
         </ref>.</p>
      <!-- this ref should be in the TEI bibliog -->
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-14" xml:lang="en">defines the range of attribute values used to indicate XML namespaces as defined by the W3C
    <ref target="https://www.w3.org/TR/1999/REC-xml-names-19990114/">Namespaces in XML</ref>
    Technical Recommendation.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">W3C <ref target="https://www.w3.org/TR/1999/REC-xml-names-19990114/">Namespaces in XML</ref> 기술적 권고안에 의해
    정의된 XML 이름공간을 나타내는 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍指出XML名稱空間，由XML technical
    recommendation中的W3C名稱空間所定義。</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">W3Cの<ref target="https://www.w3.org/TR/1999/REC-xml-names-19990114/">
    XML名前空間</ref>で定義されている名前空間を示す属性値の範囲を示す。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des
  valeurs d'attributs exprimant une espace de noms XML tels qu'ils
  sont définis par le
      W3C.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos usados para
    indicar los nombres de los espacios en XML como establecen las recomendaciones técnicas del W3C
    para los <ptr target="https://www.w3.org/TR/1999/REC-xml-names-19990114/"/></desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per
    indicare i nomi degli spazi in XML come stabilito dalle raccomandazioni tecniche del W3C per gli
    <ref target="https://www.w3.org/TR/1999/REC-xml-names-19990114/">spazi dei nomi in XML</ref>.</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <dataRef restriction="\S+" name="anyURI"/>
   </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.namespace-remarks" versionDate="2008-02-08" xml:lang="en">
      <p>The range of syntactically valid values is defined by <ref target="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986 <title>Uniform Resource Identifier
          (URI): Generic Syntax</title>
         </ref>
      </p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.namespace-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> 当該データ値は、<ref target="https://www.ietf.org/rfc/rfc2396.txt">RFC 2396 <title>Uniform Resource
          Identifier (URI) Reference</title>
         </ref> に定義されている。 </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.namespace-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>La gamme des valeurs  syntaxiquement valides est définie par <ref target="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986 <title>Uniform Resource Identifier
          (URI): Generic Syntax</title>
         </ref>.</p>
      <!-- this ref should be in the TEI bibliog -->
  </remarks>
```

^b11

