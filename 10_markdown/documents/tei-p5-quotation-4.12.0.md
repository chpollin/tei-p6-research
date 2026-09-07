---
type: representation
source-type: document
source: '[[00_sources/tei-p5-quotation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 quotation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/quotation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# quotation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9512. Git blob: `ba81c0a98f8496a39090ebbff20a347f45d07eb3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-quotation" ident="quotation">
  <gloss versionDate="2007-06-12" xml:lang="en">quotation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">citation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies editorial practice adopted with respect to quotation marks in the original.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit la pratique éditoriale adoptée par rapport aux guillements dans l’original.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원본 인용 부호에 관해 채택한 편집 방식을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">說明在編輯上是如何處理來源文件中的引文符號。</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">元資料にあった引用をどのように編集したのかを示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">beschreibt die editorische Praxis bezüglich der Anführungszeichen im Originaltext.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica las prácticas editoriales adoptadas respecto al entrecomillado en el original.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica le pratiche editoriali rispetto all'uso delle virgolette nell'originale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="quotation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:quotation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="quotationContents" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:quotation">
        <sch:report test="not( @marks )  and  not( tei:p )">
          On &lt;<sch:name/>&gt;, either the @marks attribute should be used, or a paragraph of description provided.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="marks" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">quotation marks</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">인용 부호</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">comillas</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">guillemets</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">punti interrogativi</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether or not quotation marks have been retained as content within the text.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique si les guillemets ont été retenus ou non
        comme faisant partie du texte.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">인용 부호가 텍스트에 유지되었는지 여부를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出引文符號是否在文本中被保留為內容的一部份。</desc>
      <desc versionDate="2008-04-06" xml:lang="ja">テキスト中の内容として、引用符をそのまま残したかどうかを示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">gibt an, ob Anführungszeichen als Bestandteil des
        Textes beibehalten wurden.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si se ha mantenido o no el entrecomillado en
        el texto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se le virglotette siano state mantenute o meno
        all'interno del testo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="none">
          <desc versionDate="2007-06-27" xml:lang="en">no quotation marks have been retained</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">aucun guillemet n’a été retenu.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">인용 부호가 유지되지 않았다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">不保留任何引文符號</desc>
          <desc versionDate="2008-04-06" xml:lang="es">no se ha conservado ningún uso de las comillas</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">引用符は残っていない。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le virgolette non sono state mantenute.</desc>
        </valItem>
        <valItem ident="some">
          <desc versionDate="2007-06-27" xml:lang="en">some quotation marks have been retained</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">quelques guillemetsont été retenues.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">일부의 인용 부호가 유지되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">保留部分引文符號</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se han conservado algunas comillas</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">いくつかの引用符は残っている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alcune virgolette sono state mantenute.</desc>
        </valItem>
        <valItem ident="all">
          <desc versionDate="2007-06-27" xml:lang="en">all quotation marks have been retained</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">tous les guillemets ont été conservés.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">모든 인용 부호가 유지되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">保留所有引文符號</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se han conservado todas las comillas</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">全ての引用符が残っている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutte le virgolette sono state mantenute.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-tj">
      <quotation marks="none">
        <p>No quotation marks have been retained. Instead, the <att>rend</att> attribute on the
            <gi>q</gi> element is used to specify what kinds of quotation mark was used, according
          to the following list: <list type="gloss"><label>dq</label><item>double quotes, open and close</item><label>sq</label><item>single quotes, open and close</item><label>dash</label><item>long dash open, no close</item><label>dg</label><item>double guillemets, open and close</item></list>
            </p>
      </quotation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-zn">
      <quotation marks="none">
        <p>Aucun guillemet n'a été conservé. Au lieu de cela, on a utilisé l'attribut
            <att>rend</att> pour l'élément <gi>q</gi> afin de spécifier quel type de guillemet a été
            utilisé, selon la liste suivante : <list type="gloss"><label>ga</label><item>guillemet allemand</item><label>gd</label><item>guillemet anglais ou guillemet dactylographique </item><label>gf</label><item>guillemet français</item></list>
            </p>
      </quotation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-it">
      <quotation marks="all">
        <p>Tous les guillemets sont maintenus dans le texte et sont représentés par les caractères
            Unicode appropriés.</p>
      </quotation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-dn">
      <quotation marks="none">
        <p>不保留引號，改用元素<gi>q</gi>內的屬性<att>rend</att> 來區分引號的種類，種類如下：<list type="gloss"><label>dq</label><item>雙引號，前後各一</item><label>sq</label><item>單引號，前後各一</item><label>dash</label><item>破折號，僅前面一個</item><label>dg</label><item>雙箭號，前後各一</item></list>
            </p>
      </quotation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-lh">
      <quotation marks="all">
        <p>保留所有引號，以合適的Unicode字形表示。</p>
      </quotation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-wk">
      <quotation marks="all">
        <p>All quotation marks are retained in the text and are represented by appropriate Unicode
          characters.</p>
      </quotation>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">quotation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">citation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies editorial practice adopted with respect to quotation marks in the original.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit la pratique éditoriale adoptée par rapport aux guillements dans l’original.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원본 인용 부호에 관해 채택한 편집 방식을 명시한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明在編輯上是如何處理來源文件中的引文符號。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">元資料にあった引用をどのように編集したのかを示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">beschreibt die editorische Praxis bezüglich der Anführungszeichen im Originaltext.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica las prácticas editoriales adoptadas respecto al entrecomillado en el original.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica le pratiche editoriali rispetto all'uso delle virgolette nell'originale.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="quotation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:quotation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b13

### Block 14

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="quotationContents" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:quotation">
        <sch:report test="not( @marks )  and  not( tei:p )">
          On &lt;<sch:name/>&gt;, either the @marks attribute should be used, or a paragraph of description provided.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">quotation marks</gloss>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">인용 부호</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">comillas</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">guillemets</gloss>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">punti interrogativi</gloss>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether or not quotation marks have been retained as content within the text.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique si les guillemets ont été retenus ou non
        comme faisant partie du texte.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">인용 부호가 텍스트에 유지되었는지 여부를 표시한다.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出引文符號是否在文本中被保留為內容的一部份。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">テキスト中の内容として、引用符をそのまま残したかどうかを示す。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt an, ob Anführungszeichen als Bestandteil des
        Textes beibehalten wurden.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si se ha mantenido o no el entrecomillado en
        el texto.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se le virglotette siano state mantenute o meno
        all'interno del testo.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="none">
          <desc versionDate="2007-06-27" xml:lang="en">no quotation marks have been retained</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">aucun guillemet n’a été retenu.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">인용 부호가 유지되지 않았다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">不保留任何引文符號</desc>
          <desc versionDate="2008-04-06" xml:lang="es">no se ha conservado ningún uso de las comillas</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">引用符は残っていない。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le virgolette non sono state mantenute.</desc>
        </valItem>
        <valItem ident="some">
          <desc versionDate="2007-06-27" xml:lang="en">some quotation marks have been retained</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">quelques guillemetsont été retenues.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">일부의 인용 부호가 유지되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">保留部分引文符號</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se han conservado algunas comillas</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">いくつかの引用符は残っている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alcune virgolette sono state mantenute.</desc>
        </valItem>
        <valItem ident="all">
          <desc versionDate="2007-06-27" xml:lang="en">all quotation marks have been retained</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">tous les guillemets ont été conservés.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">모든 인용 부호가 유지되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">保留所有引文符號</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se han conservado todas las comillas</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">全ての引用符が残っている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutte le virgolette sono state mantenute.</desc>
        </valItem>
      </valList>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-tj">
      <quotation marks="none">
        <p>No quotation marks have been retained. Instead, the <att>rend</att> attribute on the
            <gi>q</gi> element is used to specify what kinds of quotation mark was used, according
          to the following list: <list type="gloss"><label>dq</label><item>double quotes, open and close</item><label>sq</label><item>single quotes, open and close</item><label>dash</label><item>long dash open, no close</item><label>dg</label><item>double guillemets, open and close</item></list>
            </p>
      </quotation>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-zn">
      <quotation marks="none">
        <p>Aucun guillemet n'a été conservé. Au lieu de cela, on a utilisé l'attribut
            <att>rend</att> pour l'élément <gi>q</gi> afin de spécifier quel type de guillemet a été
            utilisé, selon la liste suivante : <list type="gloss"><label>ga</label><item>guillemet allemand</item><label>gd</label><item>guillemet anglais ou guillemet dactylographique </item><label>gf</label><item>guillemet français</item></list>
            </p>
      </quotation>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-it">
      <quotation marks="all">
        <p>Tous les guillemets sont maintenus dans le texte et sont représentés par les caractères
            Unicode appropriés.</p>
      </quotation>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-dn">
      <quotation marks="none">
        <p>不保留引號，改用元素<gi>q</gi>內的屬性<att>rend</att> 來區分引號的種類，種類如下：<list type="gloss"><label>dq</label><item>雙引號，前後各一</item><label>sq</label><item>單引號，前後各一</item><label>dash</label><item>破折號，僅前面一個</item><label>dg</label><item>雙箭號，前後各一</item></list>
            </p>
      </quotation>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-lh">
      <quotation marks="all">
        <p>保留所有引號，以合適的Unicode字形表示。</p>
      </quotation>
    </egXML>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-quotation-egXML-wk">
      <quotation marks="all">
        <p>All quotation marks are retained in the text and are represented by appropriate Unicode
          characters.</p>
      </quotation>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b36

