---
type: representation
source-type: document
source: '[[00_sources/tei-p5-anyelement-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 anyElement
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/anyElement.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# anyElement

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4990. Git blob: `1dc12c957a3e590db1d65a27f6e537564f63ee79`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" 
     schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-anyElement" ident="anyElement">
   <desc versionDate="2016-07-01" xml:lang="en">indicates the presence
   of any elements in a content model.</desc>
  <desc versionDate="2019-02-13" xml:lang="ja">コンテンツモデル内のあらゆる要素の存在を示す。</desc>
   <classes>     
     <memberOf key="att.global"/>
     <memberOf key="att.repeatable"/>     
     <memberOf key="model.contentPart"/>     
   </classes>
  <content><empty/></content>  
  <attList org="choice">
    <attDef ident="require">
      <desc versionDate="2016-11-28" xml:lang="en">supplies a list of namespaces to one of which the
        permitted elements must belong.</desc>
      <desc versionDate="2018-12-28" xml:lang="ja">許可された要素が属していなければならない名前空間のリストを提供する。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.namespace"/>
      </datatype>
    </attDef>
    <attDef ident="except">
      <desc versionDate="2016-11-28" xml:lang="en">supplies a list of namespaces or prefixed element 
        names which are not permitted.</desc>
      <desc versionDate="2018-12-28" xml:lang="ja">許可されていない名前空間または接頭辞付きの要素名のリストを提供する。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.namespaceOrName"/>
      </datatype>
      <remarks ident="anyElement-attr.except-remarks" versionDate="2017-05-11" xml:lang="en">
        <p>When RELAX NG DTD Compatibility Mode is turned on,
        validation requires that any elements which may take an
        <att>xml:id</att> be excluded from the content of
        <ident>anyName</ident> name classes. For normal TEI purposes,
        this includes anything in the TEI namespace and the
        <gi>egXML</gi> element. Default elements and namespaces to be
        excluded are set on the <att>defaultExceptions</att> attribute
        of the <gi>schemaSpec</gi>. <att>except</att> may be used when
        the exceptions need to be locally specified. Element prefixes
        must be declared using a namespace declaration on the parent
        or an ancestor element.</p>
      </remarks>
      <remarks ident="anyElement-attr.except-remarks" versionDate="2018-12-28" xml:lang="ja"><p>RELAX NG DTD互換モードが有効になっている場合、<att>xml:id</att>を<ident>anyName</ident>ネームクラスのコンテンツから除外する要素が必要。通常のTEIの目的では、これにはTEI名前空間と<gi> egXML</gi>要素のすべてが含まれる。除外されるデフォルトの要素と名前空間は、<gi>schemaSpec</gi>の<att>defaultExceptions</att>属性で設定される。例外をローカルに指定する必要がある場合は、<att>except</att>を使用できる。要素接頭辞は、親要素または祖先要素の名前空間宣言を使用して宣言する必要がある。</p></remarks>
    </attDef>
  </attList>
   
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-anyElement-egXML-vg" source="#UND">
      <content>
        <anyElement except="http://www.tei-c.org/ns/1.0"/>
      </content>
    </egXML>
    <p>This  <gi>content</gi> element permits one occurrence of any element which 
      does not belong to the TEI namespace.</p>
  </exemplum>
  
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-anyElement-egXML-dn" source="#UND">
      <content>
        <anyElement minOccurs="1" maxOccurs="unbounded" require="http://www.w3.org/1998/Math/MathML http://www.tei-c.org/ns/Examples/1.0"/>
      </content>
    </egXML>
    <p>This  <gi>content</gi> element permits one or more elements which 
      belong either to the MathML namespace or to the TEI examples namespace.</p>
  </exemplum>
  
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-anyElement-egXML-xb" source="#UND">
      <content>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <textNode/>
          <anyElement require="http://www.tei-c.org/ns/Examples/1.0"/>       
        </alternate>
      </content>
    </egXML>
    <p>This  <gi>content</gi> element permits one or more children which are
      either text nodes or elements from the TEI examples namespace. It is the equivalent of the content model <code>ANY</code>
    in an XML DTD using the TEI All schema.</p>
  </exemplum>
  
 <listRef>
    <ptr target="#TD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2016-07-01" xml:lang="en">indicates the presence
   of any elements in a content model.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2019-02-13" xml:lang="ja">コンテンツモデル内のあらゆる要素の存在を示す。</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>     
     <memberOf key="att.global"/>
     <memberOf key="att.repeatable"/>     
     <memberOf key="model.contentPart"/>     
   </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2016-11-28" xml:lang="en">supplies a list of namespaces to one of which the
        permitted elements must belong.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">許可された要素が属していなければならない名前空間のリストを提供する。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.namespace"/>
      </datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2016-11-28" xml:lang="en">supplies a list of namespaces or prefixed element 
        names which are not permitted.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2018-12-28" xml:lang="ja">許可されていない名前空間または接頭辞付きの要素名のリストを提供する。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded">
        <dataRef key="teidata.namespaceOrName"/>
      </datatype>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="anyElement-attr.except-remarks" versionDate="2017-05-11" xml:lang="en">
        <p>When RELAX NG DTD Compatibility Mode is turned on,
        validation requires that any elements which may take an
        <att>xml:id</att> be excluded from the content of
        <ident>anyName</ident> name classes. For normal TEI purposes,
        this includes anything in the TEI namespace and the
        <gi>egXML</gi> element. Default elements and namespaces to be
        excluded are set on the <att>defaultExceptions</att> attribute
        of the <gi>schemaSpec</gi>. <att>except</att> may be used when
        the exceptions need to be locally specified. Element prefixes
        must be declared using a namespace declaration on the parent
        or an ancestor element.</p>
      </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="anyElement-attr.except-remarks" versionDate="2018-12-28" xml:lang="ja"><p>RELAX NG DTD互換モードが有効になっている場合、<att>xml:id</att>を<ident>anyName</ident>ネームクラスのコンテンツから除外する要素が必要。通常のTEIの目的では、これにはTEI名前空間と<gi> egXML</gi>要素のすべてが含まれる。除外されるデフォルトの要素と名前空間は、<gi>schemaSpec</gi>の<att>defaultExceptions</att>属性で設定される。例外をローカルに指定する必要がある場合は、<att>except</att>を使用できる。要素接頭辞は、親要素または祖先要素の名前空間宣言を使用して宣言する必要がある。</p></remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-anyElement-egXML-vg" source="#UND">
      <content>
        <anyElement except="http://www.tei-c.org/ns/1.0"/>
      </content>
    </egXML>
    <p>This  <gi>content</gi> element permits one occurrence of any element which 
      does not belong to the TEI namespace.</p>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-anyElement-egXML-dn" source="#UND">
      <content>
        <anyElement minOccurs="1" maxOccurs="unbounded" require="http://www.w3.org/1998/Math/MathML http://www.tei-c.org/ns/Examples/1.0"/>
      </content>
    </egXML>
    <p>This  <gi>content</gi> element permits one or more elements which 
      belong either to the MathML namespace or to the TEI examples namespace.</p>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-anyElement-egXML-xb" source="#UND">
      <content>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <textNode/>
          <anyElement require="http://www.tei-c.org/ns/Examples/1.0"/>       
        </alternate>
      </content>
    </egXML>
    <p>This  <gi>content</gi> element permits one or more children which are
      either text nodes or elements from the TEI examples namespace. It is the equivalent of the content model <code>ANY</code>
    in an XML DTD using the TEI All schema.</p>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TD"/>
  </listRef>
```

^b16

