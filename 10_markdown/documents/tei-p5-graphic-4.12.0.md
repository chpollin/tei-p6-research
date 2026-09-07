---
type: representation
source-type: document
source: '[[00_sources/tei-p5-graphic-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 graphic
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/graphic.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# graphic

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7854. Git blob: `bd4146583403de58e05305da84432fb8dfe2ade6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="GRAPHIC" ident="graphic">
  <gloss versionDate="2016-11-29" xml:lang="en">graphic</gloss>
  <gloss versionDate="2016-11-29" xml:lang="de">Abbildung</gloss>
  <desc versionDate="2016-03-07" xml:lang="en">indicates the location of a graphic or illustration, either forming
    part of a text, or providing an image of it.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">인라인 그래픽, 삽화, 또는 도형의 위치를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出文字文件中內含的圖形、插圖、或圖表的位置。</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">テキスト列中にある図、絵、図表の場所を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">indique l'emplacement d'une image, d'une illustration ou
    d'un schéma intégrés.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la localización de un gráfico, ilustración o
    figura.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica la posizione di un grafico, di una illustrazione o
    immagine.</desc>
  <desc versionDate="2016-11-29" xml:lang="de">gibt den Ort einer Bildressource an, 
    die entweder Teil eines Texts oder ein Abbild dessen ist.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.media"/>
    <memberOf key="att.resourced"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.graphicLike"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>   
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-xi">
      <figure>
        <graphic url="fig1.png"/>
        <head>Figure One: The View from the Bridge</head>
        <figDesc>A Whistleresque view showing four or five sailing boats in the foreground, and a
          series of buoys strung out between them.</figDesc>
      </figure>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-st" source="#fr-ex-Huizinga_Aut">
      <figure>
        <graphic url="fig1.png"/>
        <head>Figure Une : Jan van Eyck, La Vierge du chancelier Rolin</head>
        <p>Si, attiré par la curiosité, on a l'imprudence de l'approcher d'un peu trop prés, c'est fini, on est pris pour tout le temps que peut durer l'effort d'une attention soutenue ; on s'extasie devant la finesse du détail ...    il va toujours plus loin, franchit une à une les croupes des collines verdoyantes ; se  repose un moment sur une ligne lointaine de montagnes neigeuses; pour se perdre ensuite   dans l'infini d'un ciel à peine bleu, où s'estompent de flottantes nuées. </p>
      </figure>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-kq" source="#biblzh-tw_n5">
      <figure>
        <graphic url="fig1.png"/>
        <head>維納斯</head>
        <figDesc> 波提且利 1484-1486年 畫布、蛋彩 佛羅倫斯，烏菲滋美術館</figDesc>
      </figure>
    </egXML>
  </exemplum>
  <exemplum versionDate="2016-03-07" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-wf" xml:lang="und" source="#UND">
      <facsimile>
        <surfaceGrp n="leaf1">
          <surface>
            <graphic url="page1.png"/>
          </surface>
          <surface>
            <graphic url="page2-highRes.png"/>
            <graphic url="page2-lowRes.png"/>
          </surface>
        </surfaceGrp>
      </facsimile>
    </egXML>
  </exemplum>
  <exemplum versionDate="2022-04-08" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-sh" xml:lang="und" source="#UND">
      <facsimile>
        <surfaceGrp n="leaf1" xml:id="spi001">
          <surface xml:id="spi001r">
            <graphic type="normal" subtype="thumbnail" url="spi/thumb/001r.jpg"/>
            <graphic type="normal" subtype="low-res" url="spi/normal/lowRes/001r.jpg"/>
            <graphic type="normal" subtype="high-res" url="spi/normal/highRes/001r.jpg"/>
            <graphic type="high-contrast" subtype="low-res" url="spi/contrast/lowRes/001r.jpg"/>
            <graphic type="high-contrast" subtype="high-res" url="spi/contrast/highRes/001r.jpg"/>
          </surface>
          <surface xml:id="spi001v">
            <graphic type="normal" subtype="thumbnail" url="spi/thumb/001v.jpg"/>
            <graphic type="normal" subtype="low-res" url="spi/normal/lowRes/001v.jpg"/>
            <graphic type="normal" subtype="high-res" url="spi/normal/highRes/001v.jpg"/>
            <graphic type="high-contrast" subtype="low-res" url="spi/contrast/lowRes/001v.jpg"/>
            <graphic type="high-contrast" subtype="high-res" url="spi/contrast/highRes/001v.jpg"/>
            <zone xml:id="spi001v_detail01">
              <graphic type="normal" subtype="thumbnail" url="spi/thumb/001v-detail01.jpg"/>
              <graphic type="normal" subtype="low-res" url="spi/normal/lowRes/001v-detail01.jpg"/>
              <graphic type="normal" subtype="high-res" url="spi/normal/highRes/001v-detail01.jpg"/>
              <graphic type="high-contrast" subtype="low-res" url="spi/contrast/lowRes/001v-detail01.jpg"/>
              <graphic type="high-contrast" subtype="high-res" url="spi/contrast/highRes/001v-detail01.jpg"/>
            </zone>
          </surface>
        </surfaceGrp>
      </facsimile>
    </egXML>
  </exemplum>
  <remarks ident="graphic-remarks" versionDate="2016-03-07" xml:lang="en">
    <p>The <att>mimeType</att> attribute should be used to supply the MIME media type of the image
      specified by the <att>url</att> attribute.</p><p>Within the body of a text, a <gi>graphic</gi> element  indicates the 
      presence of a graphic component in the source itself. Within the context of a <gi>facsimile</gi> or <gi>sourceDoc</gi> element, however, 
      a <gi>graphic</gi> element provides an additional digital representation of some part of the source being encoded.
      </p>
  </remarks>
  <remarks ident="graphic-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>mimeType</att> doit être utilisé pour spécifier le type MIME de l'image
      référencée par l'attribut <att>url</att>.</p>
  </remarks>
  <remarks ident="graphic-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>mimeType</att>は、属性<att>url</att>が指定する画像のMIME タイプを示すために使われるべきである。 </p>
  </remarks>
  <remarks ident="graphic-remarks" versionDate="2016-11-29" xml:lang="de">
    <p>Das <att>mimeType</att>-Attribut sollte genutzt werden, um den MIME Medientyp des 
      über das <att>url</att>-Attributs spezifizierten Bildes anzugeben.
      Innerhalb des Textkörpers gibt das <gi>graphic</gi>-Element das Vorkommen eines Bildes 
      oder einer Illustration in der Textvorlage an. Innerhalb eines <gi>sourceDoc</gi>- 
      oder <gi>facsimile</gi>-Elements dagegen gibt das   <gi>graphic</gi>-Element eine 
      zusätzliche Repräsentation (eines Teils) der Vorlage wieder.</p>
  </remarks>
  <listRef>
    <ptr target="#COGR" type="div2"/>
    <ptr target="#PHFAX" type="div2"/>    
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2016-11-29" xml:lang="en">graphic</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2016-11-29" xml:lang="de">Abbildung</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-03-07" xml:lang="en">indicates the location of a graphic or illustration, either forming
    part of a text, or providing an image of it.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인라인 그래픽, 삽화, 또는 도형의 위치를 표시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出文字文件中內含的圖形、插圖、或圖表的位置。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">テキスト列中にある図、絵、図表の場所を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">indique l'emplacement d'une image, d'une illustration ou
    d'un schéma intégrés.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la localización de un gráfico, ilustración o
    figura.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la posizione di un grafico, di una illustrazione o
    immagine.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-29" xml:lang="de">gibt den Ort einer Bildressource an, 
    die entweder Teil eines Texts oder ein Abbild dessen ist.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.media"/>
    <memberOf key="att.resourced"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.graphicLike"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>   
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-xi">
      <figure>
        <graphic url="fig1.png"/>
        <head>Figure One: The View from the Bridge</head>
        <figDesc>A Whistleresque view showing four or five sailing boats in the foreground, and a
          series of buoys strung out between them.</figDesc>
      </figure>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-st" source="#fr-ex-Huizinga_Aut">
      <figure>
        <graphic url="fig1.png"/>
        <head>Figure Une : Jan van Eyck, La Vierge du chancelier Rolin</head>
        <p>Si, attiré par la curiosité, on a l'imprudence de l'approcher d'un peu trop prés, c'est fini, on est pris pour tout le temps que peut durer l'effort d'une attention soutenue ; on s'extasie devant la finesse du détail ...    il va toujours plus loin, franchit une à une les croupes des collines verdoyantes ; se  repose un moment sur une ligne lointaine de montagnes neigeuses; pour se perdre ensuite   dans l'infini d'un ciel à peine bleu, où s'estompent de flottantes nuées. </p>
      </figure>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-kq" source="#biblzh-tw_n5">
      <figure>
        <graphic url="fig1.png"/>
        <head>維納斯</head>
        <figDesc> 波提且利 1484-1486年 畫布、蛋彩 佛羅倫斯，烏菲滋美術館</figDesc>
      </figure>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2016-03-07" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-wf" xml:lang="und" source="#UND">
      <facsimile>
        <surfaceGrp n="leaf1">
          <surface>
            <graphic url="page1.png"/>
          </surface>
          <surface>
            <graphic url="page2-highRes.png"/>
            <graphic url="page2-lowRes.png"/>
          </surface>
        </surfaceGrp>
      </facsimile>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum versionDate="2022-04-08" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="GRAPHIC-egXML-sh" xml:lang="und" source="#UND">
      <facsimile>
        <surfaceGrp n="leaf1" xml:id="spi001">
          <surface xml:id="spi001r">
            <graphic type="normal" subtype="thumbnail" url="spi/thumb/001r.jpg"/>
            <graphic type="normal" subtype="low-res" url="spi/normal/lowRes/001r.jpg"/>
            <graphic type="normal" subtype="high-res" url="spi/normal/highRes/001r.jpg"/>
            <graphic type="high-contrast" subtype="low-res" url="spi/contrast/lowRes/001r.jpg"/>
            <graphic type="high-contrast" subtype="high-res" url="spi/contrast/highRes/001r.jpg"/>
          </surface>
          <surface xml:id="spi001v">
            <graphic type="normal" subtype="thumbnail" url="spi/thumb/001v.jpg"/>
            <graphic type="normal" subtype="low-res" url="spi/normal/lowRes/001v.jpg"/>
            <graphic type="normal" subtype="high-res" url="spi/normal/highRes/001v.jpg"/>
            <graphic type="high-contrast" subtype="low-res" url="spi/contrast/lowRes/001v.jpg"/>
            <graphic type="high-contrast" subtype="high-res" url="spi/contrast/highRes/001v.jpg"/>
            <zone xml:id="spi001v_detail01">
              <graphic type="normal" subtype="thumbnail" url="spi/thumb/001v-detail01.jpg"/>
              <graphic type="normal" subtype="low-res" url="spi/normal/lowRes/001v-detail01.jpg"/>
              <graphic type="normal" subtype="high-res" url="spi/normal/highRes/001v-detail01.jpg"/>
              <graphic type="high-contrast" subtype="low-res" url="spi/contrast/lowRes/001v-detail01.jpg"/>
              <graphic type="high-contrast" subtype="high-res" url="spi/contrast/highRes/001v-detail01.jpg"/>
            </zone>
          </surface>
        </surfaceGrp>
      </facsimile>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="graphic-remarks" versionDate="2016-03-07" xml:lang="en">
    <p>The <att>mimeType</att> attribute should be used to supply the MIME media type of the image
      specified by the <att>url</att> attribute.</p><p>Within the body of a text, a <gi>graphic</gi> element  indicates the 
      presence of a graphic component in the source itself. Within the context of a <gi>facsimile</gi> or <gi>sourceDoc</gi> element, however, 
      a <gi>graphic</gi> element provides an additional digital representation of some part of the source being encoded.
      </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="graphic-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>mimeType</att> doit être utilisé pour spécifier le type MIME de l'image
      référencée par l'attribut <att>url</att>.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="graphic-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>mimeType</att>は、属性<att>url</att>が指定する画像のMIME タイプを示すために使われるべきである。 </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="graphic-remarks" versionDate="2016-11-29" xml:lang="de">
    <p>Das <att>mimeType</att>-Attribut sollte genutzt werden, um den MIME Medientyp des 
      über das <att>url</att>-Attributs spezifizierten Bildes anzugeben.
      Innerhalb des Textkörpers gibt das <gi>graphic</gi>-Element das Vorkommen eines Bildes 
      oder einer Illustration in der Textvorlage an. Innerhalb eines <gi>sourceDoc</gi>- 
      oder <gi>facsimile</gi>-Elements dagegen gibt das   <gi>graphic</gi>-Element eine 
      zusätzliche Repräsentation (eines Teils) der Vorlage wieder.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COGR" type="div2"/>
    <ptr target="#PHFAX" type="div2"/>    
  </listRef>
```

^b22

