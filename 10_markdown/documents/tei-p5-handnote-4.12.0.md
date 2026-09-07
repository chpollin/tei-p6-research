---
type: representation
source-type: document
source: '[[00_sources/tei-p5-handnote-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 handNote
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/handNote.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# handNote

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4484. Git blob: `01155b6ddad4d5eb3c1c493709faf8db833e6d8c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="HANDNOTE" ident="handNote">
  <gloss versionDate="2005-01-14" xml:lang="en">note on hand</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">기법에 관한 설명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">書寫特徵</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">note sur une main</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">notas sobre la mano</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nota sulla mano</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes a particular style or hand distinguished within a manuscript.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 내에서 구분되는 특별한 문체 또는 기법을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述在手稿中可明顯辨識出的特殊風格或書寫手法。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料中にある特定のスタイルまたは筆致を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">décrit un style d'écriture ou une main qui sont reconnus dans un manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe un determinado estilo o una determinada mano al interno de un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive un determinato stile o una determinata mano all'interno di un manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.handFeatures"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <!-- This is a translation of "HANDNOTE-egXML-yi" -->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDNOTE-egXML-yi_en" source="#bib4handnoteyi">
      <handNotes>
	<handNote xml:id="yien.major_hand" scope="major" medium="brown_ink" scribe="author" scribeRef="#KL">Handwriting of the copyist Karol Libelt, brown ink, in German cursive script.</handNote>
	<handNote xml:id="yien.pencil" scope="minor" medium="pencil" scribe="annotator">A note, pencil, unknown author.</handNote>
	<handNote xml:id="yien.pencil2" scope="minor" medium="pencil" scribe="archivist">Writer of the title page Józef Łepkowski, pencil.</handNote>
	<handNote xml:id="yien.pencil3" scope="minor" medium="pencil" scribe="archivist2" scribeRef="#BJK">Note on the title page, pencil, by Józef Korzeniowski.</handNote>
      </handNotes>
    </egXML>
  </exemplum>
  <exemplum xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDNOTE-egXML-yi" source="#bib4handnoteyi">
      <handNotes>
	<handNote xml:id="yide.major_hand" scope="major" medium="brown_ink" scribe="author" scribeRef="#KL">Hand des Nachschreibers Karol Libelt, braune Tinte, vorwiegend in Kurrentschrift.</handNote>
	<handNote xml:id="yide.pencil" scope="minor" medium="pencil" scribe="annotator">Eine Anmerkung, Bleistift, unbekannter Verfasser.</handNote>
	<handNote xml:id="yide.pencil2" scope="minor" medium="pencil" scribe="archivist">Schreiber des Titelblattes Józef Łepkowski, Bleistift.</handNote>
	<handNote xml:id="yide.pencil3" scope="minor" medium="pencil" scribe="archivist2" scribeRef="#BJK">Anmerkung auf dem Titelblatt, Bleistift, von Józef Korzeniowski.</handNote>
      </handNotes>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDNOTE-egXML-zj" source="#fr-ex-Lavrentev-TEI-BFM">
      <handNote xml:id="fr_scribe1">
	Premier scribe : <name type="person">inconnu</name> 
      </handNote>
      <handNote xml:id="fr_rubricateur1">
	Premier rubricateur : <name type="person">inconnu</name> 
      </handNote>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDNOTE-egXML-ca">
      <handNote scope="sole">
        <p>以類似小篆字體書寫，行間有以隸書寫成的古文字。</p>
      </handNote>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">note on hand</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">기법에 관한 설명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">書寫特徵</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">note sur une main</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">notas sobre la mano</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">nota sulla mano</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes a particular style or hand distinguished within a manuscript.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 내에서 구분되는 특별한 문체 또는 기법을 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述在手稿中可明顯辨識出的特殊風格或書寫手法。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料中にある特定のスタイルまたは筆致を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">décrit un style d'écriture ou une main qui sont reconnus dans un manuscrit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe un determinado estilo o una determinada mano al interno de un manuscrito.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive un determinato stile o una determinata mano all'interno di un manoscritto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.handFeatures"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <!-- This is a translation of "HANDNOTE-egXML-yi" -->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDNOTE-egXML-yi_en" source="#bib4handnoteyi">
      <handNotes>
	<handNote xml:id="yien.major_hand" scope="major" medium="brown_ink" scribe="author" scribeRef="#KL">Handwriting of the copyist Karol Libelt, brown ink, in German cursive script.</handNote>
	<handNote xml:id="yien.pencil" scope="minor" medium="pencil" scribe="annotator">A note, pencil, unknown author.</handNote>
	<handNote xml:id="yien.pencil2" scope="minor" medium="pencil" scribe="archivist">Writer of the title page Józef Łepkowski, pencil.</handNote>
	<handNote xml:id="yien.pencil3" scope="minor" medium="pencil" scribe="archivist2" scribeRef="#BJK">Note on the title page, pencil, by Józef Korzeniowski.</handNote>
      </handNotes>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDNOTE-egXML-yi" source="#bib4handnoteyi">
      <handNotes>
	<handNote xml:id="yide.major_hand" scope="major" medium="brown_ink" scribe="author" scribeRef="#KL">Hand des Nachschreibers Karol Libelt, braune Tinte, vorwiegend in Kurrentschrift.</handNote>
	<handNote xml:id="yide.pencil" scope="minor" medium="pencil" scribe="annotator">Eine Anmerkung, Bleistift, unbekannter Verfasser.</handNote>
	<handNote xml:id="yide.pencil2" scope="minor" medium="pencil" scribe="archivist">Schreiber des Titelblattes Józef Łepkowski, Bleistift.</handNote>
	<handNote xml:id="yide.pencil3" scope="minor" medium="pencil" scribe="archivist2" scribeRef="#BJK">Anmerkung auf dem Titelblatt, Bleistift, von Józef Korzeniowski.</handNote>
      </handNotes>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDNOTE-egXML-zj" source="#fr-ex-Lavrentev-TEI-BFM">
      <handNote xml:id="fr_scribe1">
	Premier scribe : <name type="person">inconnu</name> 
      </handNote>
      <handNote xml:id="fr_rubricateur1">
	Premier rubricateur : <name type="person">inconnu</name> 
      </handNote>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDNOTE-egXML-ca">
      <handNote scope="sole">
        <p>以類似小篆字體書寫，行間有以隸書寫成的古文字。</p>
      </handNote>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph2"/>
  </listRef>
```

^b20

