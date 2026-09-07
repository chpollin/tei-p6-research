---
type: representation
source-type: document
source: '[[00_sources/tei-p5-damagespan-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 damageSpan
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/damageSpan.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# damageSpan

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7116. Git blob: `473ac53d7d272b497e99adfdac83eebf19ced2b4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="transcr" xml:id="gi-damageSpan" ident="damageSpan">
  <gloss versionDate="2007-09-03" xml:lang="en">damaged span of text</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">텍스트의 손상 구간</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">fragmento de texto dañado</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">partie de texte endommagée</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">porzione di testo danneggiata</gloss>
  <gloss versionDate="2024-08-08" xml:lang="ja">テキストの損傷範囲</gloss>
  <desc versionDate="2007-09-03" xml:lang="en">marks the beginning of a longer sequence of text which is damaged in some way but still legible.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 방식으로 손상되었지만 여전히 읽을 수 있는 긴 텍스트 연쇄 시작부를 표시한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">marca el inicio de una secuencia de texto larga dañada de alguna manera pero aún legible.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">読める程度の損傷がある、一連のテキストの始点を示す。</desc>
  <desc versionDate="2009-11-16" xml:lang="fr">marque le début d'une longue partie de texte, endommagée d'une manière quelconque mais toujours lisible.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">segnala l'inizio di una sequenza più estesa di testo danneggiata ma ancora leggibile.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.damaged"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
  <content><empty/></content>
  <constraintSpec ident="damageSpan-requires-spanTo" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:damageSpan">
        <sch:assert test="@spanTo">The @spanTo attribute of &lt;<sch:name/>> is required.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <!-- FC j'ai traduit ici la contrainte schematron -->
  <constraintSpec ident="damageSpan-requires-spanTo-fr" scheme="schematron" xml:lang="fr">
    <constraint>
      <sch:rule context="tei:damageSpan">
        <sch:assert test="@spanTo">L'attribut spanTo est requis.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-damageSpan-egXML-cv">
      <p>Paragraph partially damaged.  This is the undamaged
portion <damageSpan spanTo="#a34"/>and this the damaged
portion of the paragraph.</p>
      <p>This paragraph is entirely damaged.</p>
      <p>Paragraph partially damaged; in the middle of this
paragraph the damage ends and the anchor point marks
the start of the  <anchor xml:id="a34"/> undamaged part of the text. ...</p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-damageSpan-egXML-fy">
      <p>Paragraph partially damaged. This is the undamaged portion <damageSpan spanTo="#fr_a34"/>and
          this the damaged portion of the paragraph.</p>
      <p>This paragraph is entirely damaged.</p>
      <p>Paragraph partially damaged; in the middle of this paragraph the damage ends and the
          anchor point marks the start of the <anchor xml:id="fr_a34"/> undamaged part of the text.
        ...</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-damageSpan-egXML-mf">
      <p>此段部份毀損。這裡是完好的部份，<damageSpan spanTo="#zh-tw_a34"/>而此為毀損的部份。</p>
      <p>此段全部毀損。</p>
      <p>段落有部份毀損，損壞處止於段落的中間，以屬性anchor標示<anchor xml:id="zh-tw_a34"/>未損內文的重新出現處。</p>
    </egXML>
  </exemplum>
  <remarks ident="damageSpan-remarks" versionDate="2009-06-29" xml:lang="en">
    <p>Both the beginning and ending of the damaged sequence must be
    marked: the beginning by the <gi>damageSpan</gi> element, the ending
    by the target of the <att>spanTo</att> attribute: if no other
    element available, the <gi>anchor</gi> element may be used for
    this purpose.</p>
    <p>The damaged text must be at least partially legible, in order
    for the encoder to be able to transcribe it. If it is not legible
    at all, the <gi>damageSpan</gi> element should not be used. Rather, the
    <gi>gap</gi> or <gi>unclear</gi> element should be employed, with the value of the <att>reason</att> attribute
    giving the cause. See further sections <ptr target="#PHDA"/> and
 <ptr target="#PHCOMB"/>.</p>
  </remarks>
  <remarks ident="damageSpan-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Le début et la fin de la partie de texte endommagée doivent être marqués : le début, par l'élément <gi>damageSpan</gi>, la fin au moyen de la cible de l'attribut <att>spanTo</att> :
                si aucun autre élément n'est disponible, l'élément <gi>anchor</gi> est utilisé à cette fin.</p>
    <p>Le texte endommagé doit être au moins partiellement lisible, afin que l'encodeur soit
                capable de le transcrire. S'il n'est pas lisible du tout, l'élément
                <gi>damageSpan</gi> ne devrait pas être utilisé. L'élément <gi>gap</gi> ou
                    <gi>unclear</gi> devrait être plutôt employé, avec un attribut <att>reason</att>
        dont la valeur donnerait la cause de cette lecture impossible. Voir les autres sections <ptr target="#PHDA"/> et <ptr target="#PHCOMB"/>.</p>
  </remarks>
  <remarks ident="damageSpan-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      当該損傷部分の始点と終点の両方を符号化しなければならない。始点は<gi>damageSpan</gi>要素で、終点はターゲットを<att>spanTo</att>属性に示す。もし他に適切な要素がなければ、<gi>anchor</gi>要素をこの目的のために使用してもよい。〔<gi>DamageSpan</gi>で囲まれた〕「損傷したテキスト」は少なくとも一部は読み取れ、符号化のために翻刻が可能なものでなければならない。全く読めない場合には、<gi>damageSpan</gi>要素を使用すべきではない。この場合は、<gi>gap</gi>要素または<gi>unclear</gi>要素が、読めない理由を示す<att>reason</att>属性と共に採用されるべきである。詳細については<ptr target="#PHDA"/>と<ptr target="#PHCOMB"/>を参照のこと。
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
<gloss versionDate="2007-09-03" xml:lang="en">damaged span of text</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">텍스트의 손상 구간</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">fragmento de texto dañado</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">partie de texte endommagée</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">porzione di testo danneggiata</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2024-08-08" xml:lang="ja">テキストの損傷範囲</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-03" xml:lang="en">marks the beginning of a longer sequence of text which is damaged in some way but still legible.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 방식으로 손상되었지만 여전히 읽을 수 있는 긴 텍스트 연쇄 시작부를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">marca el inicio de una secuencia de texto larga dañada de alguna manera pero aún legible.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">読める程度の損傷がある、一連のテキストの始点を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-11-16" xml:lang="fr">marque le début d'une longue partie de texte, endommagée d'une manière quelconque mais toujours lisible.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">segnala l'inizio di una sequenza più estesa di testo danneggiata ma ancora leggibile.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.damaged"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.global.edit"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="damageSpan-requires-spanTo" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:damageSpan">
        <sch:assert test="@spanTo">The @spanTo attribute of &lt;<sch:name/>> is required.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b15

### Block 16

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="damageSpan-requires-spanTo-fr" scheme="schematron" xml:lang="fr">
    <constraint>
      <sch:rule context="tei:damageSpan">
        <sch:assert test="@spanTo">L'attribut spanTo est requis.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-damageSpan-egXML-cv">
      <p>Paragraph partially damaged.  This is the undamaged
portion <damageSpan spanTo="#a34"/>and this the damaged
portion of the paragraph.</p>
      <p>This paragraph is entirely damaged.</p>
      <p>Paragraph partially damaged; in the middle of this
paragraph the damage ends and the anchor point marks
the start of the  <anchor xml:id="a34"/> undamaged part of the text. ...</p>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-damageSpan-egXML-fy">
      <p>Paragraph partially damaged. This is the undamaged portion <damageSpan spanTo="#fr_a34"/>and
          this the damaged portion of the paragraph.</p>
      <p>This paragraph is entirely damaged.</p>
      <p>Paragraph partially damaged; in the middle of this paragraph the damage ends and the
          anchor point marks the start of the <anchor xml:id="fr_a34"/> undamaged part of the text.
        ...</p>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-damageSpan-egXML-mf">
      <p>此段部份毀損。這裡是完好的部份，<damageSpan spanTo="#zh-tw_a34"/>而此為毀損的部份。</p>
      <p>此段全部毀損。</p>
      <p>段落有部份毀損，損壞處止於段落的中間，以屬性anchor標示<anchor xml:id="zh-tw_a34"/>未損內文的重新出現處。</p>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="damageSpan-remarks" versionDate="2009-06-29" xml:lang="en">
    <p>Both the beginning and ending of the damaged sequence must be
    marked: the beginning by the <gi>damageSpan</gi> element, the ending
    by the target of the <att>spanTo</att> attribute: if no other
    element available, the <gi>anchor</gi> element may be used for
    this purpose.</p>
    <p>The damaged text must be at least partially legible, in order
    for the encoder to be able to transcribe it. If it is not legible
    at all, the <gi>damageSpan</gi> element should not be used. Rather, the
    <gi>gap</gi> or <gi>unclear</gi> element should be employed, with the value of the <att>reason</att> attribute
    giving the cause. See further sections <ptr target="#PHDA"/> and
 <ptr target="#PHCOMB"/>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="damageSpan-remarks" versionDate="2009-11-16" xml:lang="fr">
    <p>Le début et la fin de la partie de texte endommagée doivent être marqués : le début, par l'élément <gi>damageSpan</gi>, la fin au moyen de la cible de l'attribut <att>spanTo</att> :
                si aucun autre élément n'est disponible, l'élément <gi>anchor</gi> est utilisé à cette fin.</p>
    <p>Le texte endommagé doit être au moins partiellement lisible, afin que l'encodeur soit
                capable de le transcrire. S'il n'est pas lisible du tout, l'élément
                <gi>damageSpan</gi> ne devrait pas être utilisé. L'élément <gi>gap</gi> ou
                    <gi>unclear</gi> devrait être plutôt employé, avec un attribut <att>reason</att>
        dont la valeur donnerait la cause de cette lecture impossible. Voir les autres sections <ptr target="#PHDA"/> et <ptr target="#PHCOMB"/>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="damageSpan-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
      当該損傷部分の始点と終点の両方を符号化しなければならない。始点は<gi>damageSpan</gi>要素で、終点はターゲットを<att>spanTo</att>属性に示す。もし他に適切な要素がなければ、<gi>anchor</gi>要素をこの目的のために使用してもよい。〔<gi>DamageSpan</gi>で囲まれた〕「損傷したテキスト」は少なくとも一部は読み取れ、符号化のために翻刻が可能なものでなければならない。全く読めない場合には、<gi>damageSpan</gi>要素を使用すべきではない。この場合は、<gi>gap</gi>要素または<gi>unclear</gi>要素が、読めない理由を示す<att>reason</att>属性と共に採用されるべきである。詳細については<ptr target="#PHDA"/>と<ptr target="#PHCOMB"/>を参照のこと。
  </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHDA"/>
  </listRef>
```

^b23

