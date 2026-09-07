---
type: representation
source-type: document
source: '[[00_sources/tei-p5-editorialdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 editorialDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/editorialDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# editorialDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4583. Git blob: `1471401c9e79158118cc9b616395e640ecbc6d6b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-editorialDecl" ident="editorialDecl">
  <gloss versionDate="2005-01-14" xml:lang="en">editorial practice declaration</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">déclaration des pratiques éditoriales</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">편집 실행 선언</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">編輯實行宣告</gloss>
    <gloss versionDate="2016-11-17" xml:lang="de">Angabe der Editionsprinzipien</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de la edición</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulle pratiche editoriali</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides details of editorial principles and practices applied
during the encoding of a text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">donne des précisions sur les pratiques et  les principes éditoriaux appliqués au cours de l’encodage du texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 부호화에서 적용된 편집 원리 및 기준의 상세 항목을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供文件編碼時使用的編輯原則與實行方法的細節。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストを符号化する際に適用される編集方針や編集方法の詳細を示す。</desc>
    <desc versionDate="2006-10-18" xml:lang="de">beschreibt die Details der Editionsprinzipien und Verfahren, die bei der Kodierung des Textes angewandt wurden.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona detalles de principios editoriales y prácticas aplicadas en la codificación de un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce dettagli su principi e pratiche editoriali seguite nella codifica di un testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.pLike"/>
      <classRef key="model.editorialDeclPart"/>
    </alternate>
  </content>
  <constraintSpec ident="editorialDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:editorialDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editorialDecl-egXML-be">
      <editorialDecl>
        <normalization>
          <p>All words converted to Modern American spelling using
 Websters 9th Collegiate dictionary
  </p>
        </normalization>
        <quotation marks="all">
          <p>All opening quotation marks converted to “ all closing
 quotation marks converted to &amp;cdq;.</p>
        </quotation>
      </editorialDecl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editorialDecl-egXML-xq">
      <editorialDecl>
        <normalization>
          <p>Certains mots coupés par accident typographique en fin de ligne ont été réassemblés
              sans commentaire.</p>
        </normalization>
        <quotation marks="all">
          <p>Les "guillements français" ont été remplacée par des "guillemets droits" (sans
              symétrie)</p>
        </quotation>
      </editorialDecl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editorialDecl-egXML-bz">
      <editorialDecl>
        <normalization>
          <p> 所有字皆轉換為源自Websters 9th Collegiate字典的現代美語拼法</p>
        </normalization>
        <quotation marks="all">
          <p>所有的前括號都改成" 後括號都改成 "</p>
        </quotation>
      </editorialDecl>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD53"/>
    <ptr target="#HD5"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">editorial practice declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">déclaration des pratiques éditoriales</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">편집 실행 선언</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">編輯實行宣告</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Angabe der Editionsprinzipien</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de la edición</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulle pratiche editoriali</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides details of editorial principles and practices applied
during the encoding of a text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">donne des précisions sur les pratiques et  les principes éditoriaux appliqués au cours de l’encodage du texte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 부호화에서 적용된 편집 원리 및 기준의 상세 항목을 제시한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供文件編碼時使用的編輯原則與實行方法的細節。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストを符号化する際に適用される編集方針や編集方法の詳細を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">beschreibt die Details der Editionsprinzipien und Verfahren, die bei der Kodierung des Textes angewandt wurden.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona detalles de principios editoriales y prácticas aplicadas en la codificación de un texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce dettagli su principi e pratiche editoriali seguite nella codifica di un testo.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.pLike"/>
      <classRef key="model.editorialDeclPart"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="editorialDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:editorialDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editorialDecl-egXML-be">
      <editorialDecl>
        <normalization>
          <p>All words converted to Modern American spelling using
 Websters 9th Collegiate dictionary
  </p>
        </normalization>
        <quotation marks="all">
          <p>All opening quotation marks converted to “ all closing
 quotation marks converted to &amp;cdq;.</p>
        </quotation>
      </editorialDecl>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editorialDecl-egXML-xq">
      <editorialDecl>
        <normalization>
          <p>Certains mots coupés par accident typographique en fin de ligne ont été réassemblés
              sans commentaire.</p>
        </normalization>
        <quotation marks="all">
          <p>Les "guillements français" ont été remplacée par des "guillemets droits" (sans
              symétrie)</p>
        </quotation>
      </editorialDecl>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-editorialDecl-egXML-bz">
      <editorialDecl>
        <normalization>
          <p> 所有字皆轉換為源自Websters 9th Collegiate字典的現代美語拼法</p>
        </normalization>
        <quotation marks="all">
          <p>所有的前括號都改成" 後括號都改成 "</p>
        </quotation>
      </editorialDecl>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
    <ptr target="#HD5"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b22

