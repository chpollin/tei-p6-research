---
type: representation
source-type: document
source: '[[00_sources/tei-p5-lang-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 lang
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/lang.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# lang

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4854. Git blob: `6898731bdf010fe9343c6fc4eb3719735e819d09`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-lang" ident="lang">
  <gloss versionDate="2005-01-14" xml:lang="en">language name</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">언어명</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">語言名稱</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">nom de la langue</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nombre de lengua</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nome di un alingua</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">contains the name of a language mentioned in etymological or other linguistic discussion.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어원적 또는 기타 언어적 논의에서 언급된 언어의 이름</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在詞源學或其他語言學相關訊息中所提到的語言。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">語源学または他の言語学上の論議で現れる言語名を示す。</desc>
  <desc versionDate="2009-04-08" xml:lang="fr">nom de la langue mentionnée des informations de nature linguistique (étymologique ou autre).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">el nombre de una lengua mencionada en una información etimológica o lingüística de cualquier tipo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">il nome di una lingua menzionata nell'etimologia o in altra discussione linguistica.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.nameLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lang-egXML-fu">
      <entry>
        <form><orth>publish</orth> ... </form>
        <etym><lang>ME.</lang><mentioned>publisshen</mentioned>,
          <lang>F.</lang><mentioned>publier</mentioned>, <lang>L.</lang><mentioned>publicare,
            publicatum</mentioned>. <xr>See <ref>public</ref>; cf. <ref>2d -ish</ref>.</xr></etym>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lang-egXML-hg" source="#fr-ex-TLFI">
      <entry>
        <form><orth>publier</orth> ... </form>
        <etym>Emprunté au <lang>latin</lang>
               <mentioned>publicare</mentioned>
               <def>mettre à la disposition du public ; montrer au public ; publier (un livre)</def> ,
              <label>dérivé de </label>
               <mentioned>publicus</mentioned>, <xr>v.
            <ref>public1</ref>
               </xr>. La forme <mentioned>puplier</mentioned>, <mentioned>poplier</mentioned>
               <label>attesté en </label>
               <lang>anc. fr.</lang>
               <xr> (v. <ref>supra, <bibl>Grand
                  dictionnaire de la langue française</bibl>. et.
              <bibl>Tobler-Lommatzsch</bibl>
                  </ref>.)</xr> à côté de<mentioned> publier</mentioned>,
            que l'on trouve à partir de la <date>2e moitié du XIIIe s.</date>
               <bibl>[ms. de la <date>fin XIIIe s.</date>] </bibl>
               <bibl>(Légende de Girart de
              Roussillon, 64 dans Tobler-Lommatzsch),</bibl> est une <label>altération
              d'après</label>
               <mentioned> peuple</mentioned>.</etym>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lang-egXML-bo">
      <entry>
        <form><orth>佛陀</orth> ... </form>
        <etym>從<lang>梵語</lang>
               <term>buddha</term>傳入的<lang>中古漢語</lang>音譯; </etym>
      </entry>
    </egXML>
  </exemplum>
  <remarks ident="lang-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data mixed with phrase-level elements.</p>
  </remarks>
  <remarks ident="lang-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères combinés avec des éléments du niveau
    expression.</p>
  </remarks>
  <remarks ident="lang-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 句レベル要素と共に文字データを含むかもしれない。 </p>
  </remarks>
  <listRef>
    <ptr target="#DITPET" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">language name</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">언어명</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">語言名稱</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">nom de la langue</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">nombre de lengua</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">nome di un alingua</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains the name of a language mentioned in etymological or other linguistic discussion.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어원적 또는 기타 언어적 논의에서 언급된 언어의 이름</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在詞源學或其他語言學相關訊息中所提到的語言。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">語源学または他の言語学上の論議で現れる言語名を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-08" xml:lang="fr">nom de la langue mentionnée des informations de nature linguistique (étymologique ou autre).</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">el nombre de una lengua mencionada en una información etimológica o lingüística de cualquier tipo.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">il nome di una lingua menzionata nell'etimologia o in altra discussione linguistica.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.nameLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lang-egXML-fu">
      <entry>
        <form><orth>publish</orth> ... </form>
        <etym><lang>ME.</lang><mentioned>publisshen</mentioned>,
          <lang>F.</lang><mentioned>publier</mentioned>, <lang>L.</lang><mentioned>publicare,
            publicatum</mentioned>. <xr>See <ref>public</ref>; cf. <ref>2d -ish</ref>.</xr></etym>
      </entry>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lang-egXML-hg" source="#fr-ex-TLFI">
      <entry>
        <form><orth>publier</orth> ... </form>
        <etym>Emprunté au <lang>latin</lang>
               <mentioned>publicare</mentioned>
               <def>mettre à la disposition du public ; montrer au public ; publier (un livre)</def> ,
              <label>dérivé de </label>
               <mentioned>publicus</mentioned>, <xr>v.
            <ref>public1</ref>
               </xr>. La forme <mentioned>puplier</mentioned>, <mentioned>poplier</mentioned>
               <label>attesté en </label>
               <lang>anc. fr.</lang>
               <xr> (v. <ref>supra, <bibl>Grand
                  dictionnaire de la langue française</bibl>. et.
              <bibl>Tobler-Lommatzsch</bibl>
                  </ref>.)</xr> à côté de<mentioned> publier</mentioned>,
            que l'on trouve à partir de la <date>2e moitié du XIIIe s.</date>
               <bibl>[ms. de la <date>fin XIIIe s.</date>] </bibl>
               <bibl>(Légende de Girart de
              Roussillon, 64 dans Tobler-Lommatzsch),</bibl> est une <label>altération
              d'après</label>
               <mentioned> peuple</mentioned>.</etym>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lang-egXML-bo">
      <entry>
        <form><orth>佛陀</orth> ... </form>
        <etym>從<lang>梵語</lang>
               <term>buddha</term>傳入的<lang>中古漢語</lang>音譯; </etym>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="lang-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data mixed with phrase-level elements.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="lang-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères combinés avec des éléments du niveau
    expression.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="lang-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 句レベル要素と共に文字データを含むかもしれない。 </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPET" type="div2"/>
  </listRef>
```

^b22

