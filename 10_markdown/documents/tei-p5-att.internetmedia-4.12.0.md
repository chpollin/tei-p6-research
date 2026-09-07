---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.internetmedia-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.internetMedia
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.internetMedia.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.internetMedia

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6336. Git blob: `68b3b81b77d2e5e3ebc472747533b9ee2248a290`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-internetMedia" ident="att.internetMedia">
  <desc versionDate="2007-10-18" xml:lang="en">provides attributes for specifying the type of a computer
  resource using a standard taxonomy.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준 분류법을 사용하는 컴퓨터 자원의 유형을 명시하는 속성을 제시한다.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">標準的な用語による計算機資源の種類を表す属性を示す。</desc>
  <desc versionDate="2009-05-27" xml:lang="fr">fournit des attributs pour spécifier le type de
ressource informatique selon une taxinomie normalisée.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">indica degli attributi che specificano il tipo di risorsa informatica utilizzando una tassonomia standard.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">atributos para registrar un periodo temporal normalizado</desc>
  <attList>
    <attDef ident="mimeType" usage="opt">
      <gloss versionDate="2007-07-02" xml:lang="en">MIME media type</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">MIME 매체 유형</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">Tipo de media del MIME</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">type de média MIME</gloss>
      <gloss versionDate="2022-05-09" xml:lang="ja">MIMEメディアタイプ</gloss>
      <desc versionDate="2007-06-14" xml:lang="en">specifies the applicable multimedia internet mail extension (MIME) media type.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">적용 가능한 다중매체 인터넷 메일 확장자(MIME) 매체 유형을 명시한다.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該データのMIMEタイプ。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">spécifie le type MIME (multipurpose internet mail extension) applicable.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">specifica il tipo MIME appropriato.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">El tipo de MIME</desc>
      <desc versionDate="2006-06-05" xml:lang="zh-TW">MIME協定種類</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <p>In this example <att>mimeType</att> is used to indicate that the URL points to a TEI XML file encoded in UTF-8.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-internetMedia-egXML-gr" source="#UND">
      <ref mimeType="application/tei+xml; charset=UTF-8" target="https://raw.githubusercontent.com/TEIC/TEI/dev/P5/Source/guidelines-en.xml"/>
    </egXML>
  </exemplum>
  <remarks ident="att.internetMedia-remarks" versionDate="2013-12-06" xml:lang="en">
    <p>This attribute class provides an attribute for describing a
    computer resource, typically available over the internet,
    using a value taken from a standard taxonomy. At present only a single
    taxonomy is supported, the Multipurpose Internet Mail Extensions
    (MIME) Media Type system. This typology of media types is
    defined by the Internet Engineering Task Force in <ref target="https://www.ietf.org/rfc/rfc2046.txt">RFC 2046</ref>. The
    <ref target="https://www.iana.org/assignments/media-types/">list of
    types</ref> is maintained by the Internet Assigned Numbers
    Authority (IANA). The <att>mimeType</att> attribute must have a value taken from this list.</p>
  </remarks>
  <remarks ident="att.internetMedia-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe d'attributs fournit des attributs pour décrire une ressource
                informatique, en général disponible sur internet, selon les taxinomies normalisées.
                Actuellement une seule taxinomie est reconnue : le système "Multipurpose Internet
                Mail Extensions Media Type". Ce système de typologie des types de média est définie
                par l'Internet Engineering Task Force dans<ref target="https://www.ietf.org/rfc/rfc2046.txt">RFC 2046</ref>. La <ref target="https://www.iana.org/assignments/media-types/">liste des types</ref>
                est maintenue par l'Internet Assigned Numbers Authority. </p>
  </remarks>
  <remarks ident="att.internetMedia-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta clase de atributo proporciona los atributos para describir un recurso del ordenador, típicamente disponibles en Internet, según las taxonomías estándar. Solamente una única taxonomía se utiliza actualmente, el sistema Multipurpose Internet Mail Extensions
    Media Type. Este sistema de tipología de los tipos de media es definido por el Internet Engineering Task Force <ref target="https://www.ietf.org/rfc/rfc2046.txt">RFC 2046</ref>. 
    . La <ref target="https://www.iana.org/assignments/media-types/">lista de tipos</ref> es mantenida por el Internet Assigned Numbers Authority.</p>
  </remarks>
  <remarks ident="att.internetMedia-remarks" versionDate="2022-05-09" xml:lang="ja">
    <p>
当該属性クラスは、コンピューターリソースを示すためのもので、通常、インターネット上にあるリソースを標準的な用語で示す。現時点では、MIME（Multipurpose Internet Mail Extensions）タイプのみが標準的な用語として使用可能である。このMIMEタイプについては、IETF（Internet Engineering Task Force）の<ref target="https://www.ietf.org/rfc/rfc2046.txt">RFC 2046</ref>で規定されている。<ref target="https://www.iana.org/assignments/media-types/">使用できるタイプ名のリスト</ref>の管理は、IANA（Internet Assigned Numbers Authority）によって行われている。<att>mimeType</att>属性は上記のタイプ名リストにより定義された値を含んでいなくてはならない。
    </p>
  </remarks>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">provides attributes for specifying the type of a computer
  resource using a standard taxonomy.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준 분류법을 사용하는 컴퓨터 자원의 유형을 명시하는 속성을 제시한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">標準的な用語による計算機資源の種類を表す属性を示す。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">fournit des attributs pour spécifier le type de
ressource informatique selon une taxinomie normalisée.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica degli attributi che specificano il tipo di risorsa informatica utilizzando una tassonomia standard.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">atributos para registrar un periodo temporal normalizado</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-02" xml:lang="en">MIME media type</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">MIME 매체 유형</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">Tipo de media del MIME</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">type de média MIME</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2022-05-09" xml:lang="ja">MIMEメディアタイプ</gloss>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-06-14" xml:lang="en">specifies the applicable multimedia internet mail extension (MIME) media type.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">적용 가능한 다중매체 인터넷 메일 확장자(MIME) 매체 유형을 명시한다.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該データのMIMEタイプ。</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">spécifie le type MIME (multipurpose internet mail extension) applicable.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">specifica il tipo MIME appropriato.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">El tipo de MIME</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2006-06-05" xml:lang="zh-TW">MIME協定種類</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b19

### Block 20

XML location: `/classSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>In this example <att>mimeType</att> is used to indicate that the URL points to a TEI XML file encoded in UTF-8.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-internetMedia-egXML-gr" source="#UND">
      <ref mimeType="application/tei+xml; charset=UTF-8" target="https://raw.githubusercontent.com/TEIC/TEI/dev/P5/Source/guidelines-en.xml"/>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.internetMedia-remarks" versionDate="2013-12-06" xml:lang="en">
    <p>This attribute class provides an attribute for describing a
    computer resource, typically available over the internet,
    using a value taken from a standard taxonomy. At present only a single
    taxonomy is supported, the Multipurpose Internet Mail Extensions
    (MIME) Media Type system. This typology of media types is
    defined by the Internet Engineering Task Force in <ref target="https://www.ietf.org/rfc/rfc2046.txt">RFC 2046</ref>. The
    <ref target="https://www.iana.org/assignments/media-types/">list of
    types</ref> is maintained by the Internet Assigned Numbers
    Authority (IANA). The <att>mimeType</att> attribute must have a value taken from this list.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.internetMedia-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe d'attributs fournit des attributs pour décrire une ressource
                informatique, en général disponible sur internet, selon les taxinomies normalisées.
                Actuellement une seule taxinomie est reconnue : le système "Multipurpose Internet
                Mail Extensions Media Type". Ce système de typologie des types de média est définie
                par l'Internet Engineering Task Force dans<ref target="https://www.ietf.org/rfc/rfc2046.txt">RFC 2046</ref>. La <ref target="https://www.iana.org/assignments/media-types/">liste des types</ref>
                est maintenue par l'Internet Assigned Numbers Authority. </p>
  </remarks>
```

^b22

### Block 23

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.internetMedia-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta clase de atributo proporciona los atributos para describir un recurso del ordenador, típicamente disponibles en Internet, según las taxonomías estándar. Solamente una única taxonomía se utiliza actualmente, el sistema Multipurpose Internet Mail Extensions
    Media Type. Este sistema de tipología de los tipos de media es definido por el Internet Engineering Task Force <ref target="https://www.ietf.org/rfc/rfc2046.txt">RFC 2046</ref>. 
    . La <ref target="https://www.iana.org/assignments/media-types/">lista de tipos</ref> es mantenida por el Internet Assigned Numbers Authority.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="att.internetMedia-remarks" versionDate="2022-05-09" xml:lang="ja">
    <p>
当該属性クラスは、コンピューターリソースを示すためのもので、通常、インターネット上にあるリソースを標準的な用語で示す。現時点では、MIME（Multipurpose Internet Mail Extensions）タイプのみが標準的な用語として使用可能である。このMIMEタイプについては、IETF（Internet Engineering Task Force）の<ref target="https://www.ietf.org/rfc/rfc2046.txt">RFC 2046</ref>で規定されている。<ref target="https://www.iana.org/assignments/media-types/">使用できるタイプ名のリスト</ref>の管理は、IANA（Internet Assigned Numbers Authority）によって行われている。<att>mimeType</att>属性は上記のタイプ名リストにより定義された値を含んでいなくてはならない。
    </p>
  </remarks>
```

^b24

