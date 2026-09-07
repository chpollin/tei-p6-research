---
type: representation
source-type: document
source: '[[00_sources/tei-p5-floatingtext-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 floatingText
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/floatingText.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# floatingText

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5993. Git blob: `21265610c528f3ea03413ad0bd5cf72c68cd1756`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-floatingText" ident="floatingText">
  <gloss versionDate="2020-12-20" xml:lang="en">floating text</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">texte mobile</gloss>
  <desc versionDate="2007-04-06" xml:lang="en">contains a single text of any kind, whether unitary or composite, which interrupts the text
    containing it at any point and after which the surrounding text resumes.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">단일 또는 혼합이든지 간에, 어떤 지점에서 그것을 포함한 텍스트를 중단시키고 그 이후 주변 텍스트가
    다시 시작하는 텍스트.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一份任何種類的文本，無論是單一或複合的，該份文本任意穿插於整體文本中，而週遭文字則接續其後。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ひとつのテキストを示す。下位構造はあってもよい。当該部分はテキスト中 のどこにでも出現できる。自在テキスト。</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene un unico testo di qualsiasi tipo, sia esso
    unitario o composito, che interrompe il testo che lo contiene in un qualsiasi punto e dopo il
    quale il testo circostante riprende</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient un texte quelconque, homogène ou composite, qui
    interrompt le texte le contenant à n’importe quel endroit et après lequel le texte environnant
    reprend.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un texto de cualquier tipo, unitario o
    compuesto, que se insiere en algún punto en un texto que lo contiene interrumpiéndolo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.attributable"/>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floatingText-egXML-sg">
      <body>
        <div type="scene">
          <sp>
            <p>Hush, the players begin...</p>
          </sp>
          <floatingText type="pwp">
            <body>
              <div type="act">
                <sp>
                  <l>In Athens our tale takes place [...]</l>
                </sp>
                <!-- ... rest of nested act here -->
              </div>
            </body>
          </floatingText>
          <sp>
            <p>Now that the play is finished ...</p>
          </sp>
        </div>
      </body>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floatingText-egXML-iy">
      <body>
        <div type="scene">
          <sp>
            <p>Chut ! Les acteurs commencent...</p>
          </sp>
          <floatingText type="pwp">
            <body>
              <div type="act">
                <sp>
                  <l>Notre histoire se passe à Athènes [...]</l>
                  <!-- ... rest of nested act here -->
                </sp>
              </div>
            </body>
          </floatingText>
          <sp>
            <p>La pièce est maintenant finie ...</p>
          </sp>
        </div>
      </body>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floatingText-egXML-ak">
      <body>
        <div type="scene">
          <sp>
            <p>快點，演員開始了...</p>
          </sp>
          <floatingText type="pwp">
            <body>
              <div type="act">
                <sp>
                  <l>故事開始於雅典...</l>
                </sp>
                <!-- ... 這裡是其他動作 -->
              </div>
            </body>
          </floatingText>
          <sp>
            <p>戲劇結束...</p>
          </sp>
        </div>
      </body>
    </egXML>
  </exemplum>
  <remarks ident="floatingText-remarks" versionDate="2012-04-17" xml:lang="en">
    <p>A floating text has the same content as any other <gi>text</gi>
    and may thus be interrupted by another floating text, or contain a
    <gi>group</gi> of tesselated texts.</p>
  </remarks>
  <remarks ident="floatingText-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un texte "flottant" a le même contenu que tout autre texte : il peut donc être interrompu par
      un autre texte "flottant"  ou contenir un groupe de textes composites.</p>
  </remarks>
  <remarks ident="floatingText-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 自在テキストは、他の自在テキストと同じ内容をとったり、定まった構造 の部分としてあるテキスト(充填テキスト)をとる。 </p>
  </remarks>
  <listRef>
    <ptr target="#DSFLT"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">floating text</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">texte mobile</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-06" xml:lang="en">contains a single text of any kind, whether unitary or composite, which interrupts the text
    containing it at any point and after which the surrounding text resumes.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">단일 또는 혼합이든지 간에, 어떤 지점에서 그것을 포함한 텍스트를 중단시키고 그 이후 주변 텍스트가
    다시 시작하는 텍스트.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一份任何種類的文本，無論是單一或複合的，該份文本任意穿插於整體文本中，而週遭文字則接續其後。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ひとつのテキストを示す。下位構造はあってもよい。当該部分はテキスト中 のどこにでも出現できる。自在テキスト。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene un unico testo di qualsiasi tipo, sia esso
    unitario o composito, che interrompe il testo che lo contiene in un qualsiasi punto e dopo il
    quale il testo circostante riprende</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient un texte quelconque, homogène ou composite, qui
    interrompt le texte le contenant à n’importe quel endroit et après lequel le texte environnant
    reprend.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un texto de cualquier tipo, unitario o
    compuesto, que se insiere en algún punto en un texto que lo contiene interrumpiéndolo.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.attributable"/>
  </classes>
```

^b10

### Block 11

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

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floatingText-egXML-sg">
      <body>
        <div type="scene">
          <sp>
            <p>Hush, the players begin...</p>
          </sp>
          <floatingText type="pwp">
            <body>
              <div type="act">
                <sp>
                  <l>In Athens our tale takes place [...]</l>
                </sp>
                <!-- ... rest of nested act here -->
              </div>
            </body>
          </floatingText>
          <sp>
            <p>Now that the play is finished ...</p>
          </sp>
        </div>
      </body>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floatingText-egXML-iy">
      <body>
        <div type="scene">
          <sp>
            <p>Chut ! Les acteurs commencent...</p>
          </sp>
          <floatingText type="pwp">
            <body>
              <div type="act">
                <sp>
                  <l>Notre histoire se passe à Athènes [...]</l>
                  <!-- ... rest of nested act here -->
                </sp>
              </div>
            </body>
          </floatingText>
          <sp>
            <p>La pièce est maintenant finie ...</p>
          </sp>
        </div>
      </body>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-floatingText-egXML-ak">
      <body>
        <div type="scene">
          <sp>
            <p>快點，演員開始了...</p>
          </sp>
          <floatingText type="pwp">
            <body>
              <div type="act">
                <sp>
                  <l>故事開始於雅典...</l>
                </sp>
                <!-- ... 這裡是其他動作 -->
              </div>
            </body>
          </floatingText>
          <sp>
            <p>戲劇結束...</p>
          </sp>
        </div>
      </body>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="floatingText-remarks" versionDate="2012-04-17" xml:lang="en">
    <p>A floating text has the same content as any other <gi>text</gi>
    and may thus be interrupted by another floating text, or contain a
    <gi>group</gi> of tesselated texts.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="floatingText-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Un texte "flottant" a le même contenu que tout autre texte : il peut donc être interrompu par
      un autre texte "flottant"  ou contenir un groupe de textes composites.</p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="floatingText-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 自在テキストは、他の自在テキストと同じ内容をとったり、定まった構造 の部分としてあるテキスト(充填テキスト)をとる。 </p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSFLT"/>
  </listRef>
```

^b18

