---
type: representation
source-type: document
source: '[[00_sources/tei-p5-name-4.12.0.xml]]'
converter: tools.ingest_git_blobs v2; complete XML plus XML itertext English reading
  blocks with whitespace normalized and identified locators
channel: collection
metadata:
  title: TEI P5 4.12.0 name specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/name.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# name

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.
A locator names an element that carries an `ident` attribute by that ident, so the
reading block of an attribute definition states which attribute it describes.

Source byte length: 4047. Git blob: `57c610d9430e9a48113d4e9f994bc0bbb9ca2486`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-name" ident="name">
  <gloss versionDate="2005-01-14" xml:lang="en">name, proper noun</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">이름, 고유명사</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">名稱，特定名稱</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">nom, nom propre</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">nombre, nombre propio</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">nome, nome proprio</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Name, Eigenname</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a proper noun or noun phrase.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">고유명사 또는 명사구를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個特定名稱 或名詞詞組。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">固有名詞。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient un nom propre ou un syntagme nominal.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un nombre propio o un sintagma nominal</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un nome proprio o un sintagma nominale.</desc>
  <desc versionDate="2016-11-24" xml:lang="de">enthält einen Eigennamen in Form eines Nomens oder einer Nominalphrase.</desc>  
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.personal"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.nameLike.agent"/>
    <memberOf key="model.personPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-name-egXML-av" source="#NONE">
      <name type="person">Thomas Hoccleve</name>
      <name type="place">Villingaholt</name>
      <name type="org">Vetus Latina Institut</name>
      <name type="person" ref="#HOC001">Occleve</name>
    </egXML>
  </exemplum>
  <remarks ident="name-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>Proper nouns referring to people, places, and organizations may be tagged instead with
                <gi>persName</gi>, <gi>placeName</gi>, or <gi>orgName</gi>, when the TEI module for
            names and dates is included.</p>
  </remarks>
  <remarks ident="name-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les noms propres relatifs aux personnes, aux lieux et aux organismes peuvent également
            être balisés à l'aide de <gi>persName</gi>, <gi>placeName</gi>, ou <gi>orgName</gi>,
            lorsque le module TEI concernant les noms et dates est inclus.</p>
  </remarks>
  <remarks ident="name-remarks" versionDate="2008-04-05" xml:lang="ja">
      <p> TEI名前モジュールが使われる場合には、人々、場所、組織を示す固有名 詞は、それぞれ要素<gi>persName</gi>、<gi>placeName</gi>、<gi>orgName</gi>を使い示されるかもしれない。 </p>
  </remarks>
  <remarks ident="name-remarks" versionDate="2016-11-24" xml:lang="de">
      <p>
          Eigennamen, die auf Personen, Orte und Organisationen verweisen, können stattdessen auch mit den Elementen 
          <gi>persName</gi>, <gi>placeName</gi> oder <gi>orgName</gi> ausgezeichnet werden, vorausgesetzt, das TEI-Modul 
          <ident type="module">namesdates</ident> ist inkludiert.
      </p>
  </remarks>
  <listRef>
    <ptr target="#CONARS" type="div2"/>
  </listRef>
</elementSpec>
```

## English reading blocks

### Reading 1

XML location: `/elementSpec[@ident='name']/desc[1]`.

contains a proper noun or noun phrase. ^r1

### Reading 2

XML location: `/elementSpec[@ident='name']/remarks[@ident='name-remarks']/p[1]`.

Proper nouns referring to people, places, and organizations may be tagged instead with persName, placeName, or orgName, when the TEI module for names and dates is included. ^r2

