---
type: representation
source-type: document
source: '[[00_sources/tei-p5-objectdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 objectDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/objectDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# objectDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5427. Git blob: `2b7d1ccb05774f7cde67b3335602428a13819d7a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="OBJECTDESC" ident="objectDesc">
  <gloss versionDate="2020-12-20" xml:lang="en">object description</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description d'objet</gloss>
  <desc versionDate="2019-01-17" xml:lang="en">contains a description of the physical components making up the object which is being described.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">기술되고 있는 대상을 구성하는 물리적 성분에 대한 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含討論中物件的材質組成成分描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該対象の物理的構成要素の解説を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description des composants matériels de
      l'objet en cours de traitement.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de los componentes físicos que constituyen el objeto descrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione delle componenti fisiche che costituiscono l'oggetto descritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="supportDesc" minOccurs="0"/>
        
        
          <elementRef key="layoutDesc" minOccurs="0"/>
        
      </sequence>
    </alternate>
  </content>
  <attList>
    <attDef ident="form">
      <gloss versionDate="2007-06-12" xml:lang="en">form</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">forme</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">a short  project-specific name identifying the physical form of
      the carrier, for example as a codex, roll, fragment, partial leaf,
      cutting etc.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">미제본 원고, 명부, 부분, 부분적 장, 잘라낸 것 등과 같이 물리적 형태를 식별하는,  프로젝트에서 사용하는 간단한 이름</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">一個簡短的用途專用名稱，表示該媒介的物質外形，例如手抄本、名冊、斷片、部分頁面、剪報等。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該キャリアの物理的な形を示す、プロジェクト固有の短い名前。例え
      ば、冊子、巻子、断片、切れ端など。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">contient un nom abrégé spécifique au projet,
          désignant la forme physique du support, par exemple : codex, rouleau, fragment, fragment
          de feuillet, découpe, etc.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">un nombre breve específico de un proyecto que identifica la forma física del documento, por ejemplo códex, rollo, fragmento, folio parcial, recorte, etc.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">un nome breve specifico di un progetto che identifica la forma fisica del documento, per esempio codice, rotolo, frammento, foglio parziale, ritaglio, ecc.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
<remarks ident="objectDesc-attr.form-remarks" versionDate="2013-12-21" xml:lang="en"><p>Definitions for the
terms used may typically be provided by a
	<gi>valList</gi> element in the project schema
specification.</p></remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTDESC-egXML-ds">
      <objectDesc form="codex">
        <supportDesc material="mixed">
          <p>Early modern
<material>parchment</material> and
<material>paper</material>.</p>
        </supportDesc>
        <layoutDesc>
          <layout ruledLines="25 32"/>
        </layoutDesc>
      </objectDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTDESC-egXML-vo" source="#fr-ex-BnF-Reliures">
      <objectDesc>
        <supportDesc>
          <extent>
            <dimensions type="binding">
              <height unit="mm">168</height>
              <width unit="mm">106</width>
              <depth unit="mm">22</depth>
            </dimensions>
          </extent>
        </supportDesc>
      </objectDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTDESC-egXML-lh">
      <objectDesc form="codex">
        <supportDesc material="mixed">
          <p>現代早期 <material>羊皮紙</material>與<material>白紙</material>。</p>
        </supportDesc>
        <layoutDesc>
          <layout ruledLines="25 32"/>
        </layoutDesc>
      </objectDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">object description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description d'objet</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en">contains a description of the physical components making up the object which is being described.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기술되고 있는 대상을 구성하는 물리적 성분에 대한 기술을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含討論中物件的材質組成成分描述。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該対象の物理的構成要素の解説を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description des composants matériels de
      l'objet en cours de traitement.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de los componentes físicos que constituyen el objeto descrito.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione delle componenti fisiche che costituiscono l'oggetto descritto.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="supportDesc" minOccurs="0"/>
        
        
          <elementRef key="layoutDesc" minOccurs="0"/>
        
      </sequence>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">form</gloss>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">forme</gloss>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">a short  project-specific name identifying the physical form of
      the carrier, for example as a codex, roll, fragment, partial leaf,
      cutting etc.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">미제본 원고, 명부, 부분, 부분적 장, 잘라낸 것 등과 같이 물리적 형태를 식별하는,  프로젝트에서 사용하는 간단한 이름</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">一個簡短的用途專用名稱，表示該媒介的物質外形，例如手抄本、名冊、斷片、部分頁面、剪報等。</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該キャリアの物理的な形を示す、プロジェクト固有の短い名前。例え
      ば、冊子、巻子、断片、切れ端など。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un nom abrégé spécifique au projet,
          désignant la forme physique du support, par exemple : codex, rouleau, fragment, fragment
          de feuillet, découpe, etc.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">un nombre breve específico de un proyecto que identifica la forma física del documento, por ejemplo códex, rollo, fragmento, folio parcial, recorte, etc.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">un nome breve specifico di un progetto che identifica la forma fisica del documento, per esempio codice, rotolo, frammento, foglio parziale, ritaglio, ecc.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="objectDesc-attr.form-remarks" versionDate="2013-12-21" xml:lang="en"><p>Definitions for the
terms used may typically be provided by a
	<gi>valList</gi> element in the project schema
specification.</p></remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTDESC-egXML-ds">
      <objectDesc form="codex">
        <supportDesc material="mixed">
          <p>Early modern
<material>parchment</material> and
<material>paper</material>.</p>
        </supportDesc>
        <layoutDesc>
          <layout ruledLines="25 32"/>
        </layoutDesc>
      </objectDesc>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTDESC-egXML-vo" source="#fr-ex-BnF-Reliures">
      <objectDesc>
        <supportDesc>
          <extent>
            <dimensions type="binding">
              <height unit="mm">168</height>
              <width unit="mm">106</width>
              <depth unit="mm">22</depth>
            </dimensions>
          </extent>
        </supportDesc>
      </objectDesc>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="OBJECTDESC-egXML-lh">
      <objectDesc form="codex">
        <supportDesc material="mixed">
          <p>現代早期 <material>羊皮紙</material>與<material>白紙</material>。</p>
        </supportDesc>
        <layoutDesc>
          <layout ruledLines="25 32"/>
        </layoutDesc>
      </objectDesc>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph1"/>
  </listRef>
```

^b26

