---
type: representation
source-type: document
source: '[[00_sources/documents/practice-v1-epidoc-schema-readme-e5b68eb8.txt]]'
converter: tools.ingest_practice_v1 v1; complete original plus JSON-escaped exact
  source fragments
channel: collection
metadata:
  title: README for the EpiDoc ODD and schema (schema/README.txt)
  creator: EpiDoc community (EpiDoc/Source contributors)
  date: '2026-01-26'
  format: text/plain
  identifier: https://github.com/EpiDoc/Source/blob/e5b68eb8627ac1bc55a4f9f2bec94d8276ff74b3/schema/README.txt
  license: GPL-3.0-or-later
  confidential: false
created: '2026-09-11'
updated: '2026-09-11'
---

# README for the EpiDoc ODD and schema (schema/README.txt)

Source: `schema/README.txt` in `EpiDoc/Source` at commit `e5b68eb8627ac1bc55a4f9f2bec94d8276ff74b3`.
Source SHA-256: `b3fc307a2bb30a59a19a9151139476b972d9f1ee110b3410a7cd450dd3b71a48`, 3728 bytes.
Rights: GPL-3.0-or-later. EpiDoc Schema documentation, EpiDoc/Source; GPL.
License evidence: schema/LICENSE.txt, which the README names for license details.

The complete original is inert source text and is never executed. The
separator newline before its closing fence is not part of the original.
Reading blocks are exact source byte intervals encoded as JSON strings;
their line and byte locators refer to the original.

## Complete original

```text
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXX      README.txt for EpiDoc ODD and schema              XXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

What it is:

	The EpiDoc RelaxNG schema and the TEI ODD file from which it is generated.

License:

	The TEI Schema is copyright the TEI Consortium
	(https://tei-c.org/guidelines/licensing-and-citation/).
	To the extent that the EpiDoc ODD and schema have been customized and
	amount to transformative versions of the original schema, they are
	copyright Gabriel Bodard and the other contributors (as listed in
	tei:revisionDesc). See LICENSE.txt for license details.

Technical Requirements:

	The ODD requires the OxGarage tool to generate the RelaxNG schema.
	The schema (whose canonical released versions live at
	https://www.stoa.org/epidoc/schema/) may be used by any XML editor or
	processing environment to validate EpiDoc XML files.

How to use it:

     1.  To validate your EpiDoc files in an editor:
               If using Oxygen or similar editor to edit XML files, processing instructions such as:

               <?xml-model href="http://www.stoa.org/epidoc/schema/9.1/tei-epidoc.rng"
                         schematypens="http://relaxng.org/ns/structure/1.0"?>
               <?xml-model href="http://www.stoa.org/epidoc/schema/9.1/tei-epidoc.rng"
                         schematypens="http://purl.oclc.org/dsdl/schematron"?>

               at the top of the XML file (above the <TEI> element but below the <?xml?>
               declaration) will instruct the editor to validate against this schema
               (as RelaxNG and Schematron respectively).

               You may also point at a local copy of the tei-epidoc.rng file.

      2. To generate a new version of the schema from the ODD:
               1. edit the ODD (tei-epidoc.xml) to make any changes to the EpiDoc schema.
                  *NB* that as a matter of policy the EpiDoc schema should be a conformant
                  subset of the latest TEI schema (only exceptions being when the dev TEI ODD
                  contains changes that will not make it into the TEI release for 1-6 months).
               2. Go to https://oxgarage.tei-c.org
               3. Select "Convert from:" -> "Document" -> "ODD Document"
               4. Select "Convert to:" "RELAX NG SCHEMA"
               5. Under "Select file to convert" press "Browse" and select tei-epidoc.xml
                  from your local file system.
               6. Press "Convert".
               7. Save to your local file system as tei-epidoc.rng (or a project-specific variant).
               8. Test thoroughly (and ask for support on Markup to test) before committing as
                  canonical new EpiDoc schema.
         To generate the compiled ODD, repeat the above, only changing point (4) from
         "RELAX NG Schema" to "Compiled ODD Document"

      3. How to decide which schema to use:
               1. if your project is complete and more or less static, it is recommend you use
               the most recent numbered release of the schema as of your publication,
               because this file will remain stable indefinitely;
               2. if your project is in active development and you are comfortable following
               the changes in the community fora such as the MARKUP list, and updating
               your XML if the schema changes, you should use the /latest/ release
               (https://www.stoa.org/epidoc/schema/latest/tei-epidoc.rng)
               which will be updated whenever a new schema is released.

See https://sourceforge.net/p/epidoc/wiki/Schema/ for more information on the EpiDoc schema and how to use it.

```

## Selected source reading blocks

### r1 what it is

Locator: lines 5-7, bytes 190-278, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "What it is:\n\n\tThe EpiDoc RelaxNG schema and the TEI ODD file from which it is generated." ^r1

### r2 license

Locator: lines 9-16, bytes 280-657, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "License:\n\n\tThe TEI Schema is copyright the TEI Consortium\n\t(https://tei-c.org/guidelines/licensing-and-citation/).\n\tTo the extent that the EpiDoc ODD and schema have been customized and\n\tamount to transformative versions of the original schema, they are\n\tcopyright Gabriel Bodard and the other contributors (as listed in\n\ttei:revisionDesc). See LICENSE.txt for license details." ^r2

### r3 technical requirements

Locator: lines 18-23, bytes 659-931, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "Technical Requirements:\n\n\tThe ODD requires the OxGarage tool to generate the RelaxNG schema.\n\tThe schema (whose canonical released versions live at\n\thttps://www.stoa.org/epidoc/schema/) may be used by any XML editor or\n\tprocessing environment to validate EpiDoc XML files." ^r3

### r4 generating a new schema version

Locator: lines 41-56, bytes 1753-2914, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "2. To generate a new version of the schema from the ODD:\n               1. edit the ODD (tei-epidoc.xml) to make any changes to the EpiDoc schema.\n                  *NB* that as a matter of policy the EpiDoc schema should be a conformant\n                  subset of the latest TEI schema (only exceptions being when the dev TEI ODD\n                  contains changes that will not make it into the TEI release for 1-6 months).\n               2. Go to https://oxgarage.tei-c.org\n               3. Select \"Convert from:\" -> \"Document\" -> \"ODD Document\"\n               4. Select \"Convert to:\" \"RELAX NG SCHEMA\"\n               5. Under \"Select file to convert\" press \"Browse\" and select tei-epidoc.xml\n                  from your local file system.\n               6. Press \"Convert\".\n               7. Save to your local file system as tei-epidoc.rng (or a project-specific variant).\n               8. Test thoroughly (and ask for support on Markup to test) before committing as\n                  canonical new EpiDoc schema.\n         To generate the compiled ODD, repeat the above, only changing point (4) from\n         \"RELAX NG Schema\" to \"Compiled ODD Document\"" ^r4

### r5 choosing a schema version

Locator: lines 58-66, bytes 2922-3615, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "3. How to decide which schema to use:\n               1. if your project is complete and more or less static, it is recommend you use\n               the most recent numbered release of the schema as of your publication,\n               because this file will remain stable indefinitely;\n               2. if your project is in active development and you are comfortable following\n               the changes in the community fora such as the MARKUP list, and updating\n               your XML if the schema changes, you should use the /latest/ release\n               (https://www.stoa.org/epidoc/schema/latest/tei-epidoc.rng)\n               which will be updated whenever a new schema is released." ^r5

