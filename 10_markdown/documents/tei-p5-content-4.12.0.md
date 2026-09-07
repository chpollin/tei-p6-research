---
type: representation
source-type: document
source: '[[00_sources/tei-p5-content-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 content
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/content.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# content

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7848. Git blob: `f0814440388496e957d3ed622403f296c36b09ee`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" xmlns:teix="http://www.tei-c.org/ns/Examples" module="tagdocs" xml:id="gi-content" ident="content">
  <gloss versionDate="2007-07-04" xml:lang="en">content model</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">내용 모델</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">模型宣告</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">modèle de contenu</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración del esquema</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione dello schema</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">内容モデル</gloss>
  <desc versionDate="2018-01-20" xml:lang="en">contains a declaration of the intended content model for the element (or other construct) being specified.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">기록된 스키마에 대한 선언 텍스트를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含所記錄之模型的宣告文字。</desc>
  <desc versionDate="2024-02-28" xml:lang="ja">現在の要素（あるいは他の構造）に期待される内容モデルの宣言を含む。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la déclaration d'un modèle de contenu pour le schéma documenté.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el texto de la declaración del esquema utilizado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il testo di una dichiarazione dello schema utilizzato.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      <elementRef key="valList" minOccurs="1" maxOccurs="1"/>
      <classRef key="model.contentPart" minOccurs="1" maxOccurs="1"/>
      <anyElement minOccurs="1" maxOccurs="1" require="http://relaxng.org/ns/compatibility/annotations/1.0 http://relaxng.org/ns/structure/1.0"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="autoPrefix">
      <desc versionDate="2010-05-13" xml:lang="en">controls whether or
      not pattern names generated in the corresponding RELAX NG schema
      source are automatically prefixed to avoid potential
      nameclashes.</desc>
      <desc versionDate="2024-02-28" xml:lang="ja">名前衝突の可能性を避けるために、
        パターン名 [pattern name] 
        に生成元のRELAX NGスキーマソースに応じた接頭辞を自動的に付けるかどうかを制御する。</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
      <defaultVal>true</defaultVal>
      <valList type="closed">
        <valItem ident="true">
          <desc versionDate="2010-05-13" xml:lang="en">Each name
          referenced in e.g. an <gi>rng:ref</gi> element within a
          content model is automatically prefixed by the value of the
          <att>prefix</att> attribute on the current
          <gi>schemaSpec</gi>
          </desc>
          <desc versionDate="2024-02-28" xml:lang="ja">
            参照された個々の名前。
            たとえば、ある内容モデルの中での <gi>rng:ref</gi> 
            要素には自動的にその時点の<gi>schemaSpec</gi>の<att>prefix</att>属性の値が付く。
          </desc>
        </valItem>
        <valItem ident="false">
          <desc versionDate="2010-05-13" xml:lang="en">No prefixes are
          added: any prefix required by the value of the
          <att>prefix</att> attribute on the current
          <gi>schemaSpec</gi> must therefore be supplied explicitly,
          as appropriate.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <p>This sample <gi>content</gi> element indicates that the element
    being specified has no content:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-ha" source="#UND">
      <content><empty/></content>
    </egXML></exemplum>
  <exemplum xml:lang="en">
    <p>This <gi>content</gi> element defines a content model,
    expressed directly in the TEI ODD language, that allows either a
    sequence of paragraphs or a series of <gi>msItem</gi> elements optionally
    preceded by a <gi>summary</gi>: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-xk" source="#UND">
      <content>
        <alternate>
            <classRef key="model.pLike" maxOccurs="unbounded"/>
            <sequence>
              <elementRef key="summary" minOccurs="0" maxOccurs="1"/>
              <elementRef key="msItem" maxOccurs="unbounded"/>
             </sequence>
        </alternate>
      </content>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>This sample <gi>content</gi> element defines a content model,
    expressed in the RELAX NG schema language, that allows either a
    sequence of paragraphs or a series of <gi>msItem</gi> elements optionally
    preceded by a <gi>summary</gi>: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-cc" source="#UND">
      <content>
        <choice xmlns="http://relaxng.org/ns/structure/1.0">
          <oneOrMore>
            <ref name="model.pLike"/>
          </oneOrMore>
          <group>
            <optional>
              <ref name="summary"/>
            </optional>
            <oneOrMore>
              <ref name="msItem"/>
            </oneOrMore>
          </group>
        </choice>
      </content>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p>Ce modèle de
    contenu permet d'introduire une suite de paragraphes ou une suite
    d'éléments <gi>msItem</gi> précédés éventuellement d'un résumé :
    </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-xs" source="#UND">
      <content>
        <choice xmlns="http://relaxng.org/ns/structure/1.0">
          <oneOrMore>
            <ref name="model.pLike"/>
          </oneOrMore>
          <group>
            <optional>
              <ref name="summary"/>
            </optional>
            <oneOrMore>
              <ref name="msItem"/>
            </oneOrMore>
          </group>
        </choice>
      </content>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-yf" source="#UND">
      <content>
        <choice xmlns="http://relaxng.org/ns/structure/1.0">
          <oneOrMore>
            <ref name="model.pLike"/>
          </oneOrMore>
          <group>
            <optional>
              <ref name="summary"/>
            </optional>
            <oneOrMore>
              <ref name="msItem"/>
            </oneOrMore>
          </group>
        </choice>
      </content>
    </egXML>
  </exemplum>
  <remarks ident="content-remarks" versionDate="2023-03-30" xml:lang="en">
    <p>It is required that the <gi>content</gi> element has only one child element. If several RELAX NG elements are desired, they must be wrapped in a <gi>rng:div</gi>.</p>
  </remarks>
  <remarks ident="content-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p><gi>content</gi>要素の子要素を一つだけ持つことが要求される。もし複数のRELAX NG 要素が求められる場合、<gi>rng:div</gi>に含まれるようにしなければならない。</p>
  </remarks>
  
  <listRef>
    <ptr target="#TDTAG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">content model</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">내용 모델</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">模型宣告</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">modèle de contenu</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración del esquema</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione dello schema</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">内容モデル</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-01-20" xml:lang="en">contains a declaration of the intended content model for the element (or other construct) being specified.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기록된 스키마에 대한 선언 텍스트를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含所記錄之模型的宣告文字。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">現在の要素（あるいは他の構造）に期待される内容モデルの宣言を含む。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la déclaration d'un modèle de contenu pour le schéma documenté.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el texto de la declaración del esquema utilizado.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il testo di una dichiarazione dello schema utilizzato.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <elementRef key="valList" minOccurs="1" maxOccurs="1"/>
      <classRef key="model.contentPart" minOccurs="1" maxOccurs="1"/>
      <anyElement minOccurs="1" maxOccurs="1" require="http://relaxng.org/ns/compatibility/annotations/1.0 http://relaxng.org/ns/structure/1.0"/>
    </alternate>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2010-05-13" xml:lang="en">controls whether or
      not pattern names generated in the corresponding RELAX NG schema
      source are automatically prefixed to avoid potential
      nameclashes.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2024-02-28" xml:lang="ja">名前衝突の可能性を避けるために、
        パターン名 [pattern name] 
        に生成元のRELAX NGスキーマソースに応じた接頭辞を自動的に付けるかどうかを制御する。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>true</defaultVal>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="true">
          <desc versionDate="2010-05-13" xml:lang="en">Each name
          referenced in e.g. an <gi>rng:ref</gi> element within a
          content model is automatically prefixed by the value of the
          <att>prefix</att> attribute on the current
          <gi>schemaSpec</gi>
          </desc>
          <desc versionDate="2024-02-28" xml:lang="ja">
            参照された個々の名前。
            たとえば、ある内容モデルの中での <gi>rng:ref</gi> 
            要素には自動的にその時点の<gi>schemaSpec</gi>の<att>prefix</att>属性の値が付く。
          </desc>
        </valItem>
        <valItem ident="false">
          <desc versionDate="2010-05-13" xml:lang="en">No prefixes are
          added: any prefix required by the value of the
          <att>prefix</att> attribute on the current
          <gi>schemaSpec</gi> must therefore be supplied explicitly,
          as appropriate.</desc>
        </valItem>
      </valList>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>This sample <gi>content</gi> element indicates that the element
    being specified has no content:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-ha" source="#UND">
      <content><empty/></content>
    </egXML></exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <p>This <gi>content</gi> element defines a content model,
    expressed directly in the TEI ODD language, that allows either a
    sequence of paragraphs or a series of <gi>msItem</gi> elements optionally
    preceded by a <gi>summary</gi>: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-xk" source="#UND">
      <content>
        <alternate>
            <classRef key="model.pLike" maxOccurs="unbounded"/>
            <sequence>
              <elementRef key="summary" minOccurs="0" maxOccurs="1"/>
              <elementRef key="msItem" maxOccurs="unbounded"/>
             </sequence>
        </alternate>
      </content>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <p>This sample <gi>content</gi> element defines a content model,
    expressed in the RELAX NG schema language, that allows either a
    sequence of paragraphs or a series of <gi>msItem</gi> elements optionally
    preceded by a <gi>summary</gi>: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-cc" source="#UND">
      <content>
        <choice xmlns="http://relaxng.org/ns/structure/1.0">
          <oneOrMore>
            <ref name="model.pLike"/>
          </oneOrMore>
          <group>
            <optional>
              <ref name="summary"/>
            </optional>
            <oneOrMore>
              <ref name="msItem"/>
            </oneOrMore>
          </group>
        </choice>
      </content>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p>Ce modèle de
    contenu permet d'introduire une suite de paragraphes ou une suite
    d'éléments <gi>msItem</gi> précédés éventuellement d'un résumé :
    </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-xs" source="#UND">
      <content>
        <choice xmlns="http://relaxng.org/ns/structure/1.0">
          <oneOrMore>
            <ref name="model.pLike"/>
          </oneOrMore>
          <group>
            <optional>
              <ref name="summary"/>
            </optional>
            <oneOrMore>
              <ref name="msItem"/>
            </oneOrMore>
          </group>
        </choice>
      </content>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-content-egXML-yf" source="#UND">
      <content>
        <choice xmlns="http://relaxng.org/ns/structure/1.0">
          <oneOrMore>
            <ref name="model.pLike"/>
          </oneOrMore>
          <group>
            <optional>
              <ref name="summary"/>
            </optional>
            <oneOrMore>
              <ref name="msItem"/>
            </oneOrMore>
          </group>
        </choice>
      </content>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="content-remarks" versionDate="2023-03-30" xml:lang="en">
    <p>It is required that the <gi>content</gi> element has only one child element. If several RELAX NG elements are desired, they must be wrapped in a <gi>rng:div</gi>.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="content-remarks" versionDate="2024-08-08" xml:lang="ja">
    <p><gi>content</gi>要素の子要素を一つだけ持つことが要求される。もし複数のRELAX NG 要素が求められる場合、<gi>rng:div</gi>に含まれるようにしなければならない。</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
  </listRef>
```

^b29

