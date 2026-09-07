---
type: representation
source-type: document
source: '[[00_sources/tei-p5-textdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 textDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/textDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# textDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4672. Git blob: `d59bdd287806138afe81b76be1a7a97f7d9723f6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="corpus" xml:id="gi-textDesc" ident="textDesc">
  <gloss versionDate="2005-01-14" xml:lang="en">text description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">文本描述</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description de texte</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción del texto</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione del testo</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">provides a description of a text in terms of its
situational parameters.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">장면적 매개변수를 통해 텍스트에 대해 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供文本在情境特徵方面的相關描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">状況パラメータにより、テキストの情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit la description d'un texte sous l'angle du
      contexte situationnel.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona una descripción de un texto en términos de sus parámetros situacionales</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce la descrizione di un testo in termini di paramentri situazionali.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.catDescPart"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.textDescPart" expand="sequence"/>
      <elementRef key="purpose" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <constraintSpec ident="textDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:textDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textDesc-egXML-ix" source="#UND">
      <textDesc n="Informal domestic conversation">
        <channel mode="s">  </channel>
        <constitution type="single">  </constitution>
        <derivation type="original">  </derivation>
        <domain type="domestic">  </domain>
        <factuality type="mixed">  </factuality>
        <interaction type="complete" active="plural" passive="many">  </interaction>
        <preparedness type="spontaneous">  </preparedness>
        <purpose type="entertain" degree="high">  </purpose>
        <purpose type="inform" degree="medium"/>
      </textDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textDesc-egXML-zn" source="#UND">
      <textDesc n="Informal domestic conversation">
        <channel mode="s"> </channel>
        <constitution type="single"> </constitution>
        <derivation type="original"> </derivation>
        <domain type="domestic"> </domain>
        <factuality type="mixed"> </factuality>
        <interaction type="complete" active="plural" passive="many"> </interaction>
        <preparedness type="spontaneous"> </preparedness>
        <purpose type="entertain" degree="high"> </purpose>
        <purpose type="inform" degree="medium"/>
      </textDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textDesc-egXML-jw" source="#UND">
      <textDesc n="非正式的家常談天">
        <channel mode="s"> </channel>
        <constitution type="single"> </constitution>
        <derivation type="original"> </derivation>
        <domain type="domestic"> </domain>
        <factuality type="mixed"> </factuality>
        <interaction type="complete" active="plural" passive="many"> </interaction>
        <preparedness type="spontaneous"> </preparedness>
        <purpose type="entertain" degree="high"> </purpose>
        <purpose type="inform" degree="medium"/>
      </textDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">text description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">텍스트 기술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">文本描述</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description de texte</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción del texto</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione del testo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">provides a description of a text in terms of its
situational parameters.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">장면적 매개변수를 통해 텍스트에 대해 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供文本在情境特徵方面的相關描述。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">状況パラメータにより、テキストの情報を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit la description d'un texte sous l'angle du
      contexte situationnel.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona una descripción de un texto en términos de sus parámetros situacionales</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce la descrizione di un testo in termini di paramentri situazionali.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.catDescPart"/>
    <memberOf key="model.profileDescPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.textDescPart" expand="sequence"/>
      <elementRef key="purpose" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="textDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:textDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textDesc-egXML-ix" source="#UND">
      <textDesc n="Informal domestic conversation">
        <channel mode="s">  </channel>
        <constitution type="single">  </constitution>
        <derivation type="original">  </derivation>
        <domain type="domestic">  </domain>
        <factuality type="mixed">  </factuality>
        <interaction type="complete" active="plural" passive="many">  </interaction>
        <preparedness type="spontaneous">  </preparedness>
        <purpose type="entertain" degree="high">  </purpose>
        <purpose type="inform" degree="medium"/>
      </textDesc>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textDesc-egXML-zn" source="#UND">
      <textDesc n="Informal domestic conversation">
        <channel mode="s"> </channel>
        <constitution type="single"> </constitution>
        <derivation type="original"> </derivation>
        <domain type="domestic"> </domain>
        <factuality type="mixed"> </factuality>
        <interaction type="complete" active="plural" passive="many"> </interaction>
        <preparedness type="spontaneous"> </preparedness>
        <purpose type="entertain" degree="high"> </purpose>
        <purpose type="inform" degree="medium"/>
      </textDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-textDesc-egXML-jw" source="#UND">
      <textDesc n="非正式的家常談天">
        <channel mode="s"> </channel>
        <constitution type="single"> </constitution>
        <derivation type="original"> </derivation>
        <domain type="domestic"> </domain>
        <factuality type="mixed"> </factuality>
        <interaction type="complete" active="plural" passive="many"> </interaction>
        <preparedness type="spontaneous"> </preparedness>
        <purpose type="entertain" degree="high"> </purpose>
        <purpose type="inform" degree="medium"/>
      </textDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
```

^b20

