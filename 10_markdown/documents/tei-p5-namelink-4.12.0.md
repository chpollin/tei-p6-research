---
type: representation
source-type: document
source: '[[00_sources/tei-p5-namelink-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 nameLink
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/nameLink.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# nameLink

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3907. Git blob: `b480d445fd6425be4baa424af55c247840c5bf41`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-nameLink" ident="nameLink">
  <gloss versionDate="2005-01-14" xml:lang="en">name link</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">lien entre les composants d'un nom</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a connecting phrase or link used within a name but not regarded as part of it, such as <mentioned>van der</mentioned> or
            <mentioned>of</mentioned>.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><mentioned>van der</mentioned> 또는 <mentioned>of</mentioned>와 같이 이름의 부분으로 간주되지 않는 이름 내의 연결 구 또는 연결을
        포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個名稱中的連結字彙，但不屬於該名稱的一部份，例如 van der 或是 of。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">名前の中で使われているが、その一部としては見られない、関連する句やリ ンクを示す。例えば、<mentioned>van der</mentioned>や
        <mentioned>of</mentioned>など。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient une particule ou une expression exprimant un lien, utilisés dans un nom mais considérés comme
        n'en faisant pas partie, comme <q>van der</q> ou <q>de</q>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un afijo de conexión al interno del nombre no considerado parte del nombre, como p.ej. Van Der,
        o De Las.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un affisso di connessione all'interno del nome non considerato parte del nome, come van der
        oppure of</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persNamePart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-uk">
      <persName>
        <forename>Frederick</forename>
        <nameLink>van der</nameLink>
        <surname>Tronck</surname>
      </persName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-aq">
      <persName>
        <forename>Frederick</forename>
        <nameLink>van der</nameLink>
        <surname>Tronck</surname>
      </persName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-nc">
      <persName>
        <forename>Alfred</forename>
        <nameLink>de</nameLink>
        <surname>Musset</surname>
      </persName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-lp"> 因漢文無姓名連結，故無法提供範例 </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-kg"> 因漢文無姓名連結，故無法提供範例 </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-cm">
      <persName>
        <forename>Alfred</forename>
        <nameLink>de</nameLink>
        <surname>Musset</surname>
      </persName>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPER"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">name link</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">lien entre les composants d'un nom</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a connecting phrase or link used within a name but not regarded as part of it, such as <mentioned>van der</mentioned> or
            <mentioned>of</mentioned>.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><mentioned>van der</mentioned> 또는 <mentioned>of</mentioned>와 같이 이름의 부분으로 간주되지 않는 이름 내의 연결 구 또는 연결을
        포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個名稱中的連結字彙，但不屬於該名稱的一部份，例如 van der 或是 of。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">名前の中で使われているが、その一部としては見られない、関連する句やリ ンクを示す。例えば、<mentioned>van der</mentioned>や
        <mentioned>of</mentioned>など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient une particule ou une expression exprimant un lien, utilisés dans un nom mais considérés comme
        n'en faisant pas partie, comme <q>van der</q> ou <q>de</q>.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un afijo de conexión al interno del nombre no considerado parte del nombre, como p.ej. Van Der,
        o De Las.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un affisso di connessione all'interno del nome non considerato parte del nome, come van der
        oppure of</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persNamePart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-uk">
      <persName>
        <forename>Frederick</forename>
        <nameLink>van der</nameLink>
        <surname>Tronck</surname>
      </persName>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-aq">
      <persName>
        <forename>Frederick</forename>
        <nameLink>van der</nameLink>
        <surname>Tronck</surname>
      </persName>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-nc">
      <persName>
        <forename>Alfred</forename>
        <nameLink>de</nameLink>
        <surname>Musset</surname>
      </persName>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-lp"> 因漢文無姓名連結，故無法提供範例 </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-kg"> 因漢文無姓名連結，故無法提供範例 </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nameLink-egXML-cm">
      <persName>
        <forename>Alfred</forename>
        <nameLink>de</nameLink>
        <surname>Musset</surname>
      </persName>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPER"/>
  </listRef>
```

^b18

