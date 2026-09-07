---
type: representation
source-type: document
source: '[[00_sources/tei-p5-model.namelike.agent-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 model.nameLike.agent
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/model.nameLike.agent.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# model.nameLike.agent

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 2412. Git blob: `1b7f8e972d8b0f966d67acb3456b5cf5127d50b3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" xml:id="AGENT" type="model" ident="model.nameLike.agent">
  <desc versionDate="2005-10-10" xml:lang="en">groups elements which contain names of individuals
or corporate bodies.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">개인 또는 기업체의 이름을 포함하는 요소를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集包含個人或團體名稱的元素。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">個人や団体の名前を含む要素をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui contiennent des noms
      d'individus ou de personnes morales.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que contienen nombres de individuos o de agrupaciones o sociedades.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi che contengono nomi di individui o enti societari.</desc>
  <classes>
    
    <memberOf key="model.nameLike"/>
  </classes>
  <remarks ident="model.nameLike.agent-remarks" versionDate="2005-11-08" xml:lang="en">
    <p>This class is used in the content model of elements which
    reference names of people or organizations.</p>
  </remarks>
  <remarks ident="model.nameLike.agent-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe est utilisée dans le modèle de contenu des éléments qui référencent des
                noms de personnes ou d'organisations.</p>
  </remarks>
  <remarks ident="model.nameLike.agent-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta clase se utiliza en el modelo de elementos cuyos nombres se refieren a gente o a organizaciones.</p>
  </remarks>
  <remarks ident="model.nameLike.agent-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該クラスは、人物や団体の名前を参照する要素の内容モデル中で使用さ
    れる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#CONA"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-10-10" xml:lang="en">groups elements which contain names of individuals
or corporate bodies.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">개인 또는 기업체의 이름을 포함하는 요소를 모아 놓는다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集包含個人或團體名稱的元素。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">個人や団体の名前を含む要素をまとめる。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe des éléments qui contiennent des noms
      d'individus ou de personnes morales.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa elementos que contienen nombres de individuos o de agrupaciones o sociedades.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa elementi che contengono nomi di individui o enti societari.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="model.nameLike"/>
  </classes>
```

^b8

### Block 9

XML location: `/classSpec[1]/remarks[1]`.

```xml
<remarks ident="model.nameLike.agent-remarks" versionDate="2005-11-08" xml:lang="en">
    <p>This class is used in the content model of elements which
    reference names of people or organizations.</p>
  </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/remarks[2]`.

```xml
<remarks ident="model.nameLike.agent-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cette classe est utilisée dans le modèle de contenu des éléments qui référencent des
                noms de personnes ou d'organisations.</p>
  </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/remarks[3]`.

```xml
<remarks ident="model.nameLike.agent-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Esta clase se utiliza en el modelo de elementos cuyos nombres se refieren a gente o a organizaciones.</p>
  </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/remarks[4]`.

```xml
<remarks ident="model.nameLike.agent-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    当該クラスは、人物や団体の名前を参照する要素の内容モデル中で使用さ
    れる。
    </p>
  </remarks>
```

^b12

### Block 13

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONA"/>
  </listRef>
```

^b13

