---
type: representation
source-type: document
source: '[[00_sources/tei-p5-affiliation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 affiliation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/affiliation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# affiliation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6141. Git blob: `70d5dc8b4c32d21a1f5efc5b1856ff37e65fda62`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-affiliation" ident="affiliation">
  <gloss versionDate="2008-12-09" xml:lang="en">affiliation</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">affiliation</gloss>
  <gloss versionDate="2024-04-11" xml:lang="de">Affiliation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an informal description of a person's present or past affiliation with some organization, for example an employer or sponsor.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">고용주 또는 후원자와 같이 개인의 현재 또는 과거 소속 조직에 대한 비공식적 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含非正式性的描述，關於個人現在或過去隸屬的團體，例如雇主或贊助者。</desc>
  <desc versionDate="2022-06-07" xml:lang="ja">人物が所属している、またはしていた団体に関する情報を示す。例えば、雇い主や出資者など。</desc>
  <desc versionDate="2008-12-09" xml:lang="fr">contient une description non formalisée portant sur l'affiliation présente ou passée d'une personne à une organisation, par exemple un employeur ou un sponsor.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción informal de la afiliación presente o pasada de una persona a una determinada organización, p.ej. un empleado o un patrocinador.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione informale dell'appartenenza presente o passata di una persona a una determinata organizzazione, per esempio un'azienda o un ente finanziatore.</desc>
  <desc versionDate="2024-04-11" xml:lang="de">enthält eine informelle Beschreibung der gegenwärtigen oder früheren Zugehörigkeit einer Person zu einer Organisation, z. B. eines Arbeitgebers oder Sponsors.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.addressLike"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
        <valItem ident="sponsor"/>
        <valItem ident="recommend"/>
        <valItem ident="discredit"/>
        <valItem ident="pledged"/>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-zq" source="#NONE">
      <affiliation>Junior project officer for the US <name type="org">National Endowment for
                    the Humanities</name>
            </affiliation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2018-10-30" xml:lang="en">
    <p>This example indicates that the person was affiliated with the
    Australian Journalists Association at some point between the dates
    listed.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-fa" source="#NONE">
      <affiliation notAfter="1960-01-01" notBefore="1957-02-28">Paid up member of the
                    <orgName>Australian Journalists Association</orgName>
            </affiliation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2018-10-30" xml:lang="en">
    <p>This example indicates that the person was affiliated with Mount Holyoke College throughout the entire span of the date range listed.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-pu" source="#NONE">
      <affiliation from="1902-01-01" to="1906-01-01">Was an assistant professor at Mount Holyoke College.</affiliation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-mo" source="#NONE">
      <affiliation>associé étranger de <name type="org">l'Académie des Inscriptions et
            Belles-Lettres</name>
        </affiliation>
      <affiliation notAfter="1960-01-01" notBefore="1957-02-28">Chargé de cours, puis professeur
          d’archéologie (1949-1981) et doyen (1958-1961) <orgName>à la Faculté des lettres
          d’Ankara</orgName>.</affiliation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-jl" source="#NONE">
      <affiliation><name type="org">國際獅子會</name>台灣區理監事
      </affiliation>
      <affiliation notAfter="1960-01-01" notBefore="1957-02-28"><orgName>澳洲記者協會</orgName>的付費會員</affiliation>
    </egXML>
  </exemplum>
  <remarks ident="affiliation-remarks" versionDate="2005-12-14" xml:lang="en">
    <p>If included, the name of an organization may be tagged using either the <gi>name</gi>
            element as above, or the more specific <gi>orgName</gi> element.</p>
  </remarks>
  <remarks ident="affiliation-remarks" versionDate="2009-05-29" xml:lang="fr">
    <p>S'il est présent, le nom d'une organisation peut être balisé en utilisant soit l'élément
            <gi>name</gi> comme ci-dessus, soit l'élément plus spécifique
        <gi>orgName</gi>.</p>
  </remarks>
  <remarks ident="affiliation-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 組織名は、要素<gi>name</gi>または、より特化した要素 <gi>orgName</gi>でマークアップした方がよい。 </p>
  </remarks>
  <listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="en">affiliation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">affiliation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2024-04-11" xml:lang="de">Affiliation</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an informal description of a person's present or past affiliation with some organization, for example an employer or sponsor.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">고용주 또는 후원자와 같이 개인의 현재 또는 과거 소속 조직에 대한 비공식적 기술을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含非正式性的描述，關於個人現在或過去隸屬的團體，例如雇主或贊助者。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-06-07" xml:lang="ja">人物が所属している、またはしていた団体に関する情報を示す。例えば、雇い主や出資者など。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">contient une description non formalisée portant sur l'affiliation présente ou passée d'une personne à une organisation, par exemple un employeur ou un sponsor.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción informal de la afiliación presente o pasada de una persona a una determinada organización, p.ej. un empleado o un patrocinador.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione informale dell'appartenenza presente o passata di una persona a una determinata organizzazione, per esempio un'azienda o un ente finanziatore.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2024-04-11" xml:lang="de">enthält eine informelle Beschreibung der gegenwärtigen oder früheren Zugehörigkeit einer Person zu einer Organisation, z. B. eines Arbeitgebers oder Sponsors.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.naming"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.addressLike"/>
    <memberOf key="model.persStateLike"/>
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

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="sponsor"/>
        <valItem ident="recommend"/>
        <valItem ident="discredit"/>
        <valItem ident="pledged"/>
      </valList>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-zq" source="#NONE">
      <affiliation>Junior project officer for the US <name type="org">National Endowment for
                    the Humanities</name>
            </affiliation>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2018-10-30" xml:lang="en">
    <p>This example indicates that the person was affiliated with the
    Australian Journalists Association at some point between the dates
    listed.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-fa" source="#NONE">
      <affiliation notAfter="1960-01-01" notBefore="1957-02-28">Paid up member of the
                    <orgName>Australian Journalists Association</orgName>
            </affiliation>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2018-10-30" xml:lang="en">
    <p>This example indicates that the person was affiliated with Mount Holyoke College throughout the entire span of the date range listed.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-pu" source="#NONE">
      <affiliation from="1902-01-01" to="1906-01-01">Was an assistant professor at Mount Holyoke College.</affiliation>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-mo" source="#NONE">
      <affiliation>associé étranger de <name type="org">l'Académie des Inscriptions et
            Belles-Lettres</name>
        </affiliation>
      <affiliation notAfter="1960-01-01" notBefore="1957-02-28">Chargé de cours, puis professeur
          d’archéologie (1949-1981) et doyen (1958-1961) <orgName>à la Faculté des lettres
          d’Ankara</orgName>.</affiliation>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-affiliation-egXML-jl" source="#NONE">
      <affiliation><name type="org">國際獅子會</name>台灣區理監事
      </affiliation>
      <affiliation notAfter="1960-01-01" notBefore="1957-02-28"><orgName>澳洲記者協會</orgName>的付費會員</affiliation>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="affiliation-remarks" versionDate="2005-12-14" xml:lang="en">
    <p>If included, the name of an organization may be tagged using either the <gi>name</gi>
            element as above, or the more specific <gi>orgName</gi> element.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="affiliation-remarks" versionDate="2009-05-29" xml:lang="fr">
    <p>S'il est présent, le nom d'une organisation peut être balisé en utilisant soit l'élément
            <gi>name</gi> comme ci-dessus, soit l'élément plus spécifique
        <gi>orgName</gi>.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="affiliation-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 組織名は、要素<gi>name</gi>または、より特化した要素 <gi>orgName</gi>でマークアップした方がよい。 </p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b24

