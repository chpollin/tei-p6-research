---
type: representation
source-type: document
source: '[[00_sources/documents/practice-v1-correspsearch-check-566b2d29.xql]]'
converter: tools.ingest_practice_v1 v1; complete original plus JSON-escaped exact
  source fragments
channel: collection
metadata:
  title: correspSearch CMIF check service (api/v2.0/services/check/index.xql)
  creator: Berlin-Brandenburg Academy of Sciences and Humanities (correspSearch)
  date: '2024-07-20'
  format: text/plain
  identifier: https://github.com/correspSearch/csAPI/blob/566b2d29233e3be332dc749266558cb7383cd31d/api/v2.0/services/check/index.xql
  license: LGPL-3.0-or-later
  confidential: false
created: '2026-09-11'
updated: '2026-09-11'
---

# correspSearch CMIF check service (api/v2.0/services/check/index.xql)

Source: `api/v2.0/services/check/index.xql` in `correspSearch/csAPI` at commit `566b2d29233e3be332dc749266558cb7383cd31d`.
Source SHA-256: `6fad8c20890525f3febba7586e58f19aa39a9b2b6c8fb9b963740eca3f19c4bf`, 867 bytes.
Rights: LGPL-3.0-or-later. csAPI, correspSearch, Berlin-Brandenburg Academy of Sciences and Humanities 2024, LGPL-3.0-or-later.
License evidence: LICENSE, README.md section License and CITATION.cff at the pinned commit.

The complete original is inert source text and is never executed. The
separator newline before its closing fence is not part of the original.
Reading blocks are exact source byte intervals encoded as JSON strings;
their line and byte locators refer to the original.

## Complete original

```xquery
xquery version "3.0";

import module namespace schxslt = "https://doi.org/10.5281/zenodo.1495494";
import module namespace cs-check="https://correspsearch.net/services/check/geonames" at "check-geonames.xql";

declare option exist:serialize "method=html media-type=text/html";

 let $url := request:get-parameter('url', ())

let $xml-data := 
    if (request:get-parameter('xml-file', ()))
    then request:get-uploaded-file-data('xml-file') 
    else if ($url)
    then doc($url)
    else ()
    
let $xml :=
    if (request:get-parameter('xml-file', ()))
    then parse-xml(util:base64-decode($xml-data))
    else $xml-data


let $checks :=
    element check { 
    validation:jing-report($xml, doc('cmi-customization.rng')),
    schxslt:validate($xml, doc('cmif.sch')),
    cs-check:geonames($xml)
    } 

return
transform:transform($checks, doc('view.xsl'), ())


```

## Selected source reading blocks

### r1 imported validation modules

Locator: lines 3-4, bytes 23-208, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "import module namespace schxslt = \"https://doi.org/10.5281/zenodo.1495494\";\nimport module namespace cs-check=\"https://correspsearch.net/services/check/geonames\" at \"check-geonames.xql\";" ^r1

### r2 input from upload or URL

Locator: lines 10-20, bytes 325-625, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "let $xml-data := \n    if (request:get-parameter('xml-file', ()))\n    then request:get-uploaded-file-data('xml-file') \n    else if ($url)\n    then doc($url)\n    else ()\n    \nlet $xml :=\n    if (request:get-parameter('xml-file', ()))\n    then parse-xml(util:base64-decode($xml-data))\n    else $xml-data" ^r2

### r3 applied checks and rendering

Locator: lines 23-31, bytes 628-865, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "let $checks :=\n    element check { \n    validation:jing-report($xml, doc('cmi-customization.rng')),\n    schxslt:validate($xml, doc('cmif.sch')),\n    cs-check:geonames($xml)\n    } \n\nreturn\ntransform:transform($checks, doc('view.xsl'), ())" ^r3

