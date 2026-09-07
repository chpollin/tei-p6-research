---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8969. Git blob: `651ba570507d6cf36a94ec03117d2d0a8c807322`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fDecl" ident="fDecl">
  <gloss versionDate="2005-01-14" xml:lang="en">feature declaration</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질 선언</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能宣告</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">déclaration de trait</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de rasgo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione di tratti</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">declares a single feature, specifying its name, organization,
range of allowed values, and optionally its default value.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">단일 자질, 자질 이름 명시, 조직, 허용 값의 범위, 그리고 수의적으로 기본 값을 선언한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">宣告一項功能，指明名稱、機構、有效值範圍、以及依情況提供預設值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ひとつの素性を宣言する。名前、構造、定義域、デフォルト値など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">déclare un trait unique, en en précisant le nom,
      l'organisation, la liste de valeurs autorisées et, éventuellement, la valeur par défaut.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">declara un único rasgo, indicando su nombre, organización, gama de valores posibles y, opcionalmente, su valor predeterminado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">dichiara un singolo tratto, specificandone il nome, l'organizzazione, la gamma di valori permessi, e opzionale il suo valore predefinito.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
    </classes>
  <content>
    <sequence>
      
        <elementRef key="fDescr" minOccurs="0"/>
      
      <elementRef key="vRange"/>
      
        <elementRef key="vDefault" minOccurs="0"/>
      
    </sequence>
  </content>
  <attList>
    <attDef ident="name" usage="req">
      <desc versionDate="2012-10-10" xml:lang="en">a single word which follows the rules defining a
        legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>), indicating the name of the feature being declared; matches the
<att>name</att> attribute of <gi>f</gi> elements in the text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">선언되고 있는 자질 이름을 제시한다; 텍스트 내 <gi>f</gi> 요소의 <att>name</att> 속성과 일치한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出所宣告的功能名稱；並符合文件中元素<gi>f</gi>的屬性<att>name</att>。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">素性の名前を示す。要素<gi>f</gi>の属性<att>name</att>と一致する
      もの。</desc>
      <desc versionDate="2009-04-16" xml:lang="fr">indique le nom du trait déclaré ; correspond à
          l'attribut <att>name</att> des éléments <gi>f</gi> du texte.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el nombre del rasgo que está siendo declarado; combina el atributo <att>name</att> de elementos <gi>f</gi> en el texto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il nome del tratto che si sta dichiarando; corrisponde all'attributo <att>name</att> dell'elemento <gi>f</gi> nel testo.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attDef usage="opt" ident="optional">
      <desc versionDate="2006-10-07" xml:lang="en">indicates whether or not the value of this feature may
	be present.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 자질 값의 제시 여부를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該功能值是否存在。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該素性値があるかどうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si la valeur de ce trait peut ou non exister.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el valor del rasgo debe estar presente o no.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se il valore del tratto possa o meno essere presente.</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
      <defaultVal>true</defaultVal>
      <remarks ident="fDecl-attr.optional-remarks" versionDate="2006-10-07" xml:lang="en">
        <p>If a feature is marked as optional, it is possible
	for it to be omitted from a feature structure. If an
	obligatory feature is omitted, then it is understood to have a
	default value, either explicitly declared, or, if no default
	is supplied, the special value  
<val>any</val>. If an optional feature is omitted, then it is
	understood to be missing and any possible value (including
	the default) is ignored. </p>
      </remarks>
      <remarks ident="fDecl-attr.optional-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si un trait est indiqué comme facultatif, il est possible de l'omettre d'une
                        structure de traits. Si un trait obligatoire est omis, il est alors réputé
                        avoir une valeur par défaut, déclarée explicitement, ou, si aucune valeur
                        par défaut n'est fournie, la valeur spéciale <val>any</val>. Si un trait
                        facultatif est omis, il est réputé manquant et aucune valeur possible n'est
                        prise en compte (y compris celle par défaut). </p>
      </remarks>
      <remarks ident="fDecl-attr.optional-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	素性が選択的とされる場合、素性構造から外してもよい。
	必須の素性がない場合、その値は、明示的に宣言されているデフォル
      ト値をとるとされる。デフォルト値が宣言されていない場合、特別な値
      <val>any</val>をとるとされる。
      選択的な素性がない場合、値はないか、または(デフォルト値を含む)あ
      らゆる値が無視されるとされる。
       </p>
      </remarks>
    </attDef>
    <!--    <attDef ident="org" usage="opt">
      <gloss>organization</gloss>
      <desc>specifies the organizing discipline of the feature value.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la disciplina organizativa del valor de rasgo.</desc>
      <desc versionDate="2006-10-28" xml:lang="ja">当該素性値をデータ構造を示す．</desc>
      <defaultVal>unit</defaultVal>
      <valList type="closed">
        <valItem ident="unit">
          <desc>unitary atomic value</desc>
          <desc versionDate="2007-05-04" xml:lang="es">valor aislado unitario</desc>
          <desc versionDate="2006-10-28" xml:lang="ja">(単独)</desc>
        </valItem>
        <valItem ident="set">
          <desc>set value (unordered, no duplicates)</desc>
          <desc versionDate="2007-05-04" xml:lang="es">valor de conjunto (desordenado, no duplicado)</desc>
          <desc versionDate="2006-10-28" xml:lang="ja">(集合，すなわち順序・重複が無い．)</desc>
        </valItem>
        <valItem ident="bag">
          <desc>bag value (unordered, may have duplicates)</desc>
          <desc versionDate="2007-05-04" xml:lang="es">valor de multiconjunto (desordenado, puede ser duplicado)</desc>
          <desc versionDate="2006-10-28" xml:lang="ja">(バック，すなわち順序が無く，重複有り．)</desc>
        </valItem>
        <valItem ident="list">
          <desc>list value (ordered, may have duplicates)</desc>
          <desc versionDate="2007-05-04" xml:lang="es">valor de lista (ordenado, puede ser duplicado)</desc>
          <desc versionDate="2006-10-28" xml:lang="ja">(リスト，すなわち順序が有り，重複も有る．)</desc>
        </valItem>
      </valList>
      
    </attDef>-->
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fDecl-egXML-kr">
      <fDecl name="INV">
        <fDescr>inverted sentence</fDescr>
        <vRange>
          <vAlt>
            <binary value="true"/>
            <binary value="false"/>
          </vAlt>
        </vRange>
        <vDefault>
          <binary value="false"/>
        </vDefault>
      </fDecl>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">feature declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질 선언</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能宣告</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">déclaration de trait</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de rasgo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione di tratti</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">declares a single feature, specifying its name, organization,
range of allowed values, and optionally its default value.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">단일 자질, 자질 이름 명시, 조직, 허용 값의 범위, 그리고 수의적으로 기본 값을 선언한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">宣告一項功能，指明名稱、機構、有效值範圍、以及依情況提供預設值。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ひとつの素性を宣言する。名前、構造、定義域、デフォルト値など。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">déclare un trait unique, en en précisant le nom,
      l'organisation, la liste de valeurs autorisées et, éventuellement, la valeur par défaut.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">declara un único rasgo, indicando su nombre, organización, gama de valores posibles y, opcionalmente, su valor predeterminado.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">dichiara un singolo tratto, specificandone il nome, l'organizzazione, la gamma di valori permessi, e opzionale il suo valore predefinito.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <elementRef key="fDescr" minOccurs="0"/>
      
      <elementRef key="vRange"/>
      
        <elementRef key="vDefault" minOccurs="0"/>
      
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-10-10" xml:lang="en">a single word which follows the rules defining a
        legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>), indicating the name of the feature being declared; matches the
<att>name</att> attribute of <gi>f</gi> elements in the text.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">선언되고 있는 자질 이름을 제시한다; 텍스트 내 <gi>f</gi> 요소의 <att>name</att> 속성과 일치한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出所宣告的功能名稱；並符合文件中元素<gi>f</gi>的屬性<att>name</att>。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性の名前を示す。要素<gi>f</gi>の属性<att>name</att>と一致する
      もの。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">indique le nom du trait déclaré ; correspond à
          l'attribut <att>name</att> des éléments <gi>f</gi> du texte.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el nombre del rasgo que está siendo declarado; combina el atributo <att>name</att> de elementos <gi>f</gi> en el texto.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il nome del tratto che si sta dichiarando; corrisponde all'attributo <att>name</att> dell'elemento <gi>f</gi> nel testo.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2006-10-07" xml:lang="en">indicates whether or not the value of this feature may
	be present.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 자질 값의 제시 여부를 표시한다.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該功能值是否存在。</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該素性値があるかどうかを示す。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si la valeur de ce trait peut ou non exister.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el valor del rasgo debe estar presente o no.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se il valore del tratto possa o meno essere presente.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>true</defaultVal>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="fDecl-attr.optional-remarks" versionDate="2006-10-07" xml:lang="en">
        <p>If a feature is marked as optional, it is possible
	for it to be omitted from a feature structure. If an
	obligatory feature is omitted, then it is understood to have a
	default value, either explicitly declared, or, if no default
	is supplied, the special value  
<val>any</val>. If an optional feature is omitted, then it is
	understood to be missing and any possible value (including
	the default) is ignored. </p>
      </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="fDecl-attr.optional-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si un trait est indiqué comme facultatif, il est possible de l'omettre d'une
                        structure de traits. Si un trait obligatoire est omis, il est alors réputé
                        avoir une valeur par défaut, déclarée explicitement, ou, si aucune valeur
                        par défaut n'est fournie, la valeur spéciale <val>any</val>. Si un trait
                        facultatif est omis, il est réputé manquant et aucune valeur possible n'est
                        prise en compte (y compris celle par défaut). </p>
      </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="fDecl-attr.optional-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	素性が選択的とされる場合、素性構造から外してもよい。
	必須の素性がない場合、その値は、明示的に宣言されているデフォル
      ト値をとるとされる。デフォルト値が宣言されていない場合、特別な値
      <val>any</val>をとるとされる。
      選択的な素性がない場合、値はないか、または(デフォルト値を含む)あ
      らゆる値が無視されるとされる。
       </p>
      </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fDecl-egXML-kr">
      <fDecl name="INV">
        <fDescr>inverted sentence</fDescr>
        <vRange>
          <vAlt>
            <binary value="true"/>
            <binary value="false"/>
          </vAlt>
        </vRange>
        <vDefault>
          <binary value="false"/>
        </vDefault>
      </fDecl>
    </egXML>
  </exemplum>
```

^b36

### Block 37

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b37

