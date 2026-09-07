---
type: representation
source-type: document
source: '[[00_sources/tei-p5-additions-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 additions
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/additions.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# additions

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3590. Git blob: `3ac7e117f67b4a2a9e57e021b0495d79ca10bfd5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="ADDITIONS" ident="additions">
  <gloss versionDate="2007-06-12" xml:lang="en">additions</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">ajouts</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="additions.desc">contains a description of any significant additions found
within a manuscript or other object, such as marginalia or other annotations.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">방주 또는 기타 주석과 같이 원고 내의 중요한 부가정보의 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿中任何重要增添文字的描述，例如旁註或其他註釋。</desc>
  <desc versionDate="2022-06-07" xml:lang="ja">当該手書き資料中にある、重要な付加物を示す。例えば、欄外の書き込みや注釈など。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description des ajouts significatifs
      trouvés dans un manuscrit, tels que gloses marginales ou autres annotations.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de cualquier adición significativa encontrada al interno de un manuscrito como notas al márgen u otras anotaciones.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un descrizione di qualsiasi aggiunta significativa trovata all'interno di un manoscritto come note a margine o altre annotazioni.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONS-egXML-nw" source="#UND">
      <additions>
        <p>There are several marginalia in this manuscript. Some consist of
single characters and others are figurative. On 8v is to be found a drawing of
a mans head wearing a hat. At times sentences occurs: On 5v: 
<q xml:lang="is">Her er skrif andres isslendin</q>, 
on 19r: <q xml:lang="is">þeim go</q>, 
on 21r: <q xml:lang="is">amen med aund ok munn halla rei knar hofud summu all huad
batar þad mælgi ok mal</q>, 
On 21v: some runic letters and the sentence  <q xml:lang="la">aue maria gracia plena dominus</q>.</p>
      </additions>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr" source="#UND">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONS-egXML-hs">
      <additions>
        <p>There are several marginalia in this manuscript. Some consist of single characters and
            others are figurative. On 8v is to be found a drawing of a mans head wearing a hat. At
            times sentences occurs: On 5v:<q xml:lang="is">Her er skrif andres isslendin</q>, on
            19r: <q xml:lang="is">þeim go</q>, on 21r: <q xml:lang="is">amen med aund ok munn halla
              rei knar hofud summu all huad batar þad mælgi ok mal</q>, On 21v: some runic letters
            and the sentence <q xml:lang="la">aue maria gracia plena dominus</q>.</p>
      </additions>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">additions</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">ajouts</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="additions.desc">contains a description of any significant additions found
within a manuscript or other object, such as marginalia or other annotations.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">방주 또는 기타 주석과 같이 원고 내의 중요한 부가정보의 기술을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含手稿中任何重要增添文字的描述，例如旁註或其他註釋。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2022-06-07" xml:lang="ja">当該手書き資料中にある、重要な付加物を示す。例えば、欄外の書き込みや注釈など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description des ajouts significatifs
      trouvés dans un manuscrit, tels que gloses marginales ou autres annotations.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción de cualquier adición significativa encontrada al interno de un manuscrito como notas al márgen u otras anotaciones.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un descrizione di qualsiasi aggiunta significativa trovata all'interno di un manoscritto come note a margine o altre annotazioni.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.physDescPart"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONS-egXML-nw" source="#UND">
      <additions>
        <p>There are several marginalia in this manuscript. Some consist of
single characters and others are figurative. On 8v is to be found a drawing of
a mans head wearing a hat. At times sentences occurs: On 5v: 
<q xml:lang="is">Her er skrif andres isslendin</q>, 
on 19r: <q xml:lang="is">þeim go</q>, 
on 21r: <q xml:lang="is">amen med aund ok munn halla rei knar hofud summu all huad
batar þad mælgi ok mal</q>, 
On 21v: some runic letters and the sentence  <q xml:lang="la">aue maria gracia plena dominus</q>.</p>
      </additions>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr" source="#UND">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONS-egXML-hs">
      <additions>
        <p>There are several marginalia in this manuscript. Some consist of single characters and
            others are figurative. On 8v is to be found a drawing of a mans head wearing a hat. At
            times sentences occurs: On 5v:<q xml:lang="is">Her er skrif andres isslendin</q>, on
            19r: <q xml:lang="is">þeim go</q>, on 21r: <q xml:lang="is">amen med aund ok munn halla
              rei knar hofud summu all huad batar þad mælgi ok mal</q>, On 21v: some runic letters
            and the sentence <q xml:lang="la">aue maria gracia plena dominus</q>.</p>
      </additions>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph2"/>
  </listRef>
```

^b14

