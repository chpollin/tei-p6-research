---
type: representation
source-type: document
source: '[[00_sources/tei-p5-figdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 figDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/figDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# figDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5148. Git blob: `b8d9612d18a00eb977f05b785b1dc6931e4008a8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="figures" xml:id="gi-figDesc" ident="figDesc">
  <gloss versionDate="2007-07-04" xml:lang="en">description of figure</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Beschreibung einer Abbildung</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">그림 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">圖表描述</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description d'une figure</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción de una figura</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">Descrizione di una figura</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a brief prose description of the appearance or content
of a graphic figure, for use when documenting an image without
displaying it.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"/>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含圖表內容的簡短文字描述，用於紀錄圖像但未呈現圖像的情況。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">図表の内容や現れ方について簡単な散文で解説を示す。当該図表を示さない
  で記録する場合に使用される。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une brève description de l'apparence ou
			du contenu d'une représentation graphique, pour documenter une image sans avoir à l'afficher.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una breve descripción de la apariencia o del contenido de una figura gráfica, para utilizarla al documentar una imagen sin mostrarla.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una breve descrizione dell'aspetto o del contenuto di una figura, da utilizzare quando si vuole documentare un'immagine senza mostrarla.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält einen kurzen Beschreibungstext des Inhalts oder des Aussehens einer Abbildung, um etwa
    ein Bild ohne dessen Anzeige dokumentieren zu können.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.limitedContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figDesc-egXML-nk">
      <figure>
        <graphic url="emblem1.png"/>
        <head>Emblemi d'Amore</head>
        <figDesc>A pair of  naked winged cupids, each holding a
	flaming torch, in a rural setting.</figDesc>
      </figure>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figDesc-egXML-ct">
      <figure>
        <graphic url="chap3fig2.png"/>
        <head>Dick Kennedy </head>
        <figDesc>Gravure de E. Riou représentant un jeune homme assis sur une chaise, les
                pieds sur une autre et tenant à la main une canne. En arrière plan, une théière, et
                l'inscription <q>Map of Africa</q> .</figDesc>
      </figure>
    </egXML>
  </exemplum>
  <remarks ident="figDesc-remarks" versionDate="2013-03-18" xml:lang="en">
    <p>This element is intended for use as an alternative to the
content of its parent <gi>figure</gi> element ; for example, to display
when the image is required but the equipment in use cannot display
graphic images. It may also be used for indexing or documentary
purposes.</p>
  </remarks>
  <remarks ident="figDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est prévu pour être utilisé comme alternative au contenu de son élément
                parent <gi>figure</gi>; par exemple, pour montrer que l'image est exigée mais que
               le matériel en service ne peut pas montrer des documents graphiques. Il peut également
                être employé pour l'indexation ou dans un but documentaire.</p>
  </remarks>
  <remarks ident="figDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p/>
    <p>
    当該要素は、要素<gi>figure</gi>の内容の代わりに使用されるものであ
    る。例えば、当該図表を表示する際に、機器がその表示に対応していない
    場合に使用されるものである。また、索引や記録資料を作成するために使
    用されるかもしれない。
    </p>
  </remarks>
  <remarks ident="figDesc-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Dieses Element ist als Ersatz für den Inhalt seines Elternelements <gi>figure</gi> gedacht. Zum
      Beispiel wenn das Bild nicht angezeigt werden kann und man auf einen Alternativtext angewiesen
      ist. Es kann weiters für Indexierungen und Dokumentationen benutzt werden.</p>
  </remarks>
  <listRef>
    <ptr target="#FTGRA" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">description of figure</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Beschreibung einer Abbildung</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">그림 기술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">圖表描述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description d'une figure</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción de una figura</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">Descrizione di una figura</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a brief prose description of the appearance or content
of a graphic figure, for use when documenting an image without
displaying it.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"/>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含圖表內容的簡短文字描述，用於紀錄圖像但未呈現圖像的情況。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">図表の内容や現れ方について簡単な散文で解説を示す。当該図表を示さない
  で記録する場合に使用される。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une brève description de l'apparence ou
			du contenu d'une représentation graphique, pour documenter une image sans avoir à l'afficher.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una breve descripción de la apariencia o del contenido de una figura gráfica, para utilizarla al documentar una imagen sin mostrarla.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una breve descrizione dell'aspetto o del contenuto di una figura, da utilizzare quando si vuole documentare un'immagine senza mostrarla.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält einen kurzen Beschreibungstext des Inhalts oder des Aussehens einer Abbildung, um etwa
    ein Bild ohne dessen Anzeige dokumentieren zu können.</desc>
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
    <macroRef key="macro.limitedContent"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figDesc-egXML-nk">
      <figure>
        <graphic url="emblem1.png"/>
        <head>Emblemi d'Amore</head>
        <figDesc>A pair of  naked winged cupids, each holding a
	flaming torch, in a rural setting.</figDesc>
      </figure>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-figDesc-egXML-ct">
      <figure>
        <graphic url="chap3fig2.png"/>
        <head>Dick Kennedy </head>
        <figDesc>Gravure de E. Riou représentant un jeune homme assis sur une chaise, les
                pieds sur une autre et tenant à la main une canne. En arrière plan, une théière, et
                l'inscription <q>Map of Africa</q> .</figDesc>
      </figure>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="figDesc-remarks" versionDate="2013-03-18" xml:lang="en">
    <p>This element is intended for use as an alternative to the
content of its parent <gi>figure</gi> element ; for example, to display
when the image is required but the equipment in use cannot display
graphic images. It may also be used for indexing or documentary
purposes.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="figDesc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est prévu pour être utilisé comme alternative au contenu de son élément
                parent <gi>figure</gi>; par exemple, pour montrer que l'image est exigée mais que
               le matériel en service ne peut pas montrer des documents graphiques. Il peut également
                être employé pour l'indexation ou dans un but documentaire.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="figDesc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p/>
    <p>
    当該要素は、要素<gi>figure</gi>の内容の代わりに使用されるものであ
    る。例えば、当該図表を表示する際に、機器がその表示に対応していない
    場合に使用されるものである。また、索引や記録資料を作成するために使
    用されるかもしれない。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="figDesc-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Dieses Element ist als Ersatz für den Inhalt seines Elternelements <gi>figure</gi> gedacht. Zum
      Beispiel wenn das Bild nicht angezeigt werden kann und man auf einen Alternativtext angewiesen
      ist. Es kann weiters für Indexierungen und Dokumentationen benutzt werden.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FTGRA" type="div2"/>
  </listRef>
```

^b24

