---
type: representation
source-type: document
source: '[[00_sources/tei-p5-geodecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 geoDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/geoDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# geoDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10155. Git blob: `e78accb971e1f5c2a667902c5582383d5c23e919`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-geoDecl" ident="geoDecl">
  <gloss versionDate="2007-09-23" xml:lang="en">geographic coordinates declaration</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">지리적 좌표 선언</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">declaración de las coordenadas geográficas</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">déclaration de coordonnées géographiques.</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">dichiarazione di coordinate geografiche</gloss>
  <desc versionDate="2007-07-04" xml:lang="en">documents the notation and the datum used for geographic coordinates expressed as content of the <gi>geo</gi> element elsewhere within the document.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">문서 내 어디서든지 <gi>geo</gi> 요소의 내용으로 표현된 지리적 좌표로 사용된 표기법과 자료를
    기재한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">documenta la anotación y los datos usados para los
    coordenadas geográficas expresadas como contenido del elemento <gi>geo</gi> en qualquier parte
    del documento.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該文書中にある要素<gi>geo</gi>の内容が表す座標の表記法を示す。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">documente la notation et les données utilisées pour
    exprimer les coordonnées géographiques dans l'élément <gi>geo</gi>ailleurs dans le document.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">documenta la notazione e il dato utilizzati per le
    coordinate geografiche espressi come contenuto di un elemento geo collocato altrove all'interno
    del documento</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <constraintSpec ident="geoDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:geoDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="datum" usage="opt">
      <desc versionDate="2007-06-25" xml:lang="en">supplies a commonly used code name for the datum employed.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사용된 자료의 일반적 부호명을 제시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona un nombre de código de uso general para
        los datos empleados.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">データを示す、一般に使われている符号名を示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">donne un nom de code d'usage général pour les données
        employées.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica un nome in codice comunemente impiegato per il
        dato utilizzato</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>WGS84</defaultVal>
      <valList type="semi">
        <valItem ident="WGS84">
          <gloss versionDate="2007-06-25" xml:lang="en">World Geodetic System</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">세계 측지 시스템</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">Sistema Geodésico Mundial</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">Système Géodésique Mondial</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sistema geodetico mondiale</gloss>
          <desc versionDate="2007-06-25" xml:lang="en">a pair of numbers to be interpreted as latitude followed by longitude according to
            the World Geodetic System.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">세계 측지 시스템에 따라 한 쌍의 숫자는 위도, 경도를 나타낸다.</desc>
          <desc versionDate="2008-10-02" xml:lang="fr">couple de nombres destinés à être interprétés
            comme la latitude suivie de la longitude selon le Système Géodésique Mondial.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un par de números que se interpretarán como
            latitud siguió por la longitud según el sistema geodésico del mundo.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">世界測地システムに従った、緯度、経度とされる数値組。</desc>
          <desc versionDate="2007-11-06" xml:lang="it">coppia numeri da interpretare come latitudine
            seguita da longitudine secondo il sistema geodetico mondiale</desc>
        </valItem>
        <valItem ident="MGRS">
          <gloss versionDate="2007-06-25" xml:lang="en">Military Grid Reference System</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">군사 좌표 참조 시스템</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">Sistema de Coordenadas MGRS</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">Système de Référence du Réseau Militaire,
            (MGRS).</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sistema di riferimento delle coordinate MGRS</gloss>
          <desc versionDate="2024-12-01" xml:lang="en">values supplied follow the Military Grid Reference System, 
            which designates grid zones in a string of letters and numbers that distinctly indicate each square meter on the planet.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">값은 만국 횡메르카토르 시스템 좌표에 기초하여 지리공간적 개체 부호를 제시한다.</desc>
          <desc versionDate="2008-10-02" xml:lang="fr">les valeurs fournies sont des codes objet
            d'entités geospatiales, fondées sur les coordonnées de la grille de projection
            transversale universelle de Mercator, (UTM).</desc>
          <desc versionDate="2008-04-06" xml:lang="es">los valores proporcionados son códigos objeto de
            entidades geospaciales, basados en las coordenadas Universal Transverse Mercator</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">ユニバーサル横メルカトル座標による、地理空間実体の値。</desc>
          <desc versionDate="2007-11-06" xml:lang="it">i valori indicati sono codici di entità
            geospaziali basati su coordinate UTM (Universale Trasverso di Mercatore)</desc>
        </valItem>
        <valItem ident="OSGB36">
          <gloss versionDate="2007-07-04" xml:lang="en">ordnance survey great britain</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">영국 육지 측량부</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">Système de coordonnées de Grande-Bretagne (OSGB)</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sistema di riferimento a reticolato OSGB36</gloss>
          <desc versionDate="2007-06-25" xml:lang="en">the value supplied is to be interpreted as a British National Grid Reference.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">제시된 값은 영국 측량 참조로 해석된다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el valor proporcionado debe ser interpretado como
            una referencia British National Grid.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">英国グリッド参照による値。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la valeur fournie est à interpréter selon le
            système "British national grid reference".</desc>
          <desc versionDate="2007-11-06" xml:lang="it">il valore indicato va interpretato come
            riferimento dell'OSGB36</desc>
        </valItem>
        <valItem ident="ED50">
          <gloss versionDate="2007-09-22" xml:lang="en">European Datum coordinate system</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">유럽 자료 좌표 시스템</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">Sistema de coordinadas European Datum</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">système de coordonnées de données européen.</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sistema di riferimento ED50</gloss>
          <desc versionDate="2007-09-22" xml:lang="en">the value supplied is to be interpreted as latitude followed by longitude according
            to the European Datum coordinate system.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">값은 유럽 자료 좌표 시스템에 따라 위도, 경도를 나타낸다.</desc>
          <desc versionDate="2008-10-02" xml:lang="fr">la valeur fournie doit être interprétée comme la
            latitude suivie de la longitude selon le système de coordonnées de données européen.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el valor suministrado debe ser interpretado como
            latitud seguida por la longitud según el sistema de coordenadas del European Datum.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">欧州測地基準座標システムによる、緯度、軽度となる値。</desc>
          <desc versionDate="2007-11-06" xml:lang="it">il valore indicato va interpretato come
            latitudine seguita da longitudine secondo il sistema di coordinate ED50</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geoDecl-egXML-wk" source="#UND">
      <geoDecl datum="OSGB36"/>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HDGDECL" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-09-23" xml:lang="en">geographic coordinates declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">지리적 좌표 선언</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">declaración de las coordenadas geográficas</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">déclaration de coordonnées géographiques.</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">dichiarazione di coordinate geografiche</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-07-04" xml:lang="en">documents the notation and the datum used for geographic coordinates expressed as content of the <gi>geo</gi> element elsewhere within the document.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문서 내 어디서든지 <gi>geo</gi> 요소의 내용으로 표현된 지리적 좌표로 사용된 표기법과 자료를
    기재한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">documenta la anotación y los datos usados para los
    coordenadas geográficas expresadas como contenido del elemento <gi>geo</gi> en qualquier parte
    del documento.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該文書中にある要素<gi>geo</gi>の内容が表す座標の表記法を示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">documente la notation et les données utilisées pour
    exprimer les coordonnées géographiques dans l'élément <gi>geo</gi>ailleurs dans le document.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">documenta la notazione e il dato utilizzati per le
    coordinate geografiche espressi come contenuto di un elemento geo collocato altrove all'interno
    del documento</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="geoDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:geoDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-06-25" xml:lang="en">supplies a commonly used code name for the datum employed.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사용된 자료의 일반적 부호명을 제시한다.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona un nombre de código de uso general para
        los datos empleados.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">データを示す、一般に使われている符号名を示す。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">donne un nom de code d'usage général pour les données
        employées.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica un nome in codice comunemente impiegato per il
        dato utilizzato</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>WGS84</defaultVal>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="WGS84">
          <gloss versionDate="2007-06-25" xml:lang="en">World Geodetic System</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">세계 측지 시스템</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">Sistema Geodésico Mundial</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">Système Géodésique Mondial</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sistema geodetico mondiale</gloss>
          <desc versionDate="2007-06-25" xml:lang="en">a pair of numbers to be interpreted as latitude followed by longitude according to
            the World Geodetic System.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">세계 측지 시스템에 따라 한 쌍의 숫자는 위도, 경도를 나타낸다.</desc>
          <desc versionDate="2008-10-02" xml:lang="fr">couple de nombres destinés à être interprétés
            comme la latitude suivie de la longitude selon le Système Géodésique Mondial.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un par de números que se interpretarán como
            latitud siguió por la longitud según el sistema geodésico del mundo.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">世界測地システムに従った、緯度、経度とされる数値組。</desc>
          <desc versionDate="2007-11-06" xml:lang="it">coppia numeri da interpretare come latitudine
            seguita da longitudine secondo il sistema geodetico mondiale</desc>
        </valItem>
        <valItem ident="MGRS">
          <gloss versionDate="2007-06-25" xml:lang="en">Military Grid Reference System</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">군사 좌표 참조 시스템</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">Sistema de Coordenadas MGRS</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">Système de Référence du Réseau Militaire,
            (MGRS).</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sistema di riferimento delle coordinate MGRS</gloss>
          <desc versionDate="2024-12-01" xml:lang="en">values supplied follow the Military Grid Reference System, 
            which designates grid zones in a string of letters and numbers that distinctly indicate each square meter on the planet.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">값은 만국 횡메르카토르 시스템 좌표에 기초하여 지리공간적 개체 부호를 제시한다.</desc>
          <desc versionDate="2008-10-02" xml:lang="fr">les valeurs fournies sont des codes objet
            d'entités geospatiales, fondées sur les coordonnées de la grille de projection
            transversale universelle de Mercator, (UTM).</desc>
          <desc versionDate="2008-04-06" xml:lang="es">los valores proporcionados son códigos objeto de
            entidades geospaciales, basados en las coordenadas Universal Transverse Mercator</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">ユニバーサル横メルカトル座標による、地理空間実体の値。</desc>
          <desc versionDate="2007-11-06" xml:lang="it">i valori indicati sono codici di entità
            geospaziali basati su coordinate UTM (Universale Trasverso di Mercatore)</desc>
        </valItem>
        <valItem ident="OSGB36">
          <gloss versionDate="2007-07-04" xml:lang="en">ordnance survey great britain</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">영국 육지 측량부</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">Système de coordonnées de Grande-Bretagne (OSGB)</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sistema di riferimento a reticolato OSGB36</gloss>
          <desc versionDate="2007-06-25" xml:lang="en">the value supplied is to be interpreted as a British National Grid Reference.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">제시된 값은 영국 측량 참조로 해석된다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el valor proporcionado debe ser interpretado como
            una referencia British National Grid.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">英国グリッド参照による値。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la valeur fournie est à interpréter selon le
            système "British national grid reference".</desc>
          <desc versionDate="2007-11-06" xml:lang="it">il valore indicato va interpretato come
            riferimento dell'OSGB36</desc>
        </valItem>
        <valItem ident="ED50">
          <gloss versionDate="2007-09-22" xml:lang="en">European Datum coordinate system</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">유럽 자료 좌표 시스템</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">Sistema de coordinadas European Datum</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">système de coordonnées de données européen.</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sistema di riferimento ED50</gloss>
          <desc versionDate="2007-09-22" xml:lang="en">the value supplied is to be interpreted as latitude followed by longitude according
            to the European Datum coordinate system.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">값은 유럽 자료 좌표 시스템에 따라 위도, 경도를 나타낸다.</desc>
          <desc versionDate="2008-10-02" xml:lang="fr">la valeur fournie doit être interprétée comme la
            latitude suivie de la longitude selon le système de coordonnées de données européen.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el valor suministrado debe ser interpretado como
            latitud seguida por la longitud según el sistema de coordenadas del European Datum.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">欧州測地基準座標システムによる、緯度、軽度となる値。</desc>
          <desc versionDate="2007-11-06" xml:lang="it">il valore indicato va interpretato come
            latitudine seguita da longitudine secondo il sistema di coordinate ED50</desc>
        </valItem>
      </valList>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-geoDecl-egXML-wk" source="#UND">
      <geoDecl datum="OSGB36"/>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HDGDECL" type="div3"/>
  </listRef>
```

^b25

