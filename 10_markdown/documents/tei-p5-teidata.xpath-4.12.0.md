---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.xpath-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.xpath
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.xpath.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.xpath

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 1762. Git blob: `c47c92a49e219eae7a14ad52205f5f56e589653e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.xpath">
  <desc versionDate="2013-04-14" xml:lang="en">defines attribute values which contain an XPath expression.</desc>
  <desc versionDate="2024-09-02" xml:lang="ja">XPath式を含む属性を定義する。</desc>
  <content>
    <textNode/>
  </content>
  <remarks ident="teidata.xpath-remarks" versionDate="2013-04-14" xml:lang="en">
    <p>Any XPath expression using the syntax
    defined in <ptr target="#XSLT2"/>.</p>
    <p>When writing programs that evaluate XPath expressions,
    programmers should be mindful of the possibility of malicious code
    injection attacks. For further information about XPath injection
    attacks, see the <ref target="https://owasp.org/www-community/attacks/XPATH_Injection">article at
    OWASP</ref>.</p>
  </remarks>
  <remarks ident="teidata.xpath-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p>XPath式は、<ptr target="#XSLT2"/>で定義された文法を用いる。</p>
    <p>XPath式を評価するプログラムを作成するときは、プログラマーはコー
    ドインジェクション攻撃の可能性に留意すべきである。XPathのインジェ
    クション攻撃については、<ref target="https://owasp.org/www-community/attacks/XPATH_Injection">OWASP
    に掲載された記事</ref>を参照せよ。</p>
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2013-04-14" xml:lang="en">defines attribute values which contain an XPath expression.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2024-09-02" xml:lang="ja">XPath式を含む属性を定義する。</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b3

### Block 4

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.xpath-remarks" versionDate="2013-04-14" xml:lang="en">
    <p>Any XPath expression using the syntax
    defined in <ptr target="#XSLT2"/>.</p>
    <p>When writing programs that evaluate XPath expressions,
    programmers should be mindful of the possibility of malicious code
    injection attacks. For further information about XPath injection
    attacks, see the <ref target="https://owasp.org/www-community/attacks/XPATH_Injection">article at
    OWASP</ref>.</p>
  </remarks>
```

^b4

### Block 5

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.xpath-remarks" versionDate="2024-09-02" xml:lang="ja">
    <p>XPath式は、<ptr target="#XSLT2"/>で定義された文法を用いる。</p>
    <p>XPath式を評価するプログラムを作成するときは、プログラマーはコー
    ドインジェクション攻撃の可能性に留意すべきである。XPathのインジェ
    クション攻撃については、<ref target="https://owasp.org/www-community/attacks/XPATH_Injection">OWASP
    に掲載された記事</ref>を参照せよ。</p>
  </remarks>
```

^b5

