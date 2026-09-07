---
type: representation
source-type: document
source: '[[00_sources/tei-p5-elementspec-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 elementSpec
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/elementSpec.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# elementSpec

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7509. Git blob: `90ffb914e0e2ff6dd0c930a55ffbe77f2bd15872`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" xml:id="gi-elementSpec" module="tagdocs" ident="elementSpec">
  <gloss versionDate="2007-07-04" xml:lang="en">element specification</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">요소 명시</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">especificación del elemento</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">spécification d'élément</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">specifica dell'elemento</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">documents the structure, content, and purpose of a
  single element type.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">단일 요소 유형의 구조, 내용 및 목적을 기록한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">紀錄單一元素類型的結構、內容、以及用途。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">構造、内容、その要素の目的などを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">documente la structure, le contenu et l'emploi d'un
  élément.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">documenta la estructura, contenido y finalidad de un
  único tipo de elemento.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">documenta struttura, contenuto e scopo di un unico
  tipo di elemento</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="att.namespaceable"/>
    <memberOf key="model.oddDecl"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identSynonyms"/>
        <classRef key="model.descLike"/>
      </alternate>
      <elementRef key="classes" minOccurs="0"/>
      <elementRef key="content" minOccurs="0"/>
      <elementRef key="valList" minOccurs="0"/>
      <elementRef key="constraintSpec" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="attList" minOccurs="0"/>
      <alternate maxOccurs="unbounded" minOccurs="0">
        <elementRef key="model"/>
        <elementRef key="modelGrp"/>
        <elementRef key="modelSequence"/>
      </alternate>
      <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <constraintSpec scheme="schematron" ident="child-constraint-based-on-mode" xml:lang="en">
    <!-- 
         This constraint specification is much like the
         "empty-based-on-mode" for <constraintSpec> itself, which does
         something something similar (in that it is based on @mode),
         but not quite the same.
    -->
    <constraint>
      <sch:rule context="tei:elementSpec[ @mode eq 'delete' ]">
        <sch:report test="child::*">This &lt;elementSpec> element has a @mode of "delete" even though it has child elements. Change the @mode to "add", "change", or "replace", or remove the child elements.</sch:report>
      </sch:rule>
      <sch:rule context="tei:elementSpec[ @mode = ('add','change','replace') ]">
        <sch:assert test="child::* | (@* except (@mode, @ident))">This &lt;elementSpec> element has a @mode of "<sch:value-of select="@mode"/>", but does not have any child elements or schema-changing attributes. Specify child elements, use validUntil=, predeclare=, ns=, or prefix=, or change the @mode to "delete".</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <!-- NOTE: MH added 2026-06-29 per SB for issue #2876.
    Remove the following when valList is removed from the content model. -->
  <constraintSpec ident="child-valList-deprecated" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:elementSpec/tei:valList">
        <sch:report test="true()">
          Use of &lt;valList> as a direct child of &lt;elementSpec> is deprecated
          and will be invalid after 2027-08-31. To express a controlled vocabulary
          as the content model of an element, place the &lt;valList> inside a
          &lt;content> element.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="prefix" usage="opt">
      <desc versionDate="2010-06-23" xml:lang="en">specifies a default prefix which will be
      prepended to all patterns relating to the element, unless otherwise stated.</desc>
      <datatype minOccurs="0"><dataRef key="teidata.xmlName"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementSpec-egXML-vk">
      <elementSpec module="tagdocs" ident="code">
        <gloss/>
        <desc>contains literal code</desc>
        <classes>
          <memberOf key="model.emphLike"/>
        </classes>
        <content>
          <textNode/>
        </content>
        <attList>
          <attDef ident="type" usage="opt">
            <desc>the language of the code</desc>
            <datatype>
              <dataRef key="teidata.enumerated"/>
            </datatype>
          </attDef>
        </attList>
      </elementSpec>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementSpec-egXML-wl">
      <elementSpec module="tagdocs" xml:id="fr_Code" ident="code">
        <desc>contient le code littéral</desc>
        <classes>
          <memberOf key="model.emphLike"/>
        </classes>
        <content>
          <textNode/>
        </content>
        <attList>
          <attDef ident="type" usage="opt">
            <desc>la langue du code</desc>
            <datatype>
              <dataRef key="teidata.enumerated"/>
            </datatype>
          </attDef>
        </attList>
      </elementSpec>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementSpec-egXML-xh">
      <elementSpec module="tagdocs" ident="code">
        <gloss/>
        <desc>包含文字規則</desc>
        <classes>
          <memberOf key="model.emphLike"/>
        </classes>
        <content>
          <textNode/>
        </content>
        <attList>
          <attDef ident="type" usage="opt">
            <desc>規則的表達方式</desc>
            <datatype>
              <dataRef key="teidata.enumerated"/>
            </datatype>
          </attDef>
        </attList>
      </elementSpec>
    </egXML>
  </exemplum>
  <remarks xml:lang="en" versionDate="2026-04-16" validUntil="2027-09-01">
    <p><gi>elementSpec</gi> currently allows <gi>valList</gi> as a direct child,
    but this usage is deprecated and will be removed on 2027-09-01. 
    If a <gi>valList</gi> is used to specify the content model of an element,
    it should be placed inside the <gi>content</gi> child of the 
    <gi>elementSpec</gi>.</p>
  </remarks>
  <listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">element specification</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">요소 명시</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">especificación del elemento</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">spécification d'élément</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">specifica dell'elemento</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">documents the structure, content, and purpose of a
  single element type.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">단일 요소 유형의 구조, 내용 및 목적을 기록한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">紀錄單一元素類型的結構、內容、以及用途。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">構造、内容、その要素の目的などを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">documente la structure, le contenu et l'emploi d'un
  élément.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">documenta la estructura, contenido y finalidad de un
  único tipo de elemento.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">documenta struttura, contenuto e scopo di un unico
  tipo di elemento</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.identified"/>
    <memberOf key="att.namespaceable"/>
    <memberOf key="model.oddDecl"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.identSynonyms"/>
        <classRef key="model.descLike"/>
      </alternate>
      <elementRef key="classes" minOccurs="0"/>
      <elementRef key="content" minOccurs="0"/>
      <elementRef key="valList" minOccurs="0"/>
      <elementRef key="constraintSpec" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="attList" minOccurs="0"/>
      <alternate maxOccurs="unbounded" minOccurs="0">
        <elementRef key="model"/>
        <elementRef key="modelGrp"/>
        <elementRef key="modelSequence"/>
      </alternate>
      <elementRef key="exemplum" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="listRef" minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="child-constraint-based-on-mode" xml:lang="en">
    <!-- 
         This constraint specification is much like the
         "empty-based-on-mode" for <constraintSpec> itself, which does
         something something similar (in that it is based on @mode),
         but not quite the same.
    -->
    <constraint>
      <sch:rule context="tei:elementSpec[ @mode eq 'delete' ]">
        <sch:report test="child::*">This &lt;elementSpec> element has a @mode of "delete" even though it has child elements. Change the @mode to "add", "change", or "replace", or remove the child elements.</sch:report>
      </sch:rule>
      <sch:rule context="tei:elementSpec[ @mode = ('add','change','replace') ]">
        <sch:assert test="child::* | (@* except (@mode, @ident))">This &lt;elementSpec> element has a @mode of "<sch:value-of select="@mode"/>", but does not have any child elements or schema-changing attributes. Specify child elements, use validUntil=, predeclare=, ns=, or prefix=, or change the @mode to "delete".</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="child-valList-deprecated" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:elementSpec/tei:valList">
        <sch:report test="true()">
          Use of &lt;valList> as a direct child of &lt;elementSpec> is deprecated
          and will be invalid after 2027-08-31. To express a controlled vocabulary
          as the content model of an element, place the &lt;valList> inside a
          &lt;content> element.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2010-06-23" xml:lang="en">specifies a default prefix which will be
      prepended to all patterns relating to the element, unless otherwise stated.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="0"><dataRef key="teidata.xmlName"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementSpec-egXML-vk">
      <elementSpec module="tagdocs" ident="code">
        <gloss/>
        <desc>contains literal code</desc>
        <classes>
          <memberOf key="model.emphLike"/>
        </classes>
        <content>
          <textNode/>
        </content>
        <attList>
          <attDef ident="type" usage="opt">
            <desc>the language of the code</desc>
            <datatype>
              <dataRef key="teidata.enumerated"/>
            </datatype>
          </attDef>
        </attList>
      </elementSpec>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementSpec-egXML-wl">
      <elementSpec module="tagdocs" xml:id="fr_Code" ident="code">
        <desc>contient le code littéral</desc>
        <classes>
          <memberOf key="model.emphLike"/>
        </classes>
        <content>
          <textNode/>
        </content>
        <attList>
          <attDef ident="type" usage="opt">
            <desc>la langue du code</desc>
            <datatype>
              <dataRef key="teidata.enumerated"/>
            </datatype>
          </attDef>
        </attList>
      </elementSpec>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-elementSpec-egXML-xh">
      <elementSpec module="tagdocs" ident="code">
        <gloss/>
        <desc>包含文字規則</desc>
        <classes>
          <memberOf key="model.emphLike"/>
        </classes>
        <content>
          <textNode/>
        </content>
        <attList>
          <attDef ident="type" usage="opt">
            <desc>規則的表達方式</desc>
            <datatype>
              <dataRef key="teidata.enumerated"/>
            </datatype>
          </attDef>
        </attList>
      </elementSpec>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks xml:lang="en" versionDate="2026-04-16" validUntil="2027-09-01">
    <p><gi>elementSpec</gi> currently allows <gi>valList</gi> as a direct child,
    but this usage is deprecated and will be removed on 2027-09-01. 
    If a <gi>valList</gi> is used to specify the content model of an element,
    it should be placed inside the <gi>content</gi> child of the 
    <gi>elementSpec</gi>.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TD"/>
  </listRef>
```

^b24

