---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.duration.w3c-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.duration.w3c
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.duration.w3c.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.duration.w3c

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5742. Git blob: `76eea081fe3b0891a845b205e4801372ed74996f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" predeclare="true" type="atts" ident="att.duration.w3c">
  <desc versionDate="2012-12-26" xml:lang="en">provides attributes for recording normalized temporal durations.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">시간적 지속을 규격화한 녹음에 대한 속성</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">用於記錄時間長度規格化的屬性</desc>
  <desc versionDate="2019-05-20" xml:lang="ja">正規化された時間幅を示す属性を提供する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">attributs pour enregistrer des durées de temps normalisées.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">attributi per la registrazione di durate temporali normalizzate.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">atributos para registrar un periodo temporal normalizado</desc>
  <attList>
    <attDef ident="dur" usage="opt">
      <gloss versionDate="2007-04-09" xml:lang="en">duration</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">지속</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW">時間長度</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">durée</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">durata</gloss>
      <gloss versionDate="2007-05-04" xml:lang="es">duración</gloss>
      <gloss versionDate="2019-05-20" xml:lang="ja">時間幅</gloss>
      <desc versionDate="2007-04-09" xml:lang="en">indicates the length of this element in time.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">시간선상에서 이 요소의 길이를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明此元素的時間長度。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">時間幅を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique la longueur de cet élément dans le temps.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica la durata nel tempo di tale elemento.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la longitud de este elemento en el tiempo.</desc>
      <datatype><dataRef key="teidata.duration.w3c"/></datatype>
    </attDef>
  </attList>
  <remarks ident="att.duration.w3c-remarks" versionDate="2007-06-12" xml:lang="en">
    <p>If both <att>when</att> and <att>dur</att> are specified, the
    values should be interpreted as indicating a span of time by its
    starting time (or date) and duration. In order to represent a time
    range by a duration and its ending time the <att>when-iso</att>
    attribute must be used.</p>
    <p>In providing a <soCalled>regularized</soCalled> form, no claim
    is made that the form in the source text is incorrect; the
    regularized form is simply that chosen as the main form for
    purposes of unifying variant forms under a single heading.</p>
  </remarks>
  <remarks ident="att.duration.w3c-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Si <att>when</att> et <att>dur</att> sont indiqués en même temps, leurs valeurs
                doivent être interprétées comme indiquant un espace de temps à partir de son heure
                (ou date) de départ et de sa durée. Afin de représenter une fourchette de temps par
                une durée et sa fin, l'attribut <att>when-iso</att> doit être employé.</p>
    <p>En fournissant une forme <soCalled>regularized</soCalled>, il n'est rien affrimé sur
                la correction ou l'incorrection de la forme dans le texte source ; la forme
                régularisée est simplement celle qui est choisie comme forme principale afin
                d'unifier les variantes de forme sous une seule rubrique . </p>
  </remarks>
  <remarks ident="att.duration.w3c-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Si ambos, <att>cuando</att> y <att>dur</att>, se especifican, los valores se deben interpretar como indicación de un intervalo de tiempo emtre su hora de salida (o fecha) y la duración. Para representar un intervalo de tiempo por su duración y su conlusión se debe emplear atributo <att>cuando-ISO</att>.
    el atributo debe ser utilizado.</p>
    <p>Para proporcionar una forma <soCalled>regularizada</soCalled>, no se hace ninguna declaración sobre que la forma en el texto original sea incorrecta; la forma regularizada es simplemente elegida como la forma principal con el fin de la unificación de las formas variables bajo el título.</p>
  </remarks>
  <remarks ident="att.duration.w3c-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>when</att>と<att>dur</att>が指定されている場合、その属性
    値は、開始時間(開始日)と長さとで示される時間幅を示していると解釈さ
    れるべきである。時間幅とその終了時間を示す場合には、属性
    <att>when-iso</att>が使われる必要がある。
    </p>
    <p><soCalled>正規化</soCalled>形式ということで、元テキストにある形式
    が不正確であるということを含むものではない。
    ここでいう正規化形式とは、単に、ひとつの項目に同じ値を付与すること
    を目的とするものである。
    </p>
  </remarks>
  <listRef>
    <ptr target="#CONADA"/>
    <ptr target="#NDDATE"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-26" xml:lang="en">provides attributes for recording normalized temporal durations.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시간적 지속을 규격화한 녹음에 대한 속성</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用於記錄時間長度規格化的屬性</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2019-05-20" xml:lang="ja">正規化された時間幅を示す属性を提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">attributs pour enregistrer des durées de temps normalisées.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">attributi per la registrazione di durate temporali normalizzate.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">atributos para registrar un periodo temporal normalizado</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-04-09" xml:lang="en">duration</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">지속</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">時間長度</gloss>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">durée</gloss>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">durata</gloss>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">duración</gloss>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[7]`.

```xml
<gloss versionDate="2019-05-20" xml:lang="ja">時間幅</gloss>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-04-09" xml:lang="en">indicates the length of this element in time.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시간선상에서 이 요소의 길이를 나타낸다.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明此元素的時間長度。</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間幅を示す。</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique la longueur de cet élément dans le temps.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica la durata nel tempo di tale elemento.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la longitud de este elemento en el tiempo.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.duration.w3c"/></datatype>
```

^b22

### Block 23

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.duration.w3c-remarks" versionDate="2007-06-12" xml:lang="en">
    <p>If both <att>when</att> and <att>dur</att> are specified, the
    values should be interpreted as indicating a span of time by its
    starting time (or date) and duration. In order to represent a time
    range by a duration and its ending time the <att>when-iso</att>
    attribute must be used.</p>
    <p>In providing a <soCalled>regularized</soCalled> form, no claim
    is made that the form in the source text is incorrect; the
    regularized form is simply that chosen as the main form for
    purposes of unifying variant forms under a single heading.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.duration.w3c-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Si <att>when</att> et <att>dur</att> sont indiqués en même temps, leurs valeurs
                doivent être interprétées comme indiquant un espace de temps à partir de son heure
                (ou date) de départ et de sa durée. Afin de représenter une fourchette de temps par
                une durée et sa fin, l'attribut <att>when-iso</att> doit être employé.</p>
    <p>En fournissant une forme <soCalled>regularized</soCalled>, il n'est rien affrimé sur
                la correction ou l'incorrection de la forme dans le texte source ; la forme
                régularisée est simplement celle qui est choisie comme forme principale afin
                d'unifier les variantes de forme sous une seule rubrique . </p>
  </remarks>
```

^b24

### Block 25

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.duration.w3c-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Si ambos, <att>cuando</att> y <att>dur</att>, se especifican, los valores se deben interpretar como indicación de un intervalo de tiempo emtre su hora de salida (o fecha) y la duración. Para representar un intervalo de tiempo por su duración y su conlusión se debe emplear atributo <att>cuando-ISO</att>.
    el atributo debe ser utilizado.</p>
    <p>Para proporcionar una forma <soCalled>regularizada</soCalled>, no se hace ninguna declaración sobre que la forma en el texto original sea incorrecta; la forma regularizada es simplemente elegida como la forma principal con el fin de la unificación de las formas variables bajo el título.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="att.duration.w3c-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>when</att>と<att>dur</att>が指定されている場合、その属性
    値は、開始時間(開始日)と長さとで示される時間幅を示していると解釈さ
    れるべきである。時間幅とその終了時間を示す場合には、属性
    <att>when-iso</att>が使われる必要がある。
    </p>
    <p><soCalled>正規化</soCalled>形式ということで、元テキストにある形式
    が不正確であるということを含むものではない。
    ここでいう正規化形式とは、単に、ひとつの項目に同じ値を付与すること
    を目的とするものである。
    </p>
  </remarks>
```

^b26

### Block 27

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONADA"/>
    <ptr target="#NDDATE"/>
  </listRef>
```

^b27

