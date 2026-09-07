---
type: representation
source-type: document
source: '[[00_sources/tei-p5-incident-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 incident
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/incident.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# incident

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3070. Git blob: `ab045217a32a186feaabd31eb7dc11cad83fe1d3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" xml:id="gi-incident" ident="incident">
  <gloss xml:lang="en" versionDate="2009-04-17">incident</gloss>
  <gloss xml:lang="fr" versionDate="2009-04-17">incident</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">marks any phenomenon or occurrence, not necessarily vocalized or
communicative, for example incidental noises or other events affecting
communication.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어 일시적인 소음 또는 의사소통에 영향을 미치는 다른 사건과 같이, 현상 또는 발생이지만 반드시 목소리나 의사소통을 수반하지는 않는다.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">必ずしも言語化またはコミュニケーションには上らない現象や出来事を示す。
  例えば、偶発的な雑音またはコミュニケーションに影響を与える他の事象な
  ど。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">tout phénomène ou événement, non nécessairement
			vocalisé ou destiné à la communication, par exemple des bruits fortuits ou d'autres
			événements affectant la communication.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">cualquier fenómeno o evento no necesariamente vocal o comunicativo, como ruidos accidentales u otros fenómenos que inciden en la comunicación en acto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">qualsiasi fenomeno o evento non necessariamente vocale o comunicativo, come rumori accidentali o altri fenomeni che incidano sulla comunicazione in atto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.spoken"/>
  </classes>
  <content>
    
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-incident-egXML-vf">
      <incident>
        <desc>ceiling collapses</desc>
      </incident>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-incident-egXML-wl">
      <incident>
        <desc>La vitrine s'écroule dans un grand fracas.</desc>
      </incident>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-incident-egXML-co">
      <incident>
        <desc>天花板崩塌</desc>
      </incident>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TSBAVO"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss xml:lang="en" versionDate="2009-04-17">incident</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss xml:lang="fr" versionDate="2009-04-17">incident</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">marks any phenomenon or occurrence, not necessarily vocalized or
communicative, for example incidental noises or other events affecting
communication.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어 일시적인 소음 또는 의사소통에 영향을 미치는 다른 사건과 같이, 현상 또는 발생이지만 반드시 목소리나 의사소통을 수반하지는 않는다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">必ずしも言語化またはコミュニケーションには上らない現象や出来事を示す。
  例えば、偶発的な雑音またはコミュニケーションに影響を与える他の事象な
  ど。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">tout phénomène ou événement, non nécessairement
			vocalisé ou destiné à la communication, par exemple des bruits fortuits ou d'autres
			événements affectant la communication.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">cualquier fenómeno o evento no necesariamente vocal o comunicativo, como ruidos accidentales u otros fenómenos que inciden en la comunicación en acto.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">qualsiasi fenomeno o evento non necessariamente vocale o comunicativo, come rumori accidentali o altri fenomeni che incidano sulla comunicazione in atto.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.spoken"/>
  </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-incident-egXML-vf">
      <incident>
        <desc>ceiling collapses</desc>
      </incident>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-incident-egXML-wl">
      <incident>
        <desc>La vitrine s'écroule dans un grand fracas.</desc>
      </incident>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-incident-egXML-co">
      <incident>
        <desc>天花板崩塌</desc>
      </incident>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TSBAVO"/>
  </listRef>
```

^b14

