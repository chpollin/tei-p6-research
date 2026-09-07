---
type: representation
source-type: document
source: '[[00_sources/tei-p5-hi-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 hi
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/hi.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# hi

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3890. Git blob: `d0b0087eedc25dc251eb52193b4ad3aeec90eb19`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-hi" ident="hi">
  <gloss versionDate="2005-01-14" xml:lang="en">highlighted</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">강조체</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">顯目標示</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">mis en évidence</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">subrayado</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">evidenziato</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">hervorgehoben</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">marks a word or phrase as graphically distinct from the
        surrounding text, for reasons concerning which no claim is
        made.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 이유인지는 명세하지 않고, 주변 텍스트와 시각적으로 구별된 단어나 구를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標誌其字型外觀上和週遭文字有所區別的字詞，但不指出顯目原因。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">周囲のテキストとは見た目が異なっている語句を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">distingue un mot ou une expression comme
        graphiquement distincte du texte environnant, sans en donner la raison.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">marca una palabra o frase gráficamente diferente del resto del texto que la circunda, por causas sobre las que no se hace ninguna declaracion.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">codifica una parola o sintagma in quanto graficamente distinta dal testo circostante, senza che vengano specificate le ragioni dell'evidenziazione.</desc>
    <desc versionDate="2016-11-24" xml:lang="de">markiert ein Wort oder eine Textpassage, das/die sich grafisch vom umgebenden Text abhebt, ohne dass ein inhaltlicher Grund dafür angegeben wird.</desc>
    
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.hiLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hi-egXML-fu" source="#COHQHE-eg-13"><hi rend="gothic">And this Indenture further witnesseth</hi>
            that the said <hi rend="italic">Walter Shandy</hi>, merchant,
            in consideration of the said intended marriage ...</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hi-egXML-ec" source="#fr-ex-Bataille_Arbre">
      <p>Au fronton, on lit cette inscription : <hi rend="uppercase">attends. Tu verras.</hi> Le
          notaire encore prétend qu' elle ne saurait être antérieure au XVIII siècle, car, sinon, l'
          on eût écrit --<q>tu voiras</q>--. </p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hi-egXML-yi" source="#biblzh-tw_n7">我的先生很可惜是一個<hi rend="italic">外國人</hi>。這樣來稱呼自己的先生不免有<hi rend="bold">排外</hi>的味道，但是因為語文和風俗在各國之間确有大不相同之處，我們的婚姻生活也實在有許多無法共通的地方。...</egXML>
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
<gloss versionDate="2005-01-14" xml:lang="en">highlighted</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">강조체</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">顯目標示</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">mis en évidence</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">subrayado</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">evidenziato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">hervorgehoben</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks a word or phrase as graphically distinct from the
        surrounding text, for reasons concerning which no claim is
        made.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 이유인지는 명세하지 않고, 주변 텍스트와 시각적으로 구별된 단어나 구를 표시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標誌其字型外觀上和週遭文字有所區別的字詞，但不指出顯目原因。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">周囲のテキストとは見た目が異なっている語句を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">distingue un mot ou une expression comme
        graphiquement distincte du texte environnant, sans en donner la raison.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">marca una palabra o frase gráficamente diferente del resto del texto que la circunda, por causas sobre las que no se hace ninguna declaracion.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">codifica una parola o sintagma in quanto graficamente distinta dal testo circostante, senza che vengano specificate le ragioni dell'evidenziazione.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">markiert ein Wort oder eine Textpassage, das/die sich grafisch vom umgebenden Text abhebt, ohne dass ein inhaltlicher Grund dafür angegeben wird.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.hiLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hi-egXML-fu" source="#COHQHE-eg-13"><hi rend="gothic">And this Indenture further witnesseth</hi>
            that the said <hi rend="italic">Walter Shandy</hi>, merchant,
            in consideration of the said intended marriage ...</egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hi-egXML-ec" source="#fr-ex-Bataille_Arbre">
      <p>Au fronton, on lit cette inscription : <hi rend="uppercase">attends. Tu verras.</hi> Le
          notaire encore prétend qu' elle ne saurait être antérieure au XVIII siècle, car, sinon, l'
          on eût écrit --<q>tu voiras</q>--. </p>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hi-egXML-yi" source="#biblzh-tw_n7">我的先生很可惜是一個<hi rend="italic">外國人</hi>。這樣來稱呼自己的先生不免有<hi rend="bold">排外</hi>的味道，但是因為語文和風俗在各國之間确有大不相同之處，我們的婚姻生活也實在有許多無法共通的地方。...</egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQHE"/>
    <ptr target="#COHQH"/>
  </listRef>
```

^b21

