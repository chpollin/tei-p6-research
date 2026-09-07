---
type: representation
source-type: document
source: '[[00_sources/tei-p5-licence-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 licence
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/licence.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# licence

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4018. Git blob: `7bc4b07a6d76c73c0f9660dac165708273284293`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-licence" ident="licence">
  <desc versionDate="2011-04-25" xml:lang="en">contains information about a licence or other legal agreement applicable to the text.</desc>
  <desc versionDate="2013-02-27" xml:lang="fr">contient des informations légales applicables au texte, notamment le contrat de licence définissant les droits d'utilisation.</desc>
  <desc versionDate="2016-11-17" xml:lang="de">beinhaltet für den Text gültige Lizenzinformationen oder andere rechtswirksame Vereinbarungen.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.pointing"/>
    <memberOf key="model.availabilityPart"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-licence-egXML-vy">
      <licence target="http://www.nzetc.org/tm/scholarly/tei-NZETC-Help.html#licensing">
        Licence: Creative Commons Attribution-Share Alike 3.0 New Zealand Licence
      </licence>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-licence-egXML-nl">
      <licence target="http://creativecommons.org/licenses/by/3.0/deed.fr">
        Creative Commons Attribution 3.0 non transposé (CC BY 3.0)
      </licence>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-licence-egXML-pk">
      <licence target="http://creativecommons.org/licenses/by-sa/2.0/"> Ce document
                        est publié librement sur le web à destination de la communauté scientifique
                        dans le cadre de la licence Creative Commons « Paternité-Pas d’Utilisation
                        Commerciale-Partage des Conditions Initiales à l’Identique 2.0 France ».
                      </licence>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-licence-egXML-zt">
      <availability>
        <licence target="http://creativecommons.org/licenses/by/3.0/" notBefore="2013-01-01">
          <p>The Creative Commons Attribution 3.0 Unported (CC BY 3.0) Licence 
	  applies to this document.</p>
          <p>The licence was added on January 1, 2013.</p>
        </licence>
      </availability>
    </egXML>
  </exemplum>
  <remarks ident="licence-remarks" versionDate="2011-04-25" xml:lang="en">
    <p>A <gi>licence</gi> element should be supplied for each licence
    agreement applicable to the text in question. The
    <att>target</att> attribute may be used to reference a full
    version of the licence. The <att>when</att>, <att>notBefore</att>,
    <att>notAfter</att>, <att>from</att> or <att>to</att> attributes
    may be used in combination to indicate the date or dates of
    applicability of the licence.</p>
  </remarks>
  <remarks ident="licence-remarks" versionDate="2016-11-17" xml:lang="de">
      <p>
          Das <gi>licence</gi>-Element soll für jede Lizenzvereinbarung, 
          die sich auf den Text bezieht, angegeben werden. Das <att>target</att>-Attribut 
          kann verwendet werden, um auf eine vollständige Version der Lizenz zu referenzieren. Die Attribute <att>when</att>, <att>notBefore</att>, <att>notAfter</att>, <att>from</att> oder <att>to</att> können in Kombination verwendet werden, um den Gültigkeitszeitraum der Lizenz anzugeben. 
      </p>
  </remarks>
  <listRef>
    <ptr target="#HD24"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-04-25" xml:lang="en">contains information about a licence or other legal agreement applicable to the text.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2013-02-27" xml:lang="fr">contient des informations légales applicables au texte, notamment le contrat de licence définissant les droits d'utilisation.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2016-11-17" xml:lang="de">beinhaltet für den Text gültige Lizenzinformationen oder andere rechtswirksame Vereinbarungen.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.pointing"/>
    <memberOf key="model.availabilityPart"/>
  </classes>
```

^b4

### Block 5

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b5

### Block 6

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-licence-egXML-vy">
      <licence target="http://www.nzetc.org/tm/scholarly/tei-NZETC-Help.html#licensing">
        Licence: Creative Commons Attribution-Share Alike 3.0 New Zealand Licence
      </licence>
    </egXML>
  </exemplum>
```

^b6

### Block 7

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-licence-egXML-nl">
      <licence target="http://creativecommons.org/licenses/by/3.0/deed.fr">
        Creative Commons Attribution 3.0 non transposé (CC BY 3.0)
      </licence>
    </egXML>
  </exemplum>
```

^b7

### Block 8

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-licence-egXML-pk">
      <licence target="http://creativecommons.org/licenses/by-sa/2.0/"> Ce document
                        est publié librement sur le web à destination de la communauté scientifique
                        dans le cadre de la licence Creative Commons « Paternité-Pas d’Utilisation
                        Commerciale-Partage des Conditions Initiales à l’Identique 2.0 France ».
                      </licence>
    </egXML>
  </exemplum>
```

^b8

### Block 9

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-licence-egXML-zt">
      <availability>
        <licence target="http://creativecommons.org/licenses/by/3.0/" notBefore="2013-01-01">
          <p>The Creative Commons Attribution 3.0 Unported (CC BY 3.0) Licence 
	  applies to this document.</p>
          <p>The licence was added on January 1, 2013.</p>
        </licence>
      </availability>
    </egXML>
  </exemplum>
```

^b9

### Block 10

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="licence-remarks" versionDate="2011-04-25" xml:lang="en">
    <p>A <gi>licence</gi> element should be supplied for each licence
    agreement applicable to the text in question. The
    <att>target</att> attribute may be used to reference a full
    version of the licence. The <att>when</att>, <att>notBefore</att>,
    <att>notAfter</att>, <att>from</att> or <att>to</att> attributes
    may be used in combination to indicate the date or dates of
    applicability of the licence.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="licence-remarks" versionDate="2016-11-17" xml:lang="de">
      <p>
          Das <gi>licence</gi>-Element soll für jede Lizenzvereinbarung, 
          die sich auf den Text bezieht, angegeben werden. Das <att>target</att>-Attribut 
          kann verwendet werden, um auf eine vollständige Version der Lizenz zu referenzieren. Die Attribute <att>when</att>, <att>notBefore</att>, <att>notAfter</att>, <att>from</att> oder <att>to</att> können in Kombination verwendet werden, um den Gültigkeitszeitraum der Lizenz anzugeben. 
      </p>
  </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD24"/>
  </listRef>
```

^b12

