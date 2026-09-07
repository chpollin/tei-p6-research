---
type: representation
source-type: document
source: '[[00_sources/tei-p5-vdefault-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 vDefault
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/vDefault.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# vDefault

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5883. Git blob: `d068f657c910c246edd4841bfc354da099d015a3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-vDefault" ident="vDefault">
  <gloss versionDate="2005-01-14" xml:lang="en">value default</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">기본 값</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">預設值</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">valeur par défaut</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">valor predeterminado</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">valore predefinito</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">declares the default value to be supplied when a feature structure
does not contain an instance of <gi>f</gi> for this name; if
unconditional, it is specified as one (or, depending on the value of
the <att>org</att> attribute of the enclosing <gi>fDecl</gi>) more
<gi>fs</gi> elements or primitive values;
if conditional, it is specified as
one or more <gi>if</gi> elements; if no default is specified, or no
condition matches, the value <val>none</val> is assumed.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">자질 구조가 이 이름에 대한 자질의 예를 포함하지 않는다면 제시된 기본값을 선언한다. 조건이 미명시되었을 때 하나 이상의 자질구조 요소 또는 원형 값(또는 fDecl의 org 속성 값의 의존하는 값)으로 명시된다; 만약 조건이 명시될 때, 하나 이상의 요소로 명시된다; 만약 기본 값이 명시되지 않는다면 또는 일치하는 조건이 없다면, none 값이 상정된다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在功能結構不包含元素<gi>f</gi>以提供名稱的情況下，宣告使用預設值；若無條件限制，預設值會被指明為一個 (或，取決於所包含的元素<gi>fDecl</gi>中屬性<att>org</att>的屬性值) 多個元素<gi>fs</gi>或原始值；若有條件限制，則被指明為一個或多個元素<gi> if</gi>；若無任何預設值、或無條件符合，則採用屬性值 <val>none</val>。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性構造が要素<gi>f</gi>を持たないときのデフォルト値を宣言する。条件
  的でない場合、要素<gi>fs</gi>または値がもうひとつ(または、要素
  <gi>fDecl</gi>にある属性orgの値に依存する数だけ)付与される。条件的な
  場合、要素であればひとつ以上が付与される。デフォルト値が指定されてい
  ない場合、または条件が成立しない場合は、値noneをとるする。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">déclare la valeur par défaut à fournir quand une
      structure de traits ne contient aucun cas de <gi>f</gi> pour ce nom ; si elle est inconditionnelle,
      on l'indique comme un élément <gi>fs</gi> (ou plusieurs, selon la valeur de l'attribut <att>org</att> du <gi>fDecl</gi>
      englobant) ; si elle est conditionnelle, on l'indique comme un ou plusieurs éléments <gi>if</gi> ; si
      aucune valeur par défaut n'est précisée ou si aucune condition ne correspond, la valeur nulle
      est retenue.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">declara el valor predeterminado que se aplica cuando una estructura de rasgo no contiene un valor de f para este nombre; si es incondicional, se especifica como uno (según el valor del atributo org de la fDecl) o más elementos fs o como valores primitivos; si es condicional, se especifica como uno o más elementos; si no hay un valor predeterminado, o no hay ninguna condición combinada, no se asume ningún valor.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">dichiara il valore predefinito da fornire quando una struttura di tratti non contiene una occorrenza di f per questo nome; se non condizionato, è specificato come uno o (a seconda del valore
      dell'attributo org del fDecl accluso) più elementi fs di valori primitivi; se condizionato, è specificato come uno o più elementi if; se non è specificto alcun valore predefinito, o nessuna condizione corrisponde, viene assunto il valore nessuno.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      
        <classRef key="model.featureVal" minOccurs="1" maxOccurs="unbounded"/>
      
      
        <elementRef key="if" minOccurs="1" maxOccurs="unbounded"/>
      
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vDefault-egXML-pz">
      <fDecl name="INV">
        <fDescr>inverted sentence</fDescr>
        <vRange>
          <vAlt>
            <binary value="true"/>
            <binary value="false"/>
          </vAlt>
        </vRange>
        <vDefault>
          <binary value="false"/>
        </vDefault>
      </fDecl>
    </egXML>
  </exemplum>
  <remarks ident="vDefault-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain a legal feature value, or a series of <gi>if</gi>
elements.</p>
  </remarks>
  <remarks ident="vDefault-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une valeur de trait admise ou une série d'éléments
                    <gi>if</gi>.</p>
  </remarks>
  <remarks ident="vDefault-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    正しい素性値、または一連の要素<gi>if</gi>をとる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">value default</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">기본 값</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">預設值</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">valeur par défaut</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">valor predeterminado</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">valore predefinito</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">declares the default value to be supplied when a feature structure
does not contain an instance of <gi>f</gi> for this name; if
unconditional, it is specified as one (or, depending on the value of
the <att>org</att> attribute of the enclosing <gi>fDecl</gi>) more
<gi>fs</gi> elements or primitive values;
if conditional, it is specified as
one or more <gi>if</gi> elements; if no default is specified, or no
condition matches, the value <val>none</val> is assumed.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질 구조가 이 이름에 대한 자질의 예를 포함하지 않는다면 제시된 기본값을 선언한다. 조건이 미명시되었을 때 하나 이상의 자질구조 요소 또는 원형 값(또는 fDecl의 org 속성 값의 의존하는 값)으로 명시된다; 만약 조건이 명시될 때, 하나 이상의 요소로 명시된다; 만약 기본 값이 명시되지 않는다면 또는 일치하는 조건이 없다면, none 값이 상정된다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在功能結構不包含元素<gi>f</gi>以提供名稱的情況下，宣告使用預設值；若無條件限制，預設值會被指明為一個 (或，取決於所包含的元素<gi>fDecl</gi>中屬性<att>org</att>的屬性值) 多個元素<gi>fs</gi>或原始值；若有條件限制，則被指明為一個或多個元素<gi> if</gi>；若無任何預設值、或無條件符合，則採用屬性值 <val>none</val>。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性構造が要素<gi>f</gi>を持たないときのデフォルト値を宣言する。条件
  的でない場合、要素<gi>fs</gi>または値がもうひとつ(または、要素
  <gi>fDecl</gi>にある属性orgの値に依存する数だけ)付与される。条件的な
  場合、要素であればひとつ以上が付与される。デフォルト値が指定されてい
  ない場合、または条件が成立しない場合は、値noneをとるする。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">déclare la valeur par défaut à fournir quand une
      structure de traits ne contient aucun cas de <gi>f</gi> pour ce nom ; si elle est inconditionnelle,
      on l'indique comme un élément <gi>fs</gi> (ou plusieurs, selon la valeur de l'attribut <att>org</att> du <gi>fDecl</gi>
      englobant) ; si elle est conditionnelle, on l'indique comme un ou plusieurs éléments <gi>if</gi> ; si
      aucune valeur par défaut n'est précisée ou si aucune condition ne correspond, la valeur nulle
      est retenue.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">declara el valor predeterminado que se aplica cuando una estructura de rasgo no contiene un valor de f para este nombre; si es incondicional, se especifica como uno (según el valor del atributo org de la fDecl) o más elementos fs o como valores primitivos; si es condicional, se especifica como uno o más elementos; si no hay un valor predeterminado, o no hay ninguna condición combinada, no se asume ningún valor.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">dichiara il valore predefinito da fornire quando una struttura di tratti non contiene una occorrenza di f per questo nome; se non condizionato, è specificato come uno o (a seconda del valore
      dell'attributo org del fDecl accluso) più elementi fs di valori primitivi; se condizionato, è specificato come uno o più elementi if; se non è specificto alcun valore predefinito, o nessuna condizione corrisponde, viene assunto il valore nessuno.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.featureVal" minOccurs="1" maxOccurs="unbounded"/>
      
      
        <elementRef key="if" minOccurs="1" maxOccurs="unbounded"/>
      
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vDefault-egXML-pz">
      <fDecl name="INV">
        <fDescr>inverted sentence</fDescr>
        <vRange>
          <vAlt>
            <binary value="true"/>
            <binary value="false"/>
          </vAlt>
        </vRange>
        <vDefault>
          <binary value="false"/>
        </vDefault>
      </fDecl>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="vDefault-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain a legal feature value, or a series of <gi>if</gi>
elements.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="vDefault-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une valeur de trait admise ou une série d'éléments
                    <gi>if</gi>.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="vDefault-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    正しい素性値、または一連の要素<gi>if</gi>をとる。
    </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b20

