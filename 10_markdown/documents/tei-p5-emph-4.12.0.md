---
type: representation
source-type: document
source: '[[00_sources/tei-p5-emph-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 emph
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/emph.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# emph

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4254. Git blob: `03210cc2f683e3e547c1e66fd26c74d8568bfaa2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-emph" ident="emph">
  <gloss versionDate="2005-01-14" xml:lang="en">emphasized</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">강조</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">強調</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">mis en valeur</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">enfatizado</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">enfatizzato</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">marks words or phrases which are stressed or emphasized for
        linguistic or rhetorical effect.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">언어적 또는 수사적 효과를 위해 강세가 붙거나 강조된 단어 또는 구를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">為了語言上或修辭上的效果而加重語氣或特別強調的字句。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">言語学的、修辞学的に強調されるべき語句を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">marque des mots ou des expressions qui sont
        accentués ou mis en valeur pour un motif linguistique ou rhétorique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">marca palabras o frases que se destacan o enfatizan por causas lingüísticas o retóricas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">codifica parole o sintagmi che sono messe in risalto o enfatizzate per un effetto linguistico o retorico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.emphLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-yy" source="#NONE">You took the car and did <emph>what</emph>?!!</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-jb" source="#fr-ex-Daudet_lundi">
      <div>
        <p>«Mes amis, dit-il, mes amis, je... je... »</p>
        <p>Mais quelque chose l'étouffait. Il ne pouvait pas achever sa phrase.</p>
        <p> Alors il se tourna vers le tableau, prit un morceau de craie, et, en appuyant de
            toutes ses forces, il écrivit aussi gros qu'il put : </p>
        <p>
          <emph>«vive la France !"»</emph>
        </p>
        <p> Puis il resta là, la tête appuyée au mur, et, sans parler, avec sa main il nous
            faisait signe:</p>
        <p>«C'est fini...allez-vous-en.»</p>
      </div>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-ju">
      <p> Tu sais quoi ? On l'aurait proposé pour <emph>la médaille</emph> ! </p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-bj">昨天晚上你去了<emph>哪裡</emph>?!!</egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-pz" source="#biblzh-tw_n3">
      寶玉含羞央告道：<q>好姐姐，千萬別告訴人。</q>襲人亦含羞笑問道： <q>你夢見什麼故事了？<emph>是那里流出來的那些髒東西？</emph>
         </q>
      </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-ef" source="#COHQHE-eg-11"><q>What it all comes to is this,</q> he said. <q><emph>What
                    does Christopher Robin do in the morning nowadays?</emph></q>
      </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COHQHE"/>
    <ptr target="#COHQH"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">emphasized</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">강조</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">強調</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">mis en valeur</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">enfatizado</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">enfatizzato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks words or phrases which are stressed or emphasized for
        linguistic or rhetorical effect.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">언어적 또는 수사적 효과를 위해 강세가 붙거나 강조된 단어 또는 구를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">為了語言上或修辭上的效果而加重語氣或特別強調的字句。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">言語学的、修辞学的に強調されるべき語句を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">marque des mots ou des expressions qui sont
        accentués ou mis en valeur pour un motif linguistique ou rhétorique.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">marca palabras o frases que se destacan o enfatizan por causas lingüísticas o retóricas.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">codifica parole o sintagmi che sono messe in risalto o enfatizzate per un effetto linguistico o retorico.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.emphLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-yy" source="#NONE">You took the car and did <emph>what</emph>?!!</egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-jb" source="#fr-ex-Daudet_lundi">
      <div>
        <p>«Mes amis, dit-il, mes amis, je... je... »</p>
        <p>Mais quelque chose l'étouffait. Il ne pouvait pas achever sa phrase.</p>
        <p> Alors il se tourna vers le tableau, prit un morceau de craie, et, en appuyant de
            toutes ses forces, il écrivit aussi gros qu'il put : </p>
        <p>
          <emph>«vive la France !"»</emph>
        </p>
        <p> Puis il resta là, la tête appuyée au mur, et, sans parler, avec sa main il nous
            faisait signe:</p>
        <p>«C'est fini...allez-vous-en.»</p>
      </div>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-ju">
      <p> Tu sais quoi ? On l'aurait proposé pour <emph>la médaille</emph> ! </p>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-bj">昨天晚上你去了<emph>哪裡</emph>?!!</egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-pz" source="#biblzh-tw_n3">
      寶玉含羞央告道：<q>好姐姐，千萬別告訴人。</q>襲人亦含羞笑問道： <q>你夢見什麼故事了？<emph>是那里流出來的那些髒東西？</emph>
         </q>
      </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-emph-egXML-ef" source="#COHQHE-eg-11"><q>What it all comes to is this,</q> he said. <q><emph>What
                    does Christopher Robin do in the morning nowadays?</emph></q>
      </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQHE"/>
    <ptr target="#COHQH"/>
  </listRef>
```

^b22

