---
type: representation
source-type: document
source: '[[00_sources/tei-p5-handdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 handDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/handDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# handDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6386. Git blob: `527eb043a41f6fa7d0c4a5e5c7df7e8f347b4d92`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="HANDDESC" ident="handDesc">
  <gloss versionDate="2007-08-01" xml:lang="en">description of hands</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">기법 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">descripción de las manos</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description des écritures</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">descrizione delle mani</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="script.desc">contains a description of all the different hands used in a manuscript or other object.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고에 사용된 모든 종류의 기법 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">手稿中使用的所有不同書寫種類的描述。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料にある異なる書記全てについての解説を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description des différents types
      d'écriture utilisés dans un manuscrit.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de todos los diferentes tipos de escritura usados en un manuscrito.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione dei diversi tipi di scrittura usati in un manoscritto.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
  <content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="handNote" minOccurs="1" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
  <attList>
    <attDef ident="hands">
      <gloss versionDate="2007-06-12" xml:lang="en">hands</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">mains</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">specifies the number of distinct hands identified within the manuscript.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">원고 내에서 식별되는 필적 수를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明在手稿中可清楚識別的書寫者人數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料中で特定可能な筆致の数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie le nombre de mains différentes qui ont
          pu être identifiées dans le manuscrit.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el número de manos distintas identificadas al interno de un manuscrito.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il numero delle diverse mani identificate all'interno del manoscritto.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-ar">
      <handDesc>
        <handNote scope="major">Written throughout in <term>angelicana formata</term>.</handNote>
      </handDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-yr">
      <handDesc>
        <handNote scope="major">Written throughout in <term>angelicana formata</term>.</handNote>
      </handDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-nr">
      <handDesc hands="2">
        <p>The manuscript is written in two contemporary hands, otherwise unknown, but clearly
            those of practised scribes. Hand I writes ff. 1r-22v and hand II ff. 23 and 24. Some
            scholars, notably Verner Dahlerup and Hreinn Benediktsson, have argued for a third hand
            on f. 24, but the evidence for this is insubstantial.</p>
      </handDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-bq">
      <handDesc hands="2">
        <handNote xml:id="fr_TSE" medium="typescript">Authorial typescript </handNote>
        <handNote xml:id="fr_EP" medium="red-ink">Ezra Pound's annotations</handNote>
      </handDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-tk" source="#biblzh-tw_n43">
      <handDesc hands="1">
        <p>手稿由田代安定一人控稿，同行者包括鳥居龍藏（帝國大學人類學調查員）；上領小太郎（舊民政局殖產課員）；三宅驥（帝國大學職務調查員）；小笠原富次郎（總統府技手殖產課員）。</p>
      </handDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-yg">
      <handDesc hands="2">
        <handNote xml:id="zh-tw_TSE" medium="typescript">作者打字稿</handNote>
        <handNote xml:id="zh-tw_SM" medium="red-ink">三毛的註解</handNote>
      </handDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-dq">
      <handDesc hands="2">
        <p>The manuscript is written in two contemporary hands, otherwise
unknown, but clearly those of practised scribes.  Hand I writes
ff. 1r-22v and hand II ff. 23 and 24. Some scholars, notably
Verner Dahlerup and Hreinn Benediktsson, have argued for a third hand
on f. 24, but the evidence for this is insubstantial.</p>
      </handDesc>
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
<gloss versionDate="2007-08-01" xml:lang="en">description of hands</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">기법 기술</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">descripción de las manos</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description des écritures</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">descrizione delle mani</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="script.desc">contains a description of all the different hands used in a manuscript or other object.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고에 사용된 모든 종류의 기법 기술을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">手稿中使用的所有不同書寫種類的描述。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料にある異なる書記全てについての解説を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description des différents types
      d'écriture utilisés dans un manuscrit.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de todos los diferentes tipos de escritura usados en un manuscrito.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione dei diversi tipi di scrittura usati in un manoscritto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      
      <sequence>
        
          <elementRef key="summary" minOccurs="0"/>
        
        
          <elementRef key="handNote" minOccurs="1" maxOccurs="unbounded"/>
        
      </sequence>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">hands</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">mains</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the number of distinct hands identified within the manuscript.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 내에서 식별되는 필적 수를 명시한다.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明在手稿中可清楚識別的書寫者人數。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料中で特定可能な筆致の数を示す。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie le nombre de mains différentes qui ont
          pu être identifiées dans le manuscrit.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el número de manos distintas identificadas al interno de un manuscrito.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il numero delle diverse mani identificate all'interno del manoscritto.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-ar">
      <handDesc>
        <handNote scope="major">Written throughout in <term>angelicana formata</term>.</handNote>
      </handDesc>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-yr">
      <handDesc>
        <handNote scope="major">Written throughout in <term>angelicana formata</term>.</handNote>
      </handDesc>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-nr">
      <handDesc hands="2">
        <p>The manuscript is written in two contemporary hands, otherwise unknown, but clearly
            those of practised scribes. Hand I writes ff. 1r-22v and hand II ff. 23 and 24. Some
            scholars, notably Verner Dahlerup and Hreinn Benediktsson, have argued for a third hand
            on f. 24, but the evidence for this is insubstantial.</p>
      </handDesc>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-bq">
      <handDesc hands="2">
        <handNote xml:id="fr_TSE" medium="typescript">Authorial typescript </handNote>
        <handNote xml:id="fr_EP" medium="red-ink">Ezra Pound's annotations</handNote>
      </handDesc>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-tk" source="#biblzh-tw_n43">
      <handDesc hands="1">
        <p>手稿由田代安定一人控稿，同行者包括鳥居龍藏（帝國大學人類學調查員）；上領小太郎（舊民政局殖產課員）；三宅驥（帝國大學職務調查員）；小笠原富次郎（總統府技手殖產課員）。</p>
      </handDesc>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-yg">
      <handDesc hands="2">
        <handNote xml:id="zh-tw_TSE" medium="typescript">作者打字稿</handNote>
        <handNote xml:id="zh-tw_SM" medium="red-ink">三毛的註解</handNote>
      </handDesc>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="HANDDESC-egXML-dq">
      <handDesc hands="2">
        <p>The manuscript is written in two contemporary hands, otherwise
unknown, but clearly those of practised scribes.  Hand I writes
ff. 1r-22v and hand II ff. 23 and 24. Some scholars, notably
Verner Dahlerup and Hreinn Benediktsson, have argued for a third hand
on f. 24, but the evidence for this is insubstantial.</p>
      </handDesc>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph2"/>
  </listRef>
```

^b33

