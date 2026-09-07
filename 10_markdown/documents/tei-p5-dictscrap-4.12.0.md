---
type: representation
source-type: document
source: '[[00_sources/tei-p5-dictscrap-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 dictScrap
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/dictScrap.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# dictScrap

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5633. Git blob: `44902072a9aff3ccfea5ef58101ab9b294c2a7ef`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-dictScrap" ident="dictScrap">
  <gloss versionDate="2007-07-04" xml:lang="en">dictionary scrap</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">사전 발췌부</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">fragmento de diccionario</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">bloc d'informations</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">frammento di dizionario</gloss>
  <gloss versionDate="2024-09-05" xml:lang="ja">辞書の小見出し</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">encloses a part of a dictionary entry in which other phrase-level dictionary elements are
        freely combined.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">다른 구-층위 사전 요소들이 자유롭게 결합된 사전 표제 항목의 부분을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">字典辭條的片段，包含自由組合的詞組層次字典元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">句レベルの辞書要素をとる辞書項目を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la partie d'une entrée de dictionnaire
			dans laquelle d'autres éléments de niveau <q>expression</q> sont librement associés.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">engloba una parte de la entrada del diccionario en la que otros elementos de nivel sintagmático del diccionario se combinan de forma libre.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">include una parte di una voce di dizionario in cui sono combinati liberamente altri elementi di dizionario a livello sintagmatico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.entryPart"/>
        <classRef key="model.morphLike"/>
        <classRef key="model.phrase"/>
        <classRef key="model.inter"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dictScrap-egXML-jt">
      <entry>
        <dictScrap><orth>biryani</orth> or <orth>biriani</orth>
               <pron>(%bIrI"A:nI)</pron>
               <def>any of a variety of Indian dishes ...</def>
               <etym>[from <lang>Urdu</lang>]</etym>
            </dictScrap>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dictScrap-egXML-tk" source="#fr-ex-TLFI">
      <entry>
        <dictScrap><orth>cattleya </orth> ou <orth>catleya</orth>
               <pron>[katleja]</pron>
               <def>Orchidée épiphyte, originaire d'Amérique tropicale, et dont l'espèce la plus connue
              est très recherchée pour l'élégance de ses fleurs mauves à grand labelle en cornet
              onduleux.</def>
               <etym>1845 cattleye (BESCH.); 1893 cattleya (Gde Encyclop.). Lat. sc. cattleya, nom
              donné par John Lindley, botaniste angl. (1799-1865) à un genre d'orchidées en hommage
              au botaniste angl. W. Cattley (NED. Suppl.; DEI et Gde Encyclop.) </etym>
            </dictScrap>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dictScrap-egXML-er">
      <entry>
        <dictScrap><orth>折羅</orth> 或 <orth>遮羅</orth>
               <pron>zhe2 luo2</pron>
               <def>Cālā (人名)</def>
               <etym>音譯自 <lang>梵文</lang>
               </etym>
            </dictScrap>
      </entry>
    </egXML>
  </exemplum>
  <remarks ident="dictScrap-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain any dictionary elements in any combination.</p>
    <p>This element is used to mark part of a dictionary entry in which lower level dictionary
            elements appear, but which does not itself form an identifiable structural unit.</p>
  </remarks>
  <remarks ident="dictScrap-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">peut contenir n'importe quels éléments de dictionnaire dans n'importe
                quelle combinaison.</p>
    <p>Cet élément est utilisé pour marquer la partie d'une entrée de dictionnaire dans
                laquelle les éléments de dictionnaire de niveau inférieur apparaissent sans former
                toutefois d'unité structurelle identifiable.</p>
  </remarks>
  <remarks ident="dictScrap-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    あらゆる辞書要素をとる。
    </p>
    <p>
    当該要素は、下位レベルの辞書要素から成る辞書項目を示す際に使われる。
    当該要素自体は参照可能な単位には成らない。
    </p>
  </remarks>
  <listRef>
    <ptr target="#DIBO"/>
    <ptr target="#DIEN"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">dictionary scrap</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">사전 발췌부</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">fragmento de diccionario</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">bloc d'informations</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">frammento di dizionario</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-09-05" xml:lang="ja">辞書の小見出し</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">encloses a part of a dictionary entry in which other phrase-level dictionary elements are
        freely combined.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다른 구-층위 사전 요소들이 자유롭게 결합된 사전 표제 항목의 부분을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">字典辭條的片段，包含自由組合的詞組層次字典元素。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">句レベルの辞書要素をとる辞書項目を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la partie d'une entrée de dictionnaire
			dans laquelle d'autres éléments de niveau <q>expression</q> sont librement associés.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">engloba una parte de la entrada del diccionario en la que otros elementos de nivel sintagmático del diccionario se combinan de forma libre.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">include una parte di una voce di dizionario in cui sono combinati liberamente altri elementi di dizionario a livello sintagmatico.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.entryPart"/>
        <classRef key="model.morphLike"/>
        <classRef key="model.phrase"/>
        <classRef key="model.inter"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dictScrap-egXML-jt">
      <entry>
        <dictScrap><orth>biryani</orth> or <orth>biriani</orth>
               <pron>(%bIrI"A:nI)</pron>
               <def>any of a variety of Indian dishes ...</def>
               <etym>[from <lang>Urdu</lang>]</etym>
            </dictScrap>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dictScrap-egXML-tk" source="#fr-ex-TLFI">
      <entry>
        <dictScrap><orth>cattleya </orth> ou <orth>catleya</orth>
               <pron>[katleja]</pron>
               <def>Orchidée épiphyte, originaire d'Amérique tropicale, et dont l'espèce la plus connue
              est très recherchée pour l'élégance de ses fleurs mauves à grand labelle en cornet
              onduleux.</def>
               <etym>1845 cattleye (BESCH.); 1893 cattleya (Gde Encyclop.). Lat. sc. cattleya, nom
              donné par John Lindley, botaniste angl. (1799-1865) à un genre d'orchidées en hommage
              au botaniste angl. W. Cattley (NED. Suppl.; DEI et Gde Encyclop.) </etym>
            </dictScrap>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-dictScrap-egXML-er">
      <entry>
        <dictScrap><orth>折羅</orth> 或 <orth>遮羅</orth>
               <pron>zhe2 luo2</pron>
               <def>Cālā (人名)</def>
               <etym>音譯自 <lang>梵文</lang>
               </etym>
            </dictScrap>
      </entry>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="dictScrap-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain any dictionary elements in any combination.</p>
    <p>This element is used to mark part of a dictionary entry in which lower level dictionary
            elements appear, but which does not itself form an identifiable structural unit.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="dictScrap-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">peut contenir n'importe quels éléments de dictionnaire dans n'importe
                quelle combinaison.</p>
    <p>Cet élément est utilisé pour marquer la partie d'une entrée de dictionnaire dans
                laquelle les éléments de dictionnaire de niveau inférieur apparaissent sans former
                toutefois d'unité structurelle identifiable.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="dictScrap-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    あらゆる辞書要素をとる。
    </p>
    <p>
    当該要素は、下位レベルの辞書要素から成る辞書項目を示す際に使われる。
    当該要素自体は参照可能な単位には成らない。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIBO"/>
    <ptr target="#DIEN"/>
  </listRef>
```

^b23

