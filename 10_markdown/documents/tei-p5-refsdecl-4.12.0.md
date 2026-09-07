---
type: representation
source-type: document
source: '[[00_sources/tei-p5-refsdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 refsDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/refsDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# refsDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5719. Git blob: `3dd3414515a4433657442156c42c3070019a60bb`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-refsDecl" ident="refsDecl">
  <gloss versionDate="2005-01-14" xml:lang="en">references declaration</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">Déclaration du système de références</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">참조 선언</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">參照宣告</gloss>
    <gloss versionDate="2016-11-17" xml:lang="de">Angabe der Referenzstruktur</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">declaración de referencias</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sui riferimenti</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">specifies how canonical references are constructed for this
  text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">précise la manière dont les références canoniques ont été construites pour ce texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">표준 참조가 이러한 텍스트에 대해 어떻게 구성되는가를 명시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標明本文件與某一個權威參照標準的關係。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">標準的な参照の作られ方を示す。</desc>
    <desc versionDate="2016-11-17" xml:lang="de">beschreibt, wie Standardreferenzen für diesen Text aufgebaut sind.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica cómo se han formado las referencias canónicas para este texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">specifica in che modo siano costruiti i riferimenti canonici per il testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="citeStructure" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="cRefPattern" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="refState" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
  <constraintSpec ident="refsDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:refsDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-mx" source="#UND">
      <refsDecl>
        <cRefPattern matchPattern="([A-Za-z0-9]+) ([0-9]+):([0-9]+)" replacementPattern="#xpath(//body/div[@n='$1']/div[$2]/div3[$3])"/>
      </refsDecl>
    </egXML>
    <p>This example is a formal representation for the referencing
    scheme described informally in the following example.</p>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-yw" source="#UND">
      <refsDecl>
        <cRefPattern matchPattern="([A-Za-z0-9]+) ([0-9]+):([0-9]+)" replacementPattern="#xpath(//body/div[@n='$1']/div[$2]/div3[$3])"/>
      </refsDecl>
    </egXML>
    <p>Dieses Beispiel ist eine formale Repräsentation für das im folgenden Beispiel informell
      beschriebene Referenzierungsschema.</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-vk">
      <refsDecl xml:id="fr_ASLREF">
        <cRefPattern matchPattern="(\S+) ([^.]+)\.(.*)" replacementPattern="#fr_xpath(//div1[@n='$1']/div2/[@n='$2']//lb[@n='$3'])">
          <p>Une référence a été créée en assemblant les éléments suivants dans l'ordre inverse de
              la liste qui suit : <list><item>la valeur <att>n</att> du précédent <gi>lb</gi>
                     </item><item>une période</item><item>la valeur <att>n</att> de l'ancêtre <gi>div2</gi>
                     </item><item>un espace</item><item>la valeur<att>n</att> du parent <gi>div1</gi>
                     </item></list>
               </p>
        </cRefPattern>
      </refsDecl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-go">
      <refsDecl>
        <p>參照是將位於最高層級的<gi>div</gi>元素的屬性<att>n</att>值串聯起來，
              其後跟著空格和續接的下一層級<gi>div</gi>，接著冒點，
              然後是續接的下一(最低) 層級的<gi>div</gi>所組成。</p>
      </refsDecl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-qq">
      <refsDecl>
        <p>References are made up by concatenating the value for the
        <att>n</att> attribute on the highest level <gi>div</gi>
        element, followed by a space, followed by the sequential
        number of the next level <gi>div</gi> followed by a colon
        followed by the sequential number of the next (and lowest)
        level <gi>div</gi>.</p>
      </refsDecl>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD54M"/>
    <ptr target="#HD5"/>
    <ptr target="#HD54"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">references declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">Déclaration du système de références</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">참조 선언</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">參照宣告</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2016-11-17" xml:lang="de">Angabe der Referenzstruktur</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">declaración de referencias</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">dichiarazione sui riferimenti</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies how canonical references are constructed for this
  text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">précise la manière dont les références canoniques ont été construites pour ce texte.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표준 참조가 이러한 텍스트에 대해 어떻게 구성되는가를 명시한다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明本文件與某一個權威參照標準的關係。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">標準的な参照の作られ方を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">beschreibt, wie Standardreferenzen für diesen Text aufgebaut sind.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica cómo se han formado las referencias canónicas para este texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica in che modo siano costruiti i riferimenti canonici per il testo.</desc>
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
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="citeStructure" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="cRefPattern" minOccurs="1" maxOccurs="unbounded"/>
      <elementRef key="refState" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="refsDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:refsDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-mx" source="#UND">
      <refsDecl>
        <cRefPattern matchPattern="([A-Za-z0-9]+) ([0-9]+):([0-9]+)" replacementPattern="#xpath(//body/div[@n='$1']/div[$2]/div3[$3])"/>
      </refsDecl>
    </egXML>
    <p>This example is a formal representation for the referencing
    scheme described informally in the following example.</p>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-yw" source="#UND">
      <refsDecl>
        <cRefPattern matchPattern="([A-Za-z0-9]+) ([0-9]+):([0-9]+)" replacementPattern="#xpath(//body/div[@n='$1']/div[$2]/div3[$3])"/>
      </refsDecl>
    </egXML>
    <p>Dieses Beispiel ist eine formale Repräsentation für das im folgenden Beispiel informell
      beschriebene Referenzierungsschema.</p>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-vk">
      <refsDecl xml:id="fr_ASLREF">
        <cRefPattern matchPattern="(\S+) ([^.]+)\.(.*)" replacementPattern="#fr_xpath(//div1[@n='$1']/div2/[@n='$2']//lb[@n='$3'])">
          <p>Une référence a été créée en assemblant les éléments suivants dans l'ordre inverse de
              la liste qui suit : <list><item>la valeur <att>n</att> du précédent <gi>lb</gi>
                     </item><item>une période</item><item>la valeur <att>n</att> de l'ancêtre <gi>div2</gi>
                     </item><item>un espace</item><item>la valeur<att>n</att> du parent <gi>div1</gi>
                     </item></list>
               </p>
        </cRefPattern>
      </refsDecl>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-go">
      <refsDecl>
        <p>參照是將位於最高層級的<gi>div</gi>元素的屬性<att>n</att>值串聯起來，
              其後跟著空格和續接的下一層級<gi>div</gi>，接著冒點，
              然後是續接的下一(最低) 層級的<gi>div</gi>所組成。</p>
      </refsDecl>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refsDecl-egXML-qq">
      <refsDecl>
        <p>References are made up by concatenating the value for the
        <att>n</att> attribute on the highest level <gi>div</gi>
        element, followed by a space, followed by the sequential
        number of the next level <gi>div</gi> followed by a colon
        followed by the sequential number of the next (and lowest)
        level <gi>div</gi>.</p>
      </refsDecl>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD54M"/>
    <ptr target="#HD5"/>
    <ptr target="#HD54"/>
  </listRef>
```

^b24

