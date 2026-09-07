---
type: representation
source-type: document
source: '[[00_sources/tei-p5-num-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 num
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/num.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# num

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11704. Git blob: `d8c1aba61121e4d3f3ef95216880600f5c26f9d7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-num" ident="num">
  <gloss versionDate="2005-01-14" xml:lang="en">number</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">숫자</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">數字</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">numéral</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">número</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">numero</gloss>
  <gloss versionDate="2016-11-25" xml:lang="de">Zahl</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a number, written in any form.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">다양한 형식의 숫자를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個以任何形式呈現的數字。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">各種形式による数値を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient un nombre écrit sous une forme quelconque.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un número, escrito en cualquier forma.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un numero in qualsiasi forma.</desc>
  <desc versionDate="2016-11-25" xml:lang="de">beinhaltet eine Zahl, die auf beliebige Art geschrieben sein kann.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.ranging"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.measureLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates the type of numeric value.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">수치의 유형을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出數值的種類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">数値の種類を示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">indique le type de valeur numérique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el tipo de valor numérico.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il tipo di valore numerico.</desc>
      <desc versionDate="2016-11-25" xml:lang="de">bestimmt die Art des numerischen Wertes.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="cardinal">
          <desc versionDate="2007-06-27" xml:lang="en">absolute number, e.g. 21, 21.5</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 21, 21.5와 같은 절대값</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">絕對數，例如21、21.5</desc>
          <desc versionDate="2008-04-06" xml:lang="es">número absoluto, p.ej. 21, 21,5</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">基数。例えば、21、21.5など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">nombre entier ou décimal, par exemple 21, 21.5</desc>
          <desc versionDate="2007-01-21" xml:lang="it">numero assoluto, ad esempio 21 o 21,5.</desc>
          <desc versionDate="2016-11-25" xml:lang="de">Kardinalzahl, z. B. 21, 21,5</desc>
        </valItem>
        <valItem ident="ordinal">
          <desc versionDate="2007-06-27" xml:lang="en">ordinal number, e.g. 21st</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 21번째와 같은 서수</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">序數，例如第21</desc>
          <desc versionDate="2008-04-06" xml:lang="es">número ordinal, p.ej. 21º</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">序数。例えば、21番など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">nombre ordinal, par exemple 21ème</desc>
          <desc versionDate="2007-01-21" xml:lang="it">numero ordinale, ad esempio 21°</desc>
          <desc versionDate="2016-11-25" xml:lang="de">Ordinalzahl, z. B. 21., fünfter</desc>  
        </valItem>
        <valItem ident="fraction">
          <desc versionDate="2007-06-27" xml:lang="en">fraction, e.g. one half or three-quarters</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 1/2 또는 3/4와 같은 분수</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">分數，例如二分之一或是四分之三</desc>
          <desc versionDate="2008-04-06" xml:lang="es">fracción,p.ej. una mitad o tres cuartos</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">割合。例えば、1/2、3/4など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">fraction, par exemple une moitié ou trois-quarts</desc>
          <desc versionDate="2007-01-21" xml:lang="it">frazione, ad esempio un terzo o tre quarti.</desc>
          <desc versionDate="2016-11-25" xml:lang="de">Bruchzahl, z. B. 1/2 oder drei Viertel</desc>
        </valItem>
        <valItem ident="percentage">
          <desc versionDate="2007-06-27" xml:lang="en">a percentage</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">백분율</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">百分比</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un porcentaje</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">パーセント。百分率。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">un pourcentage</desc>
          <desc versionDate="2007-01-21" xml:lang="it">percentuale.</desc>
          <desc versionDate="2016-11-25" xml:lang="de">Prozentangabe</desc>
        </valItem>
      </valList>
      <remarks ident="num-attr.type-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If a different typology is desired, other values can be used for this
                attribute.</p>
      </remarks>
      <remarks ident="num-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si une autre typologie est souhaitée, d'autres valeurs peuvent être utilisées
                    pour cet attribut.</p>
      </remarks>
      <remarks ident="num-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 上記とは別の分類が必要であれば、それを使うことができる。 </p>
      </remarks>
      <remarks ident="num-attr.type-remarks" versionDate="2016-11-25" xml:lang="de">
          <p>Je nach gewünschter Typologie können andere Werte für dieses Attribut verwendet werden.</p>
      </remarks>
    </attDef>
    <attDef ident="value" usage="opt">
      <desc versionDate="2005-11-01" xml:lang="en">supplies the value of the number in standard form.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">표준형의 숫자 값을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用標準形式來說明該數字所代表的值。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">標準的な形式で数値を示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">fournit la valeur d'un nombre sous une forme normalisée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el valor del número de forma
                estándard.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il valore del numero in formato standard.</desc>
      <desc versionDate="2016-11-25" xml:lang="de">beinhaltet den Zahlenwert in standardisierter Form.</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
      <valDesc>a numeric value.</valDesc>
      <valDesc xml:lang="fr">une valeur numérique.</valDesc>
      <valDesc xml:lang="de">ein numerischer Wert</valDesc>
      <remarks ident="num-attr.value-remarks" versionDate="2005-11-01" xml:lang="en">
        <p>The standard form used is defined by the TEI datatype <ident type="datatype">teidata.numeric</ident>.</p>
      </remarks>
      <remarks ident="num-attr.value-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La forme normalisée utilisée est définie par le type de données TEI
                qui concerne les données numériques.</p>
      </remarks>
      <remarks ident="num-attr.value-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 標準的な形式は、TEIデータ型teidata.numericで定義されている。 </p>
      </remarks>
      <remarks ident="num-attr.value-remarks" versionDate="2016-11-25" xml:lang="de">
          <p>Die benutzte standardisierte Form wird im TEI-Datentyp <ident type="datatype">teidata.numeric</ident> definiert.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-num-egXML-en">
      <p>I reached <num type="cardinal" value="21">twenty-one</num> on
my <num type="ordinal" value="21">twenty-first</num> birthday</p>
      <p>Light travels at <num value="3E10">3×10<hi rend="sup">10</hi>
            </num> cm per second.</p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-num-egXML-ts">
      <p>Pierre eut <num type="cardinal" value="10">dix</num>ans le jour de mon<num type="ordinal" value="21">vingtième </num> anniversaire.</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-num-egXML-ii">
      <p>在<num type="ordinal" value="21">第二十一</num>歲的生日那天，我變成<num type="cardinal" value="21">二十一</num>歲了... 光以每秒<num value="10E10">10<hi rend="sup">10</hi>
            </num> 公分移動。</p>
    </egXML>
  </exemplum>
  <remarks ident="num-remarks" versionDate="2005-11-01" xml:lang="en">
    <p>Detailed analyses of quantities and units of measure in historical documents may also use
            the feature structure mechanism described in chapter <ptr target="#FS"/>. The
            <gi>num</gi> element is intended for use in simple applications.</p>
  </remarks>
  <remarks ident="num-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les analyses détaillées des quantités et unités de mesure dans les textes historiques
      peuvent aussi utiliser le mécanisme de structure de traits décrit au chapitre<ptr target="#FS"/>. 
            L'élément <gi>num</gi> est conçu pour un usage dans des applications simples.</p>
  </remarks>
  <remarks ident="num-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 歴史的文書の量や大きさの詳細な分析には、<ptr target="#FS"/>で解説 されている素性構造機能を使うことになるかもしれない。
            当該要素<gi>num</gi>は、簡単なソフトウェアで使われることが想定され ている。 </p>
  </remarks>
  <remarks ident="num-remarks" versionDate="2016-11-25" xml:lang="de">
      <p>
          Detaillierte Analysen von Mengen und Maßeinheiten in historischen Dokumenten können auch den 'feature structure' 
          Mechanismus verwenden, wie in Kapitel <ptr target="#FS"/> beschrieben. Das <gi>num</gi>-Element ist für 
          einfache Anwendungen vorgesehen.
      </p>
  </remarks>
  <listRef>
    <ptr target="#CONANU" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">number</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">숫자</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">數字</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">numéral</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">número</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">numero</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Zahl</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a number, written in any form.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다양한 형식의 숫자를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個以任何形式呈現的數字。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">各種形式による数値を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient un nombre écrit sous une forme quelconque.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un número, escrito en cualquier forma.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un numero in qualsiasi forma.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">beinhaltet eine Zahl, die auf beliebige Art geschrieben sein kann.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.ranging"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.measureLike"/>
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

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the type of numeric value.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수치의 유형을 나타낸다.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出數值的種類。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">数値の種類を示す。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">indique le type de valeur numérique.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el tipo de valor numérico.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il tipo di valore numerico.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">bestimmt die Art des numerischen Wertes.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="cardinal">
          <desc versionDate="2007-06-27" xml:lang="en">absolute number, e.g. 21, 21.5</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 21, 21.5와 같은 절대값</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">絕對數，例如21、21.5</desc>
          <desc versionDate="2008-04-06" xml:lang="es">número absoluto, p.ej. 21, 21,5</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">基数。例えば、21、21.5など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">nombre entier ou décimal, par exemple 21, 21.5</desc>
          <desc versionDate="2007-01-21" xml:lang="it">numero assoluto, ad esempio 21 o 21,5.</desc>
          <desc versionDate="2016-11-25" xml:lang="de">Kardinalzahl, z. B. 21, 21,5</desc>
        </valItem>
        <valItem ident="ordinal">
          <desc versionDate="2007-06-27" xml:lang="en">ordinal number, e.g. 21st</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 21번째와 같은 서수</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">序數，例如第21</desc>
          <desc versionDate="2008-04-06" xml:lang="es">número ordinal, p.ej. 21º</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">序数。例えば、21番など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">nombre ordinal, par exemple 21ème</desc>
          <desc versionDate="2007-01-21" xml:lang="it">numero ordinale, ad esempio 21°</desc>
          <desc versionDate="2016-11-25" xml:lang="de">Ordinalzahl, z. B. 21., fünfter</desc>  
        </valItem>
        <valItem ident="fraction">
          <desc versionDate="2007-06-27" xml:lang="en">fraction, e.g. one half or three-quarters</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 1/2 또는 3/4와 같은 분수</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">分數，例如二分之一或是四分之三</desc>
          <desc versionDate="2008-04-06" xml:lang="es">fracción,p.ej. una mitad o tres cuartos</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">割合。例えば、1/2、3/4など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">fraction, par exemple une moitié ou trois-quarts</desc>
          <desc versionDate="2007-01-21" xml:lang="it">frazione, ad esempio un terzo o tre quarti.</desc>
          <desc versionDate="2016-11-25" xml:lang="de">Bruchzahl, z. B. 1/2 oder drei Viertel</desc>
        </valItem>
        <valItem ident="percentage">
          <desc versionDate="2007-06-27" xml:lang="en">a percentage</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">백분율</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">百分比</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un porcentaje</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">パーセント。百分率。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">un pourcentage</desc>
          <desc versionDate="2007-01-21" xml:lang="it">percentuale.</desc>
          <desc versionDate="2016-11-25" xml:lang="de">Prozentangabe</desc>
        </valItem>
      </valList>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="num-attr.type-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If a different typology is desired, other values can be used for this
                attribute.</p>
      </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="num-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si une autre typologie est souhaitée, d'autres valeurs peuvent être utilisées
                    pour cet attribut.</p>
      </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="num-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 上記とは別の分類が必要であれば、それを使うことができる。 </p>
      </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="num-attr.type-remarks" versionDate="2016-11-25" xml:lang="de">
          <p>Je nach gewünschter Typologie können andere Werte für dieses Attribut verwendet werden.</p>
      </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-11-01" xml:lang="en">supplies the value of the number in standard form.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준형의 숫자 값을 제시한다.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用標準形式來說明該數字所代表的值。</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">標準的な形式で数値を示す。</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">fournit la valeur d'un nombre sous une forme normalisée.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el valor del número de forma
                estándard.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il valore del numero in formato standard.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[8]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">beinhaltet den Zahlenwert in standardisierter Form.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valDesc[1]`.

```xml
<valDesc>a numeric value.</valDesc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valDesc[2]`.

```xml
<valDesc xml:lang="fr">une valeur numérique.</valDesc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valDesc[3]`.

```xml
<valDesc xml:lang="de">ein numerischer Wert</valDesc>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="num-attr.value-remarks" versionDate="2005-11-01" xml:lang="en">
        <p>The standard form used is defined by the TEI datatype <ident type="datatype">teidata.numeric</ident>.</p>
      </remarks>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="num-attr.value-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La forme normalisée utilisée est définie par le type de données TEI
                qui concerne les données numériques.</p>
      </remarks>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="num-attr.value-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 標準的な形式は、TEIデータ型teidata.numericで定義されている。 </p>
      </remarks>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="num-attr.value-remarks" versionDate="2016-11-25" xml:lang="de">
          <p>Die benutzte standardisierte Form wird im TEI-Datentyp <ident type="datatype">teidata.numeric</ident> definiert.</p>
      </remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-num-egXML-en">
      <p>I reached <num type="cardinal" value="21">twenty-one</num> on
my <num type="ordinal" value="21">twenty-first</num> birthday</p>
      <p>Light travels at <num value="3E10">3×10<hi rend="sup">10</hi>
            </num> cm per second.</p>
    </egXML>
  </exemplum>
```

^b48

### Block 49

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-num-egXML-ts">
      <p>Pierre eut <num type="cardinal" value="10">dix</num>ans le jour de mon<num type="ordinal" value="21">vingtième </num> anniversaire.</p>
    </egXML>
  </exemplum>
```

^b49

### Block 50

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-num-egXML-ii">
      <p>在<num type="ordinal" value="21">第二十一</num>歲的生日那天，我變成<num type="cardinal" value="21">二十一</num>歲了... 光以每秒<num value="10E10">10<hi rend="sup">10</hi>
            </num> 公分移動。</p>
    </egXML>
  </exemplum>
```

^b50

### Block 51

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="num-remarks" versionDate="2005-11-01" xml:lang="en">
    <p>Detailed analyses of quantities and units of measure in historical documents may also use
            the feature structure mechanism described in chapter <ptr target="#FS"/>. The
            <gi>num</gi> element is intended for use in simple applications.</p>
  </remarks>
```

^b51

### Block 52

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="num-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les analyses détaillées des quantités et unités de mesure dans les textes historiques
      peuvent aussi utiliser le mécanisme de structure de traits décrit au chapitre<ptr target="#FS"/>. 
            L'élément <gi>num</gi> est conçu pour un usage dans des applications simples.</p>
  </remarks>
```

^b52

### Block 53

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="num-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 歴史的文書の量や大きさの詳細な分析には、<ptr target="#FS"/>で解説 されている素性構造機能を使うことになるかもしれない。
            当該要素<gi>num</gi>は、簡単なソフトウェアで使われることが想定され ている。 </p>
  </remarks>
```

^b53

### Block 54

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="num-remarks" versionDate="2016-11-25" xml:lang="de">
      <p>
          Detaillierte Analysen von Mengen und Maßeinheiten in historischen Dokumenten können auch den 'feature structure' 
          Mechanismus verwenden, wie in Kapitel <ptr target="#FS"/> beschrieben. Das <gi>num</gi>-Element ist für 
          einfache Anwendungen vorgesehen.
      </p>
  </remarks>
```

^b54

### Block 55

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONANU" type="div3"/>
  </listRef>
```

^b55

