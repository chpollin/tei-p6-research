---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.persstatelike-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.persStateLike
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.persStateLike.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.persStateLike

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3116. Git blob: `333307173830c0a1a5883919e87b3bf78d7be74b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" type="model" module="tei" ident="model.persStateLike">
  <desc versionDate="2007-10-03" xml:lang="en">groups elements describing changeable characteristics of a person which have a definite
    duration, for example occupation, residence, or name.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">직업, 거주지, 이름과 같이 일정 기간 유지되는 변화가능한 사람의 특성을 기술하는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集描述人物的可改變特性，有明確的時間長度，例如職業、居所、姓名等。這些特性通常是個人或他人行為的結果。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">一定期間で変容する、個人の特性を示す要素をまとめる。例えば、仕事、住 所、名前など。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">regroupe des éléments décrivant les caractéristiques
    d'une personne, variables mais définies dans le temps, par exemple sa profession, son lieu de
    résidence ou son nom.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">clase de elementos que describen las características
    mutables o con una duración determinada en una persona, p.ej. ocupación, residencia, nombre,
    etc.; tales características de un individuo representan generalmente una consecuencia de sus
    acciones o de las de otros.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">classe di elementi che descrivono le caratteristiche
    mutevoli e con una determinata durata di una persona, per esempio occupazione, residenza, nome,
    ecc.; tali caratteristiche di un individuo rappresentano in genere una conseguenza delle sue
    azioni o di quelle degli altri</desc>
  <classes>
    
    <memberOf key="model.personPart"/>
  </classes>
  <remarks ident="model.persStateLike-remarks" versionDate="2007-10-03" xml:lang="en">
    <p>These characteristics of an individual are typically a consequence of their own action or
      that of others.</p>
  </remarks>
  <remarks ident="model.persStateLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Il s'agit en général des caractéristiques d'un individu résultant de sa propre action ou de
      celle d'autrui.</p>
  </remarks>
  <remarks ident="model.persStateLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Estas características de un individuo son típicamente una consecuencia de su propia acción o
      de la de otros.</p>
  </remarks>
  <remarks ident="model.persStateLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該個人の特性は、自らの行動などによる結果である。 </p>
  </remarks>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-10-03" xml:lang="en">groups elements describing changeable characteristics of a person which have a definite
    duration, for example occupation, residence, or name.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">직업, 거주지, 이름과 같이 일정 기간 유지되는 변화가능한 사람의 특성을 기술하는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">該元素集描述人物的可改變特性，有明確的時間長度，例如職業、居所、姓名等。這些特性通常是個人或他人行為的結果。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">一定期間で変容する、個人の特性を示す要素をまとめる。例えば、仕事、住 所、名前など。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">regroupe des éléments décrivant les caractéristiques
    d'une personne, variables mais définies dans le temps, par exemple sa profession, son lieu de
    résidence ou son nom.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">clase de elementos que describen las características
    mutables o con una duración determinada en una persona, p.ej. ocupación, residencia, nombre,
    etc.; tales características de un individuo representan generalmente una consecuencia de sus
    acciones o de las de otros.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classe di elementi che descrivono le caratteristiche
    mutevoli e con una determinata durata di una persona, per esempio occupazione, residenza, nome,
    ecc.; tali caratteristiche di un individuo rappresentano in genere una conseguenza delle sue
    azioni o di quelle degli altri</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.personPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.persStateLike-remarks" versionDate="2007-10-03" xml:lang="en">
    <p>These characteristics of an individual are typically a consequence of their own action or
      that of others.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.persStateLike-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Il s'agit en général des caractéristiques d'un individu résultant de sa propre action ou de
      celle d'autrui.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.persStateLike-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Estas características de un individuo son típicamente una consecuencia de su propia acción o
      de la de otros.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.persStateLike-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該個人の特性は、自らの行動などによる結果である。 </p>
  </remarks>
```

^b12

