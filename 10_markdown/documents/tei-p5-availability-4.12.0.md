---
type: representation
source-type: document
source: '[[00_sources/tei-p5-availability-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 availability
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/availability.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# availability

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11302. Git blob: `32b8280c3b036d504684294165b386e1857b8b2d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-availability" ident="availability">
  <gloss versionDate="2007-06-12" xml:lang="en">availability</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">disponibilité</gloss>
  <gloss versionDate="2022-06-01" xml:lang="it">disponibilità</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Verfügbarkeit</gloss>
  <desc versionDate="2011-11-17" xml:lang="en">supplies information about the availability of a text, for example any restrictions on its use or distribution, its copyright status, any licence applying to it, etc.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">renseigne sur la disponibilité du texte, par exemple sur toutes restrictions quant à son usage ou sa diffusion, son copyright, etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 이용에 관한 정보를 제시한다. 예를 들어 사용 또는 배포의 제한, 저작권 상태 등.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供關於文件可利用性的資訊，例如使用或發行上的任何限制、版權狀態等。</desc>
  <desc versionDate="2023-08-30" xml:lang="ja">テキストの利用許可に関する情報を示す。例えば、その使用や頒布の制限、著作権の状態、適用されるライセンス等。</desc>
  <desc versionDate="2016-11-17" xml:lang="de">liefert Informationen zur Verfügbarkeit eines Textes, zum Beispiel Einschränkungen bezüglich des Gebrauchs oder der Weitergabe, Lizensierungen usw.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona información sobre la disponibilidad de un texto, por ejemplo cualquier restricción en cuanto a su uso o distribución, su copyright, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni sulla disponibilità di un testo, per esempio su qualsiasi restrizione che si applica alla sua utilizzazione o distribuzione, il suo statuto in merito al copyright, etc.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.publicationStmtPart.detail"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.availabilityPart"/>
      <classRef key="model.pLike"/>
    </alternate>    
  </content>
  <constraintSpec ident="availability-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:availability"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="status" usage="opt">
      <gloss versionDate="2016-11-25" xml:lang="en">status</gloss>
      <gloss versionDate="2016-11-25" xml:lang="de">Statuscode</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">supplies a code identifying the current availability of the text.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">donne un code caractérisant la disponibilité actuelle d’un texte.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 현재 이용 가능성을 식별하는 부호를 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個代號，用來確認文件目前的可利用性。</desc>
      <desc versionDate="2008-04-06" xml:lang="ja">当該テキストの、現在の利用可能性を表すコードを示す。</desc>
      <desc versionDate="2016-11-17" xml:lang="de">gibt einen Code an, der die derzeitige Nutzbarkeit eines Textes festlegt.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona un código identificativo de la disponibilidad actual del texto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce un codice che identifica l'attuale disponibilità del testo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="free">
          <gloss versionDate="2016-11-25" xml:lang="en">free</gloss>
          <gloss versionDate="2016-11-25" xml:lang="de">frei</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the text is freely available.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte est libre de droits.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트를 자유롭게 이용할 수 있음.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文件的可利用性不受限。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto está libremente disponible.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該テキストは、自由に使用できる。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è disponibile gratuitamente.</desc>
          <desc versionDate="2016-11-17" xml:lang="de">der Text ist frei verfügbar.</desc>
        </valItem>
        <valItem ident="unknown">
          <gloss versionDate="2016-11-25" xml:lang="en">unknown</gloss>
          <gloss versionDate="2016-11-25" xml:lang="de">unbekannt</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the status of the text is unknown.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le statut du texte est inconnu.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 상태를 알 수 없다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文件狀態不明。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el estatus del texto es desconocido.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該テキストの利用可能性は不明。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la disponibilità del testo non è nota.</desc>
          <desc versionDate="2016-11-17" xml:lang="de">der Status des Textes ist unbekannt.</desc>
        </valItem>
        <valItem ident="restricted">
          <gloss versionDate="2016-11-25" xml:lang="en">restricted</gloss>
          <gloss versionDate="2016-11-25" xml:lang="de">eingeschränkt</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the text is not freely available.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte est sous droits.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트를 자유롭게 사용할 수 없음.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文件的可利用性受限制。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto no está libremente disponible.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該テキストは、自由に使用できない。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo non è disponibile gratuitamente.</desc>
          <desc versionDate="2016-11-17" xml:lang="de">der Text ist nicht frei verfügbar.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-availability-egXML-br">
      <availability status="restricted">
        <p>Available for academic research purposes only.</p>
      </availability>
      <availability status="free">
        <p>In the public domain</p>
      </availability>
      <availability status="restricted">
        <p>Available under licence from the publishers.</p>
      </availability>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-availability-egXML-nl" source="#fr-ex-Abes">
      <availability status="restricted">
        <p>L' ABES a adopté le système Créative Commons pour permettre à tous ceux qui le
        souhaitent, de reproduire tout ou partie des rubriques du site de l'ABES sur support
        papier ou support électronique.</p>
      </availability>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-availability-egXML-ot">
      <availability status="restricted">
        <p>僅供學術研究使用</p>
      </availability>
      <availability status="free">
        <p>用於公共領域</p>
      </availability>
      <availability status="restricted">
        <p>需徵求出版商授權</p>
      </availability>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-availability-egXML-pt">
      <availability>
        <licence target="http://opensource.org/licenses/MIT">
          <p>The MIT License
          applies to this document.</p>
          <p>Copyright (C) 2011 by The University of Victoria</p>
          <p>Permission is hereby granted, free of charge, to any person obtaining a copy
          of this software and associated documentation files (the "Software"), to deal
          in the Software without restriction, including without limitation the rights
          to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
          copies of the Software, and to permit persons to whom the Software is
          furnished to do so, subject to the following conditions:</p>
          <p>The above copyright notice and this permission notice shall be included in
          all copies or substantial portions of the Software.</p>
          <p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
          IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
          FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
          AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
          LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
          OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
          THE SOFTWARE.</p>
        </licence>
      </availability>
    </egXML>
  </exemplum>
  <remarks ident="availability-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">A consistent format should be adopted</p>
  </remarks>
  <remarks ident="availability-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">On devrait adopter un format de codage reconnu.</p>
  </remarks>
  <remarks ident="availability-remarks" versionDate="2008-04-06" xml:lang="es">
    <p rend="dataDesc">Se debe adoptar un formato constante</p>
  </remarks>
  <remarks ident="availability-remarks" versionDate="2023-08-30" xml:lang="ja">
    <p rend="dataDesc">一貫した形式を採用すべきである。</p>
  </remarks>
  <remarks ident="availability-remarks" versionDate="2016-11-17" xml:lang="de">
    <p rend="dataDesc">Es sollte ein einheitliches Format verwendet werden.</p>
  </remarks>
  <listRef>
    <ptr target="#HD24"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">availability</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">disponibilité</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2022-06-01" xml:lang="it">disponibilità</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Verfügbarkeit</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-17" xml:lang="en">supplies information about the availability of a text, for example any restrictions on its use or distribution, its copyright status, any licence applying to it, etc.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">renseigne sur la disponibilité du texte, par exemple sur toutes restrictions quant à son usage ou sa diffusion, son copyright, etc.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 이용에 관한 정보를 제시한다. 예를 들어 사용 또는 배포의 제한, 저작권 상태 등.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供關於文件可利用性的資訊，例如使用或發行上的任何限制、版權狀態等。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2023-08-30" xml:lang="ja">テキストの利用許可に関する情報を示す。例えば、その使用や頒布の制限、著作権の状態、適用されるライセンス等。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">liefert Informationen zur Verfügbarkeit eines Textes, zum Beispiel Einschränkungen bezüglich des Gebrauchs oder der Weitergabe, Lizensierungen usw.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona información sobre la disponibilidad de un texto, por ejemplo cualquier restricción en cuanto a su uso o distribución, su copyright, etc.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni sulla disponibilità di un testo, per esempio su qualsiasi restrizione che si applica alla sua utilizzazione o distribuzione, il suo statuto in merito al copyright, etc.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.publicationStmtPart.detail"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <classRef key="model.availabilityPart"/>
      <classRef key="model.pLike"/>
    </alternate>    
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="availability-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:availability"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="en">status</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Statuscode</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">supplies a code identifying the current availability of the text.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">donne un code caractérisant la disponibilité actuelle d’un texte.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 현재 이용 가능성을 식별하는 부호를 제공한다.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個代號，用來確認文件目前的可利用性。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">当該テキストの、現在の利用可能性を表すコードを示す。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">gibt einen Code an, der die derzeitige Nutzbarkeit eines Textes festlegt.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona un código identificativo de la disponibilidad actual del texto.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce un codice che identifica l'attuale disponibilità del testo.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="free">
          <gloss versionDate="2016-11-25" xml:lang="en">free</gloss>
          <gloss versionDate="2016-11-25" xml:lang="de">frei</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the text is freely available.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte est libre de droits.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트를 자유롭게 이용할 수 있음.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文件的可利用性不受限。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto está libremente disponible.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該テキストは、自由に使用できる。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è disponibile gratuitamente.</desc>
          <desc versionDate="2016-11-17" xml:lang="de">der Text ist frei verfügbar.</desc>
        </valItem>
        <valItem ident="unknown">
          <gloss versionDate="2016-11-25" xml:lang="en">unknown</gloss>
          <gloss versionDate="2016-11-25" xml:lang="de">unbekannt</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the status of the text is unknown.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le statut du texte est inconnu.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 상태를 알 수 없다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文件狀態不明。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el estatus del texto es desconocido.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該テキストの利用可能性は不明。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la disponibilità del testo non è nota.</desc>
          <desc versionDate="2016-11-17" xml:lang="de">der Status des Textes ist unbekannt.</desc>
        </valItem>
        <valItem ident="restricted">
          <gloss versionDate="2016-11-25" xml:lang="en">restricted</gloss>
          <gloss versionDate="2016-11-25" xml:lang="de">eingeschränkt</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">the text is not freely available.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte est sous droits.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트를 자유롭게 사용할 수 없음.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">文件的可利用性受限制。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto no está libremente disponible.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該テキストは、自由に使用できない。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo non è disponibile gratuitamente.</desc>
          <desc versionDate="2016-11-17" xml:lang="de">der Text ist nicht frei verfügbar.</desc>
        </valItem>
      </valList>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-availability-egXML-br">
      <availability status="restricted">
        <p>Available for academic research purposes only.</p>
      </availability>
      <availability status="free">
        <p>In the public domain</p>
      </availability>
      <availability status="restricted">
        <p>Available under licence from the publishers.</p>
      </availability>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-availability-egXML-nl" source="#fr-ex-Abes">
      <availability status="restricted">
        <p>L' ABES a adopté le système Créative Commons pour permettre à tous ceux qui le
        souhaitent, de reproduire tout ou partie des rubriques du site de l'ABES sur support
        papier ou support électronique.</p>
      </availability>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-availability-egXML-ot">
      <availability status="restricted">
        <p>僅供學術研究使用</p>
      </availability>
      <availability status="free">
        <p>用於公共領域</p>
      </availability>
      <availability status="restricted">
        <p>需徵求出版商授權</p>
      </availability>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-availability-egXML-pt">
      <availability>
        <licence target="http://opensource.org/licenses/MIT">
          <p>The MIT License
          applies to this document.</p>
          <p>Copyright (C) 2011 by The University of Victoria</p>
          <p>Permission is hereby granted, free of charge, to any person obtaining a copy
          of this software and associated documentation files (the "Software"), to deal
          in the Software without restriction, including without limitation the rights
          to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
          copies of the Software, and to permit persons to whom the Software is
          furnished to do so, subject to the following conditions:</p>
          <p>The above copyright notice and this permission notice shall be included in
          all copies or substantial portions of the Software.</p>
          <p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
          IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
          FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
          AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
          LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
          OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
          THE SOFTWARE.</p>
        </licence>
      </availability>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="availability-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">A consistent format should be adopted</p>
  </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="availability-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">On devrait adopter un format de codage reconnu.</p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="availability-remarks" versionDate="2008-04-06" xml:lang="es">
    <p rend="dataDesc">Se debe adoptar un formato constante</p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="availability-remarks" versionDate="2023-08-30" xml:lang="ja">
    <p rend="dataDesc">一貫した形式を採用すべきである。</p>
  </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="availability-remarks" versionDate="2016-11-17" xml:lang="de">
    <p rend="dataDesc">Es sollte ein einheitliches Format verwendet werden.</p>
  </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD24"/>
  </listRef>
```

^b37

