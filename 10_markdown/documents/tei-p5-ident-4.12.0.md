---
type: representation
source-type: document
source: '[[00_sources/tei-p5-ident-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 ident
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/ident.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# ident

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3406. Git blob: `8fc38276d6fc21d790cb95dae7241be5fde74115`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="IDENT" ident="ident">
  <gloss versionDate="2007-07-04" xml:lang="en">identifier</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">확인소</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">identificador</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">identifiant</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">identificatore</gloss>
  <desc versionDate="2011-12-01" xml:lang="en">contains an identifier or name for an object of some kind in a formal language. <gi>ident</gi> is used for tokens such as variable names, class names, type names, function names etc. in formal programming languages.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">형식 언어에서 어떤 종류의 개체에 대한 확인소 또는 이름을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個使用正式語言的某種物件的識別符碼或名稱。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">形式言語にあるオブジェクトの識別子または名前を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un identifiant ou un nom dans un langage
			formel pour un objet quelconque.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un identificador o un nombre asignado a un objeto dado en un lenguaje formal.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un identificatore o nome assegnato a un dato oggetto in un linguaggio formale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.emphLike"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <exemplum versionDate="2016-11-04" xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="IDENT-egXML-eq">
      <ident type="ns">http://www.tei-c.org/ns/Examples</ident>
    </egXML>
  </exemplum>
  <exemplum versionDate="2016-11-04" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="IDENT-egXML-to">
      <ident type="ns">http://www.tei-c.org/ns/Examples</ident>
    </egXML>
  </exemplum>
  <remarks ident="ident-remarks" versionDate="2011-12-01" xml:lang="en">
    <p>In running prose, this element may be used for any kind of
      identifier in any formal language. It should not be used for element and
      attribute names in XML, for which the special elements <gi>gi</gi>
       and <gi>att</gi> are provided.</p>
  </remarks>
  <remarks ident="ident-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans un  texte courant, cet élément peut être utilisé pour n'importe quelle sorte
                d'identifiant dans tout langage formel.</p>
  </remarks>
  <remarks ident="ident-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    散文では、当該要素は、形式言語における各種識別子を示すものとして使
  用されるかもしれない。
  </p>
  </remarks>
  <listRef>
    <ptr target="#TDphraseTE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">identifier</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">확인소</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">identificador</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">identifiant</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">identificatore</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-12-01" xml:lang="en">contains an identifier or name for an object of some kind in a formal language. <gi>ident</gi> is used for tokens such as variable names, class names, type names, function names etc. in formal programming languages.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">형식 언어에서 어떤 종류의 개체에 대한 확인소 또는 이름을 포함한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個使用正式語言的某種物件的識別符碼或名稱。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">形式言語にあるオブジェクトの識別子または名前を示す。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un identifiant ou un nom dans un langage
			formel pour un objet quelconque.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un identificador o un nombre asignado a un objeto dado en un lenguaje formal.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un identificatore o nome assegnato a un dato oggetto in un linguaggio formale.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.emphLike"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2016-11-04" xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="IDENT-egXML-eq">
      <ident type="ns">http://www.tei-c.org/ns/Examples</ident>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2016-11-04" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="IDENT-egXML-to">
      <ident type="ns">http://www.tei-c.org/ns/Examples</ident>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="ident-remarks" versionDate="2011-12-01" xml:lang="en">
    <p>In running prose, this element may be used for any kind of
      identifier in any formal language. It should not be used for element and
      attribute names in XML, for which the special elements <gi>gi</gi>
       and <gi>att</gi> are provided.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="ident-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Dans un  texte courant, cet élément peut être utilisé pour n'importe quelle sorte
                d'identifiant dans tout langage formel.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="ident-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    散文では、当該要素は、形式言語における各種識別子を示すものとして使
  用されるかもしれない。
  </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDphraseTE"/>
  </listRef>
```

^b20

