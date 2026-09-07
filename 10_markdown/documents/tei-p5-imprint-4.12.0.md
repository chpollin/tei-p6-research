---
type: representation
source-type: document
source: '[[00_sources/tei-p5-imprint-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 imprint
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/imprint.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# imprint

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3203. Git blob: `8c822f749a6ee317323649e8743ba8e9651c07b9`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-imprint" ident="imprint">
  <gloss versionDate="2005-01-14" xml:lang="en"/>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">版本說明</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">groups information relating to the publication or distribution
        of a bibliographic item.</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">regroupe des informations relatives à la
        publication ou à la distribution d'un élément bibliographique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">información de grupos acerca de la publicación o distribución de un elemento bibliográfico.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集書目項目的出版或發行相關資訊。</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni riguardo la pubblicazione o distribuzione di un'unità bibliograica.</desc>
  <desc versionDate="2006-10-28" xml:lang="ja">書誌情報の対象となるものの、出版に関する情報。</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="classCode"/>
          <elementRef key="catRef"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate>
          
            <!--just here to so odd2dtd puts parens into DTD-->
            <classRef key="model.imprintPart"/>
          
          
            <!--just here to so odd2dtd puts parens into DTD-->
            <classRef key="model.dateLike"/>
          
        </alternate>
        
          <elementRef key="respStmt" minOccurs="0" maxOccurs="unbounded"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprint-egXML-xq">
      <imprint>
        <pubPlace>Oxford</pubPlace>
        <publisher>Clarendon Press</publisher>
        <date>1987</date>
      </imprint>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprint-egXML-wq">
      <imprint>
        <pubPlace>Paris</pubPlace>
        <publisher>Les Éd. de Minuit</publisher>
        <date>2001</date>
      </imprint>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprint-egXML-jr">
      <imprint>
        <pubPlace>香港</pubPlace>
        <publisher>皇冠</publisher>
        <date>2005</date>
      </imprint>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COBICOI"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en"/>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">版本說明</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups information relating to the publication or distribution
        of a bibliographic item.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">regroupe des informations relatives à la
        publication ou à la distribution d'un élément bibliographique.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">información de grupos acerca de la publicación o distribución de un elemento bibliográfico.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集書目項目的出版或發行相關資訊。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa le informazioni riguardo la pubblicazione o distribuzione di un'unità bibliograica.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-28" xml:lang="ja">書誌情報の対象となるものの、出版に関する情報。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="classCode"/>
          <elementRef key="catRef"/>
        </alternate>
      
      <sequence minOccurs="1" maxOccurs="unbounded">
        <alternate>
          
            <!--just here to so odd2dtd puts parens into DTD-->
            <classRef key="model.imprintPart"/>
          
          
            <!--just here to so odd2dtd puts parens into DTD-->
            <classRef key="model.dateLike"/>
          
        </alternate>
        
          <elementRef key="respStmt" minOccurs="0" maxOccurs="unbounded"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprint-egXML-xq">
      <imprint>
        <pubPlace>Oxford</pubPlace>
        <publisher>Clarendon Press</publisher>
        <date>1987</date>
      </imprint>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprint-egXML-wq">
      <imprint>
        <pubPlace>Paris</pubPlace>
        <publisher>Les Éd. de Minuit</publisher>
        <date>2001</date>
      </imprint>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-imprint-egXML-jr">
      <imprint>
        <pubPlace>香港</pubPlace>
        <publisher>皇冠</publisher>
        <date>2005</date>
      </imprint>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOI"/>
  </listRef>
```

^b14

