---
type: representation
source-type: document
source: '[[00_sources/tei-p5-birth-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 birth
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/birth.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# birth

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4855. Git blob: `630b26694542f8e4b69b26e2ceb442ee28f99f51`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-birth" ident="birth">
  <gloss versionDate="2008-12-09" xml:lang="en">birth</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">naissance</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains information about a person's birth, such as its date and place.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">날짜, 장소와 같이 개인의 출생에 관한 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人的出生資訊，例如日期及地點等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物の出生に関する情報を示す。例えば、日時や場所など。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient des informations sur la naissance d'une personne, comme la date et le lieu.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene información relativa al nacimiento de una persona, p.ej. fecha y lugar de nacimiento.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative al luogo e alla data di nascita di una persona.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.locatable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.personPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <datatype>
	<dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
	<valItem ident="caesarean">
	  <gloss versionDate="2017-06-23" xml:lang="en">caesarean section</gloss>
	  <gloss versionDate="2023-09-27" xml:lang="ja">帝王切開</gloss>
	</valItem>
	<valItem ident="vaginal">
	  <gloss versionDate="2017-06-23" xml:lang="en">vaginal delivery</gloss>
	  <gloss versionDate="2023-09-27" xml:lang="ja">普通分娩</gloss>
	</valItem>
	<valItem ident="exNihilo">
	  <gloss versionDate="2017-06-23" xml:lang="en">ex nihilo</gloss>
	  <gloss versionDate="2023-09-27" xml:lang="ja">無から</gloss>
	</valItem>
	<valItem ident="incorporated"/>
	<valItem ident="founded"/>
	<valItem ident="established"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-vv">
      <birth>Before 1920, Midlands region.</birth>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-qd">
      <birth>Années 20, dans les Pouilles.</birth>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-uc" source="#fr-ex-Winock-Jeanne">
      <birth when="1901-01-16"> Elle est née le<date> 16 janvier 1901</date> à <name type="place">Louvres</name>, alors commune de <name type="place">Seine-et-Oise</name> (aujourd'hui
          dans le <name type="place">Val-d'Oise</name>), au nord-ouest de l'actuel aéroport de<name type="place"> Roissy</name>. </birth>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-xg">
      <birth>早於1920的上海租界</birth>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-ms">
      <birth when="1960-12-10"><date>1960年12月10日</date>早晨，在一個靠近<name type="place">龍山寺</name>的小平房裡</birth>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-ez">
      <birth when="1960-12-10">In a small cottage near <name type="place">Aix-la-Chapelle</name>,
        early in the morning of <date>10 Dec 1960</date>
         </birth>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <!--Example derived from https://lim.dhil.lib.sfu.ca/BURKE1.html-->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-wh">
      <birth where="https://www.wikidata.org/wiki/Q662158">Born on the Island of <placeName>North Uist</placeName></birth>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">birth</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">naissance</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains information about a person's birth, such as its date and place.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">날짜, 장소와 같이 개인의 출생에 관한 정보를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人的出生資訊，例如日期及地點等。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">人物の出生に関する情報を示す。例えば、日時や場所など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient des informations sur la naissance d'une personne, comme la date et le lieu.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene información relativa al nacimiento de una persona, p.ej. fecha y lugar de nacimiento.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene informazioni relative al luogo e alla data di nascita di una persona.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.locatable"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.personPart"/>
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

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
	<dataRef key="teidata.enumerated"/>
      </datatype>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
	<valItem ident="caesarean">
	  <gloss versionDate="2017-06-23" xml:lang="en">caesarean section</gloss>
	  <gloss versionDate="2023-09-27" xml:lang="ja">帝王切開</gloss>
	</valItem>
	<valItem ident="vaginal">
	  <gloss versionDate="2017-06-23" xml:lang="en">vaginal delivery</gloss>
	  <gloss versionDate="2023-09-27" xml:lang="ja">普通分娩</gloss>
	</valItem>
	<valItem ident="exNihilo">
	  <gloss versionDate="2017-06-23" xml:lang="en">ex nihilo</gloss>
	  <gloss versionDate="2023-09-27" xml:lang="ja">無から</gloss>
	</valItem>
	<valItem ident="incorporated"/>
	<valItem ident="founded"/>
	<valItem ident="established"/>
      </valList>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-vv">
      <birth>Before 1920, Midlands region.</birth>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-qd">
      <birth>Années 20, dans les Pouilles.</birth>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-uc" source="#fr-ex-Winock-Jeanne">
      <birth when="1901-01-16"> Elle est née le<date> 16 janvier 1901</date> à <name type="place">Louvres</name>, alors commune de <name type="place">Seine-et-Oise</name> (aujourd'hui
          dans le <name type="place">Val-d'Oise</name>), au nord-ouest de l'actuel aéroport de<name type="place"> Roissy</name>. </birth>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-xg">
      <birth>早於1920的上海租界</birth>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-ms">
      <birth when="1960-12-10"><date>1960年12月10日</date>早晨，在一個靠近<name type="place">龍山寺</name>的小平房裡</birth>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-ez">
      <birth when="1960-12-10">In a small cottage near <name type="place">Aix-la-Chapelle</name>,
        early in the morning of <date>10 Dec 1960</date>
         </birth>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
    <!--Example derived from https://lim.dhil.lib.sfu.ca/BURKE1.html-->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-birth-egXML-wh">
      <birth where="https://www.wikidata.org/wiki/Q662158">Born on the Island of <placeName>North Uist</placeName></birth>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b21

