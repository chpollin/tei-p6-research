---
type: representation
source-type: document
source: '[[00_sources/tei-p5-remarks-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 remarks
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/remarks.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# remarks

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4292. Git blob: `45fdc6e6e000999b7be20dff0223ac8d2d5bbd88`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-remarks" ident="remarks">
  <gloss versionDate="2007-06-12" xml:lang="en">remarks</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">remarques</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains any commentary or discussion about the usage of an element, attribute, class, or entity not otherwise documented within the containing element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">포함 요소 내에서 다르게 기록된 것이 없다면 요소, 속성, 부류 또는 개체의 사용 예에 관한 논평 또는 토론을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何關於元素、屬性、元素集，或實體的使用資訊之評論或討論，該元素、屬性、元素集或實體未以其他方式紀錄在所包含的元素中。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素、属性、クラス、エンティティに関する、まだ文書化されていない解説 や論議を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient tout commentaire sur l'utilisation d'un élément, d'un attribut, d'une classe ou d'une entité qui n'est pas documentée ailleurs à l'intérieur de l'élément conteneur.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier comentario o explicación relativa al uso de elementos, atributos, clases o entitades no documentados de otra manera en el elemento que los contiene.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi commento o discussione relativi all'utilizzo di elementi, attributi, classi o entità non altrimenti documentati nell'elemento che li contiene.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
    <memberOf key="att.translatable"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec scheme="schematron" ident="deprecate-identless-remarks" xml:lang="en" validUntil="2027-06-01">
    <desc type="deprecationInfo">In order to properly allow
    customization of remarks, a &lt;remarks> element must be
    identifiable; thus it needs to have an @ident attribute.</desc>
    <constraint>
      <sch:rule context="tei:remarks">
        <sch:assert test="@ident" role="warning">
          The @ident attribute will be required on &lt;remarks> after 2027-06-01.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="ident" usage="opt">
      <desc versionDate="2025-02-11" xml:lang="en">supplies the identifier by which the remarks may be referenced.</desc>
      <datatype><dataRef key="teidata.name"/></datatype>
      <remarks ident="gi-remarks-attr.ident-remarks" xml:lang="en" versionDate="2026-06-29">
        <!-- "deprecationInfo": -->
        <p>This attribute will become required (rather than optional)
        after 2027-06-01.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-remarks-egXML-ff">
      <remarks>
        <p>This element is probably redundant.</p>
      </remarks>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-remarks-egXML-jo">
      <remarks>
        <p>Cet élément est probablement superflu.</p>
      </remarks>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-remarks-egXML-lb">
      <remarks>
        <p>此元素可能是多餘的</p>
      </remarks>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TDATT"/>
    <ptr target="#TDCLA"/>
    <ptr target="#TDENT"/>
  </listRef>
</elementSpec>

```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">remarks</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">remarques</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains any commentary or discussion about the usage of an element, attribute, class, or entity not otherwise documented within the containing element.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">포함 요소 내에서 다르게 기록된 것이 없다면 요소, 속성, 부류 또는 개체의 사용 예에 관한 논평 또는 토론을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含任何關於元素、屬性、元素集，或實體的使用資訊之評論或討論，該元素、屬性、元素集或實體未以其他方式紀錄在所包含的元素中。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素、属性、クラス、エンティティに関する、まだ文書化されていない解説 や論議を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient tout commentaire sur l'utilisation d'un élément, d'un attribut, d'une classe ou d'une entité qui n'est pas documentée ailleurs à l'intérieur de l'élément conteneur.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier comentario o explicación relativa al uso de elementos, atributos, clases o entitades no documentados de otra manera en el elemento que los contiene.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un qualsiasi commento o discussione relativi all'utilizzo di elementi, attributi, classi o entità non altrimenti documentati nell'elemento che li contiene.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
    <memberOf key="att.translatable"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="deprecate-identless-remarks" xml:lang="en" validUntil="2027-06-01">
    <desc type="deprecationInfo">In order to properly allow
    customization of remarks, a &lt;remarks> element must be
    identifiable; thus it needs to have an @ident attribute.</desc>
    <constraint>
      <sch:rule context="tei:remarks">
        <sch:assert test="@ident" role="warning">
          The @ident attribute will be required on &lt;remarks> after 2027-06-01.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2025-02-11" xml:lang="en">supplies the identifier by which the remarks may be referenced.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.name"/></datatype>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="gi-remarks-attr.ident-remarks" xml:lang="en" versionDate="2026-06-29">
        <!-- "deprecationInfo": -->
        <p>This attribute will become required (rather than optional)
        after 2027-06-01.</p>
      </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-remarks-egXML-ff">
      <remarks>
        <p>This element is probably redundant.</p>
      </remarks>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-remarks-egXML-jo">
      <remarks>
        <p>Cet élément est probablement superflu.</p>
      </remarks>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-remarks-egXML-lb">
      <remarks>
        <p>此元素可能是多餘的</p>
      </remarks>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TDATT"/>
    <ptr target="#TDCLA"/>
    <ptr target="#TDENT"/>
  </listRef>
```

^b19

