---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.global.rendition-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.global.rendition
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.global.rendition.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.global.rendition

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 15841. Git blob: `529e916ee9b0d5a2579e2e30909fc6e03f3c8415`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" predeclare="true" module="tei" type="atts" xml:id="class-attr-global.rendition" ident="att.global.rendition">
  <desc versionDate="2014-12-02" xml:lang="en">provides rendering attributes common to all elements in the TEI encoding scheme.</desc>
  <desc versionDate="2019-07-21" xml:lang="ja">TEIの符号化スキーマにおけるすべての要素に共通するレンダリング属性を提供する。</desc>
  <classes/>
  <attList>
    <attDef ident="rend" usage="opt">
      <gloss versionDate="2007-07-02" xml:lang="en">rendition</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">번역</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">interpretación</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">interprétation</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">resa</gloss>
      <gloss versionDate="2019-07-21" xml:lang="ja">見た目の表示</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">indicates how the element in question was rendered or presented in the source text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">문제의 요소가 원본 텍스트에 제시된 방법을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該元素如何呈現於來源文件中</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素が、元資料でどのように表示されていたかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique comment l'élément en question a été rendu ou présenté dans le texte source.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica cómo el elemento en cuestión ha sido dado o proporcionado en el texto fuente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica come l'elemento in questione è stato reso o rappresentato nel testo originario</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-ci">
          <head rend="align(center) case(allcaps)"><lb/>To The <lb/>Duchesse <lb/>of <lb/>Newcastle,
            <lb/>On Her <lb/><hi rend="case(mixed)">New Blazing-World</hi>. </head>
        </egXML>
        <!--    <p>
          <note type="cit">From the foreword by William Newcastle in
        Margaret Cavendish, Duchess of Newcastle's <title>The
        description of a new world, called the blazing-world</title>,
        WWP TR00253</note>
        </p>-->
      </exemplum>
      <exemplum versionDate="2010-02-26" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-gy" source="#fr-ex-Belloy">
          <head rend="align(center) case(allcaps)">épître dédicatoire<lb/>à <lb/>Monsieur de Coucy <lb/>
          <lb/>.</head>
        </egXML>
      </exemplum>
      <remarks ident="att.global.rendition-attr.rend-remarks" versionDate="2012-10-24" xml:lang="en">
        <p>These Guidelines make no binding recommendations for the values of the <att>rend</att>
          attribute; the characteristics of visual presentation vary too much from text to text and
          the decision to record or ignore individual characteristics varies too much from project
          to project. Some potentially useful conventions are noted from time to time at appropriate
          points in the Guidelines. The values of the <att>rend</att> attribute are a set of 
	sequence-indeterminate individual tokens separated by whitespace.</p>
      </remarks>
      <remarks ident="att.global.rendition-attr.rend-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Ces Principes directeurs ne font aucune recommandation contraignante pour les valeurs de
          l'attribut <att>rend</att>; les caractéristiques de la présentation visuelle changent trop
          d'un texte à l'autre et la décision d'enregistrer ou d'ignorer des caractéristiques
          individuelles est trop variable d'un projet à l'autre. Quelques conventions
          potentiellement utiles sont notées de temps en temps à des points appropriés dans ces
          Principes directeurs.</p>
      </remarks>
      <remarks ident="att.global.rendition-attr.rend-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Estas guías de consulta no hacen ninguna recomendación obligatoria para los valores del
          atributo <att>rend</att>; las características de la presentación visual varían demasiado
          de texto a texto y la decisión para registrar o para omitir características individuales
          varía demasiado de proyecto a proyecto. Observar algunas convenciones que puedan resultar
          útiles en los puntos indicados en las guías de consulta.</p>
      </remarks>
      <remarks ident="att.global.rendition-attr.rend-remarks" versionDate="2019-07-21" xml:lang="ja"><p>本ガイドラインでは、当該属性<att>rend</att>の値として推奨するものはない。活字化の特徴は様々であり、それらのどれを採用するかはプロジェクトごとでおそろしく異なるからである。当ガイドラインでは、有用な記述法があれば、その都度示すことになっている。<att>rend</att>属性の値は、空白によって区切られる順序不定の個々のトークンの集合である。</p></remarks>
    </attDef>
    <attDef ident="style" usage="opt">
      <desc versionDate="2012-10-05" xml:lang="en">contains an expression in some formal style definition language which defines the rendering or presentation used for this element in the source text.</desc>
      <desc versionDate="2022-05-09" xml:lang="ja">なんらかの形式的スタイル定義言語においてソーステキスト内の当該要素のレンダリングや表示を定義する際の表現を含む。</desc>
      <datatype maxOccurs="1"><dataRef key="teidata.text"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-zu">
          <head style="text-align: center; font-variant: small-caps;"><lb/>To The <lb/>Duchesse <lb/>of <lb/>Newcastle, <lb/>On Her
              <lb/><hi style="font-variant: normal">New Blazing-World</hi>. </head>
        </egXML>
      </exemplum>
      <remarks ident="att.global.rendition-attr.style-remarks" versionDate="2017-07-02" xml:lang="en">
        <p>Unlike the attribute values of <att>rend</att>, which uses
        whitespace as a separator, the <att>style</att> attribute may
        contain whitespace. This attribute is intended for recording
        inline stylistic information concerning the source, not any
        particular output.</p>
        <p>The formal language in which values for this attribute are
        expressed may be specified using the <gi>styleDefDecl</gi>
        element in the TEI header.</p>
        <p>If <att>style</att> and <att>rendition</att> are both
        present on an element, then <att>style</att> overrides or
        complements <att>rendition</att>. <att>style</att> should not
        be used in conjunction with <att>rend</att>, because the
        latter does not employ a formal style definition language.</p>
      </remarks>
      <remarks ident="att.global.rendition-attr.style-remarks" versionDate="2019-07-21" xml:lang="ja">
        <p>空白を区切り記号とする<att>rend</att>の属性値とは異なり、<att>style</att>属性は空白を含んでもよい。この属性は資料における行に埋め込まれたスタイル情報を記録するためのものであり、何らかの出力を対象とするものではない。</p>
        <p>この属性の値を表現する形式言語はTEIヘッダにおいて<gi>styleDefDecl</gi>要素を用いて指定されてもよい。</p>
        <p>もし<att>style</att>と<att>rendition</att>の両方が一つの要素に現れる場合、<att>style</att>は<att>rendition</att>を上書きもしくは補完する。<att>style</att>は<att>rend</att>と同時に用いられるべきではない。後者は形式的なスタイル定義言語を採用しているわけではないから。</p></remarks>
    </attDef>
    <attDef ident="rendition" usage="opt">
      <gloss versionDate="2025-09-15" xml:lang="en">rendition reference</gloss>
      <gloss versionDate="2025-09-15" xml:lang="de">Darstellungsverweis</gloss>
      <gloss versionDate="2026-07-25" xml:lang="fr">référence du rendu</gloss>
      <desc versionDate="2007-09-22" xml:lang="en">points to a description of the rendering or presentation used for this element in the source text.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">원본 텍스트에서 이 요소에 대해 사용된 모양과 제시에 대한 기술을 가리킨다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">indica una descripción de la representación o de la presentación empleada para este elemento en el texto original.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素が示す表現が現れている、元資料のテキスト部分を示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">pointe vers une description du rendu ou de la présentation utilisés pour cet élément dans le texte source.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica una descrizione della resa o della presentazione utilizzate per tale elemento nel testo di partenza</desc>
      <desc versionDate="2025-09-15" xml:lang="de">verweist auf eine Beschreibung der Darstellung oder Präsentation, die für dieses Element im Quelltext verwendet wurde.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-as">
          <head rendition="#ac #sc"><lb/>To The <lb/>Duchesse <lb/>of <lb/>Newcastle, <lb/>On Her
              <lb/><hi rendition="#normal">New Blazing-World</hi>. </head>
          <!-- elsewhere... -->
          <rendition xml:id="sc" scheme="css">font-variant: small-caps</rendition>
          <rendition xml:id="normal" scheme="css">font-variant: normal</rendition>
          <rendition xml:id="ac" scheme="css">text-align: center</rendition>
        </egXML>
      </exemplum>
      <exemplum versionDate="2010-02-26" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-lq" source="#fr-ex-Belloy">
          <head rendition="#ac #sc"><lb/>épître dédicatoire <lb/>à <lb/>Monsieur de Coucy <lb/>
               </head>
          <rendition xml:id="fr_sc" scheme="css">font-variant: uppercase</rendition>
          <rendition xml:id="fr_ac" scheme="css">text-align: center</rendition>
        </egXML>
      </exemplum>
      <remarks ident="att.global.rendition-attr.rendition-remarks" versionDate="2017-07-02" xml:lang="en">
        <p>The <att>rendition</att> attribute is used in a very
        similar way to the <att>class</att> attribute defined for
        XHTML but with the important distinction that its function is
        to describe the appearance of the source text, not necessarily
        to determine how that text should be presented on screen or
        paper.</p>
        <p>If <att>rendition</att> is used to refer to a style
        definition in a formal language like CSS, it is recommended
        that it not be used in conjunction with <att>rend</att>.
        <!-- Where both <att>rendition</att> and <att>rend</att> are
        supplied, the latter is understood to override or complement
        the former. --></p>
        <p>Each URI provided should indicate a <gi>rendition</gi>
        element defining the intended rendition in terms of some
        appropriate style language, as indicated by the
        <att>scheme</att> attribute.</p>
      </remarks>
      <remarks ident="att.global.rendition-attr.rendition-remarks" versionDate="2019-07-21" xml:lang="ja">
        <p>属性<att>rendition</att>は、XHTMLの属性<att>class</att>と大変 似たように使用される。但し、重要な違いとして、当該属性は、元資 料の表現を記述するものであり、スクリーン上または紙上でどう表示 されているかを示すものではない。</p>
        <p>もし<att>rendition</att>属性がCSSのような形式言語において定義されるスタイル定義を参照するのに用いられているなら、<att>rend</att>属性と同時に用いないことが推奨される。属性<att>rendition</att>と属性<att>rend</att>の両方が使用されている場合、後者の値が前者の値を上書きする、または補うと判断される。</p>
        <p>当該属性値となるURIは、属性<att>scheme</att>で提示されているス タイル言語により、当該表現を定義する要素<gi>rendition</gi>を示すべきである。</p></remarks>
      <remarks ident="att.global.rendition-attr.rendition-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>L'attribut <att>rendition</att> est employé à peu près de la même manière que l'attribut
            <att>class</att> défini pour XHTML mais avec cette sérieuse différence que sa fonction
          est de décrire la présentation du texte source mais pas nécessairement de déterminer
          comment ce texte doit être représenté à l'écran ou sur le papier. </p>
        <p>Où <att>rendition</att> et <att>rend</att> sont donnés ensembles, il faut comprendre que
          le dernier remplace ou complète le premier.</p>
        <p> Chaque URI fourni doit indiquer un élément <gi>rendition</gi> définissant le rendu prévu
          dans les termes d'un langage approprié pour définir les styles, comme indiqué par
          l'attribut <att>scheme</att>.</p>
      </remarks>
      <remarks ident="att.global.rendition-attr.rendition-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El atributo <att>rendition</att> (interpretación) se utiliza en una manera muy similar al
          atributo <att>clase</att> definido por XHTML pero con una diferencia importante: que su
          función es describir el aspecto del texto original, no necesariamente para determinar la
          presentación visual de ese texto en la pantalla o el papel.</p>
        <p>Donde ambos <att>interpretación</att> y <att>rend</att> se dan, este último se emplea
          para reemplazar o para complementar el anterior.</p>
        <p>Cada URI proporcionado debe indicar al elemento <gi>interpretación</gi> que define la
          interpretación prevista en términos de cualquier lenguaje apropiado del estilo, según lo
          indicado por el atributo <att>scheme</att> (esquema).</p>
      </remarks>
    </attDef>
  </attList>
  <remarks ident="att.global.rendition-remarks" versionDate="2026-01-03" xml:lang="en">
    <p>These guidelines provide no semantic basis or suggested
    precedence when both <att>rend</att> and <att>rendition</att> are
    provided. For this reason simultaneous use of both is not
    recommended for interchange unless documentation explaining the
    use is provided, probably in an ODD customization.</p>
  </remarks>
  <listRef>
    <ptr target="#STGAre"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2014-12-02" xml:lang="en">provides rendering attributes common to all elements in the TEI encoding scheme.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-07-21" xml:lang="ja">TEIの符号化スキーマにおけるすべての要素に共通するレンダリング属性を提供する。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes/>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-02" xml:lang="en">rendition</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">번역</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">interpretación</gloss>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">interprétation</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">resa</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2019-07-21" xml:lang="ja">見た目の表示</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates how the element in question was rendered or presented in the source text.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">문제의 요소가 원본 텍스트에 제시된 방법을 나타낸다.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該元素如何呈現於來源文件中</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素が、元資料でどのように表示されていたかを示す。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique comment l'élément en question a été rendu ou présenté dans le texte source.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica cómo el elemento en cuestión ha sido dado o proporcionado en el texto fuente.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica come l'elemento in questione è stato reso o rappresentato nel testo originario</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-ci">
          <head rend="align(center) case(allcaps)"><lb/>To The <lb/>Duchesse <lb/>of <lb/>Newcastle,
            <lb/>On Her <lb/><hi rend="case(mixed)">New Blazing-World</hi>. </head>
        </egXML>
        <!--    <p>
          <note type="cit">From the foreword by William Newcastle in
        Margaret Cavendish, Duchess of Newcastle's <title>The
        description of a new world, called the blazing-world</title>,
        WWP TR00253</note>
        </p>-->
      </exemplum>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-gy" source="#fr-ex-Belloy">
          <head rend="align(center) case(allcaps)">épître dédicatoire<lb/>à <lb/>Monsieur de Coucy <lb/>
          <lb/>.</head>
        </egXML>
      </exemplum>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.global.rendition-attr.rend-remarks" versionDate="2012-10-24" xml:lang="en">
        <p>These Guidelines make no binding recommendations for the values of the <att>rend</att>
          attribute; the characteristics of visual presentation vary too much from text to text and
          the decision to record or ignore individual characteristics varies too much from project
          to project. Some potentially useful conventions are noted from time to time at appropriate
          points in the Guidelines. The values of the <att>rend</att> attribute are a set of 
	sequence-indeterminate individual tokens separated by whitespace.</p>
      </remarks>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.global.rendition-attr.rend-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Ces Principes directeurs ne font aucune recommandation contraignante pour les valeurs de
          l'attribut <att>rend</att>; les caractéristiques de la présentation visuelle changent trop
          d'un texte à l'autre et la décision d'enregistrer ou d'ignorer des caractéristiques
          individuelles est trop variable d'un projet à l'autre. Quelques conventions
          potentiellement utiles sont notées de temps en temps à des points appropriés dans ces
          Principes directeurs.</p>
      </remarks>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.global.rendition-attr.rend-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Estas guías de consulta no hacen ninguna recomendación obligatoria para los valores del
          atributo <att>rend</att>; las características de la presentación visual varían demasiado
          de texto a texto y la decisión para registrar o para omitir características individuales
          varía demasiado de proyecto a proyecto. Observar algunas convenciones que puedan resultar
          útiles en los puntos indicados en las guías de consulta.</p>
      </remarks>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="att.global.rendition-attr.rend-remarks" versionDate="2019-07-21" xml:lang="ja"><p>本ガイドラインでは、当該属性<att>rend</att>の値として推奨するものはない。活字化の特徴は様々であり、それらのどれを採用するかはプロジェクトごとでおそろしく異なるからである。当ガイドラインでは、有用な記述法があれば、その都度示すことになっている。<att>rend</att>属性の値は、空白によって区切られる順序不定の個々のトークンの集合である。</p></remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2012-10-05" xml:lang="en">contains an expression in some formal style definition language which defines the rendering or presentation used for this element in the source text.</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2022-05-09" xml:lang="ja">なんらかの形式的スタイル定義言語においてソーステキスト内の当該要素のレンダリングや表示を定義する際の表現を含む。</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype maxOccurs="1"><dataRef key="teidata.text"/></datatype>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-zu">
          <head style="text-align: center; font-variant: small-caps;"><lb/>To The <lb/>Duchesse <lb/>of <lb/>Newcastle, <lb/>On Her
              <lb/><hi style="font-variant: normal">New Blazing-World</hi>. </head>
        </egXML>
      </exemplum>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="att.global.rendition-attr.style-remarks" versionDate="2017-07-02" xml:lang="en">
        <p>Unlike the attribute values of <att>rend</att>, which uses
        whitespace as a separator, the <att>style</att> attribute may
        contain whitespace. This attribute is intended for recording
        inline stylistic information concerning the source, not any
        particular output.</p>
        <p>The formal language in which values for this attribute are
        expressed may be specified using the <gi>styleDefDecl</gi>
        element in the TEI header.</p>
        <p>If <att>style</att> and <att>rendition</att> are both
        present on an element, then <att>style</att> overrides or
        complements <att>rendition</att>. <att>style</att> should not
        be used in conjunction with <att>rend</att>, because the
        latter does not employ a formal style definition language.</p>
      </remarks>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="att.global.rendition-attr.style-remarks" versionDate="2019-07-21" xml:lang="ja">
        <p>空白を区切り記号とする<att>rend</att>の属性値とは異なり、<att>style</att>属性は空白を含んでもよい。この属性は資料における行に埋め込まれたスタイル情報を記録するためのものであり、何らかの出力を対象とするものではない。</p>
        <p>この属性の値を表現する形式言語はTEIヘッダにおいて<gi>styleDefDecl</gi>要素を用いて指定されてもよい。</p>
        <p>もし<att>style</att>と<att>rendition</att>の両方が一つの要素に現れる場合、<att>style</att>は<att>rendition</att>を上書きもしくは補完する。<att>style</att>は<att>rend</att>と同時に用いられるべきではない。後者は形式的なスタイル定義言語を採用しているわけではないから。</p></remarks>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2025-09-15" xml:lang="en">rendition reference</gloss>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2025-09-15" xml:lang="de">Darstellungsverweis</gloss>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[3]`.

```xml
<gloss versionDate="2026-07-25" xml:lang="fr">référence du rendu</gloss>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2007-09-22" xml:lang="en">points to a description of the rendering or presentation used for this element in the source text.</desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원본 텍스트에서 이 요소에 대해 사용된 모양과 제시에 대한 기술을 가리킨다.</desc>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">indica una descripción de la representación o de la presentación empleada para este elemento en el texto original.</desc>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素が示す表現が現れている、元資料のテキスト部分を示す。</desc>
```

^b36

### Block 37

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">pointe vers une description du rendu ou de la présentation utilisés pour cet élément dans le texte source.</desc>
```

^b37

### Block 38

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica una descrizione della resa o della presentazione utilizzate per tale elemento nel testo di partenza</desc>
```

^b38

### Block 39

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2025-09-15" xml:lang="de">verweist auf eine Beschreibung der Darstellung oder Präsentation, die für dieses Element im Quelltext verwendet wurde.</desc>
```

^b39

### Block 40

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b40

### Block 41

XML location: `/classSpec[1]/attList[1]/attDef[3]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-as">
          <head rendition="#ac #sc"><lb/>To The <lb/>Duchesse <lb/>of <lb/>Newcastle, <lb/>On Her
              <lb/><hi rendition="#normal">New Blazing-World</hi>. </head>
          <!-- elsewhere... -->
          <rendition xml:id="sc" scheme="css">font-variant: small-caps</rendition>
          <rendition xml:id="normal" scheme="css">font-variant: normal</rendition>
          <rendition xml:id="ac" scheme="css">text-align: center</rendition>
        </egXML>
      </exemplum>
```

^b41

### Block 42

XML location: `/classSpec[1]/attList[1]/attDef[3]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-global.rendition-egXML-lq" source="#fr-ex-Belloy">
          <head rendition="#ac #sc"><lb/>épître dédicatoire <lb/>à <lb/>Monsieur de Coucy <lb/>
               </head>
          <rendition xml:id="fr_sc" scheme="css">font-variant: uppercase</rendition>
          <rendition xml:id="fr_ac" scheme="css">text-align: center</rendition>
        </egXML>
      </exemplum>
```

^b42

### Block 43

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="att.global.rendition-attr.rendition-remarks" versionDate="2017-07-02" xml:lang="en">
        <p>The <att>rendition</att> attribute is used in a very
        similar way to the <att>class</att> attribute defined for
        XHTML but with the important distinction that its function is
        to describe the appearance of the source text, not necessarily
        to determine how that text should be presented on screen or
        paper.</p>
        <p>If <att>rendition</att> is used to refer to a style
        definition in a formal language like CSS, it is recommended
        that it not be used in conjunction with <att>rend</att>.
        <!-- Where both <att>rendition</att> and <att>rend</att> are
        supplied, the latter is understood to override or complement
        the former. --></p>
        <p>Each URI provided should indicate a <gi>rendition</gi>
        element defining the intended rendition in terms of some
        appropriate style language, as indicated by the
        <att>scheme</att> attribute.</p>
      </remarks>
```

^b43

### Block 44

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="att.global.rendition-attr.rendition-remarks" versionDate="2019-07-21" xml:lang="ja">
        <p>属性<att>rendition</att>は、XHTMLの属性<att>class</att>と大変 似たように使用される。但し、重要な違いとして、当該属性は、元資 料の表現を記述するものであり、スクリーン上または紙上でどう表示 されているかを示すものではない。</p>
        <p>もし<att>rendition</att>属性がCSSのような形式言語において定義されるスタイル定義を参照するのに用いられているなら、<att>rend</att>属性と同時に用いないことが推奨される。属性<att>rendition</att>と属性<att>rend</att>の両方が使用されている場合、後者の値が前者の値を上書きする、または補うと判断される。</p>
        <p>当該属性値となるURIは、属性<att>scheme</att>で提示されているス タイル言語により、当該表現を定義する要素<gi>rendition</gi>を示すべきである。</p></remarks>
```

^b44

### Block 45

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="att.global.rendition-attr.rendition-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>L'attribut <att>rendition</att> est employé à peu près de la même manière que l'attribut
            <att>class</att> défini pour XHTML mais avec cette sérieuse différence que sa fonction
          est de décrire la présentation du texte source mais pas nécessairement de déterminer
          comment ce texte doit être représenté à l'écran ou sur le papier. </p>
        <p>Où <att>rendition</att> et <att>rend</att> sont donnés ensembles, il faut comprendre que
          le dernier remplace ou complète le premier.</p>
        <p> Chaque URI fourni doit indiquer un élément <gi>rendition</gi> définissant le rendu prévu
          dans les termes d'un langage approprié pour définir les styles, comme indiqué par
          l'attribut <att>scheme</att>.</p>
      </remarks>
```

^b45

### Block 46

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[4]`.

```xml
<remarks ident="att.global.rendition-attr.rendition-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El atributo <att>rendition</att> (interpretación) se utiliza en una manera muy similar al
          atributo <att>clase</att> definido por XHTML pero con una diferencia importante: que su
          función es describir el aspecto del texto original, no necesariamente para determinar la
          presentación visual de ese texto en la pantalla o el papel.</p>
        <p>Donde ambos <att>interpretación</att> y <att>rend</att> se dan, este último se emplea
          para reemplazar o para complementar el anterior.</p>
        <p>Cada URI proporcionado debe indicar al elemento <gi>interpretación</gi> que define la
          interpretación prevista en términos de cualquier lenguaje apropiado del estilo, según lo
          indicado por el atributo <att>scheme</att> (esquema).</p>
      </remarks>
```

^b46

### Block 47

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.global.rendition-remarks" versionDate="2026-01-03" xml:lang="en">
    <p>These guidelines provide no semantic basis or suggested
    precedence when both <att>rend</att> and <att>rendition</att> are
    provided. For this reason simultaneous use of both is not
    recommended for interchange unless documentation explaining the
    use is provided, probably in an ODD customization.</p>
  </remarks>
```

^b47

### Block 48

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#STGAre"/>
  </listRef>
```

^b48

