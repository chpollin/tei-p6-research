---
type: representation
source-type: document
source: '[[00_sources/tei-p5-valitem-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 valItem
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/valItem.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# valItem

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6048. Git blob: `37648139b4ea5e0a10869900a0f01075d613c917`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-valItem" ident="valItem">
  <desc versionDate="2012-09-23" xml:lang="en">documents a single value in a predefined list of values.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">가능한 또는 필수적 항목의 목록 내에서 단일 속성 값을 기록한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含單一屬性的一個屬性值及註解對。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">属性値のひとつを解説する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">documente une valeur d'attribut unique dans une liste d'items possibles ou obligatoires.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un único valor y una glosa para un atributo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un unico valore e un'unica coppia di glosse per un attributo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
  </classes>
  <!-- ( gloss*, ( desc+, ( gloss, desc* )*, remarks* )?, paramList? ) -->
  <content>
    <sequence>
      <classRef key="model.identSynonyms" minOccurs="0" maxOccurs="unbounded"/>
      <sequence minOccurs="0">
	<classRef key="model.descLike" minOccurs="1" maxOccurs="unbounded"/>
	<sequence minOccurs="0" maxOccurs="unbounded">
	  <classRef key="model.identSynonyms" minOccurs="1" maxOccurs="1"/>
	  <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
	</sequence>
	<elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <elementRef key="paramList" minOccurs="0" maxOccurs="1"/>
    </sequence>
  </content>
  <attList>
    <attDef ident="ident" usage="req">
      <desc versionDate="2012-09-23" xml:lang="en">specifies the value concerned.</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valItem-egXML-xs">
      <valItem ident="dub">
        <altIdent xml:lang="fr">dou</altIdent>
        <equiv name="unknown"/>
        <gloss>dubious</gloss>
        <desc>used when the application of this element is doubtful or uncertain</desc>
      </valItem>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valItem-egXML-eo">
      <valItem ident="dub">
        <altIdent xml:lang="fr">dou</altIdent>
        <equiv name="unknown"/>
        <gloss>douteux</gloss>
        <desc>utilisé quand l'emploi de cet élément est douteux ou incertain.</desc>
      </valItem>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valItem-egXML-up">
      <valItem ident="dub">
        <altIdent xml:lang="fr">dou</altIdent>
        <equiv name="unknown"/>
        <gloss>dubious（無把握的）</gloss>
        <desc>適用於無法確定或對該元素的使用存疑時</desc>
      </valItem>
    </egXML>
  </exemplum>
  <exemplum versionDate="2018-01-21" xml:lang="en">
    <p>The <gi>remarks</gi> element is only allowed within <gi>valItem</gi> if the <gi>desc</gi> element is also present:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valItem-egXML-rb">
      <valList type="closed">
        <valItem ident="border">
          <desc>used to signify that there is border around a page.</desc>
        </valItem>
        <valItem ident="border-rule">
          <desc>used to signify that there is a border made of ruled lines.</desc>
        </valItem>
        <valItem ident="border-ornamental">
          <desc>used to signify that there is an ornamental border.</desc>
        </valItem>
        <valItem ident="catch">
          <gloss>catchword</gloss>
          <desc>for catch words.</desc>
        </valItem>
        <valItem ident="lineNum">
          <gloss>line number</gloss>
          <desc>for printed line numbers (usually in poetry).</desc>
        </valItem>
        <valItem ident="listHead">
          <gloss>list heading</gloss>
          <desc>for headings of lists or similar constructs; often used in tables of contents for the
            <q>page</q> heading.</desc>
        </valItem>
        <valItem ident="pageNum">
          <gloss>page number</gloss>
          <desc>for page numbers.</desc>
        </valItem>
        <valItem ident="pressFig">
          <gloss>press figure</gloss>
          <desc>for press figures. These are usually numbers, but are not sequential or regularly
            printed like signatures.</desc>
        </valItem>
        <valItem ident="sig">
          <gloss>signature</gloss>
          <desc>for printed signatures.</desc>
        </valItem>
        <valItem ident="unknown">
          <desc>for a metawork whose function you do not know.</desc>
        </valItem>
        <valItem ident="vol">
          <gloss>volume number</gloss>
          <desc>for printed volume numbers.</desc>
        </valItem>
        <valItem ident="other">
          <desc>anything not covered by the above values.</desc>
          <remarks>
            <p>Used for an ornament, decorated tool line, or symbol(s) that is not officially a
              delimiter (and thus there is no element on which to put <val>pre()</val> or
              <val>post()</val>) but is used to fill space at the bottom of a page so that a
              <gi>floatingText</gi> or similar can start at the top of the next.</p>
          </remarks>
        </valItem>
      </valList>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDATT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-09-23" xml:lang="en">documents a single value in a predefined list of values.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">가능한 또는 필수적 항목의 목록 내에서 단일 속성 값을 기록한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含單一屬性的一個屬性值及註解對。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性値のひとつを解説する。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">documente une valeur d'attribut unique dans une liste d'items possibles ou obligatoires.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un único valor y una glosa para un atributo.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un unico valore e un'unica coppia di glosse per un attributo.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.identSynonyms" minOccurs="0" maxOccurs="unbounded"/>
      <sequence minOccurs="0">
	<classRef key="model.descLike" minOccurs="1" maxOccurs="unbounded"/>
	<sequence minOccurs="0" maxOccurs="unbounded">
	  <classRef key="model.identSynonyms" minOccurs="1" maxOccurs="1"/>
	  <classRef key="model.descLike" minOccurs="0" maxOccurs="unbounded"/>
	</sequence>
	<elementRef key="remarks" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <elementRef key="paramList" minOccurs="0" maxOccurs="1"/>
    </sequence>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2012-09-23" xml:lang="en">specifies the value concerned.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valItem-egXML-xs">
      <valItem ident="dub">
        <altIdent xml:lang="fr">dou</altIdent>
        <equiv name="unknown"/>
        <gloss>dubious</gloss>
        <desc>used when the application of this element is doubtful or uncertain</desc>
      </valItem>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valItem-egXML-eo">
      <valItem ident="dub">
        <altIdent xml:lang="fr">dou</altIdent>
        <equiv name="unknown"/>
        <gloss>douteux</gloss>
        <desc>utilisé quand l'emploi de cet élément est douteux ou incertain.</desc>
      </valItem>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valItem-egXML-up">
      <valItem ident="dub">
        <altIdent xml:lang="fr">dou</altIdent>
        <equiv name="unknown"/>
        <gloss>dubious（無把握的）</gloss>
        <desc>適用於無法確定或對該元素的使用存疑時</desc>
      </valItem>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2018-01-21" xml:lang="en">
    <p>The <gi>remarks</gi> element is only allowed within <gi>valItem</gi> if the <gi>desc</gi> element is also present:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-valItem-egXML-rb">
      <valList type="closed">
        <valItem ident="border">
          <desc>used to signify that there is border around a page.</desc>
        </valItem>
        <valItem ident="border-rule">
          <desc>used to signify that there is a border made of ruled lines.</desc>
        </valItem>
        <valItem ident="border-ornamental">
          <desc>used to signify that there is an ornamental border.</desc>
        </valItem>
        <valItem ident="catch">
          <gloss>catchword</gloss>
          <desc>for catch words.</desc>
        </valItem>
        <valItem ident="lineNum">
          <gloss>line number</gloss>
          <desc>for printed line numbers (usually in poetry).</desc>
        </valItem>
        <valItem ident="listHead">
          <gloss>list heading</gloss>
          <desc>for headings of lists or similar constructs; often used in tables of contents for the
            <q>page</q> heading.</desc>
        </valItem>
        <valItem ident="pageNum">
          <gloss>page number</gloss>
          <desc>for page numbers.</desc>
        </valItem>
        <valItem ident="pressFig">
          <gloss>press figure</gloss>
          <desc>for press figures. These are usually numbers, but are not sequential or regularly
            printed like signatures.</desc>
        </valItem>
        <valItem ident="sig">
          <gloss>signature</gloss>
          <desc>for printed signatures.</desc>
        </valItem>
        <valItem ident="unknown">
          <desc>for a metawork whose function you do not know.</desc>
        </valItem>
        <valItem ident="vol">
          <gloss>volume number</gloss>
          <desc>for printed volume numbers.</desc>
        </valItem>
        <valItem ident="other">
          <desc>anything not covered by the above values.</desc>
          <remarks>
            <p>Used for an ornament, decorated tool line, or symbol(s) that is not officially a
              delimiter (and thus there is no element on which to put <val>pre()</val> or
              <val>post()</val>) but is used to fill space at the bottom of a page so that a
              <gi>floatingText</gi> or similar can start at the top of the next.</p>
          </remarks>
        </valItem>
      </valList>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDATT"/>
  </listRef>
```

^b16

