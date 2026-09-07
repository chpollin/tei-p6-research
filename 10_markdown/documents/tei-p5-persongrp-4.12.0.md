---
type: representation
source-type: document
source: '[[00_sources/tei-p5-persongrp-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 personGrp
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/personGrp.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# personGrp

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9693. Git blob: `0d78ab66f9453725c04e528b161a537f7c9df931`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="namesdates" xml:id="gi-personGrp" ident="personGrp">
  <gloss versionDate="2005-01-14" xml:lang="en">personal group</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">개인군</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">人物團體</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">groupe de personnes</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">grupo de personas</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gruppo di persone</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes a group of individuals treated as a single person for analytic purposes.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">분석적 목적을 위해 하나의 개인으로 처리된 개인군을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述一個為分析目的而被視為單一個人的團體。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">分析上、ひとりの人物として扱われる、個人のグループを示す。</desc>
  <desc versionDate="2009-03-19" xml:lang="fr">décrit un groupe d'individus traité comme une personne unique à des fins d'analyse.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe a un grupo de individuos considerados como una única persona para fines analíticos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive un gruppo di soggetti considerati come unica persona a fini analitici.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.personLike"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.personPart"/>
        <classRef key="model.global"/>
      </alternate>
    </alternate>
  </content>
  <attList>
    <attDef ident="role" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the role of this group of participants in the interaction.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">상호작용에서 참여자군의 역할을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該團體在互動中所扮演的角色。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">交流の参加者から成る当該グループの役割を示す。</desc>
      <desc versionDate="2008-12-09" xml:lang="fr">précise le rôle joué par ce groupe de personnes dans l'interaction.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el role de ese grupo de participantes en la interacción.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il ruolo del gruppo di partecipanti all'interazione.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
      <remarks ident="personGrp-attr.role-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
        project, using arbitrary keywords such as <val>movement</val>,
        <val>employers</val>, <val>relatives</val>, or
        <val>servants</val>, each of which should be associated with a
        definition. Such local definitions will typically be provided by a
        <gi>valList</gi> element in the project schema specification.</p></remarks>
    </attDef>
    <attDef ident="sex" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the sex of the participant group.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">참여자군의 성을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該參與團體的性別。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">参加者グループの性別を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise le sexe du groupe participant.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el sexo del grupo de participantes.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il sesso del gruppo di partecipanti.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.sex"/></datatype>
      <remarks ident="personGrp-attr.sex-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be defined locally by a project, or they may refer to an external standard.</p>
      </remarks>
    </attDef>
    <attDef ident="gender" usage="opt">
      <desc versionDate="2022-05-18" xml:lang="en">specifies the gender of the participant group.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
      <remarks ident="personGrp-attr.gender-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be defined locally by a project, or they may refer to an external standard.</p>
      </remarks>
    </attDef>
    <attDef ident="age" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the age group of the participants.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">참여자의 연령군을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該參與者所屬的年齡層。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該参加者の年齢層を示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise la tranche d'âge des participants.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el intervalo de edad del grupo de partecipantes.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la fascia di età del gruppo di partecipanti.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <remarks ident="personGrp-attr.age-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
        project, using arbitrary keywords such as <val>infant</val>,
        <val>child</val>, <val>teen</val>, <val>adult</val>, or
        <val>senior</val>, each of which should be associated with a
        definition. Such local definitions will typically be provided by a
        <gi>valList</gi> element in the project schema specification.</p></remarks>
    </attDef>
    <attDef ident="size" usage="opt">
      <desc versionDate="2013-12-21" xml:lang="en">describes
      informally the size or approximate size of the group for example
      by means of a number and an indication of accuracy e.g. <val>approx 200</val>.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">해당 그룹의 크기 또는 대략적 크기를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">提供該團體的 (約略) 大小。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該グループのおよその大きさを示す。</desc>
      <desc versionDate="2009-03-19" xml:lang="fr">précise la taille exacte ou approximative du groupe.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la dimensión o dimensiones aproximadas del grupo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica le dimensioni (anche approssimative) del gruppo.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-personGrp-egXML-xm" source="#UND">
      <personGrp xml:id="pg1" role="audience" sex="mixed" size="approx 50"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-personGrp-egXML-cv" source="#UND">
      <personGrp xml:id="fr_pg1" role="audience" sex="mixed" age="teen" size="approx 50"/>
    </egXML>
  </exemplum>
  <remarks ident="personGrp-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain a prose description organized as paragraphs, or any sequence of demographic elements in any combination.</p>
    <p>The global <att>xml:id</att> attribute should be used to identify each speaking participant in a spoken text if the <att>who</att>
            attribute is specified on individual utterances.</p>
  </remarks>
  <remarks ident="personGrp-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une description en texte libre organisée en paragraphes, ou une suite quelconque d'éléments relatifs à la
            démographie.</p>
    <p>Il faut utiliser l'attribut global <att>xml:id</att> pour identifier chaque locuteur dans une transcription de paroles si l'attribut
                <att>who</att> est présent pour chaque prise de parole. </p>
  </remarks>
  <remarks ident="personGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落から成る散文の解説、または一連の人口統計要素を含むかもしれない。 </p>
    <p> 個々の発話に属性<att>who</att>が付与されている場合、グローバル属性 <att>xml:id</att>は、発話テキスト中の発話者を特定するために使われる べきである。 </p>
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
<gloss versionDate="2005-01-14" xml:lang="en">personal group</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">개인군</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">人物團體</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">groupe de personnes</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">grupo de personas</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gruppo di persone</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes a group of individuals treated as a single person for analytic purposes.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">분석적 목적을 위해 하나의 개인으로 처리된 개인군을 기술한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述一個為分析目的而被視為單一個人的團體。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">分析上、ひとりの人物として扱われる、個人のグループを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">décrit un groupe d'individus traité comme une personne unique à des fins d'analyse.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe a un grupo de individuos considerados como una única persona para fines analíticos.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive un gruppo di soggetti considerati come unica persona a fini analitici.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.personLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.personPart"/>
        <classRef key="model.global"/>
      </alternate>
    </alternate>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the role of this group of participants in the interaction.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">상호작용에서 참여자군의 역할을 명시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該團體在互動中所扮演的角色。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">交流の参加者から成る当該グループの役割を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-12-09" xml:lang="fr">précise le rôle joué par ce groupe de personnes dans l'interaction.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el role de ese grupo de participantes en la interacción.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il ruolo del gruppo di partecipanti all'interazione.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="personGrp-attr.role-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
        project, using arbitrary keywords such as <val>movement</val>,
        <val>employers</val>, <val>relatives</val>, or
        <val>servants</val>, each of which should be associated with a
        definition. Such local definitions will typically be provided by a
        <gi>valList</gi> element in the project schema specification.</p></remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the sex of the participant group.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참여자군의 성을 명시한다.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該參與團體的性別。</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">参加者グループの性別を示す。</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">précise le sexe du groupe participant.</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el sexo del grupo de participantes.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il sesso del gruppo di partecipanti.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.sex"/></datatype>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="personGrp-attr.sex-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be defined locally by a project, or they may refer to an external standard.</p>
      </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2022-05-18" xml:lang="en">specifies the gender of the participant group.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded"><dataRef key="teidata.gender"/></datatype>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="personGrp-attr.gender-remarks" versionDate="2022-08-27" xml:lang="en">
        <p>Values for this attribute may be defined locally by a project, or they may refer to an external standard.</p>
      </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the age group of the participants.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참여자의 연령군을 명시한다.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該參與者所屬的年齡層。</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該参加者の年齢層を示す。</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">précise la tranche d'âge des participants.</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el intervalo de edad del grupo de partecipantes.</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la fascia di età del gruppo di partecipanti.</desc>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[4]/remarks[1]`.

```xml
<remarks ident="personGrp-attr.age-remarks" versionDate="2013-12-21" xml:lang="en">
        <p>Values for this attribute may be locally defined by a
        project, using arbitrary keywords such as <val>infant</val>,
        <val>child</val>, <val>teen</val>, <val>adult</val>, or
        <val>senior</val>, each of which should be associated with a
        definition. Such local definitions will typically be provided by a
        <gi>valList</gi> element in the project schema specification.</p></remarks>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[1]`.

```xml
<desc versionDate="2013-12-21" xml:lang="en">describes
      informally the size or approximate size of the group for example
      by means of a number and an indication of accuracy e.g. <val>approx 200</val>.</desc>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">해당 그룹의 크기 또는 대략적 크기를 명시한다.</desc>
```

^b47

### Block 48

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供該團體的 (約略) 大小。</desc>
```

^b48

### Block 49

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該グループのおよその大きさを示す。</desc>
```

^b49

### Block 50

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[5]`.

```xml
<desc versionDate="2009-03-19" xml:lang="fr">précise la taille exacte ou approximative du groupe.</desc>
```

^b50

### Block 51

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la dimensión o dimensiones aproximadas del grupo.</desc>
```

^b51

### Block 52

XML location: `/elementSpec[1]/attList[1]/attDef[5]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica le dimensioni (anche approssimative) del gruppo.</desc>
```

^b52

### Block 53

XML location: `/elementSpec[1]/attList[1]/attDef[5]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b53

### Block 54

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-personGrp-egXML-xm" source="#UND">
      <personGrp xml:id="pg1" role="audience" sex="mixed" size="approx 50"/>
    </egXML>
  </exemplum>
```

^b54

### Block 55

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-personGrp-egXML-cv" source="#UND">
      <personGrp xml:id="fr_pg1" role="audience" sex="mixed" age="teen" size="approx 50"/>
    </egXML>
  </exemplum>
```

^b55

### Block 56

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="personGrp-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain a prose description organized as paragraphs, or any sequence of demographic elements in any combination.</p>
    <p>The global <att>xml:id</att> attribute should be used to identify each speaking participant in a spoken text if the <att>who</att>
            attribute is specified on individual utterances.</p>
  </remarks>
```

^b56

### Block 57

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="personGrp-remarks" versionDate="2008-12-09" xml:lang="fr">
    <p rend="dataDesc">Peut contenir une description en texte libre organisée en paragraphes, ou une suite quelconque d'éléments relatifs à la
            démographie.</p>
    <p>Il faut utiliser l'attribut global <att>xml:id</att> pour identifier chaque locuteur dans une transcription de paroles si l'attribut
                <att>who</att> est présent pour chaque prise de parole. </p>
  </remarks>
```

^b57

### Block 58

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="personGrp-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 段落から成る散文の解説、または一連の人口統計要素を含むかもしれない。 </p>
    <p> 個々の発話に属性<att>who</att>が付与されている場合、グローバル属性 <att>xml:id</att>は、発話テキスト中の発話者を特定するために使われる べきである。 </p>
  </remarks>
```

^b58

### Block 59

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHPA"/>
  </listRef>
```

^b59

