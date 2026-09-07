---
type: representation
source-type: document
source: '[[00_sources/tei-p5-table-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 table
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/table.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# table

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11663. Git blob: `b0109a8523381652fcace6f2b94b9e18639e119e`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="figures" xml:id="gi-table" ident="table">
  <gloss versionDate="2007-06-12" xml:lang="en">table</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">tableau</gloss>
  <gloss versionDate="2017-06-19" xml:lang="de">Tabelle</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains text displayed in tabular form, in rows and columns.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">행과 열의 테이블 형식으로 제시된 텍스트를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">以表格形式呈現、包含在直行橫列中的文字內容。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">表形式で示されるテキストを、行と列で示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient du texte affiché sous forme de tableau, en
    rangées et colonnes.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene texto dispuedto en forma de tabla, con filas y
    columnas.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene testo visualizzato in forma di tabella, in righe
    e colonne.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält Text, der in Tabellenform, also in Zeilen und Spalten, dargestellt ist.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
  </classes>
  <content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.headLike"/>
          <classRef key="model.global"/>
        </alternate>
      
      <alternate>
        <sequence minOccurs="1" maxOccurs="unbounded">
          <elementRef key="row"/>
          
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          
        </sequence>
        <sequence minOccurs="1" maxOccurs="unbounded">
          
            <classRef key="model.graphicLike"/>
          
          
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          
        </sequence>
      </alternate>
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <classRef key="model.divBottom"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
  <attList>
    <attDef ident="rows" usage="opt">
      <gloss versionDate="2017-06-19" xml:lang="en">rows</gloss>
      <gloss versionDate="2017-06-19" xml:lang="de">Zeilen</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates the number of rows in the table.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">테이블의 행의 수를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出表格中的列數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該表中の行数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le nombre de rangées dans le tableau.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el número de filas en una tabla.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il numero di righe della tabella.</desc>
      <desc versionDate="2017-06-19" xml:lang="de">gibt die Anzahl der Tabellenzeilen an.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <remarks ident="table-attr.rows-remarks" versionDate="2013-11-20" xml:lang="en">
        <p>If no number is supplied, an application must calculate the
	number of rows.</p>
<p>Rows should be presented from top to bottom.</p>
      </remarks>
      <remarks ident="table-attr.rows-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Les rangées sont ordonnées de haut en bas</p>
      </remarks>
      <remarks ident="table-attr.rows-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 行は、上から下の順番で示される。 </p>
      </remarks>
      <remarks ident="table-attr.rows-remarks" versionDate="2017-06-19" xml:lang="de">
        <p>Wenn keine Zeilenanzahl angegeben wird, muss diese von einer Applikation berechnet werden.</p>
        <p>Zeilen sollten von oben nach unten notiert werden.</p>
      </remarks>
    </attDef>
    <attDef ident="cols" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">columns</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">열</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">columnas</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">colonnes</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">colonne</gloss>
      <gloss versionDate="2017-06-19" xml:lang="de">Spalten</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates the number of columns in each row of the table.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">테이블의 각 행별 열의 수를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出表格中每一列所包含的行數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該表中の列数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le nombre de colonnes dans chaque rangée du
        tableau.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el número de columnas por cada fila de la
        tabla.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il numero di colonne in ciascuna riga della
        tabella-</desc>
      <desc versionDate="2017-06-19" xml:lang="de">gibt die Anzahl der Tabellenspalten an.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <remarks ident="table-attr.cols-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If no number is supplied, an application must calculate the
	number of columns.</p>
<p>Within each row, columns should be presented left to right.</p>
      </remarks>
      <remarks ident="table-attr.cols-remarks" versionDate="2007-06-12" xml:lang="fr">
<p>Si aucun nombre n'est fourni, une application doit calculer le nombre de colonnes.</p>        <p>Dans chaque rangée, les colonnes sont ordonnées de gauche à droite.</p>
      </remarks>
      <remarks ident="table-attr.cols-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 行中において、列は左から右への順番で示される。 </p>
      </remarks>
      <remarks ident="table-attr.cols-remarks" versionDate="2017-06-19" xml:lang="de">
        <p>Wenn keine Spaltenanzahl angegeben wird, muss diese von einer Applikation berechnet werden.</p>
        <p>In einer Zeile sollten Spalten von links nach rechts notiert werden.</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-table-egXML-vy">
      <table rows="4" cols="4">
        <head>Poor Men's Lodgings in Norfolk (Mayhew, 1843)</head>
        <row role="label">
          <cell role="data"/>
          <cell role="data">Dossing Cribs or Lodging Houses</cell>
          <cell role="data">Beds</cell>
          <cell role="data">Needys or Nightly Lodgers</cell>
        </row>
        <row role="data">
          <cell role="label">Bury St Edmund's</cell>
          <cell role="data">5</cell>
          <cell role="data">8</cell>
          <cell role="data">128</cell>
        </row>
        <row role="data">
          <cell role="label">Thetford</cell>
          <cell role="data">3</cell>
          <cell role="data">6</cell>
          <cell role="data">36</cell>
        </row>
        <row role="data">
          <cell role="label">Attleboro'</cell>
          <cell role="data">3</cell>
          <cell role="data">5</cell>
          <cell role="data">20</cell>
        </row>
        <row role="data">
          <cell role="label">Wymondham</cell>
          <cell role="data">1</cell>
          <cell role="data">11</cell>
          <cell role="data">22</cell>
        </row>
      </table>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-table-egXML-cb" source="#fr-ex-Kilian-Neige">
      <table rows="4" cols="4">
        <head>Persistance de la neige dans les Alpes suisses (Denzler). </head>
        <row>
          <cell role="label">A l'altitude de</cell>
          <cell role="data">650 m.</cell>
          <cell role="data">1300m.</cell>
          <cell role="data">1950m.</cell>
          <cell role="data">2700m.</cell>
        </row>
        <row>
          <cell role="label">la neige reste</cell>
          <cell role="data">77 jours.</cell>
          <cell role="data"> 200 jours.</cell>
          <cell role="data"> 245 jours.</cell>
          <cell role="data"> 365 jours.</cell>
        </row>
      </table>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-table-egXML-ym">
      <table rows="4" cols="4">
        <head>台北飯店提供住房數目(2008年雙十國慶 )</head>
        <row role="label">
          <cell role="data"/>
          <cell role="data">經濟客房</cell>
          <cell role="data">標準客房</cell>
          <cell role="data">高級客房</cell>
        </row>
        <row role="data">
          <cell role="label">圓山大飯店</cell>
          <cell role="data">203</cell>
          <cell role="data">168</cell>
          <cell role="data">66</cell>
        </row>
        <row role="data">
          <cell role="label">凱撒大飯店</cell>
          <cell role="data">216</cell>
          <cell role="data">140</cell>
          <cell role="data">32</cell>
        </row>
        <row role="data">
          <cell role="label">喜來登大飯店</cell>
          <cell role="data">197</cell>
          <cell role="data">160</cell>
          <cell role="data">50</cell>
        </row>
        <row role="data">
          <cell role="label">君悅大飯店</cell>
          <cell role="data">177</cell>
          <cell role="data">130</cell>
          <cell role="data">22</cell>
        </row>
      </table>
    </egXML>
  </exemplum>
  <remarks ident="table-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Contains an optional heading and a series of rows.</p>
    <p>Any rendition information should be supplied using the global <att>rend</att> attribute, at
      the table, row, or cell level as appropriate.</p>
  </remarks>
  <remarks ident="table-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient un titre facultatif et une suite de rangées.</p>
    <p>Toute information relative à la restitution sera exprimée avec l'attribut global
      <att>rend</att> appliqué au tableau, à la rangée, ou à la cellule selon le cas.</p>
  </remarks>
  <remarks ident="table-remarks" versionDate="2017-06-19" xml:lang="de">
    <p rend="dataDesc">Enthält eine Reihe von Zeilen und optional eine Überschrift.</p>
    <p>Jegliche Information die grafische Darstellung betreffend, sollte mit dem globalen
      <att>rend</att>-Attribut auf der Ebene von Tabelle, Zeile oder Zelle verzeichnet werden.</p>
  </remarks>
  <listRef>
    <ptr target="#FTTAB1" type="div1"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">table</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">tableau</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Tabelle</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains text displayed in tabular form, in rows and columns.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">행과 열의 테이블 형식으로 제시된 텍스트를 포함한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">以表格形式呈現、包含在直行橫列中的文字內容。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">表形式で示されるテキストを、行と列で示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient du texte affiché sous forme de tableau, en
    rangées et colonnes.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene texto dispuedto en forma de tabla, con filas y
    columnas.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene testo visualizzato in forma di tabella, in righe
    e colonne.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält Text, der in Tabellenform, also in Zeilen und Spalten, dargestellt ist.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.listLike"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      
        <alternate minOccurs="0" maxOccurs="unbounded">
          <classRef key="model.headLike"/>
          <classRef key="model.global"/>
        </alternate>
      
      <alternate>
        <sequence minOccurs="1" maxOccurs="unbounded">
          <elementRef key="row"/>
          
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          
        </sequence>
        <sequence minOccurs="1" maxOccurs="unbounded">
          
            <classRef key="model.graphicLike"/>
          
          
            <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
          
        </sequence>
      </alternate>
      <sequence minOccurs="0" maxOccurs="unbounded">
        
          <classRef key="model.divBottom"/>
        
        
          <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
        
      </sequence>
    </sequence>
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="en">rows</gloss>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Zeilen</gloss>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the number of rows in the table.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">테이블의 행의 수를 표시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出表格中的列數。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該表中の行数を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le nombre de rangées dans le tableau.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el número de filas en una tabla.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il numero di righe della tabella.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">gibt die Anzahl der Tabellenzeilen an.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="table-attr.rows-remarks" versionDate="2013-11-20" xml:lang="en">
        <p>If no number is supplied, an application must calculate the
	number of rows.</p>
<p>Rows should be presented from top to bottom.</p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="table-attr.rows-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Les rangées sont ordonnées de haut en bas</p>
      </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="table-attr.rows-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 行は、上から下の順番で示される。 </p>
      </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="table-attr.rows-remarks" versionDate="2017-06-19" xml:lang="de">
        <p>Wenn keine Zeilenanzahl angegeben wird, muss diese von einer Applikation berechnet werden.</p>
        <p>Zeilen sollten von oben nach unten notiert werden.</p>
      </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">columns</gloss>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">열</gloss>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">columnas</gloss>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">colonnes</gloss>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">colonne</gloss>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[6]`.

```xml
<gloss versionDate="2017-06-19" xml:lang="de">Spalten</gloss>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the number of columns in each row of the table.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">테이블의 각 행별 열의 수를 표시한다.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出表格中每一列所包含的行數。</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該表中の列数を示す。</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le nombre de colonnes dans chaque rangée du
        tableau.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el número de columnas por cada fila de la
        tabla.</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il numero di colonne in ciascuna riga della
        tabella-</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[8]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">gibt die Anzahl der Tabellenspalten an.</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="table-attr.cols-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>If no number is supplied, an application must calculate the
	number of columns.</p>
<p>Within each row, columns should be presented left to right.</p>
      </remarks>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="table-attr.cols-remarks" versionDate="2007-06-12" xml:lang="fr">
<p>Si aucun nombre n'est fourni, une application doit calculer le nombre de colonnes.</p>        <p>Dans chaque rangée, les colonnes sont ordonnées de gauche à droite.</p>
      </remarks>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="table-attr.cols-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 行中において、列は左から右への順番で示される。 </p>
      </remarks>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="table-attr.cols-remarks" versionDate="2017-06-19" xml:lang="de">
        <p>Wenn keine Spaltenanzahl angegeben wird, muss diese von einer Applikation berechnet werden.</p>
        <p>In einer Zeile sollten Spalten von links nach rechts notiert werden.</p>
      </remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-table-egXML-vy">
      <table rows="4" cols="4">
        <head>Poor Men's Lodgings in Norfolk (Mayhew, 1843)</head>
        <row role="label">
          <cell role="data"/>
          <cell role="data">Dossing Cribs or Lodging Houses</cell>
          <cell role="data">Beds</cell>
          <cell role="data">Needys or Nightly Lodgers</cell>
        </row>
        <row role="data">
          <cell role="label">Bury St Edmund's</cell>
          <cell role="data">5</cell>
          <cell role="data">8</cell>
          <cell role="data">128</cell>
        </row>
        <row role="data">
          <cell role="label">Thetford</cell>
          <cell role="data">3</cell>
          <cell role="data">6</cell>
          <cell role="data">36</cell>
        </row>
        <row role="data">
          <cell role="label">Attleboro'</cell>
          <cell role="data">3</cell>
          <cell role="data">5</cell>
          <cell role="data">20</cell>
        </row>
        <row role="data">
          <cell role="label">Wymondham</cell>
          <cell role="data">1</cell>
          <cell role="data">11</cell>
          <cell role="data">22</cell>
        </row>
      </table>
    </egXML>
  </exemplum>
```

^b48

### Block 49

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-table-egXML-cb" source="#fr-ex-Kilian-Neige">
      <table rows="4" cols="4">
        <head>Persistance de la neige dans les Alpes suisses (Denzler). </head>
        <row>
          <cell role="label">A l'altitude de</cell>
          <cell role="data">650 m.</cell>
          <cell role="data">1300m.</cell>
          <cell role="data">1950m.</cell>
          <cell role="data">2700m.</cell>
        </row>
        <row>
          <cell role="label">la neige reste</cell>
          <cell role="data">77 jours.</cell>
          <cell role="data"> 200 jours.</cell>
          <cell role="data"> 245 jours.</cell>
          <cell role="data"> 365 jours.</cell>
        </row>
      </table>
    </egXML>
  </exemplum>
```

^b49

### Block 50

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-table-egXML-ym">
      <table rows="4" cols="4">
        <head>台北飯店提供住房數目(2008年雙十國慶 )</head>
        <row role="label">
          <cell role="data"/>
          <cell role="data">經濟客房</cell>
          <cell role="data">標準客房</cell>
          <cell role="data">高級客房</cell>
        </row>
        <row role="data">
          <cell role="label">圓山大飯店</cell>
          <cell role="data">203</cell>
          <cell role="data">168</cell>
          <cell role="data">66</cell>
        </row>
        <row role="data">
          <cell role="label">凱撒大飯店</cell>
          <cell role="data">216</cell>
          <cell role="data">140</cell>
          <cell role="data">32</cell>
        </row>
        <row role="data">
          <cell role="label">喜來登大飯店</cell>
          <cell role="data">197</cell>
          <cell role="data">160</cell>
          <cell role="data">50</cell>
        </row>
        <row role="data">
          <cell role="label">君悅大飯店</cell>
          <cell role="data">177</cell>
          <cell role="data">130</cell>
          <cell role="data">22</cell>
        </row>
      </table>
    </egXML>
  </exemplum>
```

^b50

### Block 51

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="table-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Contains an optional heading and a series of rows.</p>
    <p>Any rendition information should be supplied using the global <att>rend</att> attribute, at
      the table, row, or cell level as appropriate.</p>
  </remarks>
```

^b51

### Block 52

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="table-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Contient un titre facultatif et une suite de rangées.</p>
    <p>Toute information relative à la restitution sera exprimée avec l'attribut global
      <att>rend</att> appliqué au tableau, à la rangée, ou à la cellule selon le cas.</p>
  </remarks>
```

^b52

### Block 53

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="table-remarks" versionDate="2017-06-19" xml:lang="de">
    <p rend="dataDesc">Enthält eine Reihe von Zeilen und optional eine Überschrift.</p>
    <p>Jegliche Information die grafische Darstellung betreffend, sollte mit dem globalen
      <att>rend</att>-Attribut auf der Ebene von Tabelle, Zeile oder Zelle verzeichnet werden.</p>
  </remarks>
```

^b53

### Block 54

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FTTAB1" type="div1"/>
  </listRef>
```

^b54

