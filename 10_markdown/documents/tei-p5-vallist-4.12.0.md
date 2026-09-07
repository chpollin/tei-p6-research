---
type: representation
source-type: document
source: '[[00_sources/tei-p5-vallist-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 valList
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/valList.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# valList

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8503. Git blob: `5a7b38a849370584b7248ee4eec45974f94e1b8c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-valList" ident="valList">
  <gloss versionDate="2005-01-14" xml:lang="en">value list</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">값 목록</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性值列表</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">liste de valeurs</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">lista de valores</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">lista di valori</gloss>
  <desc versionDate="2012-09-23" xml:lang="en">contains one or more <gi>valItem</gi> elements defining possible values.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"> 하나의 속성에 대한 가능한 값을 정의하는 하나 이상의 <gi>valItem</gi> 요소를
  포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個或多個元素<gi>valItem</gi>，以定義一個屬性可使用的屬性值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">可能な属性値を表すひとつ以上の要素<gi>valItem</gi>を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un ou plusieurs éléments <gi>valItem</gi>
  qui définissent des valeurs possibles pour un attribut.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene uno o más elementos <gi>valItem</gi> que
  definen los valores posibles para un atributo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene uno o più elementi <gi>valItem</gi> che
  definiscono i valori possibili per un attributo</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
  </classes>
  <content>
    <elementRef key="valItem" minOccurs="0" maxOccurs="unbounded"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt">
      <desc versionDate="2012-09-23" xml:lang="en">specifies the extensibility of the list of values specified.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">명시된 속성 값 목록의 확장성을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明該屬性值列表的延展性。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">属性値リストの拡張性を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise l'extensibilité de la liste des valeurs
      de l'attribut.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la posibilidad de extender la lista de
      los valores especificados para los atributos.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la possibilità di estendere la lista dei
      valori specificati per gli attributi</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>open</defaultVal>
      <valList type="closed">
        <valItem ident="closed">
          <desc versionDate="2007-06-27" xml:lang="en">only the values specified are permitted.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">명시된 하나의 값만이 허용된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">僅允許標明的屬性值。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">solamente los valores especificados estan
          permitidos.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">許可された値のみ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">seules les valeurs indiquées sont
          autorisées.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">sono consentiti solo i valori
          specificati</desc>
        </valItem>
        <valItem ident="semi">
          <gloss versionDate="2007-07-04" xml:lang="en">semi-open</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">반개방</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">semi-ouvert</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">semiaperto</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">todos los valores indicados deben ser
          soportados pero son consentidos otros valores para los que son necesarios sistemas de
          elaboración adecuados.</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">all the values specified should be supported, but other values are legal and
          software should have appropriate fallback processing for them.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">명시된 모든 값이 지원되어야하지만, 다른 값도 적법하며 소프트웨어는 이들에 대해
          적절한 준비 프로세서를 갖추어야 한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">所有標明的屬性值應該維持有效；但其他屬性值亦為合法，且所使用的軟體對於它們應該具有適當的後備處理程序。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">todos los valores especificados deben ser
          utilizados, pero otros valores son legales y el software debe tener la posibilidad
          apropiada para proseceralos</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">付与される全値が支持されるべきであるが、その他の値も可能であ
          る。ソフトウェアは、そのための適切な代替処理を用意すべきであ る。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">toutes les valeurs indiquées doivent être
          acceptées, mais d'autres valeurs sont acceptables et le logiciel doit avoir une
          procédure qui leur est adaptée.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutti i valori indicati devono essere
          supportati ma sono consentiti altri valori per i quali sono necessari sistemi di
          eleborazione adeguati</desc>
        </valItem>
        <valItem ident="open">
          <desc versionDate="2007-06-27" xml:lang="en">the values specified are sample values only.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">명시된 값만이 표본 값이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">所標明的屬性值僅為樣本屬性值。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">los valores especificados son valores de
          muestra solamente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">付与された値は、参考値である。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les valeurs indiquées ne sont que des valeurs
          d'exemple.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i valori specificati sono solo valori
          campione</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valList-egXML-br">
      <valList type="closed">
        <valItem ident="req">
          <gloss>required</gloss>
        </valItem>
        <valItem ident="rec">
          <gloss>recommended</gloss>
        </valItem>
        <valItem ident="opt">
          <gloss>optional</gloss>
        </valItem>
      </valList>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valList-egXML-uj">
      <valList type="closed">
        <valItem ident="req">
          <gloss>exigé</gloss>
        </valItem>
        <valItem ident="rec">
          <gloss>Recommandé</gloss>
        </valItem>
        <valItem ident="opt">
          <gloss>optionnel</gloss>
        </valItem>
      </valList>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valList-egXML-jf">
      <valList type="closed">
        <valItem ident="req">
          <gloss>必要性</gloss>
        </valItem>
        <valItem ident="rec">
          <gloss>建議性</gloss>
        </valItem>
        <valItem ident="opt">
          <gloss>選擇性</gloss>
        </valItem>
      </valList>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDATT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">value list</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">값 목록</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性值列表</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">liste de valeurs</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">lista de valores</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">lista di valori</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-09-23" xml:lang="en">contains one or more <gi>valItem</gi> elements defining possible values.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"> 하나의 속성에 대한 가능한 값을 정의하는 하나 이상의 <gi>valItem</gi> 요소를
  포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個或多個元素<gi>valItem</gi>，以定義一個屬性可使用的屬性值。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">可能な属性値を表すひとつ以上の要素<gi>valItem</gi>を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un ou plusieurs éléments <gi>valItem</gi>
  qui définissent des valeurs possibles pour un attribut.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene uno o más elementos <gi>valItem</gi> que
  definen los valores posibles para un atributo.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene uno o più elementi <gi>valItem</gi> che
  definiscono i valori possibili per un attributo</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <elementRef key="valItem" minOccurs="0" maxOccurs="unbounded"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-09-23" xml:lang="en">specifies the extensibility of the list of values specified.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">명시된 속성 값 목록의 확장성을 명시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明該屬性值列表的延展性。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性値リストの拡張性を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise l'extensibilité de la liste des valeurs
      de l'attribut.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la posibilidad de extender la lista de
      los valores especificados para los atributos.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la possibilità di estendere la lista dei
      valori specificati per gli attributi</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>open</defaultVal>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="closed">
          <desc versionDate="2007-06-27" xml:lang="en">only the values specified are permitted.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">명시된 하나의 값만이 허용된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">僅允許標明的屬性值。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">solamente los valores especificados estan
          permitidos.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">許可された値のみ。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">seules les valeurs indiquées sont
          autorisées.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">sono consentiti solo i valori
          specificati</desc>
        </valItem>
        <valItem ident="semi">
          <gloss versionDate="2007-07-04" xml:lang="en">semi-open</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">반개방</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">semi-ouvert</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">semiaperto</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">todos los valores indicados deben ser
          soportados pero son consentidos otros valores para los que son necesarios sistemas de
          elaboración adecuados.</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">all the values specified should be supported, but other values are legal and
          software should have appropriate fallback processing for them.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">명시된 모든 값이 지원되어야하지만, 다른 값도 적법하며 소프트웨어는 이들에 대해
          적절한 준비 프로세서를 갖추어야 한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">所有標明的屬性值應該維持有效；但其他屬性值亦為合法，且所使用的軟體對於它們應該具有適當的後備處理程序。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">todos los valores especificados deben ser
          utilizados, pero otros valores son legales y el software debe tener la posibilidad
          apropiada para proseceralos</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">付与される全値が支持されるべきであるが、その他の値も可能であ
          る。ソフトウェアは、そのための適切な代替処理を用意すべきであ る。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">toutes les valeurs indiquées doivent être
          acceptées, mais d'autres valeurs sont acceptables et le logiciel doit avoir une
          procédure qui leur est adaptée.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutti i valori indicati devono essere
          supportati ma sono consentiti altri valori per i quali sono necessari sistemi di
          eleborazione adeguati</desc>
        </valItem>
        <valItem ident="open">
          <desc versionDate="2007-06-27" xml:lang="en">the values specified are sample values only.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">명시된 값만이 표본 값이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">所標明的屬性值僅為樣本屬性值。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">los valores especificados son valores de
          muestra solamente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">付与された値は、参考値である。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les valeurs indiquées ne sont que des valeurs
          d'exemple.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i valori specificati sono solo valori
          campione</desc>
        </valItem>
      </valList>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valList-egXML-br">
      <valList type="closed">
        <valItem ident="req">
          <gloss>required</gloss>
        </valItem>
        <valItem ident="rec">
          <gloss>recommended</gloss>
        </valItem>
        <valItem ident="opt">
          <gloss>optional</gloss>
        </valItem>
      </valList>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valList-egXML-uj">
      <valList type="closed">
        <valItem ident="req">
          <gloss>exigé</gloss>
        </valItem>
        <valItem ident="rec">
          <gloss>Recommandé</gloss>
        </valItem>
        <valItem ident="opt">
          <gloss>optionnel</gloss>
        </valItem>
      </valList>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valList-egXML-jf">
      <valList type="closed">
        <valItem ident="req">
          <gloss>必要性</gloss>
        </valItem>
        <valItem ident="rec">
          <gloss>建議性</gloss>
        </valItem>
        <valItem ident="opt">
          <gloss>選擇性</gloss>
        </valItem>
      </valList>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDATT"/>
  </listRef>
```

^b29

