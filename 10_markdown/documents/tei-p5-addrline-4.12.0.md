---
type: representation
source-type: document
source: '[[00_sources/tei-p5-addrline-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 addrLine
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/addrLine.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# addrLine

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5854. Git blob: `0090b923d3e9230a85bd973f0fad507ceb0be332`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-addrLine" ident="addrLine">
  <gloss versionDate="2007-07-04" xml:lang="en">address line</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">주소 행</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">dirección</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">ligne d'adresse</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">riga dell'indirizzo</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Adresszeile</gloss>
  <desc versionDate="2007-02-27" xml:lang="en">contains one line of a postal<!-- or other--> address.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">우편 주소의 한 행을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含郵寄地址或其他地址其的一行。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">住所情報を記述する行を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une ligne d'adresse postale.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una línea de la dirección postal.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una riga di un indirizzo (postale).</desc>
    <desc versionDate="2016-11-24" xml:lang="de">enthält eine Zeile einer Postadresse.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.addrPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addrLine-egXML-af" source="#NONE">
      <address>
        <addrLine>Computing Center, MC 135</addrLine>
        <addrLine>P.O. Box 6998</addrLine>
        <addrLine>Chicago, IL</addrLine>
        <addrLine>60680 USA</addrLine>
      </address>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addrLine-egXML-sz" source="#NONE">
      <addrLine>
        <ref target="tel:+1-201-555-0123">(201) 555 0123</ref>
      </addrLine>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addrLine-egXML-ga" source="#NONE">
      <address>
        <addrLine>44, avenue de la Libération</addrLine>
        <addrLine>B.P. 30687</addrLine>
        <addrLine>F 54063 NANCY CEDEX</addrLine>
        <addrLine>FRANCE</addrLine>
      </address>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addrLine-egXML-iw" source="#biblzh-tw_n2">
      <address>
        <addrLine> 276號4樓</addrLine>
        <addrLine>光明路</addrLine>
        <addrLine>北投區，台北市11246</addrLine>
        <addrLine>台灣，中華民國</addrLine>
      </address>
    </egXML>
  </exemplum>
  <remarks ident="addrLine-remarks" versionDate="2007-02-27" xml:lang="en">
    <p>Addresses may be encoded either as a sequence of lines, or
    using any sequence of component elements from the <ident type="class">model.addrPart</ident> class. Other non-postal forms
    of address, such as telephone numbers or email, should not be
    included within an <gi>address</gi> element directly but may be
    wrapped within an <gi>addrLine</gi> if they form part of the
    printed address in some source text. </p>
  </remarks>
  <remarks ident="addrLine-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les adresses peuvent être encodées soit comme une suite de
    lignes, soit en utilisant un jeu d'éléments de la classe <ident type="class">model.addrPart</ident>. Les types d'adresses autres
    que l'adresse postale, tels que les numéros de téléphone, les
    courriels, ne doivent pas être inclus directement à l'intérieur
    d'un élément <gi>address</gi> mais peuvent être contenus dans un
    élément <gi>addrLine</gi> s'ils font partie de l'adresse imprimée
    dans un texte source.</p>
  </remarks>
  <remarks ident="addrLine-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
            住所情報は、複数の行から構成されるか、クラス<ident type="class">model.addrPart</ident>にある要
            素から構成されているかもしれない。
            住所情報で、郵便配達には関連しない、例えば電話番号や電子メールアド
            レスについては、ここに直接は記述すべきではない。しかし、印刷物にこ
            れらが住所情報として含まれている場合には、要素<gi>addrLine</gi>を
            使い記述することはできる。
        </p>
  </remarks>
  <remarks ident="addrLine-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>
          Adressen können entweder als eine Abfolge von Zeilen kodiert werden oder als eine beliebige Folge 
          von Elementen der <ident type="class">model.addrPart</ident>-Klasse. Andere, nicht-postalische Formen von Adressen, 
          wie z. B. Telefonnummern oder E-Mail-Adressen, dürfen nicht direkt in ein <gi>address</gi>-Element eingeschlossen werden, 
          sondern müssen innerhalb eines <gi>addrLine</gi>-Elements kodiert werden, wenn sie Teil einer gedruckten Adresse in einer 
          Textvorlage sind.
      </p>
  </remarks>
  <listRef>
    <ptr target="#CONAAD"/>
    <ptr target="#HD24"/>
    <ptr target="#COBICOI"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">address line</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">주소 행</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">dirección</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">ligne d'adresse</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">riga dell'indirizzo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Adresszeile</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-02-27" xml:lang="en">contains one line of a postal<!-- or other--> address.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">우편 주소의 한 행을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含郵寄地址或其他地址其的一行。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">住所情報を記述する行を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une ligne d'adresse postale.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una línea de la dirección postal.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una riga di un indirizzo (postale).</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">enthält eine Zeile einer Postadresse.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.addrPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addrLine-egXML-af" source="#NONE">
      <address>
        <addrLine>Computing Center, MC 135</addrLine>
        <addrLine>P.O. Box 6998</addrLine>
        <addrLine>Chicago, IL</addrLine>
        <addrLine>60680 USA</addrLine>
      </address>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addrLine-egXML-sz" source="#NONE">
      <addrLine>
        <ref target="tel:+1-201-555-0123">(201) 555 0123</ref>
      </addrLine>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addrLine-egXML-ga" source="#NONE">
      <address>
        <addrLine>44, avenue de la Libération</addrLine>
        <addrLine>B.P. 30687</addrLine>
        <addrLine>F 54063 NANCY CEDEX</addrLine>
        <addrLine>FRANCE</addrLine>
      </address>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-addrLine-egXML-iw" source="#biblzh-tw_n2">
      <address>
        <addrLine> 276號4樓</addrLine>
        <addrLine>光明路</addrLine>
        <addrLine>北投區，台北市11246</addrLine>
        <addrLine>台灣，中華民國</addrLine>
      </address>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="addrLine-remarks" versionDate="2007-02-27" xml:lang="en">
    <p>Addresses may be encoded either as a sequence of lines, or
    using any sequence of component elements from the <ident type="class">model.addrPart</ident> class. Other non-postal forms
    of address, such as telephone numbers or email, should not be
    included within an <gi>address</gi> element directly but may be
    wrapped within an <gi>addrLine</gi> if they form part of the
    printed address in some source text. </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="addrLine-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les adresses peuvent être encodées soit comme une suite de
    lignes, soit en utilisant un jeu d'éléments de la classe <ident type="class">model.addrPart</ident>. Les types d'adresses autres
    que l'adresse postale, tels que les numéros de téléphone, les
    courriels, ne doivent pas être inclus directement à l'intérieur
    d'un élément <gi>address</gi> mais peuvent être contenus dans un
    élément <gi>addrLine</gi> s'ils font partie de l'adresse imprimée
    dans un texte source.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="addrLine-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
            住所情報は、複数の行から構成されるか、クラス<ident type="class">model.addrPart</ident>にある要
            素から構成されているかもしれない。
            住所情報で、郵便配達には関連しない、例えば電話番号や電子メールアド
            レスについては、ここに直接は記述すべきではない。しかし、印刷物にこ
            れらが住所情報として含まれている場合には、要素<gi>addrLine</gi>を
            使い記述することはできる。
        </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="addrLine-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>
          Adressen können entweder als eine Abfolge von Zeilen kodiert werden oder als eine beliebige Folge 
          von Elementen der <ident type="class">model.addrPart</ident>-Klasse. Andere, nicht-postalische Formen von Adressen, 
          wie z. B. Telefonnummern oder E-Mail-Adressen, dürfen nicht direkt in ein <gi>address</gi>-Element eingeschlossen werden, 
          sondern müssen innerhalb eines <gi>addrLine</gi>-Elements kodiert werden, wenn sie Teil einer gedruckten Adresse in einer 
          Textvorlage sind.
      </p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONAAD"/>
    <ptr target="#HD24"/>
    <ptr target="#COBICOI"/>
  </listRef>
```

^b26

