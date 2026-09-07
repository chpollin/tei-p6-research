---
type: representation
source-type: document
source: '[[00_sources/tei-p5-binding-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 binding
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/binding.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# binding

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11798. Git blob: `56a39f35980d310de62bb9318c3cded384fd58e3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="BINDING" ident="binding">
  <gloss versionDate="2007-06-12" xml:lang="en">binding</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">reliure</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="binding.desc">contains a description of one binding, i.e. type of covering, boards, etc. applied to a manuscript or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 제본에 대한 기술을 포함한다. 즉, 원고에 적용된 커버, 표지 등의 유형</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">一個裝訂的描述，例如使用於該手稿的封面類型、封面等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">1つの装訂に関する情報を示す。例えば、手書き資料でいうカバーの種類、 表紙など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description d'une reliure, i.e. du type de couverture, d'ais, etc., rencontrés.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la descripción de una encuadernación, p.ej. tipo de cubiertas, tablas, etc. presentes en un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la descrizione di una legatura, cioè del tipo di copertine, tavole, ecc. utilizzate per il manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.pLike"/>
      <elementRef key="condition"/>
      <elementRef key="decoNote"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="contemporary">
      <gloss versionDate="2007-06-12" xml:lang="en">contemporary</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">contemporaine</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">specifies whether or not the binding is contemporary with the majority of its
        contents.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">제본이 텍스트의 대부분 내용과 동시에 이루어졌는가의 여부를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明裝訂和其大部分內容是否出於同一時期。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該装訂が、当該内容の大部分と同年代のものかどうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie si la reliure est contemporaine ou non de
        l'essentiel du contenu du manuscrit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica si la encuardenación es coetánea o no a la
        mayoría del contenido del manuscrito.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica se la legatura è coeva o meno rispetto alla
        maggior parte del suo contenuto</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <remarks ident="binding-attr.contemporary-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the binding is contemporaneous with its
          contents; the value <val>false</val> that it is not. The value <val>unknown</val> should
          be used when the date of either binding or manuscript is unknown</p>
      </remarks>
      <remarks ident="binding-attr.contemporary-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que la reliure est contemporaine de son contenu ; la
          valeur <val>false</val> qu'elle ne l'est pas. La valeur <val>unknown</val> est employée
          quand la date de la reliure ou du manuscrit est inconnue.</p>
      </remarks>
      <remarks ident="binding-attr.contemporary-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、当該装訂が、当該内容と同時代のもの であることを示す。属性値<val>false</val>は、そうでないことを示
            す。属性値<val>unknown</val>は、当該装訂や手書き資料の年代が不 明の場合に使用されるべきである。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-wk">
      <binding contemporary="true">
        <p>Contemporary blind stamped leather over wooden boards with evidence of a fore edge clasp
          closing to the back cover.</p>
      </binding>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-ov" source="#fr-ex-BnF-Reliures">
      <binding contemporary="true">
        <p><index indexName="typo_reliure"><term>Reliure à la grecque, sur ais</term></index><index indexName="typo_decor"><term>Décor de rinceaux</term></index> Reliure à la grecque en <material>maroquin</material> orange</p>
        <decoNote type="plats"> aux armes de Henri II dorées sur une pièce de maroquin olive
            découpée à la forme exacte des armes (104 mm), mosaïquée dans un rectangle central aux
            angles orné d'un léger motif de rinceaux peints en noir, le tout encadré d'une large
            bordure mosaïquée de maroquin rouge, à plein décor de rinceaux dorés (incluant un
            croissant dans les angles) dessinés en réserve sur un fond pointillé doré.</decoNote>
        <decoNote type="plat_sup">Au plat supérieur, titre <q>i • schonerii • opera •</q> doré
            au-dessus du bloc armorial.</decoNote>
        <decoNote type="plat_inf"/>
        <decoNote type="dos">Dos long à décor analogue avec pièces losangées de maroquin rouge et
            brun mosaïquées, respectivement au centre et aux deux extrémités du dos, ornées d'un
            décor de rinceaux doré en réserve sur un fond doré pointillé, avec fer azuré au chapeau
            à chaque extrémité ; chaque pièce de maroquin est redessinée par un encadrement argenté,
            lui-même complété de rinceaux sur les côtés et relevé par des traits tracés de plume à
            effet de rayures.</decoNote>
        <decoNote type="tranchefiles">Tranchefiles doubles bicolores : points droits sur chevrons,
            bleus et jaunes.</decoNote>
        <decoNote type="coupes">Chants des ais rainurés.</decoNote>
        <decoNote type="annexes">Traces de petits boulons aux angles du rectangle intérieur ;
            traces des quatre lanières tressées d'origine sur les deux plats ; pas de traces de
            sabots.</decoNote>
        <decoNote type="tranches">Tranches dorées, ciselées et peintes (teinte rosée), à décor de
            rinceaux incluant des éléments de l'héraldique royale : triple croissant en tête, grand
            H couronné associé à un croissant en gouttière, chiffre HH en queue.</decoNote>
        <decoNote type="contreplats"/>
        <decoNote type="chasses">Absence de chasses.</decoNote>
        <!-- Description des gardes : gardes blanches ; gardes couleurs (marbrées, gaufrées, peintes, dominotées, etc.) généralement suivies de gardes blanches ; dans tous les cas, spécifier le nombre de gardes (début + fin du volume)-->
        <decoNote type="gardes">Gardes (3+2), filigrane <watermark>B</watermark>. </decoNote>
        <!-- Élément qui inclut aussi bien des remarques sur la couture que les charnières, claies ou modes d'attaches des plats : tous éléments de la structure dont la description est jugée utile à la description et l'identification de la reliure-->
        <decoNote type="structure"/>
        <condition/>
      </binding>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-tw" source="#fr-ex-BnF-Reliures">
      <bindingDesc>
        <binding contemporary="true">
          <p><index indexName="typo_reliure"><term>Reliure à décor</term></index><index indexName="typo_decor"><term>Compartiments espacés</term></index> Reliure en <material>maroquin</material> rouge sombre</p>
          <decoNote type="plats"> aux armes du chancelier Pierre Séguier, à décor de compartiments
              complétés de fers filigranés, parmi lesquels un fer à la petite tête (type B).</decoNote>
          <decoNote type="plat_sup"/>
          <decoNote type="plat_inf"/>
          <decoNote type="dos">Dos à 6 nerfs, à décor filigrané analogue ; palette ornée sur les
              nerfs et en tête et queue du dos ; titrage dans le 2e caisson.</decoNote>
          <decoNote type="tranchefiles">Tranchefiles à chapiteau tricolore (bleu, blanc et rose).</decoNote>
          <decoNote type="coupes">Coupes ornées.</decoNote>
          <decoNote type="annexes"/>
          <decoNote type="tranches">Tranches dorées.</decoNote>
          <decoNote type="contreplats">Contregardes en papier marbré à petit peigne, dans les tons
              bleu, blanc, jaune, rouge et blanc.</decoNote>
          <decoNote type="chasses">Chasses ornées.</decoNote>
          <!-- Description des gardes : gardes blanches ; gardes couleurs (marbrées, gaufrées, peintes, dominotées, etc.) généralement suivies de gardes blanches ; dans tous les cas, spécifier le nombre de gardes (début + fin du volume)-->
          <decoNote type="gardes">
            <watermark/>
          </decoNote>
          <!-- Élément qui inclut aussi bien des remarques sur la couture que les charnières, claies ou modes d'attaches des plats : tous éléments de la structure dont la description est jugée utile à la description et l'identification de la reliure-->
          <decoNote type="structure"/>
          <condition>Quelques taches sombres <!--surla --> sur le plat supérieur et larges
              éraflures du cuir au plat inférieur. Restauration en queue du mors inférieur (bande de
              cuir).</condition>
        </binding>
      </bindingDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-iq">
      <binding contemporary="true">
        <p>使用與內容物同時代的皮革包覆木版，背面有以前緣扣子扣住的跡象。</p>
      </binding>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-tx">
      <bindingDesc>
        <binding contemporary="false">
          <p> 使用與書寫的貝葉非同時代的樹條捆住</p>
        </binding>
        <binding contemporary="false">
          <p>以十九世紀的不知名棉繩重綁；裁切邊緣並鍍金</p>
        </binding>
      </bindingDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-zj">
      <bindingDesc>
        <binding contemporary="false">
          <p>Quarter bound by the Phillipps' binder, Bretherton, with his sticker on the front
            pastedown.</p>
        </binding>
        <binding contemporary="false">
          <p>Rebound by an unknown 19th c. company; edges cropped and gilt.</p>
        </binding>
      </bindingDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msphbi"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">binding</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">reliure</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="binding.desc">contains a description of one binding, i.e. type of covering, boards, etc. applied to a manuscript or other object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 제본에 대한 기술을 포함한다. 즉, 원고에 적용된 커버, 표지 등의 유형</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">一個裝訂的描述，例如使用於該手稿的封面類型、封面等。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">1つの装訂に関する情報を示す。例えば、手書き資料でいうカバーの種類、 表紙など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description d'une reliure, i.e. du type de couverture, d'ais, etc., rencontrés.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la descripción de una encuadernación, p.ej. tipo de cubiertas, tablas, etc. presentes en un manuscrito.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la descrizione di una legatura, cioè del tipo di copertine, tavole, ecc. utilizzate per il manoscritto.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.pLike"/>
      <elementRef key="condition"/>
      <elementRef key="decoNote"/>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">contemporary</gloss>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">contemporaine</gloss>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies whether or not the binding is contemporary with the majority of its
        contents.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">제본이 텍스트의 대부분 내용과 동시에 이루어졌는가의 여부를 명시한다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明裝訂和其大部分內容是否出於同一時期。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該装訂が、当該内容の大部分と同年代のものかどうかを示す。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie si la reliure est contemporaine ou non de
        l'essentiel du contenu du manuscrit.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica si la encuardenación es coetánea o no a la
        mayoría del contenido del manuscrito.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica se la legatura è coeva o meno rispetto alla
        maggior parte del suo contenuto</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="binding-attr.contemporary-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the binding is contemporaneous with its
          contents; the value <val>false</val> that it is not. The value <val>unknown</val> should
          be used when the date of either binding or manuscript is unknown</p>
      </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="binding-attr.contemporary-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que la reliure est contemporaine de son contenu ; la
          valeur <val>false</val> qu'elle ne l'est pas. La valeur <val>unknown</val> est employée
          quand la date de la reliure ou du manuscrit est inconnue.</p>
      </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="binding-attr.contemporary-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、当該装訂が、当該内容と同時代のもの であることを示す。属性値<val>false</val>は、そうでないことを示
            す。属性値<val>unknown</val>は、当該装訂や手書き資料の年代が不 明の場合に使用されるべきである。 </p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-wk">
      <binding contemporary="true">
        <p>Contemporary blind stamped leather over wooden boards with evidence of a fore edge clasp
          closing to the back cover.</p>
      </binding>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-ov" source="#fr-ex-BnF-Reliures">
      <binding contemporary="true">
        <p><index indexName="typo_reliure"><term>Reliure à la grecque, sur ais</term></index><index indexName="typo_decor"><term>Décor de rinceaux</term></index> Reliure à la grecque en <material>maroquin</material> orange</p>
        <decoNote type="plats"> aux armes de Henri II dorées sur une pièce de maroquin olive
            découpée à la forme exacte des armes (104 mm), mosaïquée dans un rectangle central aux
            angles orné d'un léger motif de rinceaux peints en noir, le tout encadré d'une large
            bordure mosaïquée de maroquin rouge, à plein décor de rinceaux dorés (incluant un
            croissant dans les angles) dessinés en réserve sur un fond pointillé doré.</decoNote>
        <decoNote type="plat_sup">Au plat supérieur, titre <q>i • schonerii • opera •</q> doré
            au-dessus du bloc armorial.</decoNote>
        <decoNote type="plat_inf"/>
        <decoNote type="dos">Dos long à décor analogue avec pièces losangées de maroquin rouge et
            brun mosaïquées, respectivement au centre et aux deux extrémités du dos, ornées d'un
            décor de rinceaux doré en réserve sur un fond doré pointillé, avec fer azuré au chapeau
            à chaque extrémité ; chaque pièce de maroquin est redessinée par un encadrement argenté,
            lui-même complété de rinceaux sur les côtés et relevé par des traits tracés de plume à
            effet de rayures.</decoNote>
        <decoNote type="tranchefiles">Tranchefiles doubles bicolores : points droits sur chevrons,
            bleus et jaunes.</decoNote>
        <decoNote type="coupes">Chants des ais rainurés.</decoNote>
        <decoNote type="annexes">Traces de petits boulons aux angles du rectangle intérieur ;
            traces des quatre lanières tressées d'origine sur les deux plats ; pas de traces de
            sabots.</decoNote>
        <decoNote type="tranches">Tranches dorées, ciselées et peintes (teinte rosée), à décor de
            rinceaux incluant des éléments de l'héraldique royale : triple croissant en tête, grand
            H couronné associé à un croissant en gouttière, chiffre HH en queue.</decoNote>
        <decoNote type="contreplats"/>
        <decoNote type="chasses">Absence de chasses.</decoNote>
        <!-- Description des gardes : gardes blanches ; gardes couleurs (marbrées, gaufrées, peintes, dominotées, etc.) généralement suivies de gardes blanches ; dans tous les cas, spécifier le nombre de gardes (début + fin du volume)-->
        <decoNote type="gardes">Gardes (3+2), filigrane <watermark>B</watermark>. </decoNote>
        <!-- Élément qui inclut aussi bien des remarques sur la couture que les charnières, claies ou modes d'attaches des plats : tous éléments de la structure dont la description est jugée utile à la description et l'identification de la reliure-->
        <decoNote type="structure"/>
        <condition/>
      </binding>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-tw" source="#fr-ex-BnF-Reliures">
      <bindingDesc>
        <binding contemporary="true">
          <p><index indexName="typo_reliure"><term>Reliure à décor</term></index><index indexName="typo_decor"><term>Compartiments espacés</term></index> Reliure en <material>maroquin</material> rouge sombre</p>
          <decoNote type="plats"> aux armes du chancelier Pierre Séguier, à décor de compartiments
              complétés de fers filigranés, parmi lesquels un fer à la petite tête (type B).</decoNote>
          <decoNote type="plat_sup"/>
          <decoNote type="plat_inf"/>
          <decoNote type="dos">Dos à 6 nerfs, à décor filigrané analogue ; palette ornée sur les
              nerfs et en tête et queue du dos ; titrage dans le 2e caisson.</decoNote>
          <decoNote type="tranchefiles">Tranchefiles à chapiteau tricolore (bleu, blanc et rose).</decoNote>
          <decoNote type="coupes">Coupes ornées.</decoNote>
          <decoNote type="annexes"/>
          <decoNote type="tranches">Tranches dorées.</decoNote>
          <decoNote type="contreplats">Contregardes en papier marbré à petit peigne, dans les tons
              bleu, blanc, jaune, rouge et blanc.</decoNote>
          <decoNote type="chasses">Chasses ornées.</decoNote>
          <!-- Description des gardes : gardes blanches ; gardes couleurs (marbrées, gaufrées, peintes, dominotées, etc.) généralement suivies de gardes blanches ; dans tous les cas, spécifier le nombre de gardes (début + fin du volume)-->
          <decoNote type="gardes">
            <watermark/>
          </decoNote>
          <!-- Élément qui inclut aussi bien des remarques sur la couture que les charnières, claies ou modes d'attaches des plats : tous éléments de la structure dont la description est jugée utile à la description et l'identification de la reliure-->
          <decoNote type="structure"/>
          <condition>Quelques taches sombres <!--surla --> sur le plat supérieur et larges
              éraflures du cuir au plat inférieur. Restauration en queue du mors inférieur (bande de
              cuir).</condition>
        </binding>
      </bindingDesc>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-iq">
      <binding contemporary="true">
        <p>使用與內容物同時代的皮革包覆木版，背面有以前緣扣子扣住的跡象。</p>
      </binding>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-tx">
      <bindingDesc>
        <binding contemporary="false">
          <p> 使用與書寫的貝葉非同時代的樹條捆住</p>
        </binding>
        <binding contemporary="false">
          <p>以十九世紀的不知名棉繩重綁；裁切邊緣並鍍金</p>
        </binding>
      </bindingDesc>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="BINDING-egXML-zj">
      <bindingDesc>
        <binding contemporary="false">
          <p>Quarter bound by the Phillipps' binder, Bretherton, with his sticker on the front
            pastedown.</p>
        </binding>
        <binding contemporary="false">
          <p>Rebound by an unknown 19th c. company; edges cropped and gilt.</p>
        </binding>
      </bindingDesc>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msphbi"/>
  </listRef>
```

^b31

