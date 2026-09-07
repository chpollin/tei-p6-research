---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.pointer-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.pointer
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.pointer.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.pointer

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4013. Git blob: `85b1ea8548cea2a0607935a611d63b2c9f6b3f2e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.pointer">
  <desc versionDate="2013-01-19" xml:lang="en">defines the range of attribute values used to provide a single
  URI, absolute or relative, pointing to some other
resource, either within the current document or elsewhere.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">현 문서 또는 다른 곳 어디서든 다른 자원에 대한 단일 포인터를 제공하는 속성 값 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍提供單一指標，連結到其他位於目前文件或他處的資源</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">現在の文書や他の場所にあるなんらかの他の資源を指す単一の相対URIもしくは絶対URIを提供するために用いる属性値の範囲を定義する。</desc>
  <desc versionDate="2009-05-29" xml:lang="fr">définit la gamme des valeurs d'attributs utilisées
      pour fournir un pointeur URI unique sur une autre ressource, soit dans le document courant, soit
      dans un autre document.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una gama de valores de atributos usados para proporcionar un indicador de cualquier recurso, bien en el documento corriente o en otro.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per indicare un unico puntatore rispetto a qualsiasi altra risorsa all'interno del documento corrente o altrove.</desc>
  <content>
      <dataRef restriction="\S+" name="anyURI"/>
   </content>
  <remarks ident="teidata.pointer-remarks" versionDate="2011-12-12" xml:lang="en">
      <p>The range of syntactically valid values is defined by
    <ref target="https://www.ietf.org/rfc/rfc3986.txt"> RFC 3986</ref>
         <title>Uniform Resource Identifier (URI): Generic
    Syntax</title>. Note that the values themselves are encoded using
    <ref target="https://www.ietf.org/rfc/rfc3987.txt">RFC
    3987</ref> 
         <title>Internationalized Resource Identifiers</title> (IRIs) mapping
    to URIs. For example, <code>
    https://secure.wikimedia.org/wikipedia/en/wiki/%</code> is encoded
    as <code>https://secure.wikimedia.org/wikipedia/en/wiki/%25</code>
    while <code>http://موقع.وزارة-الاتصالات.مصر/</code> is encoded as
    <code>http://xn--4gbrim.xn----rmckbbajlc6dj7bxne2c.xn--wgbh1c/</code>
      </p>
  </remarks>
  <remarks ident="teidata.pointer-remarks" xml:lang="ja" versionDate="2024-08-08">
      <p>
        シンタクス上正しい値の範囲は<ref target="http://www.ietf.org/rfc/rfc3986.txt">RFC 3986</ref> <title>Uniform Resource Identifier (URI): Generic Syntax</title>で定義されている。値自体は<ref target="http://www.ietf.org/rfc/rfc3987.txt">RFC 3987</ref> <title>Internationalized Resource Identifiers</title> (IRIs)をURIにマッピングして符号化する。たとえば、<code>https://secure.wikimedia.org/wikipedia/en/wiki/%</code>は <code>https://secure.wikimedia.org/wikipedia/en/wiki/%25</code>と符号化され、<code>http://موقع.وزارة-الاتصالات.مصر/</code>は<code>http://xn--4gbrim.xn----rmckbbajlc6dj7bxne2c.xn--wgbh1c/</code>と符号化される。
    </p>
  </remarks>
  <remarks ident="teidata.pointer-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>La gamme des valeurs valides syntaxiquement est définie par<ref target="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986
      <title>Uniform Resource Identifier (URI): Generic
        Syntax</title>
         </ref>
      </p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-01-19" xml:lang="en">defines the range of attribute values used to provide a single
  URI, absolute or relative, pointing to some other
resource, either within the current document or elsewhere.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 문서 또는 다른 곳 어디서든 다른 자원에 대한 단일 포인터를 제공하는 속성 값 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義的屬性值範圍提供單一指標，連結到其他位於目前文件或他處的資源</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">現在の文書や他の場所にあるなんらかの他の資源を指す単一の相対URIもしくは絶対URIを提供するために用いる属性値の範囲を定義する。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-29" xml:lang="fr">définit la gamme des valeurs d'attributs utilisées
      pour fournir un pointeur URI unique sur une autre ressource, soit dans le document courant, soit
      dans un autre document.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una gama de valores de atributos usados para proporcionar un indicador de cualquier recurso, bien en el documento corriente o en otro.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi usati per indicare un unico puntatore rispetto a qualsiasi altra risorsa all'interno del documento corrente o altrove.</desc>
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
<remarks ident="teidata.pointer-remarks" versionDate="2011-12-12" xml:lang="en">
      <p>The range of syntactically valid values is defined by
    <ref target="https://www.ietf.org/rfc/rfc3986.txt"> RFC 3986</ref>
         <title>Uniform Resource Identifier (URI): Generic
    Syntax</title>. Note that the values themselves are encoded using
    <ref target="https://www.ietf.org/rfc/rfc3987.txt">RFC
    3987</ref> 
         <title>Internationalized Resource Identifiers</title> (IRIs) mapping
    to URIs. For example, <code>
    https://secure.wikimedia.org/wikipedia/en/wiki/%</code> is encoded
    as <code>https://secure.wikimedia.org/wikipedia/en/wiki/%25</code>
    while <code>http://موقع.وزارة-الاتصالات.مصر/</code> is encoded as
    <code>http://xn--4gbrim.xn----rmckbbajlc6dj7bxne2c.xn--wgbh1c/</code>
      </p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.pointer-remarks" xml:lang="ja" versionDate="2024-08-08">
      <p>
        シンタクス上正しい値の範囲は<ref target="http://www.ietf.org/rfc/rfc3986.txt">RFC 3986</ref> <title>Uniform Resource Identifier (URI): Generic Syntax</title>で定義されている。値自体は<ref target="http://www.ietf.org/rfc/rfc3987.txt">RFC 3987</ref> <title>Internationalized Resource Identifiers</title> (IRIs)をURIにマッピングして符号化する。たとえば、<code>https://secure.wikimedia.org/wikipedia/en/wiki/%</code>は <code>https://secure.wikimedia.org/wikipedia/en/wiki/%25</code>と符号化され、<code>http://موقع.وزارة-الاتصالات.مصر/</code>は<code>http://xn--4gbrim.xn----rmckbbajlc6dj7bxne2c.xn--wgbh1c/</code>と符号化される。
    </p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.pointer-remarks" versionDate="2009-05-25" xml:lang="fr">
      <p>La gamme des valeurs valides syntaxiquement est définie par<ref target="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986
      <title>Uniform Resource Identifier (URI): Generic
        Syntax</title>
         </ref>
      </p>
  </remarks>
```

^b11

