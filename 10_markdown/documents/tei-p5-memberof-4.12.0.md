---
type: representation
source-type: document
source: '[[00_sources/tei-p5-memberof-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 memberOf
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/memberOf.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# memberOf

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9114. Git blob: `210866c27766ef8652d17be144345d94ec56a65a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="MEMBEROF" ident="memberOf">
  <desc versionDate="2012-04-22" xml:lang="en">specifies class membership of the documented element or class.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">부모 요소 또는 부류의 부류 원소 자격을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明父元素或元素集所屬的元素集。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">親要素や親クラスを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">précise à quelle classe appartiennent la classe ou
    l'élément parent.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica la pertenencia a una clase del elemento o
    clase padre.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica l'appartenenza a una classe dell'elemento o
    classe genitori</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.xtext"/>
  </content>
  <attList>
    <attDef ident="key">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the identifier for a class of which the documented element or class is a
        member or subclass.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">기록된 요소 또는 부류가 원소 또는 하위부류인 부류의 확인소를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明一元素集的識別名稱，該元素集為所紀錄元素或元素集之所屬或附屬元素集</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素またはクラスが下位要素・下位クラスとなっているクラスの識 別子を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise l’identifiant pour une classe pour laquelle
        l'élément documenté ou classe est un membre ou sous-classe.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el identificador de una clase de la cual
        el elemento o clase indicados son un miembro o una subclase.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'identificatore di una classe di cui
        l'elemento o classe indicati sono un membro o una sottoclasse</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attDef ident="mode" usage="opt">
      <desc versionDate="2007-09-15" xml:lang="en">specifies the effect of this declaration on its parent module.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">부모 모듈에 이 선언의 효과를 명시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">especifica el efecto de esta declaración en su módulo
        padre.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該宣言が親モジュールに与える影響を示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">indique l'effet de cette déclaration sur son module
        parent.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">specifica l'effetto della dichiarazione sul modulo
        genitore</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>add</defaultVal>
      <valList type="closed">
        <valItem ident="add">
          <desc versionDate="2007-09-15" xml:lang="en">this declaration is added to the current definitions</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 선언은 현 정의에 추가된다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta declaración se agrega a las definiciones
            actuales</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該宣言は、現行定義に追加される。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette déclaration s'ajoute aux définitions
            courantes.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione è aggiunta alle definizioni
            correnti</desc>
        </valItem>
        <valItem ident="delete">
          <desc versionDate="2007-09-15" xml:lang="en">this declaration and all of its children are removed from the current setup</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 선언과 이 선언의 모든 자식은 현 구성에서 제거된다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta declaración y todos sus hijos se suprimen de
            la disposición actual</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該宣言と全子要素は、現行定義から外される。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette déclaration et tous ses enfants sont
            retirés du système courant.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione e i suoi discendenti sono
            esclusi dall'impostazione corrente</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="max">
      <desc versionDate="2011-12-01" xml:lang="en">supplies the maximum number of times the element can occur in elements which use this model class in their content model</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
    <attDef ident="min">
      <desc versionDate="2011-12-01" xml:lang="en">supplies the minumum number of times the element must occur in elements which use this model class in their content model</desc>
      <datatype><dataRef key="teidata.numeric"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MEMBEROF-egXML-yh" source="#UND">
      <memberOf key="model.divLike"/>
      <memberOf key="att.identified"/>
    </egXML>
    <p>This element will appear in any content model which references <ident type="class">model.divLike</ident>,
      and will have attributes defined in <ident type="class">att.identified</ident> (in addition to any defined
      explicitly for this element).</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MEMBEROF-egXML-cz" source="#UND">
      <memberOf key="model.divLike"/>
      <memberOf key="att.identified"/>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cet élément apparaîtra dans n'importe quel modèle de contenu faisant référence à
          <ident type="class">model.divLike</ident>, et aura des attributs définis
        dans<ident type="class">att.identified</ident> (en plus de n'importe quel autre attribut défini
        explicitement pour cet élément).</p>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MEMBEROF-egXML-wi" source="#UND">
      <memberOf key="model.divLike"/>
      <memberOf key="att.identified"/>
    </egXML>
  </exemplum>
  <remarks ident="memberOf-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Elements or classes which are members of multiple (unrelated) classes will have more than one
        <gi>memberOf</gi> element, grouped by a <gi>classes</gi> element. If an element is a member
      of a class C1, which is itself a subclass of a class C2, there is no need to state this, other
      than in the documentation for class C1. </p>
    <p>Any additional comment or explanation of the class membership may be provided as content for
      this element.</p>
  </remarks>
  <remarks ident="memberOf-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les éléments ou des classes qui appartiennent à des classes multiples (sans rapport entre
      elles) auront plusieurs éléments <gi>memberOf</gi>, regroupés par un élément <gi>classes</gi>.
      Si un élément appartient à une classe C1 qui est elle-même une sous-classe d'une classe C2, il
      n'est pas nécessaire d'établir ce fait autrement que dans la documentation de la classe C1. </p>
    <p>Tout commentaire ou explication additionnels de l'appartenance à une classe peut être fourni
      comme contenu de cet élément.</p>
  </remarks>
  <remarks ident="memberOf-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 複数のクラスに所属する要素またはクラスは、要素<gi>classes</gi>でま とめられた複数の要素<gi>memberOf</gi> elementをとる。ある要素がク
      ラスC1に属し、クラスC1はクラスC2に属する場合、クラスC1につい て記録するだけで、クラスC2を宣言する必要はない。 </p>
    <p> 当該要素の内容として、クラスの所属関係に関する追加の注釈や解説が含 まれることもある。 </p>
  </remarks>
  <listRef>
    <ptr target="#TDcrystalsCEcl"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-04-22" xml:lang="en">specifies class membership of the documented element or class.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">부모 요소 또는 부류의 부류 원소 자격을 명시한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明父元素或元素集所屬的元素集。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">親要素や親クラスを示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise à quelle classe appartiennent la classe ou
    l'élément parent.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la pertenencia a una clase del elemento o
    clase padre.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica l'appartenenza a una classe dell'elemento o
    classe genitori</desc>
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
    <macroRef key="macro.xtext"/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the identifier for a class of which the documented element or class is a
        member or subclass.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기록된 요소 또는 부류가 원소 또는 하위부류인 부류의 확인소를 명시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明一元素集的識別名稱，該元素集為所紀錄元素或元素集之所屬或附屬元素集</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素またはクラスが下位要素・下位クラスとなっているクラスの識 別子を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise l’identifiant pour une classe pour laquelle
        l'élément documenté ou classe est un membre ou sous-classe.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el identificador de una clase de la cual
        el elemento o clase indicados son un miembro o una subclase.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'identificatore di una classe di cui
        l'elemento o classe indicati sono un membro o una sottoclasse</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-09-15" xml:lang="en">specifies the effect of this declaration on its parent module.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">부모 모듈에 이 선언의 효과를 명시한다.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">especifica el efecto de esta declaración en su módulo
        padre.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該宣言が親モジュールに与える影響を示す。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">indique l'effet de cette déclaration sur son module
        parent.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">specifica l'effetto della dichiarazione sul modulo
        genitore</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>add</defaultVal>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="add">
          <desc versionDate="2007-09-15" xml:lang="en">this declaration is added to the current definitions</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 선언은 현 정의에 추가된다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta declaración se agrega a las definiciones
            actuales</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該宣言は、現行定義に追加される。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette déclaration s'ajoute aux définitions
            courantes.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione è aggiunta alle definizioni
            correnti</desc>
        </valItem>
        <valItem ident="delete">
          <desc versionDate="2007-09-15" xml:lang="en">this declaration and all of its children are removed from the current setup</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 선언과 이 선언의 모든 자식은 현 구성에서 제거된다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta declaración y todos sus hijos se suprimen de
            la disposición actual</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該宣言と全子要素は、現行定義から外される。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette déclaration et tous ses enfants sont
            retirés du système courant.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione e i suoi discendenti sono
            esclusi dall'impostazione corrente</desc>
        </valItem>
      </valList>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2011-12-01" xml:lang="en">supplies the maximum number of times the element can occur in elements which use this model class in their content model</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2011-12-01" xml:lang="en">supplies the minumum number of times the element must occur in elements which use this model class in their content model</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.numeric"/></datatype>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MEMBEROF-egXML-yh" source="#UND">
      <memberOf key="model.divLike"/>
      <memberOf key="att.identified"/>
    </egXML>
    <p>This element will appear in any content model which references <ident type="class">model.divLike</ident>,
      and will have attributes defined in <ident type="class">att.identified</ident> (in addition to any defined
      explicitly for this element).</p>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MEMBEROF-egXML-cz" source="#UND">
      <memberOf key="model.divLike"/>
      <memberOf key="att.identified"/>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cet élément apparaîtra dans n'importe quel modèle de contenu faisant référence à
          <ident type="class">model.divLike</ident>, et aura des attributs définis
        dans<ident type="class">att.identified</ident> (en plus de n'importe quel autre attribut défini
        explicitement pour cet élément).</p>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MEMBEROF-egXML-wi" source="#UND">
      <memberOf key="model.divLike"/>
      <memberOf key="att.identified"/>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="memberOf-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Elements or classes which are members of multiple (unrelated) classes will have more than one
        <gi>memberOf</gi> element, grouped by a <gi>classes</gi> element. If an element is a member
      of a class C1, which is itself a subclass of a class C2, there is no need to state this, other
      than in the documentation for class C1. </p>
    <p>Any additional comment or explanation of the class membership may be provided as content for
      this element.</p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="memberOf-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les éléments ou des classes qui appartiennent à des classes multiples (sans rapport entre
      elles) auront plusieurs éléments <gi>memberOf</gi>, regroupés par un élément <gi>classes</gi>.
      Si un élément appartient à une classe C1 qui est elle-même une sous-classe d'une classe C2, il
      n'est pas nécessaire d'établir ce fait autrement que dans la documentation de la classe C1. </p>
    <p>Tout commentaire ou explication additionnels de l'appartenance à une classe peut être fourni
      comme contenu de cet élément.</p>
  </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="memberOf-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 複数のクラスに所属する要素またはクラスは、要素<gi>classes</gi>でま とめられた複数の要素<gi>memberOf</gi> elementをとる。ある要素がク
      ラスC1に属し、クラスC1はクラスC2に属する場合、クラスC1につい て記録するだけで、クラスC2を宣言する必要はない。 </p>
    <p> 当該要素の内容として、クラスの所属関係に関する追加の注釈や解説が含 まれることもある。 </p>
  </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDcrystalsCEcl"/>
  </listRef>
```

^b37

