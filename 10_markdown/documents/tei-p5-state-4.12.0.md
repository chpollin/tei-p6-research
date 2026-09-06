---
type: representation
source-type: document
source: '[[00_sources/tei-p5-state-4.12.0.xml]]'
converter: tools.ingest_git_blobs v2; complete XML plus XML itertext English reading
  blocks with whitespace normalized and identified locators
channel: collection
metadata:
  title: TEI P5 4.12.0 state specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/state.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# state

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

Source byte length: 5895. Git blob: `b9e91d5cb159d59dfbd3ea9a6c08a9a395bc3f5b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-state" ident="state">
  <gloss versionDate="2009-03-19" xml:lang="en">state</gloss>
  <gloss versionDate="2009-03-19" xml:lang="fr">statut</gloss>
  <desc versionDate="2011-12-01" xml:lang="en">contains a description of some status or quality attributed to a person, place, or organization often at some specific time or for a specific date range.</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">contient la description d'un statut ou d'une qualité actuels attribués à une personne, un lieu ou une organisation.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인, 장소, 또는 조직에 관련한 현재 지위 또는 특성 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明分界方法所定義的權威參照標準裡其中ㄧ個組件。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">人物、場所、組織などの、現在の社会的状態や地位を示す。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">enthält eine Beschreibung eines Status oder einer Qualität, die einer Person, einem Ort oder einer Organisation oft zu einem bestimmten Zeitpunkt oder für einen bestimmten Zeitraum zugeordnet wird.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">especifica un componente de una referencia canónica definida por el método milestone (hito).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica un componente di un riferimento canonico definito dal metodo milestone.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.dimensions"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.orgStateLike"/>
    <memberOf key="model.persStateLike"/>
    <memberOf key="model.placeStateLike"/>
  </classes>
  <content>
    <sequence>
      <elementRef key="precision" minOccurs="0" maxOccurs="unbounded"/>
      <alternate>
        <elementRef key="state" minOccurs="1" maxOccurs="unbounded"/>
        <sequence>
          <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
          <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.noteLike"/>
            <classRef key="model.biblLike"/>
          </alternate>
        </sequence>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.labelLike"/>
          <classRef key="model.noteLike"/>
          <classRef key="model.biblLike"/>
        </alternate>
      </alternate>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-state-egXML-dc">
        <state ref="#SCHOL" type="status">
          <label>scholar</label>
        </state>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-state-egXML-ac">
      <org>
        <orgName notAfter="1960">The Silver Beetles</orgName>
        <orgName notBefore="1960">The Beatles</orgName>
        <state type="membership" from="1960-08" to="1962-05">
          <desc>
            <persName>John Lennon</persName>
            <persName>Paul McCartney</persName>
            <persName>George Harrison</persName>
            <persName>Stuart Sutcliffe</persName>
            <persName>Pete Best</persName>
          </desc>
        </state>
        <state type="membership" notBefore="1963">
          <desc>
            <persName>John Lennon</persName>
            <persName>Paul McCartney</persName>
            <persName>George Harrison</persName>
            <persName>Ringo Starr</persName>
          </desc>
        </state>
      </org>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-state-egXML-qg">
      <state cert="high" type="social" from="1987-01-01" to="1997-12-31">
        <label>Citoyenneté</label>
        <desc>Entre 1987 et 1997a bénéficié du statut de citoyen naturalisé du ROYAUME-UNI</desc>
      </state>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-state-egXML-fg">
        <state ref="#zh-tw_SCHOL" type="status">
          <label>學者</label>
        </state>
    </egXML>
  </exemplum>
  <remarks ident="state-remarks" versionDate="2011-12-01" xml:lang="en">
    <p>Where there is confusion between <gi>trait</gi> and <gi>state</gi> the more general purpose
      element <gi>state</gi> should be used even for unchanging characteristics. If you wish to
      distinguish between characteristics that are generally perceived to be time-bound states and
      those assumed to be fixed traits, then <gi>trait</gi> is available for the more static of
      these. The <gi>state</gi> element encodes characteristics which are sometimes assumed to
      change, often at specific times or over a date range, whereas the <gi>trait</gi> elements are
      used to record characteristics, such as eye-colour, which are less subject to change. Traits are typically, but not necessarily, 
      independent of the volition or action of the holder.</p>
  </remarks>
  <listRef>
    <ptr target="#NDPERSbp"/>
    <ptr target="#NDPERSEpc"/>
  </listRef>
</elementSpec>
```

## English reading blocks

### Reading 1

XML location: `/elementSpec[@ident='state']/desc[1]`.

contains a description of some status or quality attributed to a person, place, or organization often at some specific time or for a specific date range. ^r1

### Reading 2

XML location: `/elementSpec[@ident='state']/remarks[@ident='state-remarks']/p[1]`.

Where there is confusion between trait and state the more general purpose element state should be used even for unchanging characteristics. If you wish to distinguish between characteristics that are generally perceived to be time-bound states and those assumed to be fixed traits, then trait is available for the more static of these. The state element encodes characteristics which are sometimes assumed to change, often at specific times or over a date range, whereas the trait elements are used to record characteristics, such as eye-colour, which are less subject to change. Traits are typically, but not necessarily, independent of the volition or action of the holder. ^r2

