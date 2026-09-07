---
type: representation
source-type: document
source: '[[00_sources/tei-p5-exemplum-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 exemplum
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/exemplum.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# exemplum

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4466. Git blob: `34c3bb8cf91b81e231ba5c6967b526dc1bba71a0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-exemplum" ident="exemplum">
  <gloss versionDate="2007-06-12" xml:lang="en">exemplum</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">exemple</gloss>
  <desc versionDate="2008-01-31" xml:lang="en">groups an example demonstrating the use of an element along with optional paragraphs of
    commentary.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">요소의 사용을 나타내는 단일 예를 포함한다. 수의적으로 논평문단과 함께 나타난다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含說明某一元素使用的單一範例，可任意配合註解段落。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素の使用例をひとつ示す。段落単位の解説を伴うかもしれない。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un exemple qui montre l'utilisation d'un élément
    avec de possibles paragraphes de commentaires.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un ejemplo demostrativo del uso de un elemento,
    junto a eventuales párrafos explicativos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un unico esempio che illustra l'utilizzo di un
    elemento insieme ad eventuali paragrafi di discussione</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.translatable"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <sequence>
      
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
      
      <alternate>
        <elementRef key="egXML"/>
        <elementRef key="eg"/>
      </alternate>
      
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-exemplum-egXML-tx">
      <exemplum xml:lang="en">
        <p>The <gi>name</gi> element can be used for both personal names and place names:</p>
        <eg xml:space="preserve">&lt;![CDATA[ &lt;q&gt;My dear &lt;name type="person"&gt;Mr.
          Bennet&lt;/name&gt;,&lt;/q&gt; said his lady to him one day,
          &lt;q&gt;have you heard that &lt;name type="place"&gt;Netherfield
          Park&lt;/name&gt; is let at last?&lt;/q&gt;]]&gt;</eg>
        <p>As shown above, the <att>type</att> attribute may be used to distinguish the one from the
          other.</p>
      </exemplum>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-exemplum-egXML-ak" source="#fr-ex-Ionesco-chauve">
      <exemplum>
        <p>L'élément<gi>name</gi> est employé à la fois pour les noms propres de personne et de
            lieu : </p>
        <eg xml:space="preserve">
            &lt;q&gt;
              &lt;name type="person"&gt;Mrs. Parker&lt;/name&gt;, connaît un épicier bulgare, nommé, &lt;name
                type="person"&gt;Popochef Rosenfeld&lt;/name&gt;qui vient d'arriver de &lt;name type="place"
                &gt;Constantinople&lt;/name&gt;. C'est un grand spécialiste en yaourts.&lt;/q&gt;
          </eg>
        <p>Comme il est indiqué ci-dessus, l'attribut<att>type</att> peut être utilisé pour
            distinguer un élément de l'autre.</p>
      </exemplum>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-exemplum-egXML-bi">
      <exemplum>
        <p><gi>名稱</gi>元素可以同時用於人名以及地名：</p>
        <eg xml:space="preserve">&lt;![CDATA[ &lt;q&gt;我親愛的 &lt;name
          type="person"&gt;班耐特&lt;/name&gt;先生，&lt;/q&gt; 有一天太太對他說，
          &lt;q&gt;你聽到&lt;name type="place"&gt;尼得斐莊園&lt;/name&gt;
          終於租出去了嗎？&lt;/q&gt;]]&gt;</eg>
        <p>如上所示，<att>屬性值</att> 可用來分辨人名或地名。</p>
      </exemplum>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDTAG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">exemplum</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">exemple</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2008-01-31" xml:lang="en">groups an example demonstrating the use of an element along with optional paragraphs of
    commentary.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">요소의 사용을 나타내는 단일 예를 포함한다. 수의적으로 논평문단과 함께 나타난다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含說明某一元素使用的單一範例，可任意配合註解段落。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素の使用例をひとつ示す。段落単位の解説を伴うかもしれない。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un exemple qui montre l'utilisation d'un élément
    avec de possibles paragraphes de commentaires.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un ejemplo demostrativo del uso de un elemento,
    junto a eventuales párrafos explicativos.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un unico esempio che illustra l'utilizzo di un
    elemento insieme ad eventuali paragrafi di discussione</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.translatable"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
      
      <alternate>
        <elementRef key="egXML"/>
        <elementRef key="eg"/>
      </alternate>
      
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
      
    </sequence>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-exemplum-egXML-tx">
      <exemplum xml:lang="en">
        <p>The <gi>name</gi> element can be used for both personal names and place names:</p>
        <eg xml:space="preserve">&lt;![CDATA[ &lt;q&gt;My dear &lt;name type="person"&gt;Mr.
          Bennet&lt;/name&gt;,&lt;/q&gt; said his lady to him one day,
          &lt;q&gt;have you heard that &lt;name type="place"&gt;Netherfield
          Park&lt;/name&gt; is let at last?&lt;/q&gt;]]&gt;</eg>
        <p>As shown above, the <att>type</att> attribute may be used to distinguish the one from the
          other.</p>
      </exemplum>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-exemplum-egXML-ak" source="#fr-ex-Ionesco-chauve">
      <exemplum>
        <p>L'élément<gi>name</gi> est employé à la fois pour les noms propres de personne et de
            lieu : </p>
        <eg xml:space="preserve">
            &lt;q&gt;
              &lt;name type="person"&gt;Mrs. Parker&lt;/name&gt;, connaît un épicier bulgare, nommé, &lt;name
                type="person"&gt;Popochef Rosenfeld&lt;/name&gt;qui vient d'arriver de &lt;name type="place"
                &gt;Constantinople&lt;/name&gt;. C'est un grand spécialiste en yaourts.&lt;/q&gt;
          </eg>
        <p>Comme il est indiqué ci-dessus, l'attribut<att>type</att> peut être utilisé pour
            distinguer un élément de l'autre.</p>
      </exemplum>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-exemplum-egXML-bi">
      <exemplum>
        <p><gi>名稱</gi>元素可以同時用於人名以及地名：</p>
        <eg xml:space="preserve">&lt;![CDATA[ &lt;q&gt;我親愛的 &lt;name
          type="person"&gt;班耐特&lt;/name&gt;先生，&lt;/q&gt; 有一天太太對他說，
          &lt;q&gt;你聽到&lt;name type="place"&gt;尼得斐莊園&lt;/name&gt;
          終於租出去了嗎？&lt;/q&gt;]]&gt;</eg>
        <p>如上所示，<att>屬性值</att> 可用來分辨人名或地名。</p>
      </exemplum>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
  </listRef>
```

^b15

