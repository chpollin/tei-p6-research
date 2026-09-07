---
type: representation
source-type: document
source: '[[00_sources/tei-p5-link-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 link
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/link.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# link

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4699. Git blob: `743d961428ff33ce498791282038713e372c589e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="linking" xml:id="gi-link" ident="link">
  <gloss versionDate="2007-06-12" xml:lang="en">link</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr"> lien</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">defines an association or hypertextual link among elements or passages, of some type not more precisely specifiable by other elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">다른 요소들에 의해 좀 더 명확하게 명시되지 않는 유형의 요소 또는 단락들의 연관 또는 하이퍼텍스트 연결을 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義元素或段落之間的關連或超文字連結，其他元素無法將此連結類型作更詳細說明。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">他の要素では上手く示せない、要素や一節間にある関連性やハイパーテキス トリンクを定義する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit une association ou un lien hypertextuel entre des éléments ou des passages, lien dont le type ne peut être spécifié précisément par d'autres éléments.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una asociación o vínculo hipertextual entre elementos o fragmentos de texto que no es especificable por otros elementos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce tra elementi o porzioni di testo un'associazione o legame ipertestuale non meglio specificabile da altri elementi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content><empty/></content>
  <constraintSpec ident="linkTargets3" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:link">
        <sch:assert test="contains(normalize-space(@target),' ')">You must supply at least two values for @target on &lt;<sch:name/>&gt;.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-link-egXML-rx">
      <s n="1">The state Supreme Court has refused to release <rs xml:id="R1"><rs xml:id="R2">Rahway State Prison</rs> inmate</rs> 
        <rs xml:id="R3">James Scott</rs> on bail.</s>
      <s n="2"><rs xml:id="R4">The fighter</rs> is serving 30-40 years
        for a 1975 armed robbery conviction in <rs xml:id="R5">the penitentiary</rs>.</s>
      <!-- ... -->
      <linkGrp type="periphrasis">
        <link target="#R1 #R3 #R4"/>
        <link target="#R2 #R5"/>
      </linkGrp>
    </egXML>
  </exemplum>
  <remarks ident="link-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element should only be used to encode associations not otherwise provided for by more specific elements.</p>
    <p>The location of this element within a document has no significance, unless it is included within a <gi>linkGrp</gi>, in which case it may inherit the value of the <att>type</att> attribute from the value given on the <gi>linkGrp</gi>.</p>
  </remarks>
  <remarks ident="link-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p>Cet élément n’est utilisé que pour encoder des associations ; il n’est pas préconisé pour d’autres éléments plus spécifiques. </p>
    <p> L’emplacement de cet élément dans un document n'a aucune signification, à moins qu'il ne soit inclus dans un élément <gi>linkGrp</gi> ; dans ce cas il peut hériter de la valeur donnée à l’attribut <att>type</att> de l’élément <gi>linkGrp</gi> .</p>
  </remarks>
  <remarks ident="link-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素は、他の要素では示すことができない関連性を符号化する際にの み使われるべきである。 </p>
    <p> 当該要素が、要素<gi>linkGrp</gi>でまとめられているのでなければ、当 該要素のある場所は重要ではない。要素<gi>linkGrp</gi>の下にある場合、 属性<att>type</att>の値は要素<gi>linkGrp</gi>がもつ値を継承する。 </p>
  </remarks>
  <listRef>
    <ptr target="#SAPT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">link</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr"> lien</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">defines an association or hypertextual link among elements or passages, of some type not more precisely specifiable by other elements.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다른 요소들에 의해 좀 더 명확하게 명시되지 않는 유형의 요소 또는 단락들의 연관 또는 하이퍼텍스트 연결을 정의한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義元素或段落之間的關連或超文字連結，其他元素無法將此連結類型作更詳細說明。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">他の要素では上手く示せない、要素や一節間にある関連性やハイパーテキス トリンクを定義する。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit une association ou un lien hypertextuel entre des éléments ou des passages, lien dont le type ne peut être spécifié précisément par d'autres éléments.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una asociación o vínculo hipertextual entre elementos o fragmentos de texto que no es especificable por otros elementos.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce tra elementi o porzioni di testo un'associazione o legame ipertestuale non meglio specificabile da altri elementi.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="linkTargets3" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:link">
        <sch:assert test="contains(normalize-space(@target),' ')">You must supply at least two values for @target on &lt;<sch:name/>&gt;.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-link-egXML-rx">
      <s n="1">The state Supreme Court has refused to release <rs xml:id="R1"><rs xml:id="R2">Rahway State Prison</rs> inmate</rs> 
        <rs xml:id="R3">James Scott</rs> on bail.</s>
      <s n="2"><rs xml:id="R4">The fighter</rs> is serving 30-40 years
        for a 1975 armed robbery conviction in <rs xml:id="R5">the penitentiary</rs>.</s>
      <!-- ... -->
      <linkGrp type="periphrasis">
        <link target="#R1 #R3 #R4"/>
        <link target="#R2 #R5"/>
      </linkGrp>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="link-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element should only be used to encode associations not otherwise provided for by more specific elements.</p>
    <p>The location of this element within a document has no significance, unless it is included within a <gi>linkGrp</gi>, in which case it may inherit the value of the <att>type</att> attribute from the value given on the <gi>linkGrp</gi>.</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="link-remarks" versionDate="2009-10-06" xml:lang="fr">
    <p>Cet élément n’est utilisé que pour encoder des associations ; il n’est pas préconisé pour d’autres éléments plus spécifiques. </p>
    <p> L’emplacement de cet élément dans un document n'a aucune signification, à moins qu'il ne soit inclus dans un élément <gi>linkGrp</gi> ; dans ce cas il peut hériter de la valeur donnée à l’attribut <att>type</att> de l’élément <gi>linkGrp</gi> .</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="link-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素は、他の要素では示すことができない関連性を符号化する際にの み使われるべきである。 </p>
    <p> 当該要素が、要素<gi>linkGrp</gi>でまとめられているのでなければ、当 該要素のある場所は重要ではない。要素<gi>linkGrp</gi>の下にある場合、 属性<att>type</att>の値は要素<gi>linkGrp</gi>がもつ値を継承する。 </p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#SAPT"/>
  </listRef>
```

^b17

