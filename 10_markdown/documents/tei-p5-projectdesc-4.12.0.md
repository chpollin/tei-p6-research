---
type: representation
source-type: document
source: '[[00_sources/tei-p5-projectdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 projectDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/projectDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# projectDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5753. Git blob: `a52fdb4d8a46cd0fe7a48d6a12bd2efd9d294946`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-projectDesc" ident="projectDesc">
  <gloss versionDate="2005-01-14" xml:lang="en">project description</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">description du projet</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">프로젝트 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">計畫描述</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Beschreibung des Projekts</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción del proyecto</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione del progetto</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">describes in detail the aim or purpose for which an electronic file was encoded, together
    with any other relevant information concerning the process by which it was assembled or
    collected.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">décrit en détail le but ou l’objectif visé dans
    l’encodage d’un fichier électronique, ainsi que toute autre information pertinente sur la
    manière dont il a été construit ou recueilli.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전자 파일이 부호화된 목적을 상세히 기술하며, 아울러 그것이 수집된 절차에 관한 기타 관련 정보를
    기술한다, .</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">詳述將電子檔案編碼的目標或目的，以及其他關於檔案匯集或收集程序的任何資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">制作過程に関する情報も含めて、電子ファイルが作られた目的の詳細を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">beschreibt detailliert Ziel bzw. Zweck, für den eine Datei kodiert wurde, zusammen mit weiteren relevanten Informationen, 
        die das Verfahren betreffen, nach dem die Daten zusammengestellt oder gesammelt wurden.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe con detalle el objetivo o propósito para el que
    un archivo electrónico ha sido codificado, junto a cualquier otra información relevante sobre el
    proceso de codificación.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive in dettaglio lo scopo per il quale un documento
    elettronico è sato codigicato, insieme a qualsiasi altra informazione rilevante riguardo le
    procedure di raccolta.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="projectDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:projectDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-projectDesc-egXML-gg">
      <projectDesc>
        <p>Texts collected for use in the Claremont Shakespeare Clinic, June 1990</p>
      </projectDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-projectDesc-egXML-ae" source="#fr-ex-Cyrus">
      <projectDesc>
        <p>La saisie a été effectuée par notre partenaire Datactivity. Le texte saisi a été
            ensuite converti et remis en forme selon les normes du format XML, standard d’échange ou
            d’affichage de documents permettant de séparer la forme et le contenu et offrant une
            déclinaison d’outils qui donnent la possibilité d’exploiter un texte comme une véritable
            base de données. La norme adoptée (DTD) est le TEI (Text Encoding Initiative). </p>
        <p> Affichage et manipulation du texte (mise au format, filtrage, réorganisation) se font
            sur un serveur Apache à l'aide de l'infrastructure Axkit.</p>
        <p> Le moteur logiciel du site a été développé en Xpathscript et s'appuie sur les travaux
            de Dominique Quatravaux (Alliance Francophone Pour l'Avancement d'XPathScript) et de
            Yanick Champoux (support de Libxml via YPathScript).</p>
        <p>Les programmes développés pour le site sont mis à la disposition en open-source sur
            demande (contacter Alexandre Gefen). </p>
        <p>Les fonctions de recherche plein texte sont fournies par Philologic dans le cadre du
            partenariat du projet avec ARTFL.</p>
        <p>L’architecture de travail, sous Linux, est destinée à garantir une haute disponibilité
            et des performances optimales. La liaison avec Internet est assurée par les services
            informatiques de l’Université de Neuchâtel (SITEL).</p>
      </projectDesc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-projectDesc-egXML-we">
      <projectDesc>
        <p>文件收集於1990年7月，杭州杜甫詩作研討會使用</p>
      </projectDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD51"/>
    <ptr target="#HD5"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">project description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">description du projet</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">프로젝트 기술</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">計畫描述</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Beschreibung des Projekts</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción del proyecto</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione del progetto</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes in detail the aim or purpose for which an electronic file was encoded, together
    with any other relevant information concerning the process by which it was assembled or
    collected.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">décrit en détail le but ou l’objectif visé dans
    l’encodage d’un fichier électronique, ainsi que toute autre information pertinente sur la
    manière dont il a été construit ou recueilli.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전자 파일이 부호화된 목적을 상세히 기술하며, 아울러 그것이 수집된 절차에 관한 기타 관련 정보를
    기술한다, .</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">詳述將電子檔案編碼的目標或目的，以及其他關於檔案匯集或收集程序的任何資訊。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">制作過程に関する情報も含めて、電子ファイルが作られた目的の詳細を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">beschreibt detailliert Ziel bzw. Zweck, für den eine Datei kodiert wurde, zusammen mit weiteren relevanten Informationen, 
        die das Verfahren betreffen, nach dem die Daten zusammengestellt oder gesammelt wurden.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe con detalle el objetivo o propósito para el que
    un archivo electrónico ha sido codificado, junto a cualquier otra información relevante sobre el
    proceso de codificación.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive in dettaglio lo scopo per il quale un documento
    elettronico è sato codigicato, insieme a qualsiasi altra informazione rilevante riguardo le
    procedure di raccolta.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="projectDesc-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:projectDesc"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-projectDesc-egXML-gg">
      <projectDesc>
        <p>Texts collected for use in the Claremont Shakespeare Clinic, June 1990</p>
      </projectDesc>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-projectDesc-egXML-ae" source="#fr-ex-Cyrus">
      <projectDesc>
        <p>La saisie a été effectuée par notre partenaire Datactivity. Le texte saisi a été
            ensuite converti et remis en forme selon les normes du format XML, standard d’échange ou
            d’affichage de documents permettant de séparer la forme et le contenu et offrant une
            déclinaison d’outils qui donnent la possibilité d’exploiter un texte comme une véritable
            base de données. La norme adoptée (DTD) est le TEI (Text Encoding Initiative). </p>
        <p> Affichage et manipulation du texte (mise au format, filtrage, réorganisation) se font
            sur un serveur Apache à l'aide de l'infrastructure Axkit.</p>
        <p> Le moteur logiciel du site a été développé en Xpathscript et s'appuie sur les travaux
            de Dominique Quatravaux (Alliance Francophone Pour l'Avancement d'XPathScript) et de
            Yanick Champoux (support de Libxml via YPathScript).</p>
        <p>Les programmes développés pour le site sont mis à la disposition en open-source sur
            demande (contacter Alexandre Gefen). </p>
        <p>Les fonctions de recherche plein texte sont fournies par Philologic dans le cadre du
            partenariat du projet avec ARTFL.</p>
        <p>L’architecture de travail, sous Linux, est destinée à garantir une haute disponibilité
            et des performances optimales. La liaison avec Internet est assurée par les services
            informatiques de l’Université de Neuchâtel (SITEL).</p>
      </projectDesc>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-projectDesc-egXML-we">
      <projectDesc>
        <p>文件收集於1990年7月，杭州杜甫詩作研討會使用</p>
      </projectDesc>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD51"/>
    <ptr target="#HD5"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b22

