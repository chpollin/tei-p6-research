---
type: representation
source-type: document
source: '[[00_sources/tei-p5-gloss-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 gloss
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/gloss.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# gloss

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4240. Git blob: `593c91eb0c6046c40392480add08029125b29347`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-gloss" ident="gloss">
  <gloss versionDate="2009-01-06" xml:lang="en">gloss</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">glose</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">identifies a phrase or word used to provide a gloss or definition for some other word or
    phrase.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">다른 단어나 구에 대한 해설 또는 정의를 제공할 때 사용되는 구나 단어를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明用來為另一個字詞下定義或提供註解的字詞。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">語句の説明や定義を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">identifie une expression ou un mot utilisé pour fournir
    une glose ou une définition à quelque autre mot ou expression.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">identifica una locución o palabra usada para proporcionar
    una glosa o definición sobre otra palabra o frase.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">identifica un sintagma o una parola che fornisce una
    glossa o definizione per qualche altra parola o sintagma.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cReferencing"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.translatable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.emphLike"/>
    <memberOf key="model.identEquiv"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gloss-egXML-oo" source="#COHTG-eg-42">We may define <term xml:id="tdpv" rend="sc">discoursal point of view</term> as <gloss target="#tdpv">the relationship, expressed
        through discourse structure, between the implied author or some other addresser, and the
        fiction.</gloss>
      </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gloss-egXML-iw" source="#fr-ex-Dubois_Dict_Ling"> Les<term>
          embrayeurs</term> sont <gloss>une classe de mots dont le sens varie avec la situation; ces
          mots, n'ayant pas de référence propre dans la langue, ne reçoivent un référent que
          lorsqu'ils sont inclus dans un message.</gloss>
      </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gloss-egXML-hu" source="#biblzh-tw_n4"> 我們可以定義 <term xml:id="zh-tw_tdpv" rend="sc">戀母情結</term> 為 <gloss target="#zh-tw_tdpv">佛洛伊德心理分析理論中的重要觀念，指三至六歲大的男孩在性慾上有一種戀母情結的階段，這情結更進一步發展成對父親的忌妒仇視，甚至亟欲除之而後快。</gloss>
      </egXML>
  </exemplum>
  <remarks ident="gloss-remarks" versionDate="2005-10-13" xml:lang="en">
    <p>The <att>target</att> and <att>cRef</att> attributes are mutually exclusive.</p>
  </remarks>
  <remarks ident="gloss-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les attributs <att>target</att> et <att>cRef</att> sont exclusifs l'un de l'autre.</p>
  </remarks>
  <remarks ident="gloss-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los atributos <att>blanco</att> y <att>cRef</att> son mutuamente exclusivos.</p>
  </remarks>
  <remarks ident="gloss-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>target</att>と<att>cRef</att>は、排他的に使用される。 </p>
  </remarks>
  <listRef>
    <ptr target="#COHTG"/>
    <ptr target="#TDcrystalsCEdc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="en">gloss</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">glose</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">identifies a phrase or word used to provide a gloss or definition for some other word or
    phrase.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다른 단어나 구에 대한 해설 또는 정의를 제공할 때 사용되는 구나 단어를 표시한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明用來為另一個字詞下定義或提供註解的字詞。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">語句の説明や定義を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">identifie une expression ou un mot utilisé pour fournir
    une glose ou une définition à quelque autre mot ou expression.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica una locución o palabra usada para proporcionar
    una glosa o definición sobre otra palabra o frase.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica un sintagma o una parola che fornisce una
    glossa o definizione per qualche altra parola o sintagma.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cReferencing"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.translatable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.emphLike"/>
    <memberOf key="model.identEquiv"/>
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
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gloss-egXML-oo" source="#COHTG-eg-42">We may define <term xml:id="tdpv" rend="sc">discoursal point of view</term> as <gloss target="#tdpv">the relationship, expressed
        through discourse structure, between the implied author or some other addresser, and the
        fiction.</gloss>
      </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gloss-egXML-iw" source="#fr-ex-Dubois_Dict_Ling"> Les<term>
          embrayeurs</term> sont <gloss>une classe de mots dont le sens varie avec la situation; ces
          mots, n'ayant pas de référence propre dans la langue, ne reçoivent un référent que
          lorsqu'ils sont inclus dans un message.</gloss>
      </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gloss-egXML-hu" source="#biblzh-tw_n4"> 我們可以定義 <term xml:id="zh-tw_tdpv" rend="sc">戀母情結</term> 為 <gloss target="#zh-tw_tdpv">佛洛伊德心理分析理論中的重要觀念，指三至六歲大的男孩在性慾上有一種戀母情結的階段，這情結更進一步發展成對父親的忌妒仇視，甚至亟欲除之而後快。</gloss>
      </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="gloss-remarks" versionDate="2005-10-13" xml:lang="en">
    <p>The <att>target</att> and <att>cRef</att> attributes are mutually exclusive.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="gloss-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les attributs <att>target</att> et <att>cRef</att> sont exclusifs l'un de l'autre.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="gloss-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Los atributos <att>blanco</att> y <att>cRef</att> son mutuamente exclusivos.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="gloss-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>target</att>と<att>cRef</att>は、排他的に使用される。 </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHTG"/>
    <ptr target="#TDcrystalsCEdc"/>
  </listRef>
```

^b19

