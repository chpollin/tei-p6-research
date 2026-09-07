---
type: representation
source-type: document
source: '[[00_sources/tei-p5-argument-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 argument
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/argument.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# argument

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4017. Git blob: `f9ca8ff84c101fe3a8a9976d1d9cd075c2258ff2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-argument" ident="argument">
  <gloss versionDate="2007-06-12" xml:lang="en">argument</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">argument</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">contains a formal list or prose description of the topics addressed by a subdivision of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 하위 구역에서 서술된 주제에 대한 형식적 목록 또는 산문체 기술</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">規則列表或文字敘述，說明文本分段內容包含的主題。</desc>
  <desc versionDate="2018-12-28" xml:lang="ja">下位部分にあるテキストのトピックを整形のリストまたは散文説明を含む。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">liste formelle ou description en texte libre des sujets traités dans une subdivision d’un texte.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">beinhaltet eine systematische Aufzählung oder eine Prosabeschreibung der Themen, die in einem Unterabschnitt des Textes behandelt werden.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">lista formal o descripción de los argumentos contenidos en una sección de texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">lista formale o descrizione degli argomenti contenuti in una sezione di testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.global"/>
        <classRef key="model.headLike"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.common"/>
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-argument-egXML-rv" source="#beagle">
      <argument>
        <p>Monte Video — Maldonado — Excursion
to R Polanco — Lazo and Bolas — Partridges —
Absence of Trees — Deer — Capybara, or River Hog —
Tucutuco — Molothrus, cuckoo-like habits — Tyrant
Flycatcher — Mocking-bird — Carrion Hawks —
Tubes formed by Lightning — House struck</p>
      </argument>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-argument-egXML-ww" source="#fr-ex-Gide-Journ_fx">
      <argument>
        <p>28 janvier. J’ai le plus grand mal à me réatteler aux Faux-Monnayeurs — La  Bastide. Fin mars. Besoin de couper mon travail. — Cuverville . Fin mai. Mise au net et       dactylographie de cinq chapitres des Faux-Monnayeurs. — 8 juin. Achevé les Faux- Monnayeurs. — 14 juillet. Départ pour le Congo. </p>
      </argument>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-argument-egXML-zf" source="#biblzh-tw_n49">
      <argument>
        <p>自我與他者的關係— 個體感性存在—共有性—交流性—同時性— 責任感/回應性—亦此亦彼—你中有我、我中有你—同時共存——非非此即彼—非你死我活—視域剩餘—外在性—超在性</p>
      </argument>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DSDTB"/>
    <ptr target="#DSTITL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">argument</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">argument</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains a formal list or prose description of the topics addressed by a subdivision of a text.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 하위 구역에서 서술된 주제에 대한 형식적 목록 또는 산문체 기술</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">規則列表或文字敘述，說明文本分段內容包含的主題。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">下位部分にあるテキストのトピックを整形のリストまたは散文説明を含む。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">liste formelle ou description en texte libre des sujets traités dans une subdivision d’un texte.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">beinhaltet eine systematische Aufzählung oder eine Prosabeschreibung der Themen, die in einem Unterabschnitt des Textes behandelt werden.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">lista formal o descripción de los argumentos contenidos en una sección de texto.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">lista formale o descrizione degli argomenti contenuti in una sezione di testo.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.global"/>
        <classRef key="model.headLike"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.common"/>
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-argument-egXML-rv" source="#beagle">
      <argument>
        <p>Monte Video — Maldonado — Excursion
to R Polanco — Lazo and Bolas — Partridges —
Absence of Trees — Deer — Capybara, or River Hog —
Tucutuco — Molothrus, cuckoo-like habits — Tyrant
Flycatcher — Mocking-bird — Carrion Hawks —
Tubes formed by Lightning — House struck</p>
      </argument>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-argument-egXML-ww" source="#fr-ex-Gide-Journ_fx">
      <argument>
        <p>28 janvier. J’ai le plus grand mal à me réatteler aux Faux-Monnayeurs — La  Bastide. Fin mars. Besoin de couper mon travail. — Cuverville . Fin mai. Mise au net et       dactylographie de cinq chapitres des Faux-Monnayeurs. — 8 juin. Achevé les Faux- Monnayeurs. — 14 juillet. Départ pour le Congo. </p>
      </argument>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-argument-egXML-zf" source="#biblzh-tw_n49">
      <argument>
        <p>自我與他者的關係— 個體感性存在—共有性—交流性—同時性— 責任感/回應性—亦此亦彼—你中有我、我中有你—同時共存——非非此即彼—非你死我活—視域剩餘—外在性—超在性</p>
      </argument>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSDTB"/>
    <ptr target="#DSTITL"/>
  </listRef>
```

^b16

