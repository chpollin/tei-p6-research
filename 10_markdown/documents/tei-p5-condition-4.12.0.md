---
type: representation
source-type: document
source: '[[00_sources/tei-p5-condition-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 condition
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/condition.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# condition

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4221. Git blob: `c545a9fed90c39820bdc459080978e3365bcc8f7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="CONDITION" ident="condition">
  <gloss versionDate="2007-06-12" xml:lang="en">condition</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">état matériel</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="condition.desc">contains a description of the physical
condition of the manuscript or object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고의 물리적 상태에 대한 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿材質狀況的描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料の、物理的な状態を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description de l'état matériel du
      manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de la condición física de un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione della condizione fisica del manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CONDITION-egXML-lm">
      <condition>
        <p>There are lacunae in three places in this
manuscript. After 14v two
leaves has been cut out and narrow strips leaves remains in the spine. After
68v one gathering is missing and after 101v at least one gathering of 8 leaves
has been lost. </p>
        <p>Several leaves are damaged with tears or holes or have a
irregular shape. Some of the damages do not allow the lines to be of full
length and they are apparently older than the script. There are tears on fol.
2r-v, 9r-v, 10r-v, 15r-18v, 19r-v, 20r-22v, 23r-v, 24r-28v, 30r-v, 32r-35v,
37r-v, 38r-v, 40r-43v, 45r-47v, 49r-v, 51r-v, 53r-60v, 67r-v, 68r-v, 70r-v,
74r-80v, 82r-v, 86r-v, 88r-v, 89r-v, 95r-v, 97r-98v 99r-v, 100r-v. On fol. 98
the corner has been torn off. Several leaves are in a bad condition due to
moist and wear, and have become dark, bleached or
wrinkled. </p>
        <p>The script has been
touched up in the 17th century with black ink. The touching up on the following
fols. was done by 
<name>Bishop Brynjólf Sveinsson</name>: 1v, 3r, 4r, 5r,
6v, 8v,9r, 10r, 14r, 14v, 22r,30v, 36r-52v, 72v, 77r,78r,103r, 104r,. An
AM-note says according to the lawman 
<name>Sigurður Björnsson</name> that the rest of the
touching up was done by himself and another lawman 
<name>Sigurður Jónsson</name>. 
<name>Sigurður Björnsson</name> did the touching up
on the following fols.: 46v, 47r, 48r, 49r-v, 50r, 52r-v. 
<name>Sigurður Jónsson</name> did the rest of the
touching up in the section 36r-59r containing 
<title>Bretasögur</title> 
            </p>
      </condition>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CONDITION-egXML-ha" source="#fr-ex-BnF-Reliures">
      <condition> Traces de mouillures anciennes plus ou moins importantes au bas des feuillets,
          qui n'ont pas affecté la reliure ; éraflure en tête du plat inférieur. </condition>
      <condition>Eraflures sur les deux plats, tache d'humidité dans la partie supérieure du plat
          inférieur ; mors fendus en tête et en queue avec zones restaurées (minces bandes de
          maroquin).</condition>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CONDITION-egXML-bf" source="#biblzh-tw_n40">
      <condition>
        <p>輕度破損，本案第27至30頁缺頁。</p>
      </condition>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msphco"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">condition</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">état matériel</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="condition.desc">contains a description of the physical
condition of the manuscript or object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고의 물리적 상태에 대한 기술을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿材質狀況的描述。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料の、物理的な状態を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description de l'état matériel du
      manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de la condición física de un manuscrito.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione della condizione fisica del manoscritto.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CONDITION-egXML-lm">
      <condition>
        <p>There are lacunae in three places in this
manuscript. After 14v two
leaves has been cut out and narrow strips leaves remains in the spine. After
68v one gathering is missing and after 101v at least one gathering of 8 leaves
has been lost. </p>
        <p>Several leaves are damaged with tears or holes or have a
irregular shape. Some of the damages do not allow the lines to be of full
length and they are apparently older than the script. There are tears on fol.
2r-v, 9r-v, 10r-v, 15r-18v, 19r-v, 20r-22v, 23r-v, 24r-28v, 30r-v, 32r-35v,
37r-v, 38r-v, 40r-43v, 45r-47v, 49r-v, 51r-v, 53r-60v, 67r-v, 68r-v, 70r-v,
74r-80v, 82r-v, 86r-v, 88r-v, 89r-v, 95r-v, 97r-98v 99r-v, 100r-v. On fol. 98
the corner has been torn off. Several leaves are in a bad condition due to
moist and wear, and have become dark, bleached or
wrinkled. </p>
        <p>The script has been
touched up in the 17th century with black ink. The touching up on the following
fols. was done by 
<name>Bishop Brynjólf Sveinsson</name>: 1v, 3r, 4r, 5r,
6v, 8v,9r, 10r, 14r, 14v, 22r,30v, 36r-52v, 72v, 77r,78r,103r, 104r,. An
AM-note says according to the lawman 
<name>Sigurður Björnsson</name> that the rest of the
touching up was done by himself and another lawman 
<name>Sigurður Jónsson</name>. 
<name>Sigurður Björnsson</name> did the touching up
on the following fols.: 46v, 47r, 48r, 49r-v, 50r, 52r-v. 
<name>Sigurður Jónsson</name> did the rest of the
touching up in the section 36r-59r containing 
<title>Bretasögur</title> 
            </p>
      </condition>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CONDITION-egXML-ha" source="#fr-ex-BnF-Reliures">
      <condition> Traces de mouillures anciennes plus ou moins importantes au bas des feuillets,
          qui n'ont pas affecté la reliure ; éraflure en tête du plat inférieur. </condition>
      <condition>Eraflures sur les deux plats, tache d'humidité dans la partie supérieure du plat
          inférieur ; mors fendus en tête et en queue avec zones restaurées (minces bandes de
          maroquin).</condition>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="CONDITION-egXML-bf" source="#biblzh-tw_n40">
      <condition>
        <p>輕度破損，本案第27至30頁缺頁。</p>
      </condition>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msphco"/>
  </listRef>
```

^b15

