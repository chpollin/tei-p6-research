---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.naming-4.12.0.xml]]'
converter: tools.ingest_git_blobs v1; complete XML plus XML itertext English reading
  blocks with whitespace normalized
channel: collection
metadata:
  title: TEI P5 4.12.0 att.naming specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.naming.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# att.naming

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.

Source byte length: 5936. Git blob: `43887df614b32c49625a2fabfd7ecb4e6521c8ad`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" xml:id="NAMES" type="atts" ident="att.naming">
  <desc versionDate="2006-01-05" xml:lang="en">provides attributes common to elements which refer to named persons, places, organizations etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사람, 장소, 조직 등의 이름을 지시하는 요소에 공통적 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供屬性，通用於參照到人物、地點、組織等的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">名前、人物、場所、組織を示す要素に付与される属性を示す。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">fournit des attributs communs aux éléments qui font référence à des personnes, lieux, organismes, etc., nommés.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">identifica los atributos comunes a los elementos que se refieren a personas, lugares, organizaciones, etc. indicados por nombre</desc>
  <desc versionDate="2007-01-21" xml:lang="it">identifica degli attributi comuni a elementi che si riferiscono a persone, luoghi, organizzazioni, ecc. indicati per nome.</desc>
  <classes>
    
    <memberOf key="att.canonical"/>
  </classes>
  <attList>
    <attDef ident="role" usage="opt">
      <desc versionDate="2009-10-12" xml:lang="en">may be used to specify further information about the entity referenced by
this name in the form of a set of whitespace-separated values, for example the occupation of a person, or the status of a place.</desc>
      <desc versionDate="2022-08-26" xml:lang="ja">この属性名によって参照されるエンティティに関する詳細な情報（例えば人物の職業や場所のステータスなど）を示すために用いられる。この値は空白文字で区切られる。</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
    <attDef ident="nymRef" usage="opt">
      <gloss versionDate="2007-07-02" xml:lang="en">reference to the canonical name</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">표준 이름에 대한 참조</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">referencia al nombre canónico</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">référence au nom canonique</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">riferimento al nome canonico</gloss>
      <gloss versionDate="2022-08-26" xml:lang="ja">基準化された名前への参照</gloss>
      <desc versionDate="2007-05-22" xml:lang="en">provides a means of locating the canonical form
      (<term>nym</term>) of the names associated with the object
       named by
      the element bearing it.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">URI를 포함하는 요소에 의해 명명된 대상과 연관된 이름의 표준형식 (<term>nym</term>)의 위치를 가리키는 방법을 제공한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">proporciona los medios para localizar la forma canónica (<term>nym</term>) de los nombres asociados al objeto nombrado por el elemento que lo contiene.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該要素で名前が付与されている対象に関連する基準形(<term>nym</term>)と紐付ける。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">indique comment localiser la forme canonique
            (<term>nym</term>) des noms qui sont associés à l'objet nommé par l'élément qui le contient.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica un modo di localizzare la forma canonica (nym) dei nomi associati all'oggetto definito dall'elemento che lo contiene.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
      <remarks ident="att.naming-attr.nymRef-remarks" versionDate="2008-02-02" xml:lang="en">
        <p>The value must point directly to one or more XML elements
        by means of one or more URIs, separated by whitespace. If more
        than one is supplied, the implication is that the name
        is associated with  several distinct canonical names.</p>
      </remarks>
      <remarks ident="att.naming-attr.nymRef-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur doit pointer directement vers un ou plusieurs
        éléments XML au moyen d'un ou plusieurs URIs, séparés par un
        espace blanc. Si plus d'un URI est fourni, alors le nom est
        associé à plusieurs noms canoniques distincts.</p>
      </remarks>
      <remarks ident="att.naming-attr.nymRef-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>El valor debe señalar directamente a uno o más elementos XML mediante uno o más URIs, separado por espacios en blanco.
        Si se suministra más de uno, la implicación es que el nombre está asociado a varios nombres canónicos distintos. </p>
      </remarks>
      <remarks ident="att.naming-attr.nymRef-remarks" versionDate="2022-08-26" xml:lang="ja">
        <p>
当該属性値は、ひとつ以上のXML要素を直接指示する、空白文字で区切られたひとつ以上のURIでなくてはならない。複数与えられている場合は、その名前がいくつかの異なる基準形に対応していることを示唆する。
        </p>
      </remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#CONARS"/>
    <ptr target="#NDNYM"/>
  </listRef>
</classSpec>
```

## English reading blocks

### Reading 1

XML location: `/classSpec[1]/desc[1]`.

provides attributes common to elements which refer to named persons, places, organizations etc. ^r1

### Reading 2

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

may be used to specify further information about the entity referenced by this name in the form of a set of whitespace-separated values, for example the occupation of a person, or the status of a place. ^r2

### Reading 3

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

provides a means of locating the canonical form (nym) of the names associated with the object named by the element bearing it. ^r3

### Reading 4

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]/p[1]`.

The value must point directly to one or more XML elements by means of one or more URIs, separated by whitespace. If more than one is supplied, the implication is that the name is associated with several distinct canonical names. ^r4

