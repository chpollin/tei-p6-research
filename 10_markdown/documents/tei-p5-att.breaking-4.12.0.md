---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.breaking-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.breaking
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.breaking.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.breaking

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4418. Git blob: `3b456ef7cc7f535f51730d62e909ebb44bf4c0b5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-breaking" ident="att.breaking">
  <desc versionDate="2021-08-22" xml:lang="en">provides attributes to indicate whether or not the element
  concerned is considered to  mark the end of an orthographic token in the same way
  as whitespace.</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit un attribut pour indiquer si un élément est
consideré ou pas comme marquant la fin d'un mot orthographique, comme
le fait une espace.</desc>
  <desc versionDate="2018-12-31" xml:lang="ja">当該要素が空白と同じ方法で正字トークンの終わりを示すとみなされるかどうかを示す属性を提供する。</desc>
  <attList>
    <attDef ident="break" usage="rec">
      <desc versionDate="2011-01-30" xml:lang="en">indicates whether or not the  element
	bearing this attribute should be considered to mark the end of
	an orthographic token in the same way as whitespace.</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si l'élément qui porte cet attribut
      peut être considéré comme une espace blanc indiquant la fin d'un mot
      orthographique.</desc>
      <desc versionDate="2018-12-31" xml:lang="ja">この属性を持つ要素が空白と同じ方法で正字トークンの終わりを示すとみなされるべきかどうかを示す。</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList>
        <valItem ident="yes">
          <desc versionDate="2011-01-30" xml:lang="en">the element bearing this attribute is considered
to mark the end of any adjacent orthographic token irrespective of the presence
of any adjacent whitespace</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'élément qui porte cet attribut
      peut être considéré comme  indiquant la fin d'un mot
      orthographique</desc>
          <desc versionDate="2018-12-31" xml:lang="ja">この属性を持つ要素は、隣接する任意の空白の存在に関係なく、隣接する正字法トークンの終わりをマークするとみなされる。</desc>
        </valItem>
        <valItem ident="no">
          <desc versionDate="2011-01-30" xml:lang="en">the element bearing this attribute is considered
not to mark the end of any adjacent orthographic token irrespective of the presence
of any adjacent whitespace</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'élément qui porte cet attribut
      ne peut être pas considéré comme  indiquant la fin d'un mot
      orthographique</desc>
          <desc versionDate="2018-12-31" xml:lang="ja">この属性を持つ要素は、隣接する空白の存在に関係なく、隣接する正字法トークンの終わりをマークしないとみなされる。</desc>
        </valItem>
        <valItem ident="maybe">
          <desc versionDate="2013-07-31" xml:lang="en">the encoding does not take any position on this issue.</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'encodage ne prends aucune position sur la question.</desc>
          <desc versionDate="2018-12-31" xml:lang="ja">当該符号化はこの問題に関していかなる立場もとらない。</desc>
        </valItem>
      </valList>
      <exemplum xml:lang="en">
        <p>In the following lines from the <title level="a">Dream of the Rood</title>, 
          the words <mentioned>lāðost</mentioned> and <mentioned>reord-berendum</mentioned> each start on one line and continue onto the next.
    </p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-breaking-egXML-il" xml:lang="ang">
          <ab>
      ...eƿesa tome iu icƿæs ȝeƿorden ƿita heardoſt . 
      leodum la<lb break="no"/>  ðost ærþan ichim lifes 
      ƿeȝ rihtne ȝerymde reord be<lb break="no"/>
      rendum hƿæt me þaȝeƿeorðode ƿuldres ealdor ofer...
    </ab>
        </egXML>
      </exemplum>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#CORS5"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-08-22" xml:lang="en">provides attributes to indicate whether or not the element
  concerned is considered to  mark the end of an orthographic token in the same way
  as whitespace.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit un attribut pour indiquer si un élément est
consideré ou pas comme marquant la fin d'un mot orthographique, comme
le fait une espace.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2018-12-31" xml:lang="ja">当該要素が空白と同じ方法で正字トークンの終わりを示すとみなされるかどうかを示す属性を提供する。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-01-30" xml:lang="en">indicates whether or not the  element
	bearing this attribute should be considered to mark the end of
	an orthographic token in the same way as whitespace.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si l'élément qui porte cet attribut
      peut être considéré comme une espace blanc indiquant la fin d'un mot
      orthographique.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2018-12-31" xml:lang="ja">この属性を持つ要素が空白と同じ方法で正字トークンの終わりを示すとみなされるべきかどうかを示す。</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList>
        <valItem ident="yes">
          <desc versionDate="2011-01-30" xml:lang="en">the element bearing this attribute is considered
to mark the end of any adjacent orthographic token irrespective of the presence
of any adjacent whitespace</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'élément qui porte cet attribut
      peut être considéré comme  indiquant la fin d'un mot
      orthographique</desc>
          <desc versionDate="2018-12-31" xml:lang="ja">この属性を持つ要素は、隣接する任意の空白の存在に関係なく、隣接する正字法トークンの終わりをマークするとみなされる。</desc>
        </valItem>
        <valItem ident="no">
          <desc versionDate="2011-01-30" xml:lang="en">the element bearing this attribute is considered
not to mark the end of any adjacent orthographic token irrespective of the presence
of any adjacent whitespace</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'élément qui porte cet attribut
      ne peut être pas considéré comme  indiquant la fin d'un mot
      orthographique</desc>
          <desc versionDate="2018-12-31" xml:lang="ja">この属性を持つ要素は、隣接する空白の存在に関係なく、隣接する正字法トークンの終わりをマークしないとみなされる。</desc>
        </valItem>
        <valItem ident="maybe">
          <desc versionDate="2013-07-31" xml:lang="en">the encoding does not take any position on this issue.</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">l'encodage ne prends aucune position sur la question.</desc>
          <desc versionDate="2018-12-31" xml:lang="ja">当該符号化はこの問題に関していかなる立場もとらない。</desc>
        </valItem>
      </valList>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <p>In the following lines from the <title level="a">Dream of the Rood</title>, 
          the words <mentioned>lāðost</mentioned> and <mentioned>reord-berendum</mentioned> each start on one line and continue onto the next.
    </p>
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-breaking-egXML-il" xml:lang="ang">
          <ab>
      ...eƿesa tome iu icƿæs ȝeƿorden ƿita heardoſt . 
      leodum la<lb break="no"/>  ðost ærþan ichim lifes 
      ƿeȝ rihtne ȝerymde reord be<lb break="no"/>
      rendum hƿæt me þaȝeƿeorðode ƿuldres ealdor ofer...
    </ab>
        </egXML>
      </exemplum>
```

^b9

### Block 10

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CORS5"/>
  </listRef>
```

^b10

