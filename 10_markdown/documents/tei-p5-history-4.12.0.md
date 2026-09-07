---
type: representation
source-type: document
source: '[[00_sources/tei-p5-history-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 history
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/history.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# history

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4540. Git blob: `fcb67110890904bba6572c59fee949da5843a05f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="HISTORY" ident="history">
  <gloss versionDate="2007-06-12" xml:lang="en">history</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">histoire</gloss>
  <desc versionDate="2018-10-26" xml:lang="en" xml:id="history.desc"> groups elements
describing the full history of a manuscript, manuscript part, or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고 일부의 전체 이력을 기술하는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集描述手稿或手稿部分完整歷史的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の歴史を表す要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">rassemble les éléments servant à donner un historique
      complet du manuscrit ou d'une partie du manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que describen la historia completa de un manuscrito o de una de sus partes.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che descrivono la storia completa di un manoscritto o di una sua parte.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <!--<!ELEMENT history  - -  (p+ | (origin?, provenance*, acquisition?))>-->
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="origin" minOccurs="0"/>
        
        
          <elementRef key="provenance" minOccurs="0" maxOccurs="unbounded"/>
        
        
          <elementRef key="acquisition" minOccurs="0"/>
        
      </sequence>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HISTORY-egXML-zj">
      <history>
        <origin>
          <p>Written in Durham during the mid twelfth
century.</p>
        </origin>
        <provenance>
          <p>Recorded in two medieval
catalogues of the books belonging to Durham Priory, made in 1391 and
1405.</p>
        </provenance>
        <provenance>
          <p>Given to W. Olleyf by William Ebchester, Prior (1446-56)
and later belonged to Henry Dalton, Prior of Holy Island (Lindisfarne)
according to inscriptions on ff. 4v and 5.</p>
        </provenance>
        <acquisition>
          <p>Presented to Trinity College in 1738 by
Thomas Gale and his son Roger.</p>
        </acquisition>
      </history>
    </egXML>
  </exemplum>
  <!-- suppressing this incomplete example for now (LB)  -->
  <!--  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" source="#fr-ex-BnF-Reliures">
      <history>
        <origin notBefore="1750-01-01" notAfter="1750-12-31">
          <p>Reliure exécutée par Louis-François Le Monnier (signature), Paris, vers 1750 d'après
                <ref target="#fr_bib01">Michon, 1956 (n° 38 (120)</ref> .</p>
        </origin>
        <provenance>
          <p/>
        </provenance>
        <acquisition notBefore="1833-12-31" notAfter="1848-01-31">Estampille n° 24, utilisée de
            1833 à 1848</acquisition>
      </history>
    </egXML>
  </exemplum>-->
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HISTORY-egXML-qs" source="#biblzh-tw_n45">
      <history>
        <origin>
          <p>最早由迦葉尊者以梵文手寫。</p>
        </origin>
        <provenance>
          <p>後由菩提達摩傳給慧思禪師，再經由小野妹子於推古天皇十七年（西元609年）傳入日本。</p>
          <p>淨嚴和尚於1694年以梵文悉曇體手寫抄錄。</p>
          <p>穆勒（Max Muller）於1884年轉寫成天城體及羅馬拼音，傳至歐美國家。</p>
        </provenance>
        <acquisition>
          <p>現收藏於東京博物館。</p>
        </acquisition>
      </history>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#mshy"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">history</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">histoire</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-10-26" xml:lang="en" xml:id="history.desc"> groups elements
describing the full history of a manuscript, manuscript part, or other object.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고 일부의 전체 이력을 기술하는 요소를 모아 놓는다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集描述手稿或手稿部分完整歷史的元素。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の歴史を表す要素をまとめる。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">rassemble les éléments servant à donner un historique
      complet du manuscrit ou d'une partie du manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que describen la historia completa de un manuscrito o de una de sus partes.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa gli elementi che descrivono la storia completa di un manoscritto o di una sua parte.</desc>
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
    <!--<!ELEMENT history  - -  (p+ | (origin?, provenance*, acquisition?))>-->
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="origin" minOccurs="0"/>
        
        
          <elementRef key="provenance" minOccurs="0" maxOccurs="unbounded"/>
        
        
          <elementRef key="acquisition" minOccurs="0"/>
        
      </sequence>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HISTORY-egXML-zj">
      <history>
        <origin>
          <p>Written in Durham during the mid twelfth
century.</p>
        </origin>
        <provenance>
          <p>Recorded in two medieval
catalogues of the books belonging to Durham Priory, made in 1391 and
1405.</p>
        </provenance>
        <provenance>
          <p>Given to W. Olleyf by William Ebchester, Prior (1446-56)
and later belonged to Henry Dalton, Prior of Holy Island (Lindisfarne)
according to inscriptions on ff. 4v and 5.</p>
        </provenance>
        <acquisition>
          <p>Presented to Trinity College in 1738 by
Thomas Gale and his son Roger.</p>
        </acquisition>
      </history>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HISTORY-egXML-qs" source="#biblzh-tw_n45">
      <history>
        <origin>
          <p>最早由迦葉尊者以梵文手寫。</p>
        </origin>
        <provenance>
          <p>後由菩提達摩傳給慧思禪師，再經由小野妹子於推古天皇十七年（西元609年）傳入日本。</p>
          <p>淨嚴和尚於1694年以梵文悉曇體手寫抄錄。</p>
          <p>穆勒（Max Muller）於1884年轉寫成天城體及羅馬拼音，傳至歐美國家。</p>
        </provenance>
        <acquisition>
          <p>現收藏於東京博物館。</p>
        </acquisition>
      </history>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#mshy"/>
  </listRef>
```

^b14

