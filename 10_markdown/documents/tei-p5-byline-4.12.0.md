---
type: representation
source-type: document
source: '[[00_sources/tei-p5-byline-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 byline
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/byline.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# byline

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7397. Git blob: `f031c7ddaec2cd4ad50ce65b940c997986ac1b4d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-byline" ident="byline">
  <gloss versionDate="2007-06-12" xml:lang="en">byline</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">mention de responsabilité</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Verfasserzeile</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the primary statement of responsibility given for a work
on its title page or at the head or end of the work.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">제목 페이지 또는 작품의 시작부 또는 종료부에서 작품 책임성에 대한 주요 진술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含作品的主要責任陳述，出現在題名頁或作品開頭或結尾處。</desc>
  <desc versionDate="2023-09-27" xml:lang="ja">タイトルページや作品の冒頭や最後にある、作品の主要な責任表示。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indique la responsabilité principale pour une œuvre donnée sur la page de titre ou au début ou à la fin de l’œuvre.</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält Angaben zur Hauptverantwortlichkeit eines Werks, entweder auf der Titelseite oder am Anfang oder Ende des Werks.</desc>
  <desc versionDate="2021-02-18" xml:lang="es">contiene la declaración principal de responsabilidad de una obra tal y como aparece en su título correspondiente, o al inicio o fin de la obra.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la principale dichiarazione di responsabilità per un'opera così come appare sul corrispondente frontespizio oppure all'inizio o alla fine dell'opera stessa.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <elementRef key="docAuthor"/>
      <classRef key="model.global"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-hc" source="#AI-BIBL-2">
      <byline>Written by a CITIZEN who continued all the
while in London. Never made publick before.</byline>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-fk" source="#fr-ex-Montherlant-Pitie">
      <byline>écrit par Costals sur le feuillet blanc de cette lettre : " cette correspondance n'
          était pour vous qu' un jeu. "</byline>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-pe" source="#fr-ex-Constant-Journal">
      <byline>extraits de Villoison et de Schlegel. Commencé la rédaction du quatrième
        livre.</byline>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-go">
      <byline>Reportage céleste de notre envoyé spécial au paradis</byline>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-wx">
      <dateline>Zagreb :</dateline>
      <byline>de notre envoyé spécial.</byline>
    </egXML>
  </exemplum>
  <exemplum versionDate="2021-02-18" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-tp">
      <byline>Par le docteur <docAuthor>Martin Becanus</docAuthor>, au tome troisiesme de ses
          opuscules</byline>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-pa">
      <byline>由一個倫敦土生土長的市民撰寫，先前未曾出版過。</byline>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-qo">
      <byline>錄自她自己的回憶錄</byline>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-yt">
      <byline>來自華盛頓的政治編輯喬治．瓊斯</byline>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-uw">
      <dateline>重慶:</dateline>
      <byline>外交使節專用</byline>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-ww">
      <byline>源自美國哥倫比亞大學博士<docAuthor>胡適</docAuthor>
         </byline>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-zp">
      <byline>Written from her own MEMORANDUMS</byline>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-gu">
      <byline>By George Jones, Political Editor, in Washington</byline>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-ii" source="#PHILIPOTT">
      <byline>BY
<docAuthor>THOMAS PHILIPOTT,</docAuthor>
Master of Arts,
(Somtimes)
Of Clare-Hall in Cambridge.</byline>
    </egXML>
  </exemplum>
  <remarks ident="byline-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The byline on a title page may include either the name
or a description for the document's author. Where the name is included,
it may optionally be tagged using the <gi>docAuthor</gi> element.</p>
  </remarks>
  <remarks ident="byline-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La mention de reponsabilité sur une page de titre peut inclure, soit le nom, soit la description de
                l'auteur d'un document. Lorsque le nom y est donné, on peut éventuellement l'encoder
                au moyen de l'élément <gi>docAuthor</gi>.</p>
  </remarks>
  <remarks ident="byline-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    タイトルページにある署名欄には、当該文書の作者名や説明があるかもし
    れない。作者名がある場合、要素<gi>docAuthor</gi>を使い符号化しても
    よい。
    </p>
  </remarks>
  <remarks ident="byline-remarks" versionDate="2017-06-13" xml:lang="de">
    <p>Die Verfasserzeile auf einer Titelseite kann entweder den Namen oder die Beschreibung des
      Dokumentautors enthalten. Wenn der Name angegeben wird, kann er optional mit dem
      <gi>docAuthor</gi>-Element ausgezeichnet werden.</p>
  </remarks>
  <listRef>
    <ptr target="#DSOC"/>
    <ptr target="#DSFRONT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">byline</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">mention de responsabilité</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Verfasserzeile</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the primary statement of responsibility given for a work
on its title page or at the head or end of the work.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">제목 페이지 또는 작품의 시작부 또는 종료부에서 작품 책임성에 대한 주요 진술을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含作品的主要責任陳述，出現在題名頁或作品開頭或結尾處。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">タイトルページや作品の冒頭や最後にある、作品の主要な責任表示。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique la responsabilité principale pour une œuvre donnée sur la page de titre ou au début ou à la fin de l’œuvre.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält Angaben zur Hauptverantwortlichkeit eines Werks, entweder auf der Titelseite oder am Anfang oder Ende des Werks.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2021-02-18" xml:lang="es">contiene la declaración principal de responsabilidad de una obra tal y como aparece en su título correspondiente, o al inicio o fin de la obra.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la principale dichiarazione di responsabilità per un'opera così come appare sul corrispondente frontespizio oppure all'inizio o alla fine dell'opera stessa.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.divWrapper"/>
    <memberOf key="model.pLike.front"/>
    <memberOf key="model.titlepagePart"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <classRef key="model.phrase"/>
      <elementRef key="docAuthor"/>
      <classRef key="model.global"/>
    </alternate>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-hc" source="#AI-BIBL-2">
      <byline>Written by a CITIZEN who continued all the
while in London. Never made publick before.</byline>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-fk" source="#fr-ex-Montherlant-Pitie">
      <byline>écrit par Costals sur le feuillet blanc de cette lettre : " cette correspondance n'
          était pour vous qu' un jeu. "</byline>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-pe" source="#fr-ex-Constant-Journal">
      <byline>extraits de Villoison et de Schlegel. Commencé la rédaction du quatrième
        livre.</byline>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-go">
      <byline>Reportage céleste de notre envoyé spécial au paradis</byline>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-wx">
      <dateline>Zagreb :</dateline>
      <byline>de notre envoyé spécial.</byline>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum versionDate="2021-02-18" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-tp">
      <byline>Par le docteur <docAuthor>Martin Becanus</docAuthor>, au tome troisiesme de ses
          opuscules</byline>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-pa">
      <byline>由一個倫敦土生土長的市民撰寫，先前未曾出版過。</byline>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-qo">
      <byline>錄自她自己的回憶錄</byline>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[9]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-yt">
      <byline>來自華盛頓的政治編輯喬治．瓊斯</byline>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[10]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-uw">
      <dateline>重慶:</dateline>
      <byline>外交使節專用</byline>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[11]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-ww">
      <byline>源自美國哥倫比亞大學博士<docAuthor>胡適</docAuthor>
         </byline>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[12]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-zp">
      <byline>Written from her own MEMORANDUMS</byline>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[13]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-gu">
      <byline>By George Jones, Political Editor, in Washington</byline>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[14]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-byline-egXML-ii" source="#PHILIPOTT">
      <byline>BY
<docAuthor>THOMAS PHILIPOTT,</docAuthor>
Master of Arts,
(Somtimes)
Of Clare-Hall in Cambridge.</byline>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="byline-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The byline on a title page may include either the name
or a description for the document's author. Where the name is included,
it may optionally be tagged using the <gi>docAuthor</gi> element.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="byline-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>La mention de reponsabilité sur une page de titre peut inclure, soit le nom, soit la description de
                l'auteur d'un document. Lorsque le nom y est donné, on peut éventuellement l'encoder
                au moyen de l'élément <gi>docAuthor</gi>.</p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="byline-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    タイトルページにある署名欄には、当該文書の作者名や説明があるかもし
    れない。作者名がある場合、要素<gi>docAuthor</gi>を使い符号化しても
    よい。
    </p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="byline-remarks" versionDate="2017-06-13" xml:lang="de">
    <p>Die Verfasserzeile auf einer Titelseite kann entweder den Namen oder die Beschreibung des
      Dokumentautors enthalten. Wenn der Name angegeben wird, kann er optional mit dem
      <gi>docAuthor</gi>-Element ausgezeichnet werden.</p>
  </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSOC"/>
    <ptr target="#DSFRONT"/>
  </listRef>
```

^b32

