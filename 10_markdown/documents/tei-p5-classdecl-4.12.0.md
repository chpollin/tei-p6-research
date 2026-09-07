---
type: representation
source-type: document
source: '[[00_sources/tei-p5-classdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 classDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/classDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# classDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3868. Git blob: `d4c5241249507658772f1ba1bd83c8fd1579c672`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-classDecl" ident="classDecl">
  <gloss versionDate="2005-01-14" xml:lang="en">classification declarations</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">déclaration de classification</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">분류 선언</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">分類宣告</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">分類法宣言</gloss>
  <gloss versionDate="2016-11-17" xml:lang="de">Angabe zur Klassifikation</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaraciones de clasificación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazioni sulla ckassificazione</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains one or more taxonomies defining any classificatory
codes used elsewhere in the text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient une ou plusieurs taxinomies définissant les codes de classification utilisés n’importe où dans le texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 내 어디서든 사용될 수 있는 분류 부호를 정의하는 분류법을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個或多個分類法，用來定義在文件中他處所使用之任何分類碼。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該テキスト中で使用されている分類コードを定義する、
    ひとつ以上の分類法を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">enthält eine oder mehrere Taxonomien, die im Text verwendete Klassifikationscodes definieren.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una o más taxonomías que definen cualquier código usado en algún punto del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una o più tassonomie che definiscono un qualsiasi codice classificatorio usato in un'altra porzione del testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    
      <elementRef key="taxonomy" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classDecl-egXML-ud">
      <classDecl>
        <taxonomy xml:id="LCSH">
          <bibl>Library of Congress Subject Headings</bibl>
        </taxonomy>
      </classDecl>
      <!-- ... -->
      <textClass>
        <keywords scheme="#LCSH">
          <term>Political science</term>
          <term>United States -- Politics and government --
                      Revolution, 1775-1783</term>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classDecl-egXML-sr">
      <classDecl>
        <taxonomy xml:id="RAMEAU">
          <bibl>Répertoire d'autorité-matière encyclopédique et alphabétique unifié
                      (RAMEAU) de la Bibliothèque nationale de France. <ptr target="http://rameau.bnf.fr/"/>
               </bibl>
        </taxonomy>
      </classDecl>
      <!-- ... -->
      <textClass>
        <keywords scheme="#RAMEAU">
          <term>Bien et mal -- Enseignement coranique</term>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD55"/>
    <ptr target="#HD5"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">classification declarations</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">déclaration de classification</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">분류 선언</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">分類宣告</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">分類法宣言</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Angabe zur Klassifikation</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaraciones de clasificación</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazioni sulla ckassificazione</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains one or more taxonomies defining any classificatory
codes used elsewhere in the text.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient une ou plusieurs taxinomies définissant les codes de classification utilisés n’importe où dans le texte.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 내 어디서든 사용될 수 있는 분류 부호를 정의하는 분류법을 포함한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個或多個分類法，用來定義在文件中他處所使用之任何分類碼。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキスト中で使用されている分類コードを定義する、
    ひとつ以上の分類法を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">enthält eine oder mehrere Taxonomien, die im Text verwendete Klassifikationscodes definieren.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una o más taxonomías que definen cualquier código usado en algún punto del texto.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una o più tassonomie che definiscono un qualsiasi codice classificatorio usato in un'altra porzione del testo.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <elementRef key="taxonomy" minOccurs="1" maxOccurs="unbounded"/>
    
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classDecl-egXML-ud">
      <classDecl>
        <taxonomy xml:id="LCSH">
          <bibl>Library of Congress Subject Headings</bibl>
        </taxonomy>
      </classDecl>
      <!-- ... -->
      <textClass>
        <keywords scheme="#LCSH">
          <term>Political science</term>
          <term>United States -- Politics and government --
                      Revolution, 1775-1783</term>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-classDecl-egXML-sr">
      <classDecl>
        <taxonomy xml:id="RAMEAU">
          <bibl>Répertoire d'autorité-matière encyclopédique et alphabétique unifié
                      (RAMEAU) de la Bibliothèque nationale de France. <ptr target="http://rameau.bnf.fr/"/>
               </bibl>
        </taxonomy>
      </classDecl>
      <!-- ... -->
      <textClass>
        <keywords scheme="#RAMEAU">
          <term>Bien et mal -- Enseignement coranique</term>
        </keywords>
      </textClass>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD55"/>
    <ptr target="#HD5"/>
  </listRef>
```

^b21

