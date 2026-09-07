---
type: representation
source-type: document
source: '[[00_sources/tei-p5-valdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 valDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/valDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# valDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3419. Git blob: `bddb0f2a3c4c8d3f453de44c403a386f16b714ad`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-valDesc" ident="valDesc">
  <gloss versionDate="2005-01-14" xml:lang="en">value description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">값 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性值描述</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description de la valeur</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">valor de la descripción</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione del valore</gloss>
  <desc versionDate="2013-12-22" xml:lang="en">specifies any semantic or syntactic constraint on the value that
an attribute may take, additional to the information carried by the
<gi>datatype</gi> element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">데이터 유형 요소에 의해 수행된 정보와 더불어 속성이 취할 수 있는 값에 대한 의미적 또는 통사적 제약을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">除了元素<gi>datatype</gi>所帶有的資訊之外，說明屬性可使用的屬性值在字義或語法上的限制。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素<gi>datatype</gi>にある情報に加えて、属性値の意味的・統語的制約
  を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">précise toute contrainte sémantique ou syntaxique
			sur la valeur que peut prendre un attribut, en supplément de l'information portée par
			l'élément <gi>datatype</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica cualquier vínculo de tipo semántico o sintáctico respecto al valor que un atributo puede asumir, añadiendo informaciones referentes al elemento datatype.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica un qualsiasi
  vincolo di tipo semantico o sintattico rispetto al valore che un
  attributo può assumere, aggiungendo informazioni rispetto a quanto
  contenuto nell'elemento datatype</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
    <memberOf key="att.translatable"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valDesc-egXML-nl">
      <valDesc>must point to another <gi>align</gi>
      element logically preceding this one.</valDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valDesc-egXML-qm">
      <valDesc>doit pointer vers un autre élément <gi>align</gi>précédant logiquement
        celui-ci.</valDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valDesc-egXML-wj">
      <valDesc>必須指向另一個的邏輯上先於此的元素<gi>align</gi>
         </valDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDATT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">value description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">값 기술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性值描述</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description de la valeur</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">valor de la descripción</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione del valore</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-12-22" xml:lang="en">specifies any semantic or syntactic constraint on the value that
an attribute may take, additional to the information carried by the
<gi>datatype</gi> element.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">데이터 유형 요소에 의해 수행된 정보와 더불어 속성이 취할 수 있는 값에 대한 의미적 또는 통사적 제약을 명시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">除了元素<gi>datatype</gi>所帶有的資訊之外，說明屬性可使用的屬性值在字義或語法上的限制。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素<gi>datatype</gi>にある情報に加えて、属性値の意味的・統語的制約
  を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise toute contrainte sémantique ou syntaxique
			sur la valeur que peut prendre un attribut, en supplément de l'information portée par
			l'élément <gi>datatype</gi>.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica cualquier vínculo de tipo semántico o sintáctico respecto al valor que un atributo puede asumir, añadiendo informaciones referentes al elemento datatype.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica un qualsiasi
  vincolo di tipo semantico o sintattico rispetto al valore che un
  attributo può assumere, aggiungendo informazioni rispetto a quanto
  contenuto nell'elemento datatype</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
    <memberOf key="att.translatable"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valDesc-egXML-nl">
      <valDesc>must point to another <gi>align</gi>
      element logically preceding this one.</valDesc>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valDesc-egXML-qm">
      <valDesc>doit pointer vers un autre élément <gi>align</gi>précédant logiquement
        celui-ci.</valDesc>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valDesc-egXML-wj">
      <valDesc>必須指向另一個的邏輯上先於此的元素<gi>align</gi>
         </valDesc>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDATT"/>
  </listRef>
```

^b19

