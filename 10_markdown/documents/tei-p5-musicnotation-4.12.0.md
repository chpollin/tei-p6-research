---
type: representation
source-type: document
source: '[[00_sources/tei-p5-musicnotation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 musicNotation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/musicNotation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# musicNotation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3455. Git blob: `1c4da93df2a0521ccbdbe4f44b6f5f321741d240`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="MUSICNOTATION" ident="musicNotation">
  <gloss versionDate="2020-12-20" xml:lang="en">music notation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">notation musicale</gloss>
  <desc versionDate="2005-01-14" xml:lang="en" xml:id="music.desc">contains description of type of musical notation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">악보 표기 유형 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含樂譜種類的描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">記譜法の種類を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description d'un type de notation
      musicale.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la descripción de un tipo de anotación musical.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione del tipo di annotazione musicale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-lx">
      <musicNotation>
        <p>Square notation of 4-line red staves.</p>
      </musicNotation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-rl" source="#fr-ex-Danhauser">
      <musicNotation>
        <p>Les clés se placent au commencement de la portée. Elles servent à fixer le nom des
            notes et à indiquer en même temps la place que celles-ci occupent dans l'échelle
            musicale.</p>
      </musicNotation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-dj" source="#fr-ex-Dennery-notations">
      <musicNotation>Même, si l'on voulait démontrer que les livres de chants ont été
          <term>neumés</term> dés le IXe siècle, il ne faudrait pas oublier que des livres de chants
          sans <term>neumes</term> ont été écrits jusqu'au Xe siècle. </musicNotation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-xn">
      <musicNotation>
        <p>紅色四線譜記號法</p>
      </musicNotation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-kx">
      <musicNotation>St. Gall式的<term>campo aperto</term>記譜法。</musicNotation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-ns">
      <musicNotation>Neumes in <term>campo aperto</term> of the St. Gall type.
</musicNotation>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">music notation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">notation musicale</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en" xml:id="music.desc">contains description of type of musical notation.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">악보 표기 유형 기술을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含樂譜種類的描述。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">記譜法の種類を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description d'un type de notation
      musicale.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la descripción de un tipo de anotación musical.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione del tipo di annotazione musicale.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-lx">
      <musicNotation>
        <p>Square notation of 4-line red staves.</p>
      </musicNotation>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-rl" source="#fr-ex-Danhauser">
      <musicNotation>
        <p>Les clés se placent au commencement de la portée. Elles servent à fixer le nom des
            notes et à indiquer en même temps la place que celles-ci occupent dans l'échelle
            musicale.</p>
      </musicNotation>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-dj" source="#fr-ex-Dennery-notations">
      <musicNotation>Même, si l'on voulait démontrer que les livres de chants ont été
          <term>neumés</term> dés le IXe siècle, il ne faudrait pas oublier que des livres de chants
          sans <term>neumes</term> ont été écrits jusqu'au Xe siècle. </musicNotation>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-xn">
      <musicNotation>
        <p>紅色四線譜記號法</p>
      </musicNotation>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-kx">
      <musicNotation>St. Gall式的<term>campo aperto</term>記譜法。</musicNotation>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MUSICNOTATION-egXML-ns">
      <musicNotation>Neumes in <term>campo aperto</term> of the St. Gall type.
</musicNotation>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph2"/>
  </listRef>
```

^b18

