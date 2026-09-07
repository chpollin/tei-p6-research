---
type: representation
source-type: document
source: '[[00_sources/tei-p5-perspronouns-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 persPronouns
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/persPronouns.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# persPronouns

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5514. Git blob: `a3f2eb4aca9b833ba78f56b807692f64fbd7251c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="namesdates" xml:id="gi-persPronouns" ident="persPronouns">
  <gloss versionDate="2020-12-10" xml:lang="en">personal pronouns</gloss>
  <desc versionDate="2020-12-10" xml:lang="en">indicates the personal pronouns used, or assumed to be used, by the individual being described.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persNamePart"/>
    <memberOf key="model.persStateLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <attList>
    <attDef ident="instant" mode="delete"/>
    <attDef ident="evidence" mode="replace" usage="rec">
      <gloss versionDate="2020-12-10" xml:lang="en">evidence</gloss>
      <desc versionDate="2020-12-10" xml:lang="en">indicates support
      for the listed personal pronouns.</desc>
      <datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="semi">
        <valItem ident="conjecture">
	  <gloss versionDate="2020-12-10" xml:lang="en">conjecture</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">The given value
	  was selected based on assumptions by someone besides the
	  person to whom this pronoun applies. As a result, the value
	  may be erroneous.</desc>
        </valItem>
        <valItem ident="selfIdentification">
	  <gloss versionDate="2020-12-10" xml:lang="en">self identification</gloss>
          <desc versionDate="2020-12-10" xml:lang="en">The given value
          has been explicitly stated or confirmed by the person to
          whom this pronoun applies.</desc>
        </valItem>
	<valItem ident="trustedThirdParty">
	  <gloss versionDate="2020-12-10" xml:lang="en">trusted third party</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">The given value
	  has been supplied by another individual trusted by the
	  encoder to know the preferences of the person to whom this
	  pronoun applies.</desc>
	</valItem>
      </valList>
    </attDef>
    <attDef ident="value" usage="rec">
      <gloss versionDate="2020-12-10" xml:lang="en">value</gloss>
      <desc versionDate="2020-12-10" xml:lang="en">supplies a
      regularized value for personal pronouns.</desc>
      <datatype minOccurs="1" maxOccurs="unbounded">
	<dataRef key="teidata.enumerated"/>
      </datatype>
      <valList type="open">
	<valItem ident="e">      
	  <gloss versionDate="2020-12-10" xml:lang="en">e</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">e/eirs</desc>
	</valItem>
	<valItem ident="he">      
	  <gloss versionDate="2020-12-10" xml:lang="en">he</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">he/him/his</desc>
	</valItem>
	<valItem ident="she">      
	  <gloss versionDate="2020-12-10" xml:lang="en">she</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">she/her/hers</desc>
	</valItem>
	<valItem ident="they">      
	  <gloss versionDate="2020-12-10" xml:lang="en">they</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">they/them/theirs</desc>
	</valItem>
      </valList>
      <remarks ident="persPronouns-attr.value-remarks" versionDate="2020-12-10" xml:lang="en">
	<p>
	  The sample values list shown here is intended to be
	  reflective of English usage. There is nothing restricting
	  users from defining lists reflective of other languages,
	  e.g. <val xml:lang="fr">elle</val>, <val xml:lang="fr">il</val>, and <val xml:lang="fr">ils</val>.
	</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-persPronouns-egXML-ze" source="#SUE">
      <person>
	<persName>
	  <forename>SUE</forename>
	  <addName>the T. rex</addName>
	</persName>
	<residence>The Field Museum. Chicago, Illinois, United States.</residence>
	<sex value="0"/>
	<persPronouns value="they">they/them</persPronouns>
	<note>
	  <cit>
	    <quote>Specimen FMNH PR 2081. Legendary Fossil. Apex
	    Predator. National Treasure. <emph style="text-transform:uppercase;      letter-spacing:0.25rem;">Murderbird.</emph></quote>
	    <bibl>SUEtheTrex, Twitter biography.
	    <ptr target="https://twitter.com/SUEtheTrex"/>. 
	    Accessed <date when="2020-03-25">March 25th, 2020</date>.</bibl>
	  </cit>
	</note>
      </person>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-persPronouns-egXML-cj" source="#LZ">
      <docAuthor>
	<persName>Lal Zimman</persName>
	<persPronouns value="he">(he/him/his)</persPronouns>
	<ref target="#Name">(FAQ)</ref>
	<persName type="IPA">[lɑɫ ˈzimn̩]</persName>
	<email>zimman at ucsb dot edu</email>
	<roleName>Assistant Professor of Linguistics</roleName>
	<roleName>Affiliated Faculty in Feminist Studies</roleName>
	<address>
	  <addrLine>South Hall 3518</addrLine>
	  <addrLine>University of California, Santa Barbara</addrLine>
	</address>
      </docAuthor>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-10" xml:lang="en">personal pronouns</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2020-12-10" xml:lang="en">indicates the personal pronouns used, or assumed to be used, by the individual being described.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.datable"/>
    <memberOf key="att.editLike"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.persNamePart"/>
    <memberOf key="model.persStateLike"/>
  </classes>
```

^b3

### Block 4

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b4

### Block 5

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2020-12-10" xml:lang="en">evidence</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2020-12-10" xml:lang="en">indicates support
      for the listed personal pronouns.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype>
        <dataRef key="teidata.enumerated"/>
      </datatype>
```

^b7

### Block 8

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="conjecture">
	  <gloss versionDate="2020-12-10" xml:lang="en">conjecture</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">The given value
	  was selected based on assumptions by someone besides the
	  person to whom this pronoun applies. As a result, the value
	  may be erroneous.</desc>
        </valItem>
        <valItem ident="selfIdentification">
	  <gloss versionDate="2020-12-10" xml:lang="en">self identification</gloss>
          <desc versionDate="2020-12-10" xml:lang="en">The given value
          has been explicitly stated or confirmed by the person to
          whom this pronoun applies.</desc>
        </valItem>
	<valItem ident="trustedThirdParty">
	  <gloss versionDate="2020-12-10" xml:lang="en">trusted third party</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">The given value
	  has been supplied by another individual trusted by the
	  encoder to know the preferences of the person to whom this
	  pronoun applies.</desc>
	</valItem>
      </valList>
```

^b8

### Block 9

XML location: `/elementSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2020-12-10" xml:lang="en">value</gloss>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2020-12-10" xml:lang="en">supplies a
      regularized value for personal pronouns.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="unbounded">
	<dataRef key="teidata.enumerated"/>
      </datatype>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[3]/valList[1]`.

```xml
<valList type="open">
	<valItem ident="e">      
	  <gloss versionDate="2020-12-10" xml:lang="en">e</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">e/eirs</desc>
	</valItem>
	<valItem ident="he">      
	  <gloss versionDate="2020-12-10" xml:lang="en">he</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">he/him/his</desc>
	</valItem>
	<valItem ident="she">      
	  <gloss versionDate="2020-12-10" xml:lang="en">she</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">she/her/hers</desc>
	</valItem>
	<valItem ident="they">      
	  <gloss versionDate="2020-12-10" xml:lang="en">they</gloss>
	  <desc versionDate="2020-12-10" xml:lang="en">they/them/theirs</desc>
	</valItem>
      </valList>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="persPronouns-attr.value-remarks" versionDate="2020-12-10" xml:lang="en">
	<p>
	  The sample values list shown here is intended to be
	  reflective of English usage. There is nothing restricting
	  users from defining lists reflective of other languages,
	  e.g. <val xml:lang="fr">elle</val>, <val xml:lang="fr">il</val>, and <val xml:lang="fr">ils</val>.
	</p>
      </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-persPronouns-egXML-ze" source="#SUE">
      <person>
	<persName>
	  <forename>SUE</forename>
	  <addName>the T. rex</addName>
	</persName>
	<residence>The Field Museum. Chicago, Illinois, United States.</residence>
	<sex value="0"/>
	<persPronouns value="they">they/them</persPronouns>
	<note>
	  <cit>
	    <quote>Specimen FMNH PR 2081. Legendary Fossil. Apex
	    Predator. National Treasure. <emph style="text-transform:uppercase;      letter-spacing:0.25rem;">Murderbird.</emph></quote>
	    <bibl>SUEtheTrex, Twitter biography.
	    <ptr target="https://twitter.com/SUEtheTrex"/>. 
	    Accessed <date when="2020-03-25">March 25th, 2020</date>.</bibl>
	  </cit>
	</note>
      </person>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-persPronouns-egXML-cj" source="#LZ">
      <docAuthor>
	<persName>Lal Zimman</persName>
	<persPronouns value="he">(he/him/his)</persPronouns>
	<ref target="#Name">(FAQ)</ref>
	<persName type="IPA">[lɑɫ ˈzimn̩]</persName>
	<email>zimman at ucsb dot edu</email>
	<roleName>Assistant Professor of Linguistics</roleName>
	<roleName>Affiliated Faculty in Feminist Studies</roleName>
	<address>
	  <addrLine>South Hall 3518</addrLine>
	  <addrLine>University of California, Santa Barbara</addrLine>
	</address>
      </docAuthor>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#NDPERSEpc"/>
  </listRef>
```

^b16

