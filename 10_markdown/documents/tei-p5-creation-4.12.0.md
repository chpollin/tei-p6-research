---
type: representation
source-type: document
source: '[[00_sources/tei-p5-creation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 creation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/creation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# creation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5964. Git blob: `220a00c152454bc78ac4265fb59a665eaebf193f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-creation" ident="creation">
  <gloss versionDate="2007-06-12" xml:lang="en">creation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">création</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Entstehung</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains information about the creation of a text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient des informations concernant la création d’un texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 생성에 관한 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含關於文件建置的資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストの作成に関する情報を示す。</desc>
  <desc versionDate="2016-11-17" xml:lang="de">beinhaltet Informationen zur Entstehung eines Textes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene información sobre la creación del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni riguardanti la creazione di un testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.limitedPhrase"/>
      <elementRef key="listChange"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-kd">
      <creation>
        <date>Before 1987</date>
      </creation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-ju">
      <creation>
        <date>Avant 1987</date>
      </creation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-qv">
      <creation>
        <date when="1988-07-10">10 Juillet 1988</date>
      </creation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-bu">
      <creation>
        <date>1987年之前</date>
      </creation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-av">
      <creation>
        <date when="1988-07-10">1988年7月10日</date>
      </creation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-vk">
      <creation>
        <date when="1988-07-10">10 July 1988</date>
      </creation>
    </egXML>
  </exemplum>
  <remarks ident="creation-remarks" versionDate="2011-10-31" xml:lang="en">
    <p>The <gi>creation</gi> element may be used to record details of
    a text's creation, e.g. the date and place it was composed, if
    these are of interest.</p>
    <p>It may also contain a more structured account of the various
    stages or revisions associated with the evolution of a text; this
    should be encoded using the <gi>listChange</gi> element.  It
    should not be confused with the <gi>publicationStmt</gi> element,
    which records date and place of publication.</p>
  </remarks>
  <remarks ident="creation-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L’élément <gi>creation</gi> peut être utilisé pour détailler  des éléments concernant l’origine du
      texte, c’est-à-dire sa date et son  lieu de composition ; on ne doit pas le confondre avec
      l'élément <gi>publicationStmt</gi> qui contient la date et le lieu de publication.</p>
  </remarks>
  <remarks ident="creation-remarks" versionDate="2008-04-06" xml:lang="es">
    <p> El elemento <gi>creación</gi> se puede utilizar para registrar los detalles de la creación
      de un texto, p.ej. la fecha y el lugar en el que fue compuesto, si éstos son de interés; no
      debe ser confundido con el elemento <gi>publicationStmt</gi>, que registra la fecha y el lugar
      de la publicación.</p>
  </remarks>
  <remarks ident="creation-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p><gi>creation</gi>要素はテキストが作成された詳細、たとえば時間や場所などの記録に使用できる。
      <gi>listChange</gi>要素を用いてテキストの発展段階や修正についての構造的情報を含んでもよい。
      刊行時・刊行地を記録する<gi>publicationStmt</gi>要素と混同しないように。 </p>
  </remarks>
  <remarks ident="creation-remarks" versionDate="2016-11-17" xml:lang="de">
      <p rend="dataDesc">
          Das <gi>creation</gi>-Element kann dafür verwendet werden, Einzelheiten über die Entstehung eines Textes, 
          z. B. Entstehungszeit und Entstehungsort, zu dokumentieren, wenn diese von Interesse sind. </p>
          <p>Es kann auch eine mehr oder weniger strukturierte Entstehungsgeschichte mit den einzelnen Bearbeitungs- und Revisionstufen 
          enthalten; diese sollten mithilfe des <gi>listChange</gi>-Elements ausgezeichnet werden. Das <gi>creation</gi>-Element darf 
          aber nicht mit dem <gi>publicationStmt</gi>-Element, das Zeit und Ort der Veröffentlichung verzeichnet, verwechselt werden.
      </p>
  </remarks>
  <listRef>
    <ptr target="#HD4C"/>
    <ptr target="#HD4"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">creation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">création</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Entstehung</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains information about the creation of a text.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient des informations concernant la création d’un texte.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 생성에 관한 정보를 포함한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含關於文件建置的資訊。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストの作成に関する情報を示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">beinhaltet Informationen zur Entstehung eines Textes.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene información sobre la creación del texto.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni riguardanti la creazione di un testo.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.limitedPhrase"/>
      <elementRef key="listChange"/>
    </alternate>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-kd">
      <creation>
        <date>Before 1987</date>
      </creation>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-ju">
      <creation>
        <date>Avant 1987</date>
      </creation>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-qv">
      <creation>
        <date when="1988-07-10">10 Juillet 1988</date>
      </creation>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-bu">
      <creation>
        <date>1987年之前</date>
      </creation>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-av">
      <creation>
        <date when="1988-07-10">1988年7月10日</date>
      </creation>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-creation-egXML-vk">
      <creation>
        <date when="1988-07-10">10 July 1988</date>
      </creation>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="creation-remarks" versionDate="2011-10-31" xml:lang="en">
    <p>The <gi>creation</gi> element may be used to record details of
    a text's creation, e.g. the date and place it was composed, if
    these are of interest.</p>
    <p>It may also contain a more structured account of the various
    stages or revisions associated with the evolution of a text; this
    should be encoded using the <gi>listChange</gi> element.  It
    should not be confused with the <gi>publicationStmt</gi> element,
    which records date and place of publication.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="creation-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L’élément <gi>creation</gi> peut être utilisé pour détailler  des éléments concernant l’origine du
      texte, c’est-à-dire sa date et son  lieu de composition ; on ne doit pas le confondre avec
      l'élément <gi>publicationStmt</gi> qui contient la date et le lieu de publication.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="creation-remarks" versionDate="2008-04-06" xml:lang="es">
    <p> El elemento <gi>creación</gi> se puede utilizar para registrar los detalles de la creación
      de un texto, p.ej. la fecha y el lugar en el que fue compuesto, si éstos son de interés; no
      debe ser confundido con el elemento <gi>publicationStmt</gi>, que registra la fecha y el lugar
      de la publicación.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="creation-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p><gi>creation</gi>要素はテキストが作成された詳細、たとえば時間や場所などの記録に使用できる。
      <gi>listChange</gi>要素を用いてテキストの発展段階や修正についての構造的情報を含んでもよい。
      刊行時・刊行地を記録する<gi>publicationStmt</gi>要素と混同しないように。 </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="creation-remarks" versionDate="2016-11-17" xml:lang="de">
      <p rend="dataDesc">
          Das <gi>creation</gi>-Element kann dafür verwendet werden, Einzelheiten über die Entstehung eines Textes, 
          z. B. Entstehungszeit und Entstehungsort, zu dokumentieren, wenn diese von Interesse sind. </p>
          <p>Es kann auch eine mehr oder weniger strukturierte Entstehungsgeschichte mit den einzelnen Bearbeitungs- und Revisionstufen 
          enthalten; diese sollten mithilfe des <gi>listChange</gi>-Elements ausgezeichnet werden. Das <gi>creation</gi>-Element darf 
          aber nicht mit dem <gi>publicationStmt</gi>-Element, das Zeit und Ort der Veröffentlichung verzeichnet, verwechselt werden.
      </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD4C"/>
    <ptr target="#HD4"/>
  </listRef>
```

^b25

