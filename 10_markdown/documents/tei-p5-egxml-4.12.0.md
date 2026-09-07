---
type: representation
source-type: document
source: '[[00_sources/tei-p5-egxml-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 egXML
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/egXML.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# egXML

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7870. Git blob: `d62653dd72547a1af0fd642ee5753e944d09f734`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" ns="http://www.tei-c.org/ns/Examples" xml:id="gi-egXML" ident="egXML">
  <gloss versionDate="2007-07-04" xml:lang="en">example of XML</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">XML의 예</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">ejemplo de XML</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">exemple en XML</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">esempio di XML</gloss>
  <desc versionDate="2017-02-07" xml:lang="en">a single XML fragment demonstrating the use of some XML, such as 
    elements, attributes, or processing instructions, etc., in which the <gi>egXML</gi> element functions as the 
    root element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 XML 요소 또는 속성의 사용을 나타내는 정형의 단일 XML 예를 포함하며,
    <gi>egXML</gi>는 뿌리(최상위) 요소로 기능한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含形式完整的單一XML範例的根結構，用以說明某些XML元素或屬性的使用方法。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素や属性の使用例を示す、整形式XMLデータによる用例をひとつ含む。要
    素<gi>egXML</gi>が当該用例の根要素になる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un seul exemple en XML bien formé montrant
    l'utilisation d'un élément ou d'un attribut XML.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">constituye la raíz de un único ejemplo bien formado según
    el lenguaje XML que ilustra el uso de un elemento o un atributo XML.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un unico esempio ben formato secondo il
    linguaggio XML che illustra l'impiego di un elemento o attributo XML</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.egLike"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <anyElement/>
    </alternate>
  </content>
  <attList>
    <attDef ident="valid">
      <desc versionDate="2011-01-30" xml:lang="en">indicates the intended validity of the example with respect to
a schema.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>true</defaultVal>
      <valList type="closed">
        <valItem ident="true">
          <desc versionDate="2011-12-04" xml:lang="en">the example is intended to be fully valid,
assuming that its root element, or a provided root element, 
could have been used as a possible root element in the schema concerned.</desc>
        </valItem>
        <valItem ident="feasible">
          <desc versionDate="2011-12-04" xml:lang="en">the example could be transformed into
a valid document by inserting any number of valid attributes and child
elements anywhere within it; or it is valid against a version of the
schema concerned in which the provision of character data, list, element, or attribute
values has been made optional.</desc>
        </valItem>
        <valItem ident="false">
          <desc versionDate="2011-01-30" xml:lang="en">the example is not intended to be valid,
and contains deliberate errors.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples">
<egXML>
<div>
    <head>A slide about <gi>egXML</gi></head>
    <list>
     <item><gi>egXML</gi> can be used to give XML examples in the TEI
Examples namespace</item>
     <item>Attributes values for <att>valid</att>:
      <list rend="collapsed">
      <item><val rend="green">true</val>: intended to be fully
valid</item>
      <item><val rend="amber">feasible</val>: valid if missing nodes
provided</item>
      <item><val rend="red">false</val>: not intended to be valid</item>
      </list>
      </item>
      <item>The <att>rend</att>  attribute can be
        used for recording how parts of the example were rendered.</item>
      </list>
</div>
</egXML>

  </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-egXML-egXML-rw" xml:lang="und" valid="feasible" source="#UND">
      
      <egXML valid="feasible" source="#UND">
       <text>
       <front><!-- front matter for the whole group --></front>
       <group>
       <text>
       <!-- first text -->
       </text>
       <text>
       <!-- second text -->
       </text>
       </group>
      </text>
      <!-- This example is not valid TEI, but could be made so by
      adding missing components -->

    </egXML>
    </egXML>
  </exemplum>

  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-egXML-egXML-gn" xml:lang="und" valid="false">
      &lt;egXML xmlns="http://www.tei-c.org/ns/Examples" valid="false"&gt;
         &lt;para xml:lang="en"&gt;Doubloons are a pirate's best friend&lt;/para&gt;
      &lt;/egXML&gt;
    </egXML>
  </exemplum>

  <remarks ident="egXML-remarks" versionDate="2011-12-05" xml:lang="en">
    <p>In the source of the TEI Guidelines, this element declares itself and its content as
      belonging to the namespace <ident type="ns">http://www.tei-c.org/ns/Examples</ident>. This
      enables the content of the element to be validated independently against the TEI scheme. Where
      this element is used outside this context, a different namespace or none at all may be
      preferable. The content must however be a well-formed XML fragment or document: where this is
      not the case, the more general <gi>eg</gi> element should be used in preference. <!-- JC: Commenting out 
      on 2018-01-19 until real mechanism agreed --> <!--In a TEI context 
      use of the <att>rend</att> attribute in the TEI namespace, as opposed to the TEI Examples namespace, 
      enables recording of rendition information.-->
    </p>
  </remarks>
  <remarks ident="egXML-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans la source des principes directeurs de la TEI, cet élément se déclare lui-même, ainsi que
      son contenu, comme appartenant à l'espace de noms <ident type="ns">http://www.tei-c.org/ns/Examples</ident>. Cela permet au contenu de l'élément d'être validé
      indépendamment du schéma TEI. Lorsque cet élément est utilisé hors de ce contexte, il peut
      s'avérer préférable de mettre un espace de noms différent ou pas d'espace de nom du tout. Le
      contenu doit cependant être un document ou un fragment en XML bien formé : si ce n'est pas le
      cas, on utilisera plutôt l'élément plus général <gi>eg</gi> .</p>
  </remarks>
  <remarks ident="egXML-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> TEIガイドラインでは、当該要素とその内容は、名前区間 <ident type="ns">http://www.tei-c.org/ns/Examples</ident>
      で宣言されているとする。これにより、TEIスキームとは関係なく、当該 要素の内容は妥当とされる。当該要素が、これ以外の意味で使用される場
      合には、異なる名前空間を使用することが望ましいだろう。 当該要素の内容は、整形式XMLデータでなければならない。そうでない場
      合は、より一般的な要素<gi>eg</gi>を使用すべきである。 </p>
  </remarks>
  <listRef>
    <ptr target="#TDphraseTE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">example of XML</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">XML의 예</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">ejemplo de XML</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">exemple en XML</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">esempio di XML</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">a single XML fragment demonstrating the use of some XML, such as 
    elements, attributes, or processing instructions, etc., in which the <gi>egXML</gi> element functions as the 
    root element.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 XML 요소 또는 속성의 사용을 나타내는 정형의 단일 XML 예를 포함하며,
    <gi>egXML</gi>는 뿌리(최상위) 요소로 기능한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含形式完整的單一XML範例的根結構，用以說明某些XML元素或屬性的使用方法。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素や属性の使用例を示す、整形式XMLデータによる用例をひとつ含む。要
    素<gi>egXML</gi>が当該用例の根要素になる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un seul exemple en XML bien formé montrant
    l'utilisation d'un élément ou d'un attribut XML.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">constituye la raíz de un único ejemplo bien formado según
    el lenguaje XML que ilustra el uso de un elemento o un atributo XML.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un unico esempio ben formato secondo il
    linguaggio XML che illustra l'impiego di un elemento o attributo XML</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.egLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <textNode/>
      <anyElement/>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-01-30" xml:lang="en">indicates the intended validity of the example with respect to
a schema.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>true</defaultVal>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="true">
          <desc versionDate="2011-12-04" xml:lang="en">the example is intended to be fully valid,
assuming that its root element, or a provided root element, 
could have been used as a possible root element in the schema concerned.</desc>
        </valItem>
        <valItem ident="feasible">
          <desc versionDate="2011-12-04" xml:lang="en">the example could be transformed into
a valid document by inserting any number of valid attributes and child
elements anywhere within it; or it is valid against a version of the
schema concerned in which the provision of character data, list, element, or attribute
values has been made optional.</desc>
        </valItem>
        <valItem ident="false">
          <desc versionDate="2011-01-30" xml:lang="en">the example is not intended to be valid,
and contains deliberate errors.</desc>
        </valItem>
      </valList>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples">
<egXML>
<div>
    <head>A slide about <gi>egXML</gi></head>
    <list>
     <item><gi>egXML</gi> can be used to give XML examples in the TEI
Examples namespace</item>
     <item>Attributes values for <att>valid</att>:
      <list rend="collapsed">
      <item><val rend="green">true</val>: intended to be fully
valid</item>
      <item><val rend="amber">feasible</val>: valid if missing nodes
provided</item>
      <item><val rend="red">false</val>: not intended to be valid</item>
      </list>
      </item>
      <item>The <att>rend</att>  attribute can be
        used for recording how parts of the example were rendered.</item>
      </list>
</div>
</egXML>

  </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-egXML-egXML-rw" xml:lang="und" valid="feasible" source="#UND">
      
      <egXML valid="feasible" source="#UND">
       <text>
       <front><!-- front matter for the whole group --></front>
       <group>
       <text>
       <!-- first text -->
       </text>
       <text>
       <!-- second text -->
       </text>
       </group>
      </text>
      <!-- This example is not valid TEI, but could be made so by
      adding missing components -->

    </egXML>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-egXML-egXML-gn" xml:lang="und" valid="false">
      &lt;egXML xmlns="http://www.tei-c.org/ns/Examples" valid="false"&gt;
         &lt;para xml:lang="en"&gt;Doubloons are a pirate's best friend&lt;/para&gt;
      &lt;/egXML&gt;
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="egXML-remarks" versionDate="2011-12-05" xml:lang="en">
    <p>In the source of the TEI Guidelines, this element declares itself and its content as
      belonging to the namespace <ident type="ns">http://www.tei-c.org/ns/Examples</ident>. This
      enables the content of the element to be validated independently against the TEI scheme. Where
      this element is used outside this context, a different namespace or none at all may be
      preferable. The content must however be a well-formed XML fragment or document: where this is
      not the case, the more general <gi>eg</gi> element should be used in preference. <!-- JC: Commenting out 
      on 2018-01-19 until real mechanism agreed --> <!--In a TEI context 
      use of the <att>rend</att> attribute in the TEI namespace, as opposed to the TEI Examples namespace, 
      enables recording of rendition information.-->
    </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="egXML-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans la source des principes directeurs de la TEI, cet élément se déclare lui-même, ainsi que
      son contenu, comme appartenant à l'espace de noms <ident type="ns">http://www.tei-c.org/ns/Examples</ident>. Cela permet au contenu de l'élément d'être validé
      indépendamment du schéma TEI. Lorsque cet élément est utilisé hors de ce contexte, il peut
      s'avérer préférable de mettre un espace de noms différent ou pas d'espace de nom du tout. Le
      contenu doit cependant être un document ou un fragment en XML bien formé : si ce n'est pas le
      cas, on utilisera plutôt l'élément plus général <gi>eg</gi> .</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="egXML-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> TEIガイドラインでは、当該要素とその内容は、名前区間 <ident type="ns">http://www.tei-c.org/ns/Examples</ident>
      で宣言されているとする。これにより、TEIスキームとは関係なく、当該 要素の内容は妥当とされる。当該要素が、これ以外の意味で使用される場
      合には、異なる名前空間を使用することが望ましいだろう。 当該要素の内容は、整形式XMLデータでなければならない。そうでない場
      合は、より一般的な要素<gi>eg</gi>を使用すべきである。 </p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDphraseTE"/>
  </listRef>
```

^b26

