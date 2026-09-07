---
type: representation
source-type: document
source: '[[00_sources/tei-p5-vocal-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 vocal
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/vocal.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# vocal

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4794. Git blob: `8985663c058697444d9e906601a48149792fb90b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" xml:id="gi-vocal" ident="vocal">
  <gloss versionDate="2009-04-17" xml:lang="en">vocal</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">élément vocal</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">marks any vocalized but not necessarily lexical phenomenon, for
  example voiced pauses, non-lexical backchannels, etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어 목소리가 담긴 휴지, 비어휘적 비정규적 경로 등과 같이 목소리는 나지만 어휘적 현상은 아닌 것.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">發出聲音但未必是詞彙的話語，例如有聲的停頓、非詞彙的附應等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">音声化されているが、必ずしも単語化される必要はない現象を示す。例えば、
  有声の間、単語化されない相づち、など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">tout phénomène vocalisé mais pas nécessairement
			lexical, par exemple des pauses vocales, des réactions non lexicales, etc.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">cualquier fenómeno vocal pero no necesariamente verbal, como pausa plena, backchannel no verbales, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">qualsiasi fenomeno vocale ma non necessariamente verbale, come pause piene, backchannel non verbali, ecc.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.spoken"/>
  </classes>
  <content>
    
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
  <attList>
    <attDef ident="iterated" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether or not the phenomenon is repeated.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">반복 현상 여부를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該現象是否重複發生。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該現象は繰り返されるものかどうかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si le phénomène est ou non
					répété.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el fenómeno es eventual o si se repite.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'eventuale ripetizione del fenomeno.</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <defaultVal>false</defaultVal>
      <remarks ident="vocal-attr.iterated-remarks" versionDate="2007-10-06" xml:lang="en">
        <p>The value <val>true</val> indicates that the vocal effect
	is repeated several times rather than just occurring once.</p>
      </remarks>
      <remarks ident="vocal-attr.iterated-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> signale que l'effet vocal est répété plutôt
                        qu'unique. </p>
      </remarks>
      <remarks ident="vocal-attr.iterated-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        値<val>true</val>は、音声が複数回繰り返されることを示す。
        </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vocal-egXML-ca">
      <vocal dur="PT12S">
        <desc>whistles</desc>
      </vocal>
      <vocal iterated="true">
        <desc>whistles intermittently</desc>
      </vocal>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vocal-egXML-au">
      <vocal dur="PT12S">
        <desc>sifflements</desc>
      </vocal>
      <vocal iterated="true">
        <desc>sifflements intermittents</desc>
      </vocal>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vocal-egXML-su">
      <vocal dur="PT12S">
        <desc>吹口哨</desc>
      </vocal>
      <vocal iterated="true">
        <desc>斷斷續續地吹口哨</desc>
      </vocal>
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
<gloss versionDate="2009-04-17" xml:lang="en">vocal</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">élément vocal</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">marks any vocalized but not necessarily lexical phenomenon, for
  example voiced pauses, non-lexical backchannels, etc.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어 목소리가 담긴 휴지, 비어휘적 비정규적 경로 등과 같이 목소리는 나지만 어휘적 현상은 아닌 것.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">發出聲音但未必是詞彙的話語，例如有聲的停頓、非詞彙的附應等。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">音声化されているが、必ずしも単語化される必要はない現象を示す。例えば、
  有声の間、単語化されない相づち、など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">tout phénomène vocalisé mais pas nécessairement
			lexical, par exemple des pauses vocales, des réactions non lexicales, etc.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">cualquier fenómeno vocal pero no necesariamente verbal, como pausa plena, backchannel no verbales, etc.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">qualsiasi fenomeno vocale ma non necessariamente verbale, come pause piene, backchannel non verbali, ecc.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.spoken"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether or not the phenomenon is repeated.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">반복 현상 여부를 나타낸다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該現象是否重複發生。</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該現象は繰り返されるものかどうかを示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si le phénomène est ou non
					répété.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el fenómeno es eventual o si se repite.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'eventuale ripetizione del fenomeno.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>false</defaultVal>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="vocal-attr.iterated-remarks" versionDate="2007-10-06" xml:lang="en">
        <p>The value <val>true</val> indicates that the vocal effect
	is repeated several times rather than just occurring once.</p>
      </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="vocal-attr.iterated-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> signale que l'effet vocal est répété plutôt
                        qu'unique. </p>
      </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="vocal-attr.iterated-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        値<val>true</val>は、音声が複数回繰り返されることを示す。
        </p>
      </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vocal-egXML-ca">
      <vocal dur="PT12S">
        <desc>whistles</desc>
      </vocal>
      <vocal iterated="true">
        <desc>whistles intermittently</desc>
      </vocal>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vocal-egXML-au">
      <vocal dur="PT12S">
        <desc>sifflements</desc>
      </vocal>
      <vocal iterated="true">
        <desc>sifflements intermittents</desc>
      </vocal>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vocal-egXML-su">
      <vocal dur="PT12S">
        <desc>吹口哨</desc>
      </vocal>
      <vocal iterated="true">
        <desc>斷斷續續地吹口哨</desc>
      </vocal>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TSBAVO"/>
  </listRef>
```

^b27

