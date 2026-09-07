---
type: representation
source-type: document
source: '[[00_sources/tei-p5-guidelines-guidelines-en-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 The TEI Guidelines
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/guidelines-en.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# The TEI Guidelines

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9152. Git blob: `942a9ca4688ebc9830174a53f366c0cedddf6626`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
Copyright TEI Consortium. 
Licensed under the GNU General Public License. 
See the file COPYING for details.
$Date$
$Id$
-->
<TEI xmlns="http://www.tei-c.org/ns/1.0"
     xmlns:rng="http://relaxng.org/ns/structure/1.0"
     xmlns:sch="http://purl.oclc.org/dsdl/schematron"
     version="5.0" rend="book" xml:lang="en">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>The TEI Guidelines</title>
      </titleStmt>
      <editionStmt>
        <edition>P5 <?insert version?>. Last updated on
        <?insert date?>, revision <?insert revision?></edition>
      </editionStmt>
      <publicationStmt>
        <distributor>TEI Consortium</distributor>
        <availability status="restricted">
          <licence target="http://creativecommons.org/licenses/by/3.0/">
            Distributed under a Creative Commons Attribution 3.0 Unported License.
          </licence>
          <licence target="http://www.opensource.org/licenses/BSD-2-Clause">
            <p>Copyright <?insert year?> TEI Consortium.</p>
            <p>All rights reserved.</p>     
            <p>Redistribution and use in source and binary forms, with
            or without modification, are permitted provided that the
            following conditions are met:</p>
            <list>
              <item>Redistributions of source code must retain the
              above copyright notice, this list of conditions and the
              following disclaimer.</item>
              <item>Redistributions in binary form must reproduce the
              above copyright notice, this list of conditions and the
              following disclaimer in the documentation and/or other
              materials provided with the distribution.</item>
            </list>
            <p>This software is provided by the copyright holders and
            contributors "as is" and any express or implied
            warranties, including, but not limited to, the implied
            warranties of merchantability and fitness for a particular
            purpose are disclaimed. In no event shall the copyright
            holder or contributors be liable for any direct, indirect,
            incidental, special, exemplary, or consequential damages
            (including, but not limited to, procurement of substitute
            goods or services; loss of use, data, or profits; or
            business interruption) however caused and on any theory of
            liability, whether in contract, strict liability, or tort
            (including negligence or otherwise) arising in any way out
            of the use of this software, even if advised of the
            possibility of such damage.</p>
          </licence>
          <p>TEI material can be licensed differently depending on the
          use you intend to make of it. Hence it is made available
          under both the CC+BY and BSD-2 licences. The CC+BY licence
          is generally appropriate for usages which treat TEI content
          as data or documentation. The BSD-2 licence is generally
          appropriate for usage of TEI content in a software
          environment. For further information or clarification,
          please contact the <ref target="mailto:info@tei-c.org">TEI
          Consortium</ref>.
          </p>
        </availability>   
      </publicationStmt>
      <sourceDesc><p>A long history from P2 onwards. See further <ptr target="#PREFS"/></p></sourceDesc>
    </fileDesc>
    <encodingDesc>
      <constraintDecl scheme="schematron" xml:lang="en">
        <sch:ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
        <sch:ns prefix="xs" uri="http://www.w3.org/2001/XMLSchema"/>
        <sch:ns prefix="rng" uri="http://relaxng.org/ns/structure/1.0"/>
        <sch:ns prefix="rna" uri="http://relaxng.org/ns/compatibility/annotations/1.0"/>
        <sch:ns prefix="sch" uri="http://purl.oclc.org/dsdl/schematron"/>
        <sch:ns prefix="sch1x" uri="http://www.ascc.net/xml/schematron"/>
      </constraintDecl>
    </encodingDesc>
    <revisionDesc>
      <change>
        <date>$Date$.</date>
        <name>$Id$</name>
        $Id$
      </change>
    </revisionDesc>
  </teiHeader>
  <text>
    <front xml:id="FM">
      <titlePage>
        <docAuthor>The TEI Consortium</docAuthor>
        <docTitle n="TEI P5 ">
          <titlePart><title type="sub">TEI P5: </title></titlePart>
          <titlePart>
            <title type="main">Guidelines for Electronic Text Encoding and Interchange</title>
          </titlePart>
        </docTitle>
        <byline rend="large">by the TEI Consortium</byline>
        <note place="inline">Originally edited by C.M. Sperberg-McQueen and
        Lou Burnard for the ACH-ALLC-ACL Text Encoding Initiative</note>
        <note place="inline" rend="large">Now entirely revised and expanded under the
        supervision of the Technical Council of the TEI Consortium</note>
        <docImprint>
          <publisher>Text Encoding Initiative Consortium</publisher>
        </docImprint>
        <docDate><?insert year?></docDate>
      </titlePage>
      <divGen type="toc"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/TitlePageVerso.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/Dedication.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/FM1-IntroductoryNote.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/AB-About.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/SG-GentleIntroduction.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CH-LanguagesCharacterSets.xml"/>
    </front>
    <body>   
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/ST-Infrastructure.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/HD-Header.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CO-CoreElements.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/DS-DefaultTextStructure.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/WD-NonStandardCharacters.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/VE-Verse.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/DR-PerformanceTexts.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/TS-TranscriptionsofSpeech.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CMC-ComputerMediatedCommunication.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/DI-PrintDictionaries.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/MS-ManuscriptDescription.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/PH-PrimarySources.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/TC-CriticalApparatus.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/ND-NamesDates.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/FT-TablesFormulaeGraphics.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CC-LanguageCorpora.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/SA-LinkingSegmentationAlignment.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/AI-AnalyticMechanisms.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/FS-FeatureStructures.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/GD-GraphsNetworksTrees.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/NH-Non-hierarchical.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CE-CertaintyResponsibility.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/TD-DocumentationElements.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/USE.xml"/>
    </body>
    <back>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-CLASSES-MODEL.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-CLASSES-ATTS.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-ELEMENTS.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-ATTRIBUTES.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-MACROS.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/BIB-Bibliography.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/DEPRECATIONS.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/PrefatoryNote.xml"/>
      <include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/COL-Colophon.xml"/>
    </back>
  </text>
</TEI>

```

## Source blocks

### Block 1

XML location: `/TEI[1]/teiHeader[1]/fileDesc[1]/titleStmt[1]`.

```xml
<titleStmt>
        <title>The TEI Guidelines</title>
      </titleStmt>
```

^b1

### Block 2

XML location: `/TEI[1]/teiHeader[1]/fileDesc[1]/editionStmt[1]`.

```xml
<editionStmt>
        <edition>P5 <?insert version?>. Last updated on
        <?insert date?>, revision <?insert revision?></edition>
      </editionStmt>
```

^b2

### Block 3

XML location: `/TEI[1]/teiHeader[1]/fileDesc[1]/publicationStmt[1]`.

```xml
<publicationStmt>
        <distributor>TEI Consortium</distributor>
        <availability status="restricted">
          <licence target="http://creativecommons.org/licenses/by/3.0/">
            Distributed under a Creative Commons Attribution 3.0 Unported License.
          </licence>
          <licence target="http://www.opensource.org/licenses/BSD-2-Clause">
            <p>Copyright <?insert year?> TEI Consortium.</p>
            <p>All rights reserved.</p>     
            <p>Redistribution and use in source and binary forms, with
            or without modification, are permitted provided that the
            following conditions are met:</p>
            <list>
              <item>Redistributions of source code must retain the
              above copyright notice, this list of conditions and the
              following disclaimer.</item>
              <item>Redistributions in binary form must reproduce the
              above copyright notice, this list of conditions and the
              following disclaimer in the documentation and/or other
              materials provided with the distribution.</item>
            </list>
            <p>This software is provided by the copyright holders and
            contributors "as is" and any express or implied
            warranties, including, but not limited to, the implied
            warranties of merchantability and fitness for a particular
            purpose are disclaimed. In no event shall the copyright
            holder or contributors be liable for any direct, indirect,
            incidental, special, exemplary, or consequential damages
            (including, but not limited to, procurement of substitute
            goods or services; loss of use, data, or profits; or
            business interruption) however caused and on any theory of
            liability, whether in contract, strict liability, or tort
            (including negligence or otherwise) arising in any way out
            of the use of this software, even if advised of the
            possibility of such damage.</p>
          </licence>
          <p>TEI material can be licensed differently depending on the
          use you intend to make of it. Hence it is made available
          under both the CC+BY and BSD-2 licences. The CC+BY licence
          is generally appropriate for usages which treat TEI content
          as data or documentation. The BSD-2 licence is generally
          appropriate for usage of TEI content in a software
          environment. For further information or clarification,
          please contact the <ref target="mailto:info@tei-c.org">TEI
          Consortium</ref>.
          </p>
        </availability>   
      </publicationStmt>
```

^b3

### Block 4

XML location: `/TEI[1]/teiHeader[1]/fileDesc[1]/sourceDesc[1]`.

```xml
<sourceDesc><p>A long history from P2 onwards. See further <ptr target="#PREFS"/></p></sourceDesc>
```

^b4

### Block 5

XML location: `/TEI[1]/teiHeader[1]/encodingDesc[1]/constraintDecl[1]`.

```xml
<constraintDecl scheme="schematron" xml:lang="en">
        <sch:ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
        <sch:ns prefix="xs" uri="http://www.w3.org/2001/XMLSchema"/>
        <sch:ns prefix="rng" uri="http://relaxng.org/ns/structure/1.0"/>
        <sch:ns prefix="rna" uri="http://relaxng.org/ns/compatibility/annotations/1.0"/>
        <sch:ns prefix="sch" uri="http://purl.oclc.org/dsdl/schematron"/>
        <sch:ns prefix="sch1x" uri="http://www.ascc.net/xml/schematron"/>
      </constraintDecl>
```

^b5

### Block 6

XML location: `/TEI[1]/teiHeader[1]/revisionDesc[1]`.

```xml
<revisionDesc>
      <change>
        <date>$Date$.</date>
        <name>$Id$</name>
        $Id$
      </change>
    </revisionDesc>
```

^b6

### Block 7

XML location: `/TEI[1]/text[1]/front[1]/titlePage[1]`.

```xml
<titlePage>
        <docAuthor>The TEI Consortium</docAuthor>
        <docTitle n="TEI P5 ">
          <titlePart><title type="sub">TEI P5: </title></titlePart>
          <titlePart>
            <title type="main">Guidelines for Electronic Text Encoding and Interchange</title>
          </titlePart>
        </docTitle>
        <byline rend="large">by the TEI Consortium</byline>
        <note place="inline">Originally edited by C.M. Sperberg-McQueen and
        Lou Burnard for the ACH-ALLC-ACL Text Encoding Initiative</note>
        <note place="inline" rend="large">Now entirely revised and expanded under the
        supervision of the Technical Council of the TEI Consortium</note>
        <docImprint>
          <publisher>Text Encoding Initiative Consortium</publisher>
        </docImprint>
        <docDate><?insert year?></docDate>
      </titlePage>
```

^b7

### Block 8

XML location: `/TEI[1]/text[1]/front[1]/divGen[1]`.

```xml
<divGen type="toc"/>
```

^b8

### Block 9

XML location: `/TEI[1]/text[1]/front[1]/include[1]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/TitlePageVerso.xml"/>
```

^b9

### Block 10

XML location: `/TEI[1]/text[1]/front[1]/include[2]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/Dedication.xml"/>
```

^b10

### Block 11

XML location: `/TEI[1]/text[1]/front[1]/include[3]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/FM1-IntroductoryNote.xml"/>
```

^b11

### Block 12

XML location: `/TEI[1]/text[1]/front[1]/include[4]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/AB-About.xml"/>
```

^b12

### Block 13

XML location: `/TEI[1]/text[1]/front[1]/include[5]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/SG-GentleIntroduction.xml"/>
```

^b13

### Block 14

XML location: `/TEI[1]/text[1]/front[1]/include[6]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CH-LanguagesCharacterSets.xml"/>
```

^b14

### Block 15

XML location: `/TEI[1]/text[1]/body[1]/include[1]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/ST-Infrastructure.xml"/>
```

^b15

### Block 16

XML location: `/TEI[1]/text[1]/body[1]/include[2]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/HD-Header.xml"/>
```

^b16

### Block 17

XML location: `/TEI[1]/text[1]/body[1]/include[3]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CO-CoreElements.xml"/>
```

^b17

### Block 18

XML location: `/TEI[1]/text[1]/body[1]/include[4]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/DS-DefaultTextStructure.xml"/>
```

^b18

### Block 19

XML location: `/TEI[1]/text[1]/body[1]/include[5]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/WD-NonStandardCharacters.xml"/>
```

^b19

### Block 20

XML location: `/TEI[1]/text[1]/body[1]/include[6]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/VE-Verse.xml"/>
```

^b20

### Block 21

XML location: `/TEI[1]/text[1]/body[1]/include[7]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/DR-PerformanceTexts.xml"/>
```

^b21

### Block 22

XML location: `/TEI[1]/text[1]/body[1]/include[8]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/TS-TranscriptionsofSpeech.xml"/>
```

^b22

### Block 23

XML location: `/TEI[1]/text[1]/body[1]/include[9]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CMC-ComputerMediatedCommunication.xml"/>
```

^b23

### Block 24

XML location: `/TEI[1]/text[1]/body[1]/include[10]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/DI-PrintDictionaries.xml"/>
```

^b24

### Block 25

XML location: `/TEI[1]/text[1]/body[1]/include[11]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/MS-ManuscriptDescription.xml"/>
```

^b25

### Block 26

XML location: `/TEI[1]/text[1]/body[1]/include[12]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/PH-PrimarySources.xml"/>
```

^b26

### Block 27

XML location: `/TEI[1]/text[1]/body[1]/include[13]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/TC-CriticalApparatus.xml"/>
```

^b27

### Block 28

XML location: `/TEI[1]/text[1]/body[1]/include[14]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/ND-NamesDates.xml"/>
```

^b28

### Block 29

XML location: `/TEI[1]/text[1]/body[1]/include[15]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/FT-TablesFormulaeGraphics.xml"/>
```

^b29

### Block 30

XML location: `/TEI[1]/text[1]/body[1]/include[16]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CC-LanguageCorpora.xml"/>
```

^b30

### Block 31

XML location: `/TEI[1]/text[1]/body[1]/include[17]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/SA-LinkingSegmentationAlignment.xml"/>
```

^b31

### Block 32

XML location: `/TEI[1]/text[1]/body[1]/include[18]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/AI-AnalyticMechanisms.xml"/>
```

^b32

### Block 33

XML location: `/TEI[1]/text[1]/body[1]/include[19]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/FS-FeatureStructures.xml"/>
```

^b33

### Block 34

XML location: `/TEI[1]/text[1]/body[1]/include[20]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/GD-GraphsNetworksTrees.xml"/>
```

^b34

### Block 35

XML location: `/TEI[1]/text[1]/body[1]/include[21]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/NH-Non-hierarchical.xml"/>
```

^b35

### Block 36

XML location: `/TEI[1]/text[1]/body[1]/include[22]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/CE-CertaintyResponsibility.xml"/>
```

^b36

### Block 37

XML location: `/TEI[1]/text[1]/body[1]/include[23]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/TD-DocumentationElements.xml"/>
```

^b37

### Block 38

XML location: `/TEI[1]/text[1]/body[1]/include[24]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/USE.xml"/>
```

^b38

### Block 39

XML location: `/TEI[1]/text[1]/back[1]/include[1]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-CLASSES-MODEL.xml"/>
```

^b39

### Block 40

XML location: `/TEI[1]/text[1]/back[1]/include[2]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-CLASSES-ATTS.xml"/>
```

^b40

### Block 41

XML location: `/TEI[1]/text[1]/back[1]/include[3]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-ELEMENTS.xml"/>
```

^b41

### Block 42

XML location: `/TEI[1]/text[1]/back[1]/include[4]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-ATTRIBUTES.xml"/>
```

^b42

### Block 43

XML location: `/TEI[1]/text[1]/back[1]/include[5]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/REF-MACROS.xml"/>
```

^b43

### Block 44

XML location: `/TEI[1]/text[1]/back[1]/include[6]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/BIB-Bibliography.xml"/>
```

^b44

### Block 45

XML location: `/TEI[1]/text[1]/back[1]/include[7]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/DEPRECATIONS.xml"/>
```

^b45

### Block 46

XML location: `/TEI[1]/text[1]/back[1]/include[8]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/PrefatoryNote.xml"/>
```

^b46

### Block 47

XML location: `/TEI[1]/text[1]/back[1]/include[9]`.

```xml
<include xmlns="http://www.w3.org/2001/XInclude" href="Guidelines/en/COL-Colophon.xml"/>
```

^b47

