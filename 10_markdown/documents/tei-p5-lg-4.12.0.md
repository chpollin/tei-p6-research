---
type: representation
source-type: document
source: '[[00_sources/tei-p5-lg-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 lg
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/lg.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# lg

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7511. Git blob: `f32c613290e14aaa3c1b4bcacabbb04fb427b1a5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-lg" ident="lg">
  <gloss versionDate="2005-01-14" xml:lang="en">line group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">시행군</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">行組</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">groupe de vers</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de versos</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">un gruppo di versi</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Gruppe von Vers(zeil)en</gloss>
  <desc versionDate="2012-04-17" xml:lang="en">contains one or more verse lines functioning as a formal unit, e.g. a stanza, refrain, verse paragraph, etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 연, 후렴구, 운문 단락과 같이 형식적 단위로 기능하는 운문 행군을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含形式上視為一組的詩行，例如詩節、疊句、韻文段落等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">形式単位としてある、ある韻文の行をまとまりを示す。例えば、連、リフレ イン、詩節など。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient un groupe de vers fonctionnant comme une unité formelle, par exemple une strophe, un refrain, un paragraphe en vers, etc.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un grupo de versos que funcionan como una unidad formal, p.ej. una estrofa, un refrán, un estribillo, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un gruppo di versi che costituiscono un'unità formale, per esempio una stanza, un refrain, un paragrafo in versi, ecc.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält eine oder mehrere Verse bzw. Verszeilen, die zusammen eine formale Einheit (z. B. Strophe, Refrain) bilden.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.divLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.paraPart"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.divTop"/>
        <classRef key="model.global"/>
      </alternate>      
      <alternate>
        <classRef key="model.lLike"/>
        <classRef key="model.stageLike"/>
        <classRef key="model.labelLike"/>
        <classRef key="model.pPart.transcriptional"/>
        <elementRef key="lg"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.lLike"/>
        <classRef key="model.stageLike"/>
        <classRef key="model.labelLike"/>
        <classRef key="model.pPart.transcriptional"/>
        <classRef key="model.global"/>
        <elementRef key="lg"/>
      </alternate>
      <sequence minOccurs="0" maxOccurs="unbounded">        
        <classRef key="model.divBottom"/>
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
  <constraintSpec scheme="schematron" ident="atleast1oflggapl" xml:lang="en">
    <constraint>
      <sch:rule context="tei:lg">
        <sch:assert test="count(descendant::tei:lg|descendant::tei:l|descendant::tei:gap) &gt; 0">An &lt;lg> element must contain at least one child &lt;l>, &lt;lg>, or &lt;gap> element.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="abstractModel-structure-lg-in-l" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:lg">
        <sch:report test="ancestor::tei:l[not(.//tei:note//tei:lg[. = current()])]">Abstract model violation: Lines may not contain line groups.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lg-egXML-bk" source="#CREELEY">
      <lg type="free">
        <l>Let me be my own fool</l>
        <l>of my own making, the sum of it</l>
      </lg>
      <lg type="free">
        <l>is equivocal.</l>
        <l>One says of the drunken farmer:</l>
      </lg>
      <lg type="free">
        <l>leave him lay off it. And this is</l>
        <l>the explanation.</l>
      </lg>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lg-egXML-yb" source="#fr-ex-Baudelaire-chats">
      <div type="sonnet">
        <lg type="quatrain">
          <l>Les amoureux fervents et les savants austères</l>
          <l>Aiment également, dans leur mûre saison,</l>
          <l>Les chats puissants et doux, orgueil de la maison,</l>
          <l>Qui comme eux sont frileux et comme eux sédentaires.</l>
        </lg>
        <lg type="quatrain">
          <l>Amis de la science et de la volupté</l>
          <l>Ils cherchent le silence et l'horreur des ténèbres ;</l>
          <l>L'Erèbe les eût pris pour ses coursiers funèbres,</l>
          <l>S'ils pouvaient au servage incliner leur fierté.</l>
        </lg>
        <lg type="tercet">
          <l>Ils prennent en songeant les nobles attitudes</l>
          <l>Des grands sphinx allongés au fond des solitudes,</l>
          <l>Qui semblent s'endormir dans un rêve sans fin ;</l>
        </lg>
        <lg type="tercet">
          <l>Leurs reins féconds sont pleins d'étincelles magiques,</l>
          <l>Et des parcelles d'or, ainsi qu'un sable fin,</l>
          <l>Etoilent vaguement leurs prunelles mystiques.</l>
        </lg>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lg-egXML-qu" source="#biblzh-tw_n10">
      <lg type="free">
        <l>把你的影子加點鹽</l>
        <l>醃起來</l>
        <l>風乾</l>
      </lg>
      <lg type="free">
        <l>老的時候</l>
        <l>下酒</l>
      </lg>
    </egXML>
  </exemplum>
  <remarks ident="lg-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">contains verse lines or nested line groups only, possibly prefixed by a heading.</p>
  </remarks>
  <remarks ident="lg-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">ne contient que des vers ou des groupes de vers enchâssés, éventuellement précédés d'un titre.</p>
  </remarks>
  <remarks ident="lg-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 韻文の行または(普通は見出しが付く)入れ子化された行グループのみを示 す。 </p>
  </remarks>
  <remarks ident="lg-remarks" versionDate="2017-06-13" xml:lang="de">
    <p rend="dataDesc">enthält lediglich Vers(zeil)en (<gi>l</gi>) oder verschachtelte Gruppen von Vers(zeil)en
      (<gi>lg</gi>); eine Überschrift ist fakultativ.</p>
  </remarks>
  <listRef>
    <ptr target="#COVE"/>
    <ptr target="#CODV"/>
    <ptr target="#DRPAL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">line group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">시행군</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">行組</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">groupe de vers</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de versos</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">un gruppo di versi</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Gruppe von Vers(zeil)en</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-04-17" xml:lang="en">contains one or more verse lines functioning as a formal unit, e.g. a stanza, refrain, verse paragraph, etc.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 연, 후렴구, 운문 단락과 같이 형식적 단위로 기능하는 운문 행군을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含形式上視為一組的詩行，例如詩節、疊句、韻文段落等。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">形式単位としてある、ある韻文の行をまとまりを示す。例えば、連、リフレ イン、詩節など。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient un groupe de vers fonctionnant comme une unité formelle, par exemple une strophe, un refrain, un paragraphe en vers, etc.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un grupo de versos que funcionan como una unidad formal, p.ej. una estrofa, un refrán, un estribillo, etc.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un gruppo di versi che costituiscono un'unità formale, per esempio una stanza, un refrain, un paragrafo in versi, ecc.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält eine oder mehrere Verse bzw. Verszeilen, die zusammen eine formale Einheit (z. B. Strophe, Refrain) bilden.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.divLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divPart"/>
    <memberOf key="model.paraPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.divTop"/>
        <classRef key="model.global"/>
      </alternate>      
      <alternate>
        <classRef key="model.lLike"/>
        <classRef key="model.stageLike"/>
        <classRef key="model.labelLike"/>
        <classRef key="model.pPart.transcriptional"/>
        <elementRef key="lg"/>
      </alternate>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.lLike"/>
        <classRef key="model.stageLike"/>
        <classRef key="model.labelLike"/>
        <classRef key="model.pPart.transcriptional"/>
        <classRef key="model.global"/>
        <elementRef key="lg"/>
      </alternate>
      <sequence minOccurs="0" maxOccurs="unbounded">        
        <classRef key="model.divBottom"/>
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="atleast1oflggapl" xml:lang="en">
    <constraint>
      <sch:rule context="tei:lg">
        <sch:assert test="count(descendant::tei:lg|descendant::tei:l|descendant::tei:gap) &gt; 0">An &lt;lg> element must contain at least one child &lt;l>, &lt;lg>, or &lt;gap> element.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="abstractModel-structure-lg-in-l" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:lg">
        <sch:report test="ancestor::tei:l[not(.//tei:note//tei:lg[. = current()])]">Abstract model violation: Lines may not contain line groups.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lg-egXML-bk" source="#CREELEY">
      <lg type="free">
        <l>Let me be my own fool</l>
        <l>of my own making, the sum of it</l>
      </lg>
      <lg type="free">
        <l>is equivocal.</l>
        <l>One says of the drunken farmer:</l>
      </lg>
      <lg type="free">
        <l>leave him lay off it. And this is</l>
        <l>the explanation.</l>
      </lg>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lg-egXML-yb" source="#fr-ex-Baudelaire-chats">
      <div type="sonnet">
        <lg type="quatrain">
          <l>Les amoureux fervents et les savants austères</l>
          <l>Aiment également, dans leur mûre saison,</l>
          <l>Les chats puissants et doux, orgueil de la maison,</l>
          <l>Qui comme eux sont frileux et comme eux sédentaires.</l>
        </lg>
        <lg type="quatrain">
          <l>Amis de la science et de la volupté</l>
          <l>Ils cherchent le silence et l'horreur des ténèbres ;</l>
          <l>L'Erèbe les eût pris pour ses coursiers funèbres,</l>
          <l>S'ils pouvaient au servage incliner leur fierté.</l>
        </lg>
        <lg type="tercet">
          <l>Ils prennent en songeant les nobles attitudes</l>
          <l>Des grands sphinx allongés au fond des solitudes,</l>
          <l>Qui semblent s'endormir dans un rêve sans fin ;</l>
        </lg>
        <lg type="tercet">
          <l>Leurs reins féconds sont pleins d'étincelles magiques,</l>
          <l>Et des parcelles d'or, ainsi qu'un sable fin,</l>
          <l>Etoilent vaguement leurs prunelles mystiques.</l>
        </lg>
      </div>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lg-egXML-qu" source="#biblzh-tw_n10">
      <lg type="free">
        <l>把你的影子加點鹽</l>
        <l>醃起來</l>
        <l>風乾</l>
      </lg>
      <lg type="free">
        <l>老的時候</l>
        <l>下酒</l>
      </lg>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="lg-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">contains verse lines or nested line groups only, possibly prefixed by a heading.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="lg-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">ne contient que des vers ou des groupes de vers enchâssés, éventuellement précédés d'un titre.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="lg-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 韻文の行または(普通は見出しが付く)入れ子化された行グループのみを示 す。 </p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="lg-remarks" versionDate="2017-06-13" xml:lang="de">
    <p rend="dataDesc">enthält lediglich Vers(zeil)en (<gi>l</gi>) oder verschachtelte Gruppen von Vers(zeil)en
      (<gi>lg</gi>); eine Überschrift ist fakultativ.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COVE"/>
    <ptr target="#CODV"/>
    <ptr target="#DRPAL"/>
  </listRef>
```

^b27

