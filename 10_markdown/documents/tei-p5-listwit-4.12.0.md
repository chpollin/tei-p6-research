---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listwit-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listWit
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listWit.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listWit

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6928. Git blob: `6fbf2795e20833d3cbf3e24cf4ccc361c728f974`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textcrit" xml:id="gi-listWit" ident="listWit">
  <gloss versionDate="2007-09-16" xml:lang="en">witness list</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트 목록</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">liste de témoins</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">lista dei testimoni</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">lista de testimonios</gloss>
  <desc versionDate="2007-09-16" xml:lang="en">lists definitions for all the witnesses referred to by a critical
  apparatus, optionally grouped hierarchically.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">비평적 참조 도구에 의해 참조된 모든 비교 대상 텍스트에 대한 정의 목록. 그리고 이는 계층적 그룹으로 수의적으로 구성된다.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">校勘資料中で参照されている文献の定義のリストを示す。選択的に、グルー
  プとして構造化されている。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">donne une liste de définitions pour tous les
témoignages cités dans un apparat critique, pouvant être groupées de façon hiérarchique.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una lista di tutti i testimoni a cui si fa riferimento negli elementi e attributi relativi ai testimoni nell'apparato critico.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la lista con todos los testimonios a los cuales se hace referencia en los elementos y atributos relativos a los testimonios en el aparato crítico</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.listLike"/>
  </classes>
  <content>
    <sequence>
      <!--      <rng:zeroOrMore>
        <rng:ref name="model.global"/>
      </rng:zeroOrMore>-->
      
        <classRef key="model.headLike" minOccurs="0"/>
        <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>     
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="witness"/>
          <elementRef key="listWit"/>
        </alternate>
        <!--        <rng:zeroOrMore>
          <rng:ref name="model.global"/>
        </rng:zeroOrMore>-->
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listWit-egXML-iq">
      <listWit>
        <witness xml:id="HL26">Ellesmere, Huntingdon Library 26.C.9</witness>
        <witness xml:id="PN392">Hengwrt, National Library of Wales,
   Aberystwyth, Peniarth 392D</witness>
        <witness xml:id="RP149">Bodleian Library Rawlinson Poetic 149
   (see further <ptr target="#MSRP149"/>)</witness>
      </listWit>
    </egXML>
  </exemplum>
  <remarks ident="listWit-remarks" versionDate="2007-09-16" xml:lang="en">
    <p rend="dataDesc">May contain
a series of <gi>witness</gi>  or <gi>listWit</gi> elements.
</p>
    <p>The provision of a <gi>listWit</gi> element simplifies
the automatic processing of the apparatus, e.g. the reconstruction
of the readings for all witnesses from an exhaustive apparatus.</p>
    <p>Situations commonly arise where there are many more or less
fragmentary witnesses, such that there may be quite distinct groups
of witnesses for different parts of a text or collection of
texts. Such groups may be given separately, or nested within a single
<gi>listWit</gi> element at the beginning of the file listing all the
witnesses, partial and complete, for the text, with the attestation
of fragmentary witnesses indicated within the apparatus by use of the
<gi>witStart</gi> and <gi>witEnd</gi> elements described in section
<ptr target="#TCAPMI"/>.</p>
    <p>Note however that a given witness can only be defined once, and can
therefore only appear within a single <gi>listWit</gi> element. </p>
  </remarks>
  <remarks ident="listWit-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une série d'éléments <gi>witness</gi> ou
                <gi>listWit</gi>.</p>
    <p>Fournir un élément <gi>listWit</gi> simplifie le traitement automatique de l'apparat,
                comme par exemple la reconstitution des leçons pour tous les témoins d'un apparat
                exhaustif. </p>
    <p>C'est un cas qui se produit communément lorsqu'il existe de nombreux témoins plus ou
                moins fragmentaires, de sorte qu'il peut y avoir des groupes pratiquement distincts
                de témoins pour différentes parties d'un texte ou d'une collection de textes. On
                peut donner ces groupes séparément ou bien les réunir à l'intérieur d'un seul
                élément <gi>listWit</gi> au début du fichier listant tous les témoins (parcellaires
                ou complets) pour le texte, accompagnés de l'attestation des témoins fragmentaires
                signalés dans l'apparat par l'utilisation des éléments <gi>witStart</gi> et
                    <gi>witEnd</gi> décrits dans la section .</p>
    <p>Noter cependant qu'un témoin donné ne peut être défini qu'une seule fois et ne peut
                donc figurer que dans un seul élément <gi>listWit</gi>. </p>
  </remarks>
  <remarks ident="listWit-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    一連の要素<gi>witness</gi>または<gi>listWit</gi>をとるかもしれない。
    </p>
    <p>
    要素<gi>listWit</gi>は、校勘資料を自動処理を容易にするためのもので
  ある。例えば、ある網羅的な校勘資料から、全文献の読みを自動的に再構築
  する場合である。
  </p>
    <p>
    断片的な文献しかないことはよくあるが、この場合、異なる部分ごとに文
  献やテキストをグループ化することもできる。このグループは独立したもの
  であるか、または全文献がリスト化されているファイルの冒頭において、要
  素<gi>listWit</gi>中で入れ子化されているかもしれない。当該校勘資料中
  で、要素<gi>witStart</gi>と<gi>witEnd</gi>により断片的な文献が示され
  る。この詳細は、<ptr target="#TCAPMI"/>を参照のこと。
  </p>
    <p>
    文献は、ただ1回定義されることに注意すること。下が手、要素
  <gi>listWit</gi>中で1回しか出現しない。
   </p>
  </remarks>
  <listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-09-16" xml:lang="en">witness list</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트 목록</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">liste de témoins</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">lista dei testimoni</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">lista de testimonios</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-16" xml:lang="en">lists definitions for all the witnesses referred to by a critical
  apparatus, optionally grouped hierarchically.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">비평적 참조 도구에 의해 참조된 모든 비교 대상 텍스트에 대한 정의 목록. 그리고 이는 계층적 그룹으로 수의적으로 구성된다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">校勘資料中で参照されている文献の定義のリストを示す。選択的に、グルー
  プとして構造化されている。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">donne une liste de définitions pour tous les
témoignages cités dans un apparat critique, pouvant être groupées de façon hiérarchique.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una lista di tutti i testimoni a cui si fa riferimento negli elementi e attributi relativi ai testimoni nell'apparato critico.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la lista con todos los testimonios a los cuales se hace referencia en los elementos y atributos relativos a los testimonios en el aparato crítico</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.listLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <!--      <rng:zeroOrMore>
        <rng:ref name="model.global"/>
      </rng:zeroOrMore>-->
      
        <classRef key="model.headLike" minOccurs="0"/>
        <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>     
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="witness"/>
          <elementRef key="listWit"/>
        </alternate>
        <!--        <rng:zeroOrMore>
          <rng:ref name="model.global"/>
        </rng:zeroOrMore>-->
      
    </sequence>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listWit-egXML-iq">
      <listWit>
        <witness xml:id="HL26">Ellesmere, Huntingdon Library 26.C.9</witness>
        <witness xml:id="PN392">Hengwrt, National Library of Wales,
   Aberystwyth, Peniarth 392D</witness>
        <witness xml:id="RP149">Bodleian Library Rawlinson Poetic 149
   (see further <ptr target="#MSRP149"/>)</witness>
      </listWit>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listWit-remarks" versionDate="2007-09-16" xml:lang="en">
    <p rend="dataDesc">May contain
a series of <gi>witness</gi>  or <gi>listWit</gi> elements.
</p>
    <p>The provision of a <gi>listWit</gi> element simplifies
the automatic processing of the apparatus, e.g. the reconstruction
of the readings for all witnesses from an exhaustive apparatus.</p>
    <p>Situations commonly arise where there are many more or less
fragmentary witnesses, such that there may be quite distinct groups
of witnesses for different parts of a text or collection of
texts. Such groups may be given separately, or nested within a single
<gi>listWit</gi> element at the beginning of the file listing all the
witnesses, partial and complete, for the text, with the attestation
of fragmentary witnesses indicated within the apparatus by use of the
<gi>witStart</gi> and <gi>witEnd</gi> elements described in section
<ptr target="#TCAPMI"/>.</p>
    <p>Note however that a given witness can only be defined once, and can
therefore only appear within a single <gi>listWit</gi> element. </p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="listWit-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une série d'éléments <gi>witness</gi> ou
                <gi>listWit</gi>.</p>
    <p>Fournir un élément <gi>listWit</gi> simplifie le traitement automatique de l'apparat,
                comme par exemple la reconstitution des leçons pour tous les témoins d'un apparat
                exhaustif. </p>
    <p>C'est un cas qui se produit communément lorsqu'il existe de nombreux témoins plus ou
                moins fragmentaires, de sorte qu'il peut y avoir des groupes pratiquement distincts
                de témoins pour différentes parties d'un texte ou d'une collection de textes. On
                peut donner ces groupes séparément ou bien les réunir à l'intérieur d'un seul
                élément <gi>listWit</gi> au début du fichier listant tous les témoins (parcellaires
                ou complets) pour le texte, accompagnés de l'attestation des témoins fragmentaires
                signalés dans l'apparat par l'utilisation des éléments <gi>witStart</gi> et
                    <gi>witEnd</gi> décrits dans la section .</p>
    <p>Noter cependant qu'un témoin donné ne peut être défini qu'une seule fois et ne peut
                donc figurer que dans un seul élément <gi>listWit</gi>. </p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="listWit-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    一連の要素<gi>witness</gi>または<gi>listWit</gi>をとるかもしれない。
    </p>
    <p>
    要素<gi>listWit</gi>は、校勘資料を自動処理を容易にするためのもので
  ある。例えば、ある網羅的な校勘資料から、全文献の読みを自動的に再構築
  する場合である。
  </p>
    <p>
    断片的な文献しかないことはよくあるが、この場合、異なる部分ごとに文
  献やテキストをグループ化することもできる。このグループは独立したもの
  であるか、または全文献がリスト化されているファイルの冒頭において、要
  素<gi>listWit</gi>中で入れ子化されているかもしれない。当該校勘資料中
  で、要素<gi>witStart</gi>と<gi>witEnd</gi>により断片的な文献が示され
  る。この詳細は、<ptr target="#TCAPMI"/>を参照のこと。
  </p>
    <p>
    文献は、ただ1回定義されることに注意すること。下が手、要素
  <gi>listWit</gi>中で1回しか出現しない。
   </p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TCAPLL"/>
  </listRef>
```

^b18

