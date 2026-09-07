---
type: representation
source-type: document
source: '[[00_sources/tei-p5-recordhist-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 recordHist
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/recordHist.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# recordHist

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3803. Git blob: `67a5704c91bfca88ea28c93101d609ff7a90e31d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="RECORDHIST" ident="recordHist">
  <gloss versionDate="2007-07-04" xml:lang="en">recorded history</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">기록 이력</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">historia registrada</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">histoire de la description</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">storia registrata</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="rechist.desc">provides information about the source and
revision status of the parent manuscript or object description itself.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">그 원전에 관한 정보 그리고 원고의 기술 자체의 수정 이력에 관한 정보를 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供父手稿本身說明的出處與修訂狀態相關資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">元になった手書き資料の、元や改訂に関する情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">donne des informations sur la source de la
      description et sur les modifications apportées à la description précédente.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona información relativa a la fuente y sobre el estatus de revisión de la descripción  del manuscrito del que deriva.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative alla fonte e alla revisione della descrizione stessa del manoscritto genitore.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        <elementRef key="source"/>
        
          <elementRef key="change" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RECORDHIST-egXML-wf">
      <recordHist>
        <source>
          <p>Derived from <ref target="#IMEV">IMEV 123</ref> with additional research
	by P.M.W.Robinson</p>
        </source>
        <change when="1999-06-23"><name>LDB</name> (editor)
	  checked examples against DTD version 3.6
	</change>
      </recordHist>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RECORDHIST-egXML-hq">
      <recordHist>
        <source>
          <p>Derived from <ref target="#fr_IMEV">IMEV 123</ref> with additional research by
              P.M.W.Robinson</p>
        </source>
        <change when="1999-06-23"><name>LDB</name> (editor) checked examples against DTD version
            3.6 </change>
      </recordHist>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RECORDHIST-egXML-au">
      <recordHist>
        <source>
          <p>源自<ref target="#IMEV">IMEV 123</ref>及P.M.W.羅賓森的附加研究。</p>
        </source>
        <change when="1999-06-23"><name>LDB</name> (編輯) 檢查不符DTD 3.6版本的範例</change>
      </recordHist>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msadad"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">recorded history</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">기록 이력</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">historia registrada</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">histoire de la description</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">storia registrata</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="rechist.desc">provides information about the source and
revision status of the parent manuscript or object description itself.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">그 원전에 관한 정보 그리고 원고의 기술 자체의 수정 이력에 관한 정보를 제공한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供父手稿本身說明的出處與修訂狀態相關資訊。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">元になった手書き資料の、元や改訂に関する情報を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">donne des informations sur la source de la
      description et sur les modifications apportées à la description précédente.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona información relativa a la fuente y sobre el estatus de revisión de la descripción  del manuscrito del que deriva.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative alla fonte e alla revisione della descrizione stessa del manoscritto genitore.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        <elementRef key="source"/>
        
          <elementRef key="change" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RECORDHIST-egXML-wf">
      <recordHist>
        <source>
          <p>Derived from <ref target="#IMEV">IMEV 123</ref> with additional research
	by P.M.W.Robinson</p>
        </source>
        <change when="1999-06-23"><name>LDB</name> (editor)
	  checked examples against DTD version 3.6
	</change>
      </recordHist>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RECORDHIST-egXML-hq">
      <recordHist>
        <source>
          <p>Derived from <ref target="#fr_IMEV">IMEV 123</ref> with additional research by
              P.M.W.Robinson</p>
        </source>
        <change when="1999-06-23"><name>LDB</name> (editor) checked examples against DTD version
            3.6 </change>
      </recordHist>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="RECORDHIST-egXML-au">
      <recordHist>
        <source>
          <p>源自<ref target="#IMEV">IMEV 123</ref>及P.M.W.羅賓森的附加研究。</p>
        </source>
        <change when="1999-06-23"><name>LDB</name> (編輯) 檢查不符DTD 3.6版本的範例</change>
      </recordHist>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msadad"/>
  </listRef>
```

^b19

