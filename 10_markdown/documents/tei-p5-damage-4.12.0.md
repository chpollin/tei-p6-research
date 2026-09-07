---
type: representation
source-type: document
source: '[[00_sources/tei-p5-damage-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 damage
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/damage.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# damage

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4954. Git blob: `d01b202b509bffd303c871b92a18cf8fa67e2f1f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="transcr" xml:id="gi-damage" ident="damage">
  <gloss xml:lang="en" versionDate="2007-06-12">damage</gloss>
  <gloss xml:lang="ja" versionDate="2024-08-08">損傷</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">dommage</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an area of damage to the text witness.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트의 손상 영역을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件中一塊損毀區域。</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">当該証拠資料におけるテキストの損傷部分を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">sert à encoder une zone qui a subi des dommages dans le manuscrit témoin du texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una área dañada del testimonio.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene l'area visibile del danneggiamento al testimone.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.damaged"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-damage-egXML-pr">
      <l>The Moving Finger wri<damage agent="water" group="1">es; and</damage> having writ,</l>
      <l>Moves <damage agent="water" group="1"><supplied>on: nor all your</supplied></damage> Piety nor Wit</l>
    </egXML>
  </exemplum>
  <remarks ident="damage-remarks" versionDate="2007-09-03" xml:lang="en">
    <p>Since damage to text witnesses frequently makes them harder to
    read, the <gi>damage</gi> element will often contain an
    <gi>unclear</gi> element.  If the damaged area is not continuous
    (e.g. a stain affecting several strings of text), the
    <att>group</att> attribute may be used to group together several
    related <gi>damage</gi> elements; alternatively the <gi>join</gi>
    element may be used to indicate which <gi>damage</gi> and
    <gi>unclear</gi> elements are part of the same physical
    phenomenon.</p>
    <p>The <gi>damage</gi>, <gi>gap</gi>, <gi>del</gi>, <gi>unclear</gi>
and <gi>supplied</gi> elements may be closely allied in use.  See
section <ptr target="#PHCOMB"/> for discussion of which element is
appropriate for which circumstance.</p>
  </remarks>
  <remarks ident="damage-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Puisque les dégâts causés aux témoins du texte les rendent fréquemment plus difficiles à
                lire, l'élément<gi>damage</gi> contiendra souvent un élément <gi>unclear</gi>. Si la
                zone endommagée n'est pas continue (par exemple une tache affectant plusieurs
                morceaux de texte), on utilisera l'attribut<att>group</att> pour regrouper plusieurs
                éléments <gi>damage</gi> ; alternativement, on utilisera l'élément
                <gi>join</gi>pour indiquer quels éléments <gi>damage</gi> et <gi>unclear</gi> sont
                liés au même phénomène physique.</p>
    <p>Les éléments <gi>damage</gi>, <gi>gap</gi>, <gi>del</gi>, <gi>unclear</gi>
      et<gi>supplied</gi> peuvent être utilisés en étroite association. Voir la section <ptr target="#PHCOMB"/> pour savoir en quelle circonstance chacun de ces éléments est approprié.</p>
  </remarks>
  <remarks ident="damage-remarks" versionDate="2024-08-08" xml:lang="ja"><p>
    損傷はしばしば証拠資料のテキストを読み取りにくくさせるので、
    <gi>damage</gi>要素は、 よく<gi>unclear</gi>要素をとる。
    当該損傷部分が連続的ではない場合（例えば、一個のしみがいくつかの文字に掛るなど）、
    <att>group</att>属性により、関連する複数の<gi>damage</gi>要素をまとめることができる。
    あるいは、<gi>join</gi>要素で、どの<gi>damage</gi>要素や<gi>unclear</gi>要素が、同一の物理的現象に起因するかを示すこともできる。</p>
    <p><gi>damage</gi>、<gi>gap</gi>、<gi>del</gi>、<gi>unclear</gi>、<gi>supplied</gi>などの要素は、密接に関連して用いられる。
    これらのどの要素が相応しいかについての詳細は<ptr target="#PHCOMB"/>を参照のこと。
</p>    

</remarks>
  <listRef>
    <ptr target="#PHDA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss xml:lang="en" versionDate="2007-06-12">damage</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss xml:lang="ja" versionDate="2024-08-08">損傷</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">dommage</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an area of damage to the text witness.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">비교 대상 텍스트의 손상 영역을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含文件中一塊損毀區域。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">当該証拠資料におけるテキストの損傷部分を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">sert à encoder une zone qui a subi des dommages dans le manuscrit témoin du texte.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una área dañada del testimonio.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene l'area visibile del danneggiamento al testimone.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.damaged"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-damage-egXML-pr">
      <l>The Moving Finger wri<damage agent="water" group="1">es; and</damage> having writ,</l>
      <l>Moves <damage agent="water" group="1"><supplied>on: nor all your</supplied></damage> Piety nor Wit</l>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="damage-remarks" versionDate="2007-09-03" xml:lang="en">
    <p>Since damage to text witnesses frequently makes them harder to
    read, the <gi>damage</gi> element will often contain an
    <gi>unclear</gi> element.  If the damaged area is not continuous
    (e.g. a stain affecting several strings of text), the
    <att>group</att> attribute may be used to group together several
    related <gi>damage</gi> elements; alternatively the <gi>join</gi>
    element may be used to indicate which <gi>damage</gi> and
    <gi>unclear</gi> elements are part of the same physical
    phenomenon.</p>
    <p>The <gi>damage</gi>, <gi>gap</gi>, <gi>del</gi>, <gi>unclear</gi>
and <gi>supplied</gi> elements may be closely allied in use.  See
section <ptr target="#PHCOMB"/> for discussion of which element is
appropriate for which circumstance.</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="damage-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Puisque les dégâts causés aux témoins du texte les rendent fréquemment plus difficiles à
                lire, l'élément<gi>damage</gi> contiendra souvent un élément <gi>unclear</gi>. Si la
                zone endommagée n'est pas continue (par exemple une tache affectant plusieurs
                morceaux de texte), on utilisera l'attribut<att>group</att> pour regrouper plusieurs
                éléments <gi>damage</gi> ; alternativement, on utilisera l'élément
                <gi>join</gi>pour indiquer quels éléments <gi>damage</gi> et <gi>unclear</gi> sont
                liés au même phénomène physique.</p>
    <p>Les éléments <gi>damage</gi>, <gi>gap</gi>, <gi>del</gi>, <gi>unclear</gi>
      et<gi>supplied</gi> peuvent être utilisés en étroite association. Voir la section <ptr target="#PHCOMB"/> pour savoir en quelle circonstance chacun de ces éléments est approprié.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="damage-remarks" versionDate="2024-08-08" xml:lang="ja"><p>
    損傷はしばしば証拠資料のテキストを読み取りにくくさせるので、
    <gi>damage</gi>要素は、 よく<gi>unclear</gi>要素をとる。
    当該損傷部分が連続的ではない場合（例えば、一個のしみがいくつかの文字に掛るなど）、
    <att>group</att>属性により、関連する複数の<gi>damage</gi>要素をまとめることができる。
    あるいは、<gi>join</gi>要素で、どの<gi>damage</gi>要素や<gi>unclear</gi>要素が、同一の物理的現象に起因するかを示すこともできる。</p>
    <p><gi>damage</gi>、<gi>gap</gi>、<gi>del</gi>、<gi>unclear</gi>、<gi>supplied</gi>などの要素は、密接に関連して用いられる。
    これらのどの要素が相応しいかについての詳細は<ptr target="#PHCOMB"/>を参照のこと。
</p>    

</remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHDA"/>
  </listRef>
```

^b17

