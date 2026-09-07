---
type: representation
source-type: document
source: '[[00_sources/tei-p5-speaker-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 speaker
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/speaker.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# speaker

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5288. Git blob: `f50b20eae9f8fdc7741a519406bcd4ce1e9c57db`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-speaker" ident="speaker">
  <gloss versionDate="2005-01-14" xml:lang="en"/>
  <gloss versionDate="2009-01-06" xml:lang="fr">locuteur</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">講者</gloss>
  <gloss versionDate="2017-06-13" xml:lang="de">Sprecher</gloss> 
  <desc versionDate="2012-12-27" xml:lang="en">contains a specialized form of heading or label, giving the name of one or more speakers in a
        dramatic text or fragment.</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">forme particulière de titre ou de marque qui donne le
        nom d'un ou de  plusieurs locuteurs dans un texte ou dans un fragment de texte écrit pour le
        théâtre.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">una forma especializada de encabezamiento o etiqueta,
        que da nombre a uno o más interlocutores de un texto o fragmento dramático.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">特殊的標題或標籤形式，用來表明劇本中ㄧ位或多位講者名稱。</desc>
  <desc versionDate="2007-01-21" xml:lang="it">Forma specializzata di intestazione o etichetta che
        fornisce i nomi di uno o più parlanti in un testo o frammento drammatico.</desc>
  <desc versionDate="2006-10-28" xml:lang="ja">舞台関連の文章に出てくる1人以上の発話者の名前を示す。見出しやラベル として書かれる。</desc>
  <desc versionDate="2017-06-13" xml:lang="de">enthält eine spezielle Form von Überschrift oder Bezeichnung für einen oder mehrere Namen von
    Figuren in einem Dramentext oder -fragment.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.written"/>
    </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-speaker-egXML-fm">
      <sp who="#ni #rsa">
        <speaker>Nancy and Robert</speaker>
        <stage type="delivery">(speaking simultaneously)</stage>
        <p>The future? ...</p>
      </sp>
      <list type="speakers">
        <item xml:id="ni"/>
        <item xml:id="rsa"/>
      </list>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-speaker-egXML-ym" source="#fr-ex-Koltes_Quai_Vol">
      <sp who="ko">
        <speaker>Koch.</speaker>
        <p>Ne risquez rien du tout, Monique ; rentrez.</p>
      </sp>
      <sp who="mo">
        <speaker>Monique.</speaker>
        <p>Rentrer ? comment voulez-vous que je rentre ? J'ai les clés de la voiture.</p>
      </sp>
      <sp who="ko">
        <speaker>Koch.</speaker>
        <p> Je rentrerai par mes propres moyens. </p>
      </sp>
      <sp who="mo">
        <speaker>Monique.</speaker>
        <p> Vous ? vos moyens ? quels moyens ? Seigneur ! Vous ne savez même pas conduire, vous ne
            savez pas reconnaître votre gauche de votre droite, vous auriez été incapable de
            retrouver ce fichu quartier tout seul, vous ne savez absolument rien faire tout seul. Je
            me demande bien comment vous pourriez rentrer. </p>
      </sp>
      <sp who="ko">
        <speaker>Koch.</speaker>
        <p>J'appellerai un taxi.</p>
      </sp>
      <list type="speakers">
        <item xml:id="fr_mo"/>
        <item xml:id="fr_ko"/>
      </list>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-speaker-egXML-nj" source="#biblzh-tw_n23-24">
      <sp who="#zh-tw_ni #zh-tw_rsa">
        <speaker>梁山伯與祝英台t</speaker>
        <stage type="演講或歌唱">（同時)</stage>
        <p>梁山伯與祝英台，生不成雙死不分，生不成雙死不分。</p>
      </sp>
      <list type="speakers">
        <item xml:id="zh-tw_ni"/>
        <item xml:id="zh-tw_rsa"/>
      </list>
    </egXML>
  </exemplum>
  <remarks ident="speaker-remarks" versionDate="2023-01-13" xml:lang="en">
    <p>This element may be used to transcribe which character is
    speaking in a dramatic text as indicated by the source text; the
    <att>who</att> attribute of an <gi>sp</gi> element may be used to
    point to another element (typically a <gi>role</gi>) which
    provides information about the character speaking. Either or both
    may be used.</p>
  </remarks>
  <remarks ident="speaker-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est utilisé pour indiquer quel personnage prend la parole dans une pièce de
            théâtre ; l'attribut <att>who</att> est utilisé pour pointer vers un autre élément qui fournit des
            informations sur ce personnage. L'un et ou l'autre peuvent être utilisés.</p>
  </remarks>
  <listRef>
    <ptr target="#CODR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en"/>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">locuteur</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">講者</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2017-06-13" xml:lang="de">Sprecher</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">contains a specialized form of heading or label, giving the name of one or more speakers in a
        dramatic text or fragment.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">forme particulière de titre ou de marque qui donne le
        nom d'un ou de  plusieurs locuteurs dans un texte ou dans un fragment de texte écrit pour le
        théâtre.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">una forma especializada de encabezamiento o etiqueta,
        que da nombre a uno o más interlocutores de un texto o fragmento dramático.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">特殊的標題或標籤形式，用來表明劇本中ㄧ位或多位講者名稱。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">Forma specializzata di intestazione o etichetta che
        fornisce i nomi di uno o più parlanti in un testo o frammento drammatico.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-28" xml:lang="ja">舞台関連の文章に出てくる1人以上の発話者の名前を示す。見出しやラベル として書かれる。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2017-06-13" xml:lang="de">enthält eine spezielle Form von Überschrift oder Bezeichnung für einen oder mehrere Namen von
    Figuren in einem Dramentext oder -fragment.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.written"/>
    </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-speaker-egXML-fm">
      <sp who="#ni #rsa">
        <speaker>Nancy and Robert</speaker>
        <stage type="delivery">(speaking simultaneously)</stage>
        <p>The future? ...</p>
      </sp>
      <list type="speakers">
        <item xml:id="ni"/>
        <item xml:id="rsa"/>
      </list>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-speaker-egXML-ym" source="#fr-ex-Koltes_Quai_Vol">
      <sp who="ko">
        <speaker>Koch.</speaker>
        <p>Ne risquez rien du tout, Monique ; rentrez.</p>
      </sp>
      <sp who="mo">
        <speaker>Monique.</speaker>
        <p>Rentrer ? comment voulez-vous que je rentre ? J'ai les clés de la voiture.</p>
      </sp>
      <sp who="ko">
        <speaker>Koch.</speaker>
        <p> Je rentrerai par mes propres moyens. </p>
      </sp>
      <sp who="mo">
        <speaker>Monique.</speaker>
        <p> Vous ? vos moyens ? quels moyens ? Seigneur ! Vous ne savez même pas conduire, vous ne
            savez pas reconnaître votre gauche de votre droite, vous auriez été incapable de
            retrouver ce fichu quartier tout seul, vous ne savez absolument rien faire tout seul. Je
            me demande bien comment vous pourriez rentrer. </p>
      </sp>
      <sp who="ko">
        <speaker>Koch.</speaker>
        <p>J'appellerai un taxi.</p>
      </sp>
      <list type="speakers">
        <item xml:id="fr_mo"/>
        <item xml:id="fr_ko"/>
      </list>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-speaker-egXML-nj" source="#biblzh-tw_n23-24">
      <sp who="#zh-tw_ni #zh-tw_rsa">
        <speaker>梁山伯與祝英台t</speaker>
        <stage type="演講或歌唱">（同時)</stage>
        <p>梁山伯與祝英台，生不成雙死不分，生不成雙死不分。</p>
      </sp>
      <list type="speakers">
        <item xml:id="zh-tw_ni"/>
        <item xml:id="zh-tw_rsa"/>
      </list>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="speaker-remarks" versionDate="2023-01-13" xml:lang="en">
    <p>This element may be used to transcribe which character is
    speaking in a dramatic text as indicated by the source text; the
    <att>who</att> attribute of an <gi>sp</gi> element may be used to
    point to another element (typically a <gi>role</gi>) which
    provides information about the character speaking. Either or both
    may be used.</p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="speaker-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est utilisé pour indiquer quel personnage prend la parole dans une pièce de
            théâtre ; l'attribut <att>who</att> est utilisé pour pointer vers un autre élément qui fournit des
            informations sur ce personnage. L'un et ou l'autre peuvent être utilisés.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CODR"/>
  </listRef>
```

^b19

