---
type: representation
source-type: document
source: '[[00_sources/tei-p5-placename-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 placeName
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/placeName.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# placeName

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4310. Git blob: `fe13687b5bf5ca239db161256f5e0e31da1c72b0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-placeName" ident="placeName">
  <gloss versionDate="2020-12-20" xml:lang="en">place name</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">nom de lieu</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an absolute or relative place name.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">절대적 또는 상대적 위치명을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個確切位置或相對位置的名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">絶対的、相対的場所名を示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient un nom de lieu absolu ou relatif.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la indicación absoluta o relativa de un nombre de lugar.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene l'indicazione assoluta o relativa di un nome di luogo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeNamePart"/>
    <memberOf key="model.settingPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-ud">
      <placeName>
        <settlement>Rochester</settlement>
        <region>New York</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-ko">
      <placeName>
        <settlement>Bordeaux</settlement>
        <region>Gironde</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-lp">
      <placeName>
        <geogName>Le Massif Armoricain</geogName>
        <region>Bretagne</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-um">
      <placeName>
        <measure>2,5 milles</measure>
        <offset>à l'ouest de la </offset>
        <settlement>Pointe du Raz</settlement>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-lh">
      <placeName>
        <settlement>曼徹斯特</settlement>
        <region>紐約</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-qt">
      <placeName>
        <geogName>天池</geogName>
        <region>新疆</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-oo">
      <placeName>
        <settlement>烏魯木齊</settlement>
        <offset>北邊</offset>
        <measure>十哩</measure>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-vi">
      <placeName>
        <geogName>Arrochar Alps</geogName>
        <region>Argylshire</region>
      </placeName>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-iq">
      <placeName>
        <measure>10 miles</measure>
        <offset>Northeast of</offset>
        <settlement>Attica</settlement>
      </placeName>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">place name</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">nom de lieu</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an absolute or relative place name.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">절대적 또는 상대적 위치명을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個確切位置或相對位置的名稱。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">絶対的、相対的場所名を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">contient un nom de lieu absolu ou relatif.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene la indicación absoluta o relativa de un nombre de lugar.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene l'indicazione assoluta o relativa di un nome di luogo.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.placeNamePart"/>
    <memberOf key="model.settingPart"/>
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
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-ud">
      <placeName>
        <settlement>Rochester</settlement>
        <region>New York</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-ko">
      <placeName>
        <settlement>Bordeaux</settlement>
        <region>Gironde</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-lp">
      <placeName>
        <geogName>Le Massif Armoricain</geogName>
        <region>Bretagne</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-um">
      <placeName>
        <measure>2,5 milles</measure>
        <offset>à l'ouest de la </offset>
        <settlement>Pointe du Raz</settlement>
      </placeName>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-lh">
      <placeName>
        <settlement>曼徹斯特</settlement>
        <region>紐約</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-qt">
      <placeName>
        <geogName>天池</geogName>
        <region>新疆</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-oo">
      <placeName>
        <settlement>烏魯木齊</settlement>
        <offset>北邊</offset>
        <measure>十哩</measure>
      </placeName>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-vi">
      <placeName>
        <geogName>Arrochar Alps</geogName>
        <region>Argylshire</region>
      </placeName>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[9]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-placeName-egXML-iq">
      <placeName>
        <measure>10 miles</measure>
        <offset>Northeast of</offset>
        <settlement>Attica</settlement>
      </placeName>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPLAC"/>
  </listRef>
```

^b21

