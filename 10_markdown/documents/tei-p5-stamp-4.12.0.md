---
type: representation
source-type: document
source: '[[00_sources/tei-p5-stamp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 stamp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/stamp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# stamp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2685. Git blob: `86a9660d743e91aa192b2eef15b2d5a87622d2fe`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="msdescription" xml:id="gi-stamp" ident="stamp">
  <gloss versionDate="2007-06-12" xml:lang="en">stamp</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">cachet</gloss>
  <desc versionDate="2007-02-16" xml:lang="en">contains a word or phrase describing a stamp or similar device.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">스탬프 또는 유사한 도구를 기술하는 단어 또는 구를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個字詞，描述一個印記或是類似圖案。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">印などにある語句を示す。</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">contient un mot ou une expression décrivant un cachet ou une marque du même genre.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene una parola o un sintagma che descrive un timbro o simile.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una palabra o sintagma que describe un sello o una técnica similar.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stamp-egXML-ba">
      <rubric>Apologyticu TTVLLIANI AC IGNORATIA IN XPO IHV<lb/>
SI NON LICET<lb/>
NOBIS RO<lb/>
manii imperii <stamp>Bodleian stamp</stamp>
            <lb/>
         </rubric>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stamp-egXML-lu">
      <rubric>Apologyticu TTVLLIANI AC IGNORATIA IN XPO IHV<lb/> SI NON LICET<lb/> NOBIS RO<lb/>
          manii imperii <stamp>Bodleian stamp</stamp>
            <lb/>
         </rubric>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stamp-egXML-hv">
      <rubric>乾隆御覽之寶<stamp>清乾隆玉璽</stamp>
            <lb/>
         </rubric>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mswat"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">stamp</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">cachet</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-02-16" xml:lang="en">contains a word or phrase describing a stamp or similar device.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">스탬프 또는 유사한 도구를 기술하는 단어 또는 구를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個字詞，描述一個印記或是類似圖案。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">印などにある語句を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">contient un mot ou une expression décrivant un cachet ou une marque du même genre.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene una parola o un sintagma che descrive un timbro o simile.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una palabra o sintagma que describe un sello o una técnica similar.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.pPart.msdesc"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stamp-egXML-ba">
      <rubric>Apologyticu TTVLLIANI AC IGNORATIA IN XPO IHV<lb/>
SI NON LICET<lb/>
NOBIS RO<lb/>
manii imperii <stamp>Bodleian stamp</stamp>
            <lb/>
         </rubric>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stamp-egXML-lu">
      <rubric>Apologyticu TTVLLIANI AC IGNORATIA IN XPO IHV<lb/> SI NON LICET<lb/> NOBIS RO<lb/>
          manii imperii <stamp>Bodleian stamp</stamp>
            <lb/>
         </rubric>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-stamp-egXML-hv">
      <rubric>乾隆御覽之寶<stamp>清乾隆玉璽</stamp>
            <lb/>
         </rubric>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mswat"/>
  </listRef>
```

^b15

