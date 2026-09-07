---
type: representation
source-type: document
source: '[[00_sources/tei-p5-langknowledge-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 langKnowledge
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/langKnowledge.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# langKnowledge

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7030. Git blob: `be49391ed05d5e33b57ba173d62a94ee71778b78`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-langKnowledge" ident="langKnowledge">
  <gloss versionDate="2007-07-04" xml:lang="en">language knowledge</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">언어 지식</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">conocimiento del lenguaje</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">connaissances linguistiques</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">conoscenza della lingua</gloss>
  <desc versionDate="2006-06-21" xml:lang="en">summarizes the state of a person's linguistic knowledge, either as prose or by a list of <gi>langKnown</gi> elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">산문체 또는 <gi>langKnown</gi> 요소 목록으로 개인의 언어 지식 상태를 요약한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人的語言認知狀態，可用敘述的方式或元素<gi>langKnown</gi>的條列形式來表達。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">個人の言語学的知識を散文または要素<gi>langKnown</gi>のリストでまとめ る。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">synthétise l'état des connaissances linguistiques d'une personne, soit en texte libre soit par une liste d'éléments <gi>langKnown</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">resume los conocimientos lingüísticos de una persona de forma descriptiva o a través de una lista de elementos <gi>langKnown</gi></desc>
  <desc versionDate="2007-01-21" xml:lang="it">riassume la conoscenza linguistica di una persona in forma descrittiva o tramite una lista di elementi <gi>langKnown</gi></desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <sequence>        
      <elementRef key="precision" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
	<classRef key="model.pLike"/>
	<elementRef key="langKnown" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
    </sequence>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <datatype>
	<dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
	<valItem ident="listening"/>
	<valItem ident="speaking"/>
	<valItem ident="reading"/>
	<valItem ident="writing"/>
      </valList>
    </attDef>
    <attDef ident="tags" usage="opt">
      <desc versionDate="2006-06-21" xml:lang="en">supplies one or more valid language tags for the languages specified.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">명시된 언어의 하나 이상의 유효한 언어 태그를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個或多個有效的所指語言標籤</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">ひとつ以上の言語を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">fournit un ou plusieurs codes de langue valides pour les langues spécifiées.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">asigna uno o más marcadores válidos a las lenguas indicadas.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">assegna uno o più marcatori validi alle lingue indicate.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.language"/></datatype>
      <remarks ident="langKnowledge-attr.tags-remarks" versionDate="2007-04-20" xml:lang="en">
        <p>This attribute should be supplied only if the element contains no <gi>langKnown</gi> children. Its values are language
                        <soCalled>tags</soCalled> as defined in <ref target="http://www.rfc-editor.org/rfc/rfc4646.txt">RFC 4646</ref> or its
                    successor</p>
      </remarks>
      <remarks ident="langKnowledge-attr.tags-remarks" versionDate="2008-12-09" xml:lang="fr">
        <p>Cet attribut ne doit être utilisé que si l'élément ne contient pas d'enfants <gi>langKnown</gi>. Ses valeurs sont des
                        <soCalled>codes</soCalled> de langues tels qu'ils sont définis par <ref target="http://www.rfc-editor.org/rfc/rfc4646.txt">RFC
                        4646</ref> ou ses successeurs.</p>
      </remarks>
      <remarks ident="langKnowledge-attr.tags-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性は、当該要素が子要素<gi>langKnown</gi>を含まない時にの み使われるべきである。当該属性値は、 <ref target="http://www.rfc-editor.org/rfc/rfc4646.txt"> RFC
                        4646</ref>で定義されている<soCalled>言語コード</soCalled>になる。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-xl">
      <langKnowledge tags="en-GB fr">
        <p>British English and French</p>
      </langKnowledge>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-px">
      <langKnowledge tags="en-GB fr">
        <p>Anglais britannique et français</p>
      </langKnowledge>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-zz">
      <langKnowledge>
        <langKnown tag="en-GB" level="H">Anglais britannique </langKnown>
        <langKnown tag="fr" level="M">Français</langKnown>
      </langKnowledge>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-lw">
      <langKnowledge tags="en-GB fr">
        <p>英式英文與法文</p>
      </langKnowledge>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-ll">
      <langKnowledge>
        <langKnown tag="en-GB" level="H">英式英文</langKnown>
        <langKnown tag="fr" level="M">法文</langKnown>
      </langKnowledge>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-lq">
      <langKnowledge>
        <langKnown tag="en-GB" level="H">British English</langKnown>
        <langKnown tag="fr" level="M">French</langKnown>
      </langKnowledge>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">language knowledge</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">언어 지식</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">conocimiento del lenguaje</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">connaissances linguistiques</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">conoscenza della lingua</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-06-21" xml:lang="en">summarizes the state of a person's linguistic knowledge, either as prose or by a list of <gi>langKnown</gi> elements.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">산문체 또는 <gi>langKnown</gi> 요소 목록으로 개인의 언어 지식 상태를 요약한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含個人的語言認知狀態，可用敘述的方式或元素<gi>langKnown</gi>的條列形式來表達。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">個人の言語学的知識を散文または要素<gi>langKnown</gi>のリストでまとめ る。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">synthétise l'état des connaissances linguistiques d'une personne, soit en texte libre soit par une liste d'éléments <gi>langKnown</gi>.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">resume los conocimientos lingüísticos de una persona de forma descriptiva o a través de una lista de elementos <gi>langKnown</gi></desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">riassume la conoscenza linguistica di una persona in forma descrittiva o tramite una lista di elementi <gi>langKnown</gi></desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persStateLike"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>        
      <elementRef key="precision" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
	<classRef key="model.pLike"/>
	<elementRef key="langKnown" minOccurs="1" maxOccurs="unbounded"/>
      </alternate>
    </sequence>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
	<dataRef key="teidata.enumerated"/>
      </datatype>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
	<valItem ident="listening"/>
	<valItem ident="speaking"/>
	<valItem ident="reading"/>
	<valItem ident="writing"/>
      </valList>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2006-06-21" xml:lang="en">supplies one or more valid language tags for the languages specified.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">명시된 언어의 하나 이상의 유효한 언어 태그를 제시한다.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個或多個有效的所指語言標籤</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ひとつ以上の言語を示す。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">fournit un ou plusieurs codes de langue valides pour les langues spécifiées.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">asigna uno o más marcadores válidos a las lenguas indicadas.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna uno o più marcatori validi alle lingue indicate.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.language"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="langKnowledge-attr.tags-remarks" versionDate="2007-04-20" xml:lang="en">
        <p>This attribute should be supplied only if the element contains no <gi>langKnown</gi> children. Its values are language
                        <soCalled>tags</soCalled> as defined in <ref target="http://www.rfc-editor.org/rfc/rfc4646.txt">RFC 4646</ref> or its
                    successor</p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="langKnowledge-attr.tags-remarks" versionDate="2008-12-09" xml:lang="fr">
        <p>Cet attribut ne doit être utilisé que si l'élément ne contient pas d'enfants <gi>langKnown</gi>. Ses valeurs sont des
                        <soCalled>codes</soCalled> de langues tels qu'ils sont définis par <ref target="http://www.rfc-editor.org/rfc/rfc4646.txt">RFC
                        4646</ref> ou ses successeurs.</p>
      </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="langKnowledge-attr.tags-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 当該属性は、当該要素が子要素<gi>langKnown</gi>を含まない時にの み使われるべきである。当該属性値は、 <ref target="http://www.rfc-editor.org/rfc/rfc4646.txt"> RFC
                        4646</ref>で定義されている<soCalled>言語コード</soCalled>になる。 </p>
      </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-xl">
      <langKnowledge tags="en-GB fr">
        <p>British English and French</p>
      </langKnowledge>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-px">
      <langKnowledge tags="en-GB fr">
        <p>Anglais britannique et français</p>
      </langKnowledge>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-zz">
      <langKnowledge>
        <langKnown tag="en-GB" level="H">Anglais britannique </langKnown>
        <langKnown tag="fr" level="M">Français</langKnown>
      </langKnowledge>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-lw">
      <langKnowledge tags="en-GB fr">
        <p>英式英文與法文</p>
      </langKnowledge>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-ll">
      <langKnowledge>
        <langKnown tag="en-GB" level="H">英式英文</langKnown>
        <langKnown tag="fr" level="M">法文</langKnown>
      </langKnowledge>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-langKnowledge-egXML-lq">
      <langKnowledge>
        <langKnown tag="en-GB" level="H">British English</langKnown>
        <langKnown tag="fr" level="M">French</langKnown>
      </langKnowledge>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
```

^b34

