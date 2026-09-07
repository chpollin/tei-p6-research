---
type: representation
source-type: document
source: '[[00_sources/tei-p5-lb-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 lb
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/lb.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# lb

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10071. Git blob: `897408eb459782014b8f31787281b3a3aa431349`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-lb" ident="lb">
  <gloss versionDate="2017-06-14" xml:lang="en">line beginning</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">행 바꿈</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">分行</gloss>
  <gloss versionDate="2022-05-12" xml:lang="fr">début de ligne</gloss>
  <gloss versionDate="2022-05-12" xml:lang="es">inicio de línea</gloss>
  <gloss versionDate="2022-08-17" xml:lang="it">inizio di riga</gloss>
  <gloss versionDate="2017-06-25" xml:lang="de">Zeilenanfang</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">marks the beginning of a topographic line in some edition or version of a text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 편집 또는 버전에서 새로운 (인쇄상의) 행 시작을 표지한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">標記某版本文本裡 (在印刷上) 的新起行。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ある版における新しい(印刷上の)行の始まりを示す。</desc>
  <desc versionDate="2022-05-12" xml:lang="fr">marque le début d'une nouvelle ligne (typographique) dans
    une édition ou dans une version d'un texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">marca el comienzo de una nueva línea (topográfica) en
    alguna edición o versión del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">segna l'inizio di una nuova riga (tipografica) in qualche
    edizione o versione di un testo.</desc>
  <desc versionDate="2017-06-25" xml:lang="de">markiert den Anfang einer neuen typographischen 
    Zeile in einer bestimmten Auflage oder Version eines Textes.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.breaking"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
  <content><empty/></content>
  <exemplum xml:lang="en">
    <p>This example shows the encoding of the beginning of each new topographic line within a metrical line, indicating where it occurs in both the 1667 and 1674 editions:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-vk">
      <l>Of Mans First Disobedience,<lb ed="1674"/> and<lb ed="1667"/> the Fruit</l>
      <l>Of that Forbidden Tree, whose<lb ed="1667 1674"/> mortal tast</l>
      <l>Brought Death into the World,<lb ed="1667"/> and all<lb ed="1674"/> our woe,</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <p xml:lang="fr">Cet exemple montre les sauts de ligne dans des vers, qui apparaissent à différents endroits selon les éditions.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-bq">
      <l>Of Mans First Disobedience,<lb ed="1674"/> and<lb ed="1667"/> the Fruit</l>
      <l>Of that Forbidden Tree, whose<lb ed="1667 1674"/> mortal tast</l>
      <l>Brought Death into the World,<lb ed="1667"/> and all<lb ed="1674"/> our woe,</l>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Dieses Beispiel zeigt typografische Zeilenumbrüche innerhalb von Verszeilen, so wie sie an
      verschiedenen Stellen in unterschiedlichen Ausgaben auftreten:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-ct">
      <l>Of Mans First Disobedience,<lb ed="1674"/> and<lb ed="1667"/> the Fruit</l>
      <l>Of that Forbidden Tree, whose<lb ed="1667 1674"/> mortal tast</l>
      <l>Brought Death into the World,<lb ed="1667"/> and all<lb ed="1674"/> our woe,</l>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>This example shows the encoding of the beginning of a new topographical line as a means of
preserving the visual appearance of a title page. The <att>break</att>
      attribute is used to show that the beginning of the new line does not (as elsewhere)
mark the start of a new word.  </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-cz">
      <titlePart><lb/>With Additions, ne-<lb break="no"/>ver before Printed.</titlePart>
    </egXML>
  </exemplum>
  <exemplum xml:lang="fr">
    <p xml:lang="fr">Cet exemple encode les sauts de ligne pour montre l'apparence visuelle d'une page titre. L'attribut <att>break</att> est utilisé pour montrer que le saut de ligne ne marque pas le début d'un nouveau mot.</p>
    <!--egXML xmlns="http://www.tei-c.org/ns/Examples" xml:lang="fr" source="#rab3"-->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-fu" xml:lang="fr">
      <titlePart rend="italic"><lb/>L'auteur susdict supplie les Lecteurs
<lb/>benevoles, soy reserver à rire au 
soi-<lb break="no"/>xante &amp; dixhuytiesme livre.
</titlePart>
    </egXML>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Dieses Beispiel kodiert typografische Zeilenumbrüche, um das visuelle Erscheinungsbild einer
      Titelseite zu bewahren. Das <att>break</att>-Attribut zeigt an, dass der Zeilenumbruch nicht
      (wie anderswo) den Anfang eines neuen Wortes markiert.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-qn">
      <titlePart><lb/>With Additions, ne-<lb break="no"/>ver before Printed.</titlePart>
    </egXML>
  </exemplum>
  <remarks ident="lb-remarks" versionDate="2013-01-09" xml:lang="en">
    <p>By convention, <gi>lb</gi> elements should appear at the point in the text where a new line
      starts. The <att>n</att> attribute, if used, indicates the number or other value associated
      with the text between this point and the next <gi>lb</gi> element, typically the sequence
      number of the line within the page, or other appropriate unit. This element is intended to be
      used for marking the beginning of each new topographic line on a manuscript or printed page, at the point where it
      occurs; it should not be used to tag structural units such as lines of verse (for which the
        <gi>l</gi> element is available) except in circumstances where structural units cannot
      otherwise be marked. </p>
    <p>The <att>type</att> attribute may be used to characterize the
    line beginning in any respect. The more specialized attributes
    <att>break</att>, <att>ed</att>, or <att>edRef</att> should be preferred when the
      intent is to indicate whether or not the beginning of the new topographic line
     is word-breaking, or to note the source from which it
    derives.  </p>
  </remarks>
  <remarks ident="lb-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Par convention, l'élément <gi>lb</gi> apparaît à l’endroit du texte où commence une nouvelle
      ligne. L'attribut <att>n</att>, s’il est utilisé, donne un nombre ou une autre valeur associée
      au texte entre ce point et l’élément suivant <gi>lb</gi>, spécifiquement le numéro de la ligne
      dans la page, ou une autre unité de mesure appropriée. Cet élément est prévu pour être employé
      pour marquer un saut de ligne sur un manuscrit ou sur une page imprimée, à l’endroit où il se
      survient; on n’utilisera pas de balisage structurel comme une succession de vers (pour lequel
      l’élément <gi>l</gi> est disponible) sauf dans le cas où des blocs structurés ne peuvent pas
      être marqués autrement. </p>
    <p> L'attribut <att>type</att> sera employé pour caractériser toute espèce de caractéristiques
      du saut de ligne, sauf la coupure des mots (indique par
    l'attribut <att>break</att>) ou la source concernée. </p>
  </remarks>
  <remarks ident="lb-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素にあるグローバル属性<att>n</att>は、要素<gi>lb</gi>に続く 行と関連する数値を示す。符号化する人は、改行を示す当該数値が、ペー
      ジ内にある物理的行数またはテキストの論理構造と関連するかについて、 明確で一貫した方針を採るべきである。 一般には、要素<gi>lb</gi>は、参照する行の開始地点にあるべきである。 </p>
    <p> 要素<gi>lb</gi>は、散文中における印刷上の行を示すためのものである。 韻文中の行を示す要素<gi>l</gi>とは注意して使い分けるべきである。 </p>
  </remarks>
  <remarks ident="lb-remarks" versionDate="2016-11-29" xml:lang="de">
    <p>Es ist Konvention, dass <gi>lb</gi>-Elemente an der Stelle im Text stehen sollen, 
      an der eine neue Zeile beginnt. Das <att>n</att>-Attribut enhält gegebenenfalls 
      die Nummer der Zeile oder einen ähnlichen Wert, der sich auf den Text bezieht, 
      der bis zum nächsten <gi>lb</gi> folgt, typischerweise die Nummer einer Zeile 
      auf einer Seite oder andere einschlägige Einheiten.</p> 
    <p>Das Element dient dazu, typographische oder paläographische Phänomene an der 
      Stelle zu beschreiben, an der sie auf dem Schriftträger sichtbar sind; 
      es sollte nicht für Struktureinheiten wie z. B. Verszeilen in Lyrik verwendet 
      werden (wofür das Element <gi>l</gi> zur Verfügung steht), außer wenn derartige 
      Struktureinheiten anders nicht markiert werden können. </p>
    <p>Das <att>type</att>-Attribut kann verwendet werden, den Zeilenwechsel näher 
      zu beschreiben, wenn nicht die speziellen Attribute <att>break</att> 
      (Worttrennung), <att>ed</att> oder <att>edRef</att> (Textzeuge, in dem der 
      Zeilenwechsel vorkommt) verwendet werden können.</p>
  </remarks>
  <listRef>
    <ptr target="#CORS5" type="div3"/>
    <ptr target="#DRPAL" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2017-06-14" xml:lang="en">line beginning</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">행 바꿈</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">分行</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2022-05-12" xml:lang="fr">début de ligne</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2022-05-12" xml:lang="es">inicio de línea</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2022-08-17" xml:lang="it">inizio di riga</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2017-06-25" xml:lang="de">Zeilenanfang</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">marks the beginning of a topographic line in some edition or version of a text.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 편집 또는 버전에서 새로운 (인쇄상의) 행 시작을 표지한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標記某版本文本裡 (在印刷上) 的新起行。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ある版における新しい(印刷上の)行の始まりを示す。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2022-05-12" xml:lang="fr">marque le début d'une nouvelle ligne (typographique) dans
    une édition ou dans une version d'un texte.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">marca el comienzo de una nueva línea (topográfica) en
    alguna edición o versión del texto.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">segna l'inizio di una nuova riga (tipografica) in qualche
    edizione o versione di un testo.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2017-06-25" xml:lang="de">markiert den Anfang einer neuen typographischen 
    Zeile in einer bestimmten Auflage oder Version eines Textes.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.breaking"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.spanning"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.milestoneLike"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>This example shows the encoding of the beginning of each new topographic line within a metrical line, indicating where it occurs in both the 1667 and 1674 editions:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-vk">
      <l>Of Mans First Disobedience,<lb ed="1674"/> and<lb ed="1667"/> the Fruit</l>
      <l>Of that Forbidden Tree, whose<lb ed="1667 1674"/> mortal tast</l>
      <l>Brought Death into the World,<lb ed="1667"/> and all<lb ed="1674"/> our woe,</l>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="fr">
    <p xml:lang="fr">Cet exemple montre les sauts de ligne dans des vers, qui apparaissent à différents endroits selon les éditions.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-bq">
      <l>Of Mans First Disobedience,<lb ed="1674"/> and<lb ed="1667"/> the Fruit</l>
      <l>Of that Forbidden Tree, whose<lb ed="1667 1674"/> mortal tast</l>
      <l>Brought Death into the World,<lb ed="1667"/> and all<lb ed="1674"/> our woe,</l>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Dieses Beispiel zeigt typografische Zeilenumbrüche innerhalb von Verszeilen, so wie sie an
      verschiedenen Stellen in unterschiedlichen Ausgaben auftreten:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-ct">
      <l>Of Mans First Disobedience,<lb ed="1674"/> and<lb ed="1667"/> the Fruit</l>
      <l>Of that Forbidden Tree, whose<lb ed="1667 1674"/> mortal tast</l>
      <l>Brought Death into the World,<lb ed="1667"/> and all<lb ed="1674"/> our woe,</l>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <p>This example shows the encoding of the beginning of a new topographical line as a means of
preserving the visual appearance of a title page. The <att>break</att>
      attribute is used to show that the beginning of the new line does not (as elsewhere)
mark the start of a new word.  </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-cz">
      <titlePart><lb/>With Additions, ne-<lb break="no"/>ver before Printed.</titlePart>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="fr">
    <p xml:lang="fr">Cet exemple encode les sauts de ligne pour montre l'apparence visuelle d'une page titre. L'attribut <att>break</att> est utilisé pour montrer que le saut de ligne ne marque pas le début d'un nouveau mot.</p>
    <!--egXML xmlns="http://www.tei-c.org/ns/Examples" xml:lang="fr" source="#rab3"-->
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-fu" xml:lang="fr">
      <titlePart rend="italic"><lb/>L'auteur susdict supplie les Lecteurs
<lb/>benevoles, soy reserver à rire au 
soi-<lb break="no"/>xante &amp; dixhuytiesme livre.
</titlePart>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Dieses Beispiel kodiert typografische Zeilenumbrüche, um das visuelle Erscheinungsbild einer
      Titelseite zu bewahren. Das <att>break</att>-Attribut zeigt an, dass der Zeilenumbruch nicht
      (wie anderswo) den Anfang eines neuen Wortes markiert.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-lb-egXML-qn">
      <titlePart><lb/>With Additions, ne-<lb break="no"/>ver before Printed.</titlePart>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="lb-remarks" versionDate="2013-01-09" xml:lang="en">
    <p>By convention, <gi>lb</gi> elements should appear at the point in the text where a new line
      starts. The <att>n</att> attribute, if used, indicates the number or other value associated
      with the text between this point and the next <gi>lb</gi> element, typically the sequence
      number of the line within the page, or other appropriate unit. This element is intended to be
      used for marking the beginning of each new topographic line on a manuscript or printed page, at the point where it
      occurs; it should not be used to tag structural units such as lines of verse (for which the
        <gi>l</gi> element is available) except in circumstances where structural units cannot
      otherwise be marked. </p>
    <p>The <att>type</att> attribute may be used to characterize the
    line beginning in any respect. The more specialized attributes
    <att>break</att>, <att>ed</att>, or <att>edRef</att> should be preferred when the
      intent is to indicate whether or not the beginning of the new topographic line
     is word-breaking, or to note the source from which it
    derives.  </p>
  </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="lb-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p> Par convention, l'élément <gi>lb</gi> apparaît à l’endroit du texte où commence une nouvelle
      ligne. L'attribut <att>n</att>, s’il est utilisé, donne un nombre ou une autre valeur associée
      au texte entre ce point et l’élément suivant <gi>lb</gi>, spécifiquement le numéro de la ligne
      dans la page, ou une autre unité de mesure appropriée. Cet élément est prévu pour être employé
      pour marquer un saut de ligne sur un manuscrit ou sur une page imprimée, à l’endroit où il se
      survient; on n’utilisera pas de balisage structurel comme une succession de vers (pour lequel
      l’élément <gi>l</gi> est disponible) sauf dans le cas où des blocs structurés ne peuvent pas
      être marqués autrement. </p>
    <p> L'attribut <att>type</att> sera employé pour caractériser toute espèce de caractéristiques
      du saut de ligne, sauf la coupure des mots (indique par
    l'attribut <att>break</att>) ou la source concernée. </p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="lb-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 当該要素にあるグローバル属性<att>n</att>は、要素<gi>lb</gi>に続く 行と関連する数値を示す。符号化する人は、改行を示す当該数値が、ペー
      ジ内にある物理的行数またはテキストの論理構造と関連するかについて、 明確で一貫した方針を採るべきである。 一般には、要素<gi>lb</gi>は、参照する行の開始地点にあるべきである。 </p>
    <p> 要素<gi>lb</gi>は、散文中における印刷上の行を示すためのものである。 韻文中の行を示す要素<gi>l</gi>とは注意して使い分けるべきである。 </p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="lb-remarks" versionDate="2016-11-29" xml:lang="de">
    <p>Es ist Konvention, dass <gi>lb</gi>-Elemente an der Stelle im Text stehen sollen, 
      an der eine neue Zeile beginnt. Das <att>n</att>-Attribut enhält gegebenenfalls 
      die Nummer der Zeile oder einen ähnlichen Wert, der sich auf den Text bezieht, 
      der bis zum nächsten <gi>lb</gi> folgt, typischerweise die Nummer einer Zeile 
      auf einer Seite oder andere einschlägige Einheiten.</p> 
    <p>Das Element dient dazu, typographische oder paläographische Phänomene an der 
      Stelle zu beschreiben, an der sie auf dem Schriftträger sichtbar sind; 
      es sollte nicht für Struktureinheiten wie z. B. Verszeilen in Lyrik verwendet 
      werden (wofür das Element <gi>l</gi> zur Verfügung steht), außer wenn derartige 
      Struktureinheiten anders nicht markiert werden können. </p>
    <p>Das <att>type</att>-Attribut kann verwendet werden, den Zeilenwechsel näher 
      zu beschreiben, wenn nicht die speziellen Attribute <att>break</att> 
      (Worttrennung), <att>ed</att> oder <att>edRef</att> (Textzeuge, in dem der 
      Zeilenwechsel vorkommt) verwendet werden können.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CORS5" type="div3"/>
    <ptr target="#DRPAL" type="div3"/>
  </listRef>
```

^b28

