---
type: representation
source-type: document
source: '[[00_sources/tei-p5-choice-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 choice
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/choice.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# choice

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8939. Git blob: `7033a84fa82c8aed417e19490844a80c98965a45`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-choice" ident="choice">
  <gloss versionDate="2009-01-06" xml:lang="en">choice</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">choix</gloss>
  <gloss versionDate="2016-11-25" xml:lang="de">Alternative</gloss>  
  <desc versionDate="2005-01-14" xml:lang="en">groups a number of alternative encodings for the same point in
        a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 동일 지점에서 대체 가능한 부호화를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集文件中對於同一部分文字所有可供替換的不同標記。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト中の同じ場所で、異なる符号化記述をまとめる。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">regroupe un certain nombre de balisages alternatifs possibles
        pour un même endroit  dans un texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa un número de codificaciones alternativas para el mismo punto en un texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa un numero di codifiche alternative per la stessa porzione di testo.</desc>
  <desc versionDate="2016-11-24" xml:lang="de">gruppiert alternative Kodierungen für eine Stelle im Text.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
<content>
  <alternate minOccurs="2" maxOccurs="unbounded">
    <classRef key="model.choicePart"/>
    <elementRef key="choice"/>
  </alternate>
</content>
  <exemplum xml:lang="en">
    <p>An American encoding of <title>Gulliver's Travels</title> which
            retains the British spelling but also provides a version
            regularized to American spelling might be encoded as follows.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-choice-egXML-xg" source="#COEDCOR-eg-71">
      <p>Lastly, That, upon his solemn oath to observe all the above
                articles, the said man-mountain shall have a daily allowance of
                meat and drink sufficient for the support of <choice><sic>1724</sic><corr>1728</corr></choice> of our subjects,
                with free access to our royal person, and other marks of our
                <choice><orig>favour</orig><reg>favor</reg></choice>.</p>
    </egXML>
    <!-- Gulliver's Travels -->
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Eine Kodierung von <title>Gulliver's Travels</title>, die die britische Schreibweise beibehält,
      aber auch eine der amerikanischen Rechtschreibung entsprechende Version anbietet, kann wie folgt
      kodiert werden.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-choice-egXML-lo" source="#COEDCOR-eg-71">
      <p>Lastly, That, upon his solemn oath to observe all the above
        articles, the said man-mountain shall have a daily allowance of
        meat and drink sufficient for the support of <choice><sic>1724</sic><corr>1728</corr></choice> of our subjects,
        with free access to our royal person, and other marks of our
        <choice><orig>favour</orig><reg>favor</reg></choice>.</p>
    </egXML>
    <!-- Gulliver's Travels -->
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">L'encodage d'une édition des <title>Essais</title> pourra faire état à la fois des formes
        originales et des formes modernisées correspondantes:.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-choice-egXML-yg" source="#fr-ex-Montaigne_Essais">
      <p>Ainsi lecteur, je suis<choice><orig>moy-mesmes</orig><reg>moi-même</reg></choice> la matière de mon livre : ce n'est pas raison que tu emploies ton loisir en un <choice><orig>subject</orig><reg>sujet</reg></choice>si frivole et si vain.</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-choice-egXML-qd">
      <p>清朝與日本為爭奪北韓半島控制權，爆發歷史上著名的甲午戰爭。 發生於清光緒二十年，西元 <choice><sic>1892</sic><corr>1894</corr></choice>年，雙方水陸大戰，傷亡者<choice><orig>衆</orig><reg>眾</reg></choice>。</p>
    </egXML>
  </exemplum>
  <remarks ident="choice-remarks" versionDate="2010-05-01" xml:lang="en">
    <p>Because the children of a  <gi>choice</gi> element all
            represent alternative ways of encoding the same sequence, it is
            natural to think of them as mutually exclusive. However, there may
            be cases where a full representation of a text requires the
            alternative encodings to be considered as parallel. </p>
    <p>Note also that <gi>choice</gi> elements may self-nest.</p>
    <p>Where the purpose of an encoding is to record multiple
            witnesses of a single work, rather than to identify
    multiple possible encoding decisions at a given point, the
    <gi>app</gi> element and associated elements discussed in  section
    <ptr target="#TCAPLL"/> should be preferred.</p>
  </remarks>
  <remarks ident="choice-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Parce que les éléments contenus par un élément <gi>choice</gi> correspondent  tous à des solutions
            possibles  pour encoder la même séquence, il est naturel de les envisager comme
            exclusifs les uns des autres. Toutefois il peut y avoir des cas où la pleine
            représentation d'un texte requiert de considérer ces encodages alternatifs comme
            parallèles.</p>
    <p>A Noter aussi que les <gi>choice</gi> peuvent s'imbriquer. </p>
    <p>Pour une version de <gi>choice</gi> spécialisée pour l'encodage de témoins multiples
            d'une même oeuvre, l'élément <gi>app</gi> peut etre préférable : voir la section <ptr target="#TCAPLL"/>.</p>
  </remarks>
  <remarks ident="choice-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Porque los niños de un elemento <gi>opción</gi> representan las maneras alternativas de codificar la misma secuencia, es natural pensar en ellas como mutuamente exclusivas.
            Sin embargo, puede haber casos donde una representación completa de un texto requiera que las codificaciones alternativas sean consideradas como paralelas. </p>
    <p>Se Observa también que los elementos <gi>opción</gi> pueden ser uno mismo-jerarquía.</p>
    <p>Para una versión especializada de la <gi>opción</gi> para codificar los testimonios múltiples de un único trabajo, ver la sección <ptr target="#TCAPLL"/>.</p>
  </remarks>
  <remarks ident="choice-remarks" versionDate="2024-02-28" xml:lang="ja">
    <p>
      <gi>choice</gi>要素の子要素は全て、同じ部分の異なる選択肢を示しているので、それらは択一的であるとするのが自然である。
      けれども、テキストを完全に表現するには複数の選択肢を並列的に扱う必要がある場合もあるだろう。</p>
      <p><gi>choice</gi>要素は、自らを入れ子にできることにも注意して欲しい。</p>
      <p>符号化時にありうる選択肢ではなく、1つの作品にある複数の本文を記録する目的では、
      <ptr target="#TCAPLL"/>で扱われている<gi>app</gi>要素などが望ましい。</p>
  </remarks>
  <remarks ident="choice-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>
          Da die Kindelemente des <gi>choice</gi>-Elements alternative Kodierungsmöglichkeiten der selben Textstelle repräsentieren, 
          ist es naheliegend, sie als sich gegenseitig ausschließend zu betrachten. Es sind jedoch Fälle vorstellbar, 
          in der Kodierungsalternativen als Kodierungsparallelen verstanden werden müssen, um den Text vollständig zu repräsentieren. 
      </p>
      <p>
          Man beachte außerdem, dass <gi>choice</gi>-Elemente weitere <gi>choice</gi>-Elemente als Kindelemente enthalten können.
      </p>
      <p>
          In Fällen, in denen nicht mehrere mögliche Kodierungsvarianten, sondern Varianten aus mehreren Zeugen eines Werkes kodiert werden sollen, 
          sind das <gi>app</gi>-Element und dazu gehörige Elemente, die im Abschnitt <ptr target="#TCAPLL"/> erläutert werden, zu bevorzugen.
      </p>
  </remarks>
  <listRef>
    <ptr target="#COED" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="en">choice</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">choix</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2016-11-25" xml:lang="de">Alternative</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">groups a number of alternative encodings for the same point in
        a text.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 동일 지점에서 대체 가능한 부호화를 모아 놓는다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集文件中對於同一部分文字所有可供替換的不同標記。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト中の同じ場所で、異なる符号化記述をまとめる。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">regroupe un certain nombre de balisages alternatifs possibles
        pour un même endroit  dans un texte.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa un número de codificaciones alternativas para el mismo punto en un texto.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa un numero di codifiche alternative per la stessa porzione di testo.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">gruppiert alternative Kodierungen für eine Stelle im Text.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.linePart"/>
    <memberOf key="model.pPart.editorial"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
  <alternate minOccurs="2" maxOccurs="unbounded">
    <classRef key="model.choicePart"/>
    <elementRef key="choice"/>
  </alternate>
</content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>An American encoding of <title>Gulliver's Travels</title> which
            retains the British spelling but also provides a version
            regularized to American spelling might be encoded as follows.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-choice-egXML-xg" source="#COEDCOR-eg-71">
      <p>Lastly, That, upon his solemn oath to observe all the above
                articles, the said man-mountain shall have a daily allowance of
                meat and drink sufficient for the support of <choice><sic>1724</sic><corr>1728</corr></choice> of our subjects,
                with free access to our royal person, and other marks of our
                <choice><orig>favour</orig><reg>favor</reg></choice>.</p>
    </egXML>
    <!-- Gulliver's Travels -->
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Eine Kodierung von <title>Gulliver's Travels</title>, die die britische Schreibweise beibehält,
      aber auch eine der amerikanischen Rechtschreibung entsprechende Version anbietet, kann wie folgt
      kodiert werden.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-choice-egXML-lo" source="#COEDCOR-eg-71">
      <p>Lastly, That, upon his solemn oath to observe all the above
        articles, the said man-mountain shall have a daily allowance of
        meat and drink sufficient for the support of <choice><sic>1724</sic><corr>1728</corr></choice> of our subjects,
        with free access to our royal person, and other marks of our
        <choice><orig>favour</orig><reg>favor</reg></choice>.</p>
    </egXML>
    <!-- Gulliver's Travels -->
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">L'encodage d'une édition des <title>Essais</title> pourra faire état à la fois des formes
        originales et des formes modernisées correspondantes:.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-choice-egXML-yg" source="#fr-ex-Montaigne_Essais">
      <p>Ainsi lecteur, je suis<choice><orig>moy-mesmes</orig><reg>moi-même</reg></choice> la matière de mon livre : ce n'est pas raison que tu emploies ton loisir en un <choice><orig>subject</orig><reg>sujet</reg></choice>si frivole et si vain.</p>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-choice-egXML-qd">
      <p>清朝與日本為爭奪北韓半島控制權，爆發歷史上著名的甲午戰爭。 發生於清光緒二十年，西元 <choice><sic>1892</sic><corr>1894</corr></choice>年，雙方水陸大戰，傷亡者<choice><orig>衆</orig><reg>眾</reg></choice>。</p>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="choice-remarks" versionDate="2010-05-01" xml:lang="en">
    <p>Because the children of a  <gi>choice</gi> element all
            represent alternative ways of encoding the same sequence, it is
            natural to think of them as mutually exclusive. However, there may
            be cases where a full representation of a text requires the
            alternative encodings to be considered as parallel. </p>
    <p>Note also that <gi>choice</gi> elements may self-nest.</p>
    <p>Where the purpose of an encoding is to record multiple
            witnesses of a single work, rather than to identify
    multiple possible encoding decisions at a given point, the
    <gi>app</gi> element and associated elements discussed in  section
    <ptr target="#TCAPLL"/> should be preferred.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="choice-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Parce que les éléments contenus par un élément <gi>choice</gi> correspondent  tous à des solutions
            possibles  pour encoder la même séquence, il est naturel de les envisager comme
            exclusifs les uns des autres. Toutefois il peut y avoir des cas où la pleine
            représentation d'un texte requiert de considérer ces encodages alternatifs comme
            parallèles.</p>
    <p>A Noter aussi que les <gi>choice</gi> peuvent s'imbriquer. </p>
    <p>Pour une version de <gi>choice</gi> spécialisée pour l'encodage de témoins multiples
            d'une même oeuvre, l'élément <gi>app</gi> peut etre préférable : voir la section <ptr target="#TCAPLL"/>.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="choice-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Porque los niños de un elemento <gi>opción</gi> representan las maneras alternativas de codificar la misma secuencia, es natural pensar en ellas como mutuamente exclusivas.
            Sin embargo, puede haber casos donde una representación completa de un texto requiera que las codificaciones alternativas sean consideradas como paralelas. </p>
    <p>Se Observa también que los elementos <gi>opción</gi> pueden ser uno mismo-jerarquía.</p>
    <p>Para una versión especializada de la <gi>opción</gi> para codificar los testimonios múltiples de un único trabajo, ver la sección <ptr target="#TCAPLL"/>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="choice-remarks" versionDate="2024-02-28" xml:lang="ja">
    <p>
      <gi>choice</gi>要素の子要素は全て、同じ部分の異なる選択肢を示しているので、それらは択一的であるとするのが自然である。
      けれども、テキストを完全に表現するには複数の選択肢を並列的に扱う必要がある場合もあるだろう。</p>
      <p><gi>choice</gi>要素は、自らを入れ子にできることにも注意して欲しい。</p>
      <p>符号化時にありうる選択肢ではなく、1つの作品にある複数の本文を記録する目的では、
      <ptr target="#TCAPLL"/>で扱われている<gi>app</gi>要素などが望ましい。</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="choice-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>
          Da die Kindelemente des <gi>choice</gi>-Elements alternative Kodierungsmöglichkeiten der selben Textstelle repräsentieren, 
          ist es naheliegend, sie als sich gegenseitig ausschließend zu betrachten. Es sind jedoch Fälle vorstellbar, 
          in der Kodierungsalternativen als Kodierungsparallelen verstanden werden müssen, um den Text vollständig zu repräsentieren. 
      </p>
      <p>
          Man beachte außerdem, dass <gi>choice</gi>-Elemente weitere <gi>choice</gi>-Elemente als Kindelemente enthalten können.
      </p>
      <p>
          In Fällen, in denen nicht mehrere mögliche Kodierungsvarianten, sondern Varianten aus mehreren Zeugen eines Werkes kodiert werden sollen, 
          sind das <gi>app</gi>-Element und dazu gehörige Elemente, die im Abschnitt <ptr target="#TCAPLL"/> erläutert werden, zu bevorzugen.
      </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COED" type="div3"/>
  </listRef>
```

^b23

