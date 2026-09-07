---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.dimensions-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.dimensions
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.dimensions.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.dimensions

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11773. Git blob: `f9b8845f5b652175bfb597d4e1a9c49b77921fc9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" xml:id="class-attr-dimensions" ident="att.dimensions">
  <desc versionDate="2007-08-05" xml:lang="en">provides attributes for describing the size of physical objects.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">물리적 대상의 크기를 기술하는 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供符合某種度量值的屬性值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">物理的対象の大きさを表す属性を示す。</desc>
  <desc versionDate="2009-05-25" xml:lang="fr">fournit des attributs pour décrire la taille des objets physiques.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">assegna degli attributi che descrivono la grandezza di oggetti fisici</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos que califican una determinata medición.</desc>
  <desc versionDate="2026-04-15" xml:lang="de">stellt Attribute zur Beschreibung der Größe von physischen Objekten bereit.</desc>
  <classes>
    <memberOf key="att.ranging"/>
  </classes>
  <attList>
    <attDef ident="unit" usage="opt">
      <desc versionDate="2007-08-02" xml:lang="en">names the unit used for the measurement</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">측정 단위의 이름을 기술한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">度量單位的名稱。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該大きさの単位を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">noms des unités utilisées pour la mesure.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica las unidades usadas para la medición.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica le unità usate per la misurazione.</desc>
      <desc versionDate="2026-04-15" xml:lang="de">benennt die verwendeten Einheiten für die Messung</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="cm">
          <gloss versionDate="2007-08-02" xml:lang="en">centimetres</gloss>
          <gloss versionDate="2019-04-08" xml:lang="ja">センチメートル</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">centimètres</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">centímetros</gloss>
          <gloss versionDate="2007-01-21" xml:lang="it">centimetri</gloss>
          <gloss versionDate="2026-04-15" xml:lang="de">Zentimeter</gloss>
        </valItem>
        <valItem ident="mm">
          <gloss versionDate="2007-08-02" xml:lang="en">millimetres</gloss>
          <gloss versionDate="2019-04-08" xml:lang="ja">ミリメートル</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">millimètres</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">milímetros</gloss>
          <gloss versionDate="2007-01-21" xml:lang="it">millimetri</gloss>
          <gloss versionDate="2026-04-15" xml:lang="de">Millimeter</gloss>
        </valItem>
        <valItem ident="in">
          <gloss versionDate="2007-08-02" xml:lang="en">inches</gloss>
          <gloss versionDate="2019-04-08" xml:lang="ja">インチ</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">pouces</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">pulgadas</gloss>
          <gloss versionDate="2007-01-21" xml:lang="it">pollici</gloss>
          <gloss versionDate="2026-04-15" xml:lang="de">Zoll</gloss>
        </valItem>
        <valItem ident="line">
          <desc versionDate="2007-08-02" xml:lang="en">lines of text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 행</desc>
          <desc versionDate="2008-04-06" xml:lang="es">líneas de texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">テキスト行</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">lignes de texte</desc>
          <desc versionDate="2007-11-06" xml:lang="it">righe di testo</desc>
          <desc versionDate="2026-04-15" xml:lang="de">Textzeilen</desc>
        </valItem>
        <valItem ident="char">
          <gloss versionDate="2007-08-02" xml:lang="en">characters</gloss>
          <gloss versionDate="2019-04-08" xml:lang="ja">文字</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">문자</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">caracteres</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">caratteri</gloss>
          <gloss versionDate="2026-04-15" xml:lang="de">Zeichen</gloss>
          <desc versionDate="2007-08-02" xml:lang="en">characters of text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 문자</desc>
          <desc versionDate="2008-04-06" xml:lang="es">caracteres del texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">文字列</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">caractères du texte</desc>
          <desc versionDate="2007-11-06" xml:lang="it">caratteri di testo</desc>
          <desc versionDate="2026-04-15" xml:lang="de">Textzeichen</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="quantity">
      <desc versionDate="2007-08-02" xml:lang="en">specifies the length in the units specified</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">명시된 단위의 길이를 명시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">especifica la longitud en las unidades especificadas</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該単位の大きさを示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">spécifie la longueur dans les unités indiquées</desc>
      <desc versionDate="2007-11-06" xml:lang="it">specifica la lunghezza nelle unità indicate.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="extent" usage="opt">
      <desc versionDate="2008-09-10" xml:lang="en">indicates the size of the object concerned using a project-specific vocabulary combining quantity and units in a single string of words.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">indique la dimension de l'objet en utilisant un vocabulaire spécifique à un projet qui combine la quantité et l'unité dans une chaîne seule de mots.</desc>
      <desc versionDate="2019-04-08" xml:lang="ja">単一の文字列の数量と単位を組み合わせたプロジェクト固有の語彙を使用して、関連するオブジェクトのサイズを示す。</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-dimensions-egXML-yl" source="#UND">
          <gap extent="5 words"/>
        </egXML>
      </exemplum>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-dimensions-egXML-nv" source="#UND">
          <height extent="half the page"/>
        </egXML>
      </exemplum>
    </attDef>
    <attDef ident="precision">
      <desc versionDate="2008-09-10" xml:lang="en">characterizes the precision of the values specified by the other attributes.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">caractérise la précision des valeurs spécifiées par les autres attributs.</desc>
      <desc versionDate="2019-04-08" xml:lang="ja">他の属性によって指定された値の精度を特徴付ける。</desc>
      <datatype><dataRef key="teidata.certainty"/></datatype>
    </attDef>
    <attDef ident="scope" usage="opt">
      <desc versionDate="2008-09-10" xml:lang="en">where the measurement summarizes more than one observation, specifies the applicability of this measurement.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">측정의 적용가능성을 명시하며, 하나 이상의 대상이 측정된다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">測量多個物件時，標明此度量的可應用範圍。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">対象物が複数あった場合に、当該数値の適応範囲を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie l'applicabilité de cette mesure, là où plus d'un objet est mesuré.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la aplicabilidad de esta medición, en los casos en que se mida más de un objeto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'applicabilità della misurazione, laddove venga misurato più di un oggetto</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="all">
          <desc versionDate="2007-08-02" xml:lang="en">measurement applies to all instances.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">측정은 모두 사례에 적용된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">度量可應用於所有實例。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la medida se aplica a todos los casos.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">全インスタンスに当てはまる単位。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la mesure s'applique à tous les cas.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la misurazione fa riferimento a tutti i casi</desc>
        </valItem>
        <valItem ident="most">
          <desc versionDate="2007-08-02" xml:lang="en">measurement applies to most of the instances inspected.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">측정은 대부분의 사례에 적용된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">度量可應用於大部分實例。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la medida se aplica a la mayoría de los casos examinados.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">計測インスタンスの殆どに当てはまる単位。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la mesure s'applique à la plupart des cas examinés</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la misurazione fa riferimento alla maggior parte dei casi esaminati</desc>
        </valItem>
        <valItem ident="range">
          <desc versionDate="2007-08-02" xml:lang="en">measurement applies to only the specified range of instances.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">측정이 사례의 명시적 범위에 한정하여 적용된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">度量僅應用於特定範圍的實例。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la medida se aplica solamente a los casos especificados</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">特定インスタンスにのみ当てはまる単位。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la mesure s'applique seulement à l'ensemble des exemples indiqués.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la misurazione fa riferimento solo ai casi specificati</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-08-05" xml:lang="en">provides attributes for describing the size of physical objects.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">물리적 대상의 크기를 기술하는 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供符合某種度量值的屬性值。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">物理的対象の大きさを表す属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">fournit des attributs pour décrire la taille des objets physiques.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">assegna degli attributi che descrivono la grandezza di oggetti fisici</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos que califican una determinata medición.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/desc[8]`.

```xml
<desc versionDate="2026-04-15" xml:lang="de">stellt Attribute zur Beschreibung der Größe von physischen Objekten bereit.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.ranging"/>
  </classes>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-08-02" xml:lang="en">names the unit used for the measurement</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">측정 단위의 이름을 기술한다.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">度量單位的名稱。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該大きさの単位を示す。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">noms des unités utilisées pour la mesure.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica las unidades usadas para la medición.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica le unità usate per la misurazione.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2026-04-15" xml:lang="de">benennt die verwendeten Einheiten für die Messung</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="cm">
          <gloss versionDate="2007-08-02" xml:lang="en">centimetres</gloss>
          <gloss versionDate="2019-04-08" xml:lang="ja">センチメートル</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">centimètres</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">centímetros</gloss>
          <gloss versionDate="2007-01-21" xml:lang="it">centimetri</gloss>
          <gloss versionDate="2026-04-15" xml:lang="de">Zentimeter</gloss>
        </valItem>
        <valItem ident="mm">
          <gloss versionDate="2007-08-02" xml:lang="en">millimetres</gloss>
          <gloss versionDate="2019-04-08" xml:lang="ja">ミリメートル</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">millimètres</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">milímetros</gloss>
          <gloss versionDate="2007-01-21" xml:lang="it">millimetri</gloss>
          <gloss versionDate="2026-04-15" xml:lang="de">Millimeter</gloss>
        </valItem>
        <valItem ident="in">
          <gloss versionDate="2007-08-02" xml:lang="en">inches</gloss>
          <gloss versionDate="2019-04-08" xml:lang="ja">インチ</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">pouces</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">pulgadas</gloss>
          <gloss versionDate="2007-01-21" xml:lang="it">pollici</gloss>
          <gloss versionDate="2026-04-15" xml:lang="de">Zoll</gloss>
        </valItem>
        <valItem ident="line">
          <desc versionDate="2007-08-02" xml:lang="en">lines of text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 행</desc>
          <desc versionDate="2008-04-06" xml:lang="es">líneas de texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">テキスト行</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">lignes de texte</desc>
          <desc versionDate="2007-11-06" xml:lang="it">righe di testo</desc>
          <desc versionDate="2026-04-15" xml:lang="de">Textzeilen</desc>
        </valItem>
        <valItem ident="char">
          <gloss versionDate="2007-08-02" xml:lang="en">characters</gloss>
          <gloss versionDate="2019-04-08" xml:lang="ja">文字</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">문자</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">caracteres</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">caratteri</gloss>
          <gloss versionDate="2026-04-15" xml:lang="de">Zeichen</gloss>
          <desc versionDate="2007-08-02" xml:lang="en">characters of text</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 문자</desc>
          <desc versionDate="2008-04-06" xml:lang="es">caracteres del texto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">文字列</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">caractères du texte</desc>
          <desc versionDate="2007-11-06" xml:lang="it">caratteri di testo</desc>
          <desc versionDate="2026-04-15" xml:lang="de">Textzeichen</desc>
        </valItem>
      </valList>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-08-02" xml:lang="en">specifies the length in the units specified</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">명시된 단위의 길이를 명시한다.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">especifica la longitud en las unidades especificadas</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該単位の大きさを示す。</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">spécifie la longueur dans les unités indiquées</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">specifica la lunghezza nelle unità indicate.</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2008-09-10" xml:lang="en">indicates the size of the object concerned using a project-specific vocabulary combining quantity and units in a single string of words.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">indique la dimension de l'objet en utilisant un vocabulaire spécifique à un projet qui combine la quantité et l'unité dans une chaîne seule de mots.</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2019-04-08" xml:lang="ja">単一の文字列の数量と単位を組み合わせたプロジェクト固有の語彙を使用して、関連するオブジェクトのサイズを示す。</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[3]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-dimensions-egXML-yl" source="#UND">
          <gap extent="5 words"/>
        </egXML>
      </exemplum>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[3]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-dimensions-egXML-nv" source="#UND">
          <height extent="half the page"/>
        </egXML>
      </exemplum>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2008-09-10" xml:lang="en">characterizes the precision of the values specified by the other attributes.</desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">caractérise la précision des valeurs spécifiées par les autres attributs.</desc>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2019-04-08" xml:lang="ja">他の属性によって指定された値の精度を特徴付ける。</desc>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.certainty"/></datatype>
```

^b36

### Block 37

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2008-09-10" xml:lang="en">where the measurement summarizes more than one observation, specifies the applicability of this measurement.</desc>
```

^b37

### Block 38

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">측정의 적용가능성을 명시하며, 하나 이상의 대상이 측정된다.</desc>
```

^b38

### Block 39

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">測量多個物件時，標明此度量的可應用範圍。</desc>
```

^b39

### Block 40

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">対象物が複数あった場合に、当該数値の適応範囲を示す。</desc>
```

^b40

### Block 41

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie l'applicabilité de cette mesure, là où plus d'un objet est mesuré.</desc>
```

^b41

### Block 42

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la aplicabilidad de esta medición, en los casos en que se mida más de un objeto.</desc>
```

^b42

### Block 43

XML location: `/classSpec[1]/attList[1]/attDef[5]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'applicabilità della misurazione, laddove venga misurato più di un oggetto</desc>
```

^b43

### Block 44

XML location: `/classSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b44

### Block 45

XML location: `/classSpec[1]/attList[1]/attDef[5]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="all">
          <desc versionDate="2007-08-02" xml:lang="en">measurement applies to all instances.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">측정은 모두 사례에 적용된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">度量可應用於所有實例。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la medida se aplica a todos los casos.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">全インスタンスに当てはまる単位。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la mesure s'applique à tous les cas.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la misurazione fa riferimento a tutti i casi</desc>
        </valItem>
        <valItem ident="most">
          <desc versionDate="2007-08-02" xml:lang="en">measurement applies to most of the instances inspected.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">측정은 대부분의 사례에 적용된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">度量可應用於大部分實例。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la medida se aplica a la mayoría de los casos examinados.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">計測インスタンスの殆どに当てはまる単位。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la mesure s'applique à la plupart des cas examinés</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la misurazione fa riferimento alla maggior parte dei casi esaminati</desc>
        </valItem>
        <valItem ident="range">
          <desc versionDate="2007-08-02" xml:lang="en">measurement applies to only the specified range of instances.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">측정이 사례의 명시적 범위에 한정하여 적용된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">度量僅應用於特定範圍的實例。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la medida se aplica solamente a los casos especificados</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">特定インスタンスにのみ当てはまる単位。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la mesure s'applique seulement à l'ensemble des exemples indiqués.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la misurazione fa riferimento solo ai casi specificati</desc>
        </valItem>
      </valList>
```

^b45

