---
type: representation
source-type: document
source: '[[00_sources/tei-p5-stress-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 stress
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/stress.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# stress

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2432. Git blob: `98003dabcb7a2966b90befb1b8bfaa314ddc96f2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-stress" ident="stress">
  <gloss versionDate="2007-06-12" xml:lang="en">stress</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">accentuation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the stress pattern for a dictionary headword, if given separately.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">독립적으로 제시된다면, 사전 표제어에 대한 강세 유형을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含個別標明的標題字重音模式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">切り出しが可能であれば、辞書の見出し語のアクセントパタンを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le modèle d’accentuation d'une entrée de
    dictionnaire, s’il est donné à part.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la entonación de un lema del diccionario, si se
    da separadamente.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la marcatura d'accento per un lemma, qualora sia
    fornito separatamente</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.notated"/>
    <memberOf key="model.formPart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stress-egXML-oc">
      <form>
        <orth>alternating current</orth>
        <stress>,....'..</stress>
      </form>
    </egXML>
  </exemplum>
  <remarks ident="stress-remarks" versionDate="2009-04-07" xml:lang="en">
    <p>Usually stress information is included within pronunciation information.</p>
  </remarks>
  <remarks ident="stress-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>En règle générale les informations sur l'accentuation sont comprises dans les informations sur la prononciation.</p>
  </remarks>
  <listRef>
    <ptr target="#DITPFO"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">stress</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">accentuation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the stress pattern for a dictionary headword, if given separately.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">독립적으로 제시된다면, 사전 표제어에 대한 강세 유형을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含個別標明的標題字重音模式。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">切り出しが可能であれば、辞書の見出し語のアクセントパタンを示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le modèle d’accentuation d'une entrée de
    dictionnaire, s’il est donné à part.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la entonación de un lema del diccionario, si se
    da separadamente.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la marcatura d'accento per un lemma, qualora sia
    fornito separatamente</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.notated"/>
    <memberOf key="model.formPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stress-egXML-oc">
      <form>
        <orth>alternating current</orth>
        <stress>,....'..</stress>
      </form>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="stress-remarks" versionDate="2009-04-07" xml:lang="en">
    <p>Usually stress information is included within pronunciation information.</p>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="stress-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>En règle générale les informations sur l'accentuation sont comprises dans les informations sur la prononciation.</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO"/>
  </listRef>
```

^b15

