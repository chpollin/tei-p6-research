---
type: representation
source-type: document
source: '[[00_sources/tei-p5-entry-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 entry
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/entry.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# entry

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 6025. Git blob: `1ad236d110f22d42306d1385b5831ae41467e874`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-entry" ident="entry">
  <gloss versionDate="2007-06-12" xml:lang="en">entry</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">entrée</gloss>
  <desc versionDate="2011-04-29" xml:lang="en">contains a single structured entry in any kind of lexical resource, such
  as a dictionary or lexicon.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">합리적으로 체계화된 사전 표제 항목을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含字典中一個結構完善的辭條項目。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">それなりに構造化されている辞書項目を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient une entrée structurée de dictionnaire.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una entrada razonablemente bien estructurada.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una voce di dizionario ragionevolmente ben
    strutturata.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.entryLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.entryLike"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <elementRef key="hom"/>
      <elementRef key="sense"/>
      <elementRef key="pc"/>
      <classRef key="model.entryPart.top"/>
      <classRef key="model.global"/>
      <classRef key="model.ptrLike"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entry-egXML-uo">
      <entry>
        <form>
          <orth>disproof</orth>
          <pron>dIs"pru:f</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
        <sense n="1">
          <def>facts that disprove something.</def>
        </sense>
        <sense n="2">
          <def>the act of disproving.</def>
        </sense>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entry-egXML-dp" source="#fr-ex-Grand-Robert">
      <entry>
        <form>
          <orth>poussin</orth>
          <pron>[pusë]</pron>
        </form>
        <gramGrp>
          <pos>n.</pos>
          <gen>m.</gen>
        </gramGrp>
        <sense n="1">Jeune poulet, nouvellement sorti de l'oeuf, encore couvert de duvet. La poule
            et ses poussins.</sense>
        <sense n="2">Zool. Jeune oiseau (par rapport aux adultes, aux parents). </sense>
        <sense n="3"> (êtres humains) <def n="1">Fam. Terme d'affection (enfant). </def>
               <def n="2"> Sports. Catégorie d'âge (9 ans) qui précède celle des benjamins.</def>
               <def n="3">Elève de première année dans certaines écoles (Air,
          Aéronautique).</def>
            </sense>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entry-egXML-nq">
      <entry>
        <form>
          <orth>證明</orth>
          <pron>zheng-meng</pron>
        </form>
        <gramGrp>
          <pos>名詞</pos>
        </gramGrp>
        <sense n="1">
          <def>可靠的證據或事實</def>
        </sense>
        <sense n="2">
          <def>用可靠的證據或事實來表明或斷定人或事物的真實性。</def>
        </sense>
      </entry>
    </egXML>
  </exemplum>
  <remarks ident="entry-remarks" versionDate="2013-06-20" xml:lang="en">
    <p>Like all elements, <gi>entry</gi> inherits an <att>xml:id</att> attribute from the class
        <term>global</term>. No restrictions are placed on the method used to construct
      <att>xml:id</att>s; one convenient method is to use the orthographic form of the headword,
      appending a disambiguating number where necessary. Identification codes are sometimes included
      on machine-readable tapes of dictionaries for in-house use. </p>
    <p>It is recommended to use the <gi>sense</gi> element even for an entry that has only one sense 
      to group together all parts of the definition relating to the word sense since this leads to 
      more consistent encoding across entries.</p>
  </remarks>
  <remarks ident="entry-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Comme tous les éléments, <gi>entry</gi> hérite d'un attribut <att>xml:id</att> issu de la
      classe <term>global</term>. Aucune restriction n'est donnée quant à la méthode utilisée pour
      construire les <att>xml:id</att> ; une méthode commode consiste à utiliser la forme
      orthographique de l'entrée en y ajoutant un nombre si nécessaire, pour éviter toute ambiguïté.
      Pour un usage interne, des codes d'identification sont parfois inclus sur les enregistements
      électroniques des dictionnaires. </p>
  </remarks>
  <remarks ident="entry-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 他の要素と同じく、要素<gi>entry</gi>は、クラス<term>global</term>
      から属性<att>xml:id</att>を継承している。属性<att>xml:id</att>を使 用する際の制約はない。見出し語には正書形を使うのがよい。必要であれ
      ば、曖昧性のない番号を付加してもよい。識別コードには、組織内で使用 される機械可読テープにある辞書でも使用されることがある。 </p>
  </remarks>
  <listRef>
    <ptr target="#DIBO" type="div2"/>
    <ptr target="#DIEN" type="div2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">entry</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">entrée</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-04-29" xml:lang="en">contains a single structured entry in any kind of lexical resource, such
  as a dictionary or lexicon.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">합리적으로 체계화된 사전 표제 항목을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含字典中一個結構完善的辭條項目。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">それなりに構造化されている辞書項目を示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient une entrée structurée de dictionnaire.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una entrada razonablemente bien estructurada.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una voce di dizionario ragionevolmente ben
    strutturata.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.entryLike"/>
    <memberOf key="att.sortable"/>
    <memberOf key="model.entryLike"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <elementRef key="hom"/>
      <elementRef key="sense"/>
      <elementRef key="pc"/>
      <classRef key="model.entryPart.top"/>
      <classRef key="model.global"/>
      <classRef key="model.ptrLike"/>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entry-egXML-uo">
      <entry>
        <form>
          <orth>disproof</orth>
          <pron>dIs"pru:f</pron>
        </form>
        <gramGrp>
          <pos>n</pos>
        </gramGrp>
        <sense n="1">
          <def>facts that disprove something.</def>
        </sense>
        <sense n="2">
          <def>the act of disproving.</def>
        </sense>
      </entry>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entry-egXML-dp" source="#fr-ex-Grand-Robert">
      <entry>
        <form>
          <orth>poussin</orth>
          <pron>[pusë]</pron>
        </form>
        <gramGrp>
          <pos>n.</pos>
          <gen>m.</gen>
        </gramGrp>
        <sense n="1">Jeune poulet, nouvellement sorti de l'oeuf, encore couvert de duvet. La poule
            et ses poussins.</sense>
        <sense n="2">Zool. Jeune oiseau (par rapport aux adultes, aux parents). </sense>
        <sense n="3"> (êtres humains) <def n="1">Fam. Terme d'affection (enfant). </def>
               <def n="2"> Sports. Catégorie d'âge (9 ans) qui précède celle des benjamins.</def>
               <def n="3">Elève de première année dans certaines écoles (Air,
          Aéronautique).</def>
            </sense>
      </entry>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-entry-egXML-nq">
      <entry>
        <form>
          <orth>證明</orth>
          <pron>zheng-meng</pron>
        </form>
        <gramGrp>
          <pos>名詞</pos>
        </gramGrp>
        <sense n="1">
          <def>可靠的證據或事實</def>
        </sense>
        <sense n="2">
          <def>用可靠的證據或事實來表明或斷定人或事物的真實性。</def>
        </sense>
      </entry>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="entry-remarks" versionDate="2013-06-20" xml:lang="en">
    <p>Like all elements, <gi>entry</gi> inherits an <att>xml:id</att> attribute from the class
        <term>global</term>. No restrictions are placed on the method used to construct
      <att>xml:id</att>s; one convenient method is to use the orthographic form of the headword,
      appending a disambiguating number where necessary. Identification codes are sometimes included
      on machine-readable tapes of dictionaries for in-house use. </p>
    <p>It is recommended to use the <gi>sense</gi> element even for an entry that has only one sense 
      to group together all parts of the definition relating to the word sense since this leads to 
      more consistent encoding across entries.</p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="entry-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Comme tous les éléments, <gi>entry</gi> hérite d'un attribut <att>xml:id</att> issu de la
      classe <term>global</term>. Aucune restriction n'est donnée quant à la méthode utilisée pour
      construire les <att>xml:id</att> ; une méthode commode consiste à utiliser la forme
      orthographique de l'entrée en y ajoutant un nombre si nécessaire, pour éviter toute ambiguïté.
      Pour un usage interne, des codes d'identification sont parfois inclus sur les enregistements
      électroniques des dictionnaires. </p>
  </remarks>
```

^b16

### Block 17

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="entry-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 他の要素と同じく、要素<gi>entry</gi>は、クラス<term>global</term>
      から属性<att>xml:id</att>を継承している。属性<att>xml:id</att>を使 用する際の制約はない。見出し語には正書形を使うのがよい。必要であれ
      ば、曖昧性のない番号を付加してもよい。識別コードには、組織内で使用 される機械可読テープにある辞書でも使用されることがある。 </p>
  </remarks>
```

^b17

### Block 18

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIBO" type="div2"/>
    <ptr target="#DIEN" type="div2"/>
  </listRef>
```

^b18

