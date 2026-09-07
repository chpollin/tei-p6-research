---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listrelation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listRelation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listRelation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listRelation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6781. Git blob: `6df070b881675c0156f11ca8d2a5b03a490f78f1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-listRelation" ident="listRelation">
  <desc versionDate="2011-12-02" xml:lang="en">provides information about relationships identified amongst people, places, and
    organizations, either informally as prose or as formally expressed relation links.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">donne des informations sur les relations qui existent
    entre des personnes, des lieux, ou des organisations, soit de manière informelle en prose, soit
    de manière formelle.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">비공식적으로 산문체 또는 공식적으로 표현된 관계 연결을 통하여 사람, 장소, 그리고 조직 사이에
    식별되는 관련성에 관한 정보를 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述一項語言互動中參與者之間的關係或社交關聯。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人、場所、組織間の関係に関する情報を、散文またはリンクによる形式的表 現で示す。</desc>
  <desc versionDate="2007-11-06" xml:lang="it">fornisce informazioni relative alle relazioni
    identificate tra persone, luoghi e organizzazioni, a livello informale discorsivo o sotto forma
    di legami formalmente espressi</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe las relaciones o los lazos sociales entre los
    participantes de una interacción verbal.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.listLike"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="1" maxOccurs="1">
        <classRef key="model.pLike"/>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </alternate>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-ln" source="#UND">
      <listPerson>
        <person xml:id="pp1">
          <!-- data about person pp1 -->
        </person>
        <person xml:id="pp2">
          <!-- data about person pp1 -->
        </person>
        <!-- more person (pp3, pp4) elements here -->
      <listRelation type="personal">
        <relation name="parent" active="#pp1 #pp2" passive="#pp3 #pp4"/>
        <relation name="spouse" mutual="#pp1 #pp2"/>
      </listRelation>
      <listRelation type="social">
        <relation name="employer" active="#pp1" passive="#pp3 #pp5 #pp6 #pp7"/>
      </listRelation>
     </listPerson>
    </egXML>
    <p>The persons with identifiers pp1 and pp2 are the parents of pp3 and pp4; they are also married to
      each other; pp1 is the employer of pp3, pp5, pp6, and pp7.</p>
  </exemplum>
  <exemplum versionDate="2017-06-30" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-te" source="#UND">
      <listPerson>
        <person xml:id="en_pp1">
          <!-- data about person en_pp1 -->
        </person>
        <person xml:id="en_pp2">
          <!-- data about person en_pp2 -->
        </person>
        <!-- more person (en_pp3, en_pp4) elements here -->
      </listPerson>
      <listPlace>
        <place xml:id="en_pl1">
          <!-- data about place en_pl1 -->
        </place>
        <!-- more place (en_pl2, en_pl3) elements here -->
      </listPlace>
      <listRelation>
        <relation name="residence" active="#en_pp1 #en_pp2" passive="#en_pl1"/>
      </listRelation>
    </egXML>
    <p>The persons with identifiers en_pp1 and en_pp2 live in en_pl1.</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-sa">
      <listRelation>
        <p>Tous les locuteurs sont membres de la famille Ceruli, et sont nés à Naples.</p>
      </listRelation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-kh" source="#UND">
      <listPerson>
        <person xml:id="zh-tw_pp1">
          <!-- 第一人的資料 -->
        </person>
        <!-- 更多關於此人的元素 -->
      </listPerson>
      <listRelation type="personal">
        <relation name="parent" active="#zh-tw_pp1 #zh-tw_pp2" passive="#p3 #p4"/>
        <relation name="spouse" mutual="#zh-tw_pp1 #zh-tw_pp2"/>
      </listRelation>
      <listRelation type="social">
        <relation name="employer" active="#zh-tw_pp1" passive="#p3 #p5 #p6 #p7"/>
      </listRelation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-pk">
      <listRelation>
        <p>所有說話者都是林家的人，生於台北板橋。</p>
      </listRelation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-lp">
      <listRelation>
        <p>All speakers are members of the Ceruli family, born in Naples.</p>
      </listRelation>
    </egXML>
  </exemplum>
  <remarks ident="listRelation-remarks" versionDate="2011-12-02" xml:lang="en">
    <p rend="dataDesc">May contain a prose description organized as paragraphs, or a sequence of
        <gi>relation</gi> elements.</p>
  </remarks>
  <remarks ident="listRelation-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc">Peut contenir soit une description en prose organisée en paragraphes, soit
      une suite d'éléments <gi>relation</gi>.</p>
  </remarks>
  <remarks ident="listRelation-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落または一連の要素<gi>relation</gi>による散文を含むかもしれない。 </p>
  </remarks>
  <listRef>
    <ptr target="#NDPERSREL"/>
    <!-- MDH: Original link is to chapter which does not mention this element. Should it?    -->
    <!--<ptr target="#CCAHPA"/>-->
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-12-02" xml:lang="en">provides information about relationships identified amongst people, places, and
    organizations, either informally as prose or as formally expressed relation links.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">donne des informations sur les relations qui existent
    entre des personnes, des lieux, ou des organisations, soit de manière informelle en prose, soit
    de manière formelle.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">비공식적으로 산문체 또는 공식적으로 표현된 관계 연결을 통하여 사람, 장소, 그리고 조직 사이에
    식별되는 관련성에 관한 정보를 제공한다.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述一項語言互動中參與者之間的關係或社交關聯。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人、場所、組織間の関係に関する情報を、散文またはリンクによる形式的表 現で示す。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">fornisce informazioni relative alle relazioni
    identificate tra persone, luoghi e organizzazioni, a livello informale discorsivo o sotto forma
    di legami formalmente espressi</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe las relaciones o los lazos sociales entre los
    participantes de una interacción verbal.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.biblPart"/>
    <memberOf key="model.listLike"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="1" maxOccurs="1">
        <classRef key="model.pLike"/>
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </alternate>
    </sequence>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-ln" source="#UND">
      <listPerson>
        <person xml:id="pp1">
          <!-- data about person pp1 -->
        </person>
        <person xml:id="pp2">
          <!-- data about person pp1 -->
        </person>
        <!-- more person (pp3, pp4) elements here -->
      <listRelation type="personal">
        <relation name="parent" active="#pp1 #pp2" passive="#pp3 #pp4"/>
        <relation name="spouse" mutual="#pp1 #pp2"/>
      </listRelation>
      <listRelation type="social">
        <relation name="employer" active="#pp1" passive="#pp3 #pp5 #pp6 #pp7"/>
      </listRelation>
     </listPerson>
    </egXML>
    <p>The persons with identifiers pp1 and pp2 are the parents of pp3 and pp4; they are also married to
      each other; pp1 is the employer of pp3, pp5, pp6, and pp7.</p>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-30" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-te" source="#UND">
      <listPerson>
        <person xml:id="en_pp1">
          <!-- data about person en_pp1 -->
        </person>
        <person xml:id="en_pp2">
          <!-- data about person en_pp2 -->
        </person>
        <!-- more person (en_pp3, en_pp4) elements here -->
      </listPerson>
      <listPlace>
        <place xml:id="en_pl1">
          <!-- data about place en_pl1 -->
        </place>
        <!-- more place (en_pl2, en_pl3) elements here -->
      </listPlace>
      <listRelation>
        <relation name="residence" active="#en_pp1 #en_pp2" passive="#en_pl1"/>
      </listRelation>
    </egXML>
    <p>The persons with identifiers en_pp1 and en_pp2 live in en_pl1.</p>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-sa">
      <listRelation>
        <p>Tous les locuteurs sont membres de la famille Ceruli, et sont nés à Naples.</p>
      </listRelation>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-kh" source="#UND">
      <listPerson>
        <person xml:id="zh-tw_pp1">
          <!-- 第一人的資料 -->
        </person>
        <!-- 更多關於此人的元素 -->
      </listPerson>
      <listRelation type="personal">
        <relation name="parent" active="#zh-tw_pp1 #zh-tw_pp2" passive="#p3 #p4"/>
        <relation name="spouse" mutual="#zh-tw_pp1 #zh-tw_pp2"/>
      </listRelation>
      <listRelation type="social">
        <relation name="employer" active="#zh-tw_pp1" passive="#p3 #p5 #p6 #p7"/>
      </listRelation>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-pk">
      <listRelation>
        <p>所有說話者都是林家的人，生於台北板橋。</p>
      </listRelation>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listRelation-egXML-lp">
      <listRelation>
        <p>All speakers are members of the Ceruli family, born in Naples.</p>
      </listRelation>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listRelation-remarks" versionDate="2011-12-02" xml:lang="en">
    <p rend="dataDesc">May contain a prose description organized as paragraphs, or a sequence of
        <gi>relation</gi> elements.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="listRelation-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc">Peut contenir soit une description en prose organisée en paragraphes, soit
      une suite d'éléments <gi>relation</gi>.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="listRelation-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落または一連の要素<gi>relation</gi>による散文を含むかもしれない。 </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSREL"/>
    <!-- MDH: Original link is to chapter which does not mention this element. Should it?    -->
    <!--<ptr target="#CCAHPA"/>-->
  </listRef>
```

^b19

