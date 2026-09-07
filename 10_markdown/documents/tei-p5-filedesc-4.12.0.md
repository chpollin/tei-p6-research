---
type: representation
source-type: document
source: '[[00_sources/tei-p5-filedesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fileDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fileDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fileDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7025. Git blob: `2b7b396954c75c1180f3987978d8fa8a5c049a9f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-fileDesc" ident="fileDesc">
  <gloss versionDate="2007-07-05" xml:lang="en">file description</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">description bibliographique du fichier</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">파일 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">檔案描述</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Dateibeschreibung</gloss>
  <gloss versionDate="2021-10-15" xml:lang="es">Descripción del archivo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione del file</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a full bibliographic description of an electronic file.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient une description bibliographique complète du
    fichier électronique.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전자 파일에 관한 완전한 서지 정보의 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含對電子檔案的完整書目敘述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">電子ファイルに関する完全な書誌情報を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">enthält die vollständige bibliografische Beschreibung einer elektronischen Datei.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción bibliográfica completa del archivo electrónico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione bibliografica completa di un
    file elettronico.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      <sequence>
        <elementRef key="titleStmt"/>
        
          <elementRef key="editionStmt" minOccurs="0"/>
        
        
          <elementRef key="extent" minOccurs="0"/>
        
        <elementRef key="publicationStmt"/>
        
          <elementRef key="seriesStmt" minOccurs="0" maxOccurs="unbounded"/>
        
        
          <elementRef key="notesStmt" minOccurs="0"/>
        
      </sequence>
      
        <elementRef key="sourceDesc" minOccurs="1" maxOccurs="unbounded"/>
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fileDesc-egXML-vp">
      <fileDesc>
        <titleStmt>
          <title>The shortest possible TEI document</title>
        </titleStmt>
        <publicationStmt>
          <p>Distributed as part of TEI P5</p>
        </publicationStmt>
        <sourceDesc>
          <p>No print source exists: this is an original digital text</p>
        </sourceDesc>
      </fileDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fileDesc-egXML-qs">
      <teiHeader>
        <fileDesc>
          <titleStmt>
            <title>Le document TEI minimal</title>
          </titleStmt>
          <publicationStmt>
            <p>Distribué comme partie de TEI P5</p>
          </publicationStmt>
          <sourceDesc>
            <p>Aucune source : ce document est né numérique</p>
          </sourceDesc>
        </fileDesc>
      </teiHeader>
    </egXML>
  </exemplum>
  <remarks ident="fileDesc-remarks" versionDate="2008-02-01" xml:lang="en">
    <p>The major source of information for those seeking to create a catalogue entry or
      bibliographic citation for an electronic file. As such, it provides a title and statements of
      responsibility together with details of the publication or distribution of the file, of any
      series to which it belongs, and detailed bibliographic notes for matters not addressed
      elsewhere in the header. It also contains a full bibliographic description for the source or
      sources from which the electronic text was derived.</p>
  </remarks>
  <remarks ident="fileDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est la source d'information principale pour créer une notice  de catalogage ou
      une référence bibliographique destinée à un fichier électronique. Il fournit le titre et les
      mentions de responsabilité, ainsi que des informations sur la publication ou la distribution
      du fichier, sur la collection à laquelle il appartient le cas échéant,  ainsi que des notes
      détaillées sur des informations qui n'apparaissent pas ailleurs dans l'en-tête. Il contient
      également une description bibliographique complète de la ou des sources du texte produit.</p>
  </remarks>
  <remarks ident="fileDesc-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>La fuente de información principal para intentar crear una entrada de catálogo o una citación
      bibliográfica para un fichero electrónico. Como tal, proporciona un título y las declaraciones
      de responsabilidad junto con los detalles de la publicación o de la distribución del fichero,
      de cualquier serie a la que pertenezca, y las notas bibliográficas detalladas de las materias
      no abordadas en el encabezado. También contiene una descripción bibliográfica completa para la
      fuente o las fuentes de las cuales el texto electrónico se deriva.</p>
  </remarks>
  <remarks ident="fileDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 電子ファイルの書誌項目または書誌引用を示す中心となるもの。 タイトル、当該ファイルの出版や頒布に関連する責任表示、他には記述さ
      れいない書誌情報に関する詳細な事項を含む。また、当該電子ファイルの 元になった、元資料に関する完全な書誌情報も示す。 </p>
  </remarks>
  <remarks ident="fileDesc-remarks" versionDate="2017-06-04" xml:lang="de">
      <p>Die wesentliche Informationsquelle für die Erstellung eines Katalogeintrags oder eines bibliografischen 
          Zitats einer elektronischen Datei. Das Element liefert einen Titel und Angaben zu Verantwortlichkeiten 
          zusammen mit Details zu Publikation und Distribution der Datei, sowie eine mögliche Zugehörigkeit zu einer Reihe. 
          Außerdem kann es detaillierte bibliografische Anmerkungen für Sachverhalte, die an keiner anderen Stelle im TEI-Header 
          behandelt werden können, enthalten. Es beinhaltet außerdem eine vollständige bibliografische Beschreibung der 
          Quelle selbst bzw. der Quellen von welchen sich der elektronische Text ableitet.</p>
  </remarks>
  <listRef>
    <ptr target="#HD2"/>
    <ptr target="#HD11"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-05" xml:lang="en">file description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">description bibliographique du fichier</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">파일 기술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">檔案描述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Dateibeschreibung</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2021-10-15" xml:lang="es">Descripción del archivo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione del file</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a full bibliographic description of an electronic file.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient une description bibliographique complète du
    fichier électronique.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전자 파일에 관한 완전한 서지 정보의 기술을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含對電子檔案的完整書目敘述。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">電子ファイルに関する完全な書誌情報を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">enthält die vollständige bibliografische Beschreibung einer elektronischen Datei.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción bibliográfica completa del archivo electrónico.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione bibliografica completa di un
    file elettronico.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <sequence>
        <elementRef key="titleStmt"/>
        
          <elementRef key="editionStmt" minOccurs="0"/>
        
        
          <elementRef key="extent" minOccurs="0"/>
        
        <elementRef key="publicationStmt"/>
        
          <elementRef key="seriesStmt" minOccurs="0" maxOccurs="unbounded"/>
        
        
          <elementRef key="notesStmt" minOccurs="0"/>
        
      </sequence>
      
        <elementRef key="sourceDesc" minOccurs="1" maxOccurs="unbounded"/>
      
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fileDesc-egXML-vp">
      <fileDesc>
        <titleStmt>
          <title>The shortest possible TEI document</title>
        </titleStmt>
        <publicationStmt>
          <p>Distributed as part of TEI P5</p>
        </publicationStmt>
        <sourceDesc>
          <p>No print source exists: this is an original digital text</p>
        </sourceDesc>
      </fileDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fileDesc-egXML-qs">
      <teiHeader>
        <fileDesc>
          <titleStmt>
            <title>Le document TEI minimal</title>
          </titleStmt>
          <publicationStmt>
            <p>Distribué comme partie de TEI P5</p>
          </publicationStmt>
          <sourceDesc>
            <p>Aucune source : ce document est né numérique</p>
          </sourceDesc>
        </fileDesc>
      </teiHeader>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="fileDesc-remarks" versionDate="2008-02-01" xml:lang="en">
    <p>The major source of information for those seeking to create a catalogue entry or
      bibliographic citation for an electronic file. As such, it provides a title and statements of
      responsibility together with details of the publication or distribution of the file, of any
      series to which it belongs, and detailed bibliographic notes for matters not addressed
      elsewhere in the header. It also contains a full bibliographic description for the source or
      sources from which the electronic text was derived.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="fileDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est la source d'information principale pour créer une notice  de catalogage ou
      une référence bibliographique destinée à un fichier électronique. Il fournit le titre et les
      mentions de responsabilité, ainsi que des informations sur la publication ou la distribution
      du fichier, sur la collection à laquelle il appartient le cas échéant,  ainsi que des notes
      détaillées sur des informations qui n'apparaissent pas ailleurs dans l'en-tête. Il contient
      également une description bibliographique complète de la ou des sources du texte produit.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="fileDesc-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>La fuente de información principal para intentar crear una entrada de catálogo o una citación
      bibliográfica para un fichero electrónico. Como tal, proporciona un título y las declaraciones
      de responsabilidad junto con los detalles de la publicación o de la distribución del fichero,
      de cualquier serie a la que pertenezca, y las notas bibliográficas detalladas de las materias
      no abordadas en el encabezado. También contiene una descripción bibliográfica completa para la
      fuente o las fuentes de las cuales el texto electrónico se deriva.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="fileDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 電子ファイルの書誌項目または書誌引用を示す中心となるもの。 タイトル、当該ファイルの出版や頒布に関連する責任表示、他には記述さ
      れいない書誌情報に関する詳細な事項を含む。また、当該電子ファイルの 元になった、元資料に関する完全な書誌情報も示す。 </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="fileDesc-remarks" versionDate="2017-06-04" xml:lang="de">
      <p>Die wesentliche Informationsquelle für die Erstellung eines Katalogeintrags oder eines bibliografischen 
          Zitats einer elektronischen Datei. Das Element liefert einen Titel und Angaben zu Verantwortlichkeiten 
          zusammen mit Details zu Publikation und Distribution der Datei, sowie eine mögliche Zugehörigkeit zu einer Reihe. 
          Außerdem kann es detaillierte bibliografische Anmerkungen für Sachverhalte, die an keiner anderen Stelle im TEI-Header 
          behandelt werden können, enthalten. Es beinhaltet außerdem eine vollständige bibliografische Beschreibung der 
          Quelle selbst bzw. der Quellen von welchen sich der elektronische Text ableitet.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD2"/>
    <ptr target="#HD11"/>
  </listRef>
```

^b25

