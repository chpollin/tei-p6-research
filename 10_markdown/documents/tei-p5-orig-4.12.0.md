---
type: representation
source-type: document
source: '[[00_sources/tei-p5-orig-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 orig
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/orig.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# orig

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6539. Git blob: `a3e4a6a4340e9043c2f840c078aadd90c123f3c4`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-orig" ident="orig">
  <gloss versionDate="2005-01-14" xml:lang="en">original form</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">원형식</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">原文格式</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">forme originale</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">forma original</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">forma orininaria</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">originale Form</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a reading which is marked as following the original, rather than being normalized
        or corrected.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준화 또는 수정된 것이 아닌 원형식을 따르는 해석을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標誌原文中呈現的文字，並且未經過任何修改或規格化處理。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">正規化または校正は施されていない、元の形のまま符号化されている読みを 示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une partie notée comme étant fidèle à
        l'original et non pas normalisée ou corrigée.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una lectura que se marca como fiel al
        original.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una lettura codificata come conforme
        all'originale piuttosto che ad una versione normalizzata o corretta</desc>
    <desc versionDate="2016-11-24" xml:lang="de">enthält jene Schreibweise, die der Vorlage folgt und nicht normalisiert oder korrigiert ist.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
  <content>
    <!--    <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0"
            name="macro.phraseSeq"/>-->
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <p>If all that is desired is to call attention to the original version in the copy text,
                <gi>orig</gi> may be used alone:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-on" source="#KYD">
      <l>But this will be a <orig>meere</orig> confusion</l>
      <l>And hardly shall we all be <orig>vnderstoode</orig>
            </l>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Wenn es nur darum geht, auf die originale Version der Textvorlage hinzuweisen, kann das
      <gi>orig</gi>-Element auch allein verwendet werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-kh" source="#KYD">
      <l>But this will be a <orig>meere</orig> confusion</l>
      <l>And hardly shall we all be <orig>vnderstoode</orig>
      </l>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Si on veut privilégier la version originale du texte, <gi>orig</gi> sera utilisé seul:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-mm" source="#fr-ex-Montaigne_Essais">
      <p>si mes pensées se sont entretenues des occurences <orig>estrangieres</orig> quelque
          partie du temps, quelque autre partie je les <orig>rameine</orig> à la promenade, au<orig>
            vergier</orig>, à la douceur de cette solitude et à moy. </p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Généralement, <gi>orig</gi> sera associé à la forme corrigée dans un élément
        <gi>choice</gi>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-ab" source="#fr-ex-Corneille_Theodore">
      <l>Un bienfait perd sa grâce à le trop <choice><orig>oublier</orig><corr>publier</corr></choice> ; </l>
      <l>Qui veut qu'on s'en souvienne, il le faut <choice><orig>publier</orig><corr>oublier</corr></choice>.</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-dx" source="#biblzh-tw_n15">
      <l>妹子是被大哥<orig>喫</orig>了，母親知道沒有，我可不得而知。 </l>
      <l>母親想也知道；不過哭的時候，卻<orig>并</orig>沒有說明，大約也以為應當的了。</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-cu" source="#biblzh-tw_n16">
      <l>妹子是被大哥<choice><orig>喫</orig><reg>吃</reg></choice> 了，母親知道沒有，我可不得而知。</l>
      <l>母親想也知道；不過哭的時候，卻 <choice><orig>并</orig><reg>並</reg></choice>沒有說明，大約也以為應當的了。</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>More usually, an <gi>orig</gi> will be combined with a regularized form within a
                <gi>choice</gi> element:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-hg" source="#KYD">
      <l>But this will be a <choice><orig>meere</orig><reg>mere</reg></choice> confusion</l>
      <l>And hardly shall we all be <choice><orig>vnderstoode</orig><reg>understood</reg></choice>
            </l>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>In der Regel wird ein <gi>orig</gi>-Element mit einer normalisierten Form in einem
      <gi>choice</gi> Element kombiniert:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-zh" source="#KYD">
      <l>But this will be a <choice><orig>meere</orig><reg>mere</reg></choice> confusion</l>
      <l>And hardly shall we all be <choice><orig>vnderstoode</orig><reg>understood</reg></choice>
      </l>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COEDREG" type="div2"/>
    <ptr target="#TC" type="div1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">original form</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">원형식</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">原文格式</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">forme originale</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">forma original</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">forma orininaria</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">originale Form</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a reading which is marked as following the original, rather than being normalized
        or corrected.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준화 또는 수정된 것이 아닌 원형식을 따르는 해석을 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標誌原文中呈現的文字，並且未經過任何修改或規格化處理。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">正規化または校正は施されていない、元の形のまま符号化されている読みを 示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une partie notée comme étant fidèle à
        l'original et non pas normalisée ou corrigée.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una lectura que se marca como fiel al
        original.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una lettura codificata come conforme
        all'originale piuttosto che ad una versione normalizzata o corretta</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">enthält jene Schreibweise, die der Vorlage folgt und nicht normalisiert oder korrigiert ist.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.choicePart"/>
    <memberOf key="model.pPart.transcriptional"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <!--    <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0"
            name="macro.phraseSeq"/>-->
    <macroRef key="macro.paraContent"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>If all that is desired is to call attention to the original version in the copy text,
                <gi>orig</gi> may be used alone:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-on" source="#KYD">
      <l>But this will be a <orig>meere</orig> confusion</l>
      <l>And hardly shall we all be <orig>vnderstoode</orig>
            </l>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Wenn es nur darum geht, auf die originale Version der Textvorlage hinzuweisen, kann das
      <gi>orig</gi>-Element auch allein verwendet werden:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-kh" source="#KYD">
      <l>But this will be a <orig>meere</orig> confusion</l>
      <l>And hardly shall we all be <orig>vnderstoode</orig>
      </l>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Si on veut privilégier la version originale du texte, <gi>orig</gi> sera utilisé seul:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-mm" source="#fr-ex-Montaigne_Essais">
      <p>si mes pensées se sont entretenues des occurences <orig>estrangieres</orig> quelque
          partie du temps, quelque autre partie je les <orig>rameine</orig> à la promenade, au<orig>
            vergier</orig>, à la douceur de cette solitude et à moy. </p>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Généralement, <gi>orig</gi> sera associé à la forme corrigée dans un élément
        <gi>choice</gi>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-ab" source="#fr-ex-Corneille_Theodore">
      <l>Un bienfait perd sa grâce à le trop <choice><orig>oublier</orig><corr>publier</corr></choice> ; </l>
      <l>Qui veut qu'on s'en souvienne, il le faut <choice><orig>publier</orig><corr>oublier</corr></choice>.</l>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-dx" source="#biblzh-tw_n15">
      <l>妹子是被大哥<orig>喫</orig>了，母親知道沒有，我可不得而知。 </l>
      <l>母親想也知道；不過哭的時候，卻<orig>并</orig>沒有說明，大約也以為應當的了。</l>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-cu" source="#biblzh-tw_n16">
      <l>妹子是被大哥<choice><orig>喫</orig><reg>吃</reg></choice> 了，母親知道沒有，我可不得而知。</l>
      <l>母親想也知道；不過哭的時候，卻 <choice><orig>并</orig><reg>並</reg></choice>沒有說明，大約也以為應當的了。</l>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en">
    <p>More usually, an <gi>orig</gi> will be combined with a regularized form within a
                <gi>choice</gi> element:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-hg" source="#KYD">
      <l>But this will be a <choice><orig>meere</orig><reg>mere</reg></choice> confusion</l>
      <l>And hardly shall we all be <choice><orig>vnderstoode</orig><reg>understood</reg></choice>
            </l>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>In der Regel wird ein <gi>orig</gi>-Element mit einer normalisierten Form in einem
      <gi>choice</gi> Element kombiniert:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-orig-egXML-zh" source="#KYD">
      <l>But this will be a <choice><orig>meere</orig><reg>mere</reg></choice> confusion</l>
      <l>And hardly shall we all be <choice><orig>vnderstoode</orig><reg>understood</reg></choice>
      </l>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COEDREG" type="div2"/>
    <ptr target="#TC" type="div1"/>
  </listRef>
```

^b26

