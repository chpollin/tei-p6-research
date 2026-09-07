---
type: representation
source-type: document
source: '[[00_sources/tei-p5-samplingdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 samplingDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/samplingDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# samplingDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5991. Git blob: `39136c0e3235efd128d86ac2131a5cd177b2231a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-samplingDecl" ident="samplingDecl">
  <gloss versionDate="2005-01-14" xml:lang="en">sampling declaration</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">déclaration d'échantillonnage</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">표본 추출 선언</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">取樣宣告</gloss>
    <gloss versionDate="2016-11-17" xml:lang="de">Angabe der Auswahlverfahren</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de muestra</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione di campionatura</gloss>
  <desc versionDate="2023-10-10" xml:lang="en">contains a prose description of the rationale and methods used in selecting texts, or parts of a text, for inclusion in the resource.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">contient une description en texte libre du raisonnement
    et des méthodes utilisés pour l'échantillonnage des textes dans la création d’un corpus ou
    d’une collection.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">코퍼스 또는 텍스트 집단 구축에서 표본 추출에 사용된 원리와 방법에 대한 산문체 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">以篇章描述的方式說明建立文集或文選時文件取樣的原理與方法。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">コーパス等を作成する際、テキストを標本化する原理や手法に関する、散文 による解説を含む。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">enthält eine Beschreibung der Kriterien und Methoden, 
        nach denen die Texte für ein Korpus oder eine Sammlung zusammengestellt wurden.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción en prosa sobre los fundamentos y
    métodos usados en textos de muestra en la creación de un corpus o una selección de textos.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione dei metodi e dei principi usati
    nella campionatura dei testi nella creazione o raccolta del corpus.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="samplingDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:samplingDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-samplingDecl-egXML-ak">
      <samplingDecl>
        <p>Samples of up to 2000 words taken at random from the beginning, middle, or end of each
          text identified as relevant by respondents.</p>
      </samplingDecl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-samplingDecl-egXML-xm">
      <samplingDecl>
        <p>Corpus
                      d'échantillons de 2000 mots pris au début de chaque texte. </p>
      </samplingDecl>
    </egXML>
  </exemplum>
  <remarks ident="samplingDecl-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element records all information about systematic inclusion or omission of portions of
      the text, whether a reflection of sampling procedures in the pure sense or of systematic
      omission of material deemed either too difficult to transcribe or not of sufficient
    interest.</p>
  </remarks>
  <remarks ident="samplingDecl-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément rassemble toute information sur l'inclusion ou l'omission systématique de
      segments du texte, quel que soit le résultat des procédures d'échantillonnage au sens strict,
      ou de l'omission systématique d'éléments jugés soit trop difficiles à transcrire, soit sans
      intérêt.</p>
  </remarks>
  <remarks ident="samplingDecl-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Este elemento registra toda la información sobre la inclusión sistemática o la omisión de
      fragmentos de texto, si los procedimientos de muestra en el sentido estricto o la omisión
      sistemática del material se consideran demasiado difíciles de transcribir o no de suficiente
      interés.</p>
  </remarks>
  <remarks ident="samplingDecl-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 純粋な意味での標本化過程または体系的な資料の省略が、難しすぎて転記 できない、または充分な関心が得られていないと考えられているにしても、 当該要
      素は、テキスト部分の体系的な取捨選択に関する情報の全てを 記録する。 </p>
  </remarks>
 <remarks ident="samplingDecl-remarks" versionDate="2016-11-17" xml:lang="de">
     <p>
         Dieses Element umfasst Informationen über das systematische Einbinden oder Auslassen von Textteilen. 
         Dabei kann es sich um eine Beschreibung der Auswahlprozesse handeln oder um Angaben darüber, 
         warum bestimmtes Material ausgelassen wurde, z. B. weil das Material zu schwierig zu transkribieren 
         oder nicht interessant genug war.  
     </p>
 </remarks>
  <listRef>
    <ptr target="#HD52"/>
    <ptr target="#HD5"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">sampling declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">déclaration d'échantillonnage</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">표본 추출 선언</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">取樣宣告</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Angabe der Auswahlverfahren</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de muestra</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione di campionatura</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2023-10-10" xml:lang="en">contains a prose description of the rationale and methods used in selecting texts, or parts of a text, for inclusion in the resource.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">contient une description en texte libre du raisonnement
    et des méthodes utilisés pour l'échantillonnage des textes dans la création d’un corpus ou
    d’une collection.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">코퍼스 또는 텍스트 집단 구축에서 표본 추출에 사용된 원리와 방법에 대한 산문체 기술을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">以篇章描述的方式說明建立文集或文選時文件取樣的原理與方法。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">コーパス等を作成する際、テキストを標本化する原理や手法に関する、散文 による解説を含む。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">enthält eine Beschreibung der Kriterien und Methoden, 
        nach denen die Texte für ein Korpus oder eine Sammlung zusammengestellt wurden.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción en prosa sobre los fundamentos y
    métodos usados en textos de muestra en la creación de un corpus o una selección de textos.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione dei metodi e dei principi usati
    nella campionatura dei testi nella creazione o raccolta del corpus.</desc>
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
<constraintSpec ident="samplingDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:samplingDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-samplingDecl-egXML-ak">
      <samplingDecl>
        <p>Samples of up to 2000 words taken at random from the beginning, middle, or end of each
          text identified as relevant by respondents.</p>
      </samplingDecl>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-samplingDecl-egXML-xm">
      <samplingDecl>
        <p>Corpus
                      d'échantillons de 2000 mots pris au début de chaque texte. </p>
      </samplingDecl>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="samplingDecl-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element records all information about systematic inclusion or omission of portions of
      the text, whether a reflection of sampling procedures in the pure sense or of systematic
      omission of material deemed either too difficult to transcribe or not of sufficient
    interest.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="samplingDecl-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément rassemble toute information sur l'inclusion ou l'omission systématique de
      segments du texte, quel que soit le résultat des procédures d'échantillonnage au sens strict,
      ou de l'omission systématique d'éléments jugés soit trop difficiles à transcrire, soit sans
      intérêt.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="samplingDecl-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Este elemento registra toda la información sobre la inclusión sistemática o la omisión de
      fragmentos de texto, si los procedimientos de muestra en el sentido estricto o la omisión
      sistemática del material se consideran demasiado difíciles de transcribir o no de suficiente
      interés.</p>
  </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="samplingDecl-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 純粋な意味での標本化過程または体系的な資料の省略が、難しすぎて転記 できない、または充分な関心が得られていないと考えられているにしても、 当該要
      素は、テキスト部分の体系的な取捨選択に関する情報の全てを 記録する。 </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="samplingDecl-remarks" versionDate="2016-11-17" xml:lang="de">
     <p>
         Dieses Element umfasst Informationen über das systematische Einbinden oder Auslassen von Textteilen. 
         Dabei kann es sich um eine Beschreibung der Auswahlprozesse handeln oder um Angaben darüber, 
         warum bestimmtes Material ausgelassen wurde, z. B. weil das Material zu schwierig zu transkribieren 
         oder nicht interessant genug war.  
     </p>
 </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD52"/>
    <ptr target="#HD5"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b26

