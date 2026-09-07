---
type: representation
source-type: document
source: '[[00_sources/tei-p5-app-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 app
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/app.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# app

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 13180. Git blob: `0eb1bdfe4c7db3a6f50dc0ddd117353f05bdc22c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-app" ident="app">
  <gloss versionDate="2005-01-14" xml:lang="en">apparatus entry</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">참조 도구 표제 항목</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解項目</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">entrée d'apparat critique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">entrada de aparato crítico</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">voce dell'apparato</gloss>
  <gloss versionDate="2019-01-04" xml:lang="ja">校勘情報</gloss>
  <desc versionDate="2013-10-17" xml:lang="en">contains one entry in a critical apparatus, with an optional
lemma and usually one or more readings or notes on the relevant passage.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">수의적 레마와 적어도 하나의 독법을 포함하여 비평적 참조 도구에서 하나의 표제 항목을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">一項學術編輯註解，內含一個不必備主題以及至少一個對應本。</desc>
  <desc versionDate="2018-12-28" xml:lang="ja">校勘資料中に一つのエントリを含む。関連部分に任意のレンマと、通常1つまたは複数の読みと注釈を持つ。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une entrée dans un apparat critique,
			constituée d'un lemme facultatif et d'au moins une leçon.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una entrada en el aparato crítico, con un lema opcional y, al menos, una lectura.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una singola voce in un apparato critico, con un lemma facoltativo e almeno una lettura.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
  <content>   
    <sequence>
      <elementRef key="lem" minOccurs="0"/>
      <alternate maxOccurs="unbounded" minOccurs="0">
        <classRef key="model.rdgLike"/>
        <classRef key="model.noteLike"/>
        <elementRef key="witDetail"/>
        <elementRef key="wit"/>      
        <elementRef key="rdgGrp"/>      
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">classifies the variation contained in this element according to
some convenient typology.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">다양한 유형에 따라 이 요소에 포함된 변이형을 분류한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">利用合適的分類法將此元素所標記的變異分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素で示される対象を分類する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">classifie la variation contenue dans cet
					élément selon toute typologie adéquate.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">clasifica la variación contenida en tal elemento según una tipología funcional</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica la variazione contenuta in tale elemento secondo una tipologia funzionale.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
    <attDef ident="from" usage="opt">
      <desc versionDate="2013-04-11" xml:lang="en">identifies the beginning of the lemma in the base text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">필요하다면 기본 텍스트에서 레마의 시작을 식별한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">必要情況下，指出基礎文件中該主題的開端。</desc>
      <desc versionDate="2018-12-28" xml:lang="ja">元テキストにおけるレンマの開始点を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">identifie, si nécessaire, le début du
					lemme dans le texte de base.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica, si es necesario, el inicio del lema en el texto base</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica, se necessario, l'inizio del lemma nel testo base.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="app-attr.from-remarks" versionDate="2013-06-18" xml:lang="en">
        <p>This attribute should be used when either the 
          double-end point method of apparatus markup, or the location-referenced 
          method with a URL rather than canonical reference, are used.</p>
      </remarks>
      <remarks ident="app-attr.from-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut n'est utilisé que si l'on emploie la méthode de balisage de
                        l'apparat critique dite "double-end point", c'est-à-dire que l'on indique le
                        début et la fin du bloc de texte balisé. </p>
      </remarks>
      <remarks ident="app-attr.from-remarks" versionDate="2018-12-28" xml:lang="ja"><p>この属性は、校勘資料のマークアップの両端ポイント方式（double-end point method、または正規化された参照ではなくURLを使用する場所参照方式（location-referenced method）のいずれかを使用する場合に使用する必要がある。</p></remarks>
    </attDef>
    <attDef ident="to" usage="opt">
      <desc versionDate="2013-04-11" xml:lang="en">identifies the endpoint of the lemma in the base text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">필요하다면 기본 텍스트에서 레마의 종료지점을 식별한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">必要情況下，指出基礎文件中該主題的結尾。</desc>
      <desc versionDate="2018-12-28" xml:lang="ja">元テキストにおけるレンマの終点を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">identifie, si nécessaire, la fin du lemme
					dans le texte de base.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica, si es necesario, el final del lema en el texto base</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica, se necessario, la fine del lemma nel testo base.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="app-attr.to-remarks" versionDate="2013-06-18" xml:lang="en">
        <p>This attribute is only used when the double-end point
                method of apparatus markup is used, when the encoded apparatus is not
                embedded <term>in-line</term> in the base-text.</p>
      </remarks>
      <remarks ident="app-attr.to-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut n'est utilisé que si l'on emploie la méthode de balisage de
                        l'apparat critique dite "double-end point", avec l'apparat encodé enregistré
                        dans un fichier séparé plutôt qu'incorporé au fil du texte
                        (<term>in-line</term>) dans le fichier du texte de base.</p>
      </remarks>
      <remarks ident="app-attr.to-remarks" versionDate="2018-12-28" xml:lang="ja">
        <p>
          当該属性は、符号化された校勘資料が元テキストの<term>in-line</term>に埋め込まれていない場合、校勘資料中で両端ポイント方式（double-end point method）が使用されている場合にのみ使われる。
    </p>
      </remarks>
    </attDef>
    <attDef ident="loc" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">location</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">위치</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">localización</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">emplacement</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">posizione</gloss>
      <gloss versionDate="2018-12-28" xml:lang="ja">位置</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates the location of the variation, when the
location-referenced method of apparatus markup is used.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">참조 도구 마크업의 위치 참조 방법이 사용될 때 변이형 위치를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">使用學術編輯註解標記的位置參照辦法時，指出變異的位置。</desc>
      <desc versionDate="2022-05-09" xml:lang="ja">校勘資料で location-referenced methodが採られている場合、該当する異文の場所を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique la localisation de la variante
					lorsqu'on utilise dans l'encodage de l'apparat critique une méthode de
					référencement des localisations.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la posición de la variante en caso de usar el método de señalización de la posición de la variante en la codificación del aparato.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la posizione della variante in caso di utilizzo del metodo di indicazione della posizione della variante nella codifica dell'apparato.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
      <remarks ident="app-attr.loc-remarks" versionDate="2013-11-22" xml:lang="en">
        <p>This attribute is used only when the location-referenced
encoding method is used.  It supplies a  string containing a canonical reference for the passage
      to which the variation applies.</p>
      </remarks>
      <remarks ident="app-attr.loc-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut n'est utilisé que si l'on emploie la méthode de codage par
                        référence à un emplacement ("location-referenced").</p>
      </remarks>
      <remarks ident="app-attr.loc-remarks" versionDate="2018-12-28" xml:lang="ja"><p>当該属性は、場所参照（location-referenced）符号化方式が採られている場合にのみ使用される。バリエーションが適用される節のための正規化された参照を含む文字列を提供する。</p></remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-jj" source="#UND">
      <app>
        <lem wit="#El #Hg">Experience</lem>
        <rdg wit="#La" type="substantive">Experiment</rdg>
        <rdg wit="#Ra2" type="substantive">Eryment</rdg>
      </app>
       </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-nd" source="#UND">
      <app type="substantive">
        <rdgGrp type="subvariants">
          <lem wit="#El #Hg">Experience</lem>
          <rdg wit="#Ha4">Experiens</rdg>
        </rdgGrp>
        <rdgGrp type="subvariants">
          <lem wit="#Cp #Ld1">Experiment</lem>
          <rdg wit="#La">Ex<g ref="#per"/>iment</rdg>
        </rdgGrp>
        <rdgGrp type="subvariants">
          <lem resp="#ed2013">Eriment</lem>
          <rdg wit="#Ra2">Eryment</rdg>
        </rdgGrp>
      </app>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-bu">
      <app loc="1">
        <rdg resp="#SEG">TIMΩΔA</rdg>
      </app>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-sh">
      <app loc="1-6">
        <note>Too badly worn to yield a text</note>
      </app>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-xp">
      <choice xml:id="choice3">
        <reg>σύμπαντα</reg>
        <orig>ΣΙΝΠΑΤΑΝ</orig>
      </choice>
      <!-- ... -->
      <app from="#choice3">
        <note>Mommsen's fanciful normalization, reproduced here, has not been accepted by all recent editions</note>
      </app>
    </egXML>
  </exemplum>
  <!--  <remarks>
    <p rend="dataDesc">May contain an optional lemma and one or more readings or
reading groups, each associated with witness specifications.</p>
  </remarks>
  <remarks versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir un lemme facultatif et une ou plusieurs leçons ou
                groupe de leçons, chacune associée à des spécifications de témoin.</p>
  </remarks>
  <remarks versionDate="2008-04-05" xml:lang="ja"><p rend="dataDesc">
    複数の読み，読みのまとまり，ひとつの選択的な対象語(lemma)をとる．
    </p>
  </remarks>-->
  <listRef>
    <ptr target="#TCAPEN"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">apparatus entry</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">참조 도구 표제 항목</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解項目</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">entrée d'apparat critique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">entrada de aparato crítico</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">voce dell'apparato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2019-01-04" xml:lang="ja">校勘情報</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-10-17" xml:lang="en">contains one entry in a critical apparatus, with an optional
lemma and usually one or more readings or notes on the relevant passage.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수의적 레마와 적어도 하나의 독법을 포함하여 비평적 참조 도구에서 하나의 표제 항목을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">一項學術編輯註解，內含一個不必備主題以及至少一個對應本。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">校勘資料中に一つのエントリを含む。関連部分に任意のレンマと、通常1つまたは複数の読みと注釈を持つ。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une entrée dans un apparat critique,
			constituée d'un lemme facultatif et d'au moins une leçon.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una entrada en el aparato crítico, con un lema opcional y, al menos, una lectura.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una singola voce in un apparato critico, con un lemma facoltativo e almeno una lettura.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>   
    <sequence>
      <elementRef key="lem" minOccurs="0"/>
      <alternate maxOccurs="unbounded" minOccurs="0">
        <classRef key="model.rdgLike"/>
        <classRef key="model.noteLike"/>
        <elementRef key="witDetail"/>
        <elementRef key="wit"/>      
        <elementRef key="rdgGrp"/>      
      </alternate>
    </sequence>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">classifies the variation contained in this element according to
some convenient typology.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다양한 유형에 따라 이 요소에 포함된 변이형을 분류한다.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">利用合適的分類法將此元素所標記的變異分類。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素で示される対象を分類する。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">classifie la variation contenue dans cet
					élément selon toute typologie adéquate.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clasifica la variación contenida en tal elemento según una tipología funcional</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica la variazione contenuta in tale elemento secondo una tipologia funzionale.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-04-11" xml:lang="en">identifies the beginning of the lemma in the base text.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">필요하다면 기본 텍스트에서 레마의 시작을 식별한다.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">必要情況下，指出基礎文件中該主題的開端。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">元テキストにおけるレンマの開始点を示す。</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">identifie, si nécessaire, le début du
					lemme dans le texte de base.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica, si es necesario, el inicio del lema en el texto base</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica, se necessario, l'inizio del lemma nel testo base.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="app-attr.from-remarks" versionDate="2013-06-18" xml:lang="en">
        <p>This attribute should be used when either the 
          double-end point method of apparatus markup, or the location-referenced 
          method with a URL rather than canonical reference, are used.</p>
      </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="app-attr.from-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut n'est utilisé que si l'on emploie la méthode de balisage de
                        l'apparat critique dite "double-end point", c'est-à-dire que l'on indique le
                        début et la fin du bloc de texte balisé. </p>
      </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="app-attr.from-remarks" versionDate="2018-12-28" xml:lang="ja"><p>この属性は、校勘資料のマークアップの両端ポイント方式（double-end point method、または正規化された参照ではなくURLを使用する場所参照方式（location-referenced method）のいずれかを使用する場合に使用する必要がある。</p></remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2013-04-11" xml:lang="en">identifies the endpoint of the lemma in the base text.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">필요하다면 기본 텍스트에서 레마의 종료지점을 식별한다.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">必要情況下，指出基礎文件中該主題的結尾。</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">元テキストにおけるレンマの終点を示す。</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">identifie, si nécessaire, la fin du lemme
					dans le texte de base.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica, si es necesario, el final del lema en el texto base</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica, se necessario, la fine del lemma nel testo base.</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="app-attr.to-remarks" versionDate="2013-06-18" xml:lang="en">
        <p>This attribute is only used when the double-end point
                method of apparatus markup is used, when the encoded apparatus is not
                embedded <term>in-line</term> in the base-text.</p>
      </remarks>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="app-attr.to-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut n'est utilisé que si l'on emploie la méthode de balisage de
                        l'apparat critique dite "double-end point", avec l'apparat encodé enregistré
                        dans un fichier séparé plutôt qu'incorporé au fil du texte
                        (<term>in-line</term>) dans le fichier du texte de base.</p>
      </remarks>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="app-attr.to-remarks" versionDate="2018-12-28" xml:lang="ja">
        <p>
          当該属性は、符号化された校勘資料が元テキストの<term>in-line</term>に埋め込まれていない場合、校勘資料中で両端ポイント方式（double-end point method）が使用されている場合にのみ使われる。
    </p>
      </remarks>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">location</gloss>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">위치</gloss>
```

^b48

### Block 49

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">localización</gloss>
```

^b49

### Block 50

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">emplacement</gloss>
```

^b50

### Block 51

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">posizione</gloss>
```

^b51

### Block 52

XML location: `/elementSpec[1]/attList[1]/attDef[4]/gloss[6]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">位置</gloss>
```

^b52

### Block 53

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the location of the variation, when the
location-referenced method of apparatus markup is used.</desc>
```

^b53

### Block 54

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참조 도구 마크업의 위치 참조 방법이 사용될 때 변이형 위치를 나타낸다.</desc>
```

^b54

### Block 55

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">使用學術編輯註解標記的位置參照辦法時，指出變異的位置。</desc>
```

^b55

### Block 56

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2022-05-09" xml:lang="ja">校勘資料で location-referenced methodが採られている場合、該当する異文の場所を示す。</desc>
```

^b56

### Block 57

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique la localisation de la variante
					lorsqu'on utilise dans l'encodage de l'apparat critique une méthode de
					référencement des localisations.</desc>
```

^b57

### Block 58

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la posición de la variante en caso de usar el método de señalización de la posición de la variante en la codificación del aparato.</desc>
```

^b58

### Block 59

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la posizione della variante in caso di utilizzo del metodo di indicazione della posizione della variante nella codifica dell'apparato.</desc>
```

^b59

### Block 60

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b60

### Block 61

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[1]`.

```xml
<remarks ident="app-attr.loc-remarks" versionDate="2013-11-22" xml:lang="en">
        <p>This attribute is used only when the location-referenced
encoding method is used.  It supplies a  string containing a canonical reference for the passage
      to which the variation applies.</p>
      </remarks>
```

^b61

### Block 62

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[2]`.

```xml
<remarks ident="app-attr.loc-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Cet attribut n'est utilisé que si l'on emploie la méthode de codage par
                        référence à un emplacement ("location-referenced").</p>
      </remarks>
```

^b62

### Block 63

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[3]`.

```xml
<remarks ident="app-attr.loc-remarks" versionDate="2018-12-28" xml:lang="ja"><p>当該属性は、場所参照（location-referenced）符号化方式が採られている場合にのみ使用される。バリエーションが適用される節のための正規化された参照を含む文字列を提供する。</p></remarks>
```

^b63

### Block 64

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-jj" source="#UND">
      <app>
        <lem wit="#El #Hg">Experience</lem>
        <rdg wit="#La" type="substantive">Experiment</rdg>
        <rdg wit="#Ra2" type="substantive">Eryment</rdg>
      </app>
       </egXML>
  </exemplum>
```

^b64

### Block 65

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-nd" source="#UND">
      <app type="substantive">
        <rdgGrp type="subvariants">
          <lem wit="#El #Hg">Experience</lem>
          <rdg wit="#Ha4">Experiens</rdg>
        </rdgGrp>
        <rdgGrp type="subvariants">
          <lem wit="#Cp #Ld1">Experiment</lem>
          <rdg wit="#La">Ex<g ref="#per"/>iment</rdg>
        </rdgGrp>
        <rdgGrp type="subvariants">
          <lem resp="#ed2013">Eriment</lem>
          <rdg wit="#Ra2">Eryment</rdg>
        </rdgGrp>
      </app>
    </egXML>
  </exemplum>
```

^b65

### Block 66

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-bu">
      <app loc="1">
        <rdg resp="#SEG">TIMΩΔA</rdg>
      </app>
    </egXML>
  </exemplum>
```

^b66

### Block 67

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-sh">
      <app loc="1-6">
        <note>Too badly worn to yield a text</note>
      </app>
    </egXML>
  </exemplum>
```

^b67

### Block 68

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-app-egXML-xp">
      <choice xml:id="choice3">
        <reg>σύμπαντα</reg>
        <orig>ΣΙΝΠΑΤΑΝ</orig>
      </choice>
      <!-- ... -->
      <app from="#choice3">
        <note>Mommsen's fanciful normalization, reproduced here, has not been accepted by all recent editions</note>
      </app>
    </egXML>
  </exemplum>
```

^b68

### Block 69

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPEN"/>
  </listRef>
```

^b69

