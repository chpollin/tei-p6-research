---
type: representation
source-type: document
source: '[[00_sources/tei-p5-vrange-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 vRange
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/vRange.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# vRange

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4761. Git blob: `0838a33c5177df448cd89de0dfc97882aaac97a1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-vRange" ident="vRange">
  <gloss versionDate="2005-01-14" xml:lang="en">value range</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">값의 범위</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">功能值範圍</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">gamme de valeurs</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">gama de valores</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">gamma di valori</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">defines the range of allowed values for a feature, in the form of
an <gi>fs</gi>, <gi>vAlt</gi>, or primitive value;
for the value of an <gi>f</gi> to be valid, it must be
subsumed by the specified range; if the <gi>f</gi>
contains multiple values (as sanctioned by the <att>org</att> attribute),
then each value must be subsumed by the <gi>vRange</gi>.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">fs, vAlt, 원형 값의 형태로 자질에 대해 허용된 값의 범위를 정의한다; 유효한 자질 값의 경우, 명시된 범위 내에서 포섭되어야 한다; 만약  자질이 (org 속성에 의해 확인된) 다중 값을 포함한다면, 각 값은 vRange 내에서 포섭되어야 한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">定義有效功能值的範圍，使用fs、vAlt、或原始值格式；一個有效的功能值必須包含在指定範圍之內；若<gi>f</gi>包含多個值 (由屬性<att>org</att>所認可)，則每個值皆必須以<gi>vRange</gi>納入。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素<gi>fs</gi>、<gi>vAlt</gi>で示される素性値の範囲を定義する。要素
  <gi>f</gi>の妥当な値は、その範囲内になければならない。要素<gi>f</gi>
  が複数の値をとる場合(属性orgがそれを認めている時)、各値は当該要素
  <gi>vRange</gi>が示す範囲内になければならない。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">définit la plage de valeurs autorisées pour un
    trait, sous la forme d'un <gi>fs</gi>, <gi>vAlt</gi>, ou d'une valeur primitive ; pour que la valeur d'un élément <gi>f</gi>
      soit valide, elle doit être englobée dans la plage spécifiée. Si le <gi>f</gi> contient des valeurs
    multiples (comme prévu par l'attribut <att>org</att>), chacune des valeurs doit être englobée dans
    l'élément <gi>vRange</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">define la gama de valores posibles para un rasgo, en forma de una estructura de rasgo, vAlt, o valor primitivo;  para que el valor de un rasgo sea válido, este debe ser incluido en la gama especificada; si el rasgo contiene valores múltiples (como restringidos por el atributo org), entonces cada valor debe ser incluido por el vRange.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori ammessi per un tratto, sotto forma di un fs, di un vAlt, o di valore primitivo; affinché il valore di un f sia valido deve essere
    sussunto dalla gamma specificata; se f contiene valori multipli (come sancito dall'attributo org) allora ogni valore deve essere sussunto da vRange.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <classRef key="model.featureVal"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vRange-egXML-ti">
      <fDecl name="INV">
        <fDescr>inverted sentence</fDescr>
        <vRange>
          <vAlt>
            <binary value="true"/>
            <binary value="false"/>
          </vAlt>
        </vRange>
        <vDefault>
          <binary value="false"/>
        </vDefault>
      </fDecl>
    </egXML>
  </exemplum>
  <remarks ident="vRange-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain any legal feature-value specification.</p>
    <p/>
  </remarks>
  <remarks ident="vRange-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir n'importe quelle spécification trait-valeur admise.</p>
  </remarks>
  <remarks ident="vRange-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    正しい素性値規定を含むかもしれない。
    </p>
  </remarks>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">value range</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">값의 범위</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">功能值範圍</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">gamme de valeurs</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">gama de valores</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">gamma di valori</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">defines the range of allowed values for a feature, in the form of
an <gi>fs</gi>, <gi>vAlt</gi>, or primitive value;
for the value of an <gi>f</gi> to be valid, it must be
subsumed by the specified range; if the <gi>f</gi>
contains multiple values (as sanctioned by the <att>org</att> attribute),
then each value must be subsumed by the <gi>vRange</gi>.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">fs, vAlt, 원형 값의 형태로 자질에 대해 허용된 값의 범위를 정의한다; 유효한 자질 값의 경우, 명시된 범위 내에서 포섭되어야 한다; 만약  자질이 (org 속성에 의해 확인된) 다중 값을 포함한다면, 각 값은 vRange 내에서 포섭되어야 한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">定義有效功能值的範圍，使用fs、vAlt、或原始值格式；一個有效的功能值必須包含在指定範圍之內；若<gi>f</gi>包含多個值 (由屬性<att>org</att>所認可)，則每個值皆必須以<gi>vRange</gi>納入。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素<gi>fs</gi>、<gi>vAlt</gi>で示される素性値の範囲を定義する。要素
  <gi>f</gi>の妥当な値は、その範囲内になければならない。要素<gi>f</gi>
  が複数の値をとる場合(属性orgがそれを認めている時)、各値は当該要素
  <gi>vRange</gi>が示す範囲内になければならない。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">définit la plage de valeurs autorisées pour un
    trait, sous la forme d'un <gi>fs</gi>, <gi>vAlt</gi>, ou d'une valeur primitive ; pour que la valeur d'un élément <gi>f</gi>
      soit valide, elle doit être englobée dans la plage spécifiée. Si le <gi>f</gi> contient des valeurs
    multiples (comme prévu par l'attribut <att>org</att>), chacune des valeurs doit être englobée dans
    l'élément <gi>vRange</gi>.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">define la gama de valores posibles para un rasgo, en forma de una estructura de rasgo, vAlt, o valor primitivo;  para que el valor de un rasgo sea válido, este debe ser incluido en la gama especificada; si el rasgo contiene valores múltiples (como restringidos por el atributo org), entonces cada valor debe ser incluido por el vRange.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">definisce la gamma di valori ammessi per un tratto, sotto forma di un fs, di un vAlt, o di valore primitivo; affinché il valore di un f sia valido deve essere
    sussunto dalla gamma specificata; se f contiene valori multipli (come sancito dall'attributo org) allora ogni valore deve essere sussunto da vRange.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.featureVal"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-vRange-egXML-ti">
      <fDecl name="INV">
        <fDescr>inverted sentence</fDescr>
        <vRange>
          <vAlt>
            <binary value="true"/>
            <binary value="false"/>
          </vAlt>
        </vRange>
        <vDefault>
          <binary value="false"/>
        </vDefault>
      </fDecl>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="vRange-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain any legal feature-value specification.</p>
    <p/>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="vRange-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir n'importe quelle spécification trait-valeur admise.</p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="vRange-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    正しい素性値規定を含むかもしれない。
    </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b20

