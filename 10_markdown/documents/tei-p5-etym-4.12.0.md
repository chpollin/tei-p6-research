---
type: representation
source-type: document
source: '[[00_sources/tei-p5-etym-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 etym
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/etym.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# etym

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7122. Git blob: `00ee44ace6a7bb6b926092f41095910f0384170d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-etym" ident="etym">
  <gloss versionDate="2005-01-14" xml:lang="en">etymology</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">어원</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">詞源</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">étymologie</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">etimología</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">etimologia</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">encloses the etymological information in a dictionary entry.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전 표제 항목의 어원 정보를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含詞源學資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書項目の語源情報を示す。</desc>
  <desc versionDate="2009-02-23" xml:lang="fr">contient les informations sur l'étymologie de l'entrée.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">engloba la información etimológica en una entrada de
    diccionario.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">comprende informazioni etimologiche in una voce di
    dizionario.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.global"/>
        <classRef key="model.inter"/>
        <classRef key="model.phrase"/>
        <elementRef key="def"/>
        <elementRef key="etym"/>
        <elementRef key="gramGrp"/>
        <elementRef key="lbl"/>
        <elementRef key="usg"/>
        <elementRef key="xr"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-to"><entry><form><orth>publish</orth> ... </form><etym><lang>ME.</lang><mentioned>publisshen</mentioned>,
          <lang>F.</lang><mentioned>publier</mentioned>, <lang>L.</lang><mentioned>publicare,
            publicatum</mentioned>. <xr>See <ref>public</ref>; cf. 2d <ref>-ish</ref>.</xr></etym></entry> (From: Webster's Second International)</egXML>
  </exemplum>
  <exemplum versionDate="2018-01-23" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-cm">
      <entry>
        <form><orth>weekend</orth> ... </form>
        <etym type="borrowing">
          <lbl>source:</lbl> <lang>English</lang> <oRef>weekend</oRef>
        </etym>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2018-01-23" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-oh">
      <entry>
        <form><orth>Handschuh</orth> ... </form>
        <etym type="compounding"><oRef>Hand</oRef> (<pRef notation="ipa">ˈhant</pRef>): <gloss>hand</gloss>,
          <etym type="metaphor"><oRef>Schuh</oRef> (<pRef notation="ipa">ʃuː</pRef>): <gloss>shoe</gloss></etym>
        </etym>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-te" source="#fr-ex-TLFI">
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-ea">
      <entry>
        <form><orth>佛陀</orth> ... </form>
        <etym>從<lang>梵語</lang>
               <term>buddha</term>傳入的<lang>中古漢語</lang>音譯; </etym>
      </entry>
    </egXML>
  </exemplum>
  <remarks ident="etym-remarks" versionDate="2007-02-27" xml:lang="en">
    <p rend="dataDesc">May contain character data mixed with any other elements defined in the
      dictionary tag set.</p>
    <p>There is no consensus on the internal structure of etymologies, or even on whether such a
      structure is appropriate. The <gi>etym</gi> element accordingly simply contains prose, within
      which names of languages, cited words, or parts of words, glosses, and examples will typically
      be prominent. The tagging of such internal objects is optional.</p>
  </remarks>
  <remarks ident="etym-remarks" versionDate="2009-02-23" xml:lang="fr">
    <p rend="dataDesc"> Peut contenir des caractères combinés avec n'importe quels autres éléments
      définis dans le jeu de balises propre aux dictionnaires. </p>
    <p> Il n'y a aucun consensus sur la structure interne propre à une étymologie, ou même sur le
      fait qu'une telle structure soit appropriée. L'élément <gi>etym</gi> ne contient donc que du
      texte non structuré, dans lequel les noms de langues, les mots cités, ou les parties de mots,
      les gloses et les exemples seront mis en valeur. L'encodage de tels objets internes est
      facultatif.</p>
  </remarks>
  <remarks ident="etym-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 辞書向けの要素を伴う文字列をとるかもしれない。 </p>
    <p> 語源情報に関する内容の構造について、決められたものはない。要素 <gi>etym</gi>は、引用語句、語の一部、語句注釈として散文をとること
      になる。用例は重要になるだろう。このような内容の記述は選択的である。 </p>
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
<gloss versionDate="2005-01-14" xml:lang="en">etymology</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">어원</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">詞源</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">étymologie</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">etimología</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">etimologia</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">encloses the etymological information in a dictionary entry.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전 표제 항목의 어원 정보를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含詞源學資訊。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書項目の語源情報を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-02-23" xml:lang="fr">contient les informations sur l'étymologie de l'entrée.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">engloba la información etimológica en una entrada de
    diccionario.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">comprende informazioni etimologiche in una voce di
    dizionario.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.global"/>
        <classRef key="model.inter"/>
        <classRef key="model.phrase"/>
        <elementRef key="def"/>
        <elementRef key="etym"/>
        <elementRef key="gramGrp"/>
        <elementRef key="lbl"/>
        <elementRef key="usg"/>
        <elementRef key="xr"/>
      </alternate>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-to"><entry><form><orth>publish</orth> ... </form><etym><lang>ME.</lang><mentioned>publisshen</mentioned>,
          <lang>F.</lang><mentioned>publier</mentioned>, <lang>L.</lang><mentioned>publicare,
            publicatum</mentioned>. <xr>See <ref>public</ref>; cf. 2d <ref>-ish</ref>.</xr></etym></entry> (From: Webster's Second International)</egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2018-01-23" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-cm">
      <entry>
        <form><orth>weekend</orth> ... </form>
        <etym type="borrowing">
          <lbl>source:</lbl> <lang>English</lang> <oRef>weekend</oRef>
        </etym>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2018-01-23" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-oh">
      <entry>
        <form><orth>Handschuh</orth> ... </form>
        <etym type="compounding"><oRef>Hand</oRef> (<pRef notation="ipa">ˈhant</pRef>): <gloss>hand</gloss>,
          <etym type="metaphor"><oRef>Schuh</oRef> (<pRef notation="ipa">ʃuː</pRef>): <gloss>shoe</gloss></etym>
        </etym>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-te" source="#fr-ex-TLFI">
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

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-etym-egXML-ea">
      <entry>
        <form><orth>佛陀</orth> ... </form>
        <etym>從<lang>梵語</lang>
               <term>buddha</term>傳入的<lang>中古漢語</lang>音譯; </etym>
      </entry>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="etym-remarks" versionDate="2007-02-27" xml:lang="en">
    <p rend="dataDesc">May contain character data mixed with any other elements defined in the
      dictionary tag set.</p>
    <p>There is no consensus on the internal structure of etymologies, or even on whether such a
      structure is appropriate. The <gi>etym</gi> element accordingly simply contains prose, within
      which names of languages, cited words, or parts of words, glosses, and examples will typically
      be prominent. The tagging of such internal objects is optional.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="etym-remarks" versionDate="2009-02-23" xml:lang="fr">
    <p rend="dataDesc"> Peut contenir des caractères combinés avec n'importe quels autres éléments
      définis dans le jeu de balises propre aux dictionnaires. </p>
    <p> Il n'y a aucun consensus sur la structure interne propre à une étymologie, ou même sur le
      fait qu'une telle structure soit appropriée. L'élément <gi>etym</gi> ne contient donc que du
      texte non structuré, dans lequel les noms de langues, les mots cités, ou les parties de mots,
      les gloses et les exemples seront mis en valeur. L'encodage de tels objets internes est
      facultatif.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="etym-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 辞書向けの要素を伴う文字列をとるかもしれない。 </p>
    <p> 語源情報に関する内容の構造について、決められたものはない。要素 <gi>etym</gi>は、引用語句、語の一部、語句注釈として散文をとること
      になる。用例は重要になるだろう。このような内容の記述は選択的である。 </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPET" type="div2"/>
  </listRef>
```

^b24

