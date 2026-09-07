---
type: representation
source-type: document
source: '[[00_sources/tei-p5-signed-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 signed
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/signed.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# signed

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3516. Git blob: `b2918ff4bb2ced642810b8fa779d762ae52ac6cf`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-signed" ident="signed">
  <gloss versionDate="2005-01-14" xml:lang="en">signature</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">서명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">簽名</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Signatur</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">firma</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">firma</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains the closing salutation, etc., appended to a foreword,
dedicatory epistle, or other division of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">머리말, 헌정 서한 또는 텍스트의 다른 구역에 첨부되는 결문 인사.</desc>
  <desc versionDate="2008-10-02" xml:lang="fr">contient la dernière salutation,  ajoutée à un avant-propos,
    à une  dédicace ou à une autre division du texte.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含結尾致意詞等，附加在序言、獻詞、或其他文本區段中。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">(著者以外の)序文や献呈書簡などのテキスト部分にある、結びの挨拶などを
  示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">enthält die abschließende Grußformel o.Ä. die ein Vorwort, eine Widmung oder einen anderen Abschnitt des Textes beendet.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula conclusiva o de saludo pospuesta a un prefacio, dedicatoria, u otro tipo de división textual.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una formula conclusiva o di saluto posposta rispetto a una prefazione, lettera di dedica, o altra partizione testuale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divBottomPart"/>
    <memberOf key="model.divTopPart"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-signed-egXML-lq" source="#miltPo">
      <signed>Thine to command <name>Humph. Moseley</name>
         </signed>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-signed-egXML-fm" source="#swiftLaw">
      <closer>
        <signed>Sign'd and Seal'd,
	<list><item>John Bull,</item><item>Nic. Frog.</item></list>
	           </signed>
      </closer>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-signed-egXML-rm" source="#fr-ex-Mauriac-Marquise">
      <signed>votre fidèle amante, <name>Manon Lescaut.</name>
        </signed>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-signed-egXML-lr">
      <signed><name>李敖</name>，于台北。
      </signed>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DSOC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">signature</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">서명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">簽名</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Signatur</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">firma</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">firma</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains the closing salutation, etc., appended to a foreword,
dedicatory epistle, or other division of a text.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">머리말, 헌정 서한 또는 텍스트의 다른 구역에 첨부되는 결문 인사.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-10-02" xml:lang="fr">contient la dernière salutation,  ajoutée à un avant-propos,
    à une  dédicace ou à une autre division du texte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含結尾致意詞等，附加在序言、獻詞、或其他文本區段中。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">(著者以外の)序文や献呈書簡などのテキスト部分にある、結びの挨拶などを
  示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">enthält die abschließende Grußformel o.Ä. die ein Vorwort, eine Widmung oder einen anderen Abschnitt des Textes beendet.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula conclusiva o de saludo pospuesta a un prefacio, dedicatoria, u otro tipo de división textual.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una formula conclusiva o di saluto posposta rispetto a una prefazione, lettera di dedica, o altra partizione testuale.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divBottomPart"/>
    <memberOf key="model.divTopPart"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-signed-egXML-lq" source="#miltPo">
      <signed>Thine to command <name>Humph. Moseley</name>
         </signed>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-signed-egXML-fm" source="#swiftLaw">
      <closer>
        <signed>Sign'd and Seal'd,
	<list><item>John Bull,</item><item>Nic. Frog.</item></list>
	           </signed>
      </closer>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-signed-egXML-rm" source="#fr-ex-Mauriac-Marquise">
      <signed>votre fidèle amante, <name>Manon Lescaut.</name>
        </signed>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-signed-egXML-lr">
      <signed><name>李敖</name>，于台北。
      </signed>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSOC"/>
  </listRef>
```

^b21

