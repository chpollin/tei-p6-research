---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.duration.iso-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.duration.iso
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.duration.iso.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.duration.iso

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5020. Git blob: `07548ce85dbc9ca09e422ae230a2b1dc4f683af8`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" predeclare="true" type="atts" ident="att.duration.iso">
  <desc versionDate="2012-12-26" xml:lang="en">provides attributes for recording normalized temporal durations.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">규격화된 시간적 지속을 기록하기 위한 속성</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">記錄時間長度規格化的屬性</desc>
  <desc versionDate="2019-05-20" xml:lang="ja">正規化された時間幅を記す属性を提供する。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">attributs pour l'enregistrement de durées temporelles normalisées.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">attributi per registrare durate temporali normalizzate.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">atributos para registrar duraciones de tiempo normalizadas.</desc>
  <attList>
    <attDef ident="dur-iso" usage="opt">
      <gloss versionDate="2007-04-09" xml:lang="en">duration</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">지속 기간</gloss>
      <gloss versionDate="2007-05-02" xml:lang="zh-TW">時間長度</gloss>
      <gloss versionDate="2008-12-09" xml:lang="fr">durée</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">durata</gloss>
      <gloss versionDate="2007-05-04" xml:lang="es">duración</gloss>
      <gloss versionDate="2019-05-20" xml:lang="ja">時間幅</gloss>
      <desc versionDate="2007-04-09" xml:lang="en">indicates the length of this element in time.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">시간에서 이 요소의 길이를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出此元素的時間長度。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該時間の長さを示す。</desc>
      <desc versionDate="2008-12-09" xml:lang="fr">indique la longueur de cet élément dans le temps.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica la durata nel tempo dell'elemento.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la longitud de este elemento en el tiempo.</desc>
      <datatype><dataRef key="teidata.duration.iso"/></datatype>
    </attDef>
  </attList>
  <remarks ident="att.duration.iso-remarks" versionDate="2007-06-12" xml:lang="en">
    <p>If both <att>when</att> and <att>dur</att> or <att>dur-iso</att> are specified, the values should be interpreted as indicating a span of
            time by its starting time (or date) and duration. In order to represent a time range by a duration and its ending time the
                <att>when-iso</att> attribute must be used.</p>
    <p>In providing a <soCalled>regularized</soCalled> form, no claim is made that the form in the source text is incorrect; the regularized form
            is simply that chosen as the main form for purposes of unifying variant forms under a single heading.</p>
  </remarks>
  <remarks ident="att.duration.iso-remarks" versionDate="2009-03-19" xml:lang="fr">
    <p>Si les attributs <att>when-iso</att> et <att>dur</att> ou <att>dur-iso</att> sont tous les deux spécifiés, les valeurs doivent être
            interprétées comme indiquant un intervalle de temps au moyen de son point de départ (ou date) et de sa durée. Afin de représenter une
            étendue temporelle par sa durée et sa fin on doit utiliser l'attribut <att>when-iso</att>.</p>
    <p>En fournissant une forme "régularisée", il n'est rien affirmé sur la correction ou l'incorrection de la forme dans le
            texte source ; la forme régularisée est simplement celle qui est choisie comme forme principale afin de réunir les variantes de forme sous
            une seule rubrique.</p>
  </remarks>
  <remarks ident="att.duration.iso-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>when</att>と<att>dur</att>、または属性<att>dur-iso</att> が指定されている場合、その属性値は、開始時間(開始日)と長さとで示さ れる時間幅を示していると解釈されるべきである。
                時間幅とその終了時間を示す場合には、属性<att>when-iso</att>が使わ れる必要がある。 </p>
    <p><soCalled>正規化</soCalled>形式ということで、元テキストにある形式 が不正確であるということを含むものではない。 ここでいう正規化形式とは、単に、ひとつの項目に同じ値を付与すること を目的とするものである。 </p>
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
<desc versionDate="2007-12-20" xml:lang="ko">규격화된 시간적 지속을 기록하기 위한 속성</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">記錄時間長度規格化的屬性</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2019-05-20" xml:lang="ja">正規化された時間幅を記す属性を提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">attributs pour l'enregistrement de durées temporelles normalisées.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">attributi per registrare durate temporali normalizzate.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">atributos para registrar duraciones de tiempo normalizadas.</desc>
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
<gloss versionDate="2007-12-20" xml:lang="ko">지속 기간</gloss>
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
<gloss versionDate="2008-12-09" xml:lang="fr">durée</gloss>
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
<desc versionDate="2007-12-20" xml:lang="ko">시간에서 이 요소의 길이를 나타낸다.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出此元素的時間長度。</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該時間の長さを示す。</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">indique la longueur de cet élément dans le temps.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica la durata nel tempo dell'elemento.</desc>
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
<datatype><dataRef key="teidata.duration.iso"/></datatype>
```

^b22

### Block 23

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.duration.iso-remarks" versionDate="2007-06-12" xml:lang="en">
    <p>If both <att>when</att> and <att>dur</att> or <att>dur-iso</att> are specified, the values should be interpreted as indicating a span of
            time by its starting time (or date) and duration. In order to represent a time range by a duration and its ending time the
                <att>when-iso</att> attribute must be used.</p>
    <p>In providing a <soCalled>regularized</soCalled> form, no claim is made that the form in the source text is incorrect; the regularized form
            is simply that chosen as the main form for purposes of unifying variant forms under a single heading.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.duration.iso-remarks" versionDate="2009-03-19" xml:lang="fr">
    <p>Si les attributs <att>when-iso</att> et <att>dur</att> ou <att>dur-iso</att> sont tous les deux spécifiés, les valeurs doivent être
            interprétées comme indiquant un intervalle de temps au moyen de son point de départ (ou date) et de sa durée. Afin de représenter une
            étendue temporelle par sa durée et sa fin on doit utiliser l'attribut <att>when-iso</att>.</p>
    <p>En fournissant une forme "régularisée", il n'est rien affirmé sur la correction ou l'incorrection de la forme dans le
            texte source ; la forme régularisée est simplement celle qui est choisie comme forme principale afin de réunir les variantes de forme sous
            une seule rubrique.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.duration.iso-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>when</att>と<att>dur</att>、または属性<att>dur-iso</att> が指定されている場合、その属性値は、開始時間(開始日)と長さとで示さ れる時間幅を示していると解釈されるべきである。
                時間幅とその終了時間を示す場合には、属性<att>when-iso</att>が使わ れる必要がある。 </p>
    <p><soCalled>正規化</soCalled>形式ということで、元テキストにある形式 が不正確であるということを含むものではない。 ここでいう正規化形式とは、単に、ひとつの項目に同じ値を付与すること を目的とするものである。 </p>
  </remarks>
```

^b25

### Block 26

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONADA"/>
    <ptr target="#NDDATE"/>
  </listRef>
```

^b26

