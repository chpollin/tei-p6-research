---
type: representation
source-type: document
source: '[[00_sources/tei-p5-writing-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 writing
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/writing.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# writing

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6098. Git blob: `e3717b7a1bbdb08e3c137f2c688182029855a9df`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" xml:id="gi-writing" ident="writing">
  <gloss versionDate="2009-04-17" xml:lang="en">writing</gloss>
  <gloss versionDate="2009-04-17" xml:lang="fr">texte écrit</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">contains a passage of written text revealed to participants in the
  course of a spoken text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트의 진행과정에서 참여자에게 제공되는 문어 텍스트 단락</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在口說的過程中，參與者可觀看的一段書面文字。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話テキストで参加している表す、書き起こしテキストの一節を示す。</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">fragment d'un texte écrit communiqué aux
			participants au cours du discours objet de la transcription.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">pasaje escrito hecho disponible para los participantes durante un texto dialogado.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">testo scritto reso disponibile durante un testo parlato.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.spoken"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <attList>
    <attDef ident="gradual" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether the writing is revealed all at once or
	gradually.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">글이 동시에 또는 점차적으로 드러나는지를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該書面文字是一次全部出現或逐步出現</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該書き起こしは一度に見られるか、または少しずつ見られるものかを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique si l'écrit est communiqué en une
					fois ou progressivement.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el texto escrito aparece de repente o gradualmente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se il testo scritto appare in un'unica soluzione o gradualmente.</desc>
      <datatype><dataRef key="teidata.xTruthValue"/></datatype>
      <remarks ident="writing-attr.gradual-remarks" versionDate="2007-07-03" xml:lang="en">
        <p>The value <val>true</val> indicates the writing is
	  revealed gradually; the value <val>false</val> that the
	  writing is revealed all at once.</p>
      </remarks>
      <remarks ident="writing-attr.gradual-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val> true</val> indique que le texte écrit est transmis
                        progressivement, la valeur <val>false</val> que le texte écrit est transmis
                        en une fois.</p>
      </remarks>
      <remarks ident="writing-attr.gradual-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        値<val>true</val>は、当該書き起こしが、少しずつ見えることを示
        す。値<val>false</val>は、当該書き起こしが、一度に見えることを
        示す。
        </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-writing-egXML-gg">
      <!-- ... -->
      <l>man in a coonskin cap</l>
      <writing>coonskin</writing>
      <l>in a pig pen</l>
      <writing>pig pen</writing>
      <l>wants eleven dollar bills</l>
      <writing>20 dollar bills</writing>
      <l>you only got ten</l>
      <writing>10</writing>
      <!-- ... -->
    </egXML>
    <!-- Bob Dylan, Subterranean Homesick Blues, in
    D.A. Pennebaker (director), Don't Look Back, http://myplay.com/video-player/bob_dylan/?bcpid=187832446&bclid=187743874&bctid=187835137-->
  </exemplum>
  <remarks ident="writing-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>writing</gi> element will usually be short
    and most simply transcribed as a character string; the content
    model also allows a sequence of paragraphs and paragraph-level
    elements, in case the writing has enough internal structure to
    warrant such markup.  In either case the usual phrase-level
    tags for written text are available.</p>
  </remarks>
  <remarks ident="writing-remarks" versionDate="2009-04-17" xml:lang="fr">
    <p>l'élément <gi>writing</gi> sera habituellement court et transcrit simplement comme
                une chaîne de caractères ; le modèle de contenu autorise aussi une suite de
                paragraphes et d'éléments de niveau paragraphe, dans le cas où la structure du texte écrit
                justifie un tel codage. Dans l'un ou l'autre
                cas, les balises du niveau expression utilisables pour le texte écrit sont
            disponibles.</p>
  </remarks>
  <remarks ident="writing-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>writing</gi>は、一般には、文字列として、ごく短く、簡単に転
    記されたものになる。当該書き起こしにそれなりの内部構造がある場合に
    は、その内容モデルとして、一連の段落や、段落レベルの要素をとる。ま
    た、いずれの場合も、句レベルの要素もとることができる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#TSBAWR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="en">writing</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-17" xml:lang="fr">texte écrit</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains a passage of written text revealed to participants in the
  course of a spoken text.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트의 진행과정에서 참여자에게 제공되는 문어 텍스트 단락</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在口說的過程中，參與者可觀看的一段書面文字。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話テキストで参加している表す、書き起こしテキストの一節を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">fragment d'un texte écrit communiqué aux
			participants au cours du discours objet de la transcription.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">pasaje escrito hecho disponible para los participantes durante un texto dialogado.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">testo scritto reso disponibile durante un testo parlato.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed.directed"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.timed"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.spoken"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether the writing is revealed all at once or
	gradually.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">글이 동시에 또는 점차적으로 드러나는지를 나타낸다.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該書面文字是一次全部出現或逐步出現</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該書き起こしは一度に見られるか、または少しずつ見られるものかを示す。</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique si l'écrit est communiqué en une
					fois ou progressivement.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el texto escrito aparece de repente o gradualmente.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se il testo scritto appare in un'unica soluzione o gradualmente.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xTruthValue"/></datatype>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="writing-attr.gradual-remarks" versionDate="2007-07-03" xml:lang="en">
        <p>The value <val>true</val> indicates the writing is
	  revealed gradually; the value <val>false</val> that the
	  writing is revealed all at once.</p>
      </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="writing-attr.gradual-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val> true</val> indique que le texte écrit est transmis
                        progressivement, la valeur <val>false</val> que le texte écrit est transmis
                        en une fois.</p>
      </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="writing-attr.gradual-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        値<val>true</val>は、当該書き起こしが、少しずつ見えることを示
        す。値<val>false</val>は、当該書き起こしが、一度に見えることを
        示す。
        </p>
      </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-writing-egXML-gg">
      <!-- ... -->
      <l>man in a coonskin cap</l>
      <writing>coonskin</writing>
      <l>in a pig pen</l>
      <writing>pig pen</writing>
      <l>wants eleven dollar bills</l>
      <writing>20 dollar bills</writing>
      <l>you only got ten</l>
      <writing>10</writing>
      <!-- ... -->
    </egXML>
    <!-- Bob Dylan, Subterranean Homesick Blues, in
    D.A. Pennebaker (director), Don't Look Back, http://myplay.com/video-player/bob_dylan/?bcpid=187832446&bclid=187743874&bctid=187835137-->
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="writing-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>The <gi>writing</gi> element will usually be short
    and most simply transcribed as a character string; the content
    model also allows a sequence of paragraphs and paragraph-level
    elements, in case the writing has enough internal structure to
    warrant such markup.  In either case the usual phrase-level
    tags for written text are available.</p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="writing-remarks" versionDate="2009-04-17" xml:lang="fr">
    <p>l'élément <gi>writing</gi> sera habituellement court et transcrit simplement comme
                une chaîne de caractères ; le modèle de contenu autorise aussi une suite de
                paragraphes et d'éléments de niveau paragraphe, dans le cas où la structure du texte écrit
                justifie un tel codage. Dans l'un ou l'autre
                cas, les balises du niveau expression utilisables pour le texte écrit sont
            disponibles.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="writing-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    要素<gi>writing</gi>は、一般には、文字列として、ごく短く、簡単に転
    記されたものになる。当該書き起こしにそれなりの内部構造がある場合に
    は、その内容モデルとして、一連の段落や、段落レベルの要素をとる。ま
    た、いずれの場合も、句レベルの要素もとることができる。
    </p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TSBAWR"/>
  </listRef>
```

^b27

