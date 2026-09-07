---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fvlib-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fvLib
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fvLib.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fvLib

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4712. Git blob: `cc8026bac95334b015f431cf12e8bcb5ff1c7f30`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fvLib" ident="fvLib">
  <gloss versionDate="2007-07-04" xml:lang="en">feature-value library</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질-값 라이브러리</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能值存庫</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">bibliothèque trait-valeur</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">biblioteca de valores de rasgo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">una biblioteca dei valori dei tratti</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">assembles a library of reusable feature value elements
  (including complete feature structures).</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">(완전한 자질구조를 포함하여) 다시 사용할 수 있는 자질 값 요소를 하나의 라이브러리에 모아놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">可重複使用的功能值元素的集合存庫 (包含完整功能結構) 。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">再利用が可能な素性値をライブラリとしてまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">rassemble une bibliothèque d'éléments trait-valeur
      réutilisables (y compris des structures de traits complètes).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">reúne una biblioteca de elementos de valor de rasgo reutilizables (incluyendo estructuras de rasgo completas).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raccoglie una biblioteca degli elementi dei valori dei tratti riutilizzabili (incluse le strutture complete dei tratti).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.fsdDeclPart"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    
    
        <classRef key="model.featureVal" minOccurs="0" maxOccurs="unbounded"/>
      
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fvLib-egXML-qi" source="#UND">
      <fvLib n="symbolic values">
        <symbol xml:id="sfirst" value="first"/>
        <symbol xml:id="ssecond" value="second"/>
        <!-- ... -->
        <symbol xml:id="ssing" value="singular"/>
        <symbol xml:id="splur" value="plural"/>
        <!-- ... -->
      </fvLib>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fvLib-egXML-zy" source="#UND">
      <fvLib n="symbolic values">
        <symbol xml:id="fr_sfirst" value="first"/>
        <symbol xml:id="fr_ssecond" value="second"/>
        <symbol xml:id="fr_ssing" value="singular"/>
        <symbol xml:id="fr_splur" value="plural"/>
      </fvLib>
    </egXML>
  </exemplum>
  <remarks ident="fvLib-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A feature value library may include any number
  of values of any kind, including multiple occurrences of identical
  values such as <code>&lt;binary value="true"/&gt;</code> or <code>default</code>. The only
  thing guaranteed unique in a feature value library is the set of
  labels used to identify the values. </p>
  </remarks>
  <remarks ident="fvLib-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Une bibliothèque de valeurs de trait peut inclure n'importe quel nombre de valeurs
                quelconques, y compris des occurences multiples de valeurs identiques telles que
                    <code>&lt;binary value="true"/&gt;</code> ou <code>default</code>. La
                seule chose absolument unique dans une bibliothèque de valeurs de trait est
                l'ensemble des étiquettes utilisées pour identifier les valeurs.</p>
  </remarks>
  <remarks ident="fvLib-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    素性値ライブラリには、各種の値がとれる。
    <code>&lt;binary value="true"/&gt;</code>または
    <code>default</code>のような幾度も使用される値をとれる。
    素性値ライブラリ中で唯一ユニーク性が保証されているのは、当該値を指
  定するためのラベル集合である。
   </p>
  </remarks>
  <listRef>
    <ptr target="#FSFL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">feature-value library</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질-값 라이브러리</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能值存庫</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">bibliothèque trait-valeur</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">biblioteca de valores de rasgo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">una biblioteca dei valori dei tratti</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">assembles a library of reusable feature value elements
  (including complete feature structures).</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">(완전한 자질구조를 포함하여) 다시 사용할 수 있는 자질 값 요소를 하나의 라이브러리에 모아놓는다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">可重複使用的功能值元素的集合存庫 (包含完整功能結構) 。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">再利用が可能な素性値をライブラリとしてまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">rassemble une bibliothèque d'éléments trait-valeur
      réutilisables (y compris des structures de traits complètes).</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">reúne una biblioteca de elementos de valor de rasgo reutilizables (incluyendo estructuras de rasgo completas).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raccoglie una biblioteca degli elementi dei valori dei tratti riutilizzabili (incluse le strutture complete dei tratti).</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.fsdDeclPart"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
    
        <classRef key="model.featureVal" minOccurs="0" maxOccurs="unbounded"/>
      
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fvLib-egXML-qi" source="#UND">
      <fvLib n="symbolic values">
        <symbol xml:id="sfirst" value="first"/>
        <symbol xml:id="ssecond" value="second"/>
        <!-- ... -->
        <symbol xml:id="ssing" value="singular"/>
        <symbol xml:id="splur" value="plural"/>
        <!-- ... -->
      </fvLib>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fvLib-egXML-zy" source="#UND">
      <fvLib n="symbolic values">
        <symbol xml:id="fr_sfirst" value="first"/>
        <symbol xml:id="fr_ssecond" value="second"/>
        <symbol xml:id="fr_ssing" value="singular"/>
        <symbol xml:id="fr_splur" value="plural"/>
      </fvLib>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="fvLib-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>A feature value library may include any number
  of values of any kind, including multiple occurrences of identical
  values such as <code>&lt;binary value="true"/&gt;</code> or <code>default</code>. The only
  thing guaranteed unique in a feature value library is the set of
  labels used to identify the values. </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="fvLib-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Une bibliothèque de valeurs de trait peut inclure n'importe quel nombre de valeurs
                quelconques, y compris des occurences multiples de valeurs identiques telles que
                    <code>&lt;binary value="true"/&gt;</code> ou <code>default</code>. La
                seule chose absolument unique dans une bibliothèque de valeurs de trait est
                l'ensemble des étiquettes utilisées pour identifier les valeurs.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="fvLib-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    素性値ライブラリには、各種の値がとれる。
    <code>&lt;binary value="true"/&gt;</code>または
    <code>default</code>のような幾度も使用される値をとれる。
    素性値ライブラリ中で唯一ユニーク性が保証されているのは、当該値を指
  定するためのラベル集合である。
   </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSFL"/>
  </listRef>
```

^b21

