---
type: representation
source-type: document
source: '[[00_sources/tei-p5-altidentifier-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 altIdentifier
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/altIdentifier.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# altIdentifier

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4613. Git blob: `b894c6200ea78fb6b4f42b6f1edc26b5594aabfc`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="ALTIDENTIFIER" ident="altIdentifier">
  <gloss versionDate="2005-01-14" xml:lang="en">alternative identifier</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">대체 확인소</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">替換識別符碼</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">autre identifiant</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">identificador alternativo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">identificatore alternativo.</gloss>
  <gloss versionDate="2018-12-28" xml:lang="ja">代替識別子</gloss>
  <desc versionDate="2019-01-17" xml:lang="en">contains an alternative or former structured identifier used for a manuscript or other object, such as a former catalogue number.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">이전의 카탈로그의 번호와 같이 원고에 사용된 대체 또는 이전에 구조화된 확인소를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿中的一個替換或先前使用的識別符碼，例如先前的分類碼。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料を示す、代わりとなるIDまたは昔のIDを示す。例えば、昔の
  カタログ番号など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un autre ou un ancien identifiant pour un
  manuscrit, par exemple un numéro anciennement utilisé dans un catalogue.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un identificador estructurado, alternativo o precedente, utilizado para un manuscrito, p.ej. un número antiguo de catalogación.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un identificatore strutturato alternativo o precedente utilizzato per un manoscritto, per esempio un precedente numero di catalogazione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.placeNamePart" expand="sequenceOptional"/>    
      <elementRef key="institution" minOccurs="0"/>
      <elementRef key="repository" minOccurs="0"/>
      <elementRef key="collection" minOccurs="0"/>
      <elementRef key="idno"/>
      <elementRef key="note" minOccurs="0"/>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENTIFIER-egXML-dk" source="#UND">
      <altIdentifier>
        <settlement>San Marino</settlement>
        <repository>Huntington Library</repository>
        <idno>MS.El.26.C.9</idno>
      </altIdentifier>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENTIFIER-egXML-np" source="#fr-ex-BnF-Reliures">
      <altIdentifier>
        <idno>B 106</idno>
        <note>Cote de la Bibliothèque royale au XVIIIe siècle.</note>
      </altIdentifier>
    </egXML>
  </exemplum>
  <exemplum versionDate="2007-05-02" xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENTIFIER-egXML-nt" source="#UND">
      <altIdentifier>
        <settlement>台北市中正區</settlement>
        <repository>國立歷史博物館</repository>
        <idno>MS.El.26.C.9</idno>
      </altIdentifier>
    </egXML>
  </exemplum>
  <remarks ident="altIdentifier-remarks" versionDate="2005-03-01" xml:lang="en">
    <p>An identifying number of some kind must be supplied if
    known; if it is not known, this should be stated. </p>
  </remarks>
  <remarks ident="altIdentifier-remarks" versionDate="2008-04-06" xml:lang="fr">
    <p>Un numéro identifiant quelconque doit être fourni s'il est connu ; si on ne le
    connaît pas, cela devrait être signalé.</p>
  </remarks>
  <remarks ident="altIdentifier-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      識別番号が判る場合は、示す必要がある。判らない場合は、そのことを示
      すべきである。
    </p>
  </remarks>
  <listRef>
    <ptr target="#msid"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">alternative identifier</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">대체 확인소</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">替換識別符碼</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">autre identifiant</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">identificador alternativo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">identificatore alternativo.</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2018-12-28" xml:lang="ja">代替識別子</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en">contains an alternative or former structured identifier used for a manuscript or other object, such as a former catalogue number.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이전의 카탈로그의 번호와 같이 원고에 사용된 대체 또는 이전에 구조화된 확인소를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿中的一個替換或先前使用的識別符碼，例如先前的分類碼。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料を示す、代わりとなるIDまたは昔のIDを示す。例えば、昔の
  カタログ番号など。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un autre ou un ancien identifiant pour un
  manuscrit, par exemple un numéro anciennement utilisé dans un catalogue.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un identificador estructurado, alternativo o precedente, utilizado para un manuscrito, p.ej. un número antiguo de catalogación.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un identificatore strutturato alternativo o precedente utilizzato per un manoscritto, per esempio un precedente numero di catalogazione.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.placeNamePart" expand="sequenceOptional"/>    
      <elementRef key="institution" minOccurs="0"/>
      <elementRef key="repository" minOccurs="0"/>
      <elementRef key="collection" minOccurs="0"/>
      <elementRef key="idno"/>
      <elementRef key="note" minOccurs="0"/>
    </sequence>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENTIFIER-egXML-dk" source="#UND">
      <altIdentifier>
        <settlement>San Marino</settlement>
        <repository>Huntington Library</repository>
        <idno>MS.El.26.C.9</idno>
      </altIdentifier>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENTIFIER-egXML-np" source="#fr-ex-BnF-Reliures">
      <altIdentifier>
        <idno>B 106</idno>
        <note>Cote de la Bibliothèque royale au XVIIIe siècle.</note>
      </altIdentifier>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2007-05-02" xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ALTIDENTIFIER-egXML-nt" source="#UND">
      <altIdentifier>
        <settlement>台北市中正區</settlement>
        <repository>國立歷史博物館</repository>
        <idno>MS.El.26.C.9</idno>
      </altIdentifier>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="altIdentifier-remarks" versionDate="2005-03-01" xml:lang="en">
    <p>An identifying number of some kind must be supplied if
    known; if it is not known, this should be stated. </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="altIdentifier-remarks" versionDate="2008-04-06" xml:lang="fr">
    <p>Un numéro identifiant quelconque doit être fourni s'il est connu ; si on ne le
    connaît pas, cela devrait être signalé.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="altIdentifier-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      識別番号が判る場合は、示す必要がある。判らない場合は、そのことを示
      すべきである。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msid"/>
  </listRef>
```

^b23

