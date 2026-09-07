---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fsddecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fsdDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fsdDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fsdDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4220. Git blob: `573c1df8bbb7c96248dbb83db5892524179ccbe1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fsdDecl" ident="fsdDecl">
  <gloss versionDate="2007-09-26" xml:lang="en">feature system declaration</gloss>
  <gloss versionDate="2009-04-16" xml:lang="fr">Déclaration de système de traits (FSD)</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질 체계 선언</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能系統宣告</gloss>
  <gloss versionDate="2018-07-18" xml:lang="de">Deklaration des Merkmalsystems</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración FSD (Declaración del Sistema de Rasgos)</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione su FSD (dichiarazione del sistema di tratti)</gloss>
  <desc versionDate="2007-09-26" xml:lang="en">provides a feature system declaration comprising one or more
  feature structure declarations or feature structure declaration links.</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">fournit une déclaration du système de traits consistant en une ou plusieurs déclarations de structure de traits ou des liens vers une déclaration de structure de traits.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나 이상의 자질 구조 선언 또는 자질 구조 선언 연결을 구성하고 있는 자질 체계 선언을 제시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">明確指出規範某特定功能結構類型的功能系統宣告。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ひとつ以上の素性構造宣言または素性構造宣言へのリンクを含む、素性シス
  テム宣言を示す。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">bietet eine Deklaration des Merkmalsystems, die aus einer oder mehreren 
    Merkmalstrukturdeklarationen oder Links zu Merkmalstrukturdeklarationen besteht.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la declaración del sistema de rasgos que contiene definiciones para un tipo particular de estructura de rasgos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">identifica la dichiarazione del sistema di tratti che contiene le definifioni di un particolare tipo di struttura di tratti.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
    <memberOf key="model.resource"/>
  </classes>
  <content>
    <classRef key="model.fsdDeclPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsdDecl-egXML-xx" source="#UND">
      <fsdDecl>
        <fsDecl type="GPSG">
          <fDecl xml:id="GPSG-1" name="GPSG_feat1">
            <vRange>
              <vAlt>
                <symbol value="red"/>
                <symbol value="blue"/>
                <symbol value="green"/>
              </vAlt>
            </vRange>
          </fDecl>
          <!--other feature declarations for GPSG here ... -->
        </fsDecl>
        <fsdLink type="subentry" target="http://www.example.com/fsdLib.xml#LX123"/>
      </fsdDecl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsdDecl-egXML-kb" source="#UND">
      <fsdDecl>
        <fsDecl type="GPSG">
          <fDecl xml:id="GPSG-1-fr" name="GPSG_feat1">
            <vRange>
              <vAlt>
                <symbol value="red"/>
                <symbol value="blue"/>
                <symbol value="green"/>
              </vAlt>
            </vRange>
          </fDecl>
          <!--other feature declarations for GPSG here ... -->
        </fsDecl>
        <fsdLink type="subentry" target="http://www.example.com/fsdLib.xml#LX123"/>
      </fsdDecl>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-09-26" xml:lang="en">feature system declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-16" xml:lang="fr">Déclaration de système de traits (FSD)</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질 체계 선언</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能系統宣告</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2018-07-18" xml:lang="de">Deklaration des Merkmalsystems</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración FSD (Declaración del Sistema de Rasgos)</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione su FSD (dichiarazione del sistema di tratti)</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-26" xml:lang="en">provides a feature system declaration comprising one or more
  feature structure declarations or feature structure declaration links.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">fournit une déclaration du système de traits consistant en une ou plusieurs déclarations de structure de traits ou des liens vers une déclaration de structure de traits.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나 이상의 자질 구조 선언 또는 자질 구조 선언 연결을 구성하고 있는 자질 체계 선언을 제시한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">明確指出規範某特定功能結構類型的功能系統宣告。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ひとつ以上の素性構造宣言または素性構造宣言へのリンクを含む、素性シス
  テム宣言を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">bietet eine Deklaration des Merkmalsystems, die aus einer oder mehreren 
    Merkmalstrukturdeklarationen oder Links zu Merkmalstrukturdeklarationen besteht.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la declaración del sistema de rasgos que contiene definiciones para un tipo particular de estructura de rasgos.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica la dichiarazione del sistema di tratti che contiene le definifioni di un particolare tipo di struttura di tratti.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
    <memberOf key="model.resource"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.fsdDeclPart" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsdDecl-egXML-xx" source="#UND">
      <fsdDecl>
        <fsDecl type="GPSG">
          <fDecl xml:id="GPSG-1" name="GPSG_feat1">
            <vRange>
              <vAlt>
                <symbol value="red"/>
                <symbol value="blue"/>
                <symbol value="green"/>
              </vAlt>
            </vRange>
          </fDecl>
          <!--other feature declarations for GPSG here ... -->
        </fsDecl>
        <fsdLink type="subentry" target="http://www.example.com/fsdLib.xml#LX123"/>
      </fsdDecl>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fsdDecl-egXML-kb" source="#UND">
      <fsdDecl>
        <fsDecl type="GPSG">
          <fDecl xml:id="GPSG-1-fr" name="GPSG_feat1">
            <vRange>
              <vAlt>
                <symbol value="red"/>
                <symbol value="blue"/>
                <symbol value="green"/>
              </vAlt>
            </vRange>
          </fDecl>
          <!--other feature declarations for GPSG here ... -->
        </fsDecl>
        <fsdLink type="subentry" target="http://www.example.com/fsdLib.xml#LX123"/>
      </fsdDecl>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b20

