---
type: representation
source-type: document
source: '[[00_sources/tei-p5-prologue-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 prologue
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/prologue.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# prologue

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5458. Git blob: `0e20682355fc1ea8e9b0f8c01bb8f6a43089512c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-prologue" ident="prologue">
  <gloss versionDate="2007-06-12" xml:lang="en">prologue</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">prologue</gloss>
  <gloss versionDate="2023-08-08" xml:lang="de">Prolog</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the prologue to a drama, typically spoken by an actor out of character, possibly in
    association with a particular performance or venue.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전형적으로 등장인물들 중 하나가 말하는, 때로는 특정 공연 또는 행위의 현장과 관련된, 드라마의
    개막사.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含戲劇開場白，可能和特定演出或故事場景相關，一般是由一個演員脫離劇中身份來朗讀。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene el prólogo a un drama, pronunciado normalmente
    por un actor a parte del reparto, posiblemente asociado a una puesta en escena determinada.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">舞台における前口上を示す。例えば、配役以外の人物により発話されるもの。 特定の演技や開催地と関連することもある。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient le prologue d’une pièce de théâtre, généralement
    récité par un acteur hors rôle, éventuellement associé à une représentation ou à un lieu
    particulier.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il prologo ad un'opera teatrale, di solito
    pronunciato da un attore al di fuori del ruolo teatrale, possibilmente inn relazione ad una
    particolare messa in scena o luogo di rappresentazione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.frontPart.drama"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        
          <classRef key="model.common"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <classRef key="model.divBottom"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-prologue-egXML-dm" source="#DRPRO-eg-10">
      <prologue>
        <sp>
          <l>Wits, like physicians never can agree,</l>
          <l>When of a different society.</l>
          <l>New plays are stuffed with wits, and with deboches,</l>
          <l>That crowd and sweat like cits in May-Day coaches.</l>
        </sp>
        <trailer>Written by a person of quality</trailer>
      </prologue>
    </egXML>
    <!-- A. Behn: The Rover (1697) -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-prologue-egXML-dx" source="#fr-ex-Antigone">
      <prologue>
        <head>Prologue</head>
        <sp>
          <speaker>Le Prologue.</speaker>
          <p>Voilà. Ces personnages vont vous jouer l' histoire d' Antigone. Antigone, c' est la
              petite maigre qui est assise là-bas, et qui ne dit rien. Elle regarde droit devant
              elle. Elle pense. Elle pense qu' elle va être Antigone tout à l' heure, qu' elle va
              surgir soudain de la maigre jeune fille noiraude et renfermée que personne ne prenait
              au sérieux dans la famille et se dresser seule en face du monde, seule en face de
              Créon, son oncle, qui est le roi. Elle pense qu' elle va mourir, qu' elle est jeune et
              qu' elle aussi, elle aurait bien aimé vivre. Mais il n' y a rien à faire. Elle s'
              appelle Antigone et il va falloir qu' elle joue son rôle jusqu' au bout... </p>
        </sp>
      </prologue>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-prologue-egXML-qu" source="#biblzh-tw_n35-36">
      <prologue>
        <sp>
          <l>何時姊妹再相逢，雷電轟轟雨蒙蒙？</l>
          <l>且等烽煙靜四陲，敗軍高奏凱歌回。</l>
          <l>半山夕照尚含輝。</l>
          <l>何處相逢？</l>
          <l>在荒原。</l>
          <l>共同去見麥克白。</l>
          <l>我來了，狸貓精。</l>
          <l>癩蛤蟆叫我了。</l>
          <l>來也。</l>
          <l>美即丑惡丑即美，翱翔毒霧妖云里。</l>
        </sp>
        <trailer>三女巫同下</trailer>
      </prologue>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DRPRO" type="div3"/>
    <ptr target="#DRFAB" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">prologue</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">prologue</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2023-08-08" xml:lang="de">Prolog</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the prologue to a drama, typically spoken by an actor out of character, possibly in
    association with a particular performance or venue.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전형적으로 등장인물들 중 하나가 말하는, 때로는 특정 공연 또는 행위의 현장과 관련된, 드라마의
    개막사.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含戲劇開場白，可能和特定演出或故事場景相關，一般是由一個演員脫離劇中身份來朗讀。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene el prólogo a un drama, pronunciado normalmente
    por un actor a parte del reparto, posiblemente asociado a una puesta en escena determinada.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">舞台における前口上を示す。例えば、配役以外の人物により発話されるもの。 特定の演技や開催地と関連することもある。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient le prologue d’une pièce de théâtre, généralement
    récité par un acteur hors rôle, éventuellement associé à une représentation ou à un lieu
    particulier.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il prologo ad un'opera teatrale, di solito
    pronunciato da un attore al di fuori del ruolo teatrale, possibilmente inn relazione ad una
    particolare messa in scena o luogo di rappresentazione.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.frontPart.drama"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        
          <classRef key="model.common"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <classRef key="model.divBottom"/>
        
        
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-prologue-egXML-dm" source="#DRPRO-eg-10">
      <prologue>
        <sp>
          <l>Wits, like physicians never can agree,</l>
          <l>When of a different society.</l>
          <l>New plays are stuffed with wits, and with deboches,</l>
          <l>That crowd and sweat like cits in May-Day coaches.</l>
        </sp>
        <trailer>Written by a person of quality</trailer>
      </prologue>
    </egXML>
    <!-- A. Behn: The Rover (1697) -->
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-prologue-egXML-dx" source="#fr-ex-Antigone">
      <prologue>
        <head>Prologue</head>
        <sp>
          <speaker>Le Prologue.</speaker>
          <p>Voilà. Ces personnages vont vous jouer l' histoire d' Antigone. Antigone, c' est la
              petite maigre qui est assise là-bas, et qui ne dit rien. Elle regarde droit devant
              elle. Elle pense. Elle pense qu' elle va être Antigone tout à l' heure, qu' elle va
              surgir soudain de la maigre jeune fille noiraude et renfermée que personne ne prenait
              au sérieux dans la famille et se dresser seule en face du monde, seule en face de
              Créon, son oncle, qui est le roi. Elle pense qu' elle va mourir, qu' elle est jeune et
              qu' elle aussi, elle aurait bien aimé vivre. Mais il n' y a rien à faire. Elle s'
              appelle Antigone et il va falloir qu' elle joue son rôle jusqu' au bout... </p>
        </sp>
      </prologue>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-prologue-egXML-qu" source="#biblzh-tw_n35-36">
      <prologue>
        <sp>
          <l>何時姊妹再相逢，雷電轟轟雨蒙蒙？</l>
          <l>且等烽煙靜四陲，敗軍高奏凱歌回。</l>
          <l>半山夕照尚含輝。</l>
          <l>何處相逢？</l>
          <l>在荒原。</l>
          <l>共同去見麥克白。</l>
          <l>我來了，狸貓精。</l>
          <l>癩蛤蟆叫我了。</l>
          <l>來也。</l>
          <l>美即丑惡丑即美，翱翔毒霧妖云里。</l>
        </sp>
        <trailer>三女巫同下</trailer>
      </prologue>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRPRO" type="div3"/>
    <ptr target="#DRFAB" type="div3"/>
  </listRef>
```

^b16

