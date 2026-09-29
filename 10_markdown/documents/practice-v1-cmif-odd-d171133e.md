---
type: representation
source-type: document
source: '[[00_sources/documents/practice-v1-cmif-odd-d171133e.odd]]'
converter: tools.ingest_practice_v1 v1; complete original plus JSON-escaped exact
  source fragments
channel: collection
metadata:
  title: CMIF ODD (odd/cmi-customization.odd)
  creator: TEI Correspondence SIG
  date: '2025-02-26'
  format: application/xml
  identifier: https://github.com/TEI-Correspondence-SIG/CMIF/blob/d171133e2ca7a0b987ba0564577ec79077b8d908/odd/cmi-customization.odd
  license: CC-BY-4.0 OR BSD-2-Clause
  confidential: false
created: '2026-09-11'
updated: '2026-09-11'
---

# CMIF ODD (odd/cmi-customization.odd)

Source: `odd/cmi-customization.odd` in `TEI-Correspondence-SIG/CMIF` at commit `d171133e2ca7a0b987ba0564577ec79077b8d908`.
Source SHA-256: `768f145ea785f53aa1753e8477ff8434dceee5c7570ed2daf4dd0abdd4de6890`, 12964 bytes.
Rights: CC-BY-4.0 OR BSD-2-Clause. Correspondence Metadata Interchange Format (CMIF) 1.1, TEI Correspondence SIG 2015-2025, CC BY 4.0 or BSD-2-Clause.
License evidence: LICENSE CC-BY, LICENSE BSD 2-Clause, README.md and CITATION.cff at the pinned commit.

The complete original is inert source text and is never executed. The
separator newline before its closing fence is not part of the original.
Reading blocks are exact source byte intervals encoded as JSON strings;
their line and byte locators refer to the original.

## Complete original

```xml
<?xml version="1.0" encoding="utf-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0">
    <teiHeader>
        <fileDesc>
            <titleStmt>
                <title>Correspondence Metadata Interchange Format</title>
                <title type="version">1.1</title>
                <author>TEI Correspondence SIG</author>
            </titleStmt>
            <publicationStmt>
                <authority>TEI Correspondence SIG</authority>
                <availability>
                    <licence>
                        <p>CC+BY and BSD-2 licences</p>
                    </licence>
                </availability>
            </publicationStmt>
            <sourceDesc>
                <p>Born digital</p>
            </sourceDesc>
        </fileDesc>
        <revisionDesc>
            <change when="2025-02-26">
                <persName>Stefan Dumont</persName>
                <desc>Restrict @evidence to "conjecture" and @cert to "low"</desc>
            </change>
            <change when="2025-01-08">
                <persName>Stefan Dumont</persName>
                <desc>Restrict correspAction/@type to sent/received.</desc>
            </change>
            <change when="2024-10-18">
                <persName>Klaus Rettinghaus</persName>
                <desc>Allow text content in date.</desc>
            </change>
            <change when="2023-08-05">
                <persName>Klaus Rettinghaus</persName>
                <desc>Restrict type of correspAction.</desc>
            </change>
            <change when="2023-05-08">
                <persName>Klaus Rettinghaus</persName>
                <desc>Add editorial attributes to children of correspAction.</desc>
            </change>
            <change when="2015-02-18">
                <persName>Peter Stadler</persName>
                <desc>Updated CMIF to build on the latest Jenkins P5 build. Proposal namespaces are gone.</desc>
            </change>
            <change when="2015-02-11">
                <persName>Stefan Dumont</persName>
                <desc>Updated CMIF to current state of proposal and correspSearch. teiHeader//titleStmt/respStmt replaces editor.</desc>
            </change>
            <change when="2014-07-02">
                <persName>Peter Stadler</persName>
                <desc>Initial creation of Correspondence Interchange Format schema.</desc>
            </change>
        </revisionDesc>
    </teiHeader>
    <text>
        <body>
            <p>This customization builds on the correspDesc element. 
                It aims to define an interchange format for correspondence projects. </p>
        </body>
        <back>
            <div>
                <head>Formal Specification</head>
                <schemaSpec ident="cmi-customization" start="TEI" status="stable">
                    <moduleRef key="tei"/>
                    <moduleRef key="textstructure" include="body TEI text"/>
                    <moduleRef key="core" include="bibl date editor email name note p ref title publisher"/>
                    <moduleRef key="header" include="availability correspDesc correspAction correspContext fileDesc idno licence profileDesc publicationStmt sourceDesc teiHeader titleStmt"/>
                    <moduleRef key="namesdates" include="persName orgName placeName" />
                    
                    <classSpec ident="att.editLike" module="tei" type="atts" mode="replace">
                        <attList>
                            <attDef ident="evidence" usage="opt">
                                <desc>The person is not stated in the source itself, but is based on the knowledge/research of the scholar.</desc>
                                <valList type="closed">
                                    <valItem ident="conjecture"/>  
                                </valList>
                            </attDef>
                        </attList>
                    </classSpec>
                    
                    <classSpec ident="att.global.responsibility" module="tei" type="atts" mode="replace">
                        <attList>
                            <attDef ident="cert" usage="opt">
                                <desc>The attribution of this person, place or date to this letter is uncertain.</desc>
                                <valList type="closed">
                                    <valItem ident="low"></valItem>
                                </valList>
                            </attDef>
                        </attList>
                    </classSpec>
                                        
                    <elementSpec ident="titleStmt" mode="change" module="header">
                        <content>
                            <elementRef key="title"/>
                            <elementRef key="editor" maxOccurs="unbounded"/><!-- oneOrMore -->
                        </content>
                    </elementSpec>

                    <elementSpec ident="publicationStmt" mode="change" module="header">
                        <content>
                            <elementRef key="publisher" maxOccurs="unbounded" />
                            <elementRef key="idno"/>
                            <elementRef key="date"/>
                            <elementRef key="availability"/>
                        </content>
                    </elementSpec>
                    
                    <elementSpec ident="licence" mode="change" module="header">
                        <classes mode="replace">
                            <memberOf key="att.pointing"/>
                            <memberOf key="model.availabilityPart"/>
                        </classes>
                        <attList>
                            <attDef ident="targetLang" mode="delete"/>
                            <attDef ident="evaluate" mode="delete"/>
                            <attDef ident="target" usage="req" mode="change"/>
                        </attList>
                    </elementSpec>

                    <elementSpec ident="sourceDesc" mode="change" module="header">
                        <content>
                            <elementRef key="bibl" maxOccurs="unbounded"/><!-- oneOrMore -->
                        </content>
                    </elementSpec>
                    
                    <elementSpec ident="bibl" module="core" mode="change">
                        <attList>
                            <attDef ident="type" mode="change" usage="req">
                                <valList mode="replace" type="closed">
                                    <valItem ident="online">
                                        <desc>The described edition is an online only publication</desc>
                                    </valItem>
                                    <valItem ident="print">
                                        <desc>The described edition is a print only publication</desc>
                                    </valItem>
                                    <valItem ident="hybrid">
                                        <desc>The described edition is both available online and printed</desc>
                                    </valItem>
                                </valList>
                            </attDef>
                            <attDef ident="xml:id" mode="change" usage="req">
                                <desc>Should contain a UUID, which is static, i.e. doesn't change when the CMIF
                                is change and/or regenerated. Be aware that the UUID have to begin with
                                a letter, since the definition of @xml:id requires that.</desc>
                            </attDef>
                        </attList>
                    </elementSpec>

                    <elementSpec ident="correspAction" mode="change" module="header">
                        <content>
                            <classRef key="model.correspActionPart" minOccurs="1" maxOccurs="unbounded"/>
                        </content>
                        <attList>
                            <attDef ident="type" mode="change" usage="req">
                                <valList mode="replace" type="closed">
                                    <valItem ident="sent">
                                        <desc>information concerning the sending or dispatch of a message.</desc>
                                    </valItem>
                                    <valItem ident="received">
                                        <desc>information concerning the receipt of a message.</desc>
                                    </valItem>
                                </valList>
                            </attDef>
                        </attList>
                    </elementSpec>

                    <elementSpec ident="date" mode="change" module="core">
                        <classes mode="replace">
                            <memberOf key="att.datable.w3c"/>
                            <memberOf key="att.editLike"/>
                            <memberOf key="att.global.responsibility"/>
                            <memberOf key="model.correspActionPart"/>
                        </classes>
                        <content>
                            <textNode/>
                        </content>
                    </elementSpec>
                    
                    <elementSpec ident="idno" mode="replace" module="header">
                        <desc xml:lang="en" versionDate="2015-10-16">Provides the URL of the CMI file</desc>
                        <content>
                            <dataRef key="teidata.pointer"/>
                        </content>
                        <attList>
                            <attDef ident="type" mode="add" usage="req">
                                <valList mode="add" type="closed">
                                    <valItem ident="url"/>
                                </valList>
                            </attDef>
                        </attList>
                        <exemplum>
                            <egXML xmlns="http://www.tei-c.org/ns/Examples">
                                <idno type="url">http://weber-gesamtausgabe.de/correspDesc.xml</idno>
                            </egXML>
                        </exemplum>
                    </elementSpec>
                    
                    <elementSpec ident="persName" mode="change" module="namesdates">
                        <classes mode="replace">
                            <memberOf key="model.nameLike.agent"/>
                            <memberOf key="att.canonical"/>
                            <memberOf key="att.editLike"/>
                            <memberOf key="att.global.responsibility"/>
                        </classes>
                        <content>
                            <textNode/>
                        </content>
                        <attList>
                            <attDef ident="key" mode="delete"/>
                            <attDef ident="ref" mode="change" usage="rec"/>
                        </attList>
                    </elementSpec>
                    
                    <elementSpec ident="orgName" mode="change" module="namesdates">
                        <classes mode="replace">
                            <memberOf key="model.nameLike.agent"/>
                            <memberOf key="att.canonical"/>
                            <memberOf key="att.editLike"/>
                            <memberOf key="att.global.responsibility"/>
                        </classes>
                        <content>
                            <textNode/>
                        </content>
                        <attList>
                            <attDef ident="key" mode="delete"/>
                            <attDef ident="ref" mode="change" usage="rec"/>
                        </attList>
                    </elementSpec>
                    
                    <elementSpec ident="placeName" mode="change" module="namesdates">
                        <classes mode="replace">
                            <memberOf key="model.nameLike.agent"/>
                            <memberOf key="att.canonical"/>
                            <memberOf key="att.editLike"/>
                            <memberOf key="att.global.responsibility"/>
                        </classes>
                        <content>
                            <textNode/>
                        </content>
                        <attList>
                            <attDef ident="key" mode="delete"/>
                            <attDef ident="ref" mode="change" usage="rec"/>
                        </attList>
                    </elementSpec>
                                      
                </schemaSpec>
            </div>
        </back>
    </text>
</TEI>

```

## Selected source reading blocks

### r1 schemaSpec start and module selection

Locator: lines 65-70, bytes 2778-3352, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<schemaSpec ident=\"cmi-customization\" start=\"TEI\" status=\"stable\">\n                    <moduleRef key=\"tei\"/>\n                    <moduleRef key=\"textstructure\" include=\"body TEI text\"/>\n                    <moduleRef key=\"core\" include=\"bibl date editor email name note p ref title publisher\"/>\n                    <moduleRef key=\"header\" include=\"availability correspDesc correspAction correspContext fileDesc idno licence profileDesc publicationStmt sourceDesc teiHeader titleStmt\"/>\n                    <moduleRef key=\"namesdates\" include=\"persName orgName placeName\" />" ^r1

### r2 replaced att.editLike

Locator: lines 72-81, bytes 3394-3986, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<classSpec ident=\"att.editLike\" module=\"tei\" type=\"atts\" mode=\"replace\">\n                        <attList>\n                            <attDef ident=\"evidence\" usage=\"opt\">\n                                <desc>The person is not stated in the source itself, but is based on the knowledge/research of the scholar.</desc>\n                                <valList type=\"closed\">\n                                    <valItem ident=\"conjecture\"/>  \n                                </valList>\n                            </attDef>\n                        </attList>\n                    </classSpec>" ^r2

### r3 changed correspAction

Locator: lines 151-167, bytes 7857-8861, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<elementSpec ident=\"correspAction\" mode=\"change\" module=\"header\">\n                        <content>\n                            <classRef key=\"model.correspActionPart\" minOccurs=\"1\" maxOccurs=\"unbounded\"/>\n                        </content>\n                        <attList>\n                            <attDef ident=\"type\" mode=\"change\" usage=\"req\">\n                                <valList mode=\"replace\" type=\"closed\">\n                                    <valItem ident=\"sent\">\n                                        <desc>information concerning the sending or dispatch of a message.</desc>\n                                    </valItem>\n                                    <valItem ident=\"received\">\n                                        <desc>information concerning the receipt of a message.</desc>\n                                    </valItem>\n                                </valList>\n                            </attDef>\n                        </attList>\n                    </elementSpec>" ^r3

### r4 replaced idno

Locator: lines 181-198, bytes 9470-10437, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<elementSpec ident=\"idno\" mode=\"replace\" module=\"header\">\n                        <desc xml:lang=\"en\" versionDate=\"2015-10-16\">Provides the URL of the CMI file</desc>\n                        <content>\n                            <dataRef key=\"teidata.pointer\"/>\n                        </content>\n                        <attList>\n                            <attDef ident=\"type\" mode=\"add\" usage=\"req\">\n                                <valList mode=\"add\" type=\"closed\">\n                                    <valItem ident=\"url\"/>\n                                </valList>\n                            </attDef>\n                        </attList>\n                        <exemplum>\n                            <egXML xmlns=\"http://www.tei-c.org/ns/Examples\">\n                                <idno type=\"url\">http://weber-gesamtausgabe.de/correspDesc.xml</idno>\n                            </egXML>\n                        </exemplum>\n                    </elementSpec>" ^r4

### r5 changed persName

Locator: lines 200-214, bytes 10479-11238, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<elementSpec ident=\"persName\" mode=\"change\" module=\"namesdates\">\n                        <classes mode=\"replace\">\n                            <memberOf key=\"model.nameLike.agent\"/>\n                            <memberOf key=\"att.canonical\"/>\n                            <memberOf key=\"att.editLike\"/>\n                            <memberOf key=\"att.global.responsibility\"/>\n                        </classes>\n                        <content>\n                            <textNode/>\n                        </content>\n                        <attList>\n                            <attDef ident=\"key\" mode=\"delete\"/>\n                            <attDef ident=\"ref\" mode=\"change\" usage=\"rec\"/>\n                        </attList>\n                    </elementSpec>" ^r5

### r6 revision of 2025-02-26

Locator: lines 23-26, bytes 838-1020, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<change when=\"2025-02-26\">\n                <persName>Stefan Dumont</persName>\n                <desc>Restrict @evidence to \"conjecture\" and @cert to \"low\"</desc>\n            </change>" ^r6

