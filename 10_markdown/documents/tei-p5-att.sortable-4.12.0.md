---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.sortable-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.sortable
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.sortable.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.sortable

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5886. Git blob: `ce08709dbaf68d84174cb72c834cb16731a65b58`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" xml:id="class-attr-sortable" ident="att.sortable">
  <desc versionDate="2011-11-06" xml:lang="en">provides attributes for elements in lists or groups that are sortable, but whose sorting key cannot be derived mechanically from the element content.</desc>
  <desc versionDate="2023-09-27" xml:lang="ja">ソート可能だが、ソートのキーは要素の内容から機械的に取り出すことはできないリストやグループにおける要素に関する属性。</desc>
  <attList>
    <attDef ident="sortKey" usage="opt">
      <desc versionDate="2011-11-06" xml:lang="en">supplies the sort key for this element in an index, list or group which contains it.</desc>
      <desc versionDate="2023-09-27" xml:lang="ja">インデックスやリスト、グループに含まれる要素のソートキーを提供する。</desc>
      <datatype><dataRef key="teidata.word"/></datatype>
      <exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-sortable-egXML-dk">David's other principal backer, Josiah
            ha-Kohen <index indexName="NAMES"><term sortKey="Azarya_Josiah_Kohen">Josiah ha-Kohen b. Azarya</term></index> b. Azarya, son of one of the last gaons of Sura was David's own first
            cousin.</egXML>
      </exemplum>
      <exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-sortable-egXML-tw" source="#fr-ex-Verne_Vingt"> Je me suis
            procuré une <term>clef anglaise</term> pour dévisser les écrous qui attachent le canot à
            la coque du Nautilus. Ainsi tout est prêt.</egXML>
      </exemplum>
      <remarks ident="att.sortable-attr.sortKey-remarks" versionDate="2013-12-09" xml:lang="en">
        <p>The sort key is used to determine the sequence and grouping of entries in an index. It provides a sequence of characters which, when sorted with the other values, will produced
          the desired order; specifics of sort key construction are application-dependent</p>
        <p>Dictionary order often differs from the collation sequence of machine-readable character
            sets; in English-language dictionaries, an entry for <mentioned>4-H</mentioned> will often
            appear alphabetized under <q>fourh</q>, and <mentioned>McCoy</mentioned> may be
            alphabetized under <q>maccoy</q>, while <mentioned>A1</mentioned>,
            <mentioned>A4</mentioned>, and <mentioned>A5</mentioned> may all appear in numeric order
            <soCalled>alphabetized</soCalled> between <q>a-</q> and <q>AA</q>. The sort key is
            required if the orthography of the dictionary entry does not suffice to determine its
            location.</p>
      </remarks>
      <remarks ident="att.sortable-attr.sortKey-remarks" versionDate="2013-12-09" xml:lang="fr">
        <p>La clé de tri est utilisée pour déterminer la séquence et le groupement d'entrées dans un
          index. Elle fournit une séquence de caractères qui, lorsqu'ils sont triés avec les autres valeurs, produisent l'ordre souhaité ; les détails de construction d'une clé de tri
          dépendent des applications.
.</p>
        <p>La structure d'un dictionnaire diffère souvent de l'ordre de collation des jeux de
            caractères lisibles par la machine ; dans des dictionnaires de langue anglaise, une entrée
            pour <mentioned>4-H</mentioned> apparaîtra souvent alphabétiquement sous <q>fourh</q>, et
            <mentioned>McCoy</mentioned>peut être classé alphabétiquement sous <q>maccoy</q>, tandis que <mentioned>A1</mentioned>, <mentioned>A4</mentioned> et <mentioned>A5</mentioned>
            apparaîtront tous dans un ordre alphanumérique entre <q>a-</q> et <q>AA</q>. La clef de
            tri est exigée si l'orthographe de l'entrée du dictionnaire n'est pas suffisante pour
            déterminer son emplacement.</p>
      </remarks>
      <remarks ident="att.sortable-attr.sortKey-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>La clave de ordenación se utiliza para determinar la secuencia y agrupar las entradas en
            un índice.</p>
      </remarks>
      <remarks ident="att.sortable-attr.sortKey-remarks" versionDate="2023-09-27" xml:lang="ja">
        <p>当該属性は、索引中の項目の並びやグループを決めるために使用される。
          これはほかの値によって並べ替えを行いたいときの一続きの文字を与え、それによって望まれる順序を実現する。
          ソートキー構文の詳細はアプリケーション依存である。</p>
        <p>辞書順はしばしば機械可読文字集合の照合順と異なる。
          英語圏の辞書では、<mentioned>4-H</mentioned>という項目はしばしば<q>fourh</q>としてアルファベット化され、<mentioned>McCoy</mentioned>は、<q>maccoy</q>としてアルファベット化されうる。
          それに対して、<mentioned>A1</mentioned>や<mentioned>A4</mentioned>、<mentioned>A5</mentioned>は<q>a-</q>と<q>AA</q>のあいだに数字順に置かれてしまうこともある。
          ソートキーは、辞書項目の表記が辞書における順序を決定するのに不十分な際に必要となる。</p>
      </remarks>
      
    </attDef>
  </attList>
  <listRef>
    <ptr target="#DIBO"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2011-11-06" xml:lang="en">provides attributes for elements in lists or groups that are sortable, but whose sorting key cannot be derived mechanically from the element content.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">ソート可能だが、ソートのキーは要素の内容から機械的に取り出すことはできないリストやグループにおける要素に関する属性。</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-11-06" xml:lang="en">supplies the sort key for this element in an index, list or group which contains it.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2023-09-27" xml:lang="ja">インデックスやリスト、グループに含まれる要素のソートキーを提供する。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.word"/></datatype>
```

^b5

### Block 6

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-sortable-egXML-dk">David's other principal backer, Josiah
            ha-Kohen <index indexName="NAMES"><term sortKey="Azarya_Josiah_Kohen">Josiah ha-Kohen b. Azarya</term></index> b. Azarya, son of one of the last gaons of Sura was David's own first
            cousin.</egXML>
      </exemplum>
```

^b6

### Block 7

XML location: `/classSpec[1]/attList[1]/attDef[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
        <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="class-attr-sortable-egXML-tw" source="#fr-ex-Verne_Vingt"> Je me suis
            procuré une <term>clef anglaise</term> pour dévisser les écrous qui attachent le canot à
            la coque du Nautilus. Ainsi tout est prêt.</egXML>
      </exemplum>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.sortable-attr.sortKey-remarks" versionDate="2013-12-09" xml:lang="en">
        <p>The sort key is used to determine the sequence and grouping of entries in an index. It provides a sequence of characters which, when sorted with the other values, will produced
          the desired order; specifics of sort key construction are application-dependent</p>
        <p>Dictionary order often differs from the collation sequence of machine-readable character
            sets; in English-language dictionaries, an entry for <mentioned>4-H</mentioned> will often
            appear alphabetized under <q>fourh</q>, and <mentioned>McCoy</mentioned> may be
            alphabetized under <q>maccoy</q>, while <mentioned>A1</mentioned>,
            <mentioned>A4</mentioned>, and <mentioned>A5</mentioned> may all appear in numeric order
            <soCalled>alphabetized</soCalled> between <q>a-</q> and <q>AA</q>. The sort key is
            required if the orthography of the dictionary entry does not suffice to determine its
            location.</p>
      </remarks>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.sortable-attr.sortKey-remarks" versionDate="2013-12-09" xml:lang="fr">
        <p>La clé de tri est utilisée pour déterminer la séquence et le groupement d'entrées dans un
          index. Elle fournit une séquence de caractères qui, lorsqu'ils sont triés avec les autres valeurs, produisent l'ordre souhaité ; les détails de construction d'une clé de tri
          dépendent des applications.
.</p>
        <p>La structure d'un dictionnaire diffère souvent de l'ordre de collation des jeux de
            caractères lisibles par la machine ; dans des dictionnaires de langue anglaise, une entrée
            pour <mentioned>4-H</mentioned> apparaîtra souvent alphabétiquement sous <q>fourh</q>, et
            <mentioned>McCoy</mentioned>peut être classé alphabétiquement sous <q>maccoy</q>, tandis que <mentioned>A1</mentioned>, <mentioned>A4</mentioned> et <mentioned>A5</mentioned>
            apparaîtront tous dans un ordre alphanumérique entre <q>a-</q> et <q>AA</q>. La clef de
            tri est exigée si l'orthographe de l'entrée du dictionnaire n'est pas suffisante pour
            déterminer son emplacement.</p>
      </remarks>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.sortable-attr.sortKey-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>La clave de ordenación se utiliza para determinar la secuencia y agrupar las entradas en
            un índice.</p>
      </remarks>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="att.sortable-attr.sortKey-remarks" versionDate="2023-09-27" xml:lang="ja">
        <p>当該属性は、索引中の項目の並びやグループを決めるために使用される。
          これはほかの値によって並べ替えを行いたいときの一続きの文字を与え、それによって望まれる順序を実現する。
          ソートキー構文の詳細はアプリケーション依存である。</p>
        <p>辞書順はしばしば機械可読文字集合の照合順と異なる。
          英語圏の辞書では、<mentioned>4-H</mentioned>という項目はしばしば<q>fourh</q>としてアルファベット化され、<mentioned>McCoy</mentioned>は、<q>maccoy</q>としてアルファベット化されうる。
          それに対して、<mentioned>A1</mentioned>や<mentioned>A4</mentioned>、<mentioned>A5</mentioned>は<q>a-</q>と<q>AA</q>のあいだに数字順に置かれてしまうこともある。
          ソートキーは、辞書項目の表記が辞書における順序を決定するのに不十分な際に必要となる。</p>
      </remarks>
```

^b11

### Block 12

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DIBO"/>
  </listRef>
```

^b12

