---
type: representation
source-type: document
source: '[[00_sources/tei-p5-if-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 if
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/if.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# if

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3759. Git blob: `3dea77b4090fb87e79924d2590431cdad0a60f21`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-if" ident="if">
  <desc versionDate="2005-01-14" xml:lang="en">defines a conditional default value for a feature; the condition
is specified as a feature structure, and is met if it
subsumes the feature structure in the text for which a
default value is sought.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">자질에 대한 조건부 기본 값을 정의한다: 조건은 자질구조로 명시되며, 기본 값을 요구하는 텍스트의 자질 구조를 포섭한다면 그 조건은 부합한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義一個功能的條件預設值；該條件被指明為一個功能結構，且若在需要預設值的文本中包含該功能結構時，則表示條件符合。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性の条件におけるデフォルト値を定義する。当該値には、素性構造が指定
  される。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">définit une valeur conditionnelle par défaut pour un
      trait ; la condition est indiquée comme une structure de traits et remplie si elle
      englobe la structure de traits dans le texte pour lequel on cherche une valeur par
    défaut.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define un valor predeterminado condicional para un rasgo; la condición se especifica como una estructura de rasgo, y se da si la estructura de rasgo se incluye en el texto para el que un valor predeterminado se ha dado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un valore predefinito condizionato di un tratto; la condizione è specificata come una struttura di tratti e se riscontrata sussume la struttura dei tratti nel testo per il quale si cerca un valore predefinito.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      <alternate>
        <elementRef key="fs"/>
        <elementRef key="f"/>
      </alternate>
      <elementRef key="then"/>
      
        <classRef key="model.featureVal"/>
      
    </sequence>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-if-egXML-vd" source="#UND">
      <vDefault>
        <if>
          <fs>
            <f name="VFORM">
              <symbol value="INF"/>
            </f>
            <f name="SUBJ">
              <binary value="true"/>
            </f>
          </fs>
          <then/>
          <symbol value="for"/>
        </if>
      </vDefault>
    </egXML>
  </exemplum>
  <remarks ident="if-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain a feature structure, followed by a feature value;
the two are separated by a <gi>then</gi> element.</p>
    <p/>
  </remarks>
  <remarks ident="if-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une structure de traits suivie d'une valeur de trait ;
                les deux sont séparées par un élément <gi>then</gi>.</p>
  </remarks>
  <remarks ident="if-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    素性構造と素性値が示されるかもしれない。この2つの値は、要素
    <gi>then</gi>で分けられる。
    </p>
    <p/>
  </remarks>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">defines a conditional default value for a feature; the condition
is specified as a feature structure, and is met if it
subsumes the feature structure in the text for which a
default value is sought.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질에 대한 조건부 기본 값을 정의한다: 조건은 자질구조로 명시되며, 기본 값을 요구하는 텍스트의 자질 구조를 포섭한다면 그 조건은 부합한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義一個功能的條件預設值；該條件被指明為一個功能結構，且若在需要預設值的文本中包含該功能結構時，則表示條件符合。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性の条件におけるデフォルト値を定義する。当該値には、素性構造が指定
  される。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">définit une valeur conditionnelle par défaut pour un
      trait ; la condition est indiquée comme une structure de traits et remplie si elle
      englobe la structure de traits dans le texte pour lequel on cherche une valeur par
    défaut.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define un valor predeterminado condicional para un rasgo; la condición se especifica como una estructura de rasgo, y se da si la estructura de rasgo se incluye en el texto para el que un valor predeterminado se ha dado.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un valore predefinito condizionato di un tratto; la condizione è specificata come una struttura di tratti e se riscontrata sussume la struttura dei tratti nel testo per il quale si cerca un valore predefinito.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate>
        <elementRef key="fs"/>
        <elementRef key="f"/>
      </alternate>
      <elementRef key="then"/>
      
        <classRef key="model.featureVal"/>
      
    </sequence>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-if-egXML-vd" source="#UND">
      <vDefault>
        <if>
          <fs>
            <f name="VFORM">
              <symbol value="INF"/>
            </f>
            <f name="SUBJ">
              <binary value="true"/>
            </f>
          </fs>
          <then/>
          <symbol value="for"/>
        </if>
      </vDefault>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="if-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain a feature structure, followed by a feature value;
the two are separated by a <gi>then</gi> element.</p>
    <p/>
  </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="if-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une structure de traits suivie d'une valeur de trait ;
                les deux sont séparées par un élément <gi>then</gi>.</p>
  </remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="if-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    素性構造と素性値が示されるかもしれない。この2つの値は、要素
    <gi>then</gi>で分けられる。
    </p>
    <p/>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b14

