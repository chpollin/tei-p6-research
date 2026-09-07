---
type: representation
source-type: document
source: '[[00_sources/tei-p5-collation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 collation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/collation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# collation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4599. Git blob: `e4869bb6fe3f72686938cb75aa3ce5dfed09b0de`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="COLLATION" ident="collation">
  <gloss versionDate="2007-06-12" xml:lang="en">collation</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">collation</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="collation.desc">contains a description of how the leaves, bifolia, or similar objects are physically
arranged.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">장 또는 두 장이 물리적으로 배열된 방법에 대한 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述頁面紙張的排列組成。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該の葉または一度折られた折丁が、物理的にどのように構成されているか
  を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description de l'organisation des
      feuillets ou bifeuillets d'un manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de cómo los folios o bifolios están físicamente dispuestos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione di come i fogli o bifolia siano fisicamente disposti.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-zq">
      <collation>The written leaves preceded by an original flyleaf, 
conjoint with the pastedown.</collation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-ph">
      <collation>The written leaves preceded by an original flyleaf, conjoint with the
        pastedown.</collation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-ew">
      <collation>
	<p>
	  <formula>1-5.8 6.6 (catchword, f. 46, does not match following text) 7-8.8 9.10, 11.2
	  (through f. 82) 12-14.8 15.8(-7)</formula>
	  <catchwords>Catchwords are written horizontally in center or towards the right lower
	  margin in various manners: in red ink for quires 1-6 (which are also signed in red ink
	  with letters of the alphabet and arabic numerals); quires 7-9 in ink of text within
	  yellow decorated frames; quire 10 in red decorated frame; quire 12 in ink of text;
	  quire 13 with red decorative slashes; quire 14 added in cursive hand.</catchwords>
	</p>
      </collation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-zu">
      <collation>經板分為內外兩層，外層上下各一塊紅漆木質經板，其正面有「唵嘛呢叭咪吽」六個梵文金字。</collation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-jv" source="#biblzh-tw_n39">
      <collation>
        <p>此物屬「沓姆」，即用西雙版納傣文書寫的佛經，頁面打折；打折是為了讓一頁變為多頁並折疊成一冊，其折出的每一頁的寬度和長度皆與作為書寫介質的貝葉相當。</p>
      </collation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-bq">
      <collation>
	<p>
	  <formula>1-5.8 6.6 (catchword, f. 46, does not match following text) 
	  7-8.8 9.10, 11.2 (through f. 82) 12-14.8 15.8(-7)</formula>
	  <catchwords>Catchwords are written horizontally in center 
	  or towards the right lower margin in various manners: 
	  in red ink for quires 1-6 (which are also signed in red 
	  ink with letters of the alphabet and arabic numerals); 
	  quires 7-9 in ink of text within yellow decorated frames; 
	  quire 10 in red decorated frame; quire 12 in ink of text; 
	  quire 13 with red decorative slashes; quire 14 added in 
	  cursive hand.</catchwords>
	</p>
      </collation>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">collation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">collation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="collation.desc">contains a description of how the leaves, bifolia, or similar objects are physically
arranged.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">장 또는 두 장이 물리적으로 배열된 방법에 대한 기술을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述頁面紙張的排列組成。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該の葉または一度折られた折丁が、物理的にどのように構成されているか
  を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description de l'organisation des
      feuillets ou bifeuillets d'un manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de cómo los folios o bifolios están físicamente dispuestos.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione di come i fogli o bifolia siano fisicamente disposti.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-zq">
      <collation>The written leaves preceded by an original flyleaf, 
conjoint with the pastedown.</collation>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-ph">
      <collation>The written leaves preceded by an original flyleaf, conjoint with the
        pastedown.</collation>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-ew">
      <collation>
	<p>
	  <formula>1-5.8 6.6 (catchword, f. 46, does not match following text) 7-8.8 9.10, 11.2
	  (through f. 82) 12-14.8 15.8(-7)</formula>
	  <catchwords>Catchwords are written horizontally in center or towards the right lower
	  margin in various manners: in red ink for quires 1-6 (which are also signed in red ink
	  with letters of the alphabet and arabic numerals); quires 7-9 in ink of text within
	  yellow decorated frames; quire 10 in red decorated frame; quire 12 in ink of text;
	  quire 13 with red decorative slashes; quire 14 added in cursive hand.</catchwords>
	</p>
      </collation>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-zu">
      <collation>經板分為內外兩層，外層上下各一塊紅漆木質經板，其正面有「唵嘛呢叭咪吽」六個梵文金字。</collation>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-jv" source="#biblzh-tw_n39">
      <collation>
        <p>此物屬「沓姆」，即用西雙版納傣文書寫的佛經，頁面打折；打折是為了讓一頁變為多頁並折疊成一冊，其折出的每一頁的寬度和長度皆與作為書寫介質的貝葉相當。</p>
      </collation>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="COLLATION-egXML-bq">
      <collation>
	<p>
	  <formula>1-5.8 6.6 (catchword, f. 46, does not match following text) 
	  7-8.8 9.10, 11.2 (through f. 82) 12-14.8 15.8(-7)</formula>
	  <catchwords>Catchwords are written horizontally in center 
	  or towards the right lower margin in various manners: 
	  in red ink for quires 1-6 (which are also signed in red 
	  ink with letters of the alphabet and arabic numerals); 
	  quires 7-9 in ink of text within yellow decorated frames; 
	  quire 10 in red decorated frame; quire 12 in ink of text; 
	  quire 13 with red decorative slashes; quire 14 added in 
	  cursive hand.</catchwords>
	</p>
      </collation>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph1"/>
  </listRef>
```

^b18

