---
type: representation
source-type: document
source: '[[00_sources/tei-p5-classes-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 classes
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/classes.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# classes

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6618. Git blob: `43b11e32620547e0a56872fcb4bd1f0c855058a1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" 
  schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-classes" ident="classes">
  <gloss versionDate="2007-06-12" xml:lang="en">classes</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">classes</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies all the classes of which the documented element or
class is a member or subclass.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">기록된 요소 또는 부류가 원소 또는 하위부류인 모든 부류를 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明所記錄的元素或元素集所屬或是附屬的所有元素集。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該文書化されている要素やクラスの構成要素や下位クラスを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">précise toutes les classes dont la classe ou
			l'élément documentés est un membre ou une sous-classe.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica todas las clases de las que el elemento o la clase indicados son un miembro o una subclase.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica tutte le classi delle quali l'elemento o la classe indicati sono un membro o una sottoclasse.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    
        <elementRef key="memberOf" minOccurs="0" maxOccurs="unbounded"/>
      
  </content>
  <attList>
    <attDef ident="mode" usage="opt">
      <desc versionDate="2006-03-12" xml:lang="en">specifies the effect of this declaration on its parent
    module.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">부모 모듈에 이 선언의 효과를 명시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">especifica el efecto de esta declaración en su módulo padre.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該宣言が親モジュールに与える影響を示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">indique l'effet de cette déclaration sur son
module parent.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'effetto della dichiarazione sul modulo da cui trae origine.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>replace</defaultVal>
      <valList type="closed">
        <valItem ident="change">
          <desc versionDate="2007-09-30" xml:lang="en">this declaration changes the declaration of the same
    name in the current definition</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 선언은 현 정의에서 동일 이름의 선언을 변경한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta declaración cambia la declaración del mismo nombre en la definición actual</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該宣言は、現行定義中にある同名宣言を修正する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette déclaration modifie la
déclaration de même nom dans la définition courante.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la dichiarazione modifica la dichiarazione con lo stesso nome nella definizione corrente.</desc>
        </valItem>
        <valItem ident="replace">
          <desc versionDate="2007-09-30" xml:lang="en">this declaration replaces the declaration of the same
    name in the current definition</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 선언은 현 정의에서 동일 이름의 선언을 대체한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta declaración substituye la declaración del mismo nombre en la definición actual</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該宣言は、現行定義中の同名宣言に置き換わる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette déclaration remplace la
déclaration de même nom dans la définition courante.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la dichiarazione sostituisce la dichiarazione con lo stesso nome nella definizione corrente.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classes-egXML-zm" source="#UND">
      <classes>
        <memberOf key="model.attributable"/>
        <memberOf key="att.declarable"/>
      </classes>
    </egXML>
    <p>This <gi>classes</gi> element indicates that the element documented
(which may be an element or a class) is a member of two distinct  classes: <ident type="class">model.attributable</ident> and
  <ident type="class">att.declarable</ident>. </p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classes-egXML-ea" source="#UND">
      <classes>
        <memberOf key="model.attributable"/>
        <memberOf key="att.declarable"/>
      </classes>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cet élément<gi>classes</gi>indique que l'élément documenté (qui peut être un élément ou une
        classe) est membre de deux classes distinctes : <ident type="class">model.attributable</ident> et
          <ident type="class">att.declarable</ident>. </p>
  </exemplum>
  <remarks ident="classes-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>An empty <gi>classes</gi> element indicates that the
  element documented is not a member of any class. This should not
  generally happen.</p>
  </remarks>
  <remarks ident="classes-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un élément <gi>classes</gi> vide indique que l'élément documenté n'appartient à
                aucune classe. Cela devrait être exceptionnel.</p>
  </remarks>
  <remarks ident="classes-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    空要素<gi>classes</gi>は、当該文書化されている要素は、どのクラスの
  構成要素でもないことを示す。一般には、このようなことは起こらない。
  </p>
  </remarks>
  <listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TDCLA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">classes</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">classes</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies all the classes of which the documented element or
class is a member or subclass.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기록된 요소 또는 부류가 원소 또는 하위부류인 모든 부류를 명시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明所記錄的元素或元素集所屬或是附屬的所有元素集。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該文書化されている要素やクラスの構成要素や下位クラスを示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise toutes les classes dont la classe ou
			l'élément documentés est un membre ou une sous-classe.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica todas las clases de las que el elemento o la clase indicados son un miembro o una subclase.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica tutte le classi delle quali l'elemento o la classe indicati sono un membro o una sottoclasse.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
        <elementRef key="memberOf" minOccurs="0" maxOccurs="unbounded"/>
      
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2006-03-12" xml:lang="en">specifies the effect of this declaration on its parent
    module.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">부모 모듈에 이 선언의 효과를 명시한다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">especifica el efecto de esta declaración en su módulo padre.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該宣言が親モジュールに与える影響を示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">indique l'effet de cette déclaration sur son
module parent.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'effetto della dichiarazione sul modulo da cui trae origine.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>replace</defaultVal>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="change">
          <desc versionDate="2007-09-30" xml:lang="en">this declaration changes the declaration of the same
    name in the current definition</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 선언은 현 정의에서 동일 이름의 선언을 변경한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta declaración cambia la declaración del mismo nombre en la definición actual</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該宣言は、現行定義中にある同名宣言を修正する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette déclaration modifie la
déclaration de même nom dans la définition courante.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la dichiarazione modifica la dichiarazione con lo stesso nome nella definizione corrente.</desc>
        </valItem>
        <valItem ident="replace">
          <desc versionDate="2007-09-30" xml:lang="en">this declaration replaces the declaration of the same
    name in the current definition</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 선언은 현 정의에서 동일 이름의 선언을 대체한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta declaración substituye la declaración del mismo nombre en la definición actual</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該宣言は、現行定義中の同名宣言に置き換わる。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette déclaration remplace la
déclaration de même nom dans la définition courante.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la dichiarazione sostituisce la dichiarazione con lo stesso nome nella definizione corrente.</desc>
        </valItem>
      </valList>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classes-egXML-zm" source="#UND">
      <classes>
        <memberOf key="model.attributable"/>
        <memberOf key="att.declarable"/>
      </classes>
    </egXML>
    <p>This <gi>classes</gi> element indicates that the element documented
(which may be an element or a class) is a member of two distinct  classes: <ident type="class">model.attributable</ident> and
  <ident type="class">att.declarable</ident>. </p>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classes-egXML-ea" source="#UND">
      <classes>
        <memberOf key="model.attributable"/>
        <memberOf key="att.declarable"/>
      </classes>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cet élément<gi>classes</gi>indique que l'élément documenté (qui peut être un élément ou une
        classe) est membre de deux classes distinctes : <ident type="class">model.attributable</ident> et
          <ident type="class">att.declarable</ident>. </p>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="classes-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>An empty <gi>classes</gi> element indicates that the
  element documented is not a member of any class. This should not
  generally happen.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="classes-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un élément <gi>classes</gi> vide indique que l'élément documenté n'appartient à
                aucune classe. Cela devrait être exceptionnel.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="classes-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    空要素<gi>classes</gi>は、当該文書化されている要素は、どのクラスの
  構成要素でもないことを示す。一般には、このようなことは起こらない。
  </p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TDCLA"/>
  </listRef>
```

^b26

