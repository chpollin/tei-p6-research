---
type: representation
source-type: document
source: '[[00_sources/tei-p5-correspaction-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 correspAction
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/correspAction.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# correspAction

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3887. Git blob: `d00110fafb621a169878e85915330003fa1ecd2d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-correspAction" ident="correspAction">
  <gloss versionDate="2015-10-26" xml:lang="en">correspondence action</gloss>
	<gloss versionDate="2022-06-02" xml:lang="ja">書簡に関する所作</gloss>
  <desc versionDate="2014-09-05" xml:lang="en">contains a structured
  description of the place, the name of a person/organization and the
  date related to the sending/receiving of a message or any other
  action related to the correspondence.</desc>
	<desc versionDate="2022-06-02" xml:lang="ja">メッセージの送信・受信をはじめとする書簡に関する所作についての場所、人名／組織名、日付の構造的記述を含む。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.correspDescPart"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.correspActionPart" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2015-01-29" xml:lang="en">describes the nature of the action.</desc>
	    <desc versionDate="2022-06-02" xml:lang="ja">（書簡に関する）所作の性質を記述する。</desc>
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="semi">
        <valItem ident="sent">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the sending or dispatch of a message.</desc>
		<desc versionDate="2022-06-02" xml:lang="ja">メッセージの送信や発送に関する情報。</desc>
        </valItem>
        <valItem ident="received">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the receipt of a message.</desc>
		<desc versionDate="2022-06-02" xml:lang="ja">メッセージの受信に関する情報。</desc>
        </valItem>
        <valItem ident="transmitted">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the transmission of a message, i.e. between the dispatch and the next receipt, redirect or forwarding.</desc>
          <desc versionDate="2024-03-07" xml:lang="ja">メッセージの伝達手段に関する情報。発信とその後の受信・転送等の間の情報。</desc>
	      </valItem>
        <valItem ident="redirected">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the
	  redirection of an unread message.</desc>
          <desc versionDate="2024-03-07" xml:lang="ja">〔開封せずに〕未読のままに転送されるメッセージに関する情報。</desc>
        </valItem>
        <valItem ident="forwarded">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the
	  forwarding of a message.</desc>
          <desc versionDate="2024-03-07" xml:lang="ja">〔開封後の〕メッセージの転送に関する情報。</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correspAction-egXML-lz">
      <correspAction type="sent">
        <persName>Adelbert von Chamisso</persName>
        <settlement>Vertus</settlement>
        <date when="1807-01-29"/>
      </correspAction>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD44CD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2015-10-26" xml:lang="en">correspondence action</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2022-06-02" xml:lang="ja">書簡に関する所作</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2014-09-05" xml:lang="en">contains a structured
  description of the place, the name of a person/organization and the
  date related to the sending/receiving of a message or any other
  action related to the correspondence.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2022-06-02" xml:lang="ja">メッセージの送信・受信をはじめとする書簡に関する所作についての場所、人名／組織名、日付の構造的記述を含む。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.correspDescPart"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.correspActionPart" minOccurs="1" maxOccurs="unbounded"/>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2015-01-29" xml:lang="en">describes the nature of the action.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2022-06-02" xml:lang="ja">（書簡に関する）所作の性質を記述する。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="sent">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the sending or dispatch of a message.</desc>
		<desc versionDate="2022-06-02" xml:lang="ja">メッセージの送信や発送に関する情報。</desc>
        </valItem>
        <valItem ident="received">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the receipt of a message.</desc>
		<desc versionDate="2022-06-02" xml:lang="ja">メッセージの受信に関する情報。</desc>
        </valItem>
        <valItem ident="transmitted">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the transmission of a message, i.e. between the dispatch and the next receipt, redirect or forwarding.</desc>
          <desc versionDate="2024-03-07" xml:lang="ja">メッセージの伝達手段に関する情報。発信とその後の受信・転送等の間の情報。</desc>
	      </valItem>
        <valItem ident="redirected">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the
	  redirection of an unread message.</desc>
          <desc versionDate="2024-03-07" xml:lang="ja">〔開封せずに〕未読のままに転送されるメッセージに関する情報。</desc>
        </valItem>
        <valItem ident="forwarded">
          <desc versionDate="2015-02-09" xml:lang="en">information concerning the
	  forwarding of a message.</desc>
          <desc versionDate="2024-03-07" xml:lang="ja">〔開封後の〕メッセージの転送に関する情報。</desc>
        </valItem>
      </valList>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correspAction-egXML-lz">
      <correspAction type="sent">
        <persName>Adelbert von Chamisso</persName>
        <settlement>Vertus</settlement>
        <date when="1807-01-29"/>
      </correspAction>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD44CD"/>
  </listRef>
```

^b12

