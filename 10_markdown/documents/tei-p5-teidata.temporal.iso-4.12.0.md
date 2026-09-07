---
type: representation
source-type: document
source: '[[00_sources/tei-p5-teidata.temporal.iso-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 teidata.temporal.iso
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/teidata.temporal.iso.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# teidata.temporal.iso

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4510. Git blob: `3e0d82818184d21dc020b3cd1387f8d17c758db6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<dataSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" ident="teidata.temporal.iso">
  <desc versionDate="2007-04-08" xml:lang="en">defines the range of attribute values expressing a temporal expression such as a date, a
    time, or a combination of them, that conform to the international standard <title>Data elements
      and interchange formats – Information interchange – Representation of dates and times</title>.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">날짜, 시간, 또는 이들의 조합과 같은 시간 표현의 속성 값 범위를 정의하며, 이는 국제 표준
      <title>Data elements and interchange formats – Information interchange – Representation of
      dates and times</title>을 따른다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義該系列表示時間的屬性值，例如日期、時間或兩者的組合，需符合國際標準 Data elements and
    interchange formats – Information interchange – Representation of dates and times</desc>
  <desc versionDate="2024-08-08" xml:lang="ja">日付や時間などの時間表現をとる属性値の範囲を定義する。これは、国際標準である<title>Data elements and interchange formats - Information interchange - Representation of dates and times</title>に準拠したものになる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attribut qui sont capables
    d''exprimer une valeur temporelle comme une date, une période, ou une combinaison des deux qui
    se conforment au standard international <title>Data elements and interchange formats –
      Information interchange – Representation of dates and times</title>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos que expresan una
    expresión temporal como una fecha, una hora, o una combinación de estas, de acuerdo a un
    estándard internacional <title>Elementos de datos y formatos de intercambio - Intercambio de
      información – Representación de fechas y horas</title>.</desc>
  <content>
      <alternate>
         <dataRef name="date"/>
         <dataRef name="gYear"/>
         <dataRef name="gMonth"/>
         <dataRef name="gDay"/>
         <dataRef name="gYearMonth"/>
         <dataRef name="gMonthDay"/>
         <dataRef name="time"/>
         <dataRef name="dateTime"/>
         <dataRef name="token" restriction="[0-9.,DHMPRSTWYZ/:+\-]+"/>
      </alternate>
   </content>
  <remarks ident="teidata.temporal.iso-remarks" versionDate="2022-03-23" xml:lang="en">
      <p>If it is likely that the value used is to be compared with another, then a time zone
      indicator should always be included, and only the dateTime representation should be used.</p>
      <p>For all representations for which ISO 8601:2004 describes both a <term>basic</term> and an
        <term>extended</term> format, these Guidelines recommend use of the extended format.</p>
  </remarks>
  <remarks ident="teidata.temporal.iso-remarks" versionDate="2022-03-23" xml:lang="ja">
      <p> 当該属性値が他の値と比較される場合、時間帯は必ず示されるべきである。 またはdateTimeを使うべきである(訳注：この文は修正されるかもしれな い)。 </p>
      <p> ISO 8601:2004には<term>基本形式</term>と<term>拡張形式</term>がある。 本ガイドラインでは拡張形式を使うことを推奨する。 </p>
     
  </remarks>
  <remarks ident="teidata.temporal.iso-remarks" versionDate="2022-03-23" xml:lang="fr">
      <p> S'il est vraisemblable que la valeur utilisée soit destinée à être comparer à d’autres
      valeurs, alors une indication du fuseau horaire devrait toujours être incluse, et seule la
      représentation <term>dateTime</term> devrait être employée.</p>
      <p>Pour toutes les représentations pour lesquelles l’ISO 8601:2004 décrit à la fois un format
        <term>basique</term> et un format<term> étendu </term>, ce guide d’encodage recommandande
      l’emploi du format <term> étendu </term>.</p>
      
  </remarks>
</dataSpec>
```

## Source blocks

### Block 1

XML location: `/dataSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-08" xml:lang="en">defines the range of attribute values expressing a temporal expression such as a date, a
    time, or a combination of them, that conform to the international standard <title>Data elements
      and interchange formats – Information interchange – Representation of dates and times</title>.</desc>
```

^b1

### Block 2

XML location: `/dataSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">날짜, 시간, 또는 이들의 조합과 같은 시간 표현의 속성 값 범위를 정의하며, 이는 국제 표준
      <title>Data elements and interchange formats – Information interchange – Representation of
      dates and times</title>을 따른다.</desc>
```

^b2

### Block 3

XML location: `/dataSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義該系列表示時間的屬性值，例如日期、時間或兩者的組合，需符合國際標準 Data elements and
    interchange formats – Information interchange – Representation of dates and times</desc>
```

^b3

### Block 4

XML location: `/dataSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-08-08" xml:lang="ja">日付や時間などの時間表現をとる属性値の範囲を定義する。これは、国際標準である<title>Data elements and interchange formats - Information interchange - Representation of dates and times</title>に準拠したものになる。</desc>
```

^b4

### Block 5

XML location: `/dataSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">définit la gamme des valeurs d'attribut qui sont capables
    d''exprimer une valeur temporelle comme une date, une période, ou une combinaison des deux qui
    se conforment au standard international <title>Data elements and interchange formats –
      Information interchange – Representation of dates and times</title>.</desc>
```

^b5

### Block 6

XML location: `/dataSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores de atributos que expresan una
    expresión temporal como una fecha, una hora, o una combinación de estas, de acuerdo a un
    estándard internacional <title>Elementos de datos y formatos de intercambio - Intercambio de
      información – Representación de fechas y horas</title>.</desc>
```

^b6

### Block 7

XML location: `/dataSpec[1]/content[1]`.

```xml
<content>
      <alternate>
         <dataRef name="date"/>
         <dataRef name="gYear"/>
         <dataRef name="gMonth"/>
         <dataRef name="gDay"/>
         <dataRef name="gYearMonth"/>
         <dataRef name="gMonthDay"/>
         <dataRef name="time"/>
         <dataRef name="dateTime"/>
         <dataRef name="token" restriction="[0-9.,DHMPRSTWYZ/:+\-]+"/>
      </alternate>
   </content>
```

^b7

### Block 8

XML location: `/dataSpec[1]/remarks[1]`.

```xml
<remarks ident="teidata.temporal.iso-remarks" versionDate="2022-03-23" xml:lang="en">
      <p>If it is likely that the value used is to be compared with another, then a time zone
      indicator should always be included, and only the dateTime representation should be used.</p>
      <p>For all representations for which ISO 8601:2004 describes both a <term>basic</term> and an
        <term>extended</term> format, these Guidelines recommend use of the extended format.</p>
  </remarks>
```

^b8

### Block 9

XML location: `/dataSpec[1]/remarks[2]`.

```xml
<remarks ident="teidata.temporal.iso-remarks" versionDate="2022-03-23" xml:lang="ja">
      <p> 当該属性値が他の値と比較される場合、時間帯は必ず示されるべきである。 またはdateTimeを使うべきである(訳注：この文は修正されるかもしれな い)。 </p>
      <p> ISO 8601:2004には<term>基本形式</term>と<term>拡張形式</term>がある。 本ガイドラインでは拡張形式を使うことを推奨する。 </p>
     
  </remarks>
```

^b9

### Block 10

XML location: `/dataSpec[1]/remarks[3]`.

```xml
<remarks ident="teidata.temporal.iso-remarks" versionDate="2022-03-23" xml:lang="fr">
      <p> S'il est vraisemblable que la valeur utilisée soit destinée à être comparer à d’autres
      valeurs, alors une indication du fuseau horaire devrait toujours être incluse, et seule la
      représentation <term>dateTime</term> devrait être employée.</p>
      <p>Pour toutes les représentations pour lesquelles l’ISO 8601:2004 décrit à la fois un format
        <term>basique</term> et un format<term> étendu </term>, ce guide d’encodage recommandande
      l’emploi du format <term> étendu </term>.</p>
      
  </remarks>
```

^b10

