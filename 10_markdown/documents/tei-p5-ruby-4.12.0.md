---
type: representation
source-type: document
source: '[[00_sources/tei-p5-ruby-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 ruby
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/ruby.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# ruby

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2289. Git blob: `c79a68650556b7841a2faa789e74f637b1189f1c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" ident="ruby" xml:id="gi-ruby" module="core">
  <gloss versionDate="2021-01-30" xml:lang="en">ruby container</gloss>
<gloss versionDate="2021-01-31" xml:lang="ja">ルビのためのコンテナ要素。</gloss>
<desc versionDate="2020-02-28" xml:lang="en">contains a
  passage of base text along with its associated ruby gloss(es).</desc>
<desc versionDate="2021-01-31" xml:lang="ja">ルビ及びその対象となるテキストを含む。</desc>
<classes>
  <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
  <memberOf key="att.typed"/>
  <memberOf key="model.phrase"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="rb" minOccurs="1" maxOccurs="1"/>
      <elementRef key="rt" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
  <exemplum versionDate="2021-02-01" xml:lang="mul">
    <p>The word <mentioned>入学試験</mentioned> <mentioned>nyūgakushiken</mentioned>
    (university entrance exam) is glossed with a hiragana phonation guide.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ruby-egXML-zg">
      <p xml:lang="ja">
        <!--...-->
        <ruby>
          <rb>入学試験</rb>
          <rt place="above">にゅうがくしけん</rt>
        </ruby>
        <!--...-->
      </p>
      
    </egXML>
  </exemplum>
  
  <exemplum versionDate="2021-02-01" xml:lang="en">
    <p>This fictional example shows the initialism <mentioned>TEI</mentioned>
    glossed letter-by-letter with an IPA transcription.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ruby-egXML-mt" xml:lang="en">
      <ruby>
        <rb>T</rb>
        <rt>ti:</rt>
      </ruby>
      <ruby>
        <rb>E</rb>
        <rt>i:</rt>
      </ruby>
      <ruby>
        <rb>I</rb>
        <rt>aɪ</rt>
      </ruby>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COHTGRB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2021-01-30" xml:lang="en">ruby container</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2021-01-31" xml:lang="ja">ルビのためのコンテナ要素。</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-02-28" xml:lang="en">contains a
  passage of base text along with its associated ruby gloss(es).</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2021-01-31" xml:lang="ja">ルビ及びその対象となるテキストを含む。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
  <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
  <memberOf key="att.typed"/>
  <memberOf key="model.phrase"/>
  </classes>
```

^b5

### Block 6

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <elementRef key="rb" minOccurs="1" maxOccurs="1"/>
      <elementRef key="rt" minOccurs="1" maxOccurs="unbounded"/>
    </sequence>
  </content>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2021-02-01" xml:lang="mul">
    <p>The word <mentioned>入学試験</mentioned> <mentioned>nyūgakushiken</mentioned>
    (university entrance exam) is glossed with a hiragana phonation guide.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ruby-egXML-zg">
      <p xml:lang="ja">
        <!--...-->
        <ruby>
          <rb>入学試験</rb>
          <rt place="above">にゅうがくしけん</rt>
        </ruby>
        <!--...-->
      </p>
      
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2021-02-01" xml:lang="en">
    <p>This fictional example shows the initialism <mentioned>TEI</mentioned>
    glossed letter-by-letter with an IPA transcription.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ruby-egXML-mt" xml:lang="en">
      <ruby>
        <rb>T</rb>
        <rt>ti:</rt>
      </ruby>
      <ruby>
        <rb>E</rb>
        <rt>i:</rt>
      </ruby>
      <ruby>
        <rb>I</rb>
        <rt>aɪ</rt>
      </ruby>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHTGRB"/>
  </listRef>
```

^b9

