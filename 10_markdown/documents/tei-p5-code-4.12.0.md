---
type: representation
source-type: document
source: '[[00_sources/tei-p5-code-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 code
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/code.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# code

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3426. Git blob: `d711b8bb0f7998dc2d1c1bef3671a307677c34a7`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-code" ident="code">
  <desc versionDate="2005-08-28" xml:lang="en">contains literal code from some formal language such as a
programming language.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">프로그래밍 언어와 같은 형식 언어의 문자적 부호를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個正式語言的字母代碼，像是一個程式語言。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">プログラミング言語のような形式言語のコードを示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un code littéral provenant d'un langage
			formel, comme un langage de programmation.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un código alfabético que se deriva de un lenguaje formal, p.ej. un lenguaje de programación.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un codice alfabetico derivante da un linguaggio formale, per esempio un linguaggio di programmazione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.emphLike"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <attList>
    <attDef ident="lang" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">formal language</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">형식 언어</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">lenguaje formal</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">langage formel</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">linguaggio formale</gloss>
      <gloss versionDate="2024-02-28" xml:lang="ja">形式言語</gloss>
      <desc versionDate="2006-02-06" xml:lang="en">a name identifying the formal language in which  the code is expressed.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">부호가 표현된 형식 언어를 식별하는 이름</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">表示該代碼的正式語言名稱</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該コードの形式言語名を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">nom identifiant le langage formel dans lequel le code est exprimé.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">es el nombre que identifica el lenguaje formal en el que se expresa el código.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">è il nome che identifica il linguaggio formale nel quale viene espresso il codice.</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-code-egXML-cp">
      <code lang="JAVA">
       Size fCheckbox1Size = new Size();
       fCheckbox1Size.Height = 500;
       fCheckbox1Size.Width = 500;
       xCheckbox1.setSize(fCheckbox1Size);
</code>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDphraseTE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-08-28" xml:lang="en">contains literal code from some formal language such as a
programming language.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">프로그래밍 언어와 같은 형식 언어의 문자적 부호를 포함한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個正式語言的字母代碼，像是一個程式語言。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">プログラミング言語のような形式言語のコードを示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un code littéral provenant d'un langage
			formel, comme un langage de programmation.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un código alfabético que se deriva de un lenguaje formal, p.ej. un lenguaje de programación.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un codice alfabetico derivante da un linguaggio formale, per esempio un linguaggio di programmazione.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.emphLike"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">formal language</gloss>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">형식 언어</gloss>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">lenguaje formal</gloss>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">langage formel</gloss>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">linguaggio formale</gloss>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[6]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">形式言語</gloss>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2006-02-06" xml:lang="en">a name identifying the formal language in which  the code is expressed.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">부호가 표현된 형식 언어를 식별하는 이름</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示該代碼的正式語言名稱</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該コードの形式言語名を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">nom identifiant le langage formel dans lequel le code est exprimé.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">es el nombre que identifica el lenguaje formal en el que se expresa el código.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">è il nome che identifica il linguaggio formale nel quale viene espresso il codice.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-code-egXML-cp">
      <code lang="JAVA">
       Size fCheckbox1Size = new Size();
       fCheckbox1Size.Height = 500;
       fCheckbox1Size.Width = 500;
       xCheckbox1.setSize(fCheckbox1Size);
</code>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDphraseTE"/>
  </listRef>
```

^b25

