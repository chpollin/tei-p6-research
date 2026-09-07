---
type: representation
source-type: document
source: '[[00_sources/tei-p5-msfrag-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 msFrag
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/msFrag.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# msFrag

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6317. Git blob: `495908f85dc88a997772614413cbdbd9123d1f82`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="MSFRAG" ident="msFrag">
    <gloss versionDate="2015-10-26" xml:lang="en">manuscript fragment</gloss>
<!--<gloss versionDate="2015-10-26" xml:lang="ko"></gloss>-->
<!--<gloss versionDate="2015-10-26" xml:lang="zh-TW"/>-->
    <gloss versionDate="2015-10-26" xml:lang="de">Fragment einer Handschrift</gloss>
    <gloss versionDate="2015-10-26" xml:lang="es">fragmento del manuscrito</gloss>
    <gloss versionDate="2015-10-26" xml:lang="fr">fragment d'un manuscrit</gloss>
    <gloss versionDate="2015-10-26" xml:lang="it">frammento di un manoscritto</gloss>
    <desc versionDate="2019-05-08" xml:lang="en" xml:id="msfrag.desc">contains information about a fragment described in relation to a prior context, typically as a description of a virtual reconstruction of a manuscript or other object whose fragments were catalogued separately.</desc>
<!--<desc versionDate="2007-12-20" xml:lang="ko"></desc>
    <desc versionDate="2007-05-02" xml:lang="zh-TW"></desc>
    <desc versionDate="2008-04-05" xml:lang="ja"></desc>-->
    <desc versionDate="2015-10-26" xml:lang="fr">contient des informations sur un fragment d'un manuscrit dispersé, aujourd'hui conservé séparément ou incorporé dans un autre manuscrit.</desc>
    <desc versionDate="2015-10-26" xml:lang="de">enthält Informationen zu einem Handschriftenfragment einer fragmentierten Handschrift, das heute als Einzeldokument oder eingebunden in eine Handschrift aufbewahrt wird.</desc>
<!--<desc versionDate="2007-05-04" xml:lang="es"></desc>-->
<!--<desc versionDate="2007-01-21" xml:lang="it"></desc>-->
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <sequence>
      <alternate>
        <elementRef key="altIdentifier"/>
        <elementRef key="msIdentifier"/>
      </alternate>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <!--
          The desired content model for the following is
            ( pLike | ( msContents? & physDesc? & history? & additional? ) )
          but of course we can't use interleave, as DTDs (and maybe XSD)
          will not support that. See https://github.com/TEIC/TEI/issues/2214.
      -->
      <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <!-- Cannot use maxOccurs=4 because resulting content model is ambiguous -->
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="msContents"/>
          <elementRef key="physDesc"/>
          <elementRef key="history"/>
          <elementRef key="additional"/>
        </alternate>
      </alternate>
    </sequence>
  </content>
  <exemplum versionDate="2015-10-26" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSFRAG-egXML-kv">
      <msDesc>
        <msIdentifier>
          <msName xml:lang="la">Codex Suprasliensis</msName>
        </msIdentifier>
        <msFrag>
          <msIdentifier>
            <settlement>Ljubljana</settlement>
            <repository>Narodna in univerzitetna knjiznica</repository>
            <idno>MS Kopitar 2</idno>
          </msIdentifier>
          <msContents>
            <summary>Contains ff. 10 to 42 only</summary>
          </msContents>
        </msFrag>
        <msFrag>
          <msIdentifier>
            <settlement>Warszawa</settlement>
            <repository>Biblioteka Narodowa</repository>
            <idno>BO 3.201</idno>
          </msIdentifier>
        </msFrag>
        <msFrag>
          <msIdentifier>
            <settlement>Sankt-Peterburg</settlement>
            <repository>Rossiiskaia natsional'naia biblioteka</repository>
            <idno>Q.p.I.72</idno>
          </msIdentifier>
        </msFrag>
      </msDesc>
    </egXML>
  </exemplum>
  <exemplum versionDate="2015-10-26" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSFRAG-egXML-jd">
      <msDesc>
        <msIdentifier>
          <msName>Letter of Carl Maria von Weber to Caroline Brandt. Dresden, 21st to 23rd May 1817 </msName>
        </msIdentifier>
        <history>
          <p>The second part of the letter (Weberiana Cl.II A a 2, 9) was given to Friedrich Jähns by Caroline von Weber, 
          the widow of Carl Maria von Weber. Jähns then handed this fragment over to the Berlin state library in 1881, 
          whereas the first part (Mus.ep. Weber, C. M. v. 96) remained with the family estate and found its way into the library not until 1956.
          Yet, the identification was already obvious to Jähns who noted <quote>Zu No. 50. 21. Mai 1817 gehörig</quote>
          at the top of his fragment.</p>
        </history>
        <msFrag>
          <msIdentifier>
            <country>D</country>
            <settlement>Berlin</settlement>
            <repository>Staatsbibliothek zu Berlin Preußischer Kulturbesitz</repository>
            <idno>Mus.ep. Weber, C. M. v. 96</idno>
          </msIdentifier>
          <physDesc>
            <objectDesc>
              <supportDesc>
                <p>One double leaf, four written pages without address.</p>
              </supportDesc>
            </objectDesc>
          </physDesc>
        </msFrag>
        <msFrag>
          <msIdentifier>
            <country>D</country>
            <settlement>Berlin</settlement>
            <repository>Staatsbibliothek zu Berlin Preußischer Kulturbesitz</repository>
            <idno>Weberiana Cl.II A a 2, 9</idno>
          </msIdentifier>
          <physDesc>
            <objectDesc>
              <supportDesc>
                <p>One leaf, two written pages including address.</p>
              </supportDesc>
            </objectDesc>
          </physDesc>
        </msFrag>
      </msDesc>
    </egXML>
    <p>source: http://www.weber-gesamtausgabe.de/A041180</p>
  </exemplum>
  <listRef>
    <ptr target="#msfg"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2015-10-26" xml:lang="en">manuscript fragment</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2015-10-26" xml:lang="de">Fragment einer Handschrift</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2015-10-26" xml:lang="es">fragmento del manuscrito</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2015-10-26" xml:lang="fr">fragment d'un manuscrit</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2015-10-26" xml:lang="it">frammento di un manoscritto</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-05-08" xml:lang="en" xml:id="msfrag.desc">contains information about a fragment described in relation to a prior context, typically as a description of a virtual reconstruction of a manuscript or other object whose fragments were catalogued separately.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2015-10-26" xml:lang="fr">contient des informations sur un fragment d'un manuscrit dispersé, aujourd'hui conservé séparément ou incorporé dans un autre manuscrit.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2015-10-26" xml:lang="de">enthält Informationen zu einem Handschriftenfragment einer fragmentierten Handschrift, das heute als Einzeldokument oder eingebunden in eine Handschrift aufbewahrt wird.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b9

### Block 10

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate>
        <elementRef key="altIdentifier"/>
        <elementRef key="msIdentifier"/>
      </alternate>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
      <!--
          The desired content model for the following is
            ( pLike | ( msContents? & physDesc? & history? & additional? ) )
          but of course we can't use interleave, as DTDs (and maybe XSD)
          will not support that. See https://github.com/TEIC/TEI/issues/2214.
      -->
      <alternate>
        <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
        <!-- Cannot use maxOccurs=4 because resulting content model is ambiguous -->
        <alternate minOccurs="0" maxOccurs="unbounded">
          <elementRef key="msContents"/>
          <elementRef key="physDesc"/>
          <elementRef key="history"/>
          <elementRef key="additional"/>
        </alternate>
      </alternate>
    </sequence>
  </content>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum versionDate="2015-10-26" xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSFRAG-egXML-kv">
      <msDesc>
        <msIdentifier>
          <msName xml:lang="la">Codex Suprasliensis</msName>
        </msIdentifier>
        <msFrag>
          <msIdentifier>
            <settlement>Ljubljana</settlement>
            <repository>Narodna in univerzitetna knjiznica</repository>
            <idno>MS Kopitar 2</idno>
          </msIdentifier>
          <msContents>
            <summary>Contains ff. 10 to 42 only</summary>
          </msContents>
        </msFrag>
        <msFrag>
          <msIdentifier>
            <settlement>Warszawa</settlement>
            <repository>Biblioteka Narodowa</repository>
            <idno>BO 3.201</idno>
          </msIdentifier>
        </msFrag>
        <msFrag>
          <msIdentifier>
            <settlement>Sankt-Peterburg</settlement>
            <repository>Rossiiskaia natsional'naia biblioteka</repository>
            <idno>Q.p.I.72</idno>
          </msIdentifier>
        </msFrag>
      </msDesc>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2015-10-26" xml:lang="de">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MSFRAG-egXML-jd">
      <msDesc>
        <msIdentifier>
          <msName>Letter of Carl Maria von Weber to Caroline Brandt. Dresden, 21st to 23rd May 1817 </msName>
        </msIdentifier>
        <history>
          <p>The second part of the letter (Weberiana Cl.II A a 2, 9) was given to Friedrich Jähns by Caroline von Weber, 
          the widow of Carl Maria von Weber. Jähns then handed this fragment over to the Berlin state library in 1881, 
          whereas the first part (Mus.ep. Weber, C. M. v. 96) remained with the family estate and found its way into the library not until 1956.
          Yet, the identification was already obvious to Jähns who noted <quote>Zu No. 50. 21. Mai 1817 gehörig</quote>
          at the top of his fragment.</p>
        </history>
        <msFrag>
          <msIdentifier>
            <country>D</country>
            <settlement>Berlin</settlement>
            <repository>Staatsbibliothek zu Berlin Preußischer Kulturbesitz</repository>
            <idno>Mus.ep. Weber, C. M. v. 96</idno>
          </msIdentifier>
          <physDesc>
            <objectDesc>
              <supportDesc>
                <p>One double leaf, four written pages without address.</p>
              </supportDesc>
            </objectDesc>
          </physDesc>
        </msFrag>
        <msFrag>
          <msIdentifier>
            <country>D</country>
            <settlement>Berlin</settlement>
            <repository>Staatsbibliothek zu Berlin Preußischer Kulturbesitz</repository>
            <idno>Weberiana Cl.II A a 2, 9</idno>
          </msIdentifier>
          <physDesc>
            <objectDesc>
              <supportDesc>
                <p>One leaf, two written pages including address.</p>
              </supportDesc>
            </objectDesc>
          </physDesc>
        </msFrag>
      </msDesc>
    </egXML>
    <p>source: http://www.weber-gesamtausgabe.de/A041180</p>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msfg"/>
  </listRef>
```

^b13

