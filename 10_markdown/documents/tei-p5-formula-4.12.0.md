---
type: representation
source-type: document
source: '[[00_sources/tei-p5-formula-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 formula
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/formula.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# formula

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2781. Git blob: `3dcb031a284d8710ca0293c40595a7023602250e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="figures" xml:id="gi-formula" ident="formula">
  <gloss versionDate="2007-06-12" xml:lang="en">formula</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">formule</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Formel</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a mathematical or other formula.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">수식 또는 다른 식을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含數學或其他方程式。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">数式を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une formule mathématique ou tout autre type de formule.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula matemática o de otro tipo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una formula matematica o di altra natura.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält eine mathematische oder andere Formel.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="model.graphicLike"/>
  </classes>
  <content>
       <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.graphicLike"/>
        <classRef key="model.hiLike"/>       
      </alternate>  
  </content>

  
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-formula-egXML-vc">
      <formula notation="tex">$E=mc^2$</formula>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-formula-egXML-fc">
      <formula notation="none">E=mc<hi rend="sup">2</hi>
         </formula>
    </egXML>
  </exemplum>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-formula-egXML-wy">
      <formula notation="mathml">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <mi>E</mi>
          <mo>=</mo>
          <mi>m</mi>
          <msup>
            <mrow>
              <mi>c</mi>
            </mrow>
            <mrow>
              <mn>2</mn>
            </mrow>
          </msup>
        </math>
      </formula>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#FTFOR" type="div1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">formula</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">formule</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Formel</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a mathematical or other formula.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">수식 또는 다른 식을 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含數學或其他方程式。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">数式を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une formule mathématique ou tout autre type de formule.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una fórmula matemática o de otro tipo.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una formula matematica o di altra natura.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält eine mathematische oder andere Formel.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.notated"/>
    <memberOf key="model.graphicLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
       <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.graphicLike"/>
        <classRef key="model.hiLike"/>       
      </alternate>  
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-formula-egXML-vc">
      <formula notation="tex">$E=mc^2$</formula>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-formula-egXML-fc">
      <formula notation="none">E=mc<hi rend="sup">2</hi>
         </formula>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-formula-egXML-wy">
      <formula notation="mathml">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <mi>E</mi>
          <mo>=</mo>
          <mi>m</mi>
          <msup>
            <mrow>
              <mi>c</mi>
            </mrow>
            <mrow>
              <mn>2</mn>
            </mrow>
          </msup>
        </math>
      </formula>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FTFOR" type="div1"/>
  </listRef>
```

^b17

