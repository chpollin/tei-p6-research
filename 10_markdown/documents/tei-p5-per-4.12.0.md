---
type: representation
source-type: document
source: '[[00_sources/tei-p5-per-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 per
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/per.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# per

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4621. Git blob: `9b26e45edce9af36387c00659073b298a2953780`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-per" ident="per">
  <equiv name="grammaticalPerson" uri="http://www.tc37sc4.org"/>
  <gloss versionDate="2005-01-14" xml:lang="en">person</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">인칭</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">人稱</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">personne</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">persona</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">persona</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains an indication of the grammatical person (1st, 2nd, 3rd, etc.) associated with a
    given inflected form in a dictionary.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">사전에 제시된 굴절형과 관련된 문법적 인칭(1인칭, 2인칭, 3인칭 등)의 표시를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含字典中有屈折變化單字的人稱形式 (第一、第二、第三等)  。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">辞書にある屈折形と関連する、文法上の人称(1人称、2人称、3人称など)を
  示す。</desc>
  <desc versionDate="2009-04-08" xml:lang="fr">contient des indications sur la personne
			grammaticale (1re, 2e, 3e, etc.) liée à une forme fléchie donnée dans un
			dictionnaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la persona gramatical (1ª, 2ª, 3ª, etc.) asociada con una forma flexiva en un diccionario.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">in un dizionario, contiene una indicazione della persona grammaticale (prima, seconda, terza, ecc.) associata ad una determinata forma flessa.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-per-egXML-ur">
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-per-egXML-pq">
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-per-egXML-sn">
       因漢字無「格」的現象，故不提供範例。 
    </egXML>
  </exemplum>
  <remarks ident="per-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element is synonymous with <tag>gram type="person"</tag>.</p>
  </remarks>
  <remarks ident="per-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est synonyme de <tag>gram type="person"</tag>.</p>
  </remarks>
  <remarks ident="per-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、<tag>gram type="person"</tag>と同義である。
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
<equiv name="grammaticalPerson" uri="http://www.tc37sc4.org"/>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">person</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">인칭</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">人稱</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">personne</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">persona</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">persona</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains an indication of the grammatical person (1st, 2nd, 3rd, etc.) associated with a
    given inflected form in a dictionary.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">사전에 제시된 굴절형과 관련된 문법적 인칭(1인칭, 2인칭, 3인칭 등)의 표시를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含字典中有屈折變化單字的人稱形式 (第一、第二、第三等)  。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">辞書にある屈折形と関連する、文法上の人称(1人称、2人称、3人称など)を
  示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-08" xml:lang="fr">contient des indications sur la personne
			grammaticale (1re, 2e, 3e, etc.) liée à une forme fléchie donnée dans un
			dictionnaire.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la persona gramatical (1ª, 2ª, 3ª, etc.) asociada con una forma flexiva en un diccionario.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">in un dizionario, contiene una indicazione della persona grammaticale (prima, seconda, terza, ecc.) associata ad una determinata forma flessa.</desc>
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-per-egXML-ur">
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-per-egXML-pq">
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
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-per-egXML-sn">
       因漢字無「格」的現象，故不提供範例。 
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="per-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element is synonymous with <tag>gram type="person"</tag>.</p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="per-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est synonyme de <tag>gram type="person"</tag>.</p>
  </remarks>
```

^b21

### Block 22

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="per-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、<tag>gram type="person"</tag>と同義である。
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

