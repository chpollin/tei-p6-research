---
type: representation
source-type: document
source: '[[00_sources/documents/practice-v1-dracor-build-c2f9e814.txt]]'
converter: tools.ingest_practice_v1 v1; complete original plus JSON-escaped exact
  source fragments
channel: collection
metadata:
  title: DraCor schema build script (build)
  creator: DraCor project (dracor-org)
  date: '2026-08-03'
  format: text/plain
  identifier: https://github.com/dracor-org/dracor-schema/blob/c2f9e8140bf413cb3bce44abc818d563ddc92d88/build
  license: CC-BY-4.0
  confidential: false
created: '2026-09-11'
updated: '2026-09-11'
---

# DraCor schema build script (build)

Source: `build` in `dracor-org/dracor-schema` at commit `c2f9e8140bf413cb3bce44abc818d563ddc92d88`.
Source SHA-256: `74a305786a26a2f617fa38550fb93ff24677693e2e31487a9e992e1138805b14`, 1158 bytes.
Rights: CC-BY-4.0. DraCor Schema repository, dracor.org, CC BY 4.0.
License evidence: repository LICENSE at the pinned commit; README.md scopes CC BY 4.0 to the DraCor Schema.

The complete original is inert source text and is never executed. The
separator newline before its closing fence is not part of the original.
Reading blocks are exact source byte intervals encoded as JSON strings;
their line and byte locators refer to the original.

## Complete original

```sh
#!/bin/sh

BIN=./Stylesheets/bin

if [ ! -d $BIN ]; then
  git submodule init
  git submodule update
fi

version=$(git describe --tags --dirty --always | sed s/^v// | sed s/-g/-/)

mkdir -p dist

# In JDK 24/25, these limits were significantly lowered to 100,000 bytes which
# would make the ODD transformation fail with JAXP00010003 and JAXP00010004
# errors
export JAVA_TOOL_OPTIONS="-Djdk.xml.maxGeneralEntitySizeLimit=0 -Djdk.xml.totalEntitySizeLimit=0"


# Generate full ODD
$BIN/teitoodd --odd dracor.odd dist/dracor.odd.tmp

# Transform to RNG
$BIN/teitorng --odd dist/dracor.odd.tmp dist/dracor.rng
sed -i.bak -E -e "s/(DraCor Schema)/\1 $version/" dist/dracor.rng

# Transform to Schematron
$BIN/teitoschematron --odd dist/dracor.odd.tmp dist/dracor.sch
sed -i.bak -E -e "s/(<title>ISO Schematron rules)/\1 (DraCor Schema $version)/" dist/dracor.sch

# Transform to HTML
$BIN/teitohtml --odd dist/dracor.odd.tmp dist/dracor.html.tmp
java -jar Stylesheets/lib/saxon10he.jar \
  -xsl:html.xsl \
  -s:dist/dracor.html.tmp \
  version=$version \
  > dist/index.html

cp -v dist/index.html dist/odd-$version.html

# clean up sed backups
rm -f dist/*.bak

```

## Selected source reading blocks

### r1 Stylesheets submodule location

Locator: lines 3-8, bytes 11-103, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "BIN=./Stylesheets/bin\n\nif [ ! -d $BIN ]; then\n  git submodule init\n  git submodule update\nfi" ^r1

### r2 Java XML entity limits

Locator: lines 14-17, bytes 196-457, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "# In JDK 24/25, these limits were significantly lowered to 100,000 bytes which\n# would make the ODD transformation fail with JAXP00010003 and JAXP00010004\n# errors\nexport JAVA_TOOL_OPTIONS=\"-Djdk.xml.maxGeneralEntitySizeLimit=0 -Djdk.xml.totalEntitySizeLimit=0\"" ^r2

### r3 ODD, RELAX NG and Schematron generation

Locator: lines 20-28, bytes 460-762, interval, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "# Generate full ODD\n$BIN/teitoodd --odd dracor.odd dist/dracor.odd.tmp\n\n# Transform to RNG\n$BIN/teitorng --odd dist/dracor.odd.tmp dist/dracor.rng\nsed -i.bak -E -e \"s/(DraCor Schema)/\\1 $version/\" dist/dracor.rng\n\n# Transform to Schematron\n$BIN/teitoschematron --odd dist/dracor.odd.tmp dist/dracor.sch" ^r3

