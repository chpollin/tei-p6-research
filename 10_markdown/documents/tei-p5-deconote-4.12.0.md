---
type: representation
source-type: document
source: '[[00_sources/tei-p5-deconote-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 decoNote
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/decoNote.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# decoNote

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5761. Git blob: `36937db2abc18153b321ec677332c561465b586e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="DECONOTE" ident="decoNote">
  <gloss versionDate="2007-07-04" xml:lang="en">note on decoration</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">장식에 관한 설명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">observaciones de la decoración</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">note sur un élément de décoration</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">nota sulla decorazione</gloss>
  <gloss versionDate="2024-08-08" xml:lang="ja">装飾に関する注記</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="deconote.desc">contains a note describing either a
decorative component of a manuscript or other object, or a fairly homogenous class of
such components.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 장식 성분 또는 동일 부류의 성분을 기술하는 설명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個附註，描述手稿的裝飾性要素、或是該類要素的同等分類。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料の装飾要素またはそのようなものを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une note décrivant soit un élément de
      décoration du mansucrit, soit une catégorie relativement homogène de tels éléments.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una nota que describe un componente decorativo de un manuscrito o una clase razonablemente homogénea de tales componentes.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una nota che descrive una componente decorativa di un manoscritto o una classe ragionevolmente omogenea di tali componenti.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.msItemPart"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECONOTE-egXML-am">
      <decoDesc>
        <decoNote type="initial">
          <p>The start of each book of the Bible with 
a 10-line historiated illuminated initial;
prefaces decorated with 6-line blue initials 
with red penwork flourishing; chapters marked by 
3-line plain red initials; verses with 1-line initials, 
alternately blue or red.</p>
        </decoNote>
      </decoDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECONOTE-egXML-je" source="#fr-ex-BnF-Reliures">
      <bindingDesc>
        <decoNote type="plats"> à décor d’entrelacs géométriques (structure de losange et
            rectangle) complété de fers évidés.</decoNote>
        <decoNote type="plat_sup">Titre <q>ivvenalis. persivs</q> et ex-libris de Jean Grolier
              <q>io. grolierii et amicorvm.</q> dorés respectivement au centre et au bas du plat
            supérieur. </decoNote>
        <decoNote type="plat_inf">Devise de Jean Grolier<q>portio mea sit in terra viventivm</q>
            dorée au centre du plat inférieur.</decoNote>
        <decoNote type="dos">Dos à cinq nerfs, sans décor ; simple filet doré sur chaque nerf et
            en encadrement des caissons ; passages de chaînette marqués de même.</decoNote>
        <decoNote type="tranchefiles">Tranchefiles simples unicolores, vert foncé.</decoNote>
        <decoNote type="coupes">Filet doré sur les coupes.</decoNote>
        <decoNote type="annexes"/>
        <decoNote type="tranches">Tranches dorées.</decoNote>
        <decoNote type="contreplats">Contreplats en vélin.</decoNote>
        <decoNote type="chasses">Filet doré sur les chasses.</decoNote>
        <!-- Description des gardes : gardes blanches ; gardes couleurs (marbrées, gaufrées, peintes, dominotées, etc.) généralement suivies de gardes blanches ; dans tous les cas, spécifier le nombre de gardes (début + fin du volume)-->
        <decoNote type="gardes">Gardes en papier et vélin (2+1+2 / 2+1+2) ; filigrane au
              pot.<ref>Briquet N° XX</ref>
            </decoNote>
        <!-- Élément qui inclut aussi bien des remarques sur la couture que les charnières, claies ou modes d'attaches des plats : tous éléments de la structure dont la description est jugée utile à la description et l'identification de la reliure-->
        <decoNote type="structure">Defet manuscrit utilisé comme claie au contreplat inférieur
            (visible par transparence, sous la contregarde en vélin).</decoNote>
      </bindingDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECONOTE-egXML-wh">
      <decoDesc>
        <decoNote type="initial">
          <p>每本聖經的第一個字母都是十行大小，飾以歷史圖案；引言部份的第一個字母是六行大小，並以紅筆花飾；章節的第一個字母是三行大小，紅的；韻文的第一個字母一行大小，有時是紅色有時是藍色的。</p>
        </decoNote>
      </decoDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">note on decoration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">장식에 관한 설명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">observaciones de la decoración</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">note sur un élément de décoration</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">nota sulla decorazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-08-08" xml:lang="ja">装飾に関する注記</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="deconote.desc">contains a note describing either a
decorative component of a manuscript or other object, or a fairly homogenous class of
such components.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 장식 성분 또는 동일 부류의 성분을 기술하는 설명을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個附註，描述手稿的裝飾性要素、或是該類要素的同等分類。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料の装飾要素またはそのようなものを示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une note décrivant soit un élément de
      décoration du mansucrit, soit une catégorie relativement homogène de tels éléments.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una nota que describe un componente decorativo de un manuscrito o una clase razonablemente homogénea de tales componentes.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una nota che descrive una componente decorativa di un manoscritto o una classe ragionevolmente omogenea di tali componenti.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.msItemPart"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECONOTE-egXML-am">
      <decoDesc>
        <decoNote type="initial">
          <p>The start of each book of the Bible with 
a 10-line historiated illuminated initial;
prefaces decorated with 6-line blue initials 
with red penwork flourishing; chapters marked by 
3-line plain red initials; verses with 1-line initials, 
alternately blue or red.</p>
        </decoNote>
      </decoDesc>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECONOTE-egXML-je" source="#fr-ex-BnF-Reliures">
      <bindingDesc>
        <decoNote type="plats"> à décor d’entrelacs géométriques (structure de losange et
            rectangle) complété de fers évidés.</decoNote>
        <decoNote type="plat_sup">Titre <q>ivvenalis. persivs</q> et ex-libris de Jean Grolier
              <q>io. grolierii et amicorvm.</q> dorés respectivement au centre et au bas du plat
            supérieur. </decoNote>
        <decoNote type="plat_inf">Devise de Jean Grolier<q>portio mea sit in terra viventivm</q>
            dorée au centre du plat inférieur.</decoNote>
        <decoNote type="dos">Dos à cinq nerfs, sans décor ; simple filet doré sur chaque nerf et
            en encadrement des caissons ; passages de chaînette marqués de même.</decoNote>
        <decoNote type="tranchefiles">Tranchefiles simples unicolores, vert foncé.</decoNote>
        <decoNote type="coupes">Filet doré sur les coupes.</decoNote>
        <decoNote type="annexes"/>
        <decoNote type="tranches">Tranches dorées.</decoNote>
        <decoNote type="contreplats">Contreplats en vélin.</decoNote>
        <decoNote type="chasses">Filet doré sur les chasses.</decoNote>
        <!-- Description des gardes : gardes blanches ; gardes couleurs (marbrées, gaufrées, peintes, dominotées, etc.) généralement suivies de gardes blanches ; dans tous les cas, spécifier le nombre de gardes (début + fin du volume)-->
        <decoNote type="gardes">Gardes en papier et vélin (2+1+2 / 2+1+2) ; filigrane au
              pot.<ref>Briquet N° XX</ref>
            </decoNote>
        <!-- Élément qui inclut aussi bien des remarques sur la couture que les charnières, claies ou modes d'attaches des plats : tous éléments de la structure dont la description est jugée utile à la description et l'identification de la reliure-->
        <decoNote type="structure">Defet manuscrit utilisé comme claie au contreplat inférieur
            (visible par transparence, sous la contregarde en vélin).</decoNote>
      </bindingDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="DECONOTE-egXML-wh">
      <decoDesc>
        <decoNote type="initial">
          <p>每本聖經的第一個字母都是十行大小，飾以歷史圖案；引言部份的第一個字母是六行大小，並以紅筆花飾；章節的第一個字母是三行大小，紅的；韻文的第一個字母一行大小，有時是紅色有時是藍色的。</p>
        </decoNote>
      </decoDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph3"/>
  </listRef>
```

^b20

