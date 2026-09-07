---
type: representation
source-type: document
source: '[[00_sources/tei-p5-subst-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 subst
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/subst.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# subst

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4160. Git blob: `3e91319b14d45579c15bdfeda4a299f7d39eb272`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="transcr" xml:id="gi-subst" ident="subst">
  <gloss versionDate="2007-09-02" xml:lang="en">substitution</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">대체</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">substitución</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">sostituzione</gloss>
  <gloss versionDate="2008-10-02" xml:lang="fr"> substitution</gloss>
  <desc versionDate="2020-08-11" xml:lang="en">groups one or more deletions (or surplus text) with one or more additions when the combination is to be regarded as a single intervention in the text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">결합이 텍스트에서 단일 조작으로 간주될 때 하나 이상의 삭제를 하나 이상의 추가 사항으로 대체한다.</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">regroupe une ou plusieurs parties de texte supprimées et une ou plusieurs parties de texte ajoutées, lorsque cette combinaison peut être considérée comme une intervention unique sur le texte.</desc>
  <desc versionDate="2021-02-04" xml:lang="es">agrupa una o más cancelaciones con una o más adiciones cuando la combinación se considera una única intervención en el texto.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">追加と削除が一連の調整と考えられる場合、そのひとつ以上の追加部分や削 除部分をまとめる。</desc>
  <desc versionDate="2007-11-06" xml:lang="it">raggruppa ona o più cancellazioni insieme a una o più aggiunte quando la combinazione va considerata come singolo intervento sul testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
  <content>    
    <alternate minOccurs="1" maxOccurs="unbounded">
      <elementRef key="add"/>
      <elementRef key="surplus"/>
      <elementRef key="del"/>
      <classRef key="model.milestoneLike"/>
    </alternate>
  </content>
  <constraintSpec ident="substContents1" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:subst">
        <sch:assert test="child::tei:add and (child::tei:del or child::tei:surplus)">
        &lt;<sch:name/>&gt; must have at least one child &lt;add&gt; and at least one child &lt;del&gt; or &lt;surplus&gt;.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subst-egXML-lc">
... are all included. <del hand="#RG">It is</del>
         <subst><add>T</add><del>t</del></subst>he expressed
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subst-egXML-hh">
      that he and his Sister Miſs D — <lb/>who always lived with him, wd. be <subst><del>very</del><lb/><add>principally</add></subst> remembered in her Will.
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subst-egXML-li">
      <ab>τ<subst><add place="above">ῶν</add><del>α</del></subst>
        συνκυρόντ<subst><add place="above">ων</add><del>α</del></subst>
        ἐργαστηρί<subst><add place="above">ων</add><del>α</del></subst>
         </ab>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subst-egXML-rl">
      <subst>
        <del>
          <gap reason="illegible" quantity="5" unit="character"/>
        </del>
        <add>apple</add>
      </subst>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#PHSU"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-09-02" xml:lang="en">substitution</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">대체</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">substitución</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">sostituzione</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2008-10-02" xml:lang="fr"> substitution</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-08-11" xml:lang="en">groups one or more deletions (or surplus text) with one or more additions when the combination is to be regarded as a single intervention in the text.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">결합이 텍스트에서 단일 조작으로 간주될 때 하나 이상의 삭제를 하나 이상의 추가 사항으로 대체한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">regroupe une ou plusieurs parties de texte supprimées et une ou plusieurs parties de texte ajoutées, lorsque cette combinaison peut être considérée comme une intervention unique sur le texte.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2021-02-04" xml:lang="es">agrupa una o más cancelaciones con una o más adiciones cuando la combinación se considera una única intervención en el texto.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">追加と削除が一連の調整と考えられる場合、そのひとつ以上の追加部分や削 除部分をまとめる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">raggruppa ona o più cancellazioni insieme a una o più aggiunte quando la combinazione va considerata come singolo intervento sul testo.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.transcriptional"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>    
    <alternate minOccurs="1" maxOccurs="unbounded">
      <elementRef key="add"/>
      <elementRef key="surplus"/>
      <elementRef key="del"/>
      <classRef key="model.milestoneLike"/>
    </alternate>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="substContents1" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:subst">
        <sch:assert test="child::tei:add and (child::tei:del or child::tei:surplus)">
        &lt;<sch:name/>&gt; must have at least one child &lt;add&gt; and at least one child &lt;del&gt; or &lt;surplus&gt;.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subst-egXML-lc">
... are all included. <del hand="#RG">It is</del>
         <subst><add>T</add><del>t</del></subst>he expressed
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subst-egXML-hh">
      that he and his Sister Miſs D — <lb/>who always lived with him, wd. be <subst><del>very</del><lb/><add>principally</add></subst> remembered in her Will.
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subst-egXML-li">
      <ab>τ<subst><add place="above">ῶν</add><del>α</del></subst>
        συνκυρόντ<subst><add place="above">ων</add><del>α</del></subst>
        ἐργαστηρί<subst><add place="above">ων</add><del>α</del></subst>
         </ab>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-subst-egXML-rl">
      <subst>
        <del>
          <gap reason="illegible" quantity="5" unit="character"/>
        </del>
        <add>apple</add>
      </subst>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHSU"/>
  </listRef>
```

^b19

