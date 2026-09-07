---
type: representation
source-type: document
source: '[[00_sources/tei-p5-physdesc-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 physDesc
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/physDesc.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# physDesc

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3814. Git blob: `87fd7b27f1abf715f649be8288ff01c52b072977`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="PHYSDESC" ident="physDesc">
  <gloss versionDate="2007-07-04" xml:lang="en">physical description</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">물리적 기술</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">descripción física</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">description physique</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">descrizione fisica</gloss>
  <desc versionDate="2018-10-26" xml:lang="en" xml:id="physdesc.desc">contains a full physical description of a
manuscript, manuscript part, or other object optionally subdivided using more
specialized elements from the <ident type="class">model.physDescPart</ident> class.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">model.physDescPart 클래스에서 더 특별화된 요소로 사용하기 위해 수의적으로 더 세분화한 원고 또는 원고 일부에 대한 완전한 물리적 기술을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個手稿或手稿部分的完整材質描述，可以利用model.physDescPart class中的專門元素選擇性地再分類。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料の物理的な解説を示す。選択的に、クラスmodel.physDescPartに
  ある要素に下位分解される。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la description physique complète d'un
      manuscrit ou d'une partie d'un manuscrit, éventuellement structurée en utilisant les éléments
      plus spécialisés appartenant à la classe <ident type="class">model.physDescPart</ident>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una descripción física completa de un manuscrito o de una de sus partes que puede ser ulteriormente subdividida utilizando elementos específicos de la clase <ident type="class">model.physDescPart</ident>.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione fisica completa di un manoscritto o di una sua parte che può essere ulteriormente suddivisa utilizzando elementi specifici della classe .physDescPart.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <sequence>
      
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
      
      
        <!-- not sure if this group is needed -->
        <classRef key="model.physDescPart" expand="sequenceOptional"/>
      
    </sequence>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PHYSDESC-egXML-jp">
      <physDesc>
        <objectDesc form="codex">
          <supportDesc material="perg">
            <support>Parchment.</support>
            <extent>i + 55 leaves
                 <dimensions scope="all" type="leaf" unit="inch"><height>7¼</height><width>5⅜</width></dimensions>
                  </extent>
          </supportDesc>
          <layoutDesc>
            <layout columns="2">In double columns.</layout>
          </layoutDesc>
        </objectDesc>
        <handDesc>
          <p>Written in more than one hand.</p>
        </handDesc>
        <decoDesc>
          <p>With a few coloured capitals.</p>
        </decoDesc>
      </physDesc>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msph"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">physical description</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">물리적 기술</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">descripción física</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">description physique</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">descrizione fisica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2018-10-26" xml:lang="en" xml:id="physdesc.desc">contains a full physical description of a
manuscript, manuscript part, or other object optionally subdivided using more
specialized elements from the <ident type="class">model.physDescPart</ident> class.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">model.physDescPart 클래스에서 더 특별화된 요소로 사용하기 위해 수의적으로 더 세분화한 원고 또는 원고 일부에 대한 완전한 물리적 기술을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個手稿或手稿部分的完整材質描述，可以利用model.physDescPart class中的專門元素選擇性地再分類。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料の物理的な解説を示す。選択的に、クラスmodel.physDescPartに
  ある要素に下位分解される。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la description physique complète d'un
      manuscrit ou d'une partie d'un manuscrit, éventuellement structurée en utilisant les éléments
      plus spécialisés appartenant à la classe <ident type="class">model.physDescPart</ident>.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una descripción física completa de un manuscrito o de una de sus partes que puede ser ulteriormente subdividida utilizando elementos específicos de la clase <ident type="class">model.physDescPart</ident>.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una descrizione fisica completa di un manoscritto o di una sua parte che può essere ulteriormente suddivisa utilizzando elementi specifici della classe .physDescPart.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <classRef key="model.pLike" minOccurs="0" maxOccurs="unbounded"/>
      
      
        <!-- not sure if this group is needed -->
        <classRef key="model.physDescPart" expand="sequenceOptional"/>
      
    </sequence>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="PHYSDESC-egXML-jp">
      <physDesc>
        <objectDesc form="codex">
          <supportDesc material="perg">
            <support>Parchment.</support>
            <extent>i + 55 leaves
                 <dimensions scope="all" type="leaf" unit="inch"><height>7¼</height><width>5⅜</width></dimensions>
                  </extent>
          </supportDesc>
          <layoutDesc>
            <layout columns="2">In double columns.</layout>
          </layoutDesc>
        </objectDesc>
        <handDesc>
          <p>Written in more than one hand.</p>
        </handDesc>
        <decoDesc>
          <p>With a few coloured capitals.</p>
        </decoDesc>
      </physDesc>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msph"/>
  </listRef>
```

^b17

