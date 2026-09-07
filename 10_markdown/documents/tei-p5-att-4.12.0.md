---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12651. Git blob: `67d7da4585b8ba4272ab34603bdb02940f27a28d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="ATT" ident="att">
  <gloss versionDate="2005-01-14" xml:lang="en">attribute</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">속성</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">attribut</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">atributo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">attributo</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Attribut</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">属性</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the name of an attribute appearing within running text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">현 텍스트 내에 나타나는 속성명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含在連續文字中出現的屬性名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">属性の名前を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le nom d'un attribut apparaissant dans le courant du texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de un atributo que aparece en el
    interior de un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un attributo che compare all'interno
    del testo</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält den Namen eines Attributes im Fließtext.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.phrase.xml"/>
  </classes>
  <content>
    <dataRef key="teidata.name"/>
  </content>
  <attList>
    <attDef ident="scheme" usage="opt">
      <gloss versionDate="2009-05-29" xml:lang="en">scheme</gloss>
      <gloss versionDate="2009-05-29" xml:lang="fr">schéma</gloss>
      <gloss versionDate="2017-06-19" xml:lang="de">Schema</gloss>
      <desc versionDate="2005-09-25" xml:lang="en">supplies an identifier for the scheme in which this name is defined.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 이름이 정의된 스키마에 대한 확인소를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供該標準之識別符碼，此名稱定義於該標準中。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該属性名を定義するスキームの識別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant du schéma dans lequel ce nom
        est défini.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un identificador al esquema en el cual se
        define tal nombre.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore allo schema nel quale è
        definito tale nome</desc>
      <desc versionDate="2017-06-19" xml:lang="de">liefert einen Identifikator für das Schema in dem der Name definiert ist.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>TEI</defaultVal>
      <valList type="open">
        <valItem ident="TEI">
          <gloss versionDate="2007-07-04" xml:lang="en">Text Encoding Initiative</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 부호화 표준</gloss>
          <gloss versionDate="2009-05-29" xml:lang="fr">Text Encoding Initiative</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">TEI</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">este atributo es parte del esquema TEI.</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">Text Encoding Initiative</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">テクストエンコーディングイニシアチブ</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this attribute is part of the TEI scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 속성은 TEI 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此屬性為TEI標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este atributo es parte del esquema de TEI.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該属性はTEIスキームに属している。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet attribut fait partie du modèle TEI.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'attributo è parte dello schema TEI.</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil des TEI-Schemas.</desc>
        </valItem>
        <valItem ident="DBK">
          <gloss versionDate="2007-07-04" xml:lang="en">Docbook</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">도크북</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">Docbook</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">este atributo es parte del esquema Docbook.</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">Docbook</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">Docbook</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this attribute is part of the Docbook scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 속성은 Docbook 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此屬性為Docbook 標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este atributo es parte del esquema de Docbook.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該属性は、Docbookスキームに属している。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet attribut fait partie du modèle Docbook.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'attributo è parte dello schema Docbook.</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil des Docbook-Schemas.</desc>
        </valItem>
        <valItem ident="XX">
          <gloss versionDate="2007-07-04" xml:lang="en">unknown</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">미지의</gloss>
          <gloss versionDate="2009-05-29" xml:lang="fr">inconnu</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sconosciuto</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">este atributo es parte de un esquema
            desconocido.</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">unbekannt</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">未知の</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this attribute is part of an unknown scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 속성은 미지의 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此屬性所屬的標準不明。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este atributo es parte de un esquema desconocido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該属性は、未知のスキームに属している。</desc>
          <desc versionDate="2009-05-29" xml:lang="fr">cet attribut fait partie d'un schéma inconnu.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'attributo è parte di uno schema
          sconosciuto</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil eines unbekannten Schemas.</desc>
        </valItem>
        <valItem ident="imaginary">
          <gloss versionDate="2017-06-19" xml:lang="en">imaginary</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">imaginär</gloss>
          <desc versionDate="2014-05-21" xml:lang="en">the attribute is from a non-existent scheme, for illustrative purposes only</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist aus einem nicht existierenden Schema, ausschließlich für veranschaulichende Zwecke.</desc>
          <desc versionDate="2018-12-28" xml:lang="ja">当該属性は、説明の目的のためのみの、存在しないスキームからのものである。</desc>
        </valItem>
        <valItem ident="XHTML">
          <gloss versionDate="2017-06-19" xml:lang="en">XHTML</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">Extensible Hypertext Markup Language</gloss>
          <desc versionDate="2014-05-21" xml:lang="en">the attribute is part of the XHTML language</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil von XHTML.</desc>
          <desc versionDate="2018-12-28" xml:lang="ja">当該属性はXHTML言語の一部である。</desc>
        </valItem>
        <valItem ident="XML">
          <gloss versionDate="2017-06-19" xml:lang="en">XML</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">Extensible Markup Language</gloss>
          <desc versionDate="2014-05-21" xml:lang="en">the attribute is part of the XML language</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil von XML.</desc>
          <desc versionDate="2018-12-28" xml:lang="ja">当該属性はXML言語の一部である。</desc>
        </valItem>
        <valItem ident="XI">
          <gloss versionDate="2017-06-19" xml:lang="en">XI</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">xInclude</gloss>
          <desc versionDate="2014-05-21" xml:lang="en">the attribute is defined in the xInclude schema</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil des xInclude-Schemas.</desc>
          <desc versionDate="2018-12-28" xml:lang="ja">当該属性はxIncludeスキーマで定義されている。</desc>
        </valItem>
       
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATT-egXML-sw">
      <p>The TEI defines several <soCalled>global</soCalled> attributes; their names include
        <att>xml:id</att>, <att>rend</att>, <att>xml:lang</att>, <att>n</att>, <att>xml:space</att>,
        and <att>xml:base</att>; <att scheme="XX">type</att> is not amongst them.</p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATT-egXML-yu">
      <p>La TEI définit six attributs<soCalled>globaux</soCalled> qui se nomment
          <att>xml:id</att>, <att>rend</att>, <att>xml:lang</att>, <att>n</att>,
          <att>xml:space</att>, et <att>xml:base</att>; <att scheme="XX">type</att>n'en fait pas
          partie .</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATT-egXML-ri">
      <p>TEI定義六個<soCalled>global</soCalled>屬性，包括：
      <att>xml:id</att>, <att>rend</att>, <att>xml:lang</att>, <att>n</att>, <att>xml:space</att>,
      和<att>xml:base</att>; <att scheme="XX">type</att> 不在其中。</p>
    </egXML>
  </exemplum>
  <remarks ident="att-remarks" versionDate="2017-02-07" xml:lang="en">
    <p>As an alternative to using  the <att>scheme</att> attribute a namespace prefix may be used. Where both <att>scheme</att> and a prefix are used, the prefix takes precedence.</p>
  </remarks>
  <remarks ident="att-remarks" versionDate="2017-02-07" xml:lang="fr">
    <p>Un préfixe d'espace de noms peut être utilisé pour spécifier le schéma, comme alternative à sa
      spécification par l'attribut <att>scheme</att> : le préfixe est alors prioritaire.</p>
  </remarks>
  <remarks ident="att-remarks" versionDate="2018-12-28" xml:lang="ja"><p><att>scheme</att>属性を使用する代わりに、名前空間接頭辞を使用することもできる。<att>scheme</att>と接頭辞の両方が使用されている場合は、接頭辞が優先される。
  </p></remarks>
  <remarks ident="att-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Als Alternative zur Verwendung des <att>scheme</att>-Attributes kann ein Namensraum-Präfix
      verwendet werden. Wenn <att>scheme</att> und Präfix zugleich verwendet werden, hat das Präfix
      Vorrang.</p>
  </remarks>
  <listRef>
    <ptr target="#TD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">attribute</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">속성</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">attribut</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">atributo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">attributo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Attribut</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">属性</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the name of an attribute appearing within running text.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 텍스트 내에 나타나는 속성명을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含在連續文字中出現的屬性名稱。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性の名前を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le nom d'un attribut apparaissant dans le courant du texte.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el nombre de un atributo que aparece en el
    interior de un texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il nome di un attributo che compare all'interno
    del testo</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält den Namen eines Attributes im Fließtext.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.phrase.xml"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <dataRef key="teidata.name"/>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2009-05-29" xml:lang="en">scheme</gloss>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2009-05-29" xml:lang="fr">schéma</gloss>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Schema</gloss>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-09-25" xml:lang="en">supplies an identifier for the scheme in which this name is defined.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 이름이 정의된 스키마에 대한 확인소를 제공한다.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供該標準之識別符碼，此名稱定義於該標準中。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該属性名を定義するスキームの識別子を示す。</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit l'identifiant du schéma dans lequel ce nom
        est défini.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un identificador al esquema en el cual se
        define tal nombre.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna un identificatore allo schema nel quale è
        definito tale nome</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">liefert einen Identifikator für das Schema in dem der Name definiert ist.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>TEI</defaultVal>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="TEI">
          <gloss versionDate="2007-07-04" xml:lang="en">Text Encoding Initiative</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 부호화 표준</gloss>
          <gloss versionDate="2009-05-29" xml:lang="fr">Text Encoding Initiative</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">TEI</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">este atributo es parte del esquema TEI.</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">Text Encoding Initiative</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">テクストエンコーディングイニシアチブ</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this attribute is part of the TEI scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 속성은 TEI 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此屬性為TEI標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este atributo es parte del esquema de TEI.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該属性はTEIスキームに属している。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet attribut fait partie du modèle TEI.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'attributo è parte dello schema TEI.</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil des TEI-Schemas.</desc>
        </valItem>
        <valItem ident="DBK">
          <gloss versionDate="2007-07-04" xml:lang="en">Docbook</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">도크북</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">Docbook</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">este atributo es parte del esquema Docbook.</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">Docbook</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">Docbook</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this attribute is part of the Docbook scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 속성은 Docbook 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此屬性為Docbook 標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este atributo es parte del esquema de Docbook.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該属性は、Docbookスキームに属している。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cet attribut fait partie du modèle Docbook.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'attributo è parte dello schema Docbook.</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil des Docbook-Schemas.</desc>
        </valItem>
        <valItem ident="XX">
          <gloss versionDate="2007-07-04" xml:lang="en">unknown</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">미지의</gloss>
          <gloss versionDate="2009-05-29" xml:lang="fr">inconnu</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sconosciuto</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">este atributo es parte de un esquema
            desconocido.</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">unbekannt</gloss>
          <gloss versionDate="2018-12-28" xml:lang="ja">未知の</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">this attribute is part of an unknown scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 속성은 미지의 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此屬性所屬的標準不明。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">este atributo es parte de un esquema desconocido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該属性は、未知のスキームに属している。</desc>
          <desc versionDate="2009-05-29" xml:lang="fr">cet attribut fait partie d'un schéma inconnu.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'attributo è parte di uno schema
          sconosciuto</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil eines unbekannten Schemas.</desc>
        </valItem>
        <valItem ident="imaginary">
          <gloss versionDate="2017-06-19" xml:lang="en">imaginary</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">imaginär</gloss>
          <desc versionDate="2014-05-21" xml:lang="en">the attribute is from a non-existent scheme, for illustrative purposes only</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist aus einem nicht existierenden Schema, ausschließlich für veranschaulichende Zwecke.</desc>
          <desc versionDate="2018-12-28" xml:lang="ja">当該属性は、説明の目的のためのみの、存在しないスキームからのものである。</desc>
        </valItem>
        <valItem ident="XHTML">
          <gloss versionDate="2017-06-19" xml:lang="en">XHTML</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">Extensible Hypertext Markup Language</gloss>
          <desc versionDate="2014-05-21" xml:lang="en">the attribute is part of the XHTML language</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil von XHTML.</desc>
          <desc versionDate="2018-12-28" xml:lang="ja">当該属性はXHTML言語の一部である。</desc>
        </valItem>
        <valItem ident="XML">
          <gloss versionDate="2017-06-19" xml:lang="en">XML</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">Extensible Markup Language</gloss>
          <desc versionDate="2014-05-21" xml:lang="en">the attribute is part of the XML language</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil von XML.</desc>
          <desc versionDate="2018-12-28" xml:lang="ja">当該属性はXML言語の一部である。</desc>
        </valItem>
        <valItem ident="XI">
          <gloss versionDate="2017-06-19" xml:lang="en">XI</gloss>
          <gloss versionDate="2017-06-19" xml:lang="de">xInclude</gloss>
          <desc versionDate="2014-05-21" xml:lang="en">the attribute is defined in the xInclude schema</desc>
          <desc versionDate="2017-06-19" xml:lang="de">das Attribut ist Teil des xInclude-Schemas.</desc>
          <desc versionDate="2018-12-28" xml:lang="ja">当該属性はxIncludeスキーマで定義されている。</desc>
        </valItem>
       
      </valList>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATT-egXML-sw">
      <p>The TEI defines several <soCalled>global</soCalled> attributes; their names include
        <att>xml:id</att>, <att>rend</att>, <att>xml:lang</att>, <att>n</att>, <att>xml:space</att>,
        and <att>xml:base</att>; <att scheme="XX">type</att> is not amongst them.</p>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATT-egXML-yu">
      <p>La TEI définit six attributs<soCalled>globaux</soCalled> qui se nomment
          <att>xml:id</att>, <att>rend</att>, <att>xml:lang</att>, <att>n</att>,
          <att>xml:space</att>, et <att>xml:base</att>; <att scheme="XX">type</att>n'en fait pas
          partie .</p>
    </egXML>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ATT-egXML-ri">
      <p>TEI定義六個<soCalled>global</soCalled>屬性，包括：
      <att>xml:id</att>, <att>rend</att>, <att>xml:lang</att>, <att>n</att>, <att>xml:space</att>,
      和<att>xml:base</att>; <att scheme="XX">type</att> 不在其中。</p>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="att-remarks" versionDate="2017-02-07" xml:lang="en">
    <p>As an alternative to using  the <att>scheme</att> attribute a namespace prefix may be used. Where both <att>scheme</att> and a prefix are used, the prefix takes precedence.</p>
  </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="att-remarks" versionDate="2017-02-07" xml:lang="fr">
    <p>Un préfixe d'espace de noms peut être utilisé pour spécifier le schéma, comme alternative à sa
      spécification par l'attribut <att>scheme</att> : le préfixe est alors prioritaire.</p>
  </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="att-remarks" versionDate="2018-12-28" xml:lang="ja"><p><att>scheme</att>属性を使用する代わりに、名前空間接頭辞を使用することもできる。<att>scheme</att>と接頭辞の両方が使用されている場合は、接頭辞が優先される。
  </p></remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="att-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Als Alternative zur Verwendung des <att>scheme</att>-Attributes kann ein Namensraum-Präfix
      verwendet werden. Wenn <att>scheme</att> und Präfix zugleich verwendet werden, hat das Präfix
      Vorrang.</p>
  </remarks>
```

^b39

### Block 40

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TD"/>
  </listRef>
```

^b40

