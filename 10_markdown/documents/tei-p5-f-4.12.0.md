---
type: representation
source-type: document
source: '[[00_sources/tei-p5-f-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 f
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/f.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# f

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6902. Git blob: `fea49f1e07c4d49eee933f62a402e3179bacafa6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="iso-fs" xml:id="gi-f" ident="f">
  <gloss versionDate="2007-07-05" xml:lang="en">feature</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">trait</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">Rasgo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">un tratto</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents a <term>feature value specification</term>, that
  is, the association of a name with a value of any of several different types.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><term>feature value specification</term>, 즉, 이름과 몇 가지 다른 유형의 값을 연결시킨다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個<term>功能值細節</term>，即一項名稱與任一種不同類型值之間的關連。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">素性値定義を示す。すなわち、素性名とその様々な値を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente une <term>spécification
      trait-valeur</term>, c'est-à-dire l'association d'un nom avec une valeur d’un type quelconque
      parmi plusieurs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa una <term>feature value specification (especificación de valor de rasgo)</term>, es decir, la asociación de un nombre con un valor de cualquier de los diferentes tipos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta una <term>feature value specification</term>, cioè l'associazione di un nome con il valore di uno qualsiasi di diversi tratti.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="1">
      <textNode/>
      <classRef key="model.featureVal"/>
    </alternate>    
  </content>
  <attList>
    <attDef ident="name" usage="req">
      <desc versionDate="2012-10-10" xml:lang="en">a single word which follows the rules defining a
        legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>), providing a name for the feature.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">자질에 대한 이름을 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">功能名稱</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該素性の名前を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">donne un nom pour le trait.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un nombre para un rasgo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome del tratto.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attDef ident="fVal" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">feature value</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">자질 값</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">valor del rasgo</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">valeur de traits</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">valore del tratto</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">references any element which can be used to represent the
  value of a feature.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">자질의 값을 표시할 수 있는 요소를 참조한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">參照任何可用來代表功能值的元素。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">素性値を表す要素を参照する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">référence n'importe quel élément pouvant être
          utilisé pour représenter la valeur d'un trait.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica cualquier elemento que puede ser usado para representar el valor de un rasgo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica un qualsiasi elemento che può essere usato come valore di un tratto.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="f-attr.fVal-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If this attribute is supplied as well as content, the value referenced is to be unified with  that contained.</p>
      </remarks>
      <remarks ident="f-attr.fVal-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si cet attribut est fourni en plus d'un contenu, la valeur référencée doit
                        être unifiée avec ce contenu.</p>
      </remarks>
      <remarks ident="f-attr.fVal-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	当該属性の値は、参照された要素内容とされる。
	</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-f-egXML-ct" source="#UND">
      <f name="gender">
        <symbol value="feminine"/>
      </f>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-f-egXML-vc" source="#UND">
      <f name="gender">
        <symbol value="feminine"/>
      </f>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-f-egXML-sp">
      <fs>
        <f name="voice">active</f>
        <f name="tense">SimPre</f>
      </fs>
    </egXML>
  </exemplum>
  <remarks ident="f-remarks" versionDate="2012-04-20" xml:lang="en">
    <p>The content of <gi>f</gi> may be textual, with the assumption
    that the data type of the feature value is determined by the
    schema—this is the approach used in many
    language-technology-oriented projects and recommendations.</p>
  </remarks>
  <remarks ident="f-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Si l'élément est vide, une valeur doit être fournie pour l'attribut
            <att>fVal</att>.</p>
  </remarks>
  <remarks ident="f-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    参照先の要素が空要素の場合、属性<att>fVal</att>が示す対象となる値
    が用意されていなければならない。
    </p>
  </remarks>
  <listRef>
    <ptr target="#FSBI" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-05" xml:lang="en">feature</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">trait</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">Rasgo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">un tratto</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents a <term>feature value specification</term>, that
  is, the association of a name with a value of any of several different types.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><term>feature value specification</term>, 즉, 이름과 몇 가지 다른 유형의 값을 연결시킨다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個<term>功能值細節</term>，即一項名稱與任一種不同類型值之間的關連。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性値定義を示す。すなわち、素性名とその様々な値を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente une <term>spécification
      trait-valeur</term>, c'est-à-dire l'association d'un nom avec une valeur d’un type quelconque
      parmi plusieurs.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa una <term>feature value specification (especificación de valor de rasgo)</term>, es decir, la asociación de un nombre con un valor de cualquier de los diferentes tipos.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta una <term>feature value specification</term>, cioè l'associazione di un nome con il valore di uno qualsiasi di diversi tratti.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="1">
      <textNode/>
      <classRef key="model.featureVal"/>
    </alternate>    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-10-10" xml:lang="en">a single word which follows the rules defining a
        legal XML name (see <ptr target="https://www.w3.org/TR/REC-xml/#dt-name"/>), providing a name for the feature.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질에 대한 이름을 제공한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">功能名稱</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該素性の名前を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne un nom pour le trait.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un nombre para un rasgo.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome del tratto.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">feature value</gloss>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질 값</gloss>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">valor del rasgo</gloss>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">valeur de traits</gloss>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">valore del tratto</gloss>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">references any element which can be used to represent the
  value of a feature.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질의 값을 표시할 수 있는 요소를 참조한다.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">參照任何可用來代表功能值的元素。</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">素性値を表す要素を参照する。</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">référence n'importe quel élément pouvant être
          utilisé pour représenter la valeur d'un trait.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica cualquier elemento que puede ser usado para representar el valor de un rasgo.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica un qualsiasi elemento che può essere usato come valore di un tratto.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="f-attr.fVal-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If this attribute is supplied as well as content, the value referenced is to be unified with  that contained.</p>
      </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="f-attr.fVal-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Si cet attribut est fourni en plus d'un contenu, la valeur référencée doit
                        être unifiée avec ce contenu.</p>
      </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="f-attr.fVal-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	当該属性の値は、参照された要素内容とされる。
	</p>
      </remarks>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-f-egXML-ct" source="#UND">
      <f name="gender">
        <symbol value="feminine"/>
      </f>
    </egXML>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-f-egXML-vc" source="#UND">
      <f name="gender">
        <symbol value="feminine"/>
      </f>
    </egXML>
  </exemplum>
```

^b41

### Block 42

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-f-egXML-sp">
      <fs>
        <f name="voice">active</f>
        <f name="tense">SimPre</f>
      </fs>
    </egXML>
  </exemplum>
```

^b42

### Block 43

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="f-remarks" versionDate="2012-04-20" xml:lang="en">
    <p>The content of <gi>f</gi> may be textual, with the assumption
    that the data type of the feature value is determined by the
    schema—this is the approach used in many
    language-technology-oriented projects and recommendations.</p>
  </remarks>
```

^b43

### Block 44

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="f-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Si l'élément est vide, une valeur doit être fournie pour l'attribut
            <att>fVal</att>.</p>
  </remarks>
```

^b44

### Block 45

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="f-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    参照先の要素が空要素の場合、属性<att>fVal</att>が示す対象となる値
    が用意されていなければならない。
    </p>
  </remarks>
```

^b45

### Block 46

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSBI" type="div3"/>
  </listRef>
```

^b46

