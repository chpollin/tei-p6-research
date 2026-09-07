---
type: representation
source-type: document
source: '[[00_sources/tei-p5-monogr-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 monogr
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/monogr.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# monogr

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7941. Git blob: `8534d2bd057cf4c3d3deef4abc9af2bc65dc8266`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-monogr" ident="monogr">
  <gloss versionDate="2005-01-14" xml:lang="en">monographic level</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">단행본 층위</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">專題層書目</gloss>
  <gloss versionDate="2008-01-06" xml:lang="fr">niveau monographique</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nivel monográfico.</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">monografia</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains bibliographic elements describing an item (e.g. a book or journal) published as an
    independent item (i.e. as a separate physical object).</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">독립 항목(즉, 독립된 물리적 개체)으로 출판된 항목(예를 들어 단행본 또는 학술지)을 기술하는
    참고문헌 요소를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含某一項目 (例如書或期刊) 的書目元素， 該項目為一獨立出版品 (即未附屬於其他出版品) 。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">独立したもの(例えば、物理的に独立したもの)として出版された対象(例え ば、書籍や雑誌)の書誌情報項目を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient des données bibliographiques décrivant un objet
    (par exemple une monographie ou une revue) publié comme un élément indépendant (i.e.
    matériellement séparé.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene los elementos bibliográficos que describen un
    ítem (p.ej. un libro o revista) publicado independientemente (es decir, como un objeto físico
    separado).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene elementi bilbiografici che descrivono un'opera
    (ad esempio un libro o una rivista) pubblicanti indipendentemente (cioè come un singolo
    oggetto).</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0">
          <sequence>
            <alternate>
              <elementRef key="author"/>
              <elementRef key="editor"/>
              <elementRef key="meeting"/>
              <elementRef key="respStmt"/>
            </alternate>
            
              <alternate minOccurs="0" maxOccurs="unbounded">
                <elementRef key="author"/>
                <elementRef key="editor"/>
                <elementRef key="meeting"/>
                <elementRef key="respStmt"/>
              </alternate>
            
            
              <elementRef key="title" minOccurs="1" maxOccurs="unbounded"/>
            
            
              <alternate minOccurs="0" maxOccurs="unbounded">
                <classRef key="model.ptrLike"/>
                <elementRef key="idno"/>
                <elementRef key="textLang"/>
                <elementRef key="editor"/>
                <elementRef key="respStmt"/>
              </alternate>
            
          </sequence>
          <sequence>
            
              <alternate minOccurs="1" maxOccurs="unbounded">
                <elementRef key="title"/>
                <classRef key="model.ptrLike"/>
                <elementRef key="idno"/>
              </alternate>
            
            
              <alternate minOccurs="0" maxOccurs="unbounded">
                <elementRef key="textLang"/>
                <elementRef key="author"/>
                <elementRef key="editor"/>
                <elementRef key="meeting"/>
                <elementRef key="respStmt"/>
              </alternate>
            
          </sequence>
          <sequence>
            <!-- specific to patents -->
            <elementRef key="authority"/>
            <elementRef key="idno"/>
          </sequence>
        </alternate>
      
      
        <elementRef key="availability" minOccurs="0" maxOccurs="unbounded"/>
      
      
        <classRef key="model.noteLike" minOccurs="0" maxOccurs="unbounded"/>
      
      <sequence minOccurs="0" maxOccurs="unbounded">
        <elementRef key="edition"/>
        
          <alternate minOccurs="0" maxOccurs="unbounded">
            <elementRef key="idno"/>
            <classRef key="model.ptrLike"/>
            <elementRef key="editor"/>
            <elementRef key="sponsor"/>
            <elementRef key="funder"/>
            <elementRef key="respStmt"/>
          </alternate>
        
      </sequence>
      <elementRef key="imprint"/>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="imprint"/>
          <elementRef key="extent"/>
          <elementRef key="biblScope"/>
        </alternate>
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-monogr-egXML-ig">
      <biblStruct>
        <analytic>
          <author>Chesnutt, David</author>
          <title>Historical Editions in the States</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <date when="1991-12">(December, 1991):</date>
          </imprint>
          <biblScope>25.6</biblScope>
          <biblScope unit="page" from="377" to="380">377–380</biblScope>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-monogr-egXML-wr">
      <biblStruct type="book">
        <monogr>
          <author>
            <persName>
              <forename>Leo Joachim</forename>
              <surname>Frachtenberg</surname>
            </persName>
          </author>
          <title type="main" level="m">Lower Umpqua Texts</title>
          <imprint>
            <pubPlace>New York</pubPlace>
            <publisher>Columbia University Press</publisher>
            <date>1914</date>
          </imprint>
        </monogr>
        <series>
          <title type="main" level="s">Columbia University Contributions to
                              Anthropology</title>
          <biblScope unit="volume">4</biblScope>
        </series>
      </biblStruct>
    </egXML>
  </exemplum>
  <remarks ident="monogr-remarks" versionDate="2012-10-26" xml:lang="en">
    <p rend="dataDesc">May contain specialized bibliographic elements, in a prescribed order.</p>
    <p>The <gi>monogr</gi> element may only occur only within a <gi>biblStruct</gi>, where its use
      is mandatory for the description of a monographic-level bibliographic item.</p>
  </remarks>
  <remarks ident="monogr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Cet élément contient des éléments de description bibliographique spécialisés,
      dans un ordre prescrit.</p>
    <p>L'élément <gi>monogr</gi> n'est disponible que dans l'élément <gi>biblStruct</gi>, où il faut
      l'utiliser pour encoder la description bibliographique d'une monographie.</p>
  </remarks>
  <remarks ident="monogr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 特別な書誌情報要素を、特定の順番でとるかもしれない。 </p>
    <p> 当該要素<gi>monogr</gi>は小論レベルの書誌項目を記述する際に必須で あるが、その際、要素<gi>biblStruct</gi>の中で高々1回出現する。 </p>
  </remarks>
  <listRef>
    <ptr target="#COBICOL"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">monographic level</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">단행본 층위</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">專題層書目</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-01-06" xml:lang="fr">niveau monographique</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nivel monográfico.</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">monografia</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains bibliographic elements describing an item (e.g. a book or journal) published as an
    independent item (i.e. as a separate physical object).</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">독립 항목(즉, 독립된 물리적 개체)으로 출판된 항목(예를 들어 단행본 또는 학술지)을 기술하는
    참고문헌 요소를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含某一項目 (例如書或期刊) 的書目元素， 該項目為一獨立出版品 (即未附屬於其他出版品) 。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">独立したもの(例えば、物理的に独立したもの)として出版された対象(例え ば、書籍や雑誌)の書誌情報項目を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient des données bibliographiques décrivant un objet
    (par exemple une monographie ou une revue) publié comme un élément indépendant (i.e.
    matériellement séparé.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene los elementos bibliográficos que describen un
    ítem (p.ej. un libro o revista) publicado independientemente (es decir, como un objeto físico
    separado).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene elementi bilbiografici che descrivono un'opera
    (ad esempio un libro o una rivista) pubblicanti indipendentemente (cioè come un singolo
    oggetto).</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0">
          <sequence>
            <alternate>
              <elementRef key="author"/>
              <elementRef key="editor"/>
              <elementRef key="meeting"/>
              <elementRef key="respStmt"/>
            </alternate>
            
              <alternate minOccurs="0" maxOccurs="unbounded">
                <elementRef key="author"/>
                <elementRef key="editor"/>
                <elementRef key="meeting"/>
                <elementRef key="respStmt"/>
              </alternate>
            
            
              <elementRef key="title" minOccurs="1" maxOccurs="unbounded"/>
            
            
              <alternate minOccurs="0" maxOccurs="unbounded">
                <classRef key="model.ptrLike"/>
                <elementRef key="idno"/>
                <elementRef key="textLang"/>
                <elementRef key="editor"/>
                <elementRef key="respStmt"/>
              </alternate>
            
          </sequence>
          <sequence>
            
              <alternate minOccurs="1" maxOccurs="unbounded">
                <elementRef key="title"/>
                <classRef key="model.ptrLike"/>
                <elementRef key="idno"/>
              </alternate>
            
            
              <alternate minOccurs="0" maxOccurs="unbounded">
                <elementRef key="textLang"/>
                <elementRef key="author"/>
                <elementRef key="editor"/>
                <elementRef key="meeting"/>
                <elementRef key="respStmt"/>
              </alternate>
            
          </sequence>
          <sequence>
            <!-- specific to patents -->
            <elementRef key="authority"/>
            <elementRef key="idno"/>
          </sequence>
        </alternate>
      
      
        <elementRef key="availability" minOccurs="0" maxOccurs="unbounded"/>
      
      
        <classRef key="model.noteLike" minOccurs="0" maxOccurs="unbounded"/>
      
      <sequence minOccurs="0" maxOccurs="unbounded">
        <elementRef key="edition"/>
        
          <alternate minOccurs="0" maxOccurs="unbounded">
            <elementRef key="idno"/>
            <classRef key="model.ptrLike"/>
            <elementRef key="editor"/>
            <elementRef key="sponsor"/>
            <elementRef key="funder"/>
            <elementRef key="respStmt"/>
          </alternate>
        
      </sequence>
      <elementRef key="imprint"/>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="imprint"/>
          <elementRef key="extent"/>
          <elementRef key="biblScope"/>
        </alternate>
      
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-monogr-egXML-ig">
      <biblStruct>
        <analytic>
          <author>Chesnutt, David</author>
          <title>Historical Editions in the States</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <date when="1991-12">(December, 1991):</date>
          </imprint>
          <biblScope>25.6</biblScope>
          <biblScope unit="page" from="377" to="380">377–380</biblScope>
        </monogr>
      </biblStruct>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-monogr-egXML-wr">
      <biblStruct type="book">
        <monogr>
          <author>
            <persName>
              <forename>Leo Joachim</forename>
              <surname>Frachtenberg</surname>
            </persName>
          </author>
          <title type="main" level="m">Lower Umpqua Texts</title>
          <imprint>
            <pubPlace>New York</pubPlace>
            <publisher>Columbia University Press</publisher>
            <date>1914</date>
          </imprint>
        </monogr>
        <series>
          <title type="main" level="s">Columbia University Contributions to
                              Anthropology</title>
          <biblScope unit="volume">4</biblScope>
        </series>
      </biblStruct>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="monogr-remarks" versionDate="2012-10-26" xml:lang="en">
    <p rend="dataDesc">May contain specialized bibliographic elements, in a prescribed order.</p>
    <p>The <gi>monogr</gi> element may only occur only within a <gi>biblStruct</gi>, where its use
      is mandatory for the description of a monographic-level bibliographic item.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="monogr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Cet élément contient des éléments de description bibliographique spécialisés,
      dans un ordre prescrit.</p>
    <p>L'élément <gi>monogr</gi> n'est disponible que dans l'élément <gi>biblStruct</gi>, où il faut
      l'utiliser pour encoder la description bibliographique d'une monographie.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="monogr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 特別な書誌情報要素を、特定の順番でとるかもしれない。 </p>
    <p> 当該要素<gi>monogr</gi>は小論レベルの書誌項目を記述する際に必須で あるが、その際、要素<gi>biblStruct</gi>の中で高々1回出現する。 </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOL"/>
  </listRef>
```

^b21

