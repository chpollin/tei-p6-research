---
type: representation
source-type: document
source: '[[00_sources/tei-p5-profiledesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 profileDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/profileDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# profileDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6680. Git blob: `3a5d134c6a4a33dd0cb54a09b1ec796bd3dc87f9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-profileDesc" ident="profileDesc">
  <gloss versionDate="2005-01-14" xml:lang="en">text-profile description</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">description du profil</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">텍스트-개요 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文件背景描述</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Beschreibung des Textprofils</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción del perfil del texto.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione del profilo del testo</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides a detailed description of non-bibliographic aspects of a text, specifically the
    languages and sublanguages used, the situation in which it was produced, the participants and
    their setting.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">fournit une description détaillée des aspects
    non bibliographiques du texte, notamment les langues utilisées et leurs variantes, les
    circonstances de sa production, les collaborateurs et leur statut.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">분명하게 언어와 특수 언어가 사용된 텍스트, 텍스트가 생산된 상황, 참여자, 배경에 관한 비서지적
    측면을 상세히 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供文件非書目性方面的細節描述，特別是所使用的語言及次要語言、在何種情況下製作、參與人員及其環境背景。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">書誌情報的ではない詳細な解説を示す。例えば、言語や特殊言語、生成され たときの状況、参加者など。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">enthält eine detaillierte Beschreibung der nicht-bibliografischen Merkmale des Textes, besonders der verwendeten Sprachen und Subsprachen, 
        der Entstehungsbedingungen eines Textes sowie der Beteiligten und deren Umfeld.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona una descripción detallada de los aspectos no
    bibliográficos de un texto, especialmente las lenguas y jergas usadas, la situación en que se
    aparecen, los participantes que intervienen, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce una descrizione dettagliata degli aspetti non
    bibliografici di un testo, in modo particolare le lingue e i linguaggi secondari utilizzati, la
    situazione in cui è stato prodotto il testo, i partecipanti e la relativa ambientazione</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.teiHeaderPart"/>
  </classes>
  <content>
    
      
        <classRef key="model.profileDescPart" minOccurs="0" maxOccurs="unbounded"/>
      
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-profileDesc-egXML-bf">
      <profileDesc>
        <langUsage>
          <language ident="fr">French</language>
        </langUsage>
        <textDesc n="novel">
          <channel mode="w">print; part issues</channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepared"/>
          <purpose type="entertain" degree="high"/>
          <purpose type="inform" degree="medium"/>
        </textDesc>
        <settingDesc>
          <setting>
            <name>Paris, France</name>
            <time>Late 19th century</time>
          </setting>
        </settingDesc>
      </profileDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-profileDesc-egXML-xo">
      <profileDesc>
        <langUsage>
          <language ident="fr">français</language>
        </langUsage>
        <textDesc n="roman">
          <channel mode="w">copie; extraits </channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepare"/>
          <purpose type="distraction" degree="high"/>
          <purpose type="information" degree="medium"/>
        </textDesc>
        <settingDesc>
          <setting>
            <name>Paris, France</name>
            <time>Fin 19e</time>
          </setting>
        </settingDesc>
      </profileDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-profileDesc-egXML-oe">
      <profileDesc>
        <langUsage>
          <language ident="fr">法文</language>
        </langUsage>
        <textDesc n="novel">
          <channel mode="w">出版品；專題輯</channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepared"/>
          <purpose type="entertain" degree="high"/>
          <purpose type="inform" degree="medium"/>
        </textDesc>
        <settingDesc>
          <setting>
            <name>法國巴黎</name>
            <time>19世紀晚期</time>
          </setting>
        </settingDesc>
      </profileDesc>
    </egXML>
  </exemplum>
  <remarks ident="profileDesc-remarks" versionDate="2017-06-25" xml:lang="en">
    <p>Although the content model permits it, it is rarely
meaningful to supply multiple occurrences for any of the child
elements of  <gi>profileDesc</gi> unless these are documenting multiple texts.</p>
  </remarks>
  <remarks ident="profileDesc-remarks" versionDate="2017-06-25" xml:lang="de">
      <p>Obwohl durch das Inhaltsmodell erlaubt, erscheint es in den seltensten Fällen sinnvoll, mehrere Vorkommen der erlaubten Kindelemente der <gi>profileDesc</gi> zu notieren – außer diese beziehen sich auf unterschiedliche Texte.
        </p>
  </remarks>
  <listRef>
    <ptr target="#HD4"/>
    <ptr target="#HD11"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">text-profile description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">description du profil</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">텍스트-개요 기술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文件背景描述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Beschreibung des Textprofils</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción del perfil del texto.</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione del profilo del testo</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides a detailed description of non-bibliographic aspects of a text, specifically the
    languages and sublanguages used, the situation in which it was produced, the participants and
    their setting.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">fournit une description détaillée des aspects
    non bibliographiques du texte, notamment les langues utilisées et leurs variantes, les
    circonstances de sa production, les collaborateurs et leur statut.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">분명하게 언어와 특수 언어가 사용된 텍스트, 텍스트가 생산된 상황, 참여자, 배경에 관한 비서지적
    측면을 상세히 기술한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供文件非書目性方面的細節描述，特別是所使用的語言及次要語言、在何種情況下製作、參與人員及其環境背景。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">書誌情報的ではない詳細な解説を示す。例えば、言語や特殊言語、生成され たときの状況、参加者など。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">enthält eine detaillierte Beschreibung der nicht-bibliografischen Merkmale des Textes, besonders der verwendeten Sprachen und Subsprachen, 
        der Entstehungsbedingungen eines Textes sowie der Beteiligten und deren Umfeld.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona una descripción detallada de los aspectos no
    bibliográficos de un texto, especialmente las lenguas y jergas usadas, la situación en que se
    aparecen, los participantes que intervienen, etc.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce una descrizione dettagliata degli aspetti non
    bibliografici di un testo, in modo particolare le lingue e i linguaggi secondari utilizzati, la
    situazione in cui è stato prodotto il testo, i partecipanti e la relativa ambientazione</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.teiHeaderPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      
        <classRef key="model.profileDescPart" minOccurs="0" maxOccurs="unbounded"/>
      
    
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-profileDesc-egXML-bf">
      <profileDesc>
        <langUsage>
          <language ident="fr">French</language>
        </langUsage>
        <textDesc n="novel">
          <channel mode="w">print; part issues</channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepared"/>
          <purpose type="entertain" degree="high"/>
          <purpose type="inform" degree="medium"/>
        </textDesc>
        <settingDesc>
          <setting>
            <name>Paris, France</name>
            <time>Late 19th century</time>
          </setting>
        </settingDesc>
      </profileDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-profileDesc-egXML-xo">
      <profileDesc>
        <langUsage>
          <language ident="fr">français</language>
        </langUsage>
        <textDesc n="roman">
          <channel mode="w">copie; extraits </channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepare"/>
          <purpose type="distraction" degree="high"/>
          <purpose type="information" degree="medium"/>
        </textDesc>
        <settingDesc>
          <setting>
            <name>Paris, France</name>
            <time>Fin 19e</time>
          </setting>
        </settingDesc>
      </profileDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-profileDesc-egXML-oe">
      <profileDesc>
        <langUsage>
          <language ident="fr">法文</language>
        </langUsage>
        <textDesc n="novel">
          <channel mode="w">出版品；專題輯</channel>
          <constitution type="single"/>
          <derivation type="original"/>
          <domain type="art"/>
          <factuality type="fiction"/>
          <interaction type="none"/>
          <preparedness type="prepared"/>
          <purpose type="entertain" degree="high"/>
          <purpose type="inform" degree="medium"/>
        </textDesc>
        <settingDesc>
          <setting>
            <name>法國巴黎</name>
            <time>19世紀晚期</time>
          </setting>
        </settingDesc>
      </profileDesc>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="profileDesc-remarks" versionDate="2017-06-25" xml:lang="en">
    <p>Although the content model permits it, it is rarely
meaningful to supply multiple occurrences for any of the child
elements of  <gi>profileDesc</gi> unless these are documenting multiple texts.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="profileDesc-remarks" versionDate="2017-06-25" xml:lang="de">
      <p>Obwohl durch das Inhaltsmodell erlaubt, erscheint es in den seltensten Fällen sinnvoll, mehrere Vorkommen der erlaubten Kindelemente der <gi>profileDesc</gi> zu notieren – außer diese beziehen sich auf unterschiedliche Texte.
        </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD4"/>
    <ptr target="#HD11"/>
  </listRef>
```

^b23

