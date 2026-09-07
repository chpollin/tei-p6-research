---
type: representation
source-type: document
source: '[[00_sources/tei-p5-socecstatus-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 socecStatus
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/socecStatus.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# socecStatus

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7433. Git blob: `c63b4d116603b2e4831736588d1e8c12776a4371`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-socecStatus" ident="socecStatus">
  <gloss versionDate="2005-01-14" xml:lang="en">socio-economic status</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">statut socio-économique</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">사회-경제적 지위</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">社會經濟地位</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">estatus socio-económico</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">condizione socio-economica</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an informal description of a person's perceived social or economic status.</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient une description non formalisée du statut social ou économique d'une personne.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 사회 또는 경제적 지위에 대한 비공식적 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人的社會或經濟地位的非正式描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ある個人の、社会的・経済的状態を示す、形式的でない解説を示す。</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción informal sobre el estatus socio-económico de una persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione informale della condizione socio-economica percepita di una persona.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="scheme" usage="opt">
      <desc versionDate="2013-12-06" xml:lang="en">identifies the classification system or taxonomy in use, for example by pointing to a locally-defined <gi>taxonomy</gi> element or by supplying a URI for an externally-defined system.</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">identifie le système de classification ou la taxinomie utilisés.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사용 중인 분류 체계 또는 분류법을 식별한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出所使用的分類系統或分類法。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">使われた分類システムを示す。</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica el sistema de clasificación o de taxonomía empleado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica il sistema di classificazione o la tassonomia utilizzati.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="code" usage="opt">
      <desc versionDate="2012-09-19" xml:lang="en">identifies a status code defined within the classification system or taxonomy defined by the <att>scheme</att> attribute.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">contient un code de statut existant dans le système de classification ou dans la taxonomie
                déclarés au moyen de l'attribut <att>source</att>.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko"><att>source</att> 속성에 의해 정의된 분류 체계 또는 분류법 내에서 정의된 지위 부호를 식별한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">所標明的地位代號被定義在由屬性<att>source</att>所規定的分類系統或分類法當中。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">属性<att>source</att>で定義された分類システムにある、状態コード を特定する。</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica un código relativo a la condición socio-económica definido en el sistema de
                clasificación o taxonomía establecidos por el attributo <att>source</att>.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">corrisponde a un codice relativo alla condizione socio-economica definito nel sistema di
                classificazione o tassonomia stabiliti dall'attributo <att>source</att></desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="type" usage="opt" mode="change">
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
        <valItem ident="atBirth"/>
        <valItem ident="atDeath"/>
        <valItem ident="dependent"/>
        <valItem ident="inherited"/>
        <valItem ident="independent"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-ne" source="#UND">
      <socecStatus scheme="#rg" code="#ab1"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-jg" source="#UND">
      <socecStatus scheme="#fr_rg" code="#ab1"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-sn">
      <socecStatus>Code 17 dans la PCS ( Professions et catégories
        socioprofessionnelles)</socecStatus>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-qa">
      <socecStatus>印度教種姓制度下的賤民階級</socecStatus>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-th">
      <socecStatus>Status AB1 in the RG Classification scheme</socecStatus>
    </egXML>
  </exemplum>
  <remarks ident="socecStatus-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The content of this element may be used as an alternative to the more formal specification made possible by its attributes; it may also be
            used to supplement the formal specification with commentary or clarification.</p>
  </remarks>
  <remarks ident="socecStatus-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le contenu de cet élément peut être utilisé à la place d'une caractérisation plus formelle que ses attributs permettent ; il peut aussi
            être utilisé pour compléter cette caractérisation formelle par un commentaire ou une explication.</p>
  </remarks>
  <remarks ident="socecStatus-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素の内容は、より形式的な定義の代わりに使用されるかもしれない。 または、そのような定義を補うものとして使用されるかもしれない。 </p>
  </remarks>
  <listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">socio-economic status</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">statut socio-économique</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">사회-경제적 지위</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">社會經濟地位</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">estatus socio-económico</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">condizione socio-economica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an informal description of a person's perceived social or economic status.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient une description non formalisée du statut social ou économique d'une personne.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 사회 또는 경제적 지위에 대한 비공식적 기술을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人的社會或經濟地位的非正式描述。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ある個人の、社会的・経済的状態を示す、形式的でない解説を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción informal sobre el estatus socio-económico de una persona.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione informale della condizione socio-economica percepita di una persona.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-12-06" xml:lang="en">identifies the classification system or taxonomy in use, for example by pointing to a locally-defined <gi>taxonomy</gi> element or by supplying a URI for an externally-defined system.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">identifie le système de classification ou la taxinomie utilisés.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사용 중인 분류 체계 또는 분류법을 식별한다.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出所使用的分類系統或分類法。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">使われた分類システムを示す。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica el sistema de clasificación o de taxonomía empleado.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica il sistema di classificazione o la tassonomia utilizzati.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2012-09-19" xml:lang="en">identifies a status code defined within the classification system or taxonomy defined by the <att>scheme</att> attribute.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient un code de statut existant dans le système de classification ou dans la taxonomie
                déclarés au moyen de l'attribut <att>source</att>.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><att>source</att> 속성에 의해 정의된 분류 체계 또는 분류법 내에서 정의된 지위 부호를 식별한다.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">所標明的地位代號被定義在由屬性<att>source</att>所規定的分類系統或分類法當中。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性<att>source</att>で定義された分類システムにある、状態コード を特定する。</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica un código relativo a la condición socio-económica definido en el sistema de
                clasificación o taxonomía establecidos por el attributo <att>source</att>.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">corrisponde a un codice relativo alla condizione socio-economica definito nel sistema di
                classificazione o tassonomia stabiliti dall'attributo <att>source</att></desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="atBirth"/>
        <valItem ident="atDeath"/>
        <valItem ident="dependent"/>
        <valItem ident="inherited"/>
        <valItem ident="independent"/>
      </valList>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-ne" source="#UND">
      <socecStatus scheme="#rg" code="#ab1"/>
    </egXML>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-jg" source="#UND">
      <socecStatus scheme="#fr_rg" code="#ab1"/>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-sn">
      <socecStatus>Code 17 dans la PCS ( Professions et catégories
        socioprofessionnelles)</socecStatus>
    </egXML>
  </exemplum>
```

^b36

### Block 37

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-qa">
      <socecStatus>印度教種姓制度下的賤民階級</socecStatus>
    </egXML>
  </exemplum>
```

^b37

### Block 38

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-socecStatus-egXML-th">
      <socecStatus>Status AB1 in the RG Classification scheme</socecStatus>
    </egXML>
  </exemplum>
```

^b38

### Block 39

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="socecStatus-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The content of this element may be used as an alternative to the more formal specification made possible by its attributes; it may also be
            used to supplement the formal specification with commentary or clarification.</p>
  </remarks>
```

^b39

### Block 40

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="socecStatus-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le contenu de cet élément peut être utilisé à la place d'une caractérisation plus formelle que ses attributs permettent ; il peut aussi
            être utilisé pour compléter cette caractérisation formelle par un commentaire ou une explication.</p>
  </remarks>
```

^b40

### Block 41

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="socecStatus-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素の内容は、より形式的な定義の代わりに使用されるかもしれない。 または、そのような定義を補うものとして使用されるかもしれない。 </p>
  </remarks>
```

^b41

### Block 42

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b42

