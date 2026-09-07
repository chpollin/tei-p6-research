---
type: representation
source-type: document
source: '[[00_sources/tei-p5-p-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 p
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/p.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# p

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5302. Git blob: `f1f9409a14ce69ae997e0bbe034234a759442b5d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="core" xml:id="gi-p" ident="p">
  <gloss versionDate="2005-01-14" xml:lang="en">paragraph</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">문단</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">段落</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">paragraphe</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">párrafo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">paragrafo</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Absatz</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">marks paragraphs in prose.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">산문에서 문단을 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記散文的段落。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">散文の段落を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">marque les paragraphes dans un texte en prose.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">marca párrafos en prosa.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica i paragrafi in prosa.</desc>
  <desc versionDate="2016-11-24" xml:lang="de">markiert einen Absatz in einem Prosatext.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.fragmentable"/>
    <memberOf key="att.written"/>
    <memberOf key="model.pLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <constraintSpec ident="abstractModel-structure-p-in-ab-or-p" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:p">
        <sch:report test="(ancestor::tei:ab or ancestor::tei:p) and
                       not( ancestor::tei:floatingText
                          | parent::tei:exemplum
                          | parent::tei:item
                          | parent::tei:note
                          | parent::tei:q
                          | parent::tei:quote
                          | parent::tei:remarks
                          | parent::tei:said
                          | parent::tei:sp
                          | parent::tei:stage
                          | parent::tei:cell
                          | parent::tei:figure )">
          Abstract model violation: Paragraphs may not occur inside other paragraphs or &lt;ab> elements.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <constraintSpec ident="abstractModel-structure-p-in-l" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:l//tei:p">
        <sch:assert test="ancestor::tei:floatingText | parent::tei:figure | parent::tei:note">
          Abstract model violation: Metrical lines (&lt;l> elements) may not contain higher-level structural elements such as &lt;div>, &lt;p>, or &lt;ab>, unless &lt;p> is a child of &lt;figure> or &lt;note>, or is a descendant of &lt;floatingText>.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-p-egXML-hr" source="#NJAL">
      <p>Hallgerd was outside. <q>There is blood on your axe,</q> she said. <q>What have you
                    done?</q>
            </p>
      <p><q>I have now arranged that you can be married a second time,</q> replied Thjostolf.</p>
      <p><q>Then you must mean that Thorvald is dead,</q> she said.</p>
      <p><q>Yes,</q> said Thjostolf. <q>And now you must think up some plan for me.</q>
         </p>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-p-egXML-dk" source="#fr-ex-Flaubert_Sal">
      <div>
        <p>C'était à Mégara, faubourg de Carthage, dans les jardins d'Hamilcar.</p>
        <p>Les soldats qu'il avait commandés en Sicile se donnaient un grand festin pour célébrer
            le jour anniversaire de la bataille d'Eryx, et comme le maître était absent et qu'ils se
            trouvaient nombreux, ils mangeaient et ils buvaient en pleine liberté.</p>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-p-egXML-hk" source="#biblzh-tw_n17"><p>我抬起頭，他打開了一扇窗戶，探出頭來。<q>先生？</q>
         </p><p><q>你要去哪。葛里葉？</q></p><p><q>去藥劑師那裡，先生。太太要我去，替男孩拿點東西。</q></p><p><q>你能不能也替我拿點東西？</q></p>ㄒㄒ
      <p><q>當然能，先生。</q> 忽然間風好像沒那麼刺骨了。 <q>等一下，我把它寫下來。</q>
         </p>
      </egXML>
  </exemplum>
  <listRef>
    <ptr target="#COPA" type="div2"/>
    <ptr target="#DRPAL" type="div2"/>
  </listRef>
</elementSpec>

```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">paragraph</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">문단</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">段落</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">paragraphe</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">párrafo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">paragrafo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Absatz</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks paragraphs in prose.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">산문에서 문단을 표시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記散文的段落。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">散文の段落を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">marque les paragraphes dans un texte en prose.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">marca párrafos en prosa.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica i paragrafi in prosa.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">markiert einen Absatz in einem Prosatext.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.declaring"/>
    <memberOf key="att.fragmentable"/>
    <memberOf key="att.written"/>
    <memberOf key="model.pLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="abstractModel-structure-p-in-ab-or-p" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:p">
        <sch:report test="(ancestor::tei:ab or ancestor::tei:p) and
                       not( ancestor::tei:floatingText
                          | parent::tei:exemplum
                          | parent::tei:item
                          | parent::tei:note
                          | parent::tei:q
                          | parent::tei:quote
                          | parent::tei:remarks
                          | parent::tei:said
                          | parent::tei:sp
                          | parent::tei:stage
                          | parent::tei:cell
                          | parent::tei:figure )">
          Abstract model violation: Paragraphs may not occur inside other paragraphs or &lt;ab> elements.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/constraintSpec[2]`.

```xml
<constraintSpec ident="abstractModel-structure-p-in-l" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:l//tei:p">
        <sch:assert test="ancestor::tei:floatingText | parent::tei:figure | parent::tei:note">
          Abstract model violation: Metrical lines (&lt;l> elements) may not contain higher-level structural elements such as &lt;div>, &lt;p>, or &lt;ab>, unless &lt;p> is a child of &lt;figure> or &lt;note>, or is a descendant of &lt;floatingText>.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-p-egXML-hr" source="#NJAL">
      <p>Hallgerd was outside. <q>There is blood on your axe,</q> she said. <q>What have you
                    done?</q>
            </p>
      <p><q>I have now arranged that you can be married a second time,</q> replied Thjostolf.</p>
      <p><q>Then you must mean that Thorvald is dead,</q> she said.</p>
      <p><q>Yes,</q> said Thjostolf. <q>And now you must think up some plan for me.</q>
         </p>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-p-egXML-dk" source="#fr-ex-Flaubert_Sal">
      <div>
        <p>C'était à Mégara, faubourg de Carthage, dans les jardins d'Hamilcar.</p>
        <p>Les soldats qu'il avait commandés en Sicile se donnaient un grand festin pour célébrer
            le jour anniversaire de la bataille d'Eryx, et comme le maître était absent et qu'ils se
            trouvaient nombreux, ils mangeaient et ils buvaient en pleine liberté.</p>
      </div>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-p-egXML-hk" source="#biblzh-tw_n17"><p>我抬起頭，他打開了一扇窗戶，探出頭來。<q>先生？</q>
         </p><p><q>你要去哪。葛里葉？</q></p><p><q>去藥劑師那裡，先生。太太要我去，替男孩拿點東西。</q></p><p><q>你能不能也替我拿點東西？</q></p>ㄒㄒ
      <p><q>當然能，先生。</q> 忽然間風好像沒那麼刺骨了。 <q>等一下，我把它寫下來。</q>
         </p>
      </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#COPA" type="div2"/>
    <ptr target="#DRPAL" type="div2"/>
  </listRef>
```

^b23

