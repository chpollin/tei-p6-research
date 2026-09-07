---
type: representation
source-type: document
source: '[[00_sources/tei-p5-listnym-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 listNym
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/listNym.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# listNym

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5433. Git blob: `e1562f5b5ab7c4db8f1c999031ce6885283949f6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-listNym" ident="listNym">
  <gloss versionDate="2007-07-04" xml:lang="en">list of canonical names</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">표준 이름 목록</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">lista de nombres canónicos</gloss>
  <gloss versionDate="2009-03-19" xml:lang="fr">liste de noms canoniques</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">elenco di nomi canonici</gloss>
  <desc versionDate="2007-04-12" xml:lang="en">contains a list of nyms, that is, standardized names for any thing.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 사물에 대한 표준화된 이름 목록을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一正式名稱列表，即任何事物的標準名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">別名、すなわち、一般的に使われている名前のリストを示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient une liste de noms normalisés pour tous types d'objets.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene una lista di nym, cioè nomi standard per qualsiasi cosa.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una lista de nyms, es decir, nombres estándard para cualquier cosa.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="nym" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listNym" minOccurs="1" maxOccurs="1"/>
        </alternate>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
  <constraintSpec ident="listNym-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listNym"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listNym-egXML-xn">
      <listNym type="floral">
        <nym xml:id="ROSE">
          <form>Rose</form>
        </nym>
        <nym xml:id="DAISY">
          <form>Daisy</form>
          <etym>Contraction of <mentioned>day's eye</mentioned>
                    </etym>
        </nym>
        <nym xml:id="HTHR">
          <form>Heather</form>
        </nym>
      </listNym>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listNym-egXML-wg">
      <listNym type="floral">
        <nym xml:id="fr_ROSE">
          <form>Rose</form>
        </nym>
        <nym xml:id="fr_DAISY">
          <form>Daisy</form>
          <etym>contraction de <mentioned>day's eye</mentioned>
               </etym>
        </nym>
        <nym xml:id="fr_HTHR">
          <form>Heather</form>
        </nym>
      </listNym>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listNym-egXML-wq">
      <listNym type="floral">
        <nym xml:id="zh-tw_ROSE">
          <form>玫瑰</form>
        </nym>
        <nym xml:id="zh-tw_ORCHID">
          <form>蘭花</form>
          <etym>多年生草本植物，葉細長而尖，春天開花，味清香。</etym>
        </nym>
        <nym xml:id="zh-tw_HTHR">
          <form>Heather(石南屬植物)</form>
        </nym>
      </listNym>
    </egXML>
  </exemplum>
  <remarks ident="listNym-remarks" versionDate="2007-04-12" xml:lang="en">
    <p rend="dataDesc">The type attribute may be used to distinguish lists of names of a particular type if convenient.</p>
  </remarks>
  <remarks ident="listNym-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc"> L'attribut type peut être utilisé pour établir des listes par type de nom si cela présente un intérêt.</p>
  </remarks>
  <remarks ident="listNym-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 属性typeは、特別な種類の名前を区別する際に使用されるかもしれない。 </p>
  </remarks>
  <listRef>
    <ptr target="#NDNYM"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">list of canonical names</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">표준 이름 목록</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">lista de nombres canónicos</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-03-19" xml:lang="fr">liste de noms canoniques</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">elenco di nomi canonici</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-12" xml:lang="en">contains a list of nyms, that is, standardized names for any thing.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 사물에 대한 표준화된 이름 목록을 포함한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一正式名稱列表，即任何事物的標準名稱。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">別名、すなわち、一般的に使われている名前のリストを示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient une liste de noms normalisés pour tous types d'objets.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene una lista di nym, cioè nomi standard per qualsiasi cosa.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una lista de nyms, es decir, nombres estándard para cualquier cosa.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <elementRef key="desc" minOccurs="0" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
        <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
      </alternate>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate minOccurs="1" maxOccurs="unbounded">
          <elementRef key="nym" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listNym" minOccurs="1" maxOccurs="1"/>
        </alternate>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="relation" minOccurs="1" maxOccurs="1"/>
          <elementRef key="listRelation" minOccurs="1" maxOccurs="1"/>
        </alternate>
      </sequence>
    </sequence>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="listNym-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:listNym"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listNym-egXML-xn">
      <listNym type="floral">
        <nym xml:id="ROSE">
          <form>Rose</form>
        </nym>
        <nym xml:id="DAISY">
          <form>Daisy</form>
          <etym>Contraction of <mentioned>day's eye</mentioned>
                    </etym>
        </nym>
        <nym xml:id="HTHR">
          <form>Heather</form>
        </nym>
      </listNym>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listNym-egXML-wg">
      <listNym type="floral">
        <nym xml:id="fr_ROSE">
          <form>Rose</form>
        </nym>
        <nym xml:id="fr_DAISY">
          <form>Daisy</form>
          <etym>contraction de <mentioned>day's eye</mentioned>
               </etym>
        </nym>
        <nym xml:id="fr_HTHR">
          <form>Heather</form>
        </nym>
      </listNym>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-listNym-egXML-wq">
      <listNym type="floral">
        <nym xml:id="zh-tw_ROSE">
          <form>玫瑰</form>
        </nym>
        <nym xml:id="zh-tw_ORCHID">
          <form>蘭花</form>
          <etym>多年生草本植物，葉細長而尖，春天開花，味清香。</etym>
        </nym>
        <nym xml:id="zh-tw_HTHR">
          <form>Heather(石南屬植物)</form>
        </nym>
      </listNym>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="listNym-remarks" versionDate="2007-04-12" xml:lang="en">
    <p rend="dataDesc">The type attribute may be used to distinguish lists of names of a particular type if convenient.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="listNym-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc"> L'attribut type peut être utilisé pour établir des listes par type de nom si cela présente un intérêt.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="listNym-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 属性typeは、特別な種類の名前を区別する際に使用されるかもしれない。 </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDNYM"/>
  </listRef>
```

^b22

