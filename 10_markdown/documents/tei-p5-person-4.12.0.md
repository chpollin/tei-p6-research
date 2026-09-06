---
type: representation
source-type: document
source: '[[00_sources/tei-p5-person-4.12.0.xml]]'
converter: tools.ingest_git_blobs v1; complete XML plus XML itertext English reading
  blocks with whitespace normalized
channel: collection
metadata:
  title: TEI P5 4.12.0 person specification
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/person.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-06'
updated: '2026-09-06'
---

# person

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The XML below is the complete source, preserved as inert text, including all languages,
examples, declarations, and processing instructions. A separator newline before the
closing fence is not part of the source. The converter records the exact byte length.
Reading blocks reproduce English descriptions and English remarks paragraphs using
XML `itertext`; whitespace runs become one space and surrounding whitespace is removed.
They are reading projections of this source, not additional sources or interpretations.

Source byte length: 13105. Git blob: `8aff4c8dd02eb6b8d5609f62eb9e6e03000fcd4d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-person" ident="person">
  <gloss versionDate="2008-12-09" xml:lang="en">person</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">personne</gloss>
  <desc versionDate="2005-12-14" xml:lang="en">provides information about an identifiable individual, for example a participant in a language interaction, or a person referred to in a
        historical source.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어 언어 상호작용의 참여자 또는 역사적 문헌에서 언급된 사람과 같이 식별가능한 개인에 관한 정보를 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供一個已知人物的相關資料，例如語言互動中的參與者、或是歷史來源中提及的人物。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">特定可能な個人の情報を示す。例えば、言語交流の参加者、歴史資料中で参 照される人物など。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">fournit des informations sur un individu identifiable, par exemple un participant à une interaction
        linguistique, ou une personne citée dans une source historique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona información relativa a un individuo específico, p.ej. un participante de una interacción
        verbal o una persona identificada por una fuente histórica.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce informazioni relative a un soggetto specifico, come i partecipanti a un'interazione verbale o le
        persone identificate da una fonte storica</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.personLike"/>
  </classes>
  <content>
    <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.personPart"/>
          <classRef key="model.global"/>
          <classRef key="model.ptrLike"/>
        </alternate>
    </alternate>
  </content>
  <attList>
    <attDef ident="role" usage="opt">
      <desc versionDate="2005-12-14" xml:lang="en">specifies a primary role or classification for the person.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사람에 대한 주요 역할 또는 분류를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該人物的主要角色或分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該人物の第一位の役割や分類を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise un rôle principal ou une classification principale pour cette personne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">establece el rol o la clasificación primaria de una persona.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">stabilisce il ruolo o la classificazione primaria di una persona.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
      <remarks ident="person-attr.role-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
	project, using arbitrary keywords such as <val>artist</val>,
	<val>employer</val>, <val>author</val>, <val>relative</val>, or
	<val>servant</val>, each of which should be associated with a
	definition. Such local definitions will typically be provided by a
	<gi>valList</gi> element in the project schema specification.</p></remarks>
    </attDef>
    <attDef ident="sex" usage="opt">
      <desc versionDate="2005-12-14" xml:lang="en">specifies the sex of the person.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사람의 성을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該人物的性別。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該人物の性別を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise le sexe de la personne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el sexo de una persona.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il sesso di una persona.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.sex"/></datatype>
      <remarks ident="person-attr.sex-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be defined locally by a project, or they may refer to an external standard.</p>
      </remarks>
    </attDef>
    <attDef ident="gender" usage="opt">
      <desc versionDate="2022-05-18" xml:lang="en">specifies the gender of the person.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
      <remarks ident="person-attr.gender-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be defined locally by a project, or they may refer to an external standard.</p>
      </remarks>
    </attDef>
    <attDef ident="age" usage="opt">
      <desc versionDate="2005-12-14" xml:lang="en">specifies an age group for the person.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사람의 연령군을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該人物所屬的年齡層。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該人物の年齢層を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise une tranche d'âge pour la personne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica un intervalo de edad para una persona.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la fascia di età di una persona.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <remarks ident="person-attr.age-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
	project, using arbitrary keywords such as <val>infant</val>,
	<val>child</val>, <val>teen</val>, <val>adult</val>, or
	<val>senior</val>, each of which should be associated with a
	definition. Such local definitions will typically be provided by a
	<gi>valList</gi> element in the project schema specification.</p></remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egXML-gr">
      <person sex="F" age="adult">
        <p>Female respondent, well-educated, born in Shropshire UK, 12 Jan 1950, of unknown occupation. Speaks French fluently. Socio-Economic
          status B2.</p>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egXML-il">
      <person sex="intersex" role="god" age="immortal">
        <persName>Hermaphroditos</persName>
        <persName xml:lang="grc">Ἑρμαφρόδιτος</persName>
      </person>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egXML-wh">
      <person sex="F" age="adult">
        <p>Personne interrogée, de sexe féminin, instruite, née à Shropshire, au ROYAUME-UNI le 12
            Janvier 1950, d'occupation inconnue. Parle le français couramment. Statut
            socio-économique B2.</p>
      </person>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egXML-xa">
      <person xml:id="fr_Ovi01" sex="M" role="poet">
        <persName xml:lang="en">Ovid</persName>
        <persName xml:lang="la">Publius Ovidius Naso</persName>
        <birth when="-0044-03-20"> 20 March 43 BC<placeName><settlement type="city">Sulmona</settlement><country key="IT">Italie</country></placeName>
            </birth>
        <death notBefore="0017" notAfter="0018">17 or 18 AD<placeName><settlement type="city">Tomis (Constanta)</settlement><country key="RO">Roumanie</country></placeName>
            </death>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egXML-pf">
      <person sex="F" age="adult">
        <p>女性被告。1950年1月12日生於西藏，受過良好教育，職業不明。能說流利漢語，中產階級。</p>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egXML-jr">
      <person xml:id="zh-tw_Ovi01" sex="M" role="poet">
        <persName xml:lang="en">Ovid</persName>
        <persName xml:lang="zh-TW">奧維德</persName>
        <birth when="-0044-03-20"> 西元前43年3月20日<placeName><settlement type="city">Sulmona</settlement><country key="IT">義大利</country></placeName>
            </birth>
        <death notBefore="0017" notAfter="0018">西元後17或18年<placeName><settlement type="city">Tomis (Constanta)</settlement><country key="RO">羅馬尼亞</country></placeName>
            </death>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egXML-ej">
      <person xml:id="Ovi01" sex="M" role="poet">
        <persName xml:lang="en">Ovid</persName>
        <persName xml:lang="la">Publius Ovidius Naso</persName>
        <birth when="-0044-03-20"> 20 March 43 BC <placeName><settlement type="city">Sulmona</settlement><country key="IT">Italy</country></placeName>
            </birth>
        <death notBefore="0017" notAfter="0018">17 or 18 AD <placeName><settlement type="city">Tomis (Constanta)</settlement><country key="RO">Romania</country></placeName>
            </death>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en" source="#vcard">
    <p>The following exemplifies an adaptation of the vCard standard to indicate an unknown gender for a fictional character.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egXML-np">
      <person xml:id="ariel" gender="U">
        <persName>Ariel</persName>
        <note>Character in <title level="m">The Tempest</title>.</note>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>This example demonstrates the use of a <gi>ref</gi> element to provide more information about a person.
    The private URI scheme <mentioned>lacy:</mentioned> is presumably
    declared in the <gi>teiHeader</gi> with a <gi>prefixDef</gi>.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-person-egxml-dr">
      <person age="G2" role="author" xml:id="W0212" sex="F">
        <birth when="1787"/>
        <death when="1855"/>
        <persName type="main">Mitford, Mary Russell (1787–1855)</persName>
        <persName resp="#Nicoll">MITFORD, MARY RUSSELL</persName>
        <listBibl type="lacyTitles">
          <desc>Lacy's Acting Editions</desc>
          <bibl><ref target="lacy:L1280">Foscari</ref></bibl>
          <bibl><ref target="lacy:L1337">Rienzi</ref></bibl>
        </listBibl>
        <listRef type="seeAlso">
          <ref target="https://www.victorianresearch.org/atcl/show_author.php?aid=1386">ATCL</ref>
          <ref target="https://doi.org/10.1093/ref:odnb/18859">ODNB</ref>
          <ref target="https://en.wikipedia.org/wiki/Mary_Russell_Mitford">Wikipedia</ref>
          <ref target="https://digitalmitford.org">Digital Mitford</ref>
        </listRef>
      </person>
    </egXML>
  </exemplum>
  <remarks ident="person-remarks" versionDate="2005-12-14" xml:lang="en">
    <p rend="dataDesc">May contain either a prose description organized as paragraphs, or a sequence of more specific demographic elements drawn
            from the <ident type="class">model.personPart</ident> class.</p>
  </remarks>
  <remarks ident="person-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc">Peut contenir soit une description en prose organisée en paragraphes, soit une suite d'éléments spécifiques relatifs à la
            démographie extraits de la classe <ident type="class">model.personPart</ident>.</p>
  </remarks>
  <remarks ident="person-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落による散文の解説、またはクラス <ident type="class">model.personPart</ident>にある一連の人口統計要 素を含むかもしれない。 </p>
  </remarks>
  <listRef>
    <ptr target="#NDPERSE"/>
    <ptr target="#CCAHPA"/>
  </listRef>
</elementSpec>
```

## English reading blocks

### Reading 1

XML location: `/elementSpec[1]/desc[1]`.

provides information about an identifiable individual, for example a participant in a language interaction, or a person referred to in a historical source. ^r1

### Reading 2

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

specifies a primary role or classification for the person. ^r2

### Reading 3

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]/p[1]`.

Values for this attribute may be locally defined by a project, using arbitrary keywords such as artist, employer, author, relative, or servant, each of which should be associated with a definition. Such local definitions will typically be provided by a valList element in the project schema specification. ^r3

### Reading 4

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

specifies the sex of the person. ^r4

### Reading 5

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]/p[1]`.

Values for this attribute may be defined locally by a project, or they may refer to an external standard. ^r5

### Reading 6

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

specifies the gender of the person. ^r6

### Reading 7

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]/p[1]`.

Values for this attribute may be defined locally by a project, or they may refer to an external standard. ^r7

### Reading 8

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

specifies an age group for the person. ^r8

### Reading 9

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[1]/p[1]`.

Values for this attribute may be locally defined by a project, using arbitrary keywords such as infant, child, teen, adult, or senior, each of which should be associated with a definition. Such local definitions will typically be provided by a valList element in the project schema specification. ^r9

### Reading 10

XML location: `/elementSpec[1]/remarks[1]/p[1]`.

May contain either a prose description organized as paragraphs, or a sequence of more specific demographic elements drawn from the model.personPart class. ^r10

