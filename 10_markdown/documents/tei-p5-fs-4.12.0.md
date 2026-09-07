---
type: representation
source-type: document
source: '[[00_sources/tei-p5-fs-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 fs
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/fs.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# fs

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6373. Git blob: `964315c2afa8fffa585929f489d9029f2a7cdfd1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-fs" ident="fs">
  <gloss versionDate="2007-07-04" xml:lang="en">feature structure</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자질 구조</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能結構</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">structure de traits</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">Estructura de rasgo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">struttura dei tratti</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">represents a <term>feature structure</term>, that is, a
  collection of feature-value pairs organized as a
structural unit.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><term>feature structure</term>, 즉, 구조화된 단위로서 구성된 자질-값 쌍의 집합을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個<term>功能結構</term>，即組織為一個結構單元的功能-值配對集合。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja"><term>素性構造</term>を示す。すなわち、構造単位となる素性名-素性値の
  組の集合。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">représente une <term>structure de traits</term>,
      c'est-à-dire un ensemble de paires trait-valeur organisé comme une unité structurelle.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">representa una <term>feature structure (estructura de rasgos)</term>, es decir, un conjunto de pares de valores de rasgos organizados como una unidad estructural.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">rappresenta una <term>feature structure</term>, cioè una raccolta di coppie di valori tratti organizzata come una unità strutturale.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datcat"/>
    <memberOf key="model.featureVal.complex"/>
    <memberOf key="model.global.meta"/>
  </classes>
  <content>
    
      <elementRef key="f" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
  <attList>
    <attDef ident="type" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the type of the feature structure.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">자질 구조의 유형을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">功能結構的類型。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該素性構造の種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie le type de la structure de traits.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el tipo de estructura de rasgo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il tipo di struttura dei tratti.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
    <attDef ident="feats" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">features</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">자질</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">características</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">traits</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">tratti</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">references the feature-value specifications making up this feature structure.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">자질 구조를 구성하는 자질-값 명세를 참조한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">參照組成該功能結構的功能值細節。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該素性構造を構成する素性定義を参照する。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">référence les spécifications trait-valeur qui
          caractérisent cette structure de traits.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica las especificaciones de valor de rasgo que constituyen esta estructura de
rasgo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica le specifiche del valore dei tratti che formano questa struttura.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="fs-attr.feats-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>May be used either instead of having features as content, or in
  addition. In the latter case, the features referenced and contained
  are unified. </p>
      </remarks>
      <remarks ident="fs-attr.feats-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Peut être utilisé soit à la place de traits pris comme contenu, soit en plus.
                        Dans ce dernier cas, les traits référencés et contenus sont unifiés. </p>
      </remarks>
      <remarks ident="fs-attr.feats-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	素性を内容として含まない、または追加する際に使われるかもしれな
	い。後者の場合、参照された素性と既存の素性は統合される。
	 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fs-egXML-iv" source="#UND">
      <fs type="agreement_structure">
        <f name="person">
          <symbol value="third"/>
        </f>
        <f name="number">
          <symbol value="singular"/>
        </f>
      </fs>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fs-egXML-fi" source="#UND">
      <fs type="agreement_structure">
        <f name="person">
          <symbol value="third"/>
        </f>
        <f name="number">
          <symbol value="singular"/>
        </f>
      </fs>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FSBI" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">feature structure</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질 구조</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能結構</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">structure de traits</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">Estructura de rasgo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">struttura dei tratti</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">represents a <term>feature structure</term>, that is, a
  collection of feature-value pairs organized as a
structural unit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><term>feature structure</term>, 즉, 구조화된 단위로서 구성된 자질-값 쌍의 집합을 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">表示一個<term>功能結構</term>，即組織為一個結構單元的功能-值配對集合。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja"><term>素性構造</term>を示す。すなわち、構造単位となる素性名-素性値の
  組の集合。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">représente une <term>structure de traits</term>,
      c'est-à-dire un ensemble de paires trait-valeur organisé comme une unité structurelle.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">representa una <term>feature structure (estructura de rasgos)</term>, es decir, un conjunto de pares de valores de rasgos organizados como una unidad estructural.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">rappresenta una <term>feature structure</term>, cioè una raccolta di coppie di valori tratti organizzata come una unità strutturale.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datcat"/>
    <memberOf key="model.featureVal.complex"/>
    <memberOf key="model.global.meta"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <elementRef key="f" minOccurs="0" maxOccurs="unbounded"/>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the type of the feature structure.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질 구조의 유형을 명시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">功能結構的類型。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該素性構造の種類を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie le type de la structure de traits.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el tipo de estructura de rasgo.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il tipo di struttura dei tratti.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">features</gloss>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자질</gloss>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">características</gloss>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">traits</gloss>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">tratti</gloss>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">references the feature-value specifications making up this feature structure.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">자질 구조를 구성하는 자질-값 명세를 참조한다.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">參照組成該功能結構的功能值細節。</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該素性構造を構成する素性定義を参照する。</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">référence les spécifications trait-valeur qui
          caractérisent cette structure de traits.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica las especificaciones de valor de rasgo que constituyen esta estructura de
rasgo.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica le specifiche del valore dei tratti che formano questa struttura.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="fs-attr.feats-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>May be used either instead of having features as content, or in
  addition. In the latter case, the features referenced and contained
  are unified. </p>
      </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="fs-attr.feats-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Peut être utilisé soit à la place de traits pris comme contenu, soit en plus.
                        Dans ce dernier cas, les traits référencés et contenus sont unifiés. </p>
      </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="fs-attr.feats-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	素性を内容として含まない、または追加する際に使われるかもしれな
	い。後者の場合、参照された素性と既存の素性は統合される。
	 </p>
      </remarks>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fs-egXML-iv" source="#UND">
      <fs type="agreement_structure">
        <f name="person">
          <symbol value="third"/>
        </f>
        <f name="number">
          <symbol value="singular"/>
        </f>
      </fs>
    </egXML>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-fs-egXML-fi" source="#UND">
      <fs type="agreement_structure">
        <f name="person">
          <symbol value="third"/>
        </f>
        <f name="number">
          <symbol value="singular"/>
        </f>
      </fs>
    </egXML>
  </exemplum>
```

^b41

### Block 42

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FSBI" type="div3"/>
  </listRef>
```

^b42

