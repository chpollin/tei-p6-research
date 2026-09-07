---
type: representation
source-type: document
source: '[[00_sources/tei-p5-domain-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 domain
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/domain.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# domain

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10012. Git blob: `4bfe4005e1068640a58b234a9a9233a76f54b38d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="corpus" xml:id="gi-domain" ident="domain">
  <gloss versionDate="2007-07-04" xml:lang="en">domain of use</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">사용 영역</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">應用領域</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">domaine d'usage</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">campo de uso</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">ambito di uso</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes the most important social context in which the text was
realized or for which it is intended, for example private vs. public,
education, religion, etc.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 실현되거나 사용되는 가장 중요한 사회적 맥락을 기술한다. 예를 들어 공적 대 사적, 교육, 종교 등.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述該文本最重要的應用領域或是社會用途所在，例如私人與公共、教育、宗教等。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該テキストの出現に関する最も重要な社会的状況を示す。例えば、私的、
  公的、教育上、宗教上など。</desc>
  <desc versionDate="2009-03-20" xml:lang="fr">décrit le contexte social principal dans lequel le
      texte a été réalisé ou pour lequel il est conçu, par exemple : sphère privée ou publique,
      contexte éducatif, religieux, etc.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describle el contexto social más importante en el que el texto fue realizado o para el que se destina, p.ej. privado o público, educacional, religioso, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive il più importantecontesto sociale nel quale il testo è stato realizzato, ad esempio privato o pubblico, scolastico, religioso, ecc.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.textDescPart"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <desc versionDate="2005-01-14" xml:lang="en">categorizes the domain of use.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">사용 영역을 범주화한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">將應用領域分類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該社会的状況の分類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">catégorise le domaine d'usage.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">clasifica el campo de uso.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica l'ambito di uso.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="art">
          <desc versionDate="2007-06-27" xml:lang="en">art and entertainment</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">예술과 연예</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">藝術和娛樂</desc>
          <desc versionDate="2008-04-06" xml:lang="es">arte y entretenimiento</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">芸術、娯楽。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">art et loisirs</desc>
          <desc versionDate="2007-01-21" xml:lang="it">arte e intrattenimento.</desc>
        </valItem>
        <valItem ident="domestic">
          <desc versionDate="2007-06-27" xml:lang="en">domestic and private</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">가정과 개인</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">家庭和私人</desc>
          <desc versionDate="2008-04-06" xml:lang="es">doméstico y privado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">家庭内、私的。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">domestique et privé</desc>
          <desc versionDate="2007-01-21" xml:lang="it">domestico e privato.</desc>
        </valItem>
        <valItem ident="religious">
          <desc versionDate="2007-06-27" xml:lang="en">religious and ceremonial</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">종교와 의식</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">宗教和儀式</desc>
          <desc versionDate="2008-04-06" xml:lang="es">religioso y ceremonial</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">宗教、儀式。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">religieux et rituel</desc>
          <desc versionDate="2007-01-21" xml:lang="it">religioso e cerimoniale.</desc>
        </valItem>
        <valItem ident="business">
          <desc versionDate="2007-06-27" xml:lang="en">business and work place</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">사업과 사무 공간</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">商業和工作場所</desc>
          <desc versionDate="2008-04-06" xml:lang="es">negocio y lugar de trabajo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">仕事、職場。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">entreprise et lieu de travail</desc>
          <desc versionDate="2007-01-21" xml:lang="it">lavorativo e di affari.</desc>
        </valItem>
        <valItem ident="education">
          <gloss versionDate="2007-06-27" xml:lang="en">education</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">교육</gloss>
          <gloss versionDate="2007-05-02" xml:lang="zh-TW">教育</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">educación</gloss>
          <gloss versionDate="2008-04-05" xml:lang="ja">教育。</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">éducation</gloss>
          <gloss versionDate="2007-01-21" xml:lang="it">scolastico</gloss>
        </valItem>
        <valItem ident="govt">
          <gloss versionDate="2007-07-04" xml:lang="en">government</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">정부</gloss>
          <gloss versionDate="2009-03-20" xml:lang="fr">gouvernement</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">governativo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">gubernamental y legal</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">government and law</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">정부와 법률</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">政府和法律</desc>
          <desc versionDate="2008-04-06" xml:lang="es">gobierno y ley</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">政府、法律。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">gouvernement et loi</desc>
          <desc versionDate="2007-01-21" xml:lang="it">governativo e legislativo.</desc>
        </valItem>
        <valItem ident="public">
          <desc versionDate="2007-06-27" xml:lang="en">other forms of public context</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">공적 맥락의 기타 형식</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">其他公共領域</desc>
          <desc versionDate="2008-04-06" xml:lang="es">otras formas de contexto público</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">その他の公的なもの。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">autres formes de contexte public</desc>
          <desc versionDate="2007-01-21" xml:lang="it">altre forme di contesto pubblico.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-domain-egXML-jp">
      <domain type="domestic"/>
      <domain type="rel">religious broadcast</domain>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-domain-egXML-lf">
      <domain type="domestic"/>
      <domain type="rel">Émission religieuse</domain>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-domain-egXML-wr">
      <domain type="domestic"/>
      <domain type="rel">宗教廣播</domain>
    </egXML>
  </exemplum>
  <remarks ident="domain-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Usually empty, unless some further clarification of the type
attribute is needed, in which case it may contain running
prose.</p>
    <p>The list presented here is primarily for illustrative
purposes.</p>
  </remarks>
  <remarks ident="domain-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc"> Habituellement vide, sauf si une clarification complémentaire sur le
                type de l’attribut est nécessaire : dans ce cas il peut contenir du texte non
                structuré.</p>
    <p> La liste est présentée ici dans un but d’illustration.</p>
  </remarks>
  <remarks ident="domain-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    当該属性が必要なければ、一般には属性typeの値はない。この場合は、当
  該要素の内容に散文で記述される。
  </p>
    <p>
    上記の属性値リストは、当該要素の解説を意図したものである。
    </p>
  </remarks>
  <listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">domain of use</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">사용 영역</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">應用領域</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">domaine d'usage</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">campo de uso</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">ambito di uso</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes the most important social context in which the text was
realized or for which it is intended, for example private vs. public,
education, religion, etc.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트가 실현되거나 사용되는 가장 중요한 사회적 맥락을 기술한다. 예를 들어 공적 대 사적, 교육, 종교 등.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述該文本最重要的應用領域或是社會用途所在，例如私人與公共、教育、宗教等。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストの出現に関する最も重要な社会的状況を示す。例えば、私的、
  公的、教育上、宗教上など。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-03-20" xml:lang="fr">décrit le contexte social principal dans lequel le
      texte a été réalisé ou pour lequel il est conçu, par exemple : sphère privée ou publique,
      contexte éducatif, religieux, etc.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describle el contexto social más importante en el que el texto fue realizado o para el que se destina, p.ej. privado o público, educacional, religioso, etc.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive il più importantecontesto sociale nel quale il testo è stato realizzato, ad esempio privato o pubblico, scolastico, religioso, ecc.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.textDescPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">categorizes the domain of use.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사용 영역을 범주화한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">將應用領域分類。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該社会的状況の分類を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">catégorise le domaine d'usage.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clasifica el campo de uso.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica l'ambito di uso.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="art">
          <desc versionDate="2007-06-27" xml:lang="en">art and entertainment</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">예술과 연예</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">藝術和娛樂</desc>
          <desc versionDate="2008-04-06" xml:lang="es">arte y entretenimiento</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">芸術、娯楽。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">art et loisirs</desc>
          <desc versionDate="2007-01-21" xml:lang="it">arte e intrattenimento.</desc>
        </valItem>
        <valItem ident="domestic">
          <desc versionDate="2007-06-27" xml:lang="en">domestic and private</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">가정과 개인</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">家庭和私人</desc>
          <desc versionDate="2008-04-06" xml:lang="es">doméstico y privado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">家庭内、私的。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">domestique et privé</desc>
          <desc versionDate="2007-01-21" xml:lang="it">domestico e privato.</desc>
        </valItem>
        <valItem ident="religious">
          <desc versionDate="2007-06-27" xml:lang="en">religious and ceremonial</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">종교와 의식</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">宗教和儀式</desc>
          <desc versionDate="2008-04-06" xml:lang="es">religioso y ceremonial</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">宗教、儀式。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">religieux et rituel</desc>
          <desc versionDate="2007-01-21" xml:lang="it">religioso e cerimoniale.</desc>
        </valItem>
        <valItem ident="business">
          <desc versionDate="2007-06-27" xml:lang="en">business and work place</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">사업과 사무 공간</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">商業和工作場所</desc>
          <desc versionDate="2008-04-06" xml:lang="es">negocio y lugar de trabajo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">仕事、職場。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">entreprise et lieu de travail</desc>
          <desc versionDate="2007-01-21" xml:lang="it">lavorativo e di affari.</desc>
        </valItem>
        <valItem ident="education">
          <gloss versionDate="2007-06-27" xml:lang="en">education</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">교육</gloss>
          <gloss versionDate="2007-05-02" xml:lang="zh-TW">教育</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es">educación</gloss>
          <gloss versionDate="2008-04-05" xml:lang="ja">教育。</gloss>
          <gloss versionDate="2008-03-30" xml:lang="fr">éducation</gloss>
          <gloss versionDate="2007-01-21" xml:lang="it">scolastico</gloss>
        </valItem>
        <valItem ident="govt">
          <gloss versionDate="2007-07-04" xml:lang="en">government</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">정부</gloss>
          <gloss versionDate="2009-03-20" xml:lang="fr">gouvernement</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">governativo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">gubernamental y legal</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">government and law</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">정부와 법률</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">政府和法律</desc>
          <desc versionDate="2008-04-06" xml:lang="es">gobierno y ley</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">政府、法律。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">gouvernement et loi</desc>
          <desc versionDate="2007-01-21" xml:lang="it">governativo e legislativo.</desc>
        </valItem>
        <valItem ident="public">
          <desc versionDate="2007-06-27" xml:lang="en">other forms of public context</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">공적 맥락의 기타 형식</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">其他公共領域</desc>
          <desc versionDate="2008-04-06" xml:lang="es">otras formas de contexto público</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">その他の公的なもの。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">autres formes de contexte public</desc>
          <desc versionDate="2007-01-21" xml:lang="it">altre forme di contesto pubblico.</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-domain-egXML-jp">
      <domain type="domestic"/>
      <domain type="rel">religious broadcast</domain>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-domain-egXML-lf">
      <domain type="domestic"/>
      <domain type="rel">Émission religieuse</domain>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-domain-egXML-wr">
      <domain type="domestic"/>
      <domain type="rel">宗教廣播</domain>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="domain-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Usually empty, unless some further clarification of the type
attribute is needed, in which case it may contain running
prose.</p>
    <p>The list presented here is primarily for illustrative
purposes.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="domain-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc"> Habituellement vide, sauf si une clarification complémentaire sur le
                type de l’attribut est nécessaire : dans ce cas il peut contenir du texte non
                structuré.</p>
    <p> La liste est présentée ici dans un but d’illustration.</p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="domain-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    当該属性が必要なければ、一般には属性typeの値はない。この場合は、当
  該要素の内容に散文で記述される。
  </p>
    <p>
    上記の属性値リストは、当該要素の解説を意図したものである。
    </p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
```

^b31

