---
type: representation
source-type: document
source: '[[00_sources/tei-p5-respstmt-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 respStmt
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/respStmt.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# respStmt

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6147. Git blob: `dc51e20fd826d910bf193cbfd0ee8f4016e2abb9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-respStmt" ident="respStmt">
  <gloss versionDate="2005-03-01" xml:lang="en">statement of responsibility</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">책임성 진술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">責任陳述</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">mention de responsabilité</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de responsabilidad</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione di responsabilità</gloss>
  <gloss versionDate="2017-06-04" xml:lang="de">Angaben zur Verantwortlichkeit</gloss>
  <desc versionDate="2011-11-16" xml:lang="en">supplies a statement of responsibility for the intellectual content of a text, edition,
    recording, or series, where the specialized elements for authors, editors, etc. do not suffice
    or do not apply. May also be used to encode information about individuals or organizations 
    which have played a role in the production or distribution of a bibliographic work.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트, 편집, 녹음 또는 총서의 지적 내용에 대한 책임성 진술을 제시한다. 여기에서 작가, 편집자
    등에 대한 특별한 요소는 충분치 않거나 적용되지 않는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">當未使用作者、編輯者等特定元素，或元素內容不足時，在此補充說明文件、版本、記錄、或是叢書的智慧內容所屬負責人的責任陳述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">著者や編集者など特定の役割を示す要素が充分ではない場合に、テキスト、 版、記録などの知的内容に関する責任を示す。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">indique la responsabilité quant au contenu
    intellectuel d'un texte, d'une édition, d'un enregistrement ou d'une publication en série,
    lorsque les éléments spécifiques relatifs aux auteurs, éditeurs, etc. ne suffisent pas ou ne
    s'appliquent pas.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona la declaración de la responsabilidad para el
    contenido intelectual de un texto, edición, grabación o serie, donde no basten o no se apliquen
    los elementos especializados para autores, editores, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce una dichiarazione di responsabilità per qualcuno
    responsabile del contenuto intelletuale di un testo, curatela, registrazione o collana, nel caso
    in cui gli elementi specifici per autore, curatore ecc. non sono sufficienti o non applicabili.</desc>
  <desc versionDate="2017-06-04" xml:lang="de">enthält Angaben zur Verantwortlichkeit für den intellektuellen Inhalt eines Textes, einer
    Edition, einer Aufnahme oder Reihe, wo die spezialisierten Elemente <gi>author</gi>,
    <gi>editor</gi> etc. nicht ausreichen oder unzutreffend sind; auch verwendbar für
    Informationen zu Individuen oder Organisationen, die bei der Produktion oder Verbreitung eines
    bibliografischen Objekts eine Rolle gespielt.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.recordingPart"/>
    <memberOf key="model.respLike"/>
  </classes>
  <content>
    <sequence>
      <alternate>
        <sequence>
          
          <elementRef key="resp" minOccurs="1" maxOccurs="unbounded"/>
          
          
          <classRef key="model.nameLike.agent" minOccurs="1" maxOccurs="unbounded"/>
          
        </sequence>
        <sequence>
          
          <classRef key="model.nameLike.agent" minOccurs="1" maxOccurs="unbounded"/>
          
          
          <elementRef key="resp" minOccurs="1" maxOccurs="unbounded"/>
          
        </sequence>
      </alternate>
      <elementRef key="note" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-bb">
      <respStmt>
        <resp>transcribed from original ms</resp>
        <persName>Claus Huitfeldt</persName>
      </respStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-oc">
      <respStmt>
        <resp>Nouvelle édition originale</resp>
        <persName>Geneviève Hasenohr</persName>
      </respStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-kv">
      <respStmt>
        <resp>converti en langage SGML</resp>
        <name>Alan Morrison</name>
      </respStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-ka">
      <respStmt>
        <resp>謄寫自原始手稿</resp>
        <persName>徐大明</persName>
      </respStmt>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-mo">
      <respStmt>
        <resp>轉換成SGML編碼</resp>
        <name>許雁</name>
      </respStmt>
    </egXML>
  </exemplum>
  <exemplum versionDate="2012-07-16" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-xi">
      <respStmt>
        <resp>converted to XML encoding</resp>
        <name>Alan Morrison</name>
      </respStmt>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COBICOR"/>
    <ptr target="#HD21"/>
    <ptr target="#HD22"/>
    <ptr target="#HD26"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-03-01" xml:lang="en">statement of responsibility</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">책임성 진술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">責任陳述</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">mention de responsabilité</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de responsabilidad</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione di responsabilità</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-04" xml:lang="de">Angaben zur Verantwortlichkeit</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-16" xml:lang="en">supplies a statement of responsibility for the intellectual content of a text, edition,
    recording, or series, where the specialized elements for authors, editors, etc. do not suffice
    or do not apply. May also be used to encode information about individuals or organizations 
    which have played a role in the production or distribution of a bibliographic work.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트, 편집, 녹음 또는 총서의 지적 내용에 대한 책임성 진술을 제시한다. 여기에서 작가, 편집자
    등에 대한 특별한 요소는 충분치 않거나 적용되지 않는다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">當未使用作者、編輯者等特定元素，或元素內容不足時，在此補充說明文件、版本、記錄、或是叢書的智慧內容所屬負責人的責任陳述。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">著者や編集者など特定の役割を示す要素が充分ではない場合に、テキスト、 版、記録などの知的内容に関する責任を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">indique la responsabilité quant au contenu
    intellectuel d'un texte, d'une édition, d'un enregistrement ou d'une publication en série,
    lorsque les éléments spécifiques relatifs aux auteurs, éditeurs, etc. ne suffisent pas ou ne
    s'appliquent pas.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona la declaración de la responsabilidad para el
    contenido intelectual de un texto, edición, grabación o serie, donde no basten o no se apliquen
    los elementos especializados para autores, editores, etc.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce una dichiarazione di responsabilità per qualcuno
    responsabile del contenuto intelletuale di un testo, curatela, registrazione o collana, nel caso
    in cui gli elementi specifici per autore, curatore ecc. non sono sufficienti o non applicabili.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-04" xml:lang="de">enthält Angaben zur Verantwortlichkeit für den intellektuellen Inhalt eines Textes, einer
    Edition, einer Aufnahme oder Reihe, wo die spezialisierten Elemente <gi>author</gi>,
    <gi>editor</gi> etc. nicht ausreichen oder unzutreffend sind; auch verwendbar für
    Informationen zu Individuen oder Organisationen, die bei der Produktion oder Verbreitung eines
    bibliografischen Objekts eine Rolle gespielt.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="model.recordingPart"/>
    <memberOf key="model.respLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate>
        <sequence>
          
          <elementRef key="resp" minOccurs="1" maxOccurs="unbounded"/>
          
          
          <classRef key="model.nameLike.agent" minOccurs="1" maxOccurs="unbounded"/>
          
        </sequence>
        <sequence>
          
          <classRef key="model.nameLike.agent" minOccurs="1" maxOccurs="unbounded"/>
          
          
          <elementRef key="resp" minOccurs="1" maxOccurs="unbounded"/>
          
        </sequence>
      </alternate>
      <elementRef key="note" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>    
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-bb">
      <respStmt>
        <resp>transcribed from original ms</resp>
        <persName>Claus Huitfeldt</persName>
      </respStmt>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-oc">
      <respStmt>
        <resp>Nouvelle édition originale</resp>
        <persName>Geneviève Hasenohr</persName>
      </respStmt>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-kv">
      <respStmt>
        <resp>converti en langage SGML</resp>
        <name>Alan Morrison</name>
      </respStmt>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-ka">
      <respStmt>
        <resp>謄寫自原始手稿</resp>
        <persName>徐大明</persName>
      </respStmt>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-mo">
      <respStmt>
        <resp>轉換成SGML編碼</resp>
        <name>許雁</name>
      </respStmt>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum versionDate="2012-07-16" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-respStmt-egXML-xi">
      <respStmt>
        <resp>converted to XML encoding</resp>
        <name>Alan Morrison</name>
      </respStmt>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOR"/>
    <ptr target="#HD21"/>
    <ptr target="#HD22"/>
    <ptr target="#HD26"/>
  </listRef>
```

^b24

