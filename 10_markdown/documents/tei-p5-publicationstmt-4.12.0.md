---
type: representation
source-type: document
source: '[[00_sources/tei-p5-publicationstmt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 publicationStmt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/publicationStmt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# publicationStmt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8344. Git blob: `018bfba1da7c6cb862144bd22996d29e0078948e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-publicationStmt" ident="publicationStmt">
  <gloss versionDate="2005-01-14" xml:lang="en">publication statement</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">mention de publication</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">출판 진술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">出版陳述</gloss>
    <gloss versionDate="2016-11-17" xml:lang="de">Angaben zur Veröffentlichung</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de la publicación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulla pubblicazione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">groups information concerning the publication or distribution of an electronic or other text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">regroupe des informations concernant la publication ou
    la diffusion d’un texte électronique ou d’un autre type de texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전자 또는 기타 텍스트의 출판 또는 배포에 관한 정보를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集電子文件或其他類型文件的出版或發行相關資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">電子テキストなどの出版や頒布に関する情報をまとめる。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">umfasst Angaben zu Veröffentlichung oder Vertrieb eines elektronischen oder sonstigen Textes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa la información concerniente a la publicación o
    distribución de un texto electrónico u otro texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni riguardo la pubblicazione o la
    distribuzione di un documento elettronico o di altra natua.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      
	<sequence minOccurs="1" maxOccurs="unbounded">
	  
	    <classRef key="model.publicationStmtPart.agency"/>
	  
	  
	    <classRef key="model.publicationStmtPart.detail" minOccurs="0" maxOccurs="unbounded"/>
	  
	</sequence>
      
      
	<classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
    </alternate>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-gg">
      <publicationStmt>
        <publisher>C. Muquardt </publisher>
        <pubPlace>Bruxelles &amp; Leipzig</pubPlace>
        <date when="1846"/>
      </publicationStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-rp" source="#fr-ex-Becque-ee">
      <publicationStmt>
        <distributor>ATILF (Analyse et Traitement Informatique de la Langue Française)</distributor>
        <idno type="FRANTEXT">L434</idno>
        <address>
          <addrLine>44, avenue de la Libération</addrLine>
          <addrLine>BP 30687</addrLine>
          <addrLine>54063 Nancy Cedex</addrLine>
          <addrLine>FRANCE</addrLine>
        </address>
        <availability status="free">
          <p>Dans un cadre de recherche ou d'enseignement</p>
        </availability>
      </publicationStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-zl">
      <publicationStmt>
        <publisher>重慶大學出版社</publisher>
        <pubPlace>中國：重慶</pubPlace>
        <date when="2002"/>
      </publicationStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-ku">
      <publicationStmt>
        <publisher>大塊文化</publisher>
        <pubPlace>台灣：台北</pubPlace>
        <availability>
          <p>版權所有 翻印必究</p>
        </availability>
        <date when="1992">1992</date>
      </publicationStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-xv">
      <publicationStmt>
        <publisher>Chadwyck Healey</publisher>
        <pubPlace>Cambridge</pubPlace>
        <availability>
          <p>Available under licence only</p>
        </availability>
        <date when="1992">1992</date>
      </publicationStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-zc">
      <publicationStmt>
        <publisher>Zea Books</publisher>
        <pubPlace>Lincoln, NE</pubPlace>
        <date>2017</date>
        <availability>
          <p>This is an open access work licensed under a Creative Commons Attribution 4.0 International license.</p>
        </availability>
        <ptr target="http://digitalcommons.unl.edu/zeabook/55"/>
      </publicationStmt>
    </egXML>
  </exemplum>
  <remarks ident="publicationStmt-remarks" versionDate="2014-01-11" xml:lang="en">
    <p>Where a publication statement contains several members of the
      <ident type="class">model.publicationStmtPart.agency</ident> or
      <ident type="class">model.publicationStmtPart.detail</ident>
      classes rather than one or
    more paragraphs or anonymous blocks, care should be taken to
    ensure that the repeated elements are presented in a meaningful
    order. It is a conformance requirement that elements supplying
    information about publication place, address, identifier,
    availability, and date be given following the name of the
    publisher, distributor, or authority concerned, and preferably in
    that order.</p>
  </remarks>
  <remarks ident="publicationStmt-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Bien que non imposé par les schémas, un document conforme à la TEI doit donner des
      informations sur le lieu de publication, l'adresse, l'identifiant, les droits de diffusion et la date
      dans cet ordre, après le nom de l'éditeur, du distributeur, ou de l'autorité concernée.</p>
  </remarks>
  <remarks ident="publicationStmt-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Aunque no sea hecho obligatorio por los esquemas, es un requisito para la conformidad de TEI
      que la información sobre el lugar de publicación, la dirección, el identificador, la
      disponibilidad, y la fecha de publicación. se dé en ese orden, después del nombre del editor,
      del distribuidor, o de la autoridad referida</p>
  </remarks>
  <remarks ident="publicationStmt-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> TEI準拠としてスキーマが求めるものではないが、出版に関する情報は、 出版者名、頒布者名、関連著作者に続いて、出版の場所、住所、識別子、
      可用性、日付が、この順番で出現することが望ましい。 </p>
  </remarks>
  <remarks ident="publicationStmt-remarks" versionDate="2017-06-04" xml:lang="de">
      <p>
        Wenn die Angaben zur Veröffentlichung mehrere Mitglieder der Klassen <ident type="class">model.publicationStmtPart.agency</ident> oder <ident type="class">model.publicationStmtPart.detail</ident>  
          enthalten und nicht einen oder mehrere Absätze (<gi>p</gi>) bzw. unbestimmte Einheiten (<gi>ab</gi>), dann hat 
          die Reihenfolge der Elemente eine Bedeutung, auf die zu achten ist. So müssen Elemente, die Angaben über den Veröffentlichungsort, 
          die Adresse, den Identifikator, die Verfügbarkeit und das Veröffentlichungsdatum enthalten, auf den Namen des Verlags, des 
          Distributors oder der Freigabeinstanz folgen, und zwar möglichst in dieser Reihenfolge.
      </p>
  </remarks>
  <listRef>
    <ptr target="#HD24"/>
    <ptr target="#HD2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">publication statement</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">mention de publication</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">출판 진술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">出版陳述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Angaben zur Veröffentlichung</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de la publicación</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sulla pubblicazione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups information concerning the publication or distribution of an electronic or other text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">regroupe des informations concernant la publication ou
    la diffusion d’un texte électronique ou d’un autre type de texte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전자 또는 기타 텍스트의 출판 또는 배포에 관한 정보를 모아 놓는다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集電子文件或其他類型文件的出版或發行相關資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">電子テキストなどの出版や頒布に関する情報をまとめる。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">umfasst Angaben zu Veröffentlichung oder Vertrieb eines elektronischen oder sonstigen Textes.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa la información concerniente a la publicación o
    distribución de un texto electrónico u otro texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni riguardo la pubblicazione o la
    distribuzione di un documento elettronico o di altra natua.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
	<sequence minOccurs="1" maxOccurs="unbounded">
	  
	    <classRef key="model.publicationStmtPart.agency"/>
	  
	  
	    <classRef key="model.publicationStmtPart.detail" minOccurs="0" maxOccurs="unbounded"/>
	  
	</sequence>
      
      
	<classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-gg">
      <publicationStmt>
        <publisher>C. Muquardt </publisher>
        <pubPlace>Bruxelles &amp; Leipzig</pubPlace>
        <date when="1846"/>
      </publicationStmt>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2010-02-26" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-rp" source="#fr-ex-Becque-ee">
      <publicationStmt>
        <distributor>ATILF (Analyse et Traitement Informatique de la Langue Française)</distributor>
        <idno type="FRANTEXT">L434</idno>
        <address>
          <addrLine>44, avenue de la Libération</addrLine>
          <addrLine>BP 30687</addrLine>
          <addrLine>54063 Nancy Cedex</addrLine>
          <addrLine>FRANCE</addrLine>
        </address>
        <availability status="free">
          <p>Dans un cadre de recherche ou d'enseignement</p>
        </availability>
      </publicationStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-zl">
      <publicationStmt>
        <publisher>重慶大學出版社</publisher>
        <pubPlace>中國：重慶</pubPlace>
        <date when="2002"/>
      </publicationStmt>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-ku">
      <publicationStmt>
        <publisher>大塊文化</publisher>
        <pubPlace>台灣：台北</pubPlace>
        <availability>
          <p>版權所有 翻印必究</p>
        </availability>
        <date when="1992">1992</date>
      </publicationStmt>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-xv">
      <publicationStmt>
        <publisher>Chadwyck Healey</publisher>
        <pubPlace>Cambridge</pubPlace>
        <availability>
          <p>Available under licence only</p>
        </availability>
        <date when="1992">1992</date>
      </publicationStmt>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-publicationStmt-egXML-zc">
      <publicationStmt>
        <publisher>Zea Books</publisher>
        <pubPlace>Lincoln, NE</pubPlace>
        <date>2017</date>
        <availability>
          <p>This is an open access work licensed under a Creative Commons Attribution 4.0 International license.</p>
        </availability>
        <ptr target="http://digitalcommons.unl.edu/zeabook/55"/>
      </publicationStmt>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="publicationStmt-remarks" versionDate="2014-01-11" xml:lang="en">
    <p>Where a publication statement contains several members of the
      <ident type="class">model.publicationStmtPart.agency</ident> or
      <ident type="class">model.publicationStmtPart.detail</ident>
      classes rather than one or
    more paragraphs or anonymous blocks, care should be taken to
    ensure that the repeated elements are presented in a meaningful
    order. It is a conformance requirement that elements supplying
    information about publication place, address, identifier,
    availability, and date be given following the name of the
    publisher, distributor, or authority concerned, and preferably in
    that order.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="publicationStmt-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Bien que non imposé par les schémas, un document conforme à la TEI doit donner des
      informations sur le lieu de publication, l'adresse, l'identifiant, les droits de diffusion et la date
      dans cet ordre, après le nom de l'éditeur, du distributeur, ou de l'autorité concernée.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="publicationStmt-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Aunque no sea hecho obligatorio por los esquemas, es un requisito para la conformidad de TEI
      que la información sobre el lugar de publicación, la dirección, el identificador, la
      disponibilidad, y la fecha de publicación. se dé en ese orden, después del nombre del editor,
      del distribuidor, o de la autoridad referida</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="publicationStmt-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> TEI準拠としてスキーマが求めるものではないが、出版に関する情報は、 出版者名、頒布者名、関連著作者に続いて、出版の場所、住所、識別子、
      可用性、日付が、この順番で出現することが望ましい。 </p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="publicationStmt-remarks" versionDate="2017-06-04" xml:lang="de">
      <p>
        Wenn die Angaben zur Veröffentlichung mehrere Mitglieder der Klassen <ident type="class">model.publicationStmtPart.agency</ident> oder <ident type="class">model.publicationStmtPart.detail</ident>  
          enthalten und nicht einen oder mehrere Absätze (<gi>p</gi>) bzw. unbestimmte Einheiten (<gi>ab</gi>), dann hat 
          die Reihenfolge der Elemente eine Bedeutung, auf die zu achten ist. So müssen Elemente, die Angaben über den Veröffentlichungsort, 
          die Adresse, den Identifikator, die Verfügbarkeit und das Veröffentlichungsdatum enthalten, auf den Namen des Verlags, des 
          Distributors oder der Freigabeinstanz folgen, und zwar möglichst in dieser Reihenfolge.
      </p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD24"/>
    <ptr target="#HD2"/>
  </listRef>
```

^b29

