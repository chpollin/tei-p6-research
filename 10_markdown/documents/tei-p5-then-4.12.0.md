---
type: representation
source-type: document
source: '[[00_sources/tei-p5-then-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 then
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/then.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# then

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2845. Git blob: `60b8cf519885962afc24a5d9d4db642c83a19367`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="iso-fs" xml:id="gi-then" ident="then">
  <desc versionDate="2005-01-14" xml:lang="en">separates the condition from the default in an <gi>if</gi>, or
the antecedent and the consequent in a <gi>cond</gi> element.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko"><gi>if</gi>의 기본값에서 조건을 분리시키거나 또는 <gi>cond</gi> 요소의 조건부과 결론부를 분리시킨다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">區分條件和元素<gi>if</gi>中的預設值，或是區分元素<gi>cond</gi>中的前提和結果。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">要素<gi>if</gi>中のデフォルト値と条件部、または要素<gi>cond</gi>中の
  前提部と帰結部を区切る。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">sépare la condition de la valeur par défaut dans un
      if, ou l'antécédent de la conséquence dans un élément cond.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">separa la condición del valor predeterminado, o el antecedento y el resultante en un elemento cond.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">separa la condizione dal valore predefinito in un if, o l'antecedente e il successivo in un elemento cond.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content><empty/></content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-then-egXML-lg" source="#UND">
      <cond>
        <fs>
          <f name="BAR">
            <symbol value="1"/>
          </f>
        </fs>
        <then/>
        <fs>
          <f name="FOO">
            <binary value="false"/>
          </f>
        </fs>
      </cond>
    </egXML>
  </exemplum>
  <remarks ident="then-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element is provided primarily to enhance the
human readability of the feature-system declaration.</p>
  </remarks>
  <remarks ident="then-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est fourni essentiellement pour rendre plus lisible par l'homme une
                déclaration d'un système de traits.</p>
  </remarks>
  <remarks ident="then-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、素性システム宣言を人が読みやすくするためのものである。
    </p>
  </remarks>
  <listRef>
    <ptr target="#FD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">separates the condition from the default in an <gi>if</gi>, or
the antecedent and the consequent in a <gi>cond</gi> element.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko"><gi>if</gi>의 기본값에서 조건을 분리시키거나 또는 <gi>cond</gi> 요소의 조건부과 결론부를 분리시킨다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">區分條件和元素<gi>if</gi>中的預設值，或是區分元素<gi>cond</gi>中的前提和結果。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">要素<gi>if</gi>中のデフォルト値と条件部、または要素<gi>cond</gi>中の
  前提部と帰結部を区切る。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">sépare la condition de la valeur par défaut dans un
      if, ou l'antécédent de la conséquence dans un élément cond.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">separa la condición del valor predeterminado, o el antecedento y el resultante en un elemento cond.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">separa la condizione dal valore predefinito in un if, o l'antecedente e il successivo in un elemento cond.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-then-egXML-lg" source="#UND">
      <cond>
        <fs>
          <f name="BAR">
            <symbol value="1"/>
          </f>
        </fs>
        <then/>
        <fs>
          <f name="FOO">
            <binary value="false"/>
          </f>
        </fs>
      </cond>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="then-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>This element is provided primarily to enhance the
human readability of the feature-system declaration.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="then-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément est fourni essentiellement pour rendre plus lisible par l'homme une
                déclaration d'un système de traits.</p>
  </remarks>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="then-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該要素は、素性システム宣言を人が読みやすくするためのものである。
    </p>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FD"/>
  </listRef>
```

^b14

