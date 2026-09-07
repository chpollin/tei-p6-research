---
type: representation
source-type: document
source: '[[00_sources/tei-p5-ex-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 ex
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/ex.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# ex

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2878. Git blob: `5b8e3e583653b5f91a1e002e070269b6a527180e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-ex" ident="ex">
  <gloss versionDate="2007-08-29" xml:lang="en">editorial expansion</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">편집 상술</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">développement éditorial</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">espansione</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">expansión</gloss>
  <gloss versionDate="2006-06-05" xml:lang="zh-TW">縮寫還原</gloss>
  <desc versionDate="2007-08-29" xml:lang="en">contains a sequence of letters added by an editor or
  transcriber when expanding an abbreviation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">축약을 확장할 때 편집자 또는 전사자에 의해 추가된 문자열을 포함한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene una secuencia de letras añadidas por un editor o transcriptor al expandir una abreviatura.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">編集者や転記者が、省略形を元に戻した結果の文字列を示す。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">contient une succession de lettres ajoutées par un éditeur ou un transcripteur pour développer une abréviation.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene una sequenza di lettere aggiunte da un revisore o trascrittore in fase di espansione di un'abbreviazione.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
  <content>
    <macroRef key="macro.xtext"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ex-egXML-ma">The address is Southmoor <choice><expan>R<ex>oa</ex>d</expan><abbr>Rd</abbr></choice>
      </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ex-egXML-tc">Il habite au 15 <choice><expan>b<ex>oulevard</ex>d</expan><abbr>bd</abbr></choice>Clemenceau. </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ex-egXML-mp">
    這裡是<choice><expan>清<ex>華</ex>大<ex>學</ex>
            </expan><abbr>清大</abbr></choice>
      </egXML>
  </exemplum>
  <listRef>
    <ptr target="#PHAB" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-08-29" xml:lang="en">editorial expansion</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">편집 상술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">développement éditorial</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">espansione</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">expansión</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2006-06-05" xml:lang="zh-TW">縮寫還原</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-08-29" xml:lang="en">contains a sequence of letters added by an editor or
  transcriber when expanding an abbreviation.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">축약을 확장할 때 편집자 또는 전사자에 의해 추가된 문자열을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene una secuencia de letras añadidas por un editor o transcriptor al expandir una abreviatura.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">編集者や転記者が、省略形を元に戻した結果の文字列を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">contient une succession de lettres ajoutées par un éditeur ou un transcripteur pour développer une abréviation.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene una sequenza di lettere aggiunte da un revisore o trascrittore in fase di espansione di un'abbreviazione.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.xtext"/>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ex-egXML-ma">The address is Southmoor <choice><expan>R<ex>oa</ex>d</expan><abbr>Rd</abbr></choice>
      </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ex-egXML-tc">Il habite au 15 <choice><expan>b<ex>oulevard</ex>d</expan><abbr>bd</abbr></choice>Clemenceau. </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ex-egXML-mp">
    這裡是<choice><expan>清<ex>華</ex>大<ex>學</ex>
            </expan><abbr>清大</abbr></choice>
      </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHAB" type="div3"/>
  </listRef>
```

^b18

