---
type: representation
source-type: document
source: '[[00_sources/tei-p5-cit-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 cit
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/cit.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# cit

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7245. Git blob: `84634c2747d28f3a3340e6f18cf3a89c8abbde6a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-cit" ident="cit">
  <gloss versionDate="2007-07-04" xml:lang="en">cited quotation</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">참조 인용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">cita</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">citation</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">citazione</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Zitat mit Referenz</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">引用内容</gloss>
  <desc versionDate="2007-09-23" xml:lang="en">contains a quotation from some other document, together with a bibliographic reference to
    its source. In a dictionary it may contain an example text with at least one occurrence of the
    word form, used in the sense being described, or a translation of the headword, or an example.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원문 참고문헌과 함께 제시된 다른 문서로부터의 인용을 포함한다. 사전에서는 기술된 의미로 사용된 어형이
    들어간 용례, 또는 표제어의 번역어 또는 예문을 포함할 수 있다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">從其他文件中引用的內容，並包含引用來源的書目參照資料。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">書誌参照を伴い、他の文書からの引用を示す。例えば、辞書の場合には、
    当該単語形が出現する例文を示したり、当該見出し語の翻訳や用例を示した りする。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">citation provenant d'un autre document comprenant la
    référence bibliographique de sa source. Dans un dictionnaire il peut contenir un exemple avec au
    moins une occurrence du mot employé dans l’acception qui est décrite, ou une traduction du
    mot-clé, ou un exemple.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">Una cita de algún otro documento junto a la referencia
    bibliográfica a la fuente.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">Un acitazione da un altro documento accompagnata da
    riferimenti bibliografici alla fonte.</desc>
    <desc versionDate="2017-06-04" xml:lang="de">enthält ein Zitat aus einem anderen Dokument, zusammen mit einer bibliografischen Referenz auf die Quelle. In einem Wörterbuch kann es ein Beispieltext mit mindestens einem Vorkommen der Wortform enthalten, 
        welches in dem beschriebenen Sinne verwendet wird, oder eine Übersetzung des Lemmas, oder ein Beispiel.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart.top"/>
    <memberOf key="model.quoteLike"/>
  </classes>
  <content>
    
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.biblLike"/>
        <classRef key="model.egLike"/>
        <classRef key="model.entryPart"/>
        <classRef key="model.global"/>
        <classRef key="model.graphicLike"/>
        <classRef key="model.ptrLike"/>
        <classRef key="model.attributable"/>
        <elementRef key="pc"/>
        <elementRef key="q"/>
      </alternate>
    
    <!-- if we make it model.entryPart.top, then eg <gen> isnt allowd -->
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-ph" source="#DSHD-eg-30">
      <cit>
        <quote>and the breath of the whale is frequently attended with such an insupportable smell,
          as to bring on disorder of the brain.</quote>
        <bibl>Ulloa's South America</bibl>
      </cit>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-oi" source="#fr-ex-Perec-vie">
      <cit>
        <quote>Regarde de tous tes yeux, regarde</quote>
        <bibl>Jules Verne, Michel Strogof</bibl>
      </cit>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-pi">
      <entry>
        <form>
          <orth>to horrify</orth>
        </form>
        <cit type="translation" xml:lang="en">
          <quote>horrifier</quote>
        </cit>
        <cit type="example">
          <quote>she was horrified at the expense.</quote>
          <cit type="translation" xml:lang="en">
            <quote>elle était horrifiée par la dépense.</quote>
          </cit>
        </cit>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-ih">
      <cit>
        <quote>棋開始了。上千人不再出聲兒。只有自願服務的人一會兒緊一會兒慢地用話傳出棋步，外邊兒自願服務的人就變動著棋子兒。</quote>
        <bibl>阿城，《棋王》。</bibl>
      </cit>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-sb">
      <entry>
        <form>
          <orth>horrifier</orth>
        </form>
        <cit type="translation" xml:lang="zh">
          <quote>使驚嚇</quote>
        </cit>
        <cit type="example">
          <quote>elle était horrifiée par la dépense</quote>
          <cit type="translation" xml:lang="zh">
            <quote>成本把她嚇呆了。</quote>
          </cit>
        </cit>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-sa">
      <entry>
        <form>
          <orth>horrifier</orth>
        </form>
        <cit type="translation" xml:lang="en">
          <quote>to horrify</quote>
        </cit>
        <cit type="example">
          <quote>elle était horrifiée par la dépense</quote>
          <cit type="translation" xml:lang="en">
            <quote>she was horrified at the expense.</quote>
          </cit>
        </cit>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-py">
      <cit type="example">
        <quote xml:lang="mix">Ka'an yu tsa'a Pedro.</quote>
        <media url="soundfiles-gen:S_speak_1s_on_behalf_of_Pedro_01_02_03_TS.wav" mimeType="audio/wav"/>
        <cit type="translation">
          <quote xml:lang="en">I'm speaking on behalf of Pedro.</quote>
        </cit>
        <cit type="translation">
          <quote xml:lang="es">Estoy hablando de parte de Pedro.</quote>
        </cit>
      </cit>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COHQQ"/>
    <ptr target="#DSGRP"/>
    <ptr target="#DITPEG"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">cited quotation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">참조 인용</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">cita</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">citation</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">citazione</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Zitat mit Referenz</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">引用内容</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-23" xml:lang="en">contains a quotation from some other document, together with a bibliographic reference to
    its source. In a dictionary it may contain an example text with at least one occurrence of the
    word form, used in the sense being described, or a translation of the headword, or an example.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원문 참고문헌과 함께 제시된 다른 문서로부터의 인용을 포함한다. 사전에서는 기술된 의미로 사용된 어형이
    들어간 용례, 또는 표제어의 번역어 또는 예문을 포함할 수 있다.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">從其他文件中引用的內容，並包含引用來源的書目參照資料。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">書誌参照を伴い、他の文書からの引用を示す。例えば、辞書の場合には、
    当該単語形が出現する例文を示したり、当該見出し語の翻訳や用例を示した りする。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">citation provenant d'un autre document comprenant la
    référence bibliographique de sa source. Dans un dictionnaire il peut contenir un exemple avec au
    moins une occurrence du mot employé dans l’acception qui est décrite, ou une traduction du
    mot-clé, ou un exemple.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">Una cita de algún otro documento junto a la referencia
    bibliográfica a la fuente.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">Un acitazione da un altro documento accompagnata da
    riferimenti bibliografici alla fonte.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-04" xml:lang="de">enthält ein Zitat aus einem anderen Dokument, zusammen mit einer bibliografischen Referenz auf die Quelle. In einem Wörterbuch kann es ein Beispieltext mit mindestens einem Vorkommen der Wortform enthalten, 
        welches in dem beschriebenen Sinne verwendet wird, oder eine Übersetzung des Lemmas, oder ein Beispiel.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart.top"/>
    <memberOf key="model.quoteLike"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.biblLike"/>
        <classRef key="model.egLike"/>
        <classRef key="model.entryPart"/>
        <classRef key="model.global"/>
        <classRef key="model.graphicLike"/>
        <classRef key="model.ptrLike"/>
        <classRef key="model.attributable"/>
        <elementRef key="pc"/>
        <elementRef key="q"/>
      </alternate>
    
    <!-- if we make it model.entryPart.top, then eg <gen> isnt allowd -->
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-ph" source="#DSHD-eg-30">
      <cit>
        <quote>and the breath of the whale is frequently attended with such an insupportable smell,
          as to bring on disorder of the brain.</quote>
        <bibl>Ulloa's South America</bibl>
      </cit>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-oi" source="#fr-ex-Perec-vie">
      <cit>
        <quote>Regarde de tous tes yeux, regarde</quote>
        <bibl>Jules Verne, Michel Strogof</bibl>
      </cit>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-pi">
      <entry>
        <form>
          <orth>to horrify</orth>
        </form>
        <cit type="translation" xml:lang="en">
          <quote>horrifier</quote>
        </cit>
        <cit type="example">
          <quote>she was horrified at the expense.</quote>
          <cit type="translation" xml:lang="en">
            <quote>elle était horrifiée par la dépense.</quote>
          </cit>
        </cit>
      </entry>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-ih">
      <cit>
        <quote>棋開始了。上千人不再出聲兒。只有自願服務的人一會兒緊一會兒慢地用話傳出棋步，外邊兒自願服務的人就變動著棋子兒。</quote>
        <bibl>阿城，《棋王》。</bibl>
      </cit>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-sb">
      <entry>
        <form>
          <orth>horrifier</orth>
        </form>
        <cit type="translation" xml:lang="zh">
          <quote>使驚嚇</quote>
        </cit>
        <cit type="example">
          <quote>elle était horrifiée par la dépense</quote>
          <cit type="translation" xml:lang="zh">
            <quote>成本把她嚇呆了。</quote>
          </cit>
        </cit>
      </entry>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-sa">
      <entry>
        <form>
          <orth>horrifier</orth>
        </form>
        <cit type="translation" xml:lang="en">
          <quote>to horrify</quote>
        </cit>
        <cit type="example">
          <quote>elle était horrifiée par la dépense</quote>
          <cit type="translation" xml:lang="en">
            <quote>she was horrified at the expense.</quote>
          </cit>
        </cit>
      </entry>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-cit-egXML-py">
      <cit type="example">
        <quote xml:lang="mix">Ka'an yu tsa'a Pedro.</quote>
        <media url="soundfiles-gen:S_speak_1s_on_behalf_of_Pedro_01_02_03_TS.wav" mimeType="audio/wav"/>
        <cit type="translation">
          <quote xml:lang="en">I'm speaking on behalf of Pedro.</quote>
        </cit>
        <cit type="translation">
          <quote xml:lang="es">Estoy hablando de parte de Pedro.</quote>
        </cit>
      </cit>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COHQQ"/>
    <ptr target="#DSGRP"/>
    <ptr target="#DITPEG"/>
  </listRef>
```

^b26

