---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.certainty-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.certainty
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.certainty.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.certainty

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3003. Git blob: `80861804a735bd3333d1c02ac85be9804f1546c8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.certainty">
  <desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values expressing a degree of certainty.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">확실성 정도를 표현하는 속성 값의 범위를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義表示正確度的屬性值範圍</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">確信度を示す属性値の程度を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attribut exprimant un degré de certitude.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos que exprimen un grado de certeza.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi che esprimono un grado di certezza.</desc>
  <content>
    <valList type="closed">
      <valItem ident="high"/>
      <valItem ident="medium"/>
      <valItem ident="low"/>
      <valItem ident="unknown"/>
    </valList>
  </content>
  <remarks ident="teidata.certainty-remarks" versionDate="2011-02-26" xml:lang="en">
    <p>Certainty may be expressed by one of the predefined symbolic values <val>high</val>,
    <val>medium</val>, or <val>low</val>. The value
    <val>unknown</val> should be used in cases where the encoder
    does not wish to assert an opinion about the matter. 
    <!--For a more precise indication, <ident type="datatype">teidata.probability</ident>, which provides
        an may be used instead or in addition.--></p>
  </remarks>
  <remarks ident="teidata.certainty-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>確信度は、予め定義された値<val>high</val>、<val>medium</val>、または<val>low</val>のいずれかで表現される。確信度に関して何らかの意見を表明することを望んでいない場合は、<val> unknown</val>という値が使用されるべきである。より正確な指標を望む場合は、<ident type="datatype">data.probability</ident>を先に挙げた値の代わりに、またはそれに加えて使用することができる。</p>
  </remarks>
  <remarks ident="teidata.certainty-remarks" versionDate="2009-05-25" xml:lang="fr">
    <p>Le degré de certitude peut être exprimé par l'une des valeurs symboliques prédéfinies
    <val>high</val>, <val>medium</val>, ou <val>low</val>. <!--Pour une indication précise, <ident type="datatype">data.probability</ident> peut être utilisé en remplacement ou en complément.--></p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">defines the range of attribute values expressing a degree of certainty.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">확실성 정도를 표현하는 속성 값의 범위를 정의한다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義表示正確度的屬性值範圍</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">確信度を示す属性値の程度を示す。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attribut exprimant un degré de certitude.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos que exprimen un grado de certeza.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori di attributi che esprimono un grado di certezza.</desc>
```

^b7

### Block 8

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <valList type="closed">
      <valItem ident="high"/>
      <valItem ident="medium"/>
      <valItem ident="low"/>
      <valItem ident="unknown"/>
    </valList>
  </content>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.certainty-remarks" versionDate="2011-02-26" xml:lang="en">
    <p>Certainty may be expressed by one of the predefined symbolic values <val>high</val>,
    <val>medium</val>, or <val>low</val>. The value
    <val>unknown</val> should be used in cases where the encoder
    does not wish to assert an opinion about the matter. 
    <!--For a more precise indication, <ident type="datatype">teidata.probability</ident>, which provides
        an may be used instead or in addition.--></p>
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.certainty-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p>確信度は、予め定義された値<val>high</val>、<val>medium</val>、または<val>low</val>のいずれかで表現される。確信度に関して何らかの意見を表明することを望んでいない場合は、<val> unknown</val>という値が使用されるべきである。より正確な指標を望む場合は、<ident type="datatype">data.probability</ident>を先に挙げた値の代わりに、またはそれに加えて使用することができる。</p>
  </remarks>
```

^b10

### Block 11

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.certainty-remarks" versionDate="2009-05-25" xml:lang="fr">
    <p>Le degré de certitude peut être exprimé par l'une des valeurs symboliques prédéfinies
    <val>high</val>, <val>medium</val>, ou <val>low</val>. <!--Pour une indication précise, <ident type="datatype">data.probability</ident> peut être utilisé en remplacement ou en complément.--></p>
  </remarks>
```

^b11

