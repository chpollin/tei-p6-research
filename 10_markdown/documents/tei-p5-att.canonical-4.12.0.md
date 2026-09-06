---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.canonical-4.12.0.xml]]'
converter: tools.ingest_git_blobs v1; complete XML plus XML itertext English reading
  blocks with whitespace normalized
channel: collection
metadata:
  title: TEI P5 4.12.0 att.canonical specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.canonical.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# att.canonical

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.

Source byte length: 9162. Git blob: `2682bdddfa0d9223aeffd45566b825f895b050c5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-canonical" ident="att.canonical">
  <desc versionDate="2008-09-05" xml:lang="en">provides attributes that can be used to associate a representation such as a name or title
    with canonical information about the object being named or referenced.</desc>
  <desc versionDate="2009-05-25" xml:lang="fr">fournit des attributs qui peuvent être utilisés pour
    associer une représentation telle qu'un nom ou un titre à l'information canonique concernant
    l'objet nommé ou auquel il est fait référence.</desc>
  <desc versionDate="2018-12-31" xml:lang="ja">名前やタイトルのような表現を参照対象についての典拠情報と関連付けるのに利用する属性を提供する。</desc>
  <attList>
    <attDef ident="key" usage="opt">
      <desc versionDate="2008-09-05" xml:lang="en">provides an externally-defined means of identifying the entity (or entities) being
        named, using a coded value of some kind.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">fournit un moyen, défini de façon externe,
        d'identifier l'entité (ou les entités) nommé(es), en utilisant une valeur codée
        d'un certain type.</desc>
      <desc versionDate="2018-12-31" xml:lang="ja">何らかのコード化された値を用いて、名付けられたエンティティを識別する外部的に定義された手段を提供する。</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-canonical-egXML-iv" xml:lang="fr" source="#NONE">
          <author>
            <name key="Hugo, Victor (1802-1885)" ref="http://www.idref.fr/026927608">Victor Hugo</name>
          </author>
        </egXML>
      </exemplum>
      <remarks ident="att.canonical-attr.key-remarks" versionDate="2022-12-21" xml:lang="en">
        <p>The value may be a unique identifier from a database, or any other externally-defined
          string identifying the referent. 
          No particular syntax is proposed for the values of the <att>key</att> attribute, since 
          its form will depend entirely on practice within a given project.</p>
      </remarks>
      <remarks ident="att.canonical-attr.key-remarks" versionDate="2009-05-25" xml:lang="fr">
        <p>La valeur peut être un identifiant unique dans une base de données, ou toute autre chaîne
          définie de façon externe identifiant le référent. </p>
      </remarks>
      <remarks ident="att.canonical-attr.key-remarks" versionDate="2018-12-31" xml:lang="ja"><p>値はデータベースにおけるユニークな識別子や、外部で定義された指示対象を特定するなんらかの文字列であってよい。<att>key</att>属性の値に関してさだまった構文は提案されていない。なぜならば、それぞれのプロジェクトのやりかたに完全に依存するからである。同様の理由によって、データの相互交換においてこの属性は推奨されない。在るプロジェクトで用いられた値が他のプロジェクトの値と異なることを保証できないからである。そのような場面における魔法石的対処は、<ref target="#RFC4151">RFC4151</ref>に定義されるタグURIを値とする<att>ref</att>属性を用いて、標準的なウェブにおける習慣にしたがってmagic tokenを使うことである。</p></remarks>
    </attDef>
    <attDef ident="ref" usage="opt">
      <gloss versionDate="2008-09-05" xml:lang="en">reference</gloss>
      <gloss versionDate="2009-05-25" xml:lang="fr">référence</gloss>
      <gloss versionDate="2018-12-31" xml:lang="ja">参照</gloss>
      <desc versionDate="2008-09-05" xml:lang="en">provides an explicit means of locating a full definition or identity for the entity being named by
        means of one or more URIs.</desc>
      <desc versionDate="2009-05-25" xml:lang="fr">fournit un moyen explicite de localiser une
        définition complète de l'entité nommée au moyen d'un ou plusieurs URIs.</desc>
      <desc versionDate="2018-12-31" xml:lang="ja">一つ以上のURIを用いて、名付けられたエンティティの完全な定義かIDを参照するための明確な手段を提供する。</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-canonical-egXML-te" xml:lang="en" source="#NONE">
          <name ref="http://viaf.org/viaf/109557338" type="person">Seamus Heaney</name>
        </egXML>
      </exemplum>   
      <remarks ident="att.canonical-attr.ref-remarks" versionDate="2014-01-09" xml:lang="en">
<p>The value must point directly to one or more XML elements or other resources by means of one or more URIs, separated by whitespace. If more than one is supplied the implication is that the name identifies several distinct entities.</p>
      </remarks>
      <remarks ident="att.canonical-attr.ref-remarks" versionDate="2009-05-25" xml:lang="fr">
        <p>La valeur doit pointer directement vers un ou plusieurs éléments XML au moyen d'un ou plusieurs URIs, séparés par un espace. Si plus d'un URI est fourni, cela implique que le nom identifie plusieurs entités distinctes.</p>
      </remarks>
      <remarks ident="att.canonical-attr.ref-remarks" versionDate="2018-12-31" xml:lang="ja"><p>値は1つまたは複数のXML要素あるいは、空白によって区切られた1つまたは複数のURIを指し示すものでなければならない。1つ以上の値が与えられているときは、その名前が複数の異るエンティティに対応することを示唆する。</p></remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <p>In this contrived example, a canonical reference to the same
    organisation is provided in four different ways.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-canonical-egXML-ef" xml:lang="en" source="#NZPaV01NgaK">
      <author n="1">
        <name ref="http://nzetc.victoria.ac.nz/tm/scholarly/name-427308.html" type="organisation">New Zealand Parliament, Legislative Council</name>
      </author>
       
      <author n="2">
        <name ref="nzvn:427308" type="organisation">New Zealand Parliament, Legislative Council</name>
      </author>
          
      <author n="3">
        <name ref="./named_entities.xml#o427308" type="organisation">New Zealand Parliament, Legislative Council</name>
      </author>
       
      <author n="4">
        <name key="name-427308" type="organisation">New Zealand Parliament, Legislative Council</name>
      </author>
    </egXML>
    <p>The first presumes the availability of an internet connection
    and a processor that can resolve a URI (most can). The second
    requires, in addition, a <gi>prefixDef</gi> that declares how the
    <code>nzvm</code> prefix should be interpreted. The third does not
    require an internet connection, but does require that a file named
    <name type="file">named_entities.xml</name> be in the same
    directory as the TEI document. The fourth requires that an entire
    external system for key resolution be available.</p>
  </exemplum>
  <remarks ident="att.canonical-remarks" versionDate="2022-12-21" xml:lang="en">
    <!-- For the same reason, this attribute is not recommended in
         data interchange, since there is no way of ensuring that the
         values used by one project are distinct from those used by
         another. In such a situation, a preferable approach for magic
         tokens which follows standard practice on the Web is to use a
         <att>ref</att> attribute whose value is a tag URI as defined
         in <ref target="#RFC4151">RFC 4151</ref>. -->
    <p>The <att>key</att> attribute is more flexible and
    general-purpose, but its use in interchange requires that
    documentation about how the key is to be resolved be sent to the
    recipient of the TEI document. In contrast values of the
    <att>ref</att> attribute are resolved using the widely accepted
    protocols for a URI, and thus less documentation, if any, is
    likely required by the recipient in data interchange.</p>
    <p>These guidelines provide no semantic basis or suggested
    precedence when both <att>key</att> and <att>ref</att> are
    provided. For this reason simultaneous use of both is not
    recommended unless documentation explaining the use is provided,
    probably in an ODD customization, for interchange.</p>
  </remarks>
  <listRef>
    <ptr target="#NDATTSnr"/>
  </listRef>
</classSpec>
```

## English reading blocks

### Reading 1

XML location: `/classSpec[1]/desc[1]`.

provides attributes that can be used to associate a representation such as a name or title with canonical information about the object being named or referenced. ^r1

### Reading 2

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

provides an externally-defined means of identifying the entity (or entities) being named, using a coded value of some kind. ^r2

### Reading 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]/p[1]`.

The value may be a unique identifier from a database, or any other externally-defined string identifying the referent. No particular syntax is proposed for the values of the key attribute, since its form will depend entirely on practice within a given project. ^r3

### Reading 4

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

provides an explicit means of locating a full definition or identity for the entity being named by means of one or more URIs. ^r4

### Reading 5

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]/p[1]`.

The value must point directly to one or more XML elements or other resources by means of one or more URIs, separated by whitespace. If more than one is supplied the implication is that the name identifies several distinct entities. ^r5

### Reading 6

XML location: `/classSpec[1]/remarks[1]/p[1]`.

The key attribute is more flexible and general-purpose, but its use in interchange requires that documentation about how the key is to be resolved be sent to the recipient of the TEI document. In contrast values of the ref attribute are resolved using the widely accepted protocols for a URI, and thus less documentation, if any, is likely required by the recipient in data interchange. ^r6

### Reading 7

XML location: `/classSpec[1]/remarks[1]/p[2]`.

These guidelines provide no semantic basis or suggested precedence when both key and ref are provided. For this reason simultaneous use of both is not recommended unless documentation explaining the use is provided, probably in an ODD customization, for interchange. ^r7

