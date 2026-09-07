---
type: representation
source-type: document
source: '[[00_sources/tei-p5-specgrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 specGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/specGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# specGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5714. Git blob: `e9109b29aae64e8381fbcbfa7eaac5ea942162de`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="SPECGRP" ident="specGrp">
  <gloss versionDate="2005-01-14" xml:lang="en">specification group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">명시 그룹</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">說明群組</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">groupe de spécifications</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de instrucciones</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gruppo di istruzioni</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains any convenient grouping of specifications for use within
  the current module.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">현 모듈 내에서 사용에 대한 명시를 다양한 방법의 그룹화를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含在現有模組中的細節使用說明群組。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該モジュール中にある規定をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient tout regroupement approprié de
			spécifications pour une utilisation dans le module en question.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier agrupación funcional de instrucciones para el uso al interno del módulo corriente</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi raggruppamento funzionale di istruzioni per l'uso all'interno del modulo corrente.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.oddDecl"/>
      <classRef key="model.oddRef"/>
      <classRef key="model.divPart"/>
      <elementRef key="listRef"/>
    </alternate>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRP-egXML-tm" source="#UND">
      <specGrp xml:id="xDAILC">
        <elementSpec ident="s">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="cl">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="w">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="m">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="c">
          <!-- ... -->
        </elementSpec>
      </specGrp>
    </egXML>
    <p>This specification group with identifier <ident>xDAILC</ident>
contains specifications for the elements
<gi>s</gi>,<gi>cl</gi>,<gi>w</gi>, etc.</p>
  </exemplum>
  <exemplum versionDate="2022-09-25" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRP-egXML-hk" source="#UND">
      <specGrp xml:id="fr_xDAILC">
        <elementSpec ident="s">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="cl">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="w">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="m">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="c">
          <!-- ... -->
        </elementSpec>
      </specGrp>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Le groupe de spécification avec l'identifiant <ident>xDAILC</ident> contient des
        spécifications pour les éléments <gi>s</gi>,<gi>cl</gi>,<gi>w</gi>, etc.</p>
  </exemplum>
  <remarks ident="specGrp-remarks" versionDate="2008-09-03" xml:lang="en">
    <p>A specification group is referenced by means of its
    <att>xml:id</att> attribute. The declarations it contains may be
    included in a <gi>schemaSpec</gi> or <gi>moduleSpec</gi> element
    only by reference (using a <gi>specGrpRef</gi> element): it may
    not be nested within a <gi>moduleSpec</gi> element. </p>
    <p>Different ODD processors may generate 
  representations of the specifications contained by a
  <gi>specGrp</gi> in different concrete syntaxes. </p>
  </remarks>
  <remarks ident="specGrp-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un groupe de spécifications est référencé au moyen de son attribut <att>xml:id</att>.
                Les déclarations qu'il contient ne peuvent être incluses dans un élément
                <gi>module</gi> que par référence (en utilisant un élément <gi>specGrpRef</gi>) : il
                ne peut être imbriqué dans un élément <gi>module</gi>.</p>
    <p>Différents processeurs ODD peuvent générer des représentations des spécifications
                contenues par un élément<gi>specGrp</gi> dans différentes syntaxes concrètes. </p>
  </remarks>
  <remarks ident="specGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    規定のグループは、属性<att>xml:id</att>で参照される。その宣言は、
    (要素<gi>specGrpRef</gi>による)参照にのみ示される要素
    <gi>module</gi>の中にある。
    </p>
    <p>
    ODDソフトが異なれば、要素<gi>specGrp</gi>中に、異なる文法による規
    定が生成される。TEI P5では、XMLとRELAX NGの両方によるモジュールを
    生成する。簡易RELAX NG文法は、表示にのみ使用する。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TDmodules"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">specification group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">명시 그룹</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">說明群組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">groupe de spécifications</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de instrucciones</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gruppo di istruzioni</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains any convenient grouping of specifications for use within
  the current module.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현 모듈 내에서 사용에 대한 명시를 다양한 방법의 그룹화를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含在現有模組中的細節使用說明群組。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該モジュール中にある規定をまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient tout regroupement approprié de
			spécifications pour une utilisation dans le module en question.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier agrupación funcional de instrucciones para el uso al interno del módulo corriente</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi raggruppamento funzionale di istruzioni per l'uso all'interno del modulo corrente.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.oddDecl"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.oddDecl"/>
      <classRef key="model.oddRef"/>
      <classRef key="model.divPart"/>
      <elementRef key="listRef"/>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRP-egXML-tm" source="#UND">
      <specGrp xml:id="xDAILC">
        <elementSpec ident="s">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="cl">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="w">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="m">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="c">
          <!-- ... -->
        </elementSpec>
      </specGrp>
    </egXML>
    <p>This specification group with identifier <ident>xDAILC</ident>
contains specifications for the elements
<gi>s</gi>,<gi>cl</gi>,<gi>w</gi>, etc.</p>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2022-09-25" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRP-egXML-hk" source="#UND">
      <specGrp xml:id="fr_xDAILC">
        <elementSpec ident="s">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="cl">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="w">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="m">
          <!-- ... -->
        </elementSpec>
        <elementSpec ident="c">
          <!-- ... -->
        </elementSpec>
      </specGrp>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Le groupe de spécification avec l'identifiant <ident>xDAILC</ident> contient des
        spécifications pour les éléments <gi>s</gi>,<gi>cl</gi>,<gi>w</gi>, etc.</p>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="specGrp-remarks" versionDate="2008-09-03" xml:lang="en">
    <p>A specification group is referenced by means of its
    <att>xml:id</att> attribute. The declarations it contains may be
    included in a <gi>schemaSpec</gi> or <gi>moduleSpec</gi> element
    only by reference (using a <gi>specGrpRef</gi> element): it may
    not be nested within a <gi>moduleSpec</gi> element. </p>
    <p>Different ODD processors may generate 
  representations of the specifications contained by a
  <gi>specGrp</gi> in different concrete syntaxes. </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="specGrp-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un groupe de spécifications est référencé au moyen de son attribut <att>xml:id</att>.
                Les déclarations qu'il contient ne peuvent être incluses dans un élément
                <gi>module</gi> que par référence (en utilisant un élément <gi>specGrpRef</gi>) : il
                ne peut être imbriqué dans un élément <gi>module</gi>.</p>
    <p>Différents processeurs ODD peuvent générer des représentations des spécifications
                contenues par un élément<gi>specGrp</gi> dans différentes syntaxes concrètes. </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="specGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    規定のグループは、属性<att>xml:id</att>で参照される。その宣言は、
    (要素<gi>specGrpRef</gi>による)参照にのみ示される要素
    <gi>module</gi>の中にある。
    </p>
    <p>
    ODDソフトが異なれば、要素<gi>specGrp</gi>中に、異なる文法による規
    定が生成される。TEI P5では、XMLとRELAX NGの両方によるモジュールを
    生成する。簡易RELAX NG文法は、表示にのみ使用する。
    </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDmodules"/>
  </listRef>
```

^b21

