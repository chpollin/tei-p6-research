---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.enjamb-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.enjamb
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.enjamb.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.enjamb

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7816. Git blob: `90f3c43e6e83d9ff2472ec6ada126257fcd46d76`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" predeclare="true" module="verse" xml:id="ENJAMB" type="atts" ident="att.enjamb">
  <gloss versionDate="2005-10-10" xml:lang="en">enjambement</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">시행 또는 시구의 뜻의 연속</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">詩句跨行</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">encabalgamiento</gloss>
  <gloss versionDate="2009-05-25" xml:lang="fr">enjambement</gloss>
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes that may be used to indicate enjambement of the parent element.</desc>
  <gloss versionDate="2019-06-08" xml:lang="ja">句またがり</gloss>
  <desc versionDate="2007-12-20" xml:lang="ko"><att>enjamb</att> 속성을 포함하는 요소를 모아놓는다.</desc>
  <desc versionDate="2009-05-25" xml:lang="fr">regroupe les éléments portant l'attribut <att>enjamb</att>.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集帶有屬性<att>enjamb</att>的元素。</desc>
  <desc versionDate="2019-06-16" xml:lang="ja">親要素における句またがりを示す属性を与える。</desc>
  <desc versionDate="2007-05-04" xml:lang="es">comprende los elementos definidos por el atributo <att>enjamb</att></desc>
  <desc versionDate="2007-01-21" xml:lang="it">comprende gli elementi definiti dall'attributo <att>enjamb</att></desc>
  <attList>
    <attDef ident="enjamb" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">enjambement</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">시행 또는 시구의 뜻의 연속</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">encabalgamiento</gloss>
      <gloss versionDate="2009-05-25" xml:lang="fr"> enjambement</gloss>
      <gloss versionDate="2019-06-08" xml:lang="ja">句またがり</gloss>
      <desc versionDate="2005-10-10" xml:lang="en">indicates that the end of a verse line is marked by enjambement.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">시행 또는 시구의 뜻 연속에 의해 표지된 시행의 끝을 표시한다.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">indique que la fin d'un vers est marqué par un enjambement.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出詩行末端帶有詩句跨行的標記。</desc>
      <desc versionDate="2019-06-16" xml:lang="ja">句またがりが起こる行末を示す。</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica que el final de un verso está caracterizada por un encabalgamiento.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica che la fine di un verso è caratterizzata da un enjambement.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="no">
          <desc versionDate="2007-06-27" xml:lang="en">the line is end-stopped</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">행이 끝을 맺는다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該詩句在行尾結束</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el verso contiene un punto y final.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該行が、最終である。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le vers se termine à la fin de la
ligne</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il verso finisce a fine riga.</desc>
        </valItem>
        <valItem ident="yes">
          <desc versionDate="2007-06-27" xml:lang="en">the line in question runs on into the next</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">문제의 행이 다음으로 계속 지속된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該詩句延續到下一詩行</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el verso se encabalga con el siguiente</desc>
          <desc versionDate="2019-06-16" xml:lang="ja">当該行は、次の行へとまたがる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le vers en question continue dans le
suivant</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il verso continua alla riga seguente.</desc>
        </valItem>
        <valItem ident="weak">
          <desc versionDate="2007-06-27" xml:lang="en">the line is weakly enjambed</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">행이 약하게 그 뜻이 이어진다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">詩句弱跨行</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el verso contiene un encabalgamiento suave</desc>
          <desc versionDate="2019-06-16" xml:lang="ja">当該行は、緩くまたがっている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le vers forme un enjambement faible</desc>
          <desc versionDate="2007-01-21" xml:lang="it">enjambement lieve.</desc>
        </valItem>
        <valItem ident="strong">
          <desc versionDate="2007-06-27" xml:lang="en">the line is strongly enjambed</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">행이 강하게 그 뜻이 이어진다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">詩句強跨行</desc>
          <desc versionDate="2019-06-16" xml:lang="ja">当該行は強くまたがっている。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el verso contiene un encabalgamiento abrupto</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le vers forme un enjambement fort</desc>
          <desc versionDate="2007-01-21" xml:lang="it">enjambement forte.</desc>
        </valItem>
      </valList>
      <remarks ident="att.enjamb-attr.enjamb-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>The usual practice will be to give the value <q>yes</q> to
this attribute when enjambement is being marked, or the values
<q>weak</q> and <q>strong</q> if degrees of enjambement are of interest;
if no value is given, however, the attribute does not default to a value
of <q>no</q>; this allows the attribute to be omitted entirely when
enjambement is not of particular interest.</p>
      </remarks>
      <remarks ident="att.enjamb-attr.enjamb-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La pratique courante consiste à donner la valeur <q>yes</q> à cet attribut
                        lorsqu'il existe un enjambement, ou les valeurs <q>weak</q> ou <q>strong</q>
                        s'il est intéressant de noter des degrés d'enjambement. Il n'existe pas de
                        valeur par défaut <q>no</q> ; ceci permet d'omettre totalement l'attribut
                        s'il n'est pas intéressant de noter un enjambement.</p>
      </remarks>
      <remarks ident="att.enjamb-attr.enjamb-remarks" versionDate="2019-06-16" xml:lang="ja"><p>一般的には、句またがりが現れるとことで、当該属性に値<q>yes</q>が付 与される。または、その程度により、値<q>weak</q>か<q>strong</q> が付与される。属性値が付与されていない場合でも、当該属性はデフォルト値として、値<q>no</q>を想定しない。従って、句またがりに関心を置かない場合には、当該属性を省略できる。</p></remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#VESE"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-10-10" xml:lang="en">enjambement</gloss>
```

^b1

### Block 2

XML location: `/classSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">시행 또는 시구의 뜻의 연속</gloss>
```

^b2

### Block 3

XML location: `/classSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">詩句跨行</gloss>
```

^b3

### Block 4

XML location: `/classSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">encabalgamiento</gloss>
```

^b4

### Block 5

XML location: `/classSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2009-05-25" xml:lang="fr">enjambement</gloss>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes that may be used to indicate enjambement of the parent element.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2019-06-08" xml:lang="ja">句またがり</gloss>
```

^b7

### Block 8

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><att>enjamb</att> 속성을 포함하는 요소를 모아놓는다.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">regroupe les éléments portant l'attribut <att>enjamb</att>.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集帶有屬性<att>enjamb</att>的元素。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2019-06-16" xml:lang="ja">親要素における句またがりを示す属性を与える。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">comprende los elementos definidos por el atributo <att>enjamb</att></desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">comprende gli elementi definiti dall'attributo <att>enjamb</att></desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">enjambement</gloss>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">시행 또는 시구의 뜻의 연속</gloss>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">encabalgamiento</gloss>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2009-05-25" xml:lang="fr"> enjambement</gloss>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2019-06-08" xml:lang="ja">句またがり</gloss>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">indicates that the end of a verse line is marked by enjambement.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">시행 또는 시구의 뜻 연속에 의해 표지된 시행의 끝을 표시한다.</desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2009-05-25" xml:lang="fr">indique que la fin d'un vers est marqué par un enjambement.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出詩行末端帶有詩句跨行的標記。</desc>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2019-06-16" xml:lang="ja">句またがりが起こる行末を示す。</desc>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica que el final de un verso está caracterizada por un encabalgamiento.</desc>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica che la fine di un verso è caratterizzata da un enjambement.</desc>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="no">
          <desc versionDate="2007-06-27" xml:lang="en">the line is end-stopped</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">행이 끝을 맺는다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該詩句在行尾結束</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el verso contiene un punto y final.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該行が、最終である。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le vers se termine à la fin de la
ligne</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il verso finisce a fine riga.</desc>
        </valItem>
        <valItem ident="yes">
          <desc versionDate="2007-06-27" xml:lang="en">the line in question runs on into the next</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">문제의 행이 다음으로 계속 지속된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該詩句延續到下一詩行</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el verso se encabalga con el siguiente</desc>
          <desc versionDate="2019-06-16" xml:lang="ja">当該行は、次の行へとまたがる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le vers en question continue dans le
suivant</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il verso continua alla riga seguente.</desc>
        </valItem>
        <valItem ident="weak">
          <desc versionDate="2007-06-27" xml:lang="en">the line is weakly enjambed</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">행이 약하게 그 뜻이 이어진다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">詩句弱跨行</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el verso contiene un encabalgamiento suave</desc>
          <desc versionDate="2019-06-16" xml:lang="ja">当該行は、緩くまたがっている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le vers forme un enjambement faible</desc>
          <desc versionDate="2007-01-21" xml:lang="it">enjambement lieve.</desc>
        </valItem>
        <valItem ident="strong">
          <desc versionDate="2007-06-27" xml:lang="en">the line is strongly enjambed</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">행이 강하게 그 뜻이 이어진다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">詩句強跨行</desc>
          <desc versionDate="2019-06-16" xml:lang="ja">当該行は強くまたがっている。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el verso contiene un encabalgamiento abrupto</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le vers forme un enjambement fort</desc>
          <desc versionDate="2007-01-21" xml:lang="it">enjambement forte.</desc>
        </valItem>
      </valList>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.enjamb-attr.enjamb-remarks" versionDate="2005-10-10" xml:lang="en">
        <p>The usual practice will be to give the value <q>yes</q> to
this attribute when enjambement is being marked, or the values
<q>weak</q> and <q>strong</q> if degrees of enjambement are of interest;
if no value is given, however, the attribute does not default to a value
of <q>no</q>; this allows the attribute to be omitted entirely when
enjambement is not of particular interest.</p>
      </remarks>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.enjamb-attr.enjamb-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La pratique courante consiste à donner la valeur <q>yes</q> à cet attribut
                        lorsqu'il existe un enjambement, ou les valeurs <q>weak</q> ou <q>strong</q>
                        s'il est intéressant de noter des degrés d'enjambement. Il n'existe pas de
                        valeur par défaut <q>no</q> ; ceci permet d'omettre totalement l'attribut
                        s'il n'est pas intéressant de noter un enjambement.</p>
      </remarks>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.enjamb-attr.enjamb-remarks" versionDate="2019-06-16" xml:lang="ja"><p>一般的には、句またがりが現れるとことで、当該属性に値<q>yes</q>が付 与される。または、その程度により、値<q>weak</q>か<q>strong</q> が付与される。属性値が付与されていない場合でも、当該属性はデフォルト値として、値<q>no</q>を想定しない。従って、句またがりに関心を置かない場合には、当該属性を省略できる。</p></remarks>
```

^b30

### Block 31

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#VESE"/>
  </listRef>
```

^b31

