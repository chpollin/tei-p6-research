---
type: representation
source-type: document
source: '[[00_sources/tei-p5-specgrpref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 specGrpRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/specGrpRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# specGrpRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7338. Git blob: `ef9b7c972ec32df2d9dbbeb68c61f95a76f81590`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="SPECGRPREF" ident="specGrpRef">
  <gloss versionDate="2005-01-14" xml:lang="en">reference to a specification group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">명시 그룹에 대한 참조</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">參照到一個說明群組</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">référence à un groupe de spécifications</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">referencia a un grupo de instrucciones</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">riferimento a gruppo di istruzioni</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates that the declarations contained by the <gi>specGrp</gi> referenced should be
    inserted at this point.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">참조된 <gi>specGrp</gi>에 의해 포함된 선언은 이 지점에서 삽입되어야함을 나타낸다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出被參照的元素<gi>specGrp</gi>中的宣告應在此插入。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素<gi>specGrp</gi>により含まれる宣言が、この場所に挿入されるべきこ とを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indique que les déclarations contenues dans l'élément
      <gi>specGrp</gi>référencé doivent être insérées à cet endroit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el punto en el que deben inserirse las
    declaraciones contenidas en el <gi>specGrp</gi> indicado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica il punto in cui devono essere inserite le
    dichiarazioni contenute nello <gi>specGrp</gi> indicato</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content><empty/></content>
  <attList>
    <attDef ident="target" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">points at the specification group which logically belongs here.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">여기에 국부적으로 소속된 명시 그룹을 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指向照理屬於此位置的說明群組。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">論理的にはこの場素にある規定グループを参照する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">pointe vers l'élément <gi>specGrp</gi> qui doit
        logiquement être référencé à cet endroit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el grupo de instrucciones que por lógica
        corresponde a ese punto en cuestión.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il gruppo di istruzioni che per logica
        corrisponde al punto in questione</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRPREF-egXML-pf">
      <p>This part of the module contains declarations for names of persons, places, and
        organisations: <specGrpRef target="#names.pers"/>
            <specGrpRef target="#names.place"/>
            <specGrpRef target="#names.org"/>
         </p>
      <!-- elsewhere -->
      <specGrp xml:id="names.pers">
        <!--... -->
      </specGrp>
      <!-- elsewhere -->
      <specGrp xml:id="names.place">
        <!--... -->
      </specGrp>
      <!-- elsewhere -->
      <specGrp xml:id="names.org">
        <!--... -->
      </specGrp>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRPREF-egXML-cu">
      <p>Cette partie du module contient les déclarations pour les noms de personnes, de lieux,
          des organismes : <specGrpRef target="#fr_names.pers"/>
            <specGrpRef target="#fr_names.place"/>
            <specGrpRef target="#fr_names.org"/>
        </p>
      <specGrp xml:id="fr_names.pers"> 
        <!--... -->
      </specGrp>
      <specGrp xml:id="fr_names.place">
        <!--... -->
      </specGrp>
      <specGrp xml:id="fr_names.org">
        <!--... -->
      </specGrp>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRPREF-egXML-ux">
      <p>這部份的模組包含人名、地名以及組織名稱的宣告：<specGrpRef target="#zh-tw_names.pers"/>
            <specGrpRef target="#zh-tw_names.place"/>
            <specGrpRef target="#zh-tw_names.org"/>
         </p>
      <!-- 某處 -->
      <specGrp xml:id="zh-tw_names.pers">
        <!--... -->
      </specGrp>
      <!-- 某處 -->
      <specGrp xml:id="zh-tw_names.place">
        <!--... -->
      </specGrp>
      <!-- 某處 -->
      <specGrp xml:id="zh-tw_names.org">
        <!--... -->
      </specGrp>
    </egXML>
  </exemplum>
  <remarks ident="specGrpRef-remarks" versionDate="2005-05-22" xml:lang="en">
    <p>In ODD documentation processing, a <gi>specGrpRef</gi> usually produces a comment indicating
      that a set of declarations printed in another section will be inserted at this point in the
        <gi>specGrp</gi> being discussed. In schema processing, the contents of the specified
        <gi>specGrp</gi> are made available for inclusion in the generated schema. </p>
    <p>The specification group identified by the <att>target</att> attribute will normally be part
      of the current ODD document.</p>
  </remarks>
  <remarks ident="specGrpRef-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans le traitement de la documentation ODD, un élément <gi>specGrpRef</gi> produit
      habituellement un commentaire indiquant qu'un ensemble de déclarations imprimé dans une autre
      section sera inséré à cet endroit dans le <gi>specGrp</gi> que l'on traite. Dans un traitement
      de schéma, les contenus du <gi>specGrp</gi> spécifié sont rendus disponibles pour être inclus
      dans le schéma généré.</p>
    <p>Le groupe de spécifications identifié par l'attribut <att>target</att> fera normalement
      partie du document ODD en cours.</p>
  </remarks>
  <remarks ident="specGrpRef-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> ODD文書を処理する際、要素<gi>specGrpRef</gi>は、一般に、他の章にあ る宣言の集合が、要素<gi>specGrp</gi>が示すこの場所に挿入されること
      を示すコメントを作り出す。スキーマを処理する際、要素 <gi>specGrp</gi>の内容は、生成されたスキーマ中で使用可能になる。 </p>
    <p> 属性<att>target</att>で特定されている規定グループは、一般には、当 該ODD文書の一部となる。 </p>
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
<gloss versionDate="2005-01-14" xml:lang="en">reference to a specification group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">명시 그룹에 대한 참조</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">參照到一個說明群組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">référence à un groupe de spécifications</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">referencia a un grupo de instrucciones</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">riferimento a gruppo di istruzioni</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates that the declarations contained by the <gi>specGrp</gi> referenced should be
    inserted at this point.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참조된 <gi>specGrp</gi>에 의해 포함된 선언은 이 지점에서 삽입되어야함을 나타낸다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出被參照的元素<gi>specGrp</gi>中的宣告應在此插入。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素<gi>specGrp</gi>により含まれる宣言が、この場所に挿入されるべきこ とを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique que les déclarations contenues dans l'élément
      <gi>specGrp</gi>référencé doivent être insérées à cet endroit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el punto en el que deben inserirse las
    declaraciones contenidas en el <gi>specGrp</gi> indicado.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il punto in cui devono essere inserite le
    dichiarazioni contenute nello <gi>specGrp</gi> indicato</desc>
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
<content><empty/></content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">points at the specification group which logically belongs here.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">여기에 국부적으로 소속된 명시 그룹을 가리킨다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指向照理屬於此位置的說明群組。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">論理的にはこの場素にある規定グループを参照する。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">pointe vers l'élément <gi>specGrp</gi> qui doit
        logiquement être référencé à cet endroit.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el grupo de instrucciones que por lógica
        corresponde a ese punto en cuestión.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il gruppo di istruzioni che per logica
        corrisponde al punto in questione</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRPREF-egXML-pf">
      <p>This part of the module contains declarations for names of persons, places, and
        organisations: <specGrpRef target="#names.pers"/>
            <specGrpRef target="#names.place"/>
            <specGrpRef target="#names.org"/>
         </p>
      <!-- elsewhere -->
      <specGrp xml:id="names.pers">
        <!--... -->
      </specGrp>
      <!-- elsewhere -->
      <specGrp xml:id="names.place">
        <!--... -->
      </specGrp>
      <!-- elsewhere -->
      <specGrp xml:id="names.org">
        <!--... -->
      </specGrp>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRPREF-egXML-cu">
      <p>Cette partie du module contient les déclarations pour les noms de personnes, de lieux,
          des organismes : <specGrpRef target="#fr_names.pers"/>
            <specGrpRef target="#fr_names.place"/>
            <specGrpRef target="#fr_names.org"/>
        </p>
      <specGrp xml:id="fr_names.pers"> 
        <!--... -->
      </specGrp>
      <specGrp xml:id="fr_names.place">
        <!--... -->
      </specGrp>
      <specGrp xml:id="fr_names.org">
        <!--... -->
      </specGrp>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SPECGRPREF-egXML-ux">
      <p>這部份的模組包含人名、地名以及組織名稱的宣告：<specGrpRef target="#zh-tw_names.pers"/>
            <specGrpRef target="#zh-tw_names.place"/>
            <specGrpRef target="#zh-tw_names.org"/>
         </p>
      <!-- 某處 -->
      <specGrp xml:id="zh-tw_names.pers">
        <!--... -->
      </specGrp>
      <!-- 某處 -->
      <specGrp xml:id="zh-tw_names.place">
        <!--... -->
      </specGrp>
      <!-- 某處 -->
      <specGrp xml:id="zh-tw_names.org">
        <!--... -->
      </specGrp>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="specGrpRef-remarks" versionDate="2005-05-22" xml:lang="en">
    <p>In ODD documentation processing, a <gi>specGrpRef</gi> usually produces a comment indicating
      that a set of declarations printed in another section will be inserted at this point in the
        <gi>specGrp</gi> being discussed. In schema processing, the contents of the specified
        <gi>specGrp</gi> are made available for inclusion in the generated schema. </p>
    <p>The specification group identified by the <att>target</att> attribute will normally be part
      of the current ODD document.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="specGrpRef-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans le traitement de la documentation ODD, un élément <gi>specGrpRef</gi> produit
      habituellement un commentaire indiquant qu'un ensemble de déclarations imprimé dans une autre
      section sera inséré à cet endroit dans le <gi>specGrp</gi> que l'on traite. Dans un traitement
      de schéma, les contenus du <gi>specGrp</gi> spécifié sont rendus disponibles pour être inclus
      dans le schéma généré.</p>
    <p>Le groupe de spécifications identifié par l'attribut <att>target</att> fera normalement
      partie du document ODD en cours.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="specGrpRef-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> ODD文書を処理する際、要素<gi>specGrpRef</gi>は、一般に、他の章にあ る宣言の集合が、要素<gi>specGrp</gi>が示すこの場所に挿入されること
      を示すコメントを作り出す。スキーマを処理する際、要素 <gi>specGrp</gi>の内容は、生成されたスキーマ中で使用可能になる。 </p>
    <p> 属性<att>target</att>で特定されている規定グループは、一般には、当 該ODD文書の一部となる。 </p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDmodules"/>
  </listRef>
```

^b30

