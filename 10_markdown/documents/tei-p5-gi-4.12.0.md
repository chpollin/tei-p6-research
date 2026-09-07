---
type: representation
source-type: document
source: '[[00_sources/tei-p5-gi-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 gi
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/gi.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# gi

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9386. Git blob: `69ab4aff2da377af5845e180d51c8d060d6c9421`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-gi" ident="gi">
  <gloss versionDate="2007-07-04" xml:lang="en">element name</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">요소명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">通用識別符碼</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">identifiant générique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">identificador genérico</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">identificatore generico</gloss>
  <gloss versionDate="2017-06-25" xml:lang="de">Elementname</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the name (generic identifier) of an element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">요소의 이름(일반적 확인소)을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個元素名稱 (通用識別符碼) 。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素の名前(共通識別子)を含む。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le nom  d'un élément.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre (identificador genérico) de un
    elemento.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome (identificatore generico) di un elemento.</desc>
  <desc versionDate="2017-06-25" xml:lang="de">enthält den Namen (generische Kennung) eines Elements.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.phrase.xml"/>
  </classes>
  <content>
    <dataRef key="teidata.name"/>
  </content>
  <attList>
    <attDef ident="scheme" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">supplies the name of the scheme in which this name is defined.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이름이 정의된 스키마의 이름을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供該標準之識別符碼，此名稱定義於該標準中。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該名前が定義されているスキーム名を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit le nom du modèle dans lequel ce nom est défini.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombra del esquema en el que se define
        tal nombre.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome dello schema in cui è definito tale
        nome</desc>
      <desc versionDate="2017-06-25" xml:lang="de">enthält den Namen des Schemas, in dem der Name definiert ist.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>TEI</defaultVal>
      <valList type="open">
        <valItem ident="TEI">
          <desc versionDate="2007-06-27" xml:lang="en">this element is part of the TEI scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 요소는 TEI 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此元素為TEI標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este elemento es parte del esquema de TEI.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該要素はTEIスキームにある。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément fait partie du modèle TEI.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento è parte dello schema TEI.</desc>
          <desc versionDate="2017-06-25" xml:lang="de">das Element ist Teil des TEI-Schemas.</desc>
        </valItem>
        <valItem ident="DBK">
          <gloss versionDate="2007-07-04" xml:lang="en">docbook</gloss>
          <gloss versionDate="2017-06-25" xml:lang="de">Docbook</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this element is part of the Docbook scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 요소는 Docbook 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此元素為 Docbook標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este elemento es parte del esquema de Docbook.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該要素は、DocBookスキームにある。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément fait partie du modèle Docbook.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento è parte dello schema Docbook.</desc>
          <desc versionDate="2017-06-25" xml:lang="de">das Element ist Teil des Docbook-Schemas.</desc>
        </valItem>
        <valItem ident="XX">
          <gloss versionDate="2007-07-04" xml:lang="en">unknown</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">미지의</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr"> inconnu.</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sconosciuto</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">desconocido.</gloss>
          <gloss versionDate="2017-06-25" xml:lang="de">unbekannt</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this element is part of an unknown scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 요소는 미지의 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此元素所屬的標準不明。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este elemento es parte de un esquema desconocido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該要素のスキームは不明。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément fait partie d'un modèle inconnu.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento è parte di uno schema
          sconosciuto</desc>
          <desc versionDate="2017-06-25" xml:lang="de">das Element ist Teil eines unbekannten Schemas.</desc>
        </valItem>
        <valItem ident="Schematron">
          <desc versionDate="2013-01-03" xml:lang="en">this element is from Schematron.</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">cet élément est défini dans le schéma Schematron.</desc>
          <desc versionDate="2017-06-25" xml:lang="de">es handelt sich um ein Schematron-Element.</desc>
        </valItem>
        <valItem ident="HTML">
          <desc versionDate="2013-01-03" xml:lang="en">this element is from the HTML scheme.</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">cet élément est défini dans le schéma HTML.</desc>
          <desc versionDate="2017-06-25" xml:lang="de">das Element ist Teil des HTML-Schemas.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gi-egXML-ra">
      <p>The <gi>xhtml:li</gi> element is roughly analogous to the <gi>item</gi> element, as is the
          <gi scheme="DBK">listItem</gi> element.</p>
    </egXML>
    <p>This example shows the use of both a namespace prefix and the <att>scheme</att> attribute as alternative
      ways of indicating that the <gi>gi</gi> in question is not a TEI element name: in practice only one
      method should be adopted.</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gi-egXML-iz">
      <p>L'élément <gi>xhtml:li</gi> est grosso modo analogue à l'élément <gi>item</gi>, comme
          l'est l'élément <gi scheme="DBK">listItem</gi>.</p>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cet exemple montre que l'emploi d'un espace de noms préfixe et celui de l'attribut de
        schéma sont des alternatives possibles pour indiquer que le <gi>gi</gi> en question n'est
        pas un nom d'élément TEI : dans la pratique, une seule méthode sera utilisée.</p>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gi-egXML-hn">
      <p>元素 <gi>xhtml:li</gi>大略類似元素<gi>item</gi>，以及元素 <gi scheme="DBK">listItem</gi>。</p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gi-egXML-ak">
      <p>The <gi>xhtml:li</gi> element is roughly analogous to the <gi>item</gi> element, as is the
        <gi scheme="DBK">listItem</gi> element.</p>
    </egXML>
    <p>Dieses Beispiel zeigt die Verwendung eines Namensraum-Präfix sowie den Gebrauch des
      <att>scheme</att>-Attributs als alternative Möglichkeiten um anzuzeigen, dass es sich bei
      dem betroffenen <gi>gi</gi>-Element nicht um einen TEI-Elementnamen handelt: In der Praxis
      sollte nur eine Methode verwendet werden.</p>
  </exemplum>
  <listRef>
    <ptr target="#TD"/>
    <ptr target="#TDTAG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">element name</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">요소명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">通用識別符碼</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">identifiant générique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">identificador genérico</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">identificatore generico</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-25" xml:lang="de">Elementname</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the name (generic identifier) of an element.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">요소의 이름(일반적 확인소)을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個元素名稱 (通用識別符碼) 。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素の名前(共通識別子)を含む。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le nom  d'un élément.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre (identificador genérico) de un
    elemento.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome (identificatore generico) di un elemento.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-25" xml:lang="de">enthält den Namen (generische Kennung) eines Elements.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.phrase.xml"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <dataRef key="teidata.name"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies the name of the scheme in which this name is defined.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이름이 정의된 스키마의 이름을 제시한다.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供該標準之識別符碼，此名稱定義於該標準中。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該名前が定義されているスキーム名を示す。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit le nom du modèle dans lequel ce nom est défini.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombra del esquema en el que se define
        tal nombre.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome dello schema in cui è definito tale
        nome</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2017-06-25" xml:lang="de">enthält den Namen des Schemas, in dem der Name definiert ist.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>TEI</defaultVal>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="TEI">
          <desc versionDate="2007-06-27" xml:lang="en">this element is part of the TEI scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 요소는 TEI 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此元素為TEI標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este elemento es parte del esquema de TEI.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該要素はTEIスキームにある。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément fait partie du modèle TEI.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento è parte dello schema TEI.</desc>
          <desc versionDate="2017-06-25" xml:lang="de">das Element ist Teil des TEI-Schemas.</desc>
        </valItem>
        <valItem ident="DBK">
          <gloss versionDate="2007-07-04" xml:lang="en">docbook</gloss>
          <gloss versionDate="2017-06-25" xml:lang="de">Docbook</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this element is part of the Docbook scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 요소는 Docbook 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此元素為 Docbook標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este elemento es parte del esquema de Docbook.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該要素は、DocBookスキームにある。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément fait partie du modèle Docbook.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento è parte dello schema Docbook.</desc>
          <desc versionDate="2017-06-25" xml:lang="de">das Element ist Teil des Docbook-Schemas.</desc>
        </valItem>
        <valItem ident="XX">
          <gloss versionDate="2007-07-04" xml:lang="en">unknown</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">미지의</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr"> inconnu.</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sconosciuto</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">desconocido.</gloss>
          <gloss versionDate="2017-06-25" xml:lang="de">unbekannt</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this element is part of an unknown scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 요소는 미지의 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此元素所屬的標準不明。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este elemento es parte de un esquema desconocido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該要素のスキームは不明。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet élément fait partie d'un modèle inconnu.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'elemento è parte di uno schema
          sconosciuto</desc>
          <desc versionDate="2017-06-25" xml:lang="de">das Element ist Teil eines unbekannten Schemas.</desc>
        </valItem>
        <valItem ident="Schematron">
          <desc versionDate="2013-01-03" xml:lang="en">this element is from Schematron.</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">cet élément est défini dans le schéma Schematron.</desc>
          <desc versionDate="2017-06-25" xml:lang="de">es handelt sich um ein Schematron-Element.</desc>
        </valItem>
        <valItem ident="HTML">
          <desc versionDate="2013-01-03" xml:lang="en">this element is from the HTML scheme.</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">cet élément est défini dans le schéma HTML.</desc>
          <desc versionDate="2017-06-25" xml:lang="de">das Element ist Teil des HTML-Schemas.</desc>
        </valItem>
      </valList>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gi-egXML-ra">
      <p>The <gi>xhtml:li</gi> element is roughly analogous to the <gi>item</gi> element, as is the
          <gi scheme="DBK">listItem</gi> element.</p>
    </egXML>
    <p>This example shows the use of both a namespace prefix and the <att>scheme</att> attribute as alternative
      ways of indicating that the <gi>gi</gi> in question is not a TEI element name: in practice only one
      method should be adopted.</p>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gi-egXML-iz">
      <p>L'élément <gi>xhtml:li</gi> est grosso modo analogue à l'élément <gi>item</gi>, comme
          l'est l'élément <gi scheme="DBK">listItem</gi>.</p>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cet exemple montre que l'emploi d'un espace de noms préfixe et celui de l'attribut de
        schéma sont des alternatives possibles pour indiquer que le <gi>gi</gi> en question n'est
        pas un nom d'élément TEI : dans la pratique, une seule méthode sera utilisée.</p>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gi-egXML-hn">
      <p>元素 <gi>xhtml:li</gi>大略類似元素<gi>item</gi>，以及元素 <gi scheme="DBK">listItem</gi>。</p>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gi-egXML-ak">
      <p>The <gi>xhtml:li</gi> element is roughly analogous to the <gi>item</gi> element, as is the
        <gi scheme="DBK">listItem</gi> element.</p>
    </egXML>
    <p>Dieses Beispiel zeigt die Verwendung eines Namensraum-Präfix sowie den Gebrauch des
      <att>scheme</att>-Attributs als alternative Möglichkeiten um anzuzeigen, dass es sich bei
      dem betroffenen <gi>gi</gi>-Element nicht um einen TEI-Elementnamen handelt: In der Praxis
      sollte nur eine Methode verwendet werden.</p>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TD"/>
    <ptr target="#TDTAG"/>
  </listRef>
```

^b33

