---
type: representation
source-type: document
source: '[[00_sources/tei-p5-item-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 item
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/item.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# item

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6615. Git blob: `68d3fca54225299a00f55a96993bc83f3d44df23`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-item" ident="item">
  <gloss versionDate="2017-06-04" xml:lang="en">item</gloss>
  <gloss versionDate="2017-06-04" xml:lang="de">Listenpunkt</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains one component of a list.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">목록에서 하나의 성분을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含列表中的一個項目。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">リストのいち項目を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient un composant d'une liste.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un componente de una lista.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un componente di una lista.</desc>
  <desc versionDate="2017-06-04" xml:lang="de">enthält einen Listenpunkt.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-item-egXML-gh" source="#DS-eg-01">
      <list rend="numbered">
        <head>Here begin the chapter headings of Book IV</head>
        <item n="4.1">The death of Queen Clotild.</item>
        <item n="4.2">How King Lothar wanted to appropriate one third of the Church revenues.</item>
        <item n="4.3">The wives and children of Lothar.</item>
        <item n="4.4">The Counts of the Bretons.</item>
        <item n="4.5">Saint Gall the Bishop.</item>
        <item n="4.6">The priest Cato.</item>
        <item> ...</item>
      </list>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-item-egXML-fz" source="#fr-ex-Perec-vie">
      <list>
        <head>Tentative d'inventaire de quelques-unes des choses qui ont été trouvées dans
              les escaliers au fil des ans.</head>
        <item>Plusieurs photos, dont celle d'une jeune fille de quinze<lb/> ans vêtue d'un slip
              de bain noir et d'un chandail blanc, agenouillée sur une plage,</item>
        <item>un réveil radio de toute évidence destiné à un réparateur, dans un sac plastique
              des établissements Nicolas,</item>
        <item>un soulier noir orné de brillants,</item>
        <item>une mule en chevreau doré,</item>
        <item>une boîte de pastilles Géraudel contre la toux.</item>
      </list>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-item-egXML-ek" source="#biblzh-tw_n8">
      <list rend="numbered">
        <head>以下為第三部份的各個章節標題</head>
        <item n="3.1">人物的鑑賞</item>
        <item n="3.2">情節的鑑賞</item>
        <item n="3.3">環境的鑑賞</item>
        <item n="3.4">主題的鑑賞</item>
        <item n="3.5">語言的鑑賞</item>
        <item> ...</item>
      </list>
    </egXML>
  </exemplum>
  <remarks ident="item-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain simple prose or a sequence of chunks.</p>
    <p>Whatever string of characters is used to label a list item in the copy text may be used as
      the value of the global <att>n</att> attribute, but it is not required that numbering be
      recorded explicitly. In ordered lists, the <att>n</att> attribute on the <gi>item</gi> element
      is by definition synonymous with the use of the <gi>label</gi> element to record the
      enumerator of the list item. In glossary lists, however, the term being defined should be
      given with the <gi>label</gi> element, not <att>n</att>.</p>
  </remarks>
  <remarks ident="item-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir un texte ou une succession d'extraits.</p>
    <p>Toute chaîne de caractères utilisée pour étiqueter un item de liste dans le texte peut être
      utilisée comme valeur de l'attribut global <att>n</att>, mais il n'est pas obligatoire de
      noter explicitement cette numérotation. Dans les listes ordonnées, l'attribut <att>n</att> de
      l'élément <gi>item</gi> est par définition synonyme de l'utilisation de l'élément
      <gi>label</gi> pour noter le numéro de l'item de la liste. Pour les glossaires toutefois, le
      terme défini doit être donné avec l'élément <gi>label</gi>, et non pas <att>n</att>.</p>
  </remarks>
  <remarks ident="item-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 散文または文塊を示す。 </p>
    <p> 文字列が元資料中にあるリスト項目のラベルを表すために使用される使わ れる場合、グローバル属性<att>n</att>の値として使用されるかもしれな
      い。しかし、この数は明記される必要はない。 順序付きリストの場合、要素<gi>item</gi>の属性<att>n</att>は、
      リスト項目の数を示す要素<gi>label</gi>と同じ意味で使用されている。 用語集の場合、当該要素は、属性<att>n</att>ではなく、要素
      <gi>label</gi>と共に使用されるべきである。 </p>
  </remarks>
  <remarks ident="item-remarks" versionDate="2017-06-04" xml:lang="de">
    <p rend="dataDesc">Kann einen einfachen Fließtext enthalten oder eine Sequenz von Chunks.</p>
    <p>Welche Zeichenfolge auch immer für die Kennzeichnung eines Listenpunkts in der Vorlage
      benutzt wird, kann als Wert des globalen <att>n</att>-Attributs verwendet werden, dabei muss die
      Nummerierung nicht notwendigerweise erfasst werden. In geordneten Listen ist das
      <att>n</att>-Attribut des <gi>item</gi>-Elements per Definition synonym mit dem Gebrauch des
      <gi>label</gi>-Elements, um den Zähler des Listenpunkts zu erfassen. In Glossarlisten sollte
      der zu definierende Term im <gi>label</gi>-Element und nicht im <att>n</att>-Attribut angegeben
      werden.</p>
  </remarks>
  
  <listRef>
    <ptr target="#COLI" type="div2"/>
    <ptr target="#HD6"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2017-06-04" xml:lang="en">item</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2017-06-04" xml:lang="de">Listenpunkt</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains one component of a list.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">목록에서 하나의 성분을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含列表中的一個項目。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">リストのいち項目を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient un composant d'une liste.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un componente de una lista.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un componente di una lista.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-04" xml:lang="de">enthält einen Listenpunkt.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-item-egXML-gh" source="#DS-eg-01">
      <list rend="numbered">
        <head>Here begin the chapter headings of Book IV</head>
        <item n="4.1">The death of Queen Clotild.</item>
        <item n="4.2">How King Lothar wanted to appropriate one third of the Church revenues.</item>
        <item n="4.3">The wives and children of Lothar.</item>
        <item n="4.4">The Counts of the Bretons.</item>
        <item n="4.5">Saint Gall the Bishop.</item>
        <item n="4.6">The priest Cato.</item>
        <item> ...</item>
      </list>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-item-egXML-fz" source="#fr-ex-Perec-vie">
      <list>
        <head>Tentative d'inventaire de quelques-unes des choses qui ont été trouvées dans
              les escaliers au fil des ans.</head>
        <item>Plusieurs photos, dont celle d'une jeune fille de quinze<lb/> ans vêtue d'un slip
              de bain noir et d'un chandail blanc, agenouillée sur une plage,</item>
        <item>un réveil radio de toute évidence destiné à un réparateur, dans un sac plastique
              des établissements Nicolas,</item>
        <item>un soulier noir orné de brillants,</item>
        <item>une mule en chevreau doré,</item>
        <item>une boîte de pastilles Géraudel contre la toux.</item>
      </list>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-item-egXML-ek" source="#biblzh-tw_n8">
      <list rend="numbered">
        <head>以下為第三部份的各個章節標題</head>
        <item n="3.1">人物的鑑賞</item>
        <item n="3.2">情節的鑑賞</item>
        <item n="3.3">環境的鑑賞</item>
        <item n="3.4">主題的鑑賞</item>
        <item n="3.5">語言的鑑賞</item>
        <item> ...</item>
      </list>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="item-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain simple prose or a sequence of chunks.</p>
    <p>Whatever string of characters is used to label a list item in the copy text may be used as
      the value of the global <att>n</att> attribute, but it is not required that numbering be
      recorded explicitly. In ordered lists, the <att>n</att> attribute on the <gi>item</gi> element
      is by definition synonymous with the use of the <gi>label</gi> element to record the
      enumerator of the list item. In glossary lists, however, the term being defined should be
      given with the <gi>label</gi> element, not <att>n</att>.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="item-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir un texte ou une succession d'extraits.</p>
    <p>Toute chaîne de caractères utilisée pour étiqueter un item de liste dans le texte peut être
      utilisée comme valeur de l'attribut global <att>n</att>, mais il n'est pas obligatoire de
      noter explicitement cette numérotation. Dans les listes ordonnées, l'attribut <att>n</att> de
      l'élément <gi>item</gi> est par définition synonyme de l'utilisation de l'élément
      <gi>label</gi> pour noter le numéro de l'item de la liste. Pour les glossaires toutefois, le
      terme défini doit être donné avec l'élément <gi>label</gi>, et non pas <att>n</att>.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="item-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 散文または文塊を示す。 </p>
    <p> 文字列が元資料中にあるリスト項目のラベルを表すために使用される使わ れる場合、グローバル属性<att>n</att>の値として使用されるかもしれな
      い。しかし、この数は明記される必要はない。 順序付きリストの場合、要素<gi>item</gi>の属性<att>n</att>は、
      リスト項目の数を示す要素<gi>label</gi>と同じ意味で使用されている。 用語集の場合、当該要素は、属性<att>n</att>ではなく、要素
      <gi>label</gi>と共に使用されるべきである。 </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="item-remarks" versionDate="2017-06-04" xml:lang="de">
    <p rend="dataDesc">Kann einen einfachen Fließtext enthalten oder eine Sequenz von Chunks.</p>
    <p>Welche Zeichenfolge auch immer für die Kennzeichnung eines Listenpunkts in der Vorlage
      benutzt wird, kann als Wert des globalen <att>n</att>-Attributs verwendet werden, dabei muss die
      Nummerierung nicht notwendigerweise erfasst werden. In geordneten Listen ist das
      <att>n</att>-Attribut des <gi>item</gi>-Elements per Definition synonym mit dem Gebrauch des
      <gi>label</gi>-Elements, um den Zähler des Listenpunkts zu erfassen. In Glossarlisten sollte
      der zu definierende Term im <gi>label</gi>-Element und nicht im <att>n</att>-Attribut angegeben
      werden.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COLI" type="div2"/>
    <ptr target="#HD6"/>
  </listRef>
```

^b20

