---
type: representation
source-type: document
source: '[[00_sources/tei-p5-text-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 text
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/text.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# text

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8815. Git blob: `fde92d9fe488c32308b13d331d19c16007d127e1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-text" ident="text">
  <gloss versionDate="2007-06-12" xml:lang="en">text</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">texte</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a single text of any kind, whether unitary or composite, for example a poem or
    drama, a collection of essays, a novel, a dictionary, or a corpus sample.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">어떤 종류의 단일 텍스트를 포함한다. 예를 들어, 시 또는 드라마, 수필선, 소설, 사전 또는 코퍼스
    표본과 같은 단일 텍스트 또는 혼합 텍스트.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一份任何種類的文本，無論是單一或複合的，例如詩詞或戲劇、散文集、小說、字典、或是文集範例。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ひとつのテキストを示す。単体でも複合体でもよい。例えば、詩、舞台芸術、 随筆、小説、辞書、コーパスなど。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un seul texte quelconque, simple ou composite,
    par exemple un poème ou une pièce de théâtre, un recueil d’essais, un roman, un dictionnaire ou
    un échantillon de corpus.</desc>
  <desc versionDate="2017-06-25" xml:lang="de">enthält einen einzelnen, eigenständigen oder kompilierten Text, zum Beispiel ein Gedicht oder
    Drama, eine Sammlung von Aufsätzen, einen Roman, ein Wörterbuch oder ein Korpus-Sample.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un único texto de cualquier tipo, sea este
    unitario o combinado, p.ej. un texto en verso o teatral, una recopilación de ensayos, una
    novela, un diccionario, o una fragmento de corpus.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un unico testo di qualsiasi tipo, sia esso
    unitario o composito, per esempio un testo in versi o teatrale, una raccolta di saggi, un
    romanzo, un dizionario, o una porzione di corpus</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.resource"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <sequence minOccurs="0">
        <elementRef key="front"/>
	<classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <alternate>
        <elementRef key="body"/>
        <elementRef key="group"/>
      </alternate>
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <sequence minOccurs="0">
        <elementRef key="back"/>
	<classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-oq" source="#lowellAut">
      <text>
        <front>
          <docTitle>
            <titlePart>Autumn Haze</titlePart>
          </docTitle>
        </front>
        <body>
          <l>Is it a dragonfly or a maple leaf</l>
          <l>That settles softly down upon the water?</l>
        </body>
      </text>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-ro" source="#fr-ex-Hugo-Nuit">
      <text>
        <front>
          <docTitle>
            <titlePart>Souvenir de la nuit du 4</titlePart>
          </docTitle>
        </front>
        <body>
          <l>Il avait dans sa poche une toupie en buis.</l>
        </body>
      </text>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p>Le <gi>body</gi> d'un texte peut être remplacé par un groupe de textes enchâssés, comme
        dans la structure suivante : </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-dm" valid="feasible" source="#UND">
      <TEI>
        <teiHeader>
          <!--[ en-tête du texte composite ]-->
        </teiHeader>
        <text>
          <front>
            <!--[ partie préfatoire du texte composite  ]-->
          </front>
          <group>
            <text>
              <front>
                <!--[ partie préfatoire du premier texte ]-->
              </front>
              <body>
                <!--[ corps  du premier texte ]-->
              </body>
              <back>
                <!--[ annexe  du premier texte ]-->
              </back>
            </text>
            <text>
              <front>
                <!--[ partie préfatoire du deuxième texte ]-->
              </front>
              <body>
                <!--[ corps du deuxième texte ]-->
              </body>
              <back>
                <!--[ annex du deuxième texte ]-->
              </back>
            </text>
            <!--[ encore de textes, simples ou composites  ]-->
          </group>
          <back>
            <!--[ annex du texte composite  ]-->
          </back>
        </text>
      </TEI>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-sd" source="#biblzh-tw_n59">
      <text>
        <front>
          <docTitle>
            <titlePart>憶江南</titlePart>
          </docTitle>
        </front>
        <body>
          <l>江南好，</l>
          <l>風景舊曾諳。</l>
          <l>日出江花紅胜火，</l>
          <l>春來江水綠如藍，</l>
          <l>能不憶江南。</l>
        </body>
      </text>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>The body of a text may be replaced by a group of nested texts, as in the following schematic:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-pe" valid="feasible" source="#UND">
      <text>
        <front>
          <!-- front matter for the whole group -->
        </front>
        <group>
          <text>
            <!-- first text -->
          </text>
          <text>
            <!-- second text -->
          </text>
        </group>
      </text>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Der Textkörper kann durch eine Gruppierung von verschachtelten Texten ersetzt werden, wie das folgende Beispiel zeigt:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-wv" valid="feasible" source="#UND">
      <text>
        <front>
          <!-- Vorspann für die gesamte Gruppierung -->
        </front>
        <group>
          <text>
            <!-- erster Text -->
          </text>
          <text>
            <!-- zweiter Text -->
          </text>
        </group>
      </text>
    </egXML>
  </exemplum>
  <remarks ident="text-remarks" versionDate="2007-03-30" xml:lang="en">
    <p>This element should not be used to represent a text which is inserted at an arbitrary point
      within the structure of another, for example as in an embedded or quoted narrative; the
        <gi>floatingText</gi> is provided for this purpose.</p>
  </remarks>
  <remarks ident="text-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément ne devrait pas être utilisé pour encoder un texte inséré à un endroit non
      prévisible à l'intérieur de la structure d'un autre texte, comme par exemple dans un récit qui est enchâssé 
    ou cité dans un autre ; c'est l'élément <gi>floatingText</gi> qui doit être utilisé à
      cet effet.</p>
  </remarks>
  <remarks ident="text-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素は、別の構造中、例えば引用された語りの任意の場所に挿入され るテキストを示すためには使うべきではない。この場合は、要素 <gi>floatingText</gi>が使われる。
    </p>
  </remarks>
  <remarks ident="text-remarks" versionDate="2017-06-25" xml:lang="de">
    <p>Dieses Element sollte nicht benutzt werden, um einen Text wiederzugeben, der an irgendeiner
      Stelle in einer anderen Struktur eingefügt ist, wie z. B. eine eingebettete oder zitierte
      Erzählung. Für diesen Zweck wird das Element <gi>floatingText</gi> benutzt.</p>
  </remarks>
  <listRef>
    <ptr target="#DS"/>
    <ptr target="#CCDEF"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">text</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">texte</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a single text of any kind, whether unitary or composite, for example a poem or
    drama, a collection of essays, a novel, a dictionary, or a corpus sample.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">어떤 종류의 단일 텍스트를 포함한다. 예를 들어, 시 또는 드라마, 수필선, 소설, 사전 또는 코퍼스
    표본과 같은 단일 텍스트 또는 혼합 텍스트.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一份任何種類的文本，無論是單一或複合的，例如詩詞或戲劇、散文集、小說、字典、或是文集範例。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ひとつのテキストを示す。単体でも複合体でもよい。例えば、詩、舞台芸術、 随筆、小説、辞書、コーパスなど。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un seul texte quelconque, simple ou composite,
    par exemple un poème ou une pièce de théâtre, un recueil d’essais, un roman, un dictionnaire ou
    un échantillon de corpus.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-25" xml:lang="de">enthält einen einzelnen, eigenständigen oder kompilierten Text, zum Beispiel ein Gedicht oder
    Drama, eine Sammlung von Aufsätzen, einen Roman, ein Wörterbuch oder ein Korpus-Sample.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un único texto de cualquier tipo, sea este
    unitario o combinado, p.ej. un texto en verso o teatral, una recopilación de ensayos, una
    novela, un diccionario, o una fragmento de corpus.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un unico testo di qualsiasi tipo, sia esso
    unitario o composito, per esempio un testo in versi o teatrale, una raccolta di saggi, un
    romanzo, un dizionario, o una porzione di corpus</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.resource"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <sequence minOccurs="0">
        <elementRef key="front"/>
	<classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
      <alternate>
        <elementRef key="body"/>
        <elementRef key="group"/>
      </alternate>
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <sequence minOccurs="0">
        <elementRef key="back"/>
	<classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-oq" source="#lowellAut">
      <text>
        <front>
          <docTitle>
            <titlePart>Autumn Haze</titlePart>
          </docTitle>
        </front>
        <body>
          <l>Is it a dragonfly or a maple leaf</l>
          <l>That settles softly down upon the water?</l>
        </body>
      </text>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-ro" source="#fr-ex-Hugo-Nuit">
      <text>
        <front>
          <docTitle>
            <titlePart>Souvenir de la nuit du 4</titlePart>
          </docTitle>
        </front>
        <body>
          <l>Il avait dans sa poche une toupie en buis.</l>
        </body>
      </text>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p>Le <gi>body</gi> d'un texte peut être remplacé par un groupe de textes enchâssés, comme
        dans la structure suivante : </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-dm" valid="feasible" source="#UND">
      <TEI>
        <teiHeader>
          <!--[ en-tête du texte composite ]-->
        </teiHeader>
        <text>
          <front>
            <!--[ partie préfatoire du texte composite  ]-->
          </front>
          <group>
            <text>
              <front>
                <!--[ partie préfatoire du premier texte ]-->
              </front>
              <body>
                <!--[ corps  du premier texte ]-->
              </body>
              <back>
                <!--[ annexe  du premier texte ]-->
              </back>
            </text>
            <text>
              <front>
                <!--[ partie préfatoire du deuxième texte ]-->
              </front>
              <body>
                <!--[ corps du deuxième texte ]-->
              </body>
              <back>
                <!--[ annex du deuxième texte ]-->
              </back>
            </text>
            <!--[ encore de textes, simples ou composites  ]-->
          </group>
          <back>
            <!--[ annex du texte composite  ]-->
          </back>
        </text>
      </TEI>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-sd" source="#biblzh-tw_n59">
      <text>
        <front>
          <docTitle>
            <titlePart>憶江南</titlePart>
          </docTitle>
        </front>
        <body>
          <l>江南好，</l>
          <l>風景舊曾諳。</l>
          <l>日出江花紅胜火，</l>
          <l>春來江水綠如藍，</l>
          <l>能不憶江南。</l>
        </body>
      </text>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="en">
    <p>The body of a text may be replaced by a group of nested texts, as in the following schematic:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-pe" valid="feasible" source="#UND">
      <text>
        <front>
          <!-- front matter for the whole group -->
        </front>
        <group>
          <text>
            <!-- first text -->
          </text>
          <text>
            <!-- second text -->
          </text>
        </group>
      </text>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Der Textkörper kann durch eine Gruppierung von verschachtelten Texten ersetzt werden, wie das folgende Beispiel zeigt:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-text-egXML-wv" valid="feasible" source="#UND">
      <text>
        <front>
          <!-- Vorspann für die gesamte Gruppierung -->
        </front>
        <group>
          <text>
            <!-- erster Text -->
          </text>
          <text>
            <!-- zweiter Text -->
          </text>
        </group>
      </text>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="text-remarks" versionDate="2007-03-30" xml:lang="en">
    <p>This element should not be used to represent a text which is inserted at an arbitrary point
      within the structure of another, for example as in an embedded or quoted narrative; the
        <gi>floatingText</gi> is provided for this purpose.</p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="text-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément ne devrait pas être utilisé pour encoder un texte inséré à un endroit non
      prévisible à l'intérieur de la structure d'un autre texte, comme par exemple dans un récit qui est enchâssé 
    ou cité dans un autre ; c'est l'élément <gi>floatingText</gi> qui doit être utilisé à
      cet effet.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="text-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素は、別の構造中、例えば引用された語りの任意の場所に挿入され るテキストを示すためには使うべきではない。この場合は、要素 <gi>floatingText</gi>が使われる。
    </p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="text-remarks" versionDate="2017-06-25" xml:lang="de">
    <p>Dieses Element sollte nicht benutzt werden, um einen Text wiederzugeben, der an irgendeiner
      Stelle in einer anderen Struktur eingefügt ist, wie z. B. eine eingebettete oder zitierte
      Erzählung. Für diesen Zweck wird das Element <gi>floatingText</gi> benutzt.</p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DS"/>
    <ptr target="#CCDEF"/>
  </listRef>
```

^b23

