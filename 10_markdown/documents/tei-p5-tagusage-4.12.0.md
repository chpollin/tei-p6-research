---
type: representation
source-type: document
source: '[[00_sources/tei-p5-tagusage-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 tagUsage
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/tagUsage.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# tagUsage

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9243. Git blob: `8f602c9a0ef17101667fe57da27a103852aa6181`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-tagUsage" ident="tagUsage">
  <gloss versionDate="2020-12-20" xml:lang="en">element usage</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">usage des balises</gloss>
  <gloss versionDate="2019-07-08" xml:lang="de">Verwendung eines Elements</gloss>
  <desc versionDate="2016-02-16" xml:lang="en">documents the usage of a specific element within a specified document.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">donne des informations sur l’utilisation d’un élément
    spécifique dans un texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트에서 특정 요소의 사용에 관한 정보를 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供文件中某個特定元素的使用資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト中にある特定要素の使い方に関する情報を示す。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">dokumentiert den Gebrauch eines spezifischen Elements innerhalb
    eines bestimmten Dokuments.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona información sobre el uso de un elemento
    específico al interno del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni circa l'uso di uno specifico
    elemento all'interno di un testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
  </classes>
  <content>
    <macroRef key="macro.limitedContent"/>
  </content>
  <attList>
    <attDef ident="gi" usage="req">
      <gloss versionDate="2013-11-20" xml:lang="en">generic identifier</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">요소 이름</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">nombre de elemento</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">nom de l'élément</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">nome di elemento</gloss>
      <gloss versionDate="2019-07-08" xml:lang="de">generische Kennung</gloss>
      <desc versionDate="2013-11-20" xml:lang="en">specifies the name
      (generic identifier) of the element indicated by the tag,  within the namespace indicated by the parent
        <gi>namespace</gi> element.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">nom (identifiant générique) de l’élément indiqué par
        la balise.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">태그로 제시된 요소의 이름(일반적 확인소)</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">該標籤所指明的元素名稱 (通用識別符碼)。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該タグで示された要素の名前(GI、 共通識別子)。</desc>
      <desc versionDate="2018-07-18" xml:lang="de">gibt den Namen (generische Kennung) des durch das Tag angegebenen Elements innerhalb jenes Namensraums an, 
        der im übergeordneten <gi>namespace</gi>-Element angegeben wird.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">el nombre (identificador genérico) de un elemento
        indicado mediante una etiqueta.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">il nome (identificatore generico) dell'elemento
        indicato dal marcatore.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
    </attDef>
    <attDef ident="occurs" usage="rec">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the number of occurrences of this element within the text.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">spécifie le nombre d’occurrences de cet élément dans
        le texte.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">텍스트 내부에 이 요소가 출현 횟수를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該元素在文本中出現的次數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素が、テキスト中で出現する回数を示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">gibt an, wie oft das Element im Text vorkommt.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el número de veces que un elemento
        determinado aparece en el texto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il numero di occorrenze dell'elemento nel
        testo.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
    </attDef>
    <attDef ident="withId" usage="rec">
      <gloss versionDate="2007-07-04" xml:lang="en">with unique identifier</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">고유한 확인소를 가진</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">con identificador único</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">avec identificateur unique</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">con identificatore unico</gloss>
      <gloss versionDate="2019-07-08" xml:lang="de">mit eindeutiger Kennung</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">specifies the number of occurrences of this element within the text which bear a
        distinct value for the global <att>xml:id</att> attribute.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">spécifie le nombre d’occurrences de cet élément dans
        le texte qui porte une valeur donnée pour l’attribut global <att>xml:id</att>.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">전반적 <att>xml:id</att> 속성에 대한 분별 값을 포함하는 텍스트 내의 이 요소에
        대한 출현 횟수를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出帶有明確全域屬性<att>xml:id</att>屬性值的元素在文本中的出現次數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">グローバル属性<att>xml:id</att>を持つテキスト中にある当該要素の 出現回数を示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de"> gibt an, wie oft dieses Element mit einem bestimmten
        Wert für das globale Attribut <att>xml:id</att> im Text vorkommt.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el número de veces que este elemento aparece
        en el texto con un valor distintivo apara el atributo global <att>xml:id</att>.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il numero di occorrenze dell'elemento nel
        testo e che reca un valore distinto dall'attributo globale <att>xml:id</att>.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
    </attDef>
  </attList>
  <exemplum versionDate="2016-12-05" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tagUsage-egXML-ec">
      <tagsDecl partial="true">
        <rendition xml:id="it" scheme="css" selector="foreign, hi"> font-style: italic; </rendition>
        <!-- ... -->
        <namespace name="http://www.tei-c.org/ns/1.0">
          <tagUsage gi="hi" occurs="28" withId="2"> Used to mark English words italicized in the copy text.</tagUsage>
          <tagUsage gi="foreign">Used to mark non-English words in the copy text.</tagUsage>
          <!-- ... -->
        </namespace>
      </tagsDecl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tagUsage-egXML-ww" source="#fr-ex-Dufournaud">
      <tagsDecl>
        <rendition xml:id="fr_it">A noter l'emploi d'une variante penchée ou italique dans la fonte
            actuelle.</rendition>
        <namespace name="http://www.tei-c.org/ns/1.0">
          <tagUsage gi="abbr"> Les abréviations étant très courantes et de type
              <term>brevigraph</term> (voir le manuel TEI), l'attribut "type" a cette valeur par
              défaut. Dans les autres cas, ("Sénécial" abrégé par "Sénat") , l'attribut "type " a
              explicitement la valeur "contraction" et l'attribut "expan" contient la forme
              développée.</tagUsage>
          <tagUsage gi="lb">Chaque ligne est numérotée depuis le début du corps de la lettre (sauf
              le titre).</tagUsage>
          <tagUsage gi="lb">Chaque page est numérotée sous la forme d'un numéro de folio suivi de
              "recto" ou "verso". Dans certains cas, le foliotage réel n'est pas celui qui est
              indiqué sur le registre. Dans ce cas, les deux numérotations sont gardées.</tagUsage>
          <tagUsage gi="unclear">Mots difficiles à lire</tagUsage>
          <tagUsage gi="opener">Phrase(s) d'introduction de la lettre.</tagUsage>
          <tagUsage gi="signed">Signature du copiste.</tagUsage>
        </namespace>
      </tagsDecl>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD57"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">element usage</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">usage des balises</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2019-07-08" xml:lang="de">Verwendung eines Elements</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-02-16" xml:lang="en">documents the usage of a specific element within a specified document.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">donne des informations sur l’utilisation d’un élément
    spécifique dans un texte.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트에서 특정 요소의 사용에 관한 정보를 제공한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供文件中某個特定元素的使用資訊。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト中にある特定要素の使い方に関する情報を示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">dokumentiert den Gebrauch eines spezifischen Elements innerhalb
    eines bestimmten Dokuments.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona información sobre el uso de un elemento
    específico al interno del texto.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni circa l'uso di uno specifico
    elemento all'interno di un testo.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datcat"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.limitedContent"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2013-11-20" xml:lang="en">generic identifier</gloss>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">요소 이름</gloss>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">nombre de elemento</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">nom de l'élément</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">nome di elemento</gloss>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2019-07-08" xml:lang="de">generische Kennung</gloss>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2013-11-20" xml:lang="en">specifies the name
      (generic identifier) of the element indicated by the tag,  within the namespace indicated by the parent
        <gi>namespace</gi> element.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">nom (identifiant générique) de l’élément indiqué par
        la balise.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">태그로 제시된 요소의 이름(일반적 확인소)</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">該標籤所指明的元素名稱 (通用識別符碼)。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該タグで示された要素の名前(GI、 共通識別子)。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">gibt den Namen (generische Kennung) des durch das Tag angegebenen Elements innerhalb jenes Namensraums an, 
        der im übergeordneten <gi>namespace</gi>-Element angegeben wird.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">el nombre (identificador genérico) de un elemento
        indicado mediante una etiqueta.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">il nome (identificatore generico) dell'elemento
        indicato dal marcatore.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the number of occurrences of this element within the text.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">spécifie le nombre d’occurrences de cet élément dans
        le texte.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 내부에 이 요소가 출현 횟수를 명시한다.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該元素在文本中出現的次數。</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素が、テキスト中で出現する回数を示す。</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt an, wie oft das Element im Text vorkommt.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el número de veces que un elemento
        determinado aparece en el texto.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il numero di occorrenze dell'elemento nel
        testo.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">with unique identifier</gloss>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">고유한 확인소를 가진</gloss>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">con identificador único</gloss>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">avec identificateur unique</gloss>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">con identificatore unico</gloss>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[6]`.

```xml
<gloss versionDate="2019-07-08" xml:lang="de">mit eindeutiger Kennung</gloss>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the number of occurrences of this element within the text which bear a
        distinct value for the global <att>xml:id</att> attribute.</desc>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">spécifie le nombre d’occurrences de cet élément dans
        le texte qui porte une valeur donnée pour l’attribut global <att>xml:id</att>.</desc>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전반적 <att>xml:id</att> 속성에 대한 분별 값을 포함하는 텍스트 내의 이 요소에
        대한 출현 횟수를 명시한다.</desc>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出帶有明確全域屬性<att>xml:id</att>屬性值的元素在文本中的出現次數。</desc>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">グローバル属性<att>xml:id</att>を持つテキスト中にある当該要素の 出現回数を示す。</desc>
```

^b48

### Block 49

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de"> gibt an, wie oft dieses Element mit einem bestimmten
        Wert für das globale Attribut <att>xml:id</att> im Text vorkommt.</desc>
```

^b49

### Block 50

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el número de veces que este elemento aparece
        en el texto con un valor distintivo apara el atributo global <att>xml:id</att>.</desc>
```

^b50

### Block 51

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il numero di occorrenze dell'elemento nel
        testo e che reca un valore distinto dall'attributo globale <att>xml:id</att>.</desc>
```

^b51

### Block 52

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b52

### Block 53

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2016-12-05" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tagUsage-egXML-ec">
      <tagsDecl partial="true">
        <rendition xml:id="it" scheme="css" selector="foreign, hi"> font-style: italic; </rendition>
        <!-- ... -->
        <namespace name="http://www.tei-c.org/ns/1.0">
          <tagUsage gi="hi" occurs="28" withId="2"> Used to mark English words italicized in the copy text.</tagUsage>
          <tagUsage gi="foreign">Used to mark non-English words in the copy text.</tagUsage>
          <!-- ... -->
        </namespace>
      </tagsDecl>
    </egXML>
  </exemplum>
```

^b53

### Block 54

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tagUsage-egXML-ww" source="#fr-ex-Dufournaud">
      <tagsDecl>
        <rendition xml:id="fr_it">A noter l'emploi d'une variante penchée ou italique dans la fonte
            actuelle.</rendition>
        <namespace name="http://www.tei-c.org/ns/1.0">
          <tagUsage gi="abbr"> Les abréviations étant très courantes et de type
              <term>brevigraph</term> (voir le manuel TEI), l'attribut "type" a cette valeur par
              défaut. Dans les autres cas, ("Sénécial" abrégé par "Sénat") , l'attribut "type " a
              explicitement la valeur "contraction" et l'attribut "expan" contient la forme
              développée.</tagUsage>
          <tagUsage gi="lb">Chaque ligne est numérotée depuis le début du corps de la lettre (sauf
              le titre).</tagUsage>
          <tagUsage gi="lb">Chaque page est numérotée sous la forme d'un numéro de folio suivi de
              "recto" ou "verso". Dans certains cas, le foliotage réel n'est pas celui qui est
              indiqué sur le registre. Dans ce cas, les deux numérotations sont gardées.</tagUsage>
          <tagUsage gi="unclear">Mots difficiles à lire</tagUsage>
          <tagUsage gi="opener">Phrase(s) d'introduction de la lettre.</tagUsage>
          <tagUsage gi="signed">Signature du copiste.</tagUsage>
        </namespace>
      </tagsDecl>
    </egXML>
  </exemplum>
```

^b54

### Block 55

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD57"/>
  </listRef>
```

^b55

