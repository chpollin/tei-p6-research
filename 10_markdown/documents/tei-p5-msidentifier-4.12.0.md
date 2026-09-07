---
type: representation
source-type: document
source: '[[00_sources/tei-p5-msidentifier-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 msIdentifier
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/msIdentifier.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# msIdentifier

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4790. Git blob: `3bd8b801df1c2f77d63e044b5e2cf8150aeb77a1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="MSIDENTIFIER" ident="msIdentifier">
  <gloss versionDate="2007-07-04" xml:lang="en">manuscript identifier</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">원고 확인소</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">identificador del manuscrito</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">identifiant du manuscrit</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">identificatore del manoscritto</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="msidentifier.desc">contains the information required to identify the manuscript or similar object being described.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">기술되고 있는 원고를 식별하기 위해 필요한 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含識別敘述中的手稿所需要的資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">解説されている手書き資料を特定するために必要な情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient les informations requises pour identifier le manuscrit en cours de description.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la información necesaria para identificar el manuscrito que se examina.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene l'informazione necessaria a identificare il manoscritto esaminato.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
  <content>
    <sequence>
      <sequence>
        <classRef key="model.placeNamePart" expand="sequenceOptional"/>        
        <elementRef key="institution" minOccurs="0"/>
        <elementRef key="repository" minOccurs="0"/>
        <elementRef key="collection" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="idno" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="msName"/>
        <elementRef key="objectName"/>
        <elementRef key="altIdentifier"/>
      </alternate>
    </sequence>
  </content>
  <constraintSpec scheme="schematron" ident="msId_minimal" xml:lang="en">
    <constraint>
      <sch:rule context="tei:msIdentifier">
        <sch:report test="not( parent::tei:msPart )
                          and
                          ( child::*[1]/self::idno  or  child::*[1]/self::altIdentifier  or  normalize-space(.) eq '')">An &lt;msIdentifier> must contain either a &lt;repository> or &lt;location>.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSIDENTIFIER-egXML-ie">
      <msIdentifier>
        <settlement>San Marino</settlement>
        <repository>Huntington Library</repository>
        <idno>MS.El.26.C.9</idno>
      </msIdentifier>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSIDENTIFIER-egXML-og" source="#fr-ex-BnF-Reliures">
      <msIdentifier>
        <country>France</country>
        <settlement>Paris</settlement>
        <repository xml:lang="fr">Bibliothèque nationale de France. Réserve des livres rares&gt;</repository>
        <idno>B- 73</idno>
        <!-- dans le cas des recueils : cote uniquement sans les sous-cotes -->
        <altIdentifier>
          <idno>B-121</idno>
          <note> Cote de la bibliothèque royale au XVIIIe siècle (inscrite à l'encre, sur la
              doublure de tabis).</note>
        </altIdentifier>
        <altIdentifier>
          <idno>Double de B. 274. A (Réserve)</idno>
          <note>Cote inscrite face à la page de titre, en remplacement de la cote "1541",
            barrée</note>
        </altIdentifier>
      </msIdentifier>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSIDENTIFIER-egXML-oz">
      <msIdentifier>
        <settlement>台北</settlement>
        <repository>故宮博物院</repository>
        <idno>MS.El.26.C.9</idno>
      </msIdentifier>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msid"/>
  </listRef>
</elementSpec>

```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">manuscript identifier</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">원고 확인소</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">identificador del manuscrito</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">identifiant du manuscrit</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">identificatore del manoscritto</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="msidentifier.desc">contains the information required to identify the manuscript or similar object being described.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기술되고 있는 원고를 식별하기 위해 필요한 정보를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含識別敘述中的手稿所需要的資訊。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">解説されている手書き資料を特定するために必要な情報を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient les informations requises pour identifier le manuscrit en cours de description.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la información necesaria para identificar el manuscrito que se examina.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene l'informazione necessaria a identificare il manoscritto esaminato.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.biblPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <sequence>
        <classRef key="model.placeNamePart" expand="sequenceOptional"/>        
        <elementRef key="institution" minOccurs="0"/>
        <elementRef key="repository" minOccurs="0"/>
        <elementRef key="collection" minOccurs="0" maxOccurs="unbounded"/>
        <elementRef key="idno" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="msName"/>
        <elementRef key="objectName"/>
        <elementRef key="altIdentifier"/>
      </alternate>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="msId_minimal" xml:lang="en">
    <constraint>
      <sch:rule context="tei:msIdentifier">
        <sch:report test="not( parent::tei:msPart )
                          and
                          ( child::*[1]/self::idno  or  child::*[1]/self::altIdentifier  or  normalize-space(.) eq '')">An &lt;msIdentifier> must contain either a &lt;repository> or &lt;location>.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSIDENTIFIER-egXML-ie">
      <msIdentifier>
        <settlement>San Marino</settlement>
        <repository>Huntington Library</repository>
        <idno>MS.El.26.C.9</idno>
      </msIdentifier>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSIDENTIFIER-egXML-og" source="#fr-ex-BnF-Reliures">
      <msIdentifier>
        <country>France</country>
        <settlement>Paris</settlement>
        <repository xml:lang="fr">Bibliothèque nationale de France. Réserve des livres rares&gt;</repository>
        <idno>B- 73</idno>
        <!-- dans le cas des recueils : cote uniquement sans les sous-cotes -->
        <altIdentifier>
          <idno>B-121</idno>
          <note> Cote de la bibliothèque royale au XVIIIe siècle (inscrite à l'encre, sur la
              doublure de tabis).</note>
        </altIdentifier>
        <altIdentifier>
          <idno>Double de B. 274. A (Réserve)</idno>
          <note>Cote inscrite face à la page de titre, en remplacement de la cote "1541",
            barrée</note>
        </altIdentifier>
      </msIdentifier>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSIDENTIFIER-egXML-oz">
      <msIdentifier>
        <settlement>台北</settlement>
        <repository>故宮博物院</repository>
        <idno>MS.El.26.C.9</idno>
      </msIdentifier>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msid"/>
  </listRef>
```

^b20

