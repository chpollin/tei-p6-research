---
type: representation
source-type: document
source: '[[00_sources/tei-p5-distinct-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 distinct
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/distinct.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# distinct

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7699. Git blob: `2efe44d238c0e59a402d137ef67028b42a3eb53e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-distinct" ident="distinct">
  <desc versionDate="2005-01-14" xml:lang="en">identifies any word or phrase which is regarded as linguistically distinct, for example as
        archaic, technical, dialectal, non-preferred, etc., or as forming part of a sublanguage.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">고어, 전문어, 방언, 비선호 단어 등과 같이 언어적으로 구분되거나 하위언어의 부분을 형성하는
        것으로 간주되는 임의의 단어 또는 구를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明被視為特殊用語的字詞，例如：古語、專業用語、方言、非推薦用語等，或標明形成部分次要語言的字詞</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">言語上、異なる語句を示す。例えば、古語、技術語、方言、忌諱語など。ま
        た、特定グループでしか通用しない特殊言語など。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">identifie tout mot ou toute expression en la  considérérant comme
        linguistiquement spécifique, par exemple comme étant archaïque, technique, dialectale,
        inusitée, ou comme appartenant à une langue spécifique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">identifica alguna palabra o locución que se aprecia
        lingüísticamente distinta, por ejemplo como arcaica, técnica, dialectal, forma no
        prioritaria, etc. o como integrante de un registro específico o de una jerga.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">identifica qualsiasi parola o sintagma ritenuto
        linguisticamente distinto, per esempio come arcaico, tecnico, dialettale, non preferito,
        ecc., o come parte di una lingua secondaria.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.emphLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the sublanguage or register to which the word or phrase is being assigned.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko"> 단어나 구가 속하는 하위언어 또는 레지스터를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明所標記的字詞屬於哪一種次要語言或語體層次</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該特殊言語または語句の種類を示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">précise la variété de langue ou le registre de langue
                auquels appartiennent le mot ou l'expression.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica la jerga o registro al cual se
                asigna una palabra, locución o sintagma.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica la lingua secondaria o il registro al
                quale la parola o il sintagma è ricondotto</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
    </attDef>
    <attDef ident="time" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies how the phrase is distinct diachronically.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">구가 통시적으로 구분되는 방식을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明該字詞是屬於哪一種時間上的特殊用語</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該語句の通時的特徴を示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">précise comment l'expression est diachroniquement distincte.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica como el sintagma es distinto
                diacrónicamente</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica come il sintagma sia distinto
                diacronicamente</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
    </attDef>
    <attDef ident="space" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies how the phrase is distinct diatopically.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">구가 지역적으로 구분되는 방식을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明該字詞是屬於哪一種區域上的特殊用語</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該語句の共時的特徴を示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">précise comment l'expression se caractérise de
                façon diatopique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica como la locución es distinta
                diatópicamente</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica come il sintagma sia distinto in modo
                diatopico</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
    </attDef>
    <attDef ident="social" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies how the phrase is distinct diastratically.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">구가 사회적으로 구분되는 방식을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指明該字詞是屬於哪一種社會層次分類上的特殊用語</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該語句の社会的特徴を示す。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">précise comment l'expression se caractérise de
                façon diastatique.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica como la locución es distinta
                diastáticamente.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica come il sintagma sia distinto in modo
                diastratico</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distinct-egXML-jx" source="#COHQHD-eg-18">Next morning a boy
            in that dormitory confided to his bosom friend, a <distinct type="ps_slang">fag</distinct> of 
            Macrea's, that there was trouble in their midst which King <distinct type="archaic">would fain</distinct> 
        keep secret.
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distinct-egXML-uv" source="#fr-ex-Belloc_Kepas">
      <p>- Elle fait chier, cette <distinct type="verlan">meuf</distinct>. Tu confonds amour et
            <distinct type="argot">piquouse</distinct>. Tu l'auras, ton <distinct type="argot">shoot</distinct>, merde ! </p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distinct-egXML-qa">
      張曼玉即使年過四十，依舊<distinct type="成語">風姿綽約</distinct> ，果然是東方<distinct type="hk_slang">靚妹</distinct>的最佳代表。</egXML>
  </exemplum>
  <listRef>
    <ptr target="#COHQHD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">identifies any word or phrase which is regarded as linguistically distinct, for example as
        archaic, technical, dialectal, non-preferred, etc., or as forming part of a sublanguage.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">고어, 전문어, 방언, 비선호 단어 등과 같이 언어적으로 구분되거나 하위언어의 부분을 형성하는
        것으로 간주되는 임의의 단어 또는 구를 표시한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明被視為特殊用語的字詞，例如：古語、專業用語、方言、非推薦用語等，或標明形成部分次要語言的字詞</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">言語上、異なる語句を示す。例えば、古語、技術語、方言、忌諱語など。ま
        た、特定グループでしか通用しない特殊言語など。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">identifie tout mot ou toute expression en la  considérérant comme
        linguistiquement spécifique, par exemple comme étant archaïque, technique, dialectale,
        inusitée, ou comme appartenant à une langue spécifique.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">identifica alguna palabra o locución que se aprecia
        lingüísticamente distinta, por ejemplo como arcaica, técnica, dialectal, forma no
        prioritaria, etc. o como integrante de un registro específico o de una jerga.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">identifica qualsiasi parola o sintagma ritenuto
        linguisticamente distinto, per esempio come arcaico, tecnico, dialettale, non preferito,
        ecc., o come parte di una lingua secondaria.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.emphLike"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the sublanguage or register to which the word or phrase is being assigned.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"> 단어나 구가 속하는 하위언어 또는 레지스터를 명시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明所標記的字詞屬於哪一種次要語言或語體層次</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該特殊言語または語句の種類を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">précise la variété de langue ou le registre de langue
                auquels appartiennent le mot ou l'expression.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica la jerga o registro al cual se
                asigna una palabra, locución o sintagma.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la lingua secondaria o il registro al
                quale la parola o il sintagma è ricondotto</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies how the phrase is distinct diachronically.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구가 통시적으로 구분되는 방식을 명시한다.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明該字詞是屬於哪一種時間上的特殊用語</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該語句の通時的特徴を示す。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">précise comment l'expression est diachroniquement distincte.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica como el sintagma es distinto
                diacrónicamente</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica come il sintagma sia distinto
                diacronicamente</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies how the phrase is distinct diatopically.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구가 지역적으로 구분되는 방식을 명시한다.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明該字詞是屬於哪一種區域上的特殊用語</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該語句の共時的特徴を示す。</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">précise comment l'expression se caractérise de
                façon diatopique.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica como la locución es distinta
                diatópicamente</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica come il sintagma sia distinto in modo
                diatopico</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies how the phrase is distinct diastratically.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구가 사회적으로 구분되는 방식을 명시한다.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指明該字詞是屬於哪一種社會層次分類上的特殊用語</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該語句の社会的特徴を示す。</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">précise comment l'expression se caractérise de
                façon diastatique.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica como la locución es distinta
                diastáticamente.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[4]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica come il sintagma sia distinto in modo
                diastratico</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[4]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b41

### Block 42

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distinct-egXML-jx" source="#COHQHD-eg-18">Next morning a boy
            in that dormitory confided to his bosom friend, a <distinct type="ps_slang">fag</distinct> of 
            Macrea's, that there was trouble in their midst which King <distinct type="archaic">would fain</distinct> 
        keep secret.
    </egXML>
  </exemplum>
```

^b42

### Block 43

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distinct-egXML-uv" source="#fr-ex-Belloc_Kepas">
      <p>- Elle fait chier, cette <distinct type="verlan">meuf</distinct>. Tu confonds amour et
            <distinct type="argot">piquouse</distinct>. Tu l'auras, ton <distinct type="argot">shoot</distinct>, merde ! </p>
    </egXML>
  </exemplum>
```

^b43

### Block 44

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-distinct-egXML-qa">
      張曼玉即使年過四十，依舊<distinct type="成語">風姿綽約</distinct> ，果然是東方<distinct type="hk_slang">靚妹</distinct>的最佳代表。</egXML>
  </exemplum>
```

^b44

### Block 45

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQHD"/>
  </listRef>
```

^b45

