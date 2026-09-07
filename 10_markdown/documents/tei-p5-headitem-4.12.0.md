---
type: representation
source-type: document
source: '[[00_sources/tei-p5-headitem-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 headItem
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/headItem.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# headItem

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5027. Git blob: `a0da434619982cd52eaaa5ba5f2981abe42adf79`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-headItem" ident="headItem">
  <gloss versionDate="2005-01-14" xml:lang="en">heading for list items</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">목록의 항목에 대한 표제부</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">列表項目的標題</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">intitulé d'une liste d'items</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">encabezamiento de los ítems de una lista.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">titolo per le voci della lista</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the heading for the item or gloss column in a glossary list or similar structured
        list.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">용어집 목록 또는 유사 구조의 목록에서 항목 또는 해설에 대한 표제부를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含詞彙列表或結構類似的列表中項目或註解欄位的標題。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">用語集などのリスト構造における各項目の見出しを示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient l'intitulé pour la colonne d'items ou de
        gloses dans un glossaire ou  dans une liste  semblablement structurée.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el encabezamiento de una columna de ítems o
        glosas en una lista de un glosario u otra lista de estructura similar.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il titolo per l'a voce o la colonna glossa in
        un glossario o un'altra lista strutturata in modo simile.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-headItem-egXML-ms">The simple, straightforward statement of an
            idea is preferable to the use of a worn-out expression. <list type="gloss"><headLabel rend="smallcaps">TRITE</headLabel><headItem rend="smallcaps">SIMPLE, STRAIGHTFORWARD</headItem><label>bury the hatchet</label><item>stop fighting, make peace</item><label>at loose ends</label><item>disorganized</item><label>on speaking terms</label><item>friendly</item><label>fair and square</label><item>completely honest</item><label>at death's door</label><item>near death</item></list>
        </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-headItem-egXML-qq" source="#fr-ex-franglais"> Parlez-vous
        anglosnob? Liste de quelques mots franglais et des propositions pour les remplacer : : <list type="gloss"><headLabel rend="smallcaps">Ne dites pas</headLabel><headItem rend="smallcaps">Mais dites...</headItem><label>abstract </label><item> résumé, abrégé </item><label>baby-boom </label><item>printemps démographique </item><label>carjacking </label><item>dévoituration (comme défenestration), dévoiturage(comme cambriolage, braquage) </item><label>bug </label><item>erreur, défaut, insecte, ("bogue" est inutile) </item><label>mixer</label><item>mélanger (sauf si c'est avec un mixeur)</item></list>
      </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-headItem-egXML-wj">
   經過五四運動，中國文學自文言文發展為白話文。 <list type="gloss"><headLabel rend="smallcaps">文言文</headLabel><headItem rend="smallcaps">白話文</headItem><label>汝</label><item> 你</item><label>吾</label><item>我</item><label>彼</label><item>他</item><label>爾輩</label><item>你們</item><label>吾等</label><item>我們</item></list>
      </egXML>
  </exemplum>
  <remarks ident="headItem-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>headItem</gi> element may appear only if each item in the list is preceded by a
                <gi>label</gi>.</p>
  </remarks>
  <remarks ident="headItem-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'élément <gi>headItem</gi> est utilisé uniquement si chacun des items d'une liste est
            précédé d'un élément <gi>label</gi>.</p>
  </remarks>
  <remarks ident="headItem-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>headItem</gi>は、子要素<gi>item</gi>が要素<gi>label</gi>を 伴う時にのみ使用されるだろう。 </p>
  </remarks>
  <listRef>
    <ptr target="#COLI" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">heading for list items</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">목록의 항목에 대한 표제부</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">列表項目的標題</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">intitulé d'une liste d'items</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">encabezamiento de los ítems de una lista.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">titolo per le voci della lista</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the heading for the item or gloss column in a glossary list or similar structured
        list.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">용어집 목록 또는 유사 구조의 목록에서 항목 또는 해설에 대한 표제부를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含詞彙列表或結構類似的列表中項目或註解欄位的標題。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">用語集などのリスト構造における各項目の見出しを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient l'intitulé pour la colonne d'items ou de
        gloses dans un glossaire ou  dans une liste  semblablement structurée.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el encabezamiento de una columna de ítems o
        glosas en una lista de un glosario u otra lista de estructura similar.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il titolo per l'a voce o la colonna glossa in
        un glossario o un'altra lista strutturata in modo simile.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-headItem-egXML-ms">The simple, straightforward statement of an
            idea is preferable to the use of a worn-out expression. <list type="gloss"><headLabel rend="smallcaps">TRITE</headLabel><headItem rend="smallcaps">SIMPLE, STRAIGHTFORWARD</headItem><label>bury the hatchet</label><item>stop fighting, make peace</item><label>at loose ends</label><item>disorganized</item><label>on speaking terms</label><item>friendly</item><label>fair and square</label><item>completely honest</item><label>at death's door</label><item>near death</item></list>
        </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-headItem-egXML-qq" source="#fr-ex-franglais"> Parlez-vous
        anglosnob? Liste de quelques mots franglais et des propositions pour les remplacer : : <list type="gloss"><headLabel rend="smallcaps">Ne dites pas</headLabel><headItem rend="smallcaps">Mais dites...</headItem><label>abstract </label><item> résumé, abrégé </item><label>baby-boom </label><item>printemps démographique </item><label>carjacking </label><item>dévoituration (comme défenestration), dévoiturage(comme cambriolage, braquage) </item><label>bug </label><item>erreur, défaut, insecte, ("bogue" est inutile) </item><label>mixer</label><item>mélanger (sauf si c'est avec un mixeur)</item></list>
      </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-headItem-egXML-wj">
   經過五四運動，中國文學自文言文發展為白話文。 <list type="gloss"><headLabel rend="smallcaps">文言文</headLabel><headItem rend="smallcaps">白話文</headItem><label>汝</label><item> 你</item><label>吾</label><item>我</item><label>彼</label><item>他</item><label>爾輩</label><item>你們</item><label>吾等</label><item>我們</item></list>
      </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="headItem-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>headItem</gi> element may appear only if each item in the list is preceded by a
                <gi>label</gi>.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="headItem-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'élément <gi>headItem</gi> est utilisé uniquement si chacun des items d'une liste est
            précédé d'un élément <gi>label</gi>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="headItem-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 要素<gi>headItem</gi>は、子要素<gi>item</gi>が要素<gi>label</gi>を 伴う時にのみ使用されるだろう。 </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COLI" type="div2"/>
  </listRef>
```

^b22

