---
type: representation
source-type: document
source: '[[00_sources/tei-p5-hyphenation-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 hyphenation
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/hyphenation.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# hyphenation

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10150. Git blob: `1ead01a2c8ebfe14ab4e07593bb636267e9ca73c`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-hyphenation" ident="hyphenation">
  <gloss versionDate="2009-04-27" xml:lang="en">hyphenation</gloss>
  <gloss versionDate="2009-04-27" xml:lang="fr">césurage</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">summarizes the way in which hyphenation in a source text has been treated in an encoded
    version of it.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">résume la façon dont les traits d'union sécants de fin de
    ligne d’un texte source ont été traités dans sa version encodée.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원본 텍스트의 하이픈이 부호화된 버전에서 처리된 방법을 요약한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">概述來源文件裡的連字符號在電子化的版本中是如何被處理的。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">元資料にあるハイフンが、符号化される場合にどのように扱われたかを示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">fasst zusammen, wie die Silbentrennung des Quelltextes in
    der kodierten Fassung behandelt wurde.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el modo en que han sido tratados el uso del guión
    presente en el texto fuente en la versión codificada de este.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">riassume il modo in cui il trattino nell'originale sia
    stato trattato nella versione codificata dello stesso testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="hyphenation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:hyphenation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="eol" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">end-of-line</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">행의 끝</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">fin de línea</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">fin de ligne</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">fine riga</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether or not end-of-line hyphenation has been retained in a text.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique si des traits d'union sécants de fin de ligne
        ont été conservés ou non dans un texte.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">텍스트에서 행의 끝 하이픈이 포함되었는지의 여부를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出行末連字符號是否在文本中被保留。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">行末のハイフンをそのまま残したかどうかを示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">gibt an, ob die Silbentrennung am Zeilenende im Text
        beibehalten wurde.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si el uso del guión al final de la línea se ha
        conservado en un texto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se il trattino a fine riga sia stato mantenuto
        o meno.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>some</defaultVal>
      <valList type="closed">
        <valItem ident="all">
          <desc versionDate="2007-06-27" xml:lang="en">all end-of-line hyphenation has been retained, even though the lineation of the
            original may not have been.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">tous les traits d'union sécants de fin de ligne ont été
            conservés, même si la largeur des lignes de l’original peut ne pas l’avoir été.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">원본에는 없을 수도 있지만, 모든 행 끝 하이픈이 유지되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">保留所有行末連字符號，即使原文中的不被保留。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se ha conservado la separación de corte de
            palabras mediante el guión al final de la línea, incluso cuando la lineación del
            original puede que no se haya mantenido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">元資料では改行がなかったが、行末にあるハイフンは残した。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutti i trattini di fine riga sono stati
            mantenuti, anche se l'allineamento dell'originale potrebbe non essere stato
          conservato.</desc>
        </valItem>
        <valItem ident="some">
          <desc versionDate="2007-06-27" xml:lang="en">end-of-line hyphenation has been retained in some cases.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">des traits d'union sécants de fin de ligne ont été
            conservés dans certains cas.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">일부의 경우에 행 끝 하이픈이 유지되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">行末連字符號在某些情況下被保留。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la separación silábica mediante el guión al final
            de línea se ha conservado en algunos casos.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">行末にあるハイフンは、場合によっては残した。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i trattini di fine riga sono stati mantenuti in
            alcuni casi.</desc>
        </valItem>
        <valItem ident="hard">
          <desc versionDate="2007-06-27" xml:lang="en">all soft end-of-line hyphenation has been removed: any remaining end-of-line
            hyphenation should be retained.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">tous les traits d’union sécants générés par le césurage
            en fin de ligne ont été supprimés : tout trait d’union sécant subsistant en fin de ligne doit
            être conservé.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">복합어 표시아 아닌 행 끝 하이픈이 제거되었다: 남아있는 어떤 행 끝 하이픈은 유지되어야
            한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">所有軟音的行末連字符號皆被移除：任何剩下的行末連字符號應該被保留。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se ha suprimido todo el corte de sílabas mediante
            guión al final de línea; pero se ha conservado cualquier otro corte de sílabas.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">行末にあるハイフンの殆どは除いた。いくらかは残した。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutti i trattini deboli di fine riga sono stati
            eliminati: i restanti trattini di fine riga dovrebbero essere conservati.</desc>
        </valItem>
        <valItem ident="none">
          <desc versionDate="2007-06-27" xml:lang="en">all end-of-line hyphenation has been removed: any remaining hyphenation occurred
            within the line.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">tous les traits d’union sécants en fin de ligne ont été
            supprimés : tout trait d’union sécant présent se trouvait à l’intérieur d’une ligne.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">모든 행 끝 하이픈이 제거되었다: 남아있는 어떤 하이픈은 행 내부에 나타나는 것들이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">所有行末連字符號皆被移除：剩下的是行中出現的行末連字符號。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se ha suprimido toda la separación silábica al
            final de línea; cualquier separación de sílabas conservada ocurrió dentro de la línea.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">行末にあるハイフンは全て除いた。行中にはハイフンが残っている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutti i trattini di fine riga sono stati
            eliminati: i restanti trattini si trovano all'interno di una riga.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyphenation-egXML-un">
      <hyphenation eol="some">
        <p>End-of-line hyphenation silently removed where appropriate</p>
      </hyphenation>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyphenation-egXML-rq">
      <hyphenation eol="some">
        <p>Le cas échéant, suppression du tiret de coupure de mot en de fin de ligne.</p>
      </hyphenation>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyphenation-egXML-ab">
      <hyphenation eol="some">
        <p>行末連字符號，必要時可以移除。</p>
      </hyphenation>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2009-04-27" xml:lang="en">hyphenation</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-04-27" xml:lang="fr">césurage</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">summarizes the way in which hyphenation in a source text has been treated in an encoded
    version of it.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">résume la façon dont les traits d'union sécants de fin de
    ligne d’un texte source ont été traités dans sa version encodée.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원본 텍스트의 하이픈이 부호화된 버전에서 처리된 방법을 요약한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">概述來源文件裡的連字符號在電子化的版本中是如何被處理的。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">元資料にあるハイフンが、符号化される場合にどのように扱われたかを示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">fasst zusammen, wie die Silbentrennung des Quelltextes in
    der kodierten Fassung behandelt wurde.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el modo en que han sido tratados el uso del guión
    presente en el texto fuente en la versión codificada de este.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">riassume il modo in cui il trattino nell'originale sia
    stato trattato nella versione codificata dello stesso testo.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="hyphenation-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:hyphenation"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">end-of-line</gloss>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">행의 끝</gloss>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">fin de línea</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">fin de ligne</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">fine riga</gloss>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether or not end-of-line hyphenation has been retained in a text.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique si des traits d'union sécants de fin de ligne
        ont été conservés ou non dans un texte.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트에서 행의 끝 하이픈이 포함되었는지의 여부를 표시한다.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出行末連字符號是否在文本中被保留。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">行末のハイフンをそのまま残したかどうかを示す。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt an, ob die Silbentrennung am Zeilenende im Text
        beibehalten wurde.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si el uso del guión al final de la línea se ha
        conservado en un texto.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se il trattino a fine riga sia stato mantenuto
        o meno.</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>some</defaultVal>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="all">
          <desc versionDate="2007-06-27" xml:lang="en">all end-of-line hyphenation has been retained, even though the lineation of the
            original may not have been.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">tous les traits d'union sécants de fin de ligne ont été
            conservés, même si la largeur des lignes de l’original peut ne pas l’avoir été.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">원본에는 없을 수도 있지만, 모든 행 끝 하이픈이 유지되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">保留所有行末連字符號，即使原文中的不被保留。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se ha conservado la separación de corte de
            palabras mediante el guión al final de la línea, incluso cuando la lineación del
            original puede que no se haya mantenido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">元資料では改行がなかったが、行末にあるハイフンは残した。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutti i trattini di fine riga sono stati
            mantenuti, anche se l'allineamento dell'originale potrebbe non essere stato
          conservato.</desc>
        </valItem>
        <valItem ident="some">
          <desc versionDate="2007-06-27" xml:lang="en">end-of-line hyphenation has been retained in some cases.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">des traits d'union sécants de fin de ligne ont été
            conservés dans certains cas.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">일부의 경우에 행 끝 하이픈이 유지되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">行末連字符號在某些情況下被保留。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la separación silábica mediante el guión al final
            de línea se ha conservado en algunos casos.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">行末にあるハイフンは、場合によっては残した。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">i trattini di fine riga sono stati mantenuti in
            alcuni casi.</desc>
        </valItem>
        <valItem ident="hard">
          <desc versionDate="2007-06-27" xml:lang="en">all soft end-of-line hyphenation has been removed: any remaining end-of-line
            hyphenation should be retained.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">tous les traits d’union sécants générés par le césurage
            en fin de ligne ont été supprimés : tout trait d’union sécant subsistant en fin de ligne doit
            être conservé.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">복합어 표시아 아닌 행 끝 하이픈이 제거되었다: 남아있는 어떤 행 끝 하이픈은 유지되어야
            한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">所有軟音的行末連字符號皆被移除：任何剩下的行末連字符號應該被保留。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se ha suprimido todo el corte de sílabas mediante
            guión al final de línea; pero se ha conservado cualquier otro corte de sílabas.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">行末にあるハイフンの殆どは除いた。いくらかは残した。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutti i trattini deboli di fine riga sono stati
            eliminati: i restanti trattini di fine riga dovrebbero essere conservati.</desc>
        </valItem>
        <valItem ident="none">
          <desc versionDate="2007-06-27" xml:lang="en">all end-of-line hyphenation has been removed: any remaining hyphenation occurred
            within the line.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">tous les traits d’union sécants en fin de ligne ont été
            supprimés : tout trait d’union sécant présent se trouvait à l’intérieur d’une ligne.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">모든 행 끝 하이픈이 제거되었다: 남아있는 어떤 하이픈은 행 내부에 나타나는 것들이다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">所有行末連字符號皆被移除：剩下的是行中出現的行末連字符號。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se ha suprimido toda la separación silábica al
            final de línea; cualquier separación de sílabas conservada ocurrió dentro de la línea.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">行末にあるハイフンは全て除いた。行中にはハイフンが残っている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">tutti i trattini di fine riga sono stati
            eliminati: i restanti trattini si trovano all'interno di una riga.</desc>
        </valItem>
      </valList>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyphenation-egXML-un">
      <hyphenation eol="some">
        <p>End-of-line hyphenation silently removed where appropriate</p>
      </hyphenation>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyphenation-egXML-rq">
      <hyphenation eol="some">
        <p>Le cas échéant, suppression du tiret de coupure de mot en de fin de ligne.</p>
      </hyphenation>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-hyphenation-egXML-ab">
      <hyphenation eol="some">
        <p>行末連字符號，必要時可以移除。</p>
      </hyphenation>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b33

