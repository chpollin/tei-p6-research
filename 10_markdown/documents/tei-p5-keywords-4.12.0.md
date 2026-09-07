---
type: representation
source-type: document
source: '[[00_sources/tei-p5-keywords-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 keywords
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/keywords.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# keywords

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6454. Git blob: `fcc5f16ef8feb77b491ad246477b6759ba402004`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-keywords" ident="keywords">
  <gloss versionDate="2009-04-28" xml:lang="en">keywords</gloss>
  <gloss versionDate="2009-04-28" xml:lang="fr">mot clé</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Schlagwörter</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a list of keywords or phrases identifying the topic or nature of a text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient une liste de mots clés ou d’expressions
    décrivant la nature ou le sujet d’un texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 주제 또는 특성을 식별하는 주제어 또는 구의 목록을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含標明文件主題或性質的關鍵詞或字詞列表。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキストの話題や性格を特定するキーワードや句のリストを示す。</desc>
    <desc versionDate="2016-11-24" xml:lang="de">enthält eine Zusammenstellung von Schlagwörtern oder Phrasen zur Art oder Thematik des Textes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una lista de palabras clave o sintagmas que
    identifican la temática o la naturaleza del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una lista delle parole chiave o frasi che
    identificano l'argomento o la natura di un testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      <elementRef key="term" minOccurs="1" maxOccurs="unbounded"/>      
      <elementRef key="list"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="scheme" usage="opt">
      <desc versionDate="2016-11-04" xml:lang="en">identifies the controlled vocabulary within which the set of keywords concerned is
        defined, for example by a <gi>taxonomy</gi> element, or by
      some other resource.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">désigne la liste close de mots dans lequel l'ensemble
        des mots-clés concernés est défini.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">관련 키워드 집합이 정의된 통제 어휘를 식별하며, 이 정의는 통제 어휘 내에서 수행된다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明相關關鍵詞所使用到的詞彙範圍。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該キーワードリストが定義されている統制語彙を示す。</desc>
        <desc versionDate="2016-11-24" xml:lang="de">gibt das kontrollierte Vokabular an, in dem die benutzten Schlagwörter 
            definiert sind. Dabei kann das <att>scheme</att>-Attribut auf ein <gi>taxonomy</gi>-Element oder eine andere Ressource verweisen.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">identifican el vocabulario con el que se define el
        conjunto de palabras clave referidas.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">identifica il vocabolario controllato all'interno del
        quale sono definite le parole chiave.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-keywords-egXML-zh">
      <keywords scheme="http://classificationweb.net">
        <term>Babbage, Charles</term>
        <term>Mathematicians - Great Britain - Biography</term>
      </keywords>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-keywords-egXML-lg">
      <keywords>
        <term>Fermented beverages</term>
        <term>Central Andes</term>
        <term>Schinus molle</term>
        <term>Molle beer</term>
        <term>Indigenous peoples</term>
        <term>Ethnography</term>
        <term>Archaeology</term>
      </keywords>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-keywords-egXML-dn">
      <keywords scheme="#fr_RAMEAU">
        <term>Littérature française -- 20ème siècle -- Histoire et critique</term>
        <term>Littérature française -- Histoire et critique -- Théorie, etc.</term>
        <term>Français (langue) -- Style -- Bases de données.</term>
      </keywords>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-keywords-egXML-wx">
      <keywords scheme="http://classificationweb.net">
        <term>李白</term>
        <term>詩人 - 唐代 - 傳記</term>
      </keywords>
    </egXML>
  </exemplum>
  <remarks ident="keywords-remarks" versionDate="2012-08-09" xml:lang="en">
    <p>Each individual  keyword (including compound subject headings) should
be supplied as a <gi>term</gi> element directly within the
<gi>keywords</gi>  element. An alternative usage, in which each
<gi>term</gi> appears within an <gi>item</gi> inside a <gi>list</gi> is
permitted for backwards compatibility, but is deprecated.</p>
    <p>If no control list exists for the keywords used, then no value
should be supplied for the <att>scheme</att> attribute.</p>
  </remarks>
  <remarks ident="keywords-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>Jedes einzelne Schlagwort (zusammengesetzte Themen-Schlagwörter eingeschlossen) 
          sollte als <gi>term</gi>-Element direkt im <gi>keywords</gi>-Element notiert werden. 
          Aus Gründen der Rückwärtskompatibilität ist es zwar auch erlaubt, ein <gi>term</gi>-Element 
          in einem <gi>item</gi>-Element zu notieren, das wiederum Kindelement eines <gi>list</gi>-Elementes ist. 
          Allerdings ist dieses Vorgehen veraltet und wird daher nicht empfohlen.</p>
      <p>Wenn keine kontrollierte Liste für die verwendeten Schlagwörter existiert, sollte das <att>scheme</att>-Attribute nicht gesetzt werden.</p>
  </remarks>
  <listRef>
    <ptr target="#HD43"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-04-28" xml:lang="en">keywords</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-28" xml:lang="fr">mot clé</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Schlagwörter</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a list of keywords or phrases identifying the topic or nature of a text.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient une liste de mots clés ou d’expressions
    décrivant la nature ou le sujet d’un texte.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 주제 또는 특성을 식별하는 주제어 또는 구의 목록을 포함한다.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含標明文件主題或性質的關鍵詞或字詞列表。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキストの話題や性格を特定するキーワードや句のリストを示す。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">enthält eine Zusammenstellung von Schlagwörtern oder Phrasen zur Art oder Thematik des Textes.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una lista de palabras clave o sintagmas que
    identifican la temática o la naturaleza del texto.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una lista delle parole chiave o frasi che
    identificano l'argomento o la natura di un testo.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <elementRef key="term" minOccurs="1" maxOccurs="unbounded"/>      
      <elementRef key="list"/>
    </alternate>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2016-11-04" xml:lang="en">identifies the controlled vocabulary within which the set of keywords concerned is
        defined, for example by a <gi>taxonomy</gi> element, or by
      some other resource.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">désigne la liste close de mots dans lequel l'ensemble
        des mots-clés concernés est défini.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">관련 키워드 집합이 정의된 통제 어휘를 식별하며, 이 정의는 통제 어휘 내에서 수행된다.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明相關關鍵詞所使用到的詞彙範圍。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該キーワードリストが定義されている統制語彙を示す。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">gibt das kontrollierte Vokabular an, in dem die benutzten Schlagwörter 
            definiert sind. Dabei kann das <att>scheme</att>-Attribut auf ein <gi>taxonomy</gi>-Element oder eine andere Ressource verweisen.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifican el vocabulario con el que se define el
        conjunto de palabras clave referidas.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica il vocabolario controllato all'interno del
        quale sono definite le parole chiave.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-keywords-egXML-zh">
      <keywords scheme="http://classificationweb.net">
        <term>Babbage, Charles</term>
        <term>Mathematicians - Great Britain - Biography</term>
      </keywords>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-keywords-egXML-lg">
      <keywords>
        <term>Fermented beverages</term>
        <term>Central Andes</term>
        <term>Schinus molle</term>
        <term>Molle beer</term>
        <term>Indigenous peoples</term>
        <term>Ethnography</term>
        <term>Archaeology</term>
      </keywords>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-keywords-egXML-dn">
      <keywords scheme="#fr_RAMEAU">
        <term>Littérature française -- 20ème siècle -- Histoire et critique</term>
        <term>Littérature française -- Histoire et critique -- Théorie, etc.</term>
        <term>Français (langue) -- Style -- Bases de données.</term>
      </keywords>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-keywords-egXML-wx">
      <keywords scheme="http://classificationweb.net">
        <term>李白</term>
        <term>詩人 - 唐代 - 傳記</term>
      </keywords>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="keywords-remarks" versionDate="2012-08-09" xml:lang="en">
    <p>Each individual  keyword (including compound subject headings) should
be supplied as a <gi>term</gi> element directly within the
<gi>keywords</gi>  element. An alternative usage, in which each
<gi>term</gi> appears within an <gi>item</gi> inside a <gi>list</gi> is
permitted for backwards compatibility, but is deprecated.</p>
    <p>If no control list exists for the keywords used, then no value
should be supplied for the <att>scheme</att> attribute.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="keywords-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>Jedes einzelne Schlagwort (zusammengesetzte Themen-Schlagwörter eingeschlossen) 
          sollte als <gi>term</gi>-Element direkt im <gi>keywords</gi>-Element notiert werden. 
          Aus Gründen der Rückwärtskompatibilität ist es zwar auch erlaubt, ein <gi>term</gi>-Element 
          in einem <gi>item</gi>-Element zu notieren, das wiederum Kindelement eines <gi>list</gi>-Elementes ist. 
          Allerdings ist dieses Vorgehen veraltet und wird daher nicht empfohlen.</p>
      <p>Wenn keine kontrollierte Liste für die verwendeten Schlagwörter existiert, sollte das <att>scheme</att>-Attribute nicht gesetzt werden.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD43"/>
  </listRef>
```

^b29

