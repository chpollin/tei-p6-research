---
type: representation
source-type: document
source: '[[00_sources/tei-p5-oref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 oRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/oRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# oRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7186. Git blob: `a401bc838e982548da07d1bd39d241ebf1f00d97`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-oRef" ident="oRef">
  <gloss versionDate="2005-01-14" xml:lang="en">orthographic-form reference</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">철자-형태 참조</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">拼字參照</gloss>
  <gloss versionDate="2009-04-08" xml:lang="fr">référence à la forme orthographique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">referencia ortografía</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">riferimento alla forma ortografica</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">in a dictionary example, indicates a reference to the orthographic form(s) of the headword.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전 예문에서 표제어의 철자 형식에 대한 참조를 나타낸다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在字典範例中，參照出標題字的拼字形式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書の用例において、見出し語の正書形式への参照を示す。</desc>
  <desc versionDate="2009-04-08" xml:lang="fr">dans un exemple de dictionnaire, indique une référence à
    la/aux forme(s) orthographique(s) du mot-vedette.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">en un diccionario, indica la forma ortográfica de un
    lema.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">nell'esempio in un dizionario, indica un riferimento alla
    forma (forme) ortografica del lemma.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.ptrLike.form"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <classRef key="model.gLike"/>
      <elementRef key="oRef"/>
    </alternate>  
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates the kind of typographic modification made to the headword in the reference.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">참조에서 표제어에 대한 인쇄상 변화의 종류를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出為參照出標題字所做的印刷修飾。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">参照中、見出し語に施された印刷上の修飾の種類を示す。</desc>
      <desc versionDate="2009-04-08" xml:lang="fr">indique le type de modification typographique
        apportée au mot-vedette dans la référence.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el tipo de modificación tipográfica hecha en
        el lema en la referencia.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il tipo di modifica tipografica del lemma in
        un riferimento.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="cap">
          <gloss versionDate="2007-07-04" xml:lang="en">capital</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">대문자</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">capitale</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">maiuscola</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">indicates first letter is given as capital</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">첫 문자가 대문자임을 표시한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">首字母大寫</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">冒頭文字が大文字化されている。</desc>
          <desc versionDate="2009-04-08" xml:lang="fr">indique que la première lettre est donnée en
            majuscule</desc>
          <desc versionDate="2007-05-04" xml:lang="es">indica la primera letra dada como mayúscula</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che la prima lettera è data come
            maiuscola.</desc>
        </valItem>
        <valItem ident="noHyph">
          <gloss versionDate="2007-07-04" xml:lang="en">no hyphen</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">하이픈 없음</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">ningún guión</gloss>
          <gloss versionDate="2009-04-08" xml:lang="fr">pas de trait d'union</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">nessun trattino</gloss>
          <desc versionDate="2007-07-04" xml:lang="en">indicates that the headword, though a prefix or suffix, loses its hyphen</desc>
          <desc versionDate="2007-11-06" xml:lang="it">indica che il lemma, sebbene prefisso o suffisso,
            perde il trattino</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">접두사 또는 접미사일지라도 표제어의 하이픈이 소실되었음을 표시한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que el lema, aunque sea un prefijo o un
            sufijo, no contiene su guión</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">見出し語には接頭辞、接尾辞が付いているが、ハイフンが外されて いる。</desc>
          <desc versionDate="2009-04-08" xml:lang="fr">indique que le mot-vedette perd son trait d'union, bien
            que ce mot-vedette soit un préfixe ou un suffixe.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-oRef-egXML-ev">
      <entry>
        <form>
          <orth>academy</orth>
        </form>
        <cit type="example">
          <quote>The Royal <oRef type="cap"/> of Arts</quote>
        </cit>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-oRef-egXML-co" source="#fr-ex-Giono-Regain">
      <entry>
        <form>
          <orth>fait-tout</orth>
        </form>
        <cit type="example">
          <quote>
            <q>Des casseroles et des "<oRef type="noHyph"/>faitouts" pour les ménagères.</q>
          </quote>
        </cit>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-oRef-egXML-qk">
      <entry>
        <form>
          <orth>學院</orth>
        </form>
        <cit type="example">
          <quote>皇家藝術<oRef/>
               </quote>
        </cit>
      </entry>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DIHW"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">orthographic-form reference</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">철자-형태 참조</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">拼字參照</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-04-08" xml:lang="fr">référence à la forme orthographique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">referencia ortografía</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">riferimento alla forma ortografica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">in a dictionary example, indicates a reference to the orthographic form(s) of the headword.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전 예문에서 표제어의 철자 형식에 대한 참조를 나타낸다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在字典範例中，參照出標題字的拼字形式。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書の用例において、見出し語の正書形式への参照を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-08" xml:lang="fr">dans un exemple de dictionnaire, indique une référence à
    la/aux forme(s) orthographique(s) du mot-vedette.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">en un diccionario, indica la forma ortográfica de un
    lema.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">nell'esempio in un dizionario, indica un riferimento alla
    forma (forme) ortografica del lemma.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.notated"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.ptrLike.form"/>
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
      <elementRef key="oRef"/>
    </alternate>  
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the kind of typographic modification made to the headword in the reference.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참조에서 표제어에 대한 인쇄상 변화의 종류를 표시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出為參照出標題字所做的印刷修飾。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">参照中、見出し語に施された印刷上の修飾の種類を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-04-08" xml:lang="fr">indique le type de modification typographique
        apportée au mot-vedette dans la référence.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el tipo de modificación tipográfica hecha en
        el lema en la referencia.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il tipo di modifica tipografica del lemma in
        un riferimento.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="cap">
          <gloss versionDate="2007-07-04" xml:lang="en">capital</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">대문자</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">capitale</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">maiuscola</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">indicates first letter is given as capital</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">첫 문자가 대문자임을 표시한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">首字母大寫</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">冒頭文字が大文字化されている。</desc>
          <desc versionDate="2009-04-08" xml:lang="fr">indique que la première lettre est donnée en
            majuscule</desc>
          <desc versionDate="2007-05-04" xml:lang="es">indica la primera letra dada como mayúscula</desc>
          <desc versionDate="2007-01-21" xml:lang="it">indica che la prima lettera è data come
            maiuscola.</desc>
        </valItem>
        <valItem ident="noHyph">
          <gloss versionDate="2007-07-04" xml:lang="en">no hyphen</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">하이픈 없음</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">ningún guión</gloss>
          <gloss versionDate="2009-04-08" xml:lang="fr">pas de trait d'union</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">nessun trattino</gloss>
          <desc versionDate="2007-07-04" xml:lang="en">indicates that the headword, though a prefix or suffix, loses its hyphen</desc>
          <desc versionDate="2007-11-06" xml:lang="it">indica che il lemma, sebbene prefisso o suffisso,
            perde il trattino</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">접두사 또는 접미사일지라도 표제어의 하이픈이 소실되었음을 표시한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">indica que el lema, aunque sea un prefijo o un
            sufijo, no contiene su guión</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">見出し語には接頭辞、接尾辞が付いているが、ハイフンが外されて いる。</desc>
          <desc versionDate="2009-04-08" xml:lang="fr">indique que le mot-vedette perd son trait d'union, bien
            que ce mot-vedette soit un préfixe ou un suffixe.</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-oRef-egXML-ev">
      <entry>
        <form>
          <orth>academy</orth>
        </form>
        <cit type="example">
          <quote>The Royal <oRef type="cap"/> of Arts</quote>
        </cit>
      </entry>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-oRef-egXML-co" source="#fr-ex-Giono-Regain">
      <entry>
        <form>
          <orth>fait-tout</orth>
        </form>
        <cit type="example">
          <quote>
            <q>Des casseroles et des "<oRef type="noHyph"/>faitouts" pour les ménagères.</q>
          </quote>
        </cit>
      </entry>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-oRef-egXML-qk">
      <entry>
        <form>
          <orth>學院</orth>
        </form>
        <cit type="example">
          <quote>皇家藝術<oRef/>
               </quote>
        </cit>
      </entry>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIHW"/>
  </listRef>
```

^b28

