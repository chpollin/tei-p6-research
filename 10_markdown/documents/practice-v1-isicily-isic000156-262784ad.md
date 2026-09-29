---
type: representation
source-type: document
source: '[[00_sources/documents/practice-v1-isicily-isic000156-262784ad.xml]]'
converter: tools.ingest_practice_v1 v1; complete original plus JSON-escaped exact
  source fragments
channel: collection
metadata:
  title: I.Sicily inscription ISic000156 (inscriptions/ISic000156.xml)
  creator: I.Sicily project, University of Oxford
  date: '2026-07-29'
  format: application/xml
  identifier: https://github.com/ISicily/ISicily/blob/262784ad8b4d4ee5a203abc0a772ae3eea289997/inscriptions/ISic000156.xml
  license: CC-BY-4.0
  confidential: false
created: '2026-09-11'
updated: '2026-09-11'
---

# I.Sicily inscription ISic000156 (inscriptions/ISic000156.xml)

Source: `inscriptions/ISic000156.xml` in `ISicily/ISicily` at commit `262784ad8b4d4ee5a203abc0a772ae3eea289997`.
Source SHA-256: `e70909d4b869dc2c3b340c6d4564c510bfd8c555d2f883df9007c9aedcc09a48`, 13766 bytes.
Rights: CC-BY-4.0. I.Sicily, CC BY 4.0; editors and contributors are named in the source titleStmt.
License evidence: licence.txt at the pinned commit; publicationStmt/availability/licence in the file.

The complete original is inert source text and is never executed. The
separator newline before its closing fence is not part of the original.
Reading blocks are exact source byte intervals encoded as JSON strings;
their line and byte locators refer to the original.

## Complete original

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="https://epidoc.stoa.org/schema/latest/tei-epidoc.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="../schematron/ircyr-checking.sch" schematypens="http://purl.oclc.org/dsdl/schematron"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:xi="http://www.w3.org/2001/XInclude" xml:lang="en">
    <teiHeader>
        <fileDesc>
            <titleStmt>
                <title>Fragmentary funerary inscription for a member of the gens Coponia</title>
                <editor ref="#JP">Jonathan Prag</editor>
                <principal ref="#JP">Jonathan Prag</principal>
                <funder>John Fell OUP Research Fund</funder>
                <funder>
                    <ref target="https://cordis.europa.eu/project/id/885040">ERC Advanced Grant no.885040</ref>
                </funder>
                <respStmt>
                    <name xml:id="JP" ref="http://orcid.org/0000-0003-3819-8537">Jonathan Prag</name>
                    <resp>original data collection and editing</resp>
                </respStmt>
                <respStmt>
                    <name xml:id="JCu" ref="http://orcid.org/0000-0002-6686-3728">James Cummings</name>
                    <resp>conversion to EpiDoc</resp>
                </respStmt>
                <respStmt>
                    <name xml:id="TA" ref="https://orcid.org/0000-0001-8417-7089">Tuuli Ahlholm</name>
                    <resp>EpiDoc editing</resp>
                </respStmt>
                <respStmt>
                    <name xml:id="SS" ref="https://orcid.org/0000-0003-3914-9569">Simona Stoyanova</name>
                    <resp>standardisation of template and tidying up encoding</resp>
                </respStmt>
                <respStmt>
                    <name xml:id="VF" ref="https://orcid.org/0000-0001-6302-3726">Victoria Fendel</name>
                    <resp>lemmatization and linguistic analysis</resp>
                </respStmt>
            </titleStmt>
            <publicationStmt>
                <authority>I.Sicily</authority>
                <idno type="filename">ISic000156</idno>
                <idno type="TM">493964</idno>
                <idno type="EDR"/>
                <idno type="EDH"/>
                <idno type="EDCS">10900649</idno>
                <idno type="PHI"/>
                <idno type="URI">http://sicily.classics.ox.ac.uk/inscription/ISic000156</idno>
                <idno type="DOI" when="2020-12-17">10.5281/zenodo.4334356</idno>
                <availability>
                    <licence target="http://creativecommons.org/licenses/by/4.0/">Licensed under a Creative Commons-Attribution 4.0 licence.</licence>
                </availability>
            </publicationStmt>
            <sourceDesc>
                <msDesc>
                    <msIdentifier>
                        <country>Italy</country>
                        <region>Sicily</region>
                        <settlement>Termini</settlement>
                        <repository role="museum" ref="http://sicily.classics.ox.ac.uk/museum/066">Museo Civico Baldassare Romano</repository>
                        <!--No inventory number found-->
                        <!--Adding location for old id numbers if available-->
                        <altIdentifier>
                            <settlement/>
                            <repository/>
                            <idno type="old"/>
                        </altIdentifier>
                    </msIdentifier>
                    <msContents>
                        <textLang mainLang="la">Latin</textLang>
                    </msContents>
                    <physDesc>
                        <objectDesc>
                            <supportDesc>
                                <support>
                                    <p>Fragment of a stone plaque, but Ferrua does not record the type of stone</p>
                                    <material ana="#material.inorganic.stone" type="stone.unspecified" subtype="unverified" ref="http://www.eagle-network.eu/voc/material/lod/2.html">stone</material>
                                    <objectType ana="#object.plaque" ref="http://www.eagle-network.eu/voc/objtyp/lod/259">plaque</objectType>
                                    <dimensions><!--Ferrua-->
                                        <height unit="cm">11</height>
                                        <width unit="cm">14.5</width>
                                        <depth unit="cm">2.2</depth>
                                    </dimensions>
                                </support>
                                <condition/>
                            </supportDesc>
                            <layoutDesc>
                                <layout>
                                    <rs ana="#execution.chiselled" ref="http://www.eagle-network.eu/voc/writing/lod/1">chiselled</rs>
                                    <damage/>
                                </layout>
                            </layoutDesc>
                        </objectDesc>
                        <handDesc>
                            <handNote>
                                <p>Ferrua records the presence of a hedera in the line 1 heading.</p>
                                <locus from="line1" to="line1">Line 1</locus>
                                <dimensions type="letterHeight">
                                    <height unit="mm"/>
                                </dimensions>
                                <locus from="line1" to="line2">Interlineation line 1 to 2</locus>
                                <dimensions type="interlinear">
                                    <height unit="mm"/>
                                </dimensions>
                            </handNote>
                        </handDesc>
                    </physDesc>
                    <history>
                        <origin>
                            <origPlace><region>Sicilia</region>
                                <placeName type="ancient" ref="http://pleiades.stoa.org/places/462513">Thermae Himeraeae</placeName>
                                <placeName type="modern" ref="http://sws.geonames.org/6539140">Termini Imerese</placeName>
                                <geo>37.98365, 13.69555</geo>
                            </origPlace>
                            <origDate datingMethod="#julian" notBefore-custom="0001" notAfter-custom="0250" cert="low">Imperial</origDate>
                        </origin>
                        <provenance type="found" subtype="discovered" notAfter="1941">Recorded by Ferrua 1941, who notes that the stone's origin as Termini was recorded on the reverse of the stone; it was already lost when Bivona studied the collection.</provenance>
                        <provenance type="observed" subtype="autopsied">None</provenance>
                        <provenance type="not-observed" subtype="lost">Lost.</provenance>
                    </history>
                </msDesc>
            </sourceDesc>
        </fileDesc>
        <encodingDesc>
            <p>Encoded following the latest EpiDoc guidelines</p>
            <xi:include href="../alists/ISicily-taxonomies.xml">
                <xi:fallback>
                    <p>Taxonomies for ISicily controlled values</p>
                </xi:fallback>
            </xi:include>
            <xi:include href="../alists/charDecl.xml">
                <xi:fallback>
                    <p>ISicily glyphs authority list</p>
                </xi:fallback>
            </xi:include>
        </encodingDesc>
        <profileDesc>
            <calendarDesc>
                <calendar xml:id="julian">
                    <p>Julian Calendar</p>
                </calendar>
            </calendarDesc>
            <langUsage>
                <language ident="en">English</language>
                <language ident="it">Italian</language>
                <language ident="grc">Ancient Greek</language>
                <language ident="la">Latin</language>
                <language ident="he">Hebrew</language>
                <language ident="phn">Phoenician</language>
                <language ident="xpu">Punic</language>
                <language ident="osc">Oscan</language>
                <language ident="xly">Elymian</language>
                <language ident="scx">Sikel</language>
                <language ident="sxc">Sikan</language>
            </langUsage>
            <textClass>
                <keywords scheme="https://ontology.inscriptiones.org/type_of_inscription">
                    <term ana="#function.funerary" ref="https://ontology.inscriptiones.org/type_of_inscription/Funerary">funerary</term>
                </keywords>
            </textClass>
        </profileDesc>
        <revisionDesc status="edited">
            <listChange>
                <change when="2016-12-03" who="#JCu">James Cummings autogenerated EpiDoc output from database</change>
                <change when="2019-05-24" who="#TA">Tuuli Ahlholm encoded the text and added an apparatus and a translation.</change>
                <change when="2020-10-05" who="#SS">Simona Stoyanova normalised Unicode</change>
                <change when="2020-10-08" who="#SS">Simona Stoyanova updated list of languages</change>
                <change when="2020-11-20" who="#SS">Simona Stoyanova added EDCS numbers</change>
                <change when="2020-11-26" who="#SS">Simona Stoyanova restructured bibliography</change>
                <change when="2020-12-17" who="#JP">Updated Zenodo DOI</change>
                <change when="2021-01-19" who="#SS">renumbered files, uris and references</change>
                <change when="2024-05-08" who="#JP">Jonathan Prag revised from publication</change>
                <change when="2025-07-24" who="#VF">Victoria Fendel's lemmatizations were added</change>
            </listChange>
        </revisionDesc>
    </teiHeader>
    <facsimile>
        <surface/><!-- 
        <surface type="front">
            <graphic n="screen" url="ISic000156_tiled.tif" height="3680px" width="5520px">
                <desc>I.Sicily with the permission of the Assessorato Regionale dei Beni Culturali e dell’Identità Siciliana - Dipartimento dei Beni Culturali e dell’Identità Siciliana</desc>
            </graphic>
            <graphic n="print" url="ISic000156.jpg" height="3680px" width="5520px">
                <desc>I.Sicily with the permission of the Assessorato Regionale dei Beni Culturali e dell’Identità Siciliana - Dipartimento dei Beni Culturali e dell’Identità Siciliana</desc>
            </graphic>
         </surface> -->
    </facsimile>
    <text>
        <body>
            <div type="edition" subtype="primary" xml:space="preserve" xml:lang="la" resp="#TA #JP">
                <ab>
                    <lb n="1"/><w n="5"><expan><abbr>D</abbr><ex>is</ex></expan></w> <g ref="#ivy-leaf" n="10">❦</g> <w n="15"><supplied reason="lost"><expan><abbr>M</abbr><ex>anibus</ex></expan></supplied></w>
                    <lb n="2"/><persName type="attested"><name><w part="I" n="20">Copo<supplied reason="lost">ni</supplied></w></name></persName> <gap reason="lost" extent="unknown" unit="character" n="25"/>
                </ab>
            </div>
            <div type="edition" subtype="simple-lemmatized" resp="#VF">
                <ab>
                    <w n="5" lemma="dis">Dis</w>
                    <w n="15" lemma="manes">Manibus</w>
                    <w n="20" lemma="Coponius">Coponi</w>
                    <gap reason="lost" extent="unknown" unit="character" n="25"><desc>[-?-]</desc></gap>
                </ab>
            </div>
            <div type="apparatus">
                <listApp>
                    <app>
                        <note>Text of Ferrua</note>
                    </app>
                </listApp>
            </div>
            <div type="translation" xml:lang="en" resp="#TA">
                <p>To the Shades of the Underworld. Copo[ni---].</p>
            </div>
            <div type="commentary">
                <p/>
            </div>
            <div type="bibliography">
                <listBibl type="edition">
                    <bibl type="bulletin" n="AE">
                        <date>1994</date>
                        <citedRange>776</citedRange>
                        <ptr target="https://www.zotero.org/groups/382445/items/R46KDTZX"/>
                        <ref target="https://biblio.inscriptiones.org/epig10001283">https://biblio.inscriptiones.org/epig10001283</ref>
                    </bibl>
                    <bibl type="corpus" n="ILMusTermini">
                         <author>Bivona</author>
                         <date>1994</date> 
                        <citedRange>77</citedRange>
                        <ptr target="https://www.zotero.org/groups/382445/items/JCV85C79"/>
                        <ref target="https://biblio.inscriptiones.org/epig10002137">https://biblio.inscriptiones.org/epig10002137</ref>
                    </bibl>
                    <bibl>
                        <author>Ferrua</author>
                        <date>1941</date>
                        <citedRange>264 no.28c</citedRange>
                        <ptr target="https://www.zotero.org/groups/382445/items/P7QQ9SB6"/>
                        <ref target="https://biblio.inscriptiones.org/epig10002655">https://biblio.inscriptiones.org/epig10002655</ref>
                    </bibl>
                </listBibl>
                <listBibl type="discussion">
                    <bibl/>
                </listBibl>
            </div>
        </body>
    </text>
</TEI>
```

## Selected source reading blocks

### r1 schema association processing instructions

Locator: lines 2-3, bytes 39-292, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<?xml-model href=\"https://epidoc.stoa.org/schema/latest/tei-epidoc.rng\" type=\"application/xml\" schematypens=\"http://relaxng.org/ns/structure/1.0\"?>\n<?xml-model href=\"../schematron/ircyr-checking.sch\" schematypens=\"http://purl.oclc.org/dsdl/schematron\"?>" ^r1

### r2 file licence

Locator: lines 46-48, bytes 2567-2764, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<availability>\n                    <licence target=\"http://creativecommons.org/licenses/by/4.0/\">Licensed under a Creative Commons-Attribution 4.0 licence.</licence>\n                </availability>" ^r2

### r3 date of origin

Locator: lines 111-111, bytes 6446-6556, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<origDate datingMethod=\"#julian\" notBefore-custom=\"0001\" notAfter-custom=\"0250\" cert=\"low\">Imperial</origDate>" ^r3

### r4 encoding description with XIncludes

Locator: lines 120-132, bytes 7149-7672, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<encodingDesc>\n            <p>Encoded following the latest EpiDoc guidelines</p>\n            <xi:include href=\"../alists/ISicily-taxonomies.xml\">\n                <xi:fallback>\n                    <p>Taxonomies for ISicily controlled values</p>\n                </xi:fallback>\n            </xi:include>\n            <xi:include href=\"../alists/charDecl.xml\">\n                <xi:fallback>\n                    <p>ISicily glyphs authority list</p>\n                </xi:fallback>\n            </xi:include>\n        </encodingDesc>" ^r4

### r5 revision status

Locator: lines 158-158, bytes 8870-8900, start-tag, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<revisionDesc status=\"edited\">" ^r5

### r6 primary edition

Locator: lines 186-191, bytes 10799-11370, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<div type=\"edition\" subtype=\"primary\" xml:space=\"preserve\" xml:lang=\"la\" resp=\"#TA #JP\">\n                <ab>\n                    <lb n=\"1\"/><w n=\"5\"><expan><abbr>D</abbr><ex>is</ex></expan></w> <g ref=\"#ivy-leaf\" n=\"10\">❦</g> <w n=\"15\"><supplied reason=\"lost\"><expan><abbr>M</abbr><ex>anibus</ex></expan></supplied></w>\n                    <lb n=\"2\"/><persName type=\"attested\"><name><w part=\"I\" n=\"20\">Copo<supplied reason=\"lost\">ni</supplied></w></name></persName> <gap reason=\"lost\" extent=\"unknown\" unit=\"character\" n=\"25\"/>\n                </ab>\n            </div>" ^r6

