---
type: representation
source-type: document
source: '[[00_sources/tei-p5-surrogates-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 surrogates
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/surrogates.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# surrogates

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3730. Git blob: `29620861532877d325dff883791d21a4c24ccbd6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="SURROGATES" ident="surrogates">
  <gloss versionDate="2007-06-12" xml:lang="en">surrogates</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">reproductions</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="surrogates.desc">contains information about any representations of the manuscript or other object being described which
may exist in the holding institution or elsewhere.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">보유 기관 또는 다른 곳에서 있을 수 있는 원고의 디지털 또는 사진 표시에 관한 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含關於任何手稿的數位化或攝影呈現的資訊，可能存在於保管機構或是其他地方。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料が電子化されたものまたは写真の表現に関する情報を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur toute reproduction
      numérique ou photographique du manuscrit en cours de description, qu'elle soit détenue par
      l'institution de conservation ou ailleurs.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene informaciones relativas a eventuales representaciones digitales o gráficas del manuscrito en exámen eventualmente existentes en la institución depositaria o en cualquier otro lugar.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative a eventuali rappresentazioni digitali o grafiche del manoscritto in esame eventualmente esistenti nell'istituzione depositaria o altrove.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SURROGATES-egXML-zw">
      <surrogates>
        <bibl>
          <title type="gmd">diapositive</title>
          <idno>AM 74 a, fol.</idno>
          <date>May 1984</date>
        </bibl>
        <bibl>
          <title type="gmd">b/w prints</title>
          <idno>AM 75 a, fol.</idno>
          <date>1972</date>
        </bibl>
      </surrogates>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SURROGATES-egXML-cj">
      <surrogates>
        <p>
          <bibl>
            <title type="gmd">diapositive</title>
            <idno>AM 74 a, fol.</idno>
            <date>May 1984</date>
          </bibl>
          <bibl>
            <title type="gmd">b/w prints</title>
            <idno>AM 75 a, fol.</idno>
            <date>1972</date>
          </bibl>
        </p>
      </surrogates>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SURROGATES-egXML-ij">
      <surrogates>
        <bibl>
          <title type="gmd">透明正片</title>
          <idno>AM 74 a, fol.</idno>
          <date>May 1984</date>
        </bibl>
        <bibl>
          <title type="gmd">黑白輸出</title>
          <idno>AM 75 a, fol.</idno>
          <date>1972</date>
        </bibl>
      </surrogates>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msad"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">surrogates</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">reproductions</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="surrogates.desc">contains information about any representations of the manuscript or other object being described which
may exist in the holding institution or elsewhere.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">보유 기관 또는 다른 곳에서 있을 수 있는 원고의 디지털 또는 사진 표시에 관한 정보를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含關於任何手稿的數位化或攝影呈現的資訊，可能存在於保管機構或是其他地方。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料が電子化されたものまたは写真の表現に関する情報を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient des informations sur toute reproduction
      numérique ou photographique du manuscrit en cours de description, qu'elle soit détenue par
      l'institution de conservation ou ailleurs.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene informaciones relativas a eventuales representaciones digitales o gráficas del manuscrito en exámen eventualmente existentes en la institución depositaria o en cualquier otro lugar.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative a eventuali rappresentazioni digitali o grafiche del manoscritto in esame eventualmente esistenti nell'istituzione depositaria o altrove.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SURROGATES-egXML-zw">
      <surrogates>
        <bibl>
          <title type="gmd">diapositive</title>
          <idno>AM 74 a, fol.</idno>
          <date>May 1984</date>
        </bibl>
        <bibl>
          <title type="gmd">b/w prints</title>
          <idno>AM 75 a, fol.</idno>
          <date>1972</date>
        </bibl>
      </surrogates>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SURROGATES-egXML-cj">
      <surrogates>
        <p>
          <bibl>
            <title type="gmd">diapositive</title>
            <idno>AM 74 a, fol.</idno>
            <date>May 1984</date>
          </bibl>
          <bibl>
            <title type="gmd">b/w prints</title>
            <idno>AM 75 a, fol.</idno>
            <date>1972</date>
          </bibl>
        </p>
      </surrogates>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="SURROGATES-egXML-ij">
      <surrogates>
        <bibl>
          <title type="gmd">透明正片</title>
          <idno>AM 74 a, fol.</idno>
          <date>May 1984</date>
        </bibl>
        <bibl>
          <title type="gmd">黑白輸出</title>
          <idno>AM 75 a, fol.</idno>
          <date>1972</date>
        </bibl>
      </surrogates>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msad"/>
  </listRef>
```

^b15

