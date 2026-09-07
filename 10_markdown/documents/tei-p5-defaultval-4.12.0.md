---
type: representation
source-type: document
source: '[[00_sources/tei-p5-defaultval-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 defaultVal
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/defaultVal.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# defaultVal

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3021. Git blob: `88b66fbc1023e7a590162aa7a2e343754ac05f99`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-defaultVal" ident="defaultVal">
  <gloss versionDate="2007-07-04" xml:lang="en">default value</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">기본 값</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">valor por defecto</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">valeur par défaut</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">valore predefinito</gloss>
  <gloss versionDate="2024-08-12" xml:lang="ja">既定値</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies the default declared value for an attribute.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">속성에 대한 기본 선언 값을 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明屬性的預設宣告值。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">属性の既定値を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">précise la valeur déclarée par défaut pour un
			attribut.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica el valor predefinido declarado para un atributo</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica il valore predefinito dichiarato per un attributo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-defaultVal-egXML-mc">
      <defaultVal>#IMPLIED</defaultVal>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-defaultVal-egXML-gb">
      <defaultVal>#IMPLIED</defaultVal>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-defaultVal-egXML-ke">
      <defaultVal>預設值</defaultVal>
    </egXML>
  </exemplum>
  <remarks ident="defaultVal-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">any legal declared value or TEI-defined keyword</p>
  </remarks>
  <remarks ident="defaultVal-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Toute valeur déclarée dans les règles ou tout mot-clé défini en
            TEI.</p>
  </remarks>
  <remarks ident="defaultVal-remarks" versionDate="2024-08-12" xml:lang="ja">
    <p rend="dataDesc">
      予約された値もしくはTEIで定義されたキーワード。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TDATT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">default value</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">기본 값</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">valor por defecto</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">valeur par défaut</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">valore predefinito</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2024-08-12" xml:lang="ja">既定値</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the default declared value for an attribute.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">속성에 대한 기본 선언 값을 명시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明屬性的預設宣告值。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">属性の既定値を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise la valeur déclarée par défaut pour un
			attribut.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el valor predefinido declarado para un atributo</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il valore predefinito dichiarato per un attributo.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.combinable"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-defaultVal-egXML-mc">
      <defaultVal>#IMPLIED</defaultVal>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-defaultVal-egXML-gb">
      <defaultVal>#IMPLIED</defaultVal>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-defaultVal-egXML-ke">
      <defaultVal>預設值</defaultVal>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="defaultVal-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">any legal declared value or TEI-defined keyword</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="defaultVal-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Toute valeur déclarée dans les règles ou tout mot-clé défini en
            TEI.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="defaultVal-remarks" versionDate="2024-08-12" xml:lang="ja">
    <p rend="dataDesc">
      予約された値もしくはTEIで定義されたキーワード。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDATT"/>
  </listRef>
```

^b23

