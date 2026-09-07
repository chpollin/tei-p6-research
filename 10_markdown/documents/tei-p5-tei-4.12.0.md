---
type: representation
source-type: document
source: '[[00_sources/tei-p5-tei-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 TEI
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/TEI.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# TEI

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12986. Git blob: `30a91d9e8610f20c8b8e4974b3749dd5cd0d5b56`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="textstructure" xml:id="gi-TEI" ident="TEI">
  <gloss versionDate="2005-12-24" xml:lang="en">TEI document</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">TEI 문서</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">TEI文件</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">document TEI</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">TEI-Dokument</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">documento TEI</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">documento TEI</gloss>
  <gloss versionDate="2018-12-17" xml:lang="ja">TEI文書</gloss>
  <desc versionDate="2019-06-27" xml:lang="en">contains a single TEI-conformant document, combining
    a single TEI header with one or more members of the <ident type="class">model.resource</ident> class. Multiple <gi>TEI</gi>
    elements may be combined within a <gi>TEI</gi> (or <gi>teiCorpus</gi>) element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">TEI 헤더와 텍스트로 구성된 단일 TEI 구조 문서를 포함한다. 독립 요소 또는 <gi>teiCorpus</gi> 요소의 부분.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含符合TEI標準的單一文件，由一個TEI標頭及一份文本組成，可單獨出現或是作為元素<gi>teiCorpus</gi>的一部分。</desc>
  <desc versionDate="2018-12-17" xml:lang="ja">一つ以上の<ident type="class">model.resource</ident>クラスを持つ一つのTEIヘッダを持つ、単一のTEI準拠文書を含む。<gi>teiCorpus</gi>エレメントには複数の<gi>TEI</gi>要素が含まれてもよい。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un seul document conforme à la TEI, qui
            comprend un en-tête TEI et un texte, soit de façon isolée, soit comme  partie d’un
            élément <gi>teiCorpus</gi>.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält ein einzelnes TEI-konformes Dokument, das aus einem einzigen TEI-Header und einem oder
    mehreren Mitgliedern der <ident type="class">model.resource</ident>-Klasse besteht. Mehrere
    <gi>TEI</gi>-Elemente können in einem <gi>teiCorpus</gi>-Element zusammengefasst werden.</desc>
  <desc versionDate="2022-06-02" xml:lang="es">contiene un solo documento conforme a la norma TEI, combinando un solo encabezado TEI (teiHeader) con uno o más miembros de la clase <ident type="class">model.resource</ident>. Múltiples elementos TEI se pueden combinar al interno de un elemento <gi>TEI</gi> o <gi>teiCorpus</gi>.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un documento TEI-conforme, comprendente un'intestazione e un testo, sia esso isolato o parte di un elemento <gi>teiCorpus</gi></desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.describedResource"/>
  </classes>
  <content>
    <!-- teiHeader, ( ( model.resource+, TEI* ) | TEI+ ) -->
    <sequence>
      <elementRef key="teiHeader"/>
      <alternate>
        <sequence>
          <classRef key="model.resource" minOccurs="1" maxOccurs="unbounded"/>
          <elementRef key="TEI" minOccurs="0" maxOccurs="unbounded"/>
        </sequence>
        <elementRef key="TEI" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="version" usage="opt">
      <desc versionDate="2018-01-24" xml:lang="en">specifies the version number of the TEI Guidelines against
      which this document is valid.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">TEI 스키마의 버전</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">TEI架構的版本</desc>
      <desc versionDate="2018-12-17" xml:lang="ja">当該文書が妥当（に符号化される）TEIスキームの版を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">la version majeure du schéma TEI.</desc>
      <desc versionDate="2018-07-18" xml:lang="de">gibt die Versionsnummer der TEI-Richtlinien an, gegen die dieses Dokument validiert wird.</desc>
      <desc versionDate="2022-05-02" xml:lang="es">especifica el número de versión de las Directrices TEI frente a las cuales este documento es válido.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">la versione dello schema TEI.</desc>
      <datatype><dataRef key="teidata.version"/></datatype>
      <remarks ident="TEI-attr.version-remarks" versionDate="2018-01-24" xml:lang="en">
        <p>Major editions of the Guidelines have long been informally referred to by a name made up
          of the letter P (for Proposal) followed by a digit. The current release is one of the many
          releases of the fifth major edition of the Guidelines, known as P5. This attribute may be 
          used to associate a TEI document with a specific release of the P5 Guidelines, in the absence 
          of a more precise association provided by the <att>source</att> attribute on the associated 
          <gi>schemaSpec</gi>.</p>
      </remarks>
      <remarks ident="TEI-attr.version-remarks" versionDate="2022-05-02" xml:lang="es"><p>Durante mucho tiempo, se ha hecho referencia informalmente a las principales ediciones de las Directrices con un nombre compuesto por la letra P (de Propuesta) seguida de un dígito. El lanzamiento actual es uno de los muchos lanzamientos de la quinta edición principal de las Directrices, conocida como P5. Este atributo puede utilizarse para asociar un documento TEI con una publicación específica de las Directrices P5, en ausencia de una asociación más precisa proporcionada por el atributo fuente en el <gi>schemaSpec</gi> asociado.</p></remarks>
      <remarks ident="TEI-attr.version-remarks" versionDate="2018-07-18" xml:lang="de">
        <p>Hauptausgaben der TEI-Richtlinien werden seit langem informell mit einem Namen bezeichnet, der sich aus dem Buchstaben P (für proposal) 
          und einer Ziffer zusammensetzt. Die aktuelle Ausgabe ist eine der vielen Ausgaben 
          der fünften Hauptausgabe der Richtlinien, bekannt als P5. Dieses Attribut kann dazu verwendet werden, 
          um ein TEI-Dokument einer bestimmten Version der P5-Richtlinien zuzuordnen, sofern keine genauere Zuordnung durch 
          das Attribut <att>source</att> im assoziierten <gi>schemaSpec</gi>-Element angegeben ist.</p>
      </remarks>
      <remarks ident="TEI-attr.version-remarks" versionDate="2018-12-17" xml:lang="ja">
        <p>ガイドラインのメジャーな版は、長い間、P（ProposalのP）と数字からなる名前で呼ばれてきました。このリリースは、P5と呼ばれる5番目のメジャーな版のなかの多くのリリースのひとつです。この属性は、<gi>schemaSpec</gi>の<att>source</att>属性によってより適切に関連づけられていない場合、任意のTEI文書を特定のP5ガイドラインのリリースと関連づけることができる。</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-TEI-egXML-ws" source="#NONE">
      <TEI version="3.3.0">
        <teiHeader>
          <fileDesc>
            <titleStmt>
              <title>The shortest TEI Document Imaginable</title>
            </titleStmt>
            <publicationStmt>
              <p>First published as part of TEI P2, this is the P5
              version using a namespace.</p>
            </publicationStmt>
            <sourceDesc>
              <p>No source: this is an original work.</p>
            </sourceDesc>
          </fileDesc>
        </teiHeader>
        <text>
          <body>
            <p>This is about the shortest TEI document imaginable.</p>
          </body>
        </text>
      </TEI>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-TEI-egXML-cy" source="#NONE">
      <TEI version="2.9.1">
        <teiHeader>
          <fileDesc>
            <titleStmt>
              <title>A TEI Document containing four page images </title>
            </titleStmt>
            <publicationStmt>
              <p>Unpublished demonstration file.</p>
            </publicationStmt>
            <sourceDesc>
              <p>No source: this is an original work.</p>
            </sourceDesc>
          </fileDesc>
        </teiHeader>
        <facsimile>
          <graphic url="page1.png"/>
          <graphic url="page2.png"/>
          <graphic url="page3.png"/>
          <graphic url="page4.png"/>
        </facsimile>
      </TEI>
    </egXML>
  </exemplum>

  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-TEI-egXML-gb" source="#NONE">
      <TEI version="3.3.0">
        <teiHeader>
          <fileDesc>
            <titleStmt>
              <title>Le document TEI le plus court possible.</title>
            </titleStmt>
            <publicationStmt>
              <p>D'abord publié comme faisant partie de la TEI P2.</p>
            </publicationStmt>
            <sourceDesc>
              <p>Aucune source : il s'agit d'un document original.</p>
            </sourceDesc>
          </fileDesc>
        </teiHeader>
        <text>
          <body>
            <p>A peu pres, le document TEI le plus court envisageable.</p>
          </body>
        </text>
      </TEI>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" source="#NONE" xml:id="gi-TEI-egXML-sb">
      <TEI version="3.3.0">
        <teiHeader>
          <fileDesc>
            <titleStmt>
              <title>TEI中文指引</title>
            </titleStmt>
            <publicationStmt>
              <p>將與TEI 中文在地化計劃等文件一同出版</p>
            </publicationStmt>
            <sourceDesc>
              <p>譯自TEI P5 英文指引</p>
            </sourceDesc>
          </fileDesc>
        </teiHeader>
        <text>
          <body>
            <p>這是TEI P5的中文指引...</p>
          </body>
        </text>
      </TEI>
    </egXML>
  </exemplum>
  
    <remarks ident="TEI-remarks" versionDate="2024-12-10" xml:lang="en">
    <p>As with all elements in the TEI scheme (except <gi>egXML</gi>) this element is
     in the TEI namespace (see <ptr target="#SGname"/>). Thus, when it is used as the
     outermost element of a TEI document, it is necessary to specify the TEI namespace
     on it. This is customarily achieved by including <ident type="ns">http://www.tei-c.org/ns/1.0</ident> as the value of the XML namespace declaration (xmlns), without indicating a prefix,
     and then not using a prefix on TEI elements in the rest of the document. For example:
     <tag type="start">TEI version="4.8.1" xml:lang="it" xmlns="http://www.tei-c.org/ns/1.0"</tag>.</p>
   </remarks>
  <remarks ident="TEI-remarks" versionDate="2024-12-10" xml:lang="es">
    <p>Como todos los elementos en el esquema TEI (excepto <gi>egXML</gi>), este elemento se encuentra en el espacio de nombres (<foreign>namespace</foreign>) de TEI (cf. <ptr target="#SGname"/>). Por lo tanto, cuando se utiliza como el elemento más externo de un documento TEI, es necesario especificar el espacio de nombres de TEI en su interior. Esto se hace, normalmente, incluyendo <ident type="ns">http://www.tei-c.org/ns/1.0</ident> como valor de la declaración de espacio de nombres (xmlns) sin indicar un prefijo, y por lo tanto sin necesidad de utilizar un prefijo en los elementos TEI del resto del documento. Por ejemplo: <tag type="start">TEI version="4.8.1" xml:lang="it" xmlns="http://www.tei-c.org/ns/1.0"</tag>.</p></remarks>
  <remarks ident="TEI-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est obligatoire.</p>
  </remarks>
  <remarks ident="TEI-remarks" versionDate="2018-12-17" xml:lang="ja">
    <p>
      当該要素は必須であり、<att>xmlns</att> 属性を用いてTEIの名前空間 <code>http://www.tei-c.org/ns/1.0</code> を指定することになっている。
    </p>
  </remarks>
  <remarks ident="TEI-remarks" versionDate="2022-04-07" xml:lang="de">
    <p>Dieses Element ist obligatorisch. Es ist notwendig, 
      auch den TEI-Namensraum <ident type="ns">http://www.tei-c.org/ns/1.0</ident> anzugeben, z.B. 
      <tag type="start">TEI version="4.4.0" xml:lang="it" 
        xmlns="http://www.tei-c.org/ns/1.0"</tag>.</p>
  </remarks>
  <listRef>
    <ptr target="#DS"/>
    <ptr target="#CCDEF"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-12-24" xml:lang="en">TEI document</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">TEI 문서</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">TEI文件</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">document TEI</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">TEI-Dokument</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">documento TEI</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">documento TEI</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2018-12-17" xml:lang="ja">TEI文書</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-06-27" xml:lang="en">contains a single TEI-conformant document, combining
    a single TEI header with one or more members of the <ident type="class">model.resource</ident> class. Multiple <gi>TEI</gi>
    elements may be combined within a <gi>TEI</gi> (or <gi>teiCorpus</gi>) element.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">TEI 헤더와 텍스트로 구성된 단일 TEI 구조 문서를 포함한다. 독립 요소 또는 <gi>teiCorpus</gi> 요소의 부분.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含符合TEI標準的單一文件，由一個TEI標頭及一份文本組成，可單獨出現或是作為元素<gi>teiCorpus</gi>的一部分。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2018-12-17" xml:lang="ja">一つ以上の<ident type="class">model.resource</ident>クラスを持つ一つのTEIヘッダを持つ、単一のTEI準拠文書を含む。<gi>teiCorpus</gi>エレメントには複数の<gi>TEI</gi>要素が含まれてもよい。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un seul document conforme à la TEI, qui
            comprend un en-tête TEI et un texte, soit de façon isolée, soit comme  partie d’un
            élément <gi>teiCorpus</gi>.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält ein einzelnes TEI-konformes Dokument, das aus einem einzigen TEI-Header und einem oder
    mehreren Mitgliedern der <ident type="class">model.resource</ident>-Klasse besteht. Mehrere
    <gi>TEI</gi>-Elemente können in einem <gi>teiCorpus</gi>-Element zusammengefasst werden.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2022-06-02" xml:lang="es">contiene un solo documento conforme a la norma TEI, combinando un solo encabezado TEI (teiHeader) con uno o más miembros de la clase <ident type="class">model.resource</ident>. Múltiples elementos TEI se pueden combinar al interno de un elemento <gi>TEI</gi> o <gi>teiCorpus</gi>.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un documento TEI-conforme, comprendente un'intestazione e un testo, sia esso isolato o parte di un elemento <gi>teiCorpus</gi></desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.describedResource"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!-- teiHeader, ( ( model.resource+, TEI* ) | TEI+ ) -->
    <sequence>
      <elementRef key="teiHeader"/>
      <alternate>
        <sequence>
          <classRef key="model.resource" minOccurs="1" maxOccurs="unbounded"/>
          <elementRef key="TEI" minOccurs="0" maxOccurs="unbounded"/>
        </sequence>
        <elementRef key="TEI" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
    </sequence>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2018-01-24" xml:lang="en">specifies the version number of the TEI Guidelines against
      which this document is valid.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">TEI 스키마의 버전</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">TEI架構的版本</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2018-12-17" xml:lang="ja">当該文書が妥当（に符号化される）TEIスキームの版を示す。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">la version majeure du schéma TEI.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">gibt die Versionsnummer der TEI-Richtlinien an, gegen die dieses Dokument validiert wird.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2022-05-02" xml:lang="es">especifica el número de versión de las Directrices TEI frente a las cuales este documento es válido.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">la versione dello schema TEI.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.version"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="TEI-attr.version-remarks" versionDate="2018-01-24" xml:lang="en">
        <p>Major editions of the Guidelines have long been informally referred to by a name made up
          of the letter P (for Proposal) followed by a digit. The current release is one of the many
          releases of the fifth major edition of the Guidelines, known as P5. This attribute may be 
          used to associate a TEI document with a specific release of the P5 Guidelines, in the absence 
          of a more precise association provided by the <att>source</att> attribute on the associated 
          <gi>schemaSpec</gi>.</p>
      </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="TEI-attr.version-remarks" versionDate="2022-05-02" xml:lang="es"><p>Durante mucho tiempo, se ha hecho referencia informalmente a las principales ediciones de las Directrices con un nombre compuesto por la letra P (de Propuesta) seguida de un dígito. El lanzamiento actual es uno de los muchos lanzamientos de la quinta edición principal de las Directrices, conocida como P5. Este atributo puede utilizarse para asociar un documento TEI con una publicación específica de las Directrices P5, en ausencia de una asociación más precisa proporcionada por el atributo fuente en el <gi>schemaSpec</gi> asociado.</p></remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="TEI-attr.version-remarks" versionDate="2018-07-18" xml:lang="de">
        <p>Hauptausgaben der TEI-Richtlinien werden seit langem informell mit einem Namen bezeichnet, der sich aus dem Buchstaben P (für proposal) 
          und einer Ziffer zusammensetzt. Die aktuelle Ausgabe ist eine der vielen Ausgaben 
          der fünften Hauptausgabe der Richtlinien, bekannt als P5. Dieses Attribut kann dazu verwendet werden, 
          um ein TEI-Dokument einer bestimmten Version der P5-Richtlinien zuzuordnen, sofern keine genauere Zuordnung durch 
          das Attribut <att>source</att> im assoziierten <gi>schemaSpec</gi>-Element angegeben ist.</p>
      </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="TEI-attr.version-remarks" versionDate="2018-12-17" xml:lang="ja">
        <p>ガイドラインのメジャーな版は、長い間、P（ProposalのP）と数字からなる名前で呼ばれてきました。このリリースは、P5と呼ばれる5番目のメジャーな版のなかの多くのリリースのひとつです。この属性は、<gi>schemaSpec</gi>の<att>source</att>属性によってより適切に関連づけられていない場合、任意のTEI文書を特定のP5ガイドラインのリリースと関連づけることができる。</p>
      </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-TEI-egXML-ws" source="#NONE">
      <TEI version="3.3.0">
        <teiHeader>
          <fileDesc>
            <titleStmt>
              <title>The shortest TEI Document Imaginable</title>
            </titleStmt>
            <publicationStmt>
              <p>First published as part of TEI P2, this is the P5
              version using a namespace.</p>
            </publicationStmt>
            <sourceDesc>
              <p>No source: this is an original work.</p>
            </sourceDesc>
          </fileDesc>
        </teiHeader>
        <text>
          <body>
            <p>This is about the shortest TEI document imaginable.</p>
          </body>
        </text>
      </TEI>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-TEI-egXML-cy" source="#NONE">
      <TEI version="2.9.1">
        <teiHeader>
          <fileDesc>
            <titleStmt>
              <title>A TEI Document containing four page images </title>
            </titleStmt>
            <publicationStmt>
              <p>Unpublished demonstration file.</p>
            </publicationStmt>
            <sourceDesc>
              <p>No source: this is an original work.</p>
            </sourceDesc>
          </fileDesc>
        </teiHeader>
        <facsimile>
          <graphic url="page1.png"/>
          <graphic url="page2.png"/>
          <graphic url="page3.png"/>
          <graphic url="page4.png"/>
        </facsimile>
      </TEI>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-TEI-egXML-gb" source="#NONE">
      <TEI version="3.3.0">
        <teiHeader>
          <fileDesc>
            <titleStmt>
              <title>Le document TEI le plus court possible.</title>
            </titleStmt>
            <publicationStmt>
              <p>D'abord publié comme faisant partie de la TEI P2.</p>
            </publicationStmt>
            <sourceDesc>
              <p>Aucune source : il s'agit d'un document original.</p>
            </sourceDesc>
          </fileDesc>
        </teiHeader>
        <text>
          <body>
            <p>A peu pres, le document TEI le plus court envisageable.</p>
          </body>
        </text>
      </TEI>
    </egXML>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" source="#NONE" xml:id="gi-TEI-egXML-sb">
      <TEI version="3.3.0">
        <teiHeader>
          <fileDesc>
            <titleStmt>
              <title>TEI中文指引</title>
            </titleStmt>
            <publicationStmt>
              <p>將與TEI 中文在地化計劃等文件一同出版</p>
            </publicationStmt>
            <sourceDesc>
              <p>譯自TEI P5 英文指引</p>
            </sourceDesc>
          </fileDesc>
        </teiHeader>
        <text>
          <body>
            <p>這是TEI P5的中文指引...</p>
          </body>
        </text>
      </TEI>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="TEI-remarks" versionDate="2024-12-10" xml:lang="en">
    <p>As with all elements in the TEI scheme (except <gi>egXML</gi>) this element is
     in the TEI namespace (see <ptr target="#SGname"/>). Thus, when it is used as the
     outermost element of a TEI document, it is necessary to specify the TEI namespace
     on it. This is customarily achieved by including <ident type="ns">http://www.tei-c.org/ns/1.0</ident> as the value of the XML namespace declaration (xmlns), without indicating a prefix,
     and then not using a prefix on TEI elements in the rest of the document. For example:
     <tag type="start">TEI version="4.8.1" xml:lang="it" xmlns="http://www.tei-c.org/ns/1.0"</tag>.</p>
   </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="TEI-remarks" versionDate="2024-12-10" xml:lang="es">
    <p>Como todos los elementos en el esquema TEI (excepto <gi>egXML</gi>), este elemento se encuentra en el espacio de nombres (<foreign>namespace</foreign>) de TEI (cf. <ptr target="#SGname"/>). Por lo tanto, cuando se utiliza como el elemento más externo de un documento TEI, es necesario especificar el espacio de nombres de TEI en su interior. Esto se hace, normalmente, incluyendo <ident type="ns">http://www.tei-c.org/ns/1.0</ident> como valor de la declaración de espacio de nombres (xmlns) sin indicar un prefijo, y por lo tanto sin necesidad de utilizar un prefijo en los elementos TEI del resto del documento. Por ejemplo: <tag type="start">TEI version="4.8.1" xml:lang="it" xmlns="http://www.tei-c.org/ns/1.0"</tag>.</p></remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="TEI-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est obligatoire.</p>
  </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="TEI-remarks" versionDate="2018-12-17" xml:lang="ja">
    <p>
      当該要素は必須であり、<att>xmlns</att> 属性を用いてTEIの名前空間 <code>http://www.tei-c.org/ns/1.0</code> を指定することになっている。
    </p>
  </remarks>
```

^b39

### Block 40

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="TEI-remarks" versionDate="2022-04-07" xml:lang="de">
    <p>Dieses Element ist obligatorisch. Es ist notwendig, 
      auch den TEI-Namensraum <ident type="ns">http://www.tei-c.org/ns/1.0</ident> anzugeben, z.B. 
      <tag type="start">TEI version="4.4.0" xml:lang="it" 
        xmlns="http://www.tei-c.org/ns/1.0"</tag>.</p>
  </remarks>
```

^b40

### Block 41

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DS"/>
    <ptr target="#CCDEF"/>
  </listRef>
```

^b41

