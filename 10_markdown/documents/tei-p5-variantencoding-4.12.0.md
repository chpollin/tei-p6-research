---
type: representation
source-type: document
source: '[[00_sources/tei-p5-variantencoding-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 variantEncoding
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/variantEncoding.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# variantEncoding

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12312. Git blob: `974a7f3acafe94170e66c37d8803f4f854fa9369`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="textcrit" xml:id="gi-variantEncoding" ident="variantEncoding">
  <gloss versionDate="2020-12-20" xml:lang="en">variant encoding</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">Méthode d'encodage des variantes</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">declares the method used to encode text-critical variants.</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">sert à déclarer la méthode utilisée pour encoder les variantes critiques du texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 비평 이문을 부호화하는 방법을 선언한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">宣告在標記不同版本中的變異字體時所使用的方法。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">校勘対象を符号化する手法を示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">gibt die Methode an, nach
  der die textkritischen Varianten kodiert sind.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">declara el método empleado para codificar las variantes del aparato crítico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica il metodo adottato per codificare varianti critiche del testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="method" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">indicates which method is used to encode the apparatus of
variants.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique quelle méthode est utilisée pour encoder des variantes dans l’apparat critique.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이문의 참조 도구를 부화하는 방법을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明標記變異的學術編輯註解時所使用的方法。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">異なる校勘資料を符号化する手法を示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">gibt die Methode an, nach
  der textkritische Apparat kodiert ist.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el método seguido para codificar el aparato crítico de las variantes.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il metodo adottato per codificare l'apparato di varianti.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="location-referenced">
          <desc versionDate="2007-06-27" xml:lang="en">apparatus uses line numbers or other canonical reference scheme
referenced in a base text.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">l’apparat critique se réfère aux numéros de ligne ou à tout autre schéma de référence canonique contenu dans le texte de base.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">참조 도구는 기본 텍스트에서 참조된 행 수 또는 다른 표준 참조 스키마를 사용한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解使用基礎文件中被參照的行數或其他標準參照架構。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el aparato emplea números de línea u otro esquema canónico de referencia referidos en el texto base.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">校勘資料の基底テキスト中には、参照される行番号または標準的
          な参照スキームがある。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'apparato utilizza righe numerate o un altro schema di riferimento canonico indicato in un testo base.</desc>
        </valItem>
        <valItem ident="double-end-point">
          <desc versionDate="2007-06-27" xml:lang="en">apparatus indicates the precise locations of the beginning and
ending of each lemma relative to a base text.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">l’apparat critique indique la localisation précise du début et de la fin de chaque lemme dans le texte de base.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">참조 도구는 기본 텍스트에 관하여 각 레마의 시작부와 종료부의 정확한 위치를 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解指出與基礎文件相關的各主題起始與結束的確切位置</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el aparato indica las localizaciones exactas del principio y de la conclusión de cada lema concerniente a un texto base.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">校勘資料の基底テキスト上にある各校合部分の始点と終点の正確な
          場所が示されている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'apparato indica la localizzazione precisa dell'inizio e delle fine di ciascun lemma relativo a un testo base.</desc>
        </valItem>
        <valItem ident="parallel-segmentation">
          <desc versionDate="2007-06-27" xml:lang="en">alternate readings of a passage are given in parallel in the
text; no notion of a base text is necessary.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">différentes leçons d’un passage sont données en parallèle dans le texte ; la notion de texte de base n’est pas nécessaire.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">단락의 교대식 독법은 텍스트에서 병렬로 제시된다. 기본 텍스트의 어떤 개념도 필요하지 않다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文件中一個段落的多個替代讀本以平行方式呈現；不需要基礎文件</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las lecturas alternativs de un pasaje se dan paralelamente en el texto; no es necesaria ninguna noción sobre un texto base necesaria.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">ある一節の別の解釈が、当該テキスト中に併置されている。基底テ
          キストという視点は必要なくなる。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">letture alternative di un brano sono fornite in parallelo nel testo; non è necessaria alcune nozione di un testo base.</desc>
        </valItem>
      </valList>
      <remarks ident="variantEncoding-attr.method-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The value <q>parallel-segmentation</q> requires in-line
encoding of the apparatus.</p>
      </remarks>
      <remarks ident="variantEncoding-attr.method-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <q>parallel-segmentation</q> nécessite un encodage de l'apparat incorporé au texte.</p>
      </remarks>
      <remarks ident="variantEncoding-attr.method-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        値<q>parallel-segmentation</q>は、校勘資料には、インラインで情
        報が記録されていること示す。
        </p>
      </remarks>
    </attDef>
    <attDef ident="location" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether the apparatus appears within the running text
or external to it.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique si l’apparat critique est intérieur ou extérieur au texte.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">참조 도구가 현 텍스트 내에서 또는 그 외부에서 나타나는가를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該學術編輯註解出現在連續文字內部或其外部。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">校合の情報が、本文中、または外部にあるかを示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">gibt an, ob der Apparat
  innerhalb oder außerhalb des Textes erscheint.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el aparato aparece al interno o al externo del texto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se l'apparato compare all'interno del testo, o esternamente.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <constraintSpec ident="variantEncodingLocation" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:variantEncoding">
            <sch:report test="@location eq 'external' and @method eq 'parallel-segmentation'">
              The @location value "external" is inconsistent with the
              parallel-segmentation method of apparatus markup.</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <valList type="closed">
        <valItem ident="internal">
          <desc versionDate="2007-06-27" xml:lang="en">apparatus appears within the running text.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">l’apparat critique est intérieur au texte.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">참조 도구가 현 텍스트 내에서 나타난다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解出現在連續文字內部</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el aparato aparece dentro del texto.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">校合の情報は、本文中にある。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'apparato compare all'interno del testo.</desc>
        </valItem>
        <valItem ident="external">
          <desc versionDate="2007-06-27" xml:lang="en">apparatus appears outside the base text.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">l’apparat critique est extérieur au texte.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">참조 도구가 기본 텍스트 밖에 나타난다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解出現在基礎文件外部</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el aparato aparece fuera del texto base.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">校合の情報は、本文外、すなわち基底テキスト外にある。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'apparato compare esternamente al testo.</desc>
        </valItem>
      </valList>
      <remarks ident="variantEncoding-attr.location-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The value <q>external</q> is inconsistent with the
parallel-segmentation method of apparatus markup.</p>
      </remarks>
      <remarks ident="variantEncoding-attr.location-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <q>external</q> n'est pas compatible avec la méthode de segmentation parallèle.</p>
      </remarks>
      <remarks ident="variantEncoding-attr.location-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        値<q>external</q>は、校勘資料のマークアップがインラインである
        場合と矛盾する。
        </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-variantEncoding-egXML-gn" source="#UND">
      <variantEncoding method="location-referenced" location="external"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-variantEncoding-egXML-cr" source="#UND">
      <variantEncoding method="location-referenced" location="external"/>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TCAPEN"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">variant encoding</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">Méthode d'encodage des variantes</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">declares the method used to encode text-critical variants.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">sert à déclarer la méthode utilisée pour encoder les variantes critiques du texte.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 비평 이문을 부호화하는 방법을 선언한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">宣告在標記不同版本中的變異字體時所使用的方法。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">校勘対象を符号化する手法を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt die Methode an, nach
  der die textkritischen Varianten kodiert sind.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">declara el método empleado para codificar las variantes del aparato crítico.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il metodo adottato per codificare varianti critiche del testo.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates which method is used to encode the apparatus of
variants.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique quelle méthode est utilisée pour encoder des variantes dans l’apparat critique.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이문의 참조 도구를 부화하는 방법을 제시한다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明標記變異的學術編輯註解時所使用的方法。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">異なる校勘資料を符号化する手法を示す。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt die Methode an, nach
  der textkritische Apparat kodiert ist.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el método seguido para codificar el aparato crítico de las variantes.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il metodo adottato per codificare l'apparato di varianti.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="location-referenced">
          <desc versionDate="2007-06-27" xml:lang="en">apparatus uses line numbers or other canonical reference scheme
referenced in a base text.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">l’apparat critique se réfère aux numéros de ligne ou à tout autre schéma de référence canonique contenu dans le texte de base.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">참조 도구는 기본 텍스트에서 참조된 행 수 또는 다른 표준 참조 스키마를 사용한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解使用基礎文件中被參照的行數或其他標準參照架構。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el aparato emplea números de línea u otro esquema canónico de referencia referidos en el texto base.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">校勘資料の基底テキスト中には、参照される行番号または標準的
          な参照スキームがある。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'apparato utilizza righe numerate o un altro schema di riferimento canonico indicato in un testo base.</desc>
        </valItem>
        <valItem ident="double-end-point">
          <desc versionDate="2007-06-27" xml:lang="en">apparatus indicates the precise locations of the beginning and
ending of each lemma relative to a base text.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">l’apparat critique indique la localisation précise du début et de la fin de chaque lemme dans le texte de base.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">참조 도구는 기본 텍스트에 관하여 각 레마의 시작부와 종료부의 정확한 위치를 나타낸다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解指出與基礎文件相關的各主題起始與結束的確切位置</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el aparato indica las localizaciones exactas del principio y de la conclusión de cada lema concerniente a un texto base.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">校勘資料の基底テキスト上にある各校合部分の始点と終点の正確な
          場所が示されている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'apparato indica la localizzazione precisa dell'inizio e delle fine di ciascun lemma relativo a un testo base.</desc>
        </valItem>
        <valItem ident="parallel-segmentation">
          <desc versionDate="2007-06-27" xml:lang="en">alternate readings of a passage are given in parallel in the
text; no notion of a base text is necessary.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">différentes leçons d’un passage sont données en parallèle dans le texte ; la notion de texte de base n’est pas nécessaire.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">단락의 교대식 독법은 텍스트에서 병렬로 제시된다. 기본 텍스트의 어떤 개념도 필요하지 않다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文件中一個段落的多個替代讀本以平行方式呈現；不需要基礎文件</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las lecturas alternativs de un pasaje se dan paralelamente en el texto; no es necesaria ninguna noción sobre un texto base necesaria.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">ある一節の別の解釈が、当該テキスト中に併置されている。基底テ
          キストという視点は必要なくなる。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">letture alternative di un brano sono fornite in parallelo nel testo; non è necessaria alcune nozione di un testo base.</desc>
        </valItem>
      </valList>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="variantEncoding-attr.method-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The value <q>parallel-segmentation</q> requires in-line
encoding of the apparatus.</p>
      </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="variantEncoding-attr.method-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <q>parallel-segmentation</q> nécessite un encodage de l'apparat incorporé au texte.</p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="variantEncoding-attr.method-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        値<q>parallel-segmentation</q>は、校勘資料には、インラインで情
        報が記録されていること示す。
        </p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether the apparatus appears within the running text
or external to it.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique si l’apparat critique est intérieur ou extérieur au texte.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참조 도구가 현 텍스트 내에서 또는 그 외부에서 나타나는가를 표시한다.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該學術編輯註解出現在連續文字內部或其外部。</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">校合の情報が、本文中、または外部にあるかを示す。</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt an, ob der Apparat
  innerhalb oder außerhalb des Textes erscheint.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el aparato aparece al interno o al externo del texto.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se l'apparato compare all'interno del testo, o esternamente.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/constraintSpec[1]`.

```xml
<constraintSpec ident="variantEncodingLocation" scheme="schematron" xml:lang="en">
        <constraint>
          <sch:rule context="tei:variantEncoding">
            <sch:report test="@location eq 'external' and @method eq 'parallel-segmentation'">
              The @location value "external" is inconsistent with the
              parallel-segmentation method of apparatus markup.</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="internal">
          <desc versionDate="2007-06-27" xml:lang="en">apparatus appears within the running text.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">l’apparat critique est intérieur au texte.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">참조 도구가 현 텍스트 내에서 나타난다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解出現在連續文字內部</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el aparato aparece dentro del texto.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">校合の情報は、本文中にある。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'apparato compare all'interno del testo.</desc>
        </valItem>
        <valItem ident="external">
          <desc versionDate="2007-06-27" xml:lang="en">apparatus appears outside the base text.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">l’apparat critique est extérieur au texte.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">참조 도구가 기본 텍스트 밖에 나타난다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">學術編輯註解出現在基礎文件外部</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el aparato aparece fuera del texto base.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">校合の情報は、本文外、すなわち基底テキスト外にある。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">l'apparato compare esternamente al testo.</desc>
        </valItem>
      </valList>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="variantEncoding-attr.location-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>The value <q>external</q> is inconsistent with the
parallel-segmentation method of apparatus markup.</p>
      </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="variantEncoding-attr.location-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <q>external</q> n'est pas compatible avec la méthode de segmentation parallèle.</p>
      </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="variantEncoding-attr.location-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        値<q>external</q>は、校勘資料のマークアップがインラインである
        場合と矛盾する。
        </p>
      </remarks>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-variantEncoding-egXML-gn" source="#UND">
      <variantEncoding method="location-referenced" location="external"/>
    </egXML>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-variantEncoding-egXML-cr" source="#UND">
      <variantEncoding method="location-referenced" location="external"/>
    </egXML>
  </exemplum>
```

^b41

### Block 42

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPEN"/>
  </listRef>
```

^b42

