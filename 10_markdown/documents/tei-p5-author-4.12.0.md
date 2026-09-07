---
type: representation
source-type: document
source: '[[00_sources/tei-p5-author-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 author
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/author.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# author

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9440. Git blob: `97e26b3bc113969e7e20dfedc7a40cbb863563a6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-author" ident="author">
  <gloss xml:lang="en" versionDate="2011-11-26">author</gloss>
  <gloss xml:lang="es" versionDate="2022-02-24">autor/a</gloss>
  <gloss versionDate="2011-11-26" xml:lang="fr">auteur</gloss>
  <gloss versionDate="2017-06-04" xml:lang="de">Autor</gloss>
  <desc versionDate="2011-11-26" xml:lang="en">in a bibliographic reference, contains the name(s) of an author, personal or corporate, of a work; for example in the same form as that provided by a recognized bibliographic name authority.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">참고문헌에 작가, 단독 저자, 공동 저자의 이름을 포함한다; 서지 항목의 책임에 관한 1차적 진술.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在書目參照中，包含一件作品的作者 (群) 姓名，無論是個人或是團體性質；這也是書目項目責任歸屬的主要陳述。</desc>
  <desc versionDate="2023-08-30" xml:lang="ja">書誌参照において、作品の著者となる人や法人の名前を、たとえば、よく知られた書誌典拠情報機関の形式で提供されるものに合わせるなどして記述する。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">dans une référence bibliographique contient le nom de la (des) personne(s) physique(s) ou du collectif, auteur(s) d'une oeuvre ; par exemple dans la même forme que celle utilisée par une référence bibliographique reconnue.</desc>
  <desc versionDate="2022-02-24" xml:lang="es">en una referencia bibliográfica, contiene el nombre del autor/a/es, ya sea una persona o una institución, de una obra; por ejemplo, en la misma forma que la proporcionada por una autoridad bibliográfica reconocida.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">in un riferimento bibliografico contiene il nome dell'autore (o degli autori), personale o collettivo, di un'opera; è la dichiarazione di responsabilità primaria di ciascuna unità bibliografica.</desc>
  <desc versionDate="2017-06-04" xml:lang="de">enthält in einer bibliografischen Referenz den oder die Namen eines Autors eines Werks (oder einer für das Werk verantwortlichen Körperschaft); zum Beispiel in der Form, wie sie eine anerkannte bibliografische Instanz anbietet.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.naming"/>
    <memberOf key="model.respLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-author-egXML-lq" source="#COBICOR-eg-251">
      <author>British Broadcasting Corporation</author>
      <author>La Fayette, Marie Madeleine Pioche de la Vergne, comtesse de (1634–1693)</author>
      <author>Anonymous</author>
      <author>Bill and Melinda Gates Foundation</author>
      <author>
        <persName>Beaumont, Francis</persName>
        and
        <persName>John Fletcher</persName>
      </author>
      <author><orgName key="BBC">British Broadcasting
      Corporation</orgName>: Radio 3 Network</author>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-author-egXML-zl">
      <author>La Fayette, Marie Madeleine Pioche de la Vergne, comtesse de (1634–1693)</author>
      <author>Anonyme</author>
      <author>Erckmann-Chatrian</author>
      <author>
        <orgName key="ARTE">Association relative à la télévision européenne</orgName>
      </author>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-author-egXML-wu">
      <author>中央日報</author>
      <author>中央通訊社董事長馬星野</author>
    </egXML>
  </exemplum>
  <remarks ident="author-remarks" versionDate="2009-03-18" xml:lang="en">
    <p>Particularly where cataloguing is likely to be based on the
    content of the header, it is advisable to use a generally recognized
    name authority file to supply the content for this element.  The
    attributes <att>key</att> or <att>ref</att> may also be used to
    reference canonical information about the author(s) intended from any
    appropriate authority, such as a library catalogue or online
    resource. </p>
    <p>In the case of a broadcast, use this element for the name of
    the company or network responsible for making the broadcast.</p>
    <p>Where an author is unknown or unspecified, this element may contain
    text such as <mentioned>Unknown</mentioned> or
    <mentioned>Anonymous</mentioned>. When the appropriate TEI modules are
    in use, it may also contain detailed tagging of the names used for people, organizations or
    places, in particular where  multiple names are given.</p>
  </remarks>
  <remarks ident="author-remarks" versionDate="2022-04-10" xml:lang="es">
    <p>En particular, cuando es probable que la catalogación se base en el contenido del encabezado, 
      se recomienda utilizar una autoridad bibliográfica de nombres generalmente reconocida para 
      proporcionar el contenido de este elemento. Los atributos <att>key</att> o <att>ref</att> 
      también se pueden usar para hacer referencia a información canónica sobre el/la autor/a o 
      autores procedente de cualquier autoridad apropiada, como un catálogo de biblioteca o un 
      recurso en línea. En el caso de una retransmisión, este elemento debe usarse para el nombre 
      de la empresa o cadena responsable de realizar dicha retransmisión. Cuando se desconoce o no 
      se especifica un/a autor/a, este elemento puede contener texto como <mentioned>Desconocido/a</mentioned> 
      o <mentioned>Anónimo</mentioned>. Cuando se utilizan los módulos TEI apropiados, también puede contener 
      etiquetas detalladas de los nombres utilizados para personas, organizaciones o lugares, en particular 
      cuando se proporcionan varios nombres.</p>
  </remarks>
  <remarks ident="author-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Il est conseillé d'utiliser des listes d'autorité reconnues
    pour trouver la forme exacte des noms de personnes, en particulier
    lorsque le catalogage repose sur le contenu de l'en-tête TEI. Les
    attributs <att>key</att> ou <att>ref</att> seront aussi employés
    pour donner une référence canonique documentant l'auteur concerné
    grâce à une autorité appropriée, comme le catalogue d'une
    bibliothèque ou une ressource en ligne. </p>
    <p>Dans le cas d'une émission, cet élément sert à encoder le nom de la société ou du
      réseau qui diffuse le programme.</p>
  </remarks>
  <remarks ident="author-remarks" versionDate="2023-08-30" xml:lang="ja">
  <p>特にヘッダの内容をもとに目録作成が行われると考えられる場合、この要素の内容を広く知られた名前典拠ファイルに準拠することを推奨する。
      <att>key</att>や<att>ref</att>属性によって何らかの適切な典拠（たとえば図書館目録やオンライン情報のような）における著者（達）についての標準的な参照情報を示すこともできる。</p>
      <p>放送番組の場合には、その番組の制作に責任を持つ放送局や放送ネットワークの名前を用いる。</p>
      <p>著者が不明であったり不明確である場合、この要素は<mentioned>不詳</mentioned>や<mentioned>匿名</mentioned>のようなテキストであってもよい。
      特に、複数の名前が用いられている場合には、適切なTEIモジュールを用いて、人や組織、場所に関する名前をより詳細にタグ付けしてもよい。</p>
  </remarks>
  <remarks ident="author-remarks" versionDate="2017-06-04" xml:lang="de">
    <p>Insbesondere wenn eine Katalogisierung auf Basis des TEI-Headers erfolgen soll, ist es ratsam
      einen Namen aus einer annerkannten Normdatei zu verwenden. Die Attribute <att>key</att> und
      <att>ref</att> können außerdem benutzt werden, um auf kanonische Informationen über
      einen Autor zu verweisen, etwa in einem Bibliothekskatalog oder einer Online-Ressource.</p>
    <p>Im Fall von Rundfunksendungen sollte dies Element benutzt werden, um den Namen der Firma oder
      der Sendergruppe zu notieren, welche diese Rundfunksendung verantwortet.</p>
    <p>Wo ein Autor unbekannt oder nicht angegeben ist, kann dieses Element Text wie z. B.
      <mentioned>Unbekannt</mentioned> oder <mentioned>Nicht angegeben</mentioned> beinhalten.
      Wenn die entsprechenden TEI-Module benutzt werden, kann das Element auch detaillierte
      Auszeichnungen für Namen von Personen, Organisationen oder Orten beinhalten - insbesondere
      wenn mehrere Namen vorhanden sind.</p>
  </remarks>
  <listRef>
    <ptr target="#COBICOR"/>
    <ptr target="#HD21"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss xml:lang="en" versionDate="2011-11-26">author</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss xml:lang="es" versionDate="2022-02-24">autor/a</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2011-11-26" xml:lang="fr">auteur</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2017-06-04" xml:lang="de">Autor</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-26" xml:lang="en">in a bibliographic reference, contains the name(s) of an author, personal or corporate, of a work; for example in the same form as that provided by a recognized bibliographic name authority.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참고문헌에 작가, 단독 저자, 공동 저자의 이름을 포함한다; 서지 항목의 책임에 관한 1차적 진술.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在書目參照中，包含一件作品的作者 (群) 姓名，無論是個人或是團體性質；這也是書目項目責任歸屬的主要陳述。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2023-08-30" xml:lang="ja">書誌参照において、作品の著者となる人や法人の名前を、たとえば、よく知られた書誌典拠情報機関の形式で提供されるものに合わせるなどして記述する。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">dans une référence bibliographique contient le nom de la (des) personne(s) physique(s) ou du collectif, auteur(s) d'une oeuvre ; par exemple dans la même forme que celle utilisée par une référence bibliographique reconnue.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2022-02-24" xml:lang="es">en una referencia bibliográfica, contiene el nombre del autor/a/es, ya sea una persona o una institución, de una obra; por ejemplo, en la misma forma que la proporcionada por una autoridad bibliográfica reconocida.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">in un riferimento bibliografico contiene il nome dell'autore (o degli autori), personale o collettivo, di un'opera; è la dichiarazione di responsabilità primaria di ciascuna unità bibliografica.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-04" xml:lang="de">enthält in einer bibliografischen Referenz den oder die Namen eines Autors eines Werks (oder einer für das Werk verantwortlichen Körperschaft); zum Beispiel in der Form, wie sie eine anerkannte bibliografische Instanz anbietet.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.naming"/>
    <memberOf key="model.respLike"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-author-egXML-lq" source="#COBICOR-eg-251">
      <author>British Broadcasting Corporation</author>
      <author>La Fayette, Marie Madeleine Pioche de la Vergne, comtesse de (1634–1693)</author>
      <author>Anonymous</author>
      <author>Bill and Melinda Gates Foundation</author>
      <author>
        <persName>Beaumont, Francis</persName>
        and
        <persName>John Fletcher</persName>
      </author>
      <author><orgName key="BBC">British Broadcasting
      Corporation</orgName>: Radio 3 Network</author>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-author-egXML-zl">
      <author>La Fayette, Marie Madeleine Pioche de la Vergne, comtesse de (1634–1693)</author>
      <author>Anonyme</author>
      <author>Erckmann-Chatrian</author>
      <author>
        <orgName key="ARTE">Association relative à la télévision européenne</orgName>
      </author>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-author-egXML-wu">
      <author>中央日報</author>
      <author>中央通訊社董事長馬星野</author>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="author-remarks" versionDate="2009-03-18" xml:lang="en">
    <p>Particularly where cataloguing is likely to be based on the
    content of the header, it is advisable to use a generally recognized
    name authority file to supply the content for this element.  The
    attributes <att>key</att> or <att>ref</att> may also be used to
    reference canonical information about the author(s) intended from any
    appropriate authority, such as a library catalogue or online
    resource. </p>
    <p>In the case of a broadcast, use this element for the name of
    the company or network responsible for making the broadcast.</p>
    <p>Where an author is unknown or unspecified, this element may contain
    text such as <mentioned>Unknown</mentioned> or
    <mentioned>Anonymous</mentioned>. When the appropriate TEI modules are
    in use, it may also contain detailed tagging of the names used for people, organizations or
    places, in particular where  multiple names are given.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="author-remarks" versionDate="2022-04-10" xml:lang="es">
    <p>En particular, cuando es probable que la catalogación se base en el contenido del encabezado, 
      se recomienda utilizar una autoridad bibliográfica de nombres generalmente reconocida para 
      proporcionar el contenido de este elemento. Los atributos <att>key</att> o <att>ref</att> 
      también se pueden usar para hacer referencia a información canónica sobre el/la autor/a o 
      autores procedente de cualquier autoridad apropiada, como un catálogo de biblioteca o un 
      recurso en línea. En el caso de una retransmisión, este elemento debe usarse para el nombre 
      de la empresa o cadena responsable de realizar dicha retransmisión. Cuando se desconoce o no 
      se especifica un/a autor/a, este elemento puede contener texto como <mentioned>Desconocido/a</mentioned> 
      o <mentioned>Anónimo</mentioned>. Cuando se utilizan los módulos TEI apropiados, también puede contener 
      etiquetas detalladas de los nombres utilizados para personas, organizaciones o lugares, en particular 
      cuando se proporcionan varios nombres.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="author-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Il est conseillé d'utiliser des listes d'autorité reconnues
    pour trouver la forme exacte des noms de personnes, en particulier
    lorsque le catalogage repose sur le contenu de l'en-tête TEI. Les
    attributs <att>key</att> ou <att>ref</att> seront aussi employés
    pour donner une référence canonique documentant l'auteur concerné
    grâce à une autorité appropriée, comme le catalogue d'une
    bibliothèque ou une ressource en ligne. </p>
    <p>Dans le cas d'une émission, cet élément sert à encoder le nom de la société ou du
      réseau qui diffuse le programme.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="author-remarks" versionDate="2023-08-30" xml:lang="ja">
  <p>特にヘッダの内容をもとに目録作成が行われると考えられる場合、この要素の内容を広く知られた名前典拠ファイルに準拠することを推奨する。
      <att>key</att>や<att>ref</att>属性によって何らかの適切な典拠（たとえば図書館目録やオンライン情報のような）における著者（達）についての標準的な参照情報を示すこともできる。</p>
      <p>放送番組の場合には、その番組の制作に責任を持つ放送局や放送ネットワークの名前を用いる。</p>
      <p>著者が不明であったり不明確である場合、この要素は<mentioned>不詳</mentioned>や<mentioned>匿名</mentioned>のようなテキストであってもよい。
      特に、複数の名前が用いられている場合には、適切なTEIモジュールを用いて、人や組織、場所に関する名前をより詳細にタグ付けしてもよい。</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="author-remarks" versionDate="2017-06-04" xml:lang="de">
    <p>Insbesondere wenn eine Katalogisierung auf Basis des TEI-Headers erfolgen soll, ist es ratsam
      einen Namen aus einer annerkannten Normdatei zu verwenden. Die Attribute <att>key</att> und
      <att>ref</att> können außerdem benutzt werden, um auf kanonische Informationen über
      einen Autor zu verweisen, etwa in einem Bibliothekskatalog oder einer Online-Ressource.</p>
    <p>Im Fall von Rundfunksendungen sollte dies Element benutzt werden, um den Namen der Firma oder
      der Sendergruppe zu notieren, welche diese Rundfunksendung verantwortet.</p>
    <p>Wo ein Autor unbekannt oder nicht angegeben ist, kann dieses Element Text wie z. B.
      <mentioned>Unbekannt</mentioned> oder <mentioned>Nicht angegeben</mentioned> beinhalten.
      Wenn die entsprechenden TEI-Module benutzt werden, kann das Element auch detaillierte
      Auszeichnungen für Namen von Personen, Organisationen oder Orten beinhalten - insbesondere
      wenn mehrere Namen vorhanden sind.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COBICOR"/>
    <ptr target="#HD21"/>
  </listRef>
```

^b23

