---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.duration-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.duration
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.duration.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.duration

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5339. Git blob: `033999ded674839878985bc5d7cddf480ad051b3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="spoken" predeclare="true" type="atts" ident="att.duration">
  <!--desc>attributes for recording normalized temporal durations</desc-->
  <desc versionDate="2007-04-20" xml:lang="en">provides attributes for normalization of elements that contain datable events.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">날짜를 정할 수 있는 사건을 포함하는 요소의 규격화를 위한 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供用於元素規格化的屬性，這些元素包含日期明確的事件。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">時間事象を含む要素の正規化手法を表す属性を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour la normalisation des
      éléments qui contiennent des mentions d'événements datables.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">indica degli attributi per la normalizzazione di elementi che contengono eventi databili.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para la normalización de elementos que contienen eventos datables</desc>
  <classes>
    <memberOf key="att.duration.iso"/>
    
    <memberOf key="att.duration.w3c"/>
  </classes>
  <remarks ident="att.duration-remarks" versionDate="2007-06-12" xml:lang="en">
    <p>This <soCalled>superclass</soCalled> provides attributes that
    can be used to provide normalized values of temporal information.
    By default, the attributes from the <ident type="class">att.duration.w3c</ident> class are provided. If the
    module for names &amp; dates is loaded, this class also provides
    attributes from the <ident type="class">att.duration.iso</ident>
    class. In general, the possible values of attributes restricted to
    the W3C datatypes form a subset of those values available via the
    ISO 8601 standard. However, the greater expressiveness of the ISO
    datatypes is rarely needed, and there exists much greater software
    support for the W3C datatypes.</p>
  </remarks>
  <remarks ident="att.duration-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette<soCalled>superclasse</soCalled> fournit des attributs qui peuvent être employés
                pour fournir des valeurs normalisées d'information relative au temps. Par défaut,
                les attributs de la classe <ident type="class">att.duration.w3c</ident> sont
                fournis. Si le module pour les noms et dates est chargé, cette classe fournit
                également des attributs de la classe<ident type="class">att.duration.iso</ident>. En
                général, les valeurs possibles des attributs limitées aux types de données W3C
                forment un sous-ensemble des valeurs que l'on trouve dans la norme ISO 8601.
                Cependant, il est rarement nécessaire de recourir aux possibilités très étendues des
                types de données de l'ISO, il existe en effet une bien plus grande offre logicielle
                pour le traitement des types de données W3C.</p>
  </remarks>
  <remarks ident="att.duration-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta <soCalled>superclase</soCalled> proporciona atributos que se pueden utilizar para proporcionar los valores normalizados de la información temporal.
    Por defecto, los atributos de la clase <ident type="class">att.duration.w3c</ident> son proporcionados. Si el módulo para los nombres y las fechas se activa, esta clase también proporciona atributos para la clase <ident type="class">att.duration.iso</ident>
. En general, los valores posibles de los atributos son los restringidos por la forma de los datatypes de W3C, un subconjunto de esos valores disponibles vía el estándar de ISO 8601. Sin embargo, la mayoría de expresiones de los datatypes de ISO se necesitan raramente, y existe software de soporte para los datatypes de W3C.</p>
  </remarks>
  <remarks ident="att.duration-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    このいわゆる<soCalled>親クラス(スーパークラス)</soCalled>は、
    正規化された値を属性値として持つ、時間情報を示す属性になる。
    デフォルト値として、当該属性は、クラス
    <ident type="class">att.datable.w3c</ident>が付与されている。
    名前と日付に関するモジュールが使用される場合、当該クラスは、クラス
    <ident type="class">att.duration.iso</ident>から属性が与えられる。    
    一般には、W3Cのデータ形式に従った属性値は、ITO8601に従った属性値の
    下位要素になっている。しかし、より強力な表現力を持つISOのデータ形
    式が必要になることはない。さらに強力な表現力をサポートするソフトウェ
    アも存在する。        
    </p>
  </remarks>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-20" xml:lang="en">provides attributes for normalization of elements that contain datable events.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">날짜를 정할 수 있는 사건을 포함하는 요소의 규격화를 위한 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供用於元素規格化的屬性，這些元素包含日期明確的事件。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">時間事象を含む要素の正規化手法を表す属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit des attributs pour la normalisation des
      éléments qui contiennent des mentions d'événements datables.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica degli attributi per la normalizzazione di elementi che contengono eventi databili.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos para la normalización de elementos que contienen eventos datables</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.duration.iso"/>
    
    <memberOf key="att.duration.w3c"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="att.duration-remarks" versionDate="2007-06-12" xml:lang="en">
    <p>This <soCalled>superclass</soCalled> provides attributes that
    can be used to provide normalized values of temporal information.
    By default, the attributes from the <ident type="class">att.duration.w3c</ident> class are provided. If the
    module for names &amp; dates is loaded, this class also provides
    attributes from the <ident type="class">att.duration.iso</ident>
    class. In general, the possible values of attributes restricted to
    the W3C datatypes form a subset of those values available via the
    ISO 8601 standard. However, the greater expressiveness of the ISO
    datatypes is rarely needed, and there exists much greater software
    support for the W3C datatypes.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="att.duration-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette<soCalled>superclasse</soCalled> fournit des attributs qui peuvent être employés
                pour fournir des valeurs normalisées d'information relative au temps. Par défaut,
                les attributs de la classe <ident type="class">att.duration.w3c</ident> sont
                fournis. Si le module pour les noms et dates est chargé, cette classe fournit
                également des attributs de la classe<ident type="class">att.duration.iso</ident>. En
                général, les valeurs possibles des attributs limitées aux types de données W3C
                forment un sous-ensemble des valeurs que l'on trouve dans la norme ISO 8601.
                Cependant, il est rarement nécessaire de recourir aux possibilités très étendues des
                types de données de l'ISO, il existe en effet une bien plus grande offre logicielle
                pour le traitement des types de données W3C.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="att.duration-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta <soCalled>superclase</soCalled> proporciona atributos que se pueden utilizar para proporcionar los valores normalizados de la información temporal.
    Por defecto, los atributos de la clase <ident type="class">att.duration.w3c</ident> son proporcionados. Si el módulo para los nombres y las fechas se activa, esta clase también proporciona atributos para la clase <ident type="class">att.duration.iso</ident>
. En general, los valores posibles de los atributos son los restringidos por la forma de los datatypes de W3C, un subconjunto de esos valores disponibles vía el estándar de ISO 8601. Sin embargo, la mayoría de expresiones de los datatypes de ISO se necesitan raramente, y existe software de soporte para los datatypes de W3C.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="att.duration-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    このいわゆる<soCalled>親クラス(スーパークラス)</soCalled>は、
    正規化された値を属性値として持つ、時間情報を示す属性になる。
    デフォルト値として、当該属性は、クラス
    <ident type="class">att.datable.w3c</ident>が付与されている。
    名前と日付に関するモジュールが使用される場合、当該クラスは、クラス
    <ident type="class">att.duration.iso</ident>から属性が与えられる。    
    一般には、W3Cのデータ形式に従った属性値は、ITO8601に従った属性値の
    下位要素になっている。しかし、より強力な表現力を持つISOのデータ形
    式が必要になることはない。さらに強力な表現力をサポートするソフトウェ
    アも存在する。        
    </p>
  </remarks>
```

^b12

