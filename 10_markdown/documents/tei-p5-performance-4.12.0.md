---
type: representation
source-type: document
source: '[[00_sources/tei-p5-performance-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 performance
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/performance.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# performance

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6732. Git blob: `1bfdaf140ee5f425ffddea1b2dd1da10ffc65436`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="drama" xml:id="gi-performance" ident="performance">
  <gloss versionDate="2007-06-12" xml:lang="en">performance</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">représentation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a section of front or back matter describing how a dramatic piece is to be
    performed in general or how it was performed on some specific occasion.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">드라마가 일반적으로 공연되는 방법 또는 특정 상황에서 공연되었던 방식을 기술하는, 앞부분 또는 뒷부분의
    절.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含前頁或後頁部分，描述戲劇作品的一般演出方式、或曾經在某些特定場合的演出方式。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene una sección del encabezado o de la conclusión
    que describe cómo un fragmento dramático debe ser realizado en general o cómo fue realizado en
    una función determinada.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">芝居の部分が、一般にどのように演技されるのか、特定の場面でどのように 演技されるのかを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une partie de la préface ou de la postface
    décrivant comment la pièce de théâtre doit être jouée normalement ou comment elle a été jouée à
    telle ou telle occasion particulière.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una sezione del peritesto iniziale o finale che
    descrive come mettere in scena l'opera teatrale, o come è stata messa in scena in qualche
    occasione particolare.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.frontPart.drama"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        
          <classRef key="model.common"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <classRef key="model.divBottom"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-zw" source="#FR1B">
      <performance>
        <p><rs type="place">Gateway Theatre, Edinburgh</rs>, <date>6 September 1948</date><castList><castItem><role>Anath Bithiah</role><actor>Athene Seyler</actor></castItem><castItem><role>Shendi</role><actor>Robert Rietty</actor></castItem></castList></p>
        <p>Directed by <name>E. Martin Browne</name>
            </p>
      </performance>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-si" source="#fr-ex-Teste">
      <performance>
        <p><rs type="place">Théâtre national du Petit-Odéon, Paris</rs>, <date>du 10 Décembre 1974
              au 12 Janvier 1975</date><castList><castItem><role>Paul Valéry</role><actor>Michel Duchaussoy</actor></castItem><castItem><role>Joseph</role><actor>Gérad Caillaud</actor></castItem><castItem><role>M. Teste</role><actor>Pierre Dux</actor></castItem><castItem><role>Mme Teste</role><actor>Claude Winter</actor></castItem><castItem><role>L'abbé Mosson</role><actor>Jacques Toja</actor></castItem></castList></p>
        <p>Adaptation et mise en scène de <name>Pierre Franck</name>
            </p>
      </performance>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-ls" source="#fr-ex-Knock">
      <performance>
        <p>Distribution <rs type="place">Comédie des Champs-Elysées, Paris,</rs>
               <date>1923</date>(par ordre d'entrée en scène) <castList><castItem>Knock : Louis Jouvet</castItem></castList>
            </p>
      </performance>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-cu" source="#biblzh-tw_n34">
      <performance>
        <p><rs type="place">新竹市文化局演藝廳</rs>, <date>2008年3月14日</date><castList><castItem><role>劉福春</role><actor>陳忠義</actor></castItem><castItem><role>劉麗月</role><actor>陳慧如</actor></castItem></castList></p>
        <p>監製： <name>李永得</name>
            </p>
      </performance>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-hi">
      <performance>
        <p>首演假<rs type="place">台北國家劇院</rs>於 <date>2007年10月12日</date>
               <castList><castItem>劉麗君: 徐堰鈴飾</castItem></castList>
            </p>
      </performance>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-kz">
      <performance>
        <p>Cast of the original production at the <rs type="place">Savoy Theatre, London,</rs> on
            <date>September 24, 1907</date>
               <castList><castItem>Colonel Hope : Mr A.E.George</castItem></castList>
            </p>
      </performance>
    </egXML>
  </exemplum>
  <remarks ident="performance-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">contains paragraphs and an optional cast list only.</p>
    <p/>
  </remarks>
  <remarks ident="performance-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">contient des paragraphes et éventuellement, un élément <gi>castList</gi>.</p>
  </remarks>
  <remarks ident="performance-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落と選択的な配役リストのみを含む。 </p>
    <p/>
  </remarks>
  <listRef>
    <ptr target="#DRPERF"/>
    <ptr target="#DRFAB" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">performance</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">représentation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a section of front or back matter describing how a dramatic piece is to be
    performed in general or how it was performed on some specific occasion.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">드라마가 일반적으로 공연되는 방법 또는 특정 상황에서 공연되었던 방식을 기술하는, 앞부분 또는 뒷부분의
    절.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含前頁或後頁部分，描述戲劇作品的一般演出方式、或曾經在某些特定場合的演出方式。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene una sección del encabezado o de la conclusión
    que describe cómo un fragmento dramático debe ser realizado en general o cómo fue realizado en
    una función determinada.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">芝居の部分が、一般にどのように演技されるのか、特定の場面でどのように 演技されるのかを示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une partie de la préface ou de la postface
    décrivant comment la pièce de théâtre doit être jouée normalement ou comment elle a été jouée à
    telle ou telle occasion particulière.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una sezione del peritesto iniziale o finale che
    descrive come mettere in scena l'opera teatrale, o come è stata messa in scena in qualche
    occasione particolare.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.frontPart.drama"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.divTop"/>
          <classRef key="model.global"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        
          <classRef key="model.common"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <classRef key="model.divBottom"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-zw" source="#FR1B">
      <performance>
        <p><rs type="place">Gateway Theatre, Edinburgh</rs>, <date>6 September 1948</date><castList><castItem><role>Anath Bithiah</role><actor>Athene Seyler</actor></castItem><castItem><role>Shendi</role><actor>Robert Rietty</actor></castItem></castList></p>
        <p>Directed by <name>E. Martin Browne</name>
            </p>
      </performance>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-si" source="#fr-ex-Teste">
      <performance>
        <p><rs type="place">Théâtre national du Petit-Odéon, Paris</rs>, <date>du 10 Décembre 1974
              au 12 Janvier 1975</date><castList><castItem><role>Paul Valéry</role><actor>Michel Duchaussoy</actor></castItem><castItem><role>Joseph</role><actor>Gérad Caillaud</actor></castItem><castItem><role>M. Teste</role><actor>Pierre Dux</actor></castItem><castItem><role>Mme Teste</role><actor>Claude Winter</actor></castItem><castItem><role>L'abbé Mosson</role><actor>Jacques Toja</actor></castItem></castList></p>
        <p>Adaptation et mise en scène de <name>Pierre Franck</name>
            </p>
      </performance>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-ls" source="#fr-ex-Knock">
      <performance>
        <p>Distribution <rs type="place">Comédie des Champs-Elysées, Paris,</rs>
               <date>1923</date>(par ordre d'entrée en scène) <castList><castItem>Knock : Louis Jouvet</castItem></castList>
            </p>
      </performance>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-cu" source="#biblzh-tw_n34">
      <performance>
        <p><rs type="place">新竹市文化局演藝廳</rs>, <date>2008年3月14日</date><castList><castItem><role>劉福春</role><actor>陳忠義</actor></castItem><castItem><role>劉麗月</role><actor>陳慧如</actor></castItem></castList></p>
        <p>監製： <name>李永得</name>
            </p>
      </performance>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-hi">
      <performance>
        <p>首演假<rs type="place">台北國家劇院</rs>於 <date>2007年10月12日</date>
               <castList><castItem>劉麗君: 徐堰鈴飾</castItem></castList>
            </p>
      </performance>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-performance-egXML-kz">
      <performance>
        <p>Cast of the original production at the <rs type="place">Savoy Theatre, London,</rs> on
            <date>September 24, 1907</date>
               <castList><castItem>Colonel Hope : Mr A.E.George</castItem></castList>
            </p>
      </performance>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="performance-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">contains paragraphs and an optional cast list only.</p>
    <p/>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="performance-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">contient des paragraphes et éventuellement, un élément <gi>castList</gi>.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="performance-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落と選択的な配役リストのみを含む。 </p>
    <p/>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DRPERF"/>
    <ptr target="#DRFAB" type="div3"/>
  </listRef>
```

^b21

