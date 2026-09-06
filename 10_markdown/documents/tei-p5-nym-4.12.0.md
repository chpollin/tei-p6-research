---
type: representation
source-type: document
source: '[[00_sources/tei-p5-nym-4.12.0.xml]]'
converter: tools.ingest_git_blobs v1; complete XML plus XML itertext English reading
  blocks with whitespace normalized
channel: collection
metadata:
  title: TEI P5 4.12.0 nym specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/nym.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# nym

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.

Source byte length: 4085. Git blob: `16a0f11f5fa5202048d2b93e204e60bd0e03530f`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-nym" ident="nym">
  <gloss versionDate="2007-07-04" xml:lang="en">canonical name</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">표준 이름</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">nombre canónico</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">nome canonico</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">nom canonique</gloss>
  <desc versionDate="2012-03-05" xml:lang="en">contains the definition for a canonical name or name component of any kind.</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient la définition de tout nom ou partie de nom dans leur forme canonique.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준 이름 또는 어떤 종류의 이름부 정의를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一標準名稱或任何部分名稱的定義。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">各種名前の、標準的な名前または名前の部分の定義を示す。</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene la definizione di un nome o di una parte di nome canonici di qualsiasi tipo.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene la definición para un nombre canónico o parte de nombre de cualquier tipo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <sequence>

          <elementRef key="idno" minOccurs="0" maxOccurs="unbounded"/>
          <classRef key="model.entryPart" minOccurs="0" maxOccurs="unbounded"/>
        
      
      
        
          <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
        
      
      
        
          <elementRef key="nym" minOccurs="0" maxOccurs="unbounded"/>
        
      
    </sequence>
  </content>
  <attList>
    <attDef ident="parts">
      <desc versionDate="2007-04-12" xml:lang="en">points to constituent nyms.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">구성성분 이름을 가리킨다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">連結到組成的正式名稱</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">構成別名を参照する。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">pointe vers des éléments constituants canoniques.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica nym costitutivi.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">señala un componente nyms.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nym-egXML-jc">
      <nym xml:id="J452">
        <form>
          <orth xml:lang="en-US">Ian</orth>
          <orth xml:lang="en-x-Scots">Iain</orth>
        </form>
      </nym>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nym-egXML-fn">
      <nym xml:id="fr_J452">
        <form>
          <orth xml:lang="en-US">Ian</orth>
          <orth xml:lang="en-x-Scots">lain</orth>
        </form>
      </nym>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-nym-egXML-rt">
      <nym xml:id="zh-tw_J452">
        <form>
          <orth xml:lang="zh-TW">歡</orth>
          <orth xml:lang="zh-CN">欢</orth>
        </form>
      </nym>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDNYM" type="div2"/>
  </listRef>
</elementSpec>
```

## English reading blocks

### Reading 1

XML location: `/elementSpec[1]/desc[1]`.

contains the definition for a canonical name or name component of any kind. ^r1

### Reading 2

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

points to constituent nyms. ^r2

