---
type: representation
source-type: document
source: '[[00_sources/tei-p5-spgrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 spGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/spGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# spGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5216. Git blob: `22bb28af3d7b06ff37898eb3d6ff90a45398091b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-spGrp" ident="spGrp">
  <gloss versionDate="2011-11-19" xml:lang="en">speech group</gloss>
  <desc versionDate="2026-01-19" xml:lang="en">contains a group of speeches, speech groups, or songs in a performance text presented
  in a source as constituting a single unit or
  <soCalled>number</soCalled>.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.divLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
  </classes>
  <content>
    <sequence>     
        <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <elementRef key="sp"/>
          <elementRef key="spGrp"/>
          <classRef key="model.stageLike"/>
        </alternate>   
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-spGrp-egXML-rc" source="#RphCnd">
      
      <stage>A Page brings a seat, which is placed next to the throne, on its R., Cinderella occupies
        it, the sisters sit on her R. H., and the fête continues. A fanciful dance by appropriate
        characters, followed by a party of Tyrolese singers and dancers, who enter dressed in the
        costume of their nation. While some dance, the others accompany them by their voices
        alone.</stage>

      <spGrp>
        <head>TYROLIENNE.</head>
        <spGrp org="parallel">  
          <sp>
            <speaker>Men.</speaker>
            <l>Whilst to joy we sing inviting,</l>
            <l>With our strains thy steps uniting</l>
            <l>With thy smiles our pains requiting</l>
            <l>Lovely maid, our eyes delight.</l>
          </sp>
          <sp>
            <speaker>Women.</speaker>
            <l>Swift as the flash</l>
            <l>That mocks the sight</l>
            <l>Thou seem'st a bird</l>
            <l>In airy flight.</l>
          </sp>
        </spGrp>
        <sp>
          <speaker>Together.</speaker>
          <l>When, home returning,</l>
          <l>We leave these cool fountains,</l>
          <l>In our native mountains</l>
          <l>Thy praise we'll recite.</l>
        </sp>
        <spGrp org="parallel">  
          <sp>
            <speaker>Men.</speaker>
            <l>Fresh flowers</l>
            <l>Washed by showers</l>
            <l>In Love's bowers,</l>
            <l>Are less fair and bright.</l>
          </sp>
          <sp>
            <speaker>Women.</speaker>
            <l>Thy steps so light,</l>
            <l>Our songs invite;</l>
            <l>Come, fairy sprite,</l>
            <l>Our eyes delight.</l>
          </sp></spGrp>
        <sp>
          <speaker>Together.</speaker>
          <l>When, home returning,</l>
          <l>We leave these cool fountains,</l>
          <l>In our native mountains</l>
          <l>Thy praise we'll recite.</l>
        </sp>
      </spGrp>     
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-spGrp-egXML-lm" source="#MasCab">
      <sp>
        <speaker>FRAULEIN SCHNEIDER:</speaker>
        <p>Herr Schultz! Can I believe what I see? <stage>(HERR SCHULTZ nods 
proudly)</stage> But this is — too much to accept. So rare — so costly —
so luxurious.</p>
      </sp>
      <stage>(She sings)</stage>
      <spGrp n="4">
        <sp>
          <l>If you bought me diamonds, If you bought me pearls,</l>
          <l>If you bought me roses like some other gents</l>
          <l>Might bring to other girls,</l>
          <l>It couldn't please me more</l>
          <l>Than the gift I see -</l>
          <stage>(She takes a large pineapple out of the bag)</stage>
          <l>A pineapple for me!</l>
        </sp>
        <sp>
          <speaker>SCHULTZ:</speaker>
          <stage>(Singing)</stage>
          <l>If, in your emotion,</l>
          <l>You began to sway,</l>
          <l>Went to get some air,</l>
          <l>Or grabbed a chair</l>
          <l>To keep from fainting dead away,</l>
          <l>It couldn't please me more</l>
          <l>Than to see you cling</l>
          <l>To the pineapple I bring.</l>
        </sp>
        <sp>
          <speaker>
BOTH:</speaker>
          <l>Ah, ah, ah, ah, ah, ah, ah, ah</l>
        </sp>
        <!-- ... -->
        <stage>(They dance)</stage>
      </spGrp>
      <sp>
        <speaker>FRAULEIN SCHNEIDER:</speaker>
        <p>But you must not bring me
any more pineapples! Do you hear? It is not proper.  It is a gift a
young man would present to his lady love. It makes me blush!
</p>
      </sp>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DRSPG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2011-11-19" xml:lang="en">speech group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2026-01-19" xml:lang="en">contains a group of speeches, speech groups, or songs in a performance text presented
  in a source as constituting a single unit or
  <soCalled>number</soCalled>.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.divLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>     
        <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <classRef key="model.global"/>
          <elementRef key="sp"/>
          <elementRef key="spGrp"/>
          <classRef key="model.stageLike"/>
        </alternate>   
    </sequence>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-spGrp-egXML-rc" source="#RphCnd">
      
      <stage>A Page brings a seat, which is placed next to the throne, on its R., Cinderella occupies
        it, the sisters sit on her R. H., and the fête continues. A fanciful dance by appropriate
        characters, followed by a party of Tyrolese singers and dancers, who enter dressed in the
        costume of their nation. While some dance, the others accompany them by their voices
        alone.</stage>

      <spGrp>
        <head>TYROLIENNE.</head>
        <spGrp org="parallel">  
          <sp>
            <speaker>Men.</speaker>
            <l>Whilst to joy we sing inviting,</l>
            <l>With our strains thy steps uniting</l>
            <l>With thy smiles our pains requiting</l>
            <l>Lovely maid, our eyes delight.</l>
          </sp>
          <sp>
            <speaker>Women.</speaker>
            <l>Swift as the flash</l>
            <l>That mocks the sight</l>
            <l>Thou seem'st a bird</l>
            <l>In airy flight.</l>
          </sp>
        </spGrp>
        <sp>
          <speaker>Together.</speaker>
          <l>When, home returning,</l>
          <l>We leave these cool fountains,</l>
          <l>In our native mountains</l>
          <l>Thy praise we'll recite.</l>
        </sp>
        <spGrp org="parallel">  
          <sp>
            <speaker>Men.</speaker>
            <l>Fresh flowers</l>
            <l>Washed by showers</l>
            <l>In Love's bowers,</l>
            <l>Are less fair and bright.</l>
          </sp>
          <sp>
            <speaker>Women.</speaker>
            <l>Thy steps so light,</l>
            <l>Our songs invite;</l>
            <l>Come, fairy sprite,</l>
            <l>Our eyes delight.</l>
          </sp></spGrp>
        <sp>
          <speaker>Together.</speaker>
          <l>When, home returning,</l>
          <l>We leave these cool fountains,</l>
          <l>In our native mountains</l>
          <l>Thy praise we'll recite.</l>
        </sp>
      </spGrp>     
    </egXML>
  </exemplum>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-spGrp-egXML-lm" source="#MasCab">
      <sp>
        <speaker>FRAULEIN SCHNEIDER:</speaker>
        <p>Herr Schultz! Can I believe what I see? <stage>(HERR SCHULTZ nods 
proudly)</stage> But this is — too much to accept. So rare — so costly —
so luxurious.</p>
      </sp>
      <stage>(She sings)</stage>
      <spGrp n="4">
        <sp>
          <l>If you bought me diamonds, If you bought me pearls,</l>
          <l>If you bought me roses like some other gents</l>
          <l>Might bring to other girls,</l>
          <l>It couldn't please me more</l>
          <l>Than the gift I see -</l>
          <stage>(She takes a large pineapple out of the bag)</stage>
          <l>A pineapple for me!</l>
        </sp>
        <sp>
          <speaker>SCHULTZ:</speaker>
          <stage>(Singing)</stage>
          <l>If, in your emotion,</l>
          <l>You began to sway,</l>
          <l>Went to get some air,</l>
          <l>Or grabbed a chair</l>
          <l>To keep from fainting dead away,</l>
          <l>It couldn't please me more</l>
          <l>Than to see you cling</l>
          <l>To the pineapple I bring.</l>
        </sp>
        <sp>
          <speaker>
BOTH:</speaker>
          <l>Ah, ah, ah, ah, ah, ah, ah, ah</l>
        </sp>
        <!-- ... -->
        <stage>(They dance)</stage>
      </spGrp>
      <sp>
        <speaker>FRAULEIN SCHNEIDER:</speaker>
        <p>But you must not bring me
any more pineapples! Do you hear? It is not proper.  It is a gift a
young man would present to his lady love. It makes me blush!
</p>
      </sp>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRSPG"/>
  </listRef>
```

^b7

