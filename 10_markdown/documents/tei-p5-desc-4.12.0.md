---
type: representation
source-type: document
source: '[[00_sources/tei-p5-desc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 desc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/desc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# desc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8049. Git blob: `d7700949b6e6a880fb2c8b93effcae047f078f87`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-desc" ident="desc">
  <gloss versionDate="2005-01-14" xml:lang="en">description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">描述</gloss>
  <gloss versionDate="2024-09-05" xml:lang="ja">説明</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">descripción</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">descrizione</gloss>
  <gloss versionDate="2008-12-09" xml:lang="fr">description</gloss>
  <gloss versionDate="2017-06-04" xml:lang="de">Beschreibung</gloss>
  <desc versionDate="2021-03-15" xml:lang="en">contains a short description of the purpose, function, or
    use of its parent element,
    or when the parent is a documentation element, describes or defines the object being documented. 
   <!--Alternate: provides a short description of that which its parent element represents or documents.-->
  </desc>
  <desc versionDate="2007-12-20" xml:lang="ko">요소, 속성, 또는 속성 값의 목적과 적용에 대한 간단한 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一段簡短描述，說明一元素、屬性、或屬性值的應用與目的。</desc>
  <desc versionDate="2024-09-05" xml:lang="ja">この要素の親要素（典型的には記述的要素やエンティティ）によって記述されるオブジェクトの簡単な説明（を含む）</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une courte description de l'objet documenté par
    son élément parent, qui comprend son utilisation prévue, son but, ou son application là où c'est
    approprié.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una breve descripción del objetivo y la
    aplicación de un elemento, atributo o valor de un atributo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una breve descrizione dello scopo o
    dell'applicazione di un elemento, attributo, o valore di attributo.</desc>
  <desc versionDate="2017-06-04" xml:lang="de">enthält eine kurze
  Beschreibung des Objekts, das von seinem übergeordneten Element
  annotiert wird, üblicherweise einem Dokumentationselement oder einer
  Einheit.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.translatable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.descLike"/>
    <memberOf key="model.labelLike"/>
  </classes>
  <content>
    <macroRef key="macro.limitedContent"/>
  </content>
  <constraintSpec ident="deprecationInfo-only-in-deprecated" scheme="schematron" xml:lang="en">
    <desc versionDate="2018-09-13" xml:lang="en">A <gi>desc</gi> with
    a <att>type</att> of <val>deprecationInfo</val> should only occur
    when its parent element is being deprecated. Furthermore, it
    should always occur in an element that is being deprecated when
    <gi>desc</gi> is a valid child of that element.</desc>
    <constraint>
      <sch:rule context="tei:desc[ @type eq 'deprecationInfo']">
        <sch:assert test="../@validUntil">Information about a
        deprecation should only be present in a specification element
        that is being deprecated: that is, only an element that has a
        @validUntil attribute should have a child &lt;desc
        type="deprecationInfo"&gt;.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="type" mode="change">
      <valList type="semi">
        <valItem ident="deprecationInfo">
          <gloss versionDate="2018-09-14" xml:lang="en">deprecation
          information</gloss>
          <desc versionDate="2018-09-14" xml:lang="en">This element
          describes why or how its parent element is being deprecated,
          typically including recommendations for alternate
          encoding.</desc>
        </valItem>
      </valList>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-ue">
           <dataSpec module="tei" ident="teidata.point" validUntil="2050-02-25">
            <desc type="deprecationInfo" versionDate="2018-09-14" xml:lang="en">Several standards bodies, including NIST in the USA,
            strongly recommend against ending the representation of a number
            with a decimal point. So instead of <q>3.</q> use either <q>3</q>
            or <q>3.0</q>.</desc>
            <!-- ... -->
         </dataSpec>
        </egXML>
      </exemplum>
    </attDef>
  </attList>
  <exemplum versionDate="2021-03-15" xml:lang="en">
    <p>Example of a <gi>desc</gi> element inside a documentation element.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-zo" source="#SELF">
      <dataSpec module="tei" ident="teidata.point">
        <desc versionDate="2010-10-17" xml:lang="en">defines the data type used to express a point in cartesian space.</desc>
        <content>
          <dataRef name="token" restriction="(-?[0-9]+(\.[0-9]+)?,-?[0-9]+(\.[0-9]+)?)"/>
        </content>
        <!-- ... -->
      </dataSpec>
    </egXML>
  </exemplum>
  <exemplum versionDate="2021-03-15" xml:lang="en">
    <p>Example of a <gi>desc</gi> element in a non-documentation element.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-up" source="#SELF"> 
        <place xml:id="KERG2">
          <placeName>Kerguelen Islands</placeName>
          <!-- ... -->
          <terrain>
            <desc>antarctic tundra</desc>
          </terrain>
          <!-- ... -->
        </place>
      </egXML> 
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-xh">
      <desc>contient une description brève de la raison d'être et du champ d'application d'un
          élément, d'un attribut ou de la valeur d'un attribut, d'une classe ou une entité.</desc>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-cm">
      <desc>包含某個元素或屬性之定義與用法的簡短描述。</desc>
    </egXML>
  </exemplum>
  <remarks ident="desc-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">When used in a specification element such as <gi>elementSpec</gi>, TEI convention requires that this be expressed as a finite clause, begining
      with an active verb.</p>
  </remarks>
  <remarks ident="desc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">La convention TEI exige que cela soit exprimé sous la  forme d'une proposition finie,
      introduite  par un verbe actif.</p>
  </remarks>
  <remarks ident="desc-remarks" versionDate="2008-04-06" xml:lang="es">
    <p rend="dataDesc">La convención de TEI requiere que esto esté expresado como cláusula finita,
      comenzando con un verbo activo.</p>
  </remarks>
  <remarks ident="desc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> TEIの慣習では、動詞を先頭にした文で表現される(訳注：英語で表現する 場合のこと)。 </p>
  </remarks>
  <remarks ident="desc-remarks" versionDate="2017-06-04" xml:lang="de">
    <p rend="dataDesc">Wenn die Beschreibung innerhalb eines Spezifikationselements wie zum Beispiel
      <gi>elementSpec</gi> verwendet wird, empfiehlt die TEI, dass diese durch einen vollständigen
      Satz ausgedrückt wird, der mit einem Verb im Aktiv beginnt.</p>
  </remarks>
  <listRef>
    <ptr target="#TDcrystalsCEdc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">기술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">描述</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2024-09-05" xml:lang="ja">説明</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">descripción</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">descrizione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2008-12-09" xml:lang="fr">description</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2017-06-04" xml:lang="de">Beschreibung</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2021-03-15" xml:lang="en">contains a short description of the purpose, function, or
    use of its parent element,
    or when the parent is a documentation element, describes or defines the object being documented. 
   <!--Alternate: provides a short description of that which its parent element represents or documents.-->
  </desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">요소, 속성, 또는 속성 값의 목적과 적용에 대한 간단한 기술을 포함한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一段簡短描述，說明一元素、屬性、或屬性值的應用與目的。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2024-09-05" xml:lang="ja">この要素の親要素（典型的には記述的要素やエンティティ）によって記述されるオブジェクトの簡単な説明（を含む）</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une courte description de l'objet documenté par
    son élément parent, qui comprend son utilisation prévue, son but, ou son application là où c'est
    approprié.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una breve descripción del objetivo y la
    aplicación de un elemento, atributo o valor de un atributo.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una breve descrizione dello scopo o
    dell'applicazione di un elemento, attributo, o valore di attributo.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-04" xml:lang="de">enthält eine kurze
  Beschreibung des Objekts, das von seinem übergeordneten Element
  annotiert wird, üblicherweise einem Dokumentationselement oder einer
  Einheit.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.translatable"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.descLike"/>
    <memberOf key="model.labelLike"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.limitedContent"/>
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="deprecationInfo-only-in-deprecated" scheme="schematron" xml:lang="en">
    <desc versionDate="2018-09-13" xml:lang="en">A <gi>desc</gi> with
    a <att>type</att> of <val>deprecationInfo</val> should only occur
    when its parent element is being deprecated. Furthermore, it
    should always occur in an element that is being deprecated when
    <gi>desc</gi> is a valid child of that element.</desc>
    <constraint>
      <sch:rule context="tei:desc[ @type eq 'deprecationInfo']">
        <sch:assert test="../@validUntil">Information about a
        deprecation should only be present in a specification element
        that is being deprecated: that is, only an element that has a
        @validUntil attribute should have a child &lt;desc
        type="deprecationInfo"&gt;.</sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="deprecationInfo">
          <gloss versionDate="2018-09-14" xml:lang="en">deprecation
          information</gloss>
          <desc versionDate="2018-09-14" xml:lang="en">This element
          describes why or how its parent element is being deprecated,
          typically including recommendations for alternate
          encoding.</desc>
        </valItem>
      </valList>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-ue">
           <dataSpec module="tei" ident="teidata.point" validUntil="2050-02-25">
            <desc type="deprecationInfo" versionDate="2018-09-14" xml:lang="en">Several standards bodies, including NIST in the USA,
            strongly recommend against ending the representation of a number
            with a decimal point. So instead of <q>3.</q> use either <q>3</q>
            or <q>3.0</q>.</desc>
            <!-- ... -->
         </dataSpec>
        </egXML>
      </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2021-03-15" xml:lang="en">
    <p>Example of a <gi>desc</gi> element inside a documentation element.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-zo" source="#SELF">
      <dataSpec module="tei" ident="teidata.point">
        <desc versionDate="2010-10-17" xml:lang="en">defines the data type used to express a point in cartesian space.</desc>
        <content>
          <dataRef name="token" restriction="(-?[0-9]+(\.[0-9]+)?,-?[0-9]+(\.[0-9]+)?)"/>
        </content>
        <!-- ... -->
      </dataSpec>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2021-03-15" xml:lang="en">
    <p>Example of a <gi>desc</gi> element in a non-documentation element.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-up" source="#SELF"> 
        <place xml:id="KERG2">
          <placeName>Kerguelen Islands</placeName>
          <!-- ... -->
          <terrain>
            <desc>antarctic tundra</desc>
          </terrain>
          <!-- ... -->
        </place>
      </egXML> 
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-xh">
      <desc>contient une description brève de la raison d'être et du champ d'application d'un
          élément, d'un attribut ou de la valeur d'un attribut, d'une classe ou une entité.</desc>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-desc-egXML-cm">
      <desc>包含某個元素或屬性之定義與用法的簡短描述。</desc>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="desc-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">When used in a specification element such as <gi>elementSpec</gi>, TEI convention requires that this be expressed as a finite clause, begining
      with an active verb.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="desc-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">La convention TEI exige que cela soit exprimé sous la  forme d'une proposition finie,
      introduite  par un verbe actif.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="desc-remarks" versionDate="2008-04-06" xml:lang="es">
    <p rend="dataDesc">La convención de TEI requiere que esto esté expresado como cláusula finita,
      comenzando con un verbo activo.</p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="desc-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> TEIの慣習では、動詞を先頭にした文で表現される(訳注：英語で表現する 場合のこと)。 </p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/remarks[5]`.

```xml
<remarks ident="desc-remarks" versionDate="2017-06-04" xml:lang="de">
    <p rend="dataDesc">Wenn die Beschreibung innerhalb eines Spezifikationselements wie zum Beispiel
      <gi>elementSpec</gi> verwendet wird, empfiehlt die TEI, dass diese durch einen vollständigen
      Satz ausgedrückt wird, der mit einem Verb im Aktiv beginnt.</p>
  </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDcrystalsCEdc"/>
  </listRef>
```

^b31

