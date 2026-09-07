---
type: representation
source-type: document
source: '[[00_sources/tei-p5-entryfree-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 entryFree
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/entryFree.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# entryFree

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4966. Git blob: `31703ad1b563337ef59e47ef1b3ad0098decc1a3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-entryFree" ident="entryFree">
  <gloss versionDate="2007-07-04" xml:lang="en">unstructured entry</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">구조화되지 않은 표제 항목</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">entrada no estructurada</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">entrée libre</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">voce non strutturata</gloss>
  <desc versionDate="2011-04-29" xml:lang="en">contains a single unstructured entry in any kind of lexical
  resource, such as a dictionary or lexicon.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><gi>entry</gi> 요소에 의해 부과된 제약에 반드시 부합할 필요 없는 사전 표제 항목을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">所包含的辭條項目未必符合元素<gi>entry</gi>該有的限制條件。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素<gi>entry</gi>にある制約に必ずしも従わない辞書項目を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une entrée de dictionnaire qui ne se
			conforme pas nécessairement aux contraintes imposées par l’élément
		<gi>entry</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una entrada de diccionario no necesariamente conforme con las restricciones impuestas por el elemento <gi>entry</gi> (entrada).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una voce di dizionario non necessariamente conforme ai vincoli imposti dall'elemento entry.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.entryLike"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.entryLike"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entryFree-egXML-se">
      <entryFree><orth>biryani</orth> or <orth>biriani</orth>
            <pron>(%bIrI"A:nI)</pron>
            <def>any of a variety of Indian dishes ...</def>
            <etym>[from <lang>Urdu</lang>]</etym>
         </entryFree>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entryFree-egXML-mc" source="#fr-ex-Grand-Robert">
      <entryFree>
        <form>
          <orth>langouste</orth>
          <pron>[lägust]</pron>
        </form>
        <pos>n.</pos>
        <gen> f. </gen>
        <sense n="1">Grand crustacé marin (Décapodes macroures) aux pattes antérieures dépourvues
            de pinces, aux antennes longues et fortes, et dont la chair est très appréciée.</sense>
        <sense n="2">Fig. et fam. (vulg.). Femme, maîtresse.</sense>
        <etym>XIIIe ; languste, v. 1120, «sauterelle»; encore dans Corneille (Hymnes, 7) ; anc.
            provençal langosta, altér. du lat. class. locusta «sauterelle». </etym>
      </entryFree>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entryFree-egXML-av">
      <entryFree><orth>折羅</orth> 或 <orth>遮羅</orth>
            <pron>zhe2 luo2</pron>
            <def>Cālā (人名)</def>
            <etym>音譯自 <lang>梵文</lang>
            </etym>
         </entryFree>
    </egXML>
  </exemplum>
  <remarks ident="entryFree-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain any dictionary elements in any combination.</p>
  </remarks>
  <remarks ident="entryFree-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir n'importe quels éléments du dictionnaire dans n'importe
                quel ordre.</p>
  </remarks>
  <remarks ident="entryFree-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    あらゆる組み合わせの辞書要素が含まれる。
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
<gloss versionDate="2007-07-04" xml:lang="en">unstructured entry</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">구조화되지 않은 표제 항목</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">entrada no estructurada</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">entrée libre</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">voce non strutturata</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-04-29" xml:lang="en">contains a single unstructured entry in any kind of lexical
  resource, such as a dictionary or lexicon.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><gi>entry</gi> 요소에 의해 부과된 제약에 반드시 부합할 필요 없는 사전 표제 항목을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">所包含的辭條項目未必符合元素<gi>entry</gi>該有的限制條件。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素<gi>entry</gi>にある制約に必ずしも従わない辞書項目を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une entrée de dictionnaire qui ne se
			conforme pas nécessairement aux contraintes imposées par l’élément
		<gi>entry</gi>.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una entrada de diccionario no necesariamente conforme con las restricciones impuestas por el elemento <gi>entry</gi> (entrada).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una voce di dizionario non necessariamente conforme ai vincoli imposti dall'elemento entry.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.entryLike"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.entryLike"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
```

^b14

### Block 15

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

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entryFree-egXML-se">
      <entryFree><orth>biryani</orth> or <orth>biriani</orth>
            <pron>(%bIrI"A:nI)</pron>
            <def>any of a variety of Indian dishes ...</def>
            <etym>[from <lang>Urdu</lang>]</etym>
         </entryFree>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entryFree-egXML-mc" source="#fr-ex-Grand-Robert">
      <entryFree>
        <form>
          <orth>langouste</orth>
          <pron>[lägust]</pron>
        </form>
        <pos>n.</pos>
        <gen> f. </gen>
        <sense n="1">Grand crustacé marin (Décapodes macroures) aux pattes antérieures dépourvues
            de pinces, aux antennes longues et fortes, et dont la chair est très appréciée.</sense>
        <sense n="2">Fig. et fam. (vulg.). Femme, maîtresse.</sense>
        <etym>XIIIe ; languste, v. 1120, «sauterelle»; encore dans Corneille (Hymnes, 7) ; anc.
            provençal langosta, altér. du lat. class. locusta «sauterelle». </etym>
      </entryFree>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entryFree-egXML-av">
      <entryFree><orth>折羅</orth> 或 <orth>遮羅</orth>
            <pron>zhe2 luo2</pron>
            <def>Cālā (人名)</def>
            <etym>音譯自 <lang>梵文</lang>
            </etym>
         </entryFree>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="entryFree-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain any dictionary elements in any combination.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="entryFree-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir n'importe quels éléments du dictionnaire dans n'importe
                quel ordre.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="entryFree-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    あらゆる組み合わせの辞書要素が含まれる。
    </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIBO"/>
    <ptr target="#DIEN"/>
  </listRef>
```

^b22

