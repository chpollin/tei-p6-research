---
type: representation
source-type: document
source: '[[00_sources/tei-p5-category-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 category
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/category.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# category

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5707. Git blob: `2d82ba093511a5e3a44bdb9d6b7dd68917297f3f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-category" ident="category">
  <gloss versionDate="2009-01-05" xml:lang="en">category</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">catégorie</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Kategorie</gloss>
  <gloss versionDate="2023-10-02" xml:lang="ja">分類</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an individual descriptive category, possibly nested within a superordinate
  category, within a user-defined taxonomy.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr"> contient une catégorie descriptive particulière,
  éventuellement intégrée dans une catégorie de niveau supérieur, à l’intérieur d’une taxinomie
  définie par l’utilisateur.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사용자가 정의한 분류법 안의 개별 기술 범주를 포함한다. 상위 범주 내에 포함될 수 있다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在使用者定義之分類法當中，此元素包含一項個別的描述性類目，該類目可能位於一個更上層的類目之中。</desc>
  <desc versionDate="2023-10-02" xml:lang="ja">利用者が定義した分類法に基づく、分類上の単一の項目を示す。上位分類の中に入れることもできる。</desc>
  <desc versionDate="2016-11-17" xml:lang="de">enthält eine eigenständige, gegebenfalls in eine übergeordnete Kategorie eingebettete, deskriptive Kategorie in einer benutzerdefinierten Taxonomie.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una categoría descriptiva individual,
  posiblemente anidada dentro de una categoría superior, dentro de una taxonomía definida por el
  usuario.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una sola categoria descrittiva, possibilmente
  innestata in una categoria più generale, all'interno di una tassonomia definita dall'utente.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
  </classes>
  <content>
    <sequence>
      <alternate>
        <elementRef key="catDesc" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.descLike"/>
          <elementRef key="equiv"/>
          <elementRef key="gloss"/>
        </alternate>
      </alternate>
      <elementRef key="category" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-dq">
      <category xml:id="b1">
        <catDesc>Prose reportage</catDesc>
      </category>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-ch">
      <category xml:id="fr_tax.a.d2">
        <catDesc>Récits de voyage</catDesc>
      </category>
      <bibl>indexation selon le système d'indexation RAMEAU, géré par la Bibliothèque nationale de
      France</bibl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-ib">
      <category xml:id="fr_b1">
        <catDesc>Devinettes et énigmes </catDesc>
        <category xml:id="fr_b11">
          <catDesc>Anagrammes </catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-mz">
      <category xml:id="zh-tw_b1">
        <catDesc>報導文學</catDesc>
      </category>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-tm">
      <category xml:id="zh-tw_b2">
        <catDesc>散文 </catDesc>
        <category xml:id="zh-tw_b11">
          <catDesc>報導性質</catDesc>
        </category>
        <category xml:id="zh-tw_b12">
          <catDesc>虛構</catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-fc">
      <category xml:id="b2">
        <catDesc>Prose </catDesc>
        <category xml:id="b11">
          <catDesc>journalism</catDesc>
        </category>
        <category xml:id="b12">
          <catDesc>fiction</catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-ac">
      <category xml:id="LIT">
        <catDesc xml:lang="pl">literatura piękna</catDesc>
        <catDesc xml:lang="en">fiction</catDesc>
        <category xml:id="LPROSE">
          <catDesc xml:lang="pl">proza</catDesc>
          <catDesc xml:lang="en">prose</catDesc>
        </category>
        <category xml:id="LPOETRY">
          <catDesc xml:lang="pl">poezja</catDesc>
          <catDesc xml:lang="en">poetry</catDesc>
        </category>
        <category xml:id="LDRAMA">
          <catDesc xml:lang="pl">dramat</catDesc>
          <catDesc xml:lang="en">drama</catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD55"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="en">category</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">catégorie</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Kategorie</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2023-10-02" xml:lang="ja">分類</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an individual descriptive category, possibly nested within a superordinate
  category, within a user-defined taxonomy.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr"> contient une catégorie descriptive particulière,
  éventuellement intégrée dans une catégorie de niveau supérieur, à l’intérieur d’une taxinomie
  définie par l’utilisateur.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사용자가 정의한 분류법 안의 개별 기술 범주를 포함한다. 상위 범주 내에 포함될 수 있다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在使用者定義之分類法當中，此元素包含一項個別的描述性類目，該類目可能位於一個更上層的類目之中。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2023-10-02" xml:lang="ja">利用者が定義した分類法に基づく、分類上の単一の項目を示す。上位分類の中に入れることもできる。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">enthält eine eigenständige, gegebenfalls in eine übergeordnete Kategorie eingebettete, deskriptive Kategorie in einer benutzerdefinierten Taxonomie.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una categoría descriptiva individual,
  posiblemente anidada dentro de una categoría superior, dentro de una taxonomía definida por el
  usuario.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una sola categoria descrittiva, possibilmente
  innestata in una categoria più generale, all'interno di una tassonomia definita dall'utente.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate>
        <elementRef key="catDesc" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.descLike"/>
          <elementRef key="equiv"/>
          <elementRef key="gloss"/>
        </alternate>
      </alternate>
      <elementRef key="category" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-dq">
      <category xml:id="b1">
        <catDesc>Prose reportage</catDesc>
      </category>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-ch">
      <category xml:id="fr_tax.a.d2">
        <catDesc>Récits de voyage</catDesc>
      </category>
      <bibl>indexation selon le système d'indexation RAMEAU, géré par la Bibliothèque nationale de
      France</bibl>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-ib">
      <category xml:id="fr_b1">
        <catDesc>Devinettes et énigmes </catDesc>
        <category xml:id="fr_b11">
          <catDesc>Anagrammes </catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-mz">
      <category xml:id="zh-tw_b1">
        <catDesc>報導文學</catDesc>
      </category>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-tm">
      <category xml:id="zh-tw_b2">
        <catDesc>散文 </catDesc>
        <category xml:id="zh-tw_b11">
          <catDesc>報導性質</catDesc>
        </category>
        <category xml:id="zh-tw_b12">
          <catDesc>虛構</catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-fc">
      <category xml:id="b2">
        <catDesc>Prose </catDesc>
        <category xml:id="b11">
          <catDesc>journalism</catDesc>
        </category>
        <category xml:id="b12">
          <catDesc>fiction</catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-category-egXML-ac">
      <category xml:id="LIT">
        <catDesc xml:lang="pl">literatura piękna</catDesc>
        <catDesc xml:lang="en">fiction</catDesc>
        <category xml:id="LPROSE">
          <catDesc xml:lang="pl">proza</catDesc>
          <catDesc xml:lang="en">prose</catDesc>
        </category>
        <category xml:id="LPOETRY">
          <catDesc xml:lang="pl">poezja</catDesc>
          <catDesc xml:lang="en">poetry</catDesc>
        </category>
        <category xml:id="LDRAMA">
          <catDesc xml:lang="pl">dramat</catDesc>
          <catDesc xml:lang="en">drama</catDesc>
        </category>
      </category>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD55"/>
  </listRef>
```

^b22

