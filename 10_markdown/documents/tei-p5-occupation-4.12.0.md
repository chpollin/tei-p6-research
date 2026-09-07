---
type: representation
source-type: document
source: '[[00_sources/tei-p5-occupation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 occupation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/occupation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# occupation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7957. Git blob: `30c91fc4d45614b95eb4046dcee34038bd1558a6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-occupation" ident="occupation">
  <gloss versionDate="2008-12-09" xml:lang="en">occupation</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">activité</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an informal description of a person's trade, profession or occupation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인의 직업에 대한 비공식적 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含非正式的敘述，表示個人所從事的行業或所屬的專業。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物の仕事や職業の、形式的でない説明を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient une description non formalisée de l'activité, de la profession ou de l'occupation d'une personne.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción informal de las actividades, la profesión o la ocupación de una persona.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione informale dell'attività, professione o occupazione di una persona.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
        <valItem ident="primary"/>
        <valItem ident="other"/>
        <valItem ident="paid"/>
        <valItem ident="unpaid"/>
      </valList>
    </attDef>
    <attDef ident="scheme" usage="opt">
      <desc versionDate="2013-12-21" xml:lang="en">indicates the
      classification system or taxonomy in use, for example by
      supplying the identifier of a <gi>taxonomy</gi> element, or
      pointing to some other resource.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">헤더에 <gi>taxonomy</gi> 요소의 확인소를 제공하여 분류 체계 또는 분류법을 식별한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供標頭中元素<gi>taxonomy</gi>的識別符號，來標明所使用的分類系統或分類法。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">ヘダー内にある要素<gi>taxonomy</gi>の識別子により、使われている 分類システムを示す。</desc>
      <desc versionDate="2008-12-09" xml:lang="fr">identifie le système de classification ou la taxinomie utilisés, en fournissant l'identifiant
                d'un élément <gi>taxonomy</gi> déclaré ailleurs dans l'en-tête.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica el sistema de clasificación o la taxonomía utilizada para la identificación de un
                elemento <gi>taxonomy</gi> colocado en el encabezado.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica il sistema di classificazione o la tassonomia utilizzate tramite l'identificatore di
                un elemento <gi>taxonomy</gi> collocato nell'intestazione</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
    <attDef ident="code" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">identifies an occupation code defined within the classification system or taxonomy defined by the <att>scheme</att>
                attribute.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko"><att>scheme</att> 속성에 의해 정의된 분류 체계 또는 분류법 내에서 정의된 직업 부호를 식별한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明分類系統或分類法中所定義的職業代碼，該分類系統或分類法由屬性<att>scheme</att>所定義。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">属性<att>scheme</att>で定義されている分類システムの中で定義され る仕事コードを示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">contient un code d'activité défini dans le système de classification ou dans la taxonomie déclaré
                dans l'attribut <att>scheme</att>.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifica un código relativo a la ocupación definido en el sistema de clasificación o taxonomía
                establecido por el atributo <att>scheme</att>.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">corrisponde a un codice relativo all'occupazione definito nel sistema di classificazione o
                tassonomia stabiliti dall'attributo <att>scheme</att></desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-tv">
      <occupation>accountant</occupation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-ly">
      <occupation>Comptable</occupation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-ll">
      <occupation scheme="#fr_rg" code="#acc">Comptable</occupation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-ba">
      <occupation scheme="#fr_rg" code="#acc">Comptable spécialisé dans l'industrie
        pétrolière</occupation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-we">
      <occupation>會計師</occupation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-ts">
      <occupation scheme="#zh-tw_rg" code="#acc">擅長油業的會計師</occupation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-cz">
      <occupation scheme="#occupationtaxonomy" code="#acc">accountant</occupation>
    </egXML>
  </exemplum>
  <remarks ident="occupation-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The content of this element may be used as an alternative to the more formal specification made possible by its attributes; it may also be
            used to supplement the formal specification with commentary or clarification.</p>
  </remarks>
  <remarks ident="occupation-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p>Le contenu de cet élément peut être utilisé à la place d'une caractérisation plus formelle que ses attributs permettent ; il peut aussi
            être utilisé pour compléter cette caractérisation formelle par un commentaire ou une explication.</p>
  </remarks>
  <remarks ident="occupation-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素の内容は、より形式的な定義の代替として使用されるかもしれな い。また、解説または分類を伴う形式的定義を補うために使用されるかも しれない。 </p>
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
<gloss versionDate="2008-12-09" xml:lang="en">occupation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">activité</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an informal description of a person's trade, profession or occupation.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인의 직업에 대한 비공식적 기술을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含非正式的敘述，表示個人所從事的行業或所屬的專業。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物の仕事や職業の、形式的でない説明を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient une description non formalisée de l'activité, de la profession ou de l'occupation d'une personne.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción informal de las actividades, la profesión o la ocupación de una persona.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione informale dell'attività, professione o occupazione di una persona.</desc>
```

^b9

### Block 10

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

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="primary"/>
        <valItem ident="other"/>
        <valItem ident="paid"/>
        <valItem ident="unpaid"/>
      </valList>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">indicates the
      classification system or taxonomy in use, for example by
      supplying the identifier of a <gi>taxonomy</gi> element, or
      pointing to some other resource.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">헤더에 <gi>taxonomy</gi> 요소의 확인소를 제공하여 분류 체계 또는 분류법을 식별한다.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供標頭中元素<gi>taxonomy</gi>的識別符號，來標明所使用的分類系統或分類法。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ヘダー内にある要素<gi>taxonomy</gi>の識別子により、使われている 分類システムを示す。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">identifie le système de classification ou la taxinomie utilisés, en fournissant l'identifiant
                d'un élément <gi>taxonomy</gi> déclaré ailleurs dans l'en-tête.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica el sistema de clasificación o la taxonomía utilizada para la identificación de un
                elemento <gi>taxonomy</gi> colocado en el encabezado.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica il sistema di classificazione o la tassonomia utilizzate tramite l'identificatore di
                un elemento <gi>taxonomy</gi> collocato nell'intestazione</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">identifies an occupation code defined within the classification system or taxonomy defined by the <att>scheme</att>
                attribute.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><att>scheme</att> 속성에 의해 정의된 분류 체계 또는 분류법 내에서 정의된 직업 부호를 식별한다.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明分類系統或分類法中所定義的職業代碼，該分類系統或分類法由屬性<att>scheme</att>所定義。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性<att>scheme</att>で定義されている分類システムの中で定義され る仕事コードを示す。</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient un code d'activité défini dans le système de classification ou dans la taxonomie déclaré
                dans l'attribut <att>scheme</att>.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica un código relativo a la ocupación definido en el sistema de clasificación o taxonomía
                establecido por el atributo <att>scheme</att>.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">corrisponde a un codice relativo all'occupazione definito nel sistema di classificazione o
                tassonomia stabiliti dall'attributo <att>scheme</att></desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-tv">
      <occupation>accountant</occupation>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-ly">
      <occupation>Comptable</occupation>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-ll">
      <occupation scheme="#fr_rg" code="#acc">Comptable</occupation>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-ba">
      <occupation scheme="#fr_rg" code="#acc">Comptable spécialisé dans l'industrie
        pétrolière</occupation>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-we">
      <occupation>會計師</occupation>
    </egXML>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-ts">
      <occupation scheme="#zh-tw_rg" code="#acc">擅長油業的會計師</occupation>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-occupation-egXML-cz">
      <occupation scheme="#occupationtaxonomy" code="#acc">accountant</occupation>
    </egXML>
  </exemplum>
```

^b36

### Block 37

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="occupation-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The content of this element may be used as an alternative to the more formal specification made possible by its attributes; it may also be
            used to supplement the formal specification with commentary or clarification.</p>
  </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="occupation-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p>Le contenu de cet élément peut être utilisé à la place d'une caractérisation plus formelle que ses attributs permettent ; il peut aussi
            être utilisé pour compléter cette caractérisation formelle par un commentaire ou une explication.</p>
  </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="occupation-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素の内容は、より形式的な定義の代替として使用されるかもしれな い。また、解説または分類を伴う形式的定義を補うために使用されるかも しれない。 </p>
  </remarks>
```

^b39

### Block 40

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b40

