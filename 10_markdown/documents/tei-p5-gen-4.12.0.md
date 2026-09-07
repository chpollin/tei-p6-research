---
type: representation
source-type: document
source: '[[00_sources/tei-p5-gen-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 gen
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/gen.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# gen

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4277. Git blob: `f250f2f45f9c64f646df4765311040e59a8f0b48`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-gen" ident="gen">
  <equiv name="grammaticalGender" uri="http://www.tc37sc4.org"/>
  <gloss versionDate="2005-01-14" xml:lang="en">gender</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">성</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">性別</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">genre</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">género</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">genere</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">identifies the morphological gender of a lexical item, as given in the dictionary.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전에 제시된 어휘항목의 형태론적 성을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">說明字彙項目的性別。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書中の語彙項目にある文法形態素の性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">identifie le genre morphologique d'un élément
			lexical, tel qu'il est donné par le dictionnaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">identifica el género morfológico de un elemento léxico, como viene dado en el diccionario.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">identifica il genere morfologico di un'unità lessicale, secondo la modalità del dizionario.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.morphLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gen-egXML-in">
      <entry>
        <form>
          <orth>pamplemousse</orth>
        </form>
        <gramGrp>
          <pos>noun</pos>
          <gen>masculine</gen>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gen-egXML-he">
      <entry>
        <form>
          <orth>pamplemousse</orth>
        </form>
        <gramGrp>
          <pos>nom</pos>
          <gen>masculin</gen>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gen-egXML-vq">
      <entry>
        <form>
          <orth>pamplemousse</orth>
        </form>
        <gramGrp>
          <pos>名詞</pos>
          <gen>陽性</gen>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
  <remarks ident="gen-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data and phrase-level elements. Typical content
            will be <mentioned>masculine</mentioned>, <mentioned>feminine</mentioned>,
            <mentioned>neuter</mentioned> etc.</p>
    <p>This element is synonymous with <tag>gram type="gender"</tag>.</p>
  </remarks>
  <remarks ident="gen-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient des caractères et des éléments du niveau expression. Le
      contenu type sera : <mentioned>masculin</mentioned>,
      <mentioned>féminin</mentioned>, <mentioned>neutre</mentioned>, etc.</p>
    <p>Cet élément est synonyme de<tag>gram type="gender"</tag>.</p>
  </remarks>
  <remarks ident="gen-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    文字データや句レベルの要素をとるかもしれない。よくあるのは、
      <mentioned>男性</mentioned>、<mentioned>女性</mentioned>、<mentioned>中性</mentioned>など。
    </p>
    <p>
    当該要素は、<tag>gram type="gender"</tag>と同義である。
    </p>
  </remarks>
  <listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/equiv[1]`.

```xml
<equiv name="grammaticalGender" uri="http://www.tc37sc4.org"/>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">gender</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">성</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">性別</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">genre</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">género</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">genere</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">identifies the morphological gender of a lexical item, as given in the dictionary.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전에 제시된 어휘항목의 형태론적 성을 표시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明字彙項目的性別。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書中の語彙項目にある文法形態素の性を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">identifie le genre morphologique d'un élément
			lexical, tel qu'il est donné par le dictionnaire.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica el género morfológico de un elemento léxico, como viene dado en el diccionario.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica il genere morfologico di un'unità lessicale, secondo la modalità del dizionario.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.morphLike"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gen-egXML-in">
      <entry>
        <form>
          <orth>pamplemousse</orth>
        </form>
        <gramGrp>
          <pos>noun</pos>
          <gen>masculine</gen>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gen-egXML-he">
      <entry>
        <form>
          <orth>pamplemousse</orth>
        </form>
        <gramGrp>
          <pos>nom</pos>
          <gen>masculin</gen>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-gen-egXML-vq">
      <entry>
        <form>
          <orth>pamplemousse</orth>
        </form>
        <gramGrp>
          <pos>名詞</pos>
          <gen>陽性</gen>
        </gramGrp>
      </entry>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="gen-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data and phrase-level elements. Typical content
            will be <mentioned>masculine</mentioned>, <mentioned>feminine</mentioned>,
            <mentioned>neuter</mentioned> etc.</p>
    <p>This element is synonymous with <tag>gram type="gender"</tag>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="gen-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient des caractères et des éléments du niveau expression. Le
      contenu type sera : <mentioned>masculin</mentioned>,
      <mentioned>féminin</mentioned>, <mentioned>neutre</mentioned>, etc.</p>
    <p>Cet élément est synonyme de<tag>gram type="gender"</tag>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="gen-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    文字データや句レベルの要素をとるかもしれない。よくあるのは、
      <mentioned>男性</mentioned>、<mentioned>女性</mentioned>、<mentioned>中性</mentioned>など。
    </p>
    <p>
    当該要素は、<tag>gram type="gender"</tag>と同義である。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO" type="div2"/>
  </listRef>
```

^b23

