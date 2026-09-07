---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.tabledecoration-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.tableDecoration
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.tableDecoration.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.tableDecoration

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10704. Git blob: `579bd6df55f52f803a687c207e3117631074a84d`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="figures" type="atts" ident="att.tableDecoration">
  <desc versionDate="2006-04-17" xml:lang="en">provides attributes used to decorate rows or cells of a table.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">테이블의 행 또는 셀을 장식하는 속성을 제공한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">提供屬性，用以裝飾表格內的儲存格或列。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">表の行またはセルを修飾する属性を示す。</desc>
  <desc versionDate="2009-05-28" xml:lang="fr">fournit des attributs pour mettre en forme les lignes ou les cellules d'un tableau.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">proporciona atributos usados para decorar filas o celdas de una tabla.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi utilizzati per decorare righe e celle di una tabella.</desc>
  <attList>
    <attDef ident="role" usage="opt">
      <gloss versionDate="2009-05-28" xml:lang="en">role</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">rôle</gloss>
      <desc versionDate="2006-04-17" xml:lang="en">indicates the kind of information held in this cell or
in each cell of this row.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 셀에 또는 이 행의 각 셀에 나타난 정보의 종류를 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出此儲存格或列當中，各儲存格所包含的資訊類型。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該セル、または当該行中のセルにある情報の種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le type des
      informations contenues dans cette cellule ou dans chaque cellule de cette ligne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el tipo de información contenida en la celda en cuestión o en cada una de las celdas de la fila.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il tipo di informazione contenuta nela cella in questione o in ciascuna delle celle della riga presa in esame.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>data</defaultVal>
      <valList type="semi">
        <valItem ident="label">
          <desc versionDate="2007-06-27" xml:lang="en">labelling or descriptive information only.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표지 또는 기술적 정보만 허용</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">僅為標號或描述性資訊。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">etiquetado o información descriptiva solamente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">記述的情報またはラベルのみ。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">uniquement des informations relatives au codage ou à la description</desc>
          <desc versionDate="2007-01-21" xml:lang="it">informazione esclusivamente descrittiva o del tipo etichetta.</desc>
        </valItem>
        <valItem ident="data">
          <desc versionDate="2007-06-27" xml:lang="en">data values.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">데이터 값</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">數據值。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">valores de datos.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">日付情報。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">valeurs de données</desc>
          <desc versionDate="2007-01-21" xml:lang="it">valori di dati.</desc>
        </valItem>
      </valList>
      <remarks ident="att.tableDecoration-attr.role-remarks" versionDate="2006-04-17" xml:lang="en">
        <p>When this attribute is specified on a row, its value is the
	default for all cells in this row. When specified on a cell,
	its value overrides any default specified by the
<att>role</att> attribute of the parent <gi>row</gi> element.</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.role-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p> Quand cet attribut est appliqué à une ligne de tableau, sa valeur est
                        transmise comme valeur par défaut à toutes les cellules de cette ligne.
                        Quand il est spécifié sur une cellule, sa valeur annule et remplace toute
                        valeur spécifiée par défaut dans l'attribut <att>role</att> de l'élément
                        parent <gi>row</gi>.</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.role-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Cuando este atributo se especifica en una fila, su valor es el valor por defecto para todas las celdas de esta fila. Cuando está especificado en una celda, su valor reemplaza cualquier valor por defecto especificado por
el atributo <att>role</att> (papel) del elemento padre <gi>row</gi> (fila).</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.role-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該属性が行に付与されている場合、当該属性値は当該行中の全セル
        のデフォルト値になる。当該属性がセルに付与されている場合、当該
        属性値は、親要素<gi>row</gi>の属性<att>role</att>にあるデフォ
        ルト値を上書きする。
      </p>
      </remarks>
    </attDef>
    <attDef ident="rows" usage="opt">
      <gloss versionDate="2009-05-28" xml:lang="en">rows</gloss>
      <gloss versionDate="2009-05-28" xml:lang="fr">lignes</gloss>
      <desc versionDate="2006-04-17" xml:lang="en">indicates the number of rows occupied by this cell or row.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 셀 또는 행에 의해 사용된 행의 수를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出此儲存格或列所占的列數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該セルまたは行を含む行の数を示す。</desc>
      <desc versionDate="2009-05-28" xml:lang="fr">indique le nombre de lignes occupées par la cellule ou la ligne en question.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el número de filas ocupado por una celda o por la fila en cuestión.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il numero di righe occupate dalla cella o riga in questione.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <defaultVal>1</defaultVal>
      <remarks ident="att.tableDecoration-attr.rows-remarks" versionDate="2013-12-09" xml:lang="en">
        <p>A value greater than one indicates that this
      cell <!--(or row)-->
      spans several rows. Where several cells span multiple rows, it may be more convenient
to use nested tables.</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.rows-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p> Lorsque plusieurs cellules s'étendent sur plusieurs lignes, il peut être plus pratique d'employer des tableaux inclus.</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.rows-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Donde varias celdas atraviesan varias filas, puede ser más conveniente utilizar los vectores jerarquizados.</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.rows-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        複数のセルが複数行に渡る場合には、入れ子の表を使った方が便利で
        ある。
        </p>
      </remarks>
    </attDef>
    <attDef ident="cols" usage="opt">
      <gloss versionDate="2007-07-02" xml:lang="en">columns</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">열</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">columnas</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">colonnes</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">colonne</gloss>
      <desc versionDate="2006-04-17" xml:lang="en">indicates the number of columns occupied by this cell or
	row.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 셀 또는 행에 의해 사용된 열의 수를 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出此儲存格或列所佔的欄位數。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該セルまたは行を含む列の数を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le nombre de colonnes occupées par cette cellule ou cette ligne.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el número de columnas que abraza una celda o fila.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il numero di colonne occupate dalla cella o riga.</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <defaultVal>1</defaultVal>
      <remarks ident="att.tableDecoration-attr.cols-remarks" versionDate="2013-12-09" xml:lang="en">
        <p>A value greater than one indicates that this cell or row
        spans several columns. Where an initial cell spans an entire
        row, it may be better treated as a heading.</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.cols-remarks" versionDate="2013-12-09" xml:lang="fr">
        <p>Une valeur plus grande que 1 indique que cette cellule (ou cette ligne)
        occupe plusieurs colonnes. Lorsqu'une première cellule s'étend sur une ligne entière, il peut être préférable de la considérer comme un titre.</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.cols-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Donde una celda inicial atraviesa una fila entera, puede ser tratada como título.</p>
      </remarks>
      <remarks ident="att.tableDecoration-attr.cols-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        始めのセルが行全体である場合には、見出しとして扱った方がよい。
        </p>
      </remarks>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#FT"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2006-04-17" xml:lang="en">provides attributes used to decorate rows or cells of a table.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">테이블의 행 또는 셀을 장식하는 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">提供屬性，用以裝飾表格內的儲存格或列。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">表の行またはセルを修飾する属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">fournit des attributs pour mettre en forme les lignes ou les cellules d'un tableau.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">proporciona atributos usados para decorar filas o celdas de una tabla.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">assegna degli attributi utilizzati per decorare righe e celle di una tabella.</desc>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="en">role</gloss>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">rôle</gloss>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2006-04-17" xml:lang="en">indicates the kind of information held in this cell or
in each cell of this row.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 셀에 또는 이 행의 각 셀에 나타난 정보의 종류를 제시한다.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出此儲存格或列當中，各儲存格所包含的資訊類型。</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該セル、または当該行中のセルにある情報の種類を示す。</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le type des
      informations contenues dans cette cellule ou dans chaque cellule de cette ligne.</desc>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el tipo de información contenida en la celda en cuestión o en cada una de las celdas de la fila.</desc>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il tipo di informazione contenuta nela cella in questione o in ciascuna delle celle della riga presa in esame.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>data</defaultVal>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="label">
          <desc versionDate="2007-06-27" xml:lang="en">labelling or descriptive information only.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표지 또는 기술적 정보만 허용</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">僅為標號或描述性資訊。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">etiquetado o información descriptiva solamente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">記述的情報またはラベルのみ。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">uniquement des informations relatives au codage ou à la description</desc>
          <desc versionDate="2007-01-21" xml:lang="it">informazione esclusivamente descrittiva o del tipo etichetta.</desc>
        </valItem>
        <valItem ident="data">
          <desc versionDate="2007-06-27" xml:lang="en">data values.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">데이터 값</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">數據值。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">valores de datos.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">日付情報。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">valeurs de données</desc>
          <desc versionDate="2007-01-21" xml:lang="it">valori di dati.</desc>
        </valItem>
      </valList>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.tableDecoration-attr.role-remarks" versionDate="2006-04-17" xml:lang="en">
        <p>When this attribute is specified on a row, its value is the
	default for all cells in this row. When specified on a cell,
	its value overrides any default specified by the
<att>role</att> attribute of the parent <gi>row</gi> element.</p>
      </remarks>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.tableDecoration-attr.role-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p> Quand cet attribut est appliqué à une ligne de tableau, sa valeur est
                        transmise comme valeur par défaut à toutes les cellules de cette ligne.
                        Quand il est spécifié sur une cellule, sa valeur annule et remplace toute
                        valeur spécifiée par défaut dans l'attribut <att>role</att> de l'élément
                        parent <gi>row</gi>.</p>
      </remarks>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.tableDecoration-attr.role-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Cuando este atributo se especifica en una fila, su valor es el valor por defecto para todas las celdas de esta fila. Cuando está especificado en una celda, su valor reemplaza cualquier valor por defecto especificado por
el atributo <att>role</att> (papel) del elemento padre <gi>row</gi> (fila).</p>
      </remarks>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="att.tableDecoration-attr.role-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        当該属性が行に付与されている場合、当該属性値は当該行中の全セル
        のデフォルト値になる。当該属性がセルに付与されている場合、当該
        属性値は、親要素<gi>row</gi>の属性<att>role</att>にあるデフォ
        ルト値を上書きする。
      </p>
      </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="en">rows</gloss>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2009-05-28" xml:lang="fr">lignes</gloss>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2006-04-17" xml:lang="en">indicates the number of rows occupied by this cell or row.</desc>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 셀 또는 행에 의해 사용된 행의 수를 나타낸다.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出此儲存格或列所占的列數。</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該セルまたは行を含む行の数を示す。</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2009-05-28" xml:lang="fr">indique le nombre de lignes occupées par la cellule ou la ligne en question.</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el número de filas ocupado por una celda o por la fila en cuestión.</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il numero di righe occupate dalla cella o riga in questione.</desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>1</defaultVal>
```

^b34

### Block 35

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="att.tableDecoration-attr.rows-remarks" versionDate="2013-12-09" xml:lang="en">
        <p>A value greater than one indicates that this
      cell <!--(or row)-->
      spans several rows. Where several cells span multiple rows, it may be more convenient
to use nested tables.</p>
      </remarks>
```

^b35

### Block 36

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="att.tableDecoration-attr.rows-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p> Lorsque plusieurs cellules s'étendent sur plusieurs lignes, il peut être plus pratique d'employer des tableaux inclus.</p>
      </remarks>
```

^b36

### Block 37

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="att.tableDecoration-attr.rows-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Donde varias celdas atraviesan varias filas, puede ser más conveniente utilizar los vectores jerarquizados.</p>
      </remarks>
```

^b37

### Block 38

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="att.tableDecoration-attr.rows-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        複数のセルが複数行に渡る場合には、入れ子の表を使った方が便利で
        ある。
        </p>
      </remarks>
```

^b38

### Block 39

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2007-07-02" xml:lang="en">columns</gloss>
```

^b39

### Block 40

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">열</gloss>
```

^b40

### Block 41

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">columnas</gloss>
```

^b41

### Block 42

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">colonnes</gloss>
```

^b42

### Block 43

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">colonne</gloss>
```

^b43

### Block 44

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2006-04-17" xml:lang="en">indicates the number of columns occupied by this cell or
	row.</desc>
```

^b44

### Block 45

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 셀 또는 행에 의해 사용된 열의 수를 나타낸다.</desc>
```

^b45

### Block 46

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出此儲存格或列所佔的欄位數。</desc>
```

^b46

### Block 47

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該セルまたは行を含む列の数を示す。</desc>
```

^b47

### Block 48

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le nombre de colonnes occupées par cette cellule ou cette ligne.</desc>
```

^b48

### Block 49

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el número de columnas que abraza una celda o fila.</desc>
```

^b49

### Block 50

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il numero di colonne occupate dalla cella o riga.</desc>
```

^b50

### Block 51

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b51

### Block 52

XML location: `/classSpec[1]/attList[1]/attDef[3]/defaultVal[1]`.

```xml
<defaultVal>1</defaultVal>
```

^b52

### Block 53

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[1]`.

```xml
<remarks ident="att.tableDecoration-attr.cols-remarks" versionDate="2013-12-09" xml:lang="en">
        <p>A value greater than one indicates that this cell or row
        spans several columns. Where an initial cell spans an entire
        row, it may be better treated as a heading.</p>
      </remarks>
```

^b53

### Block 54

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[2]`.

```xml
<remarks ident="att.tableDecoration-attr.cols-remarks" versionDate="2013-12-09" xml:lang="fr">
        <p>Une valeur plus grande que 1 indique que cette cellule (ou cette ligne)
        occupe plusieurs colonnes. Lorsqu'une première cellule s'étend sur une ligne entière, il peut être préférable de la considérer comme un titre.</p>
      </remarks>
```

^b54

### Block 55

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[3]`.

```xml
<remarks ident="att.tableDecoration-attr.cols-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Donde una celda inicial atraviesa una fila entera, puede ser tratada como título.</p>
      </remarks>
```

^b55

### Block 56

XML location: `/classSpec[1]/attList[1]/attDef[3]/remarks[4]`.

```xml
<remarks ident="att.tableDecoration-attr.cols-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        始めのセルが行全体である場合には、見出しとして扱った方がよい。
        </p>
      </remarks>
```

^b56

### Block 57

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#FT"/>
  </listRef>
```

^b57

