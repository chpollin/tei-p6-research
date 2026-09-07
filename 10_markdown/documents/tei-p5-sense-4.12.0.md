---
type: representation
source-type: document
source: '[[00_sources/tei-p5-sense-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 sense
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/sense.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# sense

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5414. Git blob: `b9a2701e69021a7950b7805b0227ffa3a5d85f8b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-sense" ident="sense">
  <desc versionDate="2007-10-18" xml:lang="en">groups together all information relating to one word sense in a dictionary entry, for
    example definitions, examples, and translation equivalents.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 사전 표제 항목에서 하나의 단어 의미와 관련된 모든 정보를 모아 놓는다. 예를 들어 정의,
    예문, 번역어</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集辭條中一個字義的所有相關資訊(定義、範例、翻譯等)。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書項目にある単語の意味と関連する情報をまとめる。例えば、定義、用例、 翻訳など。</desc>
  <desc versionDate="2009-04-08" xml:lang="fr">regroupe toutes les informations relatives à un des sens
    d’un mot dans une entrée de dictionnaire (définitions, exemples, équivalents linguistiques,
    etc.).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa toda la información relativa al significado de una
    palabra en una entrada de diccionario (definiciones, ejemplos, sinónimos, etc.)</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa tutte le informazioni attinenti al senso di una
    parola in una voce di dizionario (definizioni, esempi, equivalente traduttivo, ecc.).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.entryPart"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <elementRef key="sense"/>
        <classRef key="model.entryPart.top"/>
        <classRef key="model.phrase"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <attList>
    <attDef ident="level" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">gives the nesting depth of this sense.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">의미의 층위를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該字義在辭條中的層次。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該意味情報の構造の深さを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le niveau de ce sens dans la hiérarchie.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">la profundidad de anidamiente</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce il grado di nidificazione del senso.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sense-egXML-hu">
      <sense n="2">
        <usg type="time">Vx.</usg>
        <def>Vaillance, bravoure (spécial., au combat)</def>
        <cit type="example">
          <quote>La valeur n'attend pas le nombre des années</quote>
          <bibl>
            <author>Corneille</author>
          </bibl>
        </cit>
      </sense>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sense-egXML-sb" source="#fr-ex-TLFI">
      <sense n="2">
        <usg type="time">Vx.</usg>
        <def>Vaillance, bravoure (spécial., au combat)</def>
        <cit type="example">
          <quote>La valeur n'attend pas le nombre des années.</quote>
          <bibl>
            <author>Corneille</author>
            <title>Le Cid</title>
          </bibl>
        </cit>
      </sense>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sense-egXML-dw" source="#biblzh-tw_n28">
      <sense n="2">
        <usg type="time">現代</usg>
        <def>胭脂和香粉，舊時借指婦女</def>
        <cit type="example">
          <quote>那一年頌蓮留著齊耳的短髮，用一條天藍色的緞帶箍住，她的臉是圓圓的，不施脂粉，但顯得有點蒼白。</quote>
          <bibl>
            <author>蘇童</author>
          </bibl>
        </cit>
      </sense>
    </egXML>
  </exemplum>
  <remarks ident="sense-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data mixed with any other elements defined in the
      dictionary tag set.</p>
  </remarks>
  <remarks ident="sense-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères combinés avec tout autre élément défini dans le
      jeu de balises du dictionnaire.</p>
  </remarks>
  <remarks ident="sense-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 辞書向けタグ集合で定義されている他の要素と文字データが混在するかも しれない。 </p>
  </remarks>
  <listRef>
    <ptr target="#DIEN" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-18" xml:lang="en">groups together all information relating to one word sense in a dictionary entry, for
    example definitions, examples, and translation equivalents.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 사전 표제 항목에서 하나의 단어 의미와 관련된 모든 정보를 모아 놓는다. 예를 들어 정의,
    예문, 번역어</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集辭條中一個字義的所有相關資訊(定義、範例、翻譯等)。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書項目にある単語の意味と関連する情報をまとめる。例えば、定義、用例、 翻訳など。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-08" xml:lang="fr">regroupe toutes les informations relatives à un des sens
    d’un mot dans une entrée de dictionnaire (définitions, exemples, équivalents linguistiques,
    etc.).</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa toda la información relativa al significado de una
    palabra en una entrada de diccionario (definiciones, ejemplos, sinónimos, etc.)</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa tutte le informazioni attinenti al senso di una
    parola in una voce di dizionario (definizioni, esempi, equivalente traduttivo, ecc.).</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.entryPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <elementRef key="sense"/>
        <classRef key="model.entryPart.top"/>
        <classRef key="model.phrase"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">gives the nesting depth of this sense.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">의미의 층위를 제시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該字義在辭條中的層次。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該意味情報の構造の深さを示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le niveau de ce sens dans la hiérarchie.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">la profundidad de anidamiente</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il grado di nidificazione del senso.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sense-egXML-hu">
      <sense n="2">
        <usg type="time">Vx.</usg>
        <def>Vaillance, bravoure (spécial., au combat)</def>
        <cit type="example">
          <quote>La valeur n'attend pas le nombre des années</quote>
          <bibl>
            <author>Corneille</author>
          </bibl>
        </cit>
      </sense>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sense-egXML-sb" source="#fr-ex-TLFI">
      <sense n="2">
        <usg type="time">Vx.</usg>
        <def>Vaillance, bravoure (spécial., au combat)</def>
        <cit type="example">
          <quote>La valeur n'attend pas le nombre des années.</quote>
          <bibl>
            <author>Corneille</author>
            <title>Le Cid</title>
          </bibl>
        </cit>
      </sense>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-sense-egXML-dw" source="#biblzh-tw_n28">
      <sense n="2">
        <usg type="time">現代</usg>
        <def>胭脂和香粉，舊時借指婦女</def>
        <cit type="example">
          <quote>那一年頌蓮留著齊耳的短髮，用一條天藍色的緞帶箍住，她的臉是圓圓的，不施脂粉，但顯得有點蒼白。</quote>
          <bibl>
            <author>蘇童</author>
          </bibl>
        </cit>
      </sense>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="sense-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data mixed with any other elements defined in the
      dictionary tag set.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="sense-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères combinés avec tout autre élément défini dans le
      jeu de balises du dictionnaire.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="sense-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 辞書向けタグ集合で定義されている他の要素と文字データが混在するかも しれない。 </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIEN" type="div2"/>
  </listRef>
```

^b24

