---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fsdlink-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fsdLink
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fsdLink.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fsdLink

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5107. Git blob: `56bd017441c2efab90a7382c7fb2f5fe2af51745`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fsdLink" ident="fsdLink">
  <gloss versionDate="2007-09-26" xml:lang="en">feature structure declaration link</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질 구조 선언 연결</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">enlace a la declaración de la estructura de rasgos</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">lien vers la déclaration d'une structure de traits</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">collegamento alla dichiarazione della struttura di tratti</gloss>
  <desc versionDate="2007-09-26" xml:lang="en">associates the name of a typed feature structure with a feature
structure declaration for it.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">자질 구조 선언에 유형화된 자질 구조의 이름을 관련시킨다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">asocia el nombre de una estructura de rasgos dada con una declaración de la estructura de rasgos para ella.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性構造宣言により素性構造の名前を示す。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">associe le nom d'une structure de traits <q>type</q> à
sa déclaration de structure de traits.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">associa il nome di una struttura di tratti alla dichiarazione relativa.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.fsdDeclPart"/>
    </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="type" usage="req">
      <desc versionDate="2007-09-26" xml:lang="en">identifies the type of feature structure to be documented;
      this will be the value of the <att>type</att> attribute on at least one
feature structure.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">기록된 자질 구조의 유형을 식별한다; 이것은 적어도 하나 이상의 자질 구조에 대한 <att>유형</att> 값이 될 것이다.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">解説される素性構造を示す。少なくともひとつの素性構造に関する属性
      <att>type</att>の値が付与される。</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica il tipo di dichiarazione del sistema di tratti attraverso il FSD, sarà il valore dell'attributo <att>type</att> di almeno una struttura di tratti.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica el tipo de estructura de rasgos documentada por el FSD; éste será el valor del atributo <att>type</att> al menos en una estructura de rasgos.</desc>
      <desc versionDate="2009-04-16" xml:lang="fr">identifie le type de structure de traits à documenter ; ce sera la valeur de l’attribut <att>type</att> d’au moins une structure de traits.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
    <attDef ident="target" usage="req">
      <desc versionDate="2007-09-26" xml:lang="en">supplies a pointer to a feature structure declaration
      (<gi>fsDecl</gi>) element within the current document or elsewhere.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">현 문서 내 또는  다른 문서에서 자질 구조 선언 (<gi>fsDecl</gi>) 요소에 대한 포인터를 제공한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona un puntero a una declaración de estructura de rasgos (elemento <gi>fsDecl</gi>) al interno del documento actual u otro.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">素性構造宣言要素(<gi>fsDecl</gi>)へのポインタが示される。</desc>
      <desc versionDate="2009-04-16" xml:lang="fr">fournit un pointeur vers un élément de
        déclaration de structure de traits (<gi>fsDecl</gi>) dans le document courant ou
ailleurs.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">fornisce un puntatore che indica l'elemento relativo alla dichiarazione di una struttura di tratti (fsDecl) all'interno del documento corrente o altrove.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsdLink-egXML-kt" source="#UND">
      <fsdLink type="subentry" target="http://www.example.com/fsdLib.xml#L1234"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsdLink-egXML-sx" source="#UND">
      <fsdLink type="subentry" target="http://www.example.com/fsdLib.xml#L1234"/>
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
<gloss versionDate="2007-09-26" xml:lang="en">feature structure declaration link</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질 구조 선언 연결</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">enlace a la declaración de la estructura de rasgos</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">lien vers la déclaration d'une structure de traits</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">collegamento alla dichiarazione della struttura di tratti</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-26" xml:lang="en">associates the name of a typed feature structure with a feature
structure declaration for it.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질 구조 선언에 유형화된 자질 구조의 이름을 관련시킨다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">asocia el nombre de una estructura de rasgos dada con una declaración de la estructura de rasgos para ella.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性構造宣言により素性構造の名前を示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">associe le nom d'une structure de traits <q>type</q> à
sa déclaration de structure de traits.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">associa il nome di una struttura di tratti alla dichiarazione relativa.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.fsdDeclPart"/>
    </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-09-26" xml:lang="en">identifies the type of feature structure to be documented;
      this will be the value of the <att>type</att> attribute on at least one
feature structure.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기록된 자질 구조의 유형을 식별한다; 이것은 적어도 하나 이상의 자질 구조에 대한 <att>유형</att> 값이 될 것이다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">解説される素性構造を示す。少なくともひとつの素性構造に関する属性
      <att>type</att>の値が付与される。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica il tipo di dichiarazione del sistema di tratti attraverso il FSD, sarà il valore dell'attributo <att>type</att> di almeno una struttura di tratti.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica el tipo de estructura de rasgos documentada por el FSD; éste será el valor del atributo <att>type</att> al menos en una estructura de rasgos.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">identifie le type de structure de traits à documenter ; ce sera la valeur de l’attribut <att>type</att> d’au moins une structure de traits.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-09-26" xml:lang="en">supplies a pointer to a feature structure declaration
      (<gi>fsDecl</gi>) element within the current document or elsewhere.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 문서 내 또는  다른 문서에서 자질 구조 선언 (<gi>fsDecl</gi>) 요소에 대한 포인터를 제공한다.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona un puntero a una declaración de estructura de rasgos (elemento <gi>fsDecl</gi>) al interno del documento actual u otro.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性構造宣言要素(<gi>fsDecl</gi>)へのポインタが示される。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">fournit un pointeur vers un élément de
        déclaration de structure de traits (<gi>fsDecl</gi>) dans le document courant ou
ailleurs.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">fornisce un puntatore che indica l'elemento relativo alla dichiarazione di una struttura di tratti (fsDecl) all'interno del documento corrente o altrove.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsdLink-egXML-kt" source="#UND">
      <fsdLink type="subentry" target="http://www.example.com/fsdLib.xml#L1234"/>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsdLink-egXML-sx" source="#UND">
      <fsdLink type="subentry" target="http://www.example.com/fsdLib.xml#L1234"/>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b30

