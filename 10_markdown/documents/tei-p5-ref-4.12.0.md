---
type: representation
source-type: document
source: '[[00_sources/tei-p5-ref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 ref
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/ref.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# ref

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4939. Git blob: `ff4a201020789d781170eb5550874eb11f7f9fac`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-ref" ident="ref">
  <gloss versionDate="2007-07-04" xml:lang="en">reference</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">참조</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">referencia</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">référence</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">riferimento</gloss>
  <gloss versionDate="2016-11-25" xml:lang="de">Referenz</gloss>
  <desc versionDate="2006-01-11" xml:lang="en">defines a reference to another location, possibly modified by additional text or comment.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">부가적인 텍스트 또는 해설로 수정될 수 있는, 다른 위치로 참조를 정의한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明與其他位置互相參照的符號，或許包含附加的文字或註解。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">他の場所への参照を定義する。多くは、追加テキストまたはコメントを含む。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">définit une référence vers un autre emplacement, la référence étant éventuellement modifiée ou complétée par un texte ou un commentaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define una referencia a otra localización, posiblemente modificada por un texto o comentario adicional.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce un riferimento ad un'altra posizione, può essere modificata da un commento o testo ulteriore.</desc>
  <desc versionDate="2016-11-25" xml:lang="de">definiert einen externen oder internen Verweis, der auch durch einen zusätzlichen Text oder Kommentar ergänzt werden kann.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cReferencing"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.internetMedia"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.annotationPart.body"/>
    <memberOf key="model.ptrLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <constraintSpec scheme="schematron" ident="refAtts" xml:lang="en">
    <constraint>
      <sch:rule context="tei:ref">
        <sch:report test="@target and @cRef">Only one of the attributes @target and @cRef may be supplied on &lt;<sch:name/>>.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-eq">See especially <ref target="http://www.natcorp.ox.ac.uk/Texts/A02.xml#s2">the second
      sentence</ref> 
      </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-yc">See also <ref target="#locution">s.v. <term>locution</term>
         </ref>.</egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-ym">Cf. tout particulièrement <ref target="#SEC12">la section 12, page 34</ref>.</egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-rv">Cf. tout particulièrement 
    <ref cRef="B1/234">le vers 234 du Livre I</ref>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-xz"><ref target="http://www.natcorp.ox.ac.uk/Texts/A02.xml#s2"> 關於第二行，</ref> 請參考 <ref>下列
    <term>慣用語</term>
    </ref>.</egXML>
  </exemplum>
  <remarks ident="ref-remarks" versionDate="2005-10-13" xml:lang="en">
    <p>The <att>target</att> and <att>cRef</att> attributes are mutually exclusive.</p>
  </remarks>
  <remarks ident="ref-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les attributs <att>target</att> et <att>cRef</att> sont exclusifs l'un de l'autre.</p>
  </remarks>
  <remarks ident="ref-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>target</att>と<att>cRef</att>は、排他的に使用される。 </p>
  </remarks>
  <remarks ident="ref-remarks" versionDate="2016-11-25" xml:lang="de">
    <p>Die <att>target</att> und <att>cRef</att>-Attribute schließen sich gegenseitig aus.</p>
  </remarks>
  <listRef>
    <ptr target="#COXR"/>
    <ptr target="#SAPT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">reference</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">참조</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">referencia</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">référence</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">riferimento</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Referenz</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-01-11" xml:lang="en">defines a reference to another location, possibly modified by additional text or comment.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">부가적인 텍스트 또는 해설로 수정될 수 있는, 다른 위치로 참조를 정의한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明與其他位置互相參照的符號，或許包含附加的文字或註解。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">他の場所への参照を定義する。多くは、追加テキストまたはコメントを含む。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">définit une référence vers un autre emplacement, la référence étant éventuellement modifiée ou complétée par un texte ou un commentaire.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define una referencia a otra localización, posiblemente modificada por un texto o comentario adicional.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce un riferimento ad un'altra posizione, può essere modificata da un commento o testo ulteriore.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-25" xml:lang="de">definiert einen externen oder internen Verweis, der auch durch einen zusätzlichen Text oder Kommentar ergänzt werden kann.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cReferencing"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.internetMedia"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.annotationPart.body"/>
    <memberOf key="model.ptrLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="refAtts" xml:lang="en">
    <constraint>
      <sch:rule context="tei:ref">
        <sch:report test="@target and @cRef">Only one of the attributes @target and @cRef may be supplied on &lt;<sch:name/>>.</sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-eq">See especially <ref target="http://www.natcorp.ox.ac.uk/Texts/A02.xml#s2">the second
      sentence</ref> 
      </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-yc">See also <ref target="#locution">s.v. <term>locution</term>
         </ref>.</egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-ym">Cf. tout particulièrement <ref target="#SEC12">la section 12, page 34</ref>.</egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-rv">Cf. tout particulièrement 
    <ref cRef="B1/234">le vers 234 du Livre I</ref>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-ref-egXML-xz"><ref target="http://www.natcorp.ox.ac.uk/Texts/A02.xml#s2"> 關於第二行，</ref> 請參考 <ref>下列
    <term>慣用語</term>
    </ref>.</egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="ref-remarks" versionDate="2005-10-13" xml:lang="en">
    <p>The <att>target</att> and <att>cRef</att> attributes are mutually exclusive.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="ref-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les attributs <att>target</att> et <att>cRef</att> sont exclusifs l'un de l'autre.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="ref-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 属性<att>target</att>と<att>cRef</att>は、排他的に使用される。 </p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="ref-remarks" versionDate="2016-11-25" xml:lang="de">
    <p>Die <att>target</att> und <att>cRef</att>-Attribute schließen sich gegenseitig aus.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COXR"/>
    <ptr target="#SAPT"/>
  </listRef>
```

^b28

