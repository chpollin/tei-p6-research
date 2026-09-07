---
type: representation
source-type: document
source: '[[00_sources/tei-p5-tns-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 tns
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/tns.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# tns

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4309. Git blob: `0d40013d891230994c5c90c5d49c65e591ac0580`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-tns" ident="tns">
  <equiv name="grammaticalTense" uri="http://www.tc37sc4.org"/>
  <gloss versionDate="2005-01-14" xml:lang="en">tense</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">시제</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">時態</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">temps</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">tiempo</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">tempo</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates the grammatical tense associated with a given inflected form in a dictionary.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전에 제시된 굴절형과 관련된 문법적 시제를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">說明某屈折形式的時態。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書にある屈折形と関連する文法上の時制を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">indique le temps grammatical lié à une forme
			fléchie donnée dans un dictionnaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el tiempo gramatical asociado con con una forma flexiva dada en un diccionario</desc>
  <desc versionDate="2007-01-21" xml:lang="it">in un dizionario, indica il tempo grammaticale associato ad una determinata forma flessa.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.morphLike"/>
  </classes>
  <content>
    <macroRef key="macro.paraContent"/>
  </content>
  <exemplum xml:lang="en">
    <p>Taken from <bibl><title>Wörterbuch der Deutschen Sprache.</title><title> Veranstaltet und herausgegeben von
          Joachim Heinrich Campe. Vierter Theil. S - bis - T.</title> (Braunschweig 1810. In der
        Schulbuchhandlung)</bibl>: <q rend="display">Treffen, v. unregelm. ... du triffst, ... </q>
      </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tns-egXML-od">
      <entry>
        <form type="inflected">
          <gramGrp>
            <per value="2"/>
            <number value="singular"/>
            <tns value="present"/>
            <mood value="indicative"/>
          </gramGrp>
          <form type="personalpronoun">
            <orth>du</orth>
          </form>
          <form type="headword">
            <orth>
              <oRef>triffst</oRef>
            </orth>
          </form>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tns-egXML-oz">
      <entry>
        <form type="flexion">
          <gramGrp>
            <per value="2"/>
            <number value="singulier"/>
            <tns value="présent"/>
            <mood value="indicatif"/>
          </gramGrp>
          <form type="pronom_personnel">
            <orth>tu</orth>
          </form>
          <form type="entrée">
            <orth>
              <oRef>vas</oRef>
            </orth>
          </form>
        </form>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tns-egXML-gv">
       因漢語無時態變化，故不提供範例。 
    </egXML>
  </exemplum>
  <remarks ident="tns-remarks" versionDate="2007-04-26" xml:lang="en">
    <p>This element is synonymous with <tag>gram type="tense"</tag>.</p>
  </remarks>
  <remarks ident="tns-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est synonyme de <tag>gram type="tense"</tag>.</p>
  </remarks>
  <remarks ident="tns-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、<tag>gram type="tense"</tag>と同義である。
    </p>
  </remarks>
  <listRef>
    <ptr target="#DITPFO"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/equiv[1]`.

```xml
<equiv name="grammaticalTense" uri="http://www.tc37sc4.org"/>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">tense</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">시제</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">時態</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">temps</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">tiempo</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">tempo</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the grammatical tense associated with a given inflected form in a dictionary.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전에 제시된 굴절형과 관련된 문법적 시제를 표시한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明某屈折形式的時態。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書にある屈折形と関連する文法上の時制を示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le temps grammatical lié à une forme
			fléchie donnée dans un dictionnaire.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el tiempo gramatical asociado con con una forma flexiva dada en un diccionario</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">in un dizionario, indica il tempo grammaticale associato ad una determinata forma flessa.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="model.morphLike"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.paraContent"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>Taken from <bibl><title>Wörterbuch der Deutschen Sprache.</title><title> Veranstaltet und herausgegeben von
          Joachim Heinrich Campe. Vierter Theil. S - bis - T.</title> (Braunschweig 1810. In der
        Schulbuchhandlung)</bibl>: <q rend="display">Treffen, v. unregelm. ... du triffst, ... </q>
      </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tns-egXML-od">
      <entry>
        <form type="inflected">
          <gramGrp>
            <per value="2"/>
            <number value="singular"/>
            <tns value="present"/>
            <mood value="indicative"/>
          </gramGrp>
          <form type="personalpronoun">
            <orth>du</orth>
          </form>
          <form type="headword">
            <orth>
              <oRef>triffst</oRef>
            </orth>
          </form>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tns-egXML-oz">
      <entry>
        <form type="flexion">
          <gramGrp>
            <per value="2"/>
            <number value="singulier"/>
            <tns value="présent"/>
            <mood value="indicatif"/>
          </gramGrp>
          <form type="pronom_personnel">
            <orth>tu</orth>
          </form>
          <form type="entrée">
            <orth>
              <oRef>vas</oRef>
            </orth>
          </form>
        </form>
      </entry>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-tns-egXML-gv">
       因漢語無時態變化，故不提供範例。 
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="tns-remarks" versionDate="2007-04-26" xml:lang="en">
    <p>This element is synonymous with <tag>gram type="tense"</tag>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="tns-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est synonyme de <tag>gram type="tense"</tag>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="tns-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、<tag>gram type="tense"</tag>と同義である。
    </p>
  </remarks>
```

^b22

### Block 23

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPFO"/>
  </listRef>
```

^b23

