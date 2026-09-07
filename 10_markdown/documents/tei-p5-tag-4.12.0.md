---
type: representation
source-type: document
source: '[[00_sources/tei-p5-tag-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 tag
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/tag.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# tag

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10758. Git blob: `037ef1c9ad6ea5cdabca06ff069c55fce7dc09f2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="tagdocs" xml:id="gi-tag" ident="tag">
  <gloss versionDate="2007-06-12" xml:lang="en">tag</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">balise</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains text of a complete start- or end-tag, possibly including attribute specifications,
    but excluding the opening and closing markup delimiter characters.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">속성 명시를 포함하나 시작 및 종료 마크업 구분 문자를 제외한, 완전한 시작 또는 종료 태그의 텍스트를
    포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含具有完整開始標籤與結束標籤的文字，可能包括屬性說明，但不包含開頭及結尾標記定義符號。</desc>
  <desc versionDate="2008-04-06" xml:lang="ja">完全な開始タグ、終了タグのテキストを示す。属性規定はとることも可能だ
    が、タグ開始区切子、タグ終了区切子は含まない。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">le contenu d'une balise ouvrante ou fermante, avec
    éventuellement des spécifications d'attributs, mais à l'exclusion des caractères marquant
    l'ouverture et la fermeture de la balise.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene el texto completo de un marcador inicial o
    final, posiblemente incluyendo eventuales descripciones de atributos, pero nunca los caracteres
    de delimitación de inicio y fin del marcador.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene il testo completo di un marcatore iniziale o
    finale, ivi comprese eventuali descrizioni di attributi ma esclusi i caratteri di delimitazione
    di inizio e fine del marcatore</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.phrase.xml"/>
  </classes>
  <content>
    <textNode/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2008-04-05" xml:lang="en">indicates the type of XML tag intended.</desc>
      <desc versionDate="2009-01-23" xml:lang="fr">indique quel type de balise XML est prévu.</desc>
      <desc versionDate="2008-04-08" xml:lang="it">indica di quale tipo di marcatore XML si tratta.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="start">
          <desc versionDate="2008-04-05" xml:lang="en">a start-tag, with delimiters &lt; and &gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">une balise de début, délimitée par les signes
            &lt;et &gt; est prévue.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica uno start-tag delimitato dai segni
            &lt; e &gt;</desc>
        </valItem>
        <valItem ident="end">
          <desc versionDate="2008-04-05" xml:lang="en">an end-tag, with delimiters &lt;/ and &gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">une balise de fin, délimitée par les signes
            &lt;/ and &gt; est prévue.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica un end-tag delimitato dai segni &lt;/
            e &gt;</desc>
        </valItem>
        <valItem ident="empty">
          <desc versionDate="2008-04-05" xml:lang="en">an empty tag, with delimiters &lt; and /&gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">une balise vide, délimitée par les signes
            &lt; and /&gt; est prévue.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica un marcatore vuoto delimitato dai segni
            &lt; e /&gt;</desc>
        </valItem>
        <valItem ident="pi">
          <desc versionDate="2008-04-05" xml:lang="en">a pi (processing instruction), with delimiters &lt;? and ?&gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">un PI (Processing Instruction), délimité par les
            signes &lt;? and ?&gt; est prévu.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica una pi (istruzione di processing)
            delimitata dai segni &lt;? e ?&gt;</desc>
        </valItem>
        <valItem ident="comment">
          <desc versionDate="2008-04-05" xml:lang="en">a comment, with delimiters &lt;!-- and --&gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">un commentaire délimité par les signes
            &lt;!-- et --&gt; est prévu.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica un commento delimitato dai segni
            &lt;!-- e --&gt;</desc>
        </valItem>
        <valItem ident="ms">
          <desc versionDate="2008-04-05" xml:lang="en">a marked-section, with delimiters &lt;[CDATA[ and ]]&gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">une section marquée, délimitée par les signes
            &lt;[CDATA[ et ]]&gt; est prévue.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica una sezione marcata, delimitata dai segni
            &lt;[CDATA[ e ]]&gt;</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="scheme" usage="opt">
      <desc versionDate="2008-04-05" xml:lang="en">supplies the name of the schema in which this tag is defined.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 이름이 정의된 스키마의 이름을 제공한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供該標準之識別符碼，此名稱定義於該標準中。</desc>
      <desc versionDate="2008-04-06" xml:lang="ja">当該タグ名が定義されているスキームの名前を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit le nom du modèle dans lequel ce nom est
        défini</desc>
      <desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre del esquema en que tal nombre
        es definido.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">fornisce il nome dello schema in cui è definito il
        nome</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>TEI</defaultVal>
      <valList type="open">
        <valItem ident="TEI">
          <gloss versionDate="2007-07-04" xml:lang="en">text encoding initiative</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 부호화 표준</gloss>
          <desc versionDate="2008-04-05" xml:lang="en">This tag is defined as part of the TEI scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 태그는 TEI 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此標籤為TEI標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta etiqueta es parte del esquema de TEI.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該タグは、TEIスキームに属する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette balise fait partie d'un modèle TEI.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il marcatore è parte dello schema TEI.</desc>
        </valItem>
        <valItem ident="DBK">
          <gloss versionDate="2007-07-04" xml:lang="en">docbook</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">도크북</gloss>
          <desc versionDate="2007-07-04" xml:lang="en">this tag is part of the Docbook scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 태그는 Docbook 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此標籤為Dockbook標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta etiqueta es parte del esquema de Docbook.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該タグは、DOcbookスキームに属する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette balise fait partie d'un modèle Docbook.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il marcatore è parte dello schema Docbook.</desc>
        </valItem>
        <valItem ident="XX">
          <gloss versionDate="2007-07-04" xml:lang="en">unknown</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">미지의</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">desconocido</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">inconnu</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sconosciuto</gloss>
          <desc versionDate="2007-07-04" xml:lang="en">this tag is part of an unknown scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 태그는 미지의 스키마의 부분이다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta etiqueta es parte de un esquema desconocido.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該タグは、不明スキームに属する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette balise fait partie d'un modèle inconnu.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">il marcatore è parte di uno schema
          sconosciuto</desc>
        </valItem>
        <valItem ident="Schematron"/>
        <valItem ident="HTML"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tag-egXML-qd">Mark the start of each italicised phrase with a
        <tag>hi rend="it"</tag> tag, and its end with a <tag type="end">hi</tag> tag.<tag type="comment">Example updated on 2008-04-05</tag>
      </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tag-egXML-fs">Marque le début de tout groupe de mots en
        italique avec la balise <tag>hi rend="it"</tag>, et le termine avec le tag <tag type="end">hi</tag>
         <tag type="comment">Example updated on 2008-04-05</tag>
      </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tag-egXML-hg"> 於所有斜體字的前頭以<tag>hi rend="it"</tag>
      標籤，並以<tag>/hi</tag>標籤結尾。</egXML>
  </exemplum>
  <listRef>
    <ptr target="#TD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">tag</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">balise</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains text of a complete start- or end-tag, possibly including attribute specifications,
    but excluding the opening and closing markup delimiter characters.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">속성 명시를 포함하나 시작 및 종료 마크업 구분 문자를 제외한, 완전한 시작 또는 종료 태그의 텍스트를
    포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含具有完整開始標籤與結束標籤的文字，可能包括屬性說明，但不包含開頭及結尾標記定義符號。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">完全な開始タグ、終了タグのテキストを示す。属性規定はとることも可能だ
    が、タグ開始区切子、タグ終了区切子は含まない。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">le contenu d'une balise ouvrante ou fermante, avec
    éventuellement des spécifications d'attributs, mais à l'exclusion des caractères marquant
    l'ouverture et la fermeture de la balise.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene el texto completo de un marcador inicial o
    final, posiblemente incluyendo eventuales descripciones de atributos, pero nunca los caracteres
    de delimitación de inicio y fin del marcador.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene il testo completo di un marcatore iniziale o
    finale, ivi comprese eventuali descrizioni di attributi ma esclusi i caratteri di delimitazione
    di inizio e fine del marcatore</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.phrase.xml"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <textNode/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2008-04-05" xml:lang="en">indicates the type of XML tag intended.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-23" xml:lang="fr">indique quel type de balise XML est prévu.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-08" xml:lang="it">indica di quale tipo di marcatore XML si tratta.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="start">
          <desc versionDate="2008-04-05" xml:lang="en">a start-tag, with delimiters &lt; and &gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">une balise de début, délimitée par les signes
            &lt;et &gt; est prévue.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica uno start-tag delimitato dai segni
            &lt; e &gt;</desc>
        </valItem>
        <valItem ident="end">
          <desc versionDate="2008-04-05" xml:lang="en">an end-tag, with delimiters &lt;/ and &gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">une balise de fin, délimitée par les signes
            &lt;/ and &gt; est prévue.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica un end-tag delimitato dai segni &lt;/
            e &gt;</desc>
        </valItem>
        <valItem ident="empty">
          <desc versionDate="2008-04-05" xml:lang="en">an empty tag, with delimiters &lt; and /&gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">une balise vide, délimitée par les signes
            &lt; and /&gt; est prévue.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica un marcatore vuoto delimitato dai segni
            &lt; e /&gt;</desc>
        </valItem>
        <valItem ident="pi">
          <desc versionDate="2008-04-05" xml:lang="en">a pi (processing instruction), with delimiters &lt;? and ?&gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">un PI (Processing Instruction), délimité par les
            signes &lt;? and ?&gt; est prévu.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica una pi (istruzione di processing)
            delimitata dai segni &lt;? e ?&gt;</desc>
        </valItem>
        <valItem ident="comment">
          <desc versionDate="2008-04-05" xml:lang="en">a comment, with delimiters &lt;!-- and --&gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">un commentaire délimité par les signes
            &lt;!-- et --&gt; est prévu.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica un commento delimitato dai segni
            &lt;!-- e --&gt;</desc>
        </valItem>
        <valItem ident="ms">
          <desc versionDate="2008-04-05" xml:lang="en">a marked-section, with delimiters &lt;[CDATA[ and ]]&gt; is intended</desc>
          <desc versionDate="2009-01-23" xml:lang="fr">une section marquée, délimitée par les signes
            &lt;[CDATA[ et ]]&gt; est prévue.</desc>
          <desc versionDate="2008-04-08" xml:lang="it">indica una sezione marcata, delimitata dai segni
            &lt;[CDATA[ e ]]&gt;</desc>
        </valItem>
      </valList>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2008-04-05" xml:lang="en">supplies the name of the schema in which this tag is defined.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 이름이 정의된 스키마의 이름을 제공한다.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供該標準之識別符碼，此名稱定義於該標準中。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="ja">当該タグ名が定義されているスキームの名前を示す。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit le nom du modèle dans lequel ce nom est
        défini</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona el nombre del esquema en que tal nombre
        es definido.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce il nome dello schema in cui è definito il
        nome</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>TEI</defaultVal>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="TEI">
          <gloss versionDate="2007-07-04" xml:lang="en">text encoding initiative</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">텍스트 부호화 표준</gloss>
          <desc versionDate="2008-04-05" xml:lang="en">This tag is defined as part of the TEI scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 태그는 TEI 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此標籤為TEI標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta etiqueta es parte del esquema de TEI.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該タグは、TEIスキームに属する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette balise fait partie d'un modèle TEI.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il marcatore è parte dello schema TEI.</desc>
        </valItem>
        <valItem ident="DBK">
          <gloss versionDate="2007-07-04" xml:lang="en">docbook</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">도크북</gloss>
          <desc versionDate="2007-07-04" xml:lang="en">this tag is part of the Docbook scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 태그는 Docbook 스키마의 부분이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">此標籤為Dockbook標準的一部份。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta etiqueta es parte del esquema de Docbook.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該タグは、DOcbookスキームに属する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette balise fait partie d'un modèle Docbook.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il marcatore è parte dello schema Docbook.</desc>
        </valItem>
        <valItem ident="XX">
          <gloss versionDate="2007-07-04" xml:lang="en">unknown</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">미지의</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">desconocido</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">inconnu</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sconosciuto</gloss>
          <desc versionDate="2007-07-04" xml:lang="en">this tag is part of an unknown scheme.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">이 태그는 미지의 스키마의 부분이다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">esta etiqueta es parte de un esquema desconocido.</desc>
          <desc versionDate="2008-04-06" xml:lang="ja">当該タグは、不明スキームに属する。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">cette balise fait partie d'un modèle inconnu.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">il marcatore è parte di uno schema
          sconosciuto</desc>
        </valItem>
        <valItem ident="Schematron"/>
        <valItem ident="HTML"/>
      </valList>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tag-egXML-qd">Mark the start of each italicised phrase with a
        <tag>hi rend="it"</tag> tag, and its end with a <tag type="end">hi</tag> tag.<tag type="comment">Example updated on 2008-04-05</tag>
      </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tag-egXML-fs">Marque le début de tout groupe de mots en
        italique avec la balise <tag>hi rend="it"</tag>, et le termine avec le tag <tag type="end">hi</tag>
         <tag type="comment">Example updated on 2008-04-05</tag>
      </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tag-egXML-hg"> 於所有斜體字的前頭以<tag>hi rend="it"</tag>
      標籤，並以<tag>/hi</tag>標籤結尾。</egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TD"/>
  </listRef>
```

^b30

