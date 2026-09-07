---
type: representation
source-type: document
source: '[[00_sources/tei-p5-closer-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 closer
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/closer.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# closer

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5840. Git blob: `a9195129b979634a7dd13146250fab53d3d57373`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-closer" ident="closer">
  <gloss versionDate="2007-06-12" xml:lang="en">closer</gloss>
  <gloss versionDate="2022-06-16" xml:lang="es">cierre</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">formule finale</gloss>
  <desc versionDate="2007-04-06" xml:lang="en">groups together salutations, datelines, bylines, and similar phrases appearing as a final group at
    the end of a division, especially of a letter.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구역의 마지막, 특히 편지의 종료부에 발문으로 나타나는 인사말, 날짜 표시란, 그리고 유사 구를 합하여
    모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集日期地點、署名、稱呼語、及其他在區段結尾出現的類似措辭，尤指信件結尾。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">挨拶文言、日付欄など、ある区分の終わり、特に手紙の終わりにある一連の文言をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe une formule de politesse, une indication d'une
    date et d'autres expressions semblables figurant comme expression à la fin d’une division, en
    particulier à la fin d’une lettre.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">fasst Grußformeln, Datumszeilen und ähnliche Phrasen zusammen, die am Ende eines Abschnitts
    stehen, vor allem bei einem Brief.</desc>
  <desc versionDate="2022-06-16" xml:lang="es">agrupa saludos, fechas, y expresiones similares que
aparecen en la última sección al final de una división, especialmente en una carta.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa dateline, byline, formule conclusive o di
    saluto ed espressioni simili utilizzate alla fine di una partizione, soprattutto in una lettera</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divBottomPart"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <elementRef key="byline"/>
        <elementRef key="signed"/>
        <elementRef key="dateline"/>
        <elementRef key="salute"/>
        <classRef key="model.phrase"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-kq">
      <div type="letter">
        <p> perhaps you will favour me with a sight of it when convenient.</p>
        <closer>
          <salute>I remain, &amp;c. &amp;c.</salute>
          <signed>H. Colburn</signed>
        </closer>
      </div>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-th" source="#fr-ex-Billetdoux">
      <div type="letter">
        <p> N'y voyez que le signe de l'intérêt que je que je porte à une profession qui fut la
            mienne. Je désire en effet, insérer votre article dans un ouvrage sur la presse
            française contemporaine. </p>
        <closer>
          <salute>Veuillez agréer, je vous prie, Monsieur, l'assurance de mes sentiments les
              meilleurs. </salute>
          <signed> Françoise Giroud</signed>
        </closer>
      </div>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-ne" source="#fr-ex-Montesquieu">
      <div type="chapter">
        <p>Voilà, cher Rhedi, ce que j' appelle le droit public. Voilà le droit des gens, ou
            plutôt celui de la raison. </p>
        <closer>
          <dateline><name type="place">à Paris </name>, <date>le 4 de la lune de Zilhagé, 1716. </date></dateline>
        </closer>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-ly">
      <div type="letter">
        <p> 不久，我們就能再見面。</p>
        <closer>
          <salute>祝事事順心</salute>
          <signed>謝甯</signed>
        </closer>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-mo">
      <div type="chapter">
        <p> 自己想吃人，又怕被別人吃了，都用著疑心极深的眼光，面面相覷。…… </p>
        <closer>
          <dateline>
            <name type="place">南京</name>
            <date>1918–1919</date>
          </dateline>
        </closer>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-fk" source="#DSCO-eg-53">
      <div type="chapter">
        <p><!-- ... --> and his heart was going like mad and yes I said yes I will Yes.</p>
        <closer>
          <dateline>
            <name type="place">Trieste-Zürich-Paris,</name>
            <date>1914–1921</date>
          </dateline>
        </closer>
      </div>
    </egXML>
    <!-- James Joyce, Ulysses -->
  </exemplum>
  <listRef>
    <!-- Fix for bug 3232950.  -->
    <!--<ptr target="#DSCO"/>-->
    <ptr target="#DSOC"/>
    <ptr target="#DSDTB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">closer</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2022-06-16" xml:lang="es">cierre</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">formule finale</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-04-06" xml:lang="en">groups together salutations, datelines, bylines, and similar phrases appearing as a final group at
    the end of a division, especially of a letter.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구역의 마지막, 특히 편지의 종료부에 발문으로 나타나는 인사말, 날짜 표시란, 그리고 유사 구를 합하여
    모아 놓는다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集日期地點、署名、稱呼語、及其他在區段結尾出現的類似措辭，尤指信件結尾。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">挨拶文言、日付欄など、ある区分の終わり、特に手紙の終わりにある一連の文言をまとめる。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe une formule de politesse, une indication d'une
    date et d'autres expressions semblables figurant comme expression à la fin d’une division, en
    particulier à la fin d’une lettre.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">fasst Grußformeln, Datumszeilen und ähnliche Phrasen zusammen, die am Ende eines Abschnitts
    stehen, vor allem bei einem Brief.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2022-06-16" xml:lang="es">agrupa saludos, fechas, y expresiones similares que
aparecen en la última sección al final de una división, especialmente en una carta.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa dateline, byline, formule conclusive o di
    saluto ed espressioni simili utilizzate alla fine di una partizione, soprattutto in una lettera</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divBottomPart"/>
  </classes>
```

^b12

### Block 13

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <elementRef key="byline"/>
        <elementRef key="signed"/>
        <elementRef key="dateline"/>
        <elementRef key="salute"/>
        <classRef key="model.phrase"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-kq">
      <div type="letter">
        <p> perhaps you will favour me with a sight of it when convenient.</p>
        <closer>
          <salute>I remain, &amp;c. &amp;c.</salute>
          <signed>H. Colburn</signed>
        </closer>
      </div>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-th" source="#fr-ex-Billetdoux">
      <div type="letter">
        <p> N'y voyez que le signe de l'intérêt que je que je porte à une profession qui fut la
            mienne. Je désire en effet, insérer votre article dans un ouvrage sur la presse
            française contemporaine. </p>
        <closer>
          <salute>Veuillez agréer, je vous prie, Monsieur, l'assurance de mes sentiments les
              meilleurs. </salute>
          <signed> Françoise Giroud</signed>
        </closer>
      </div>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-ne" source="#fr-ex-Montesquieu">
      <div type="chapter">
        <p>Voilà, cher Rhedi, ce que j' appelle le droit public. Voilà le droit des gens, ou
            plutôt celui de la raison. </p>
        <closer>
          <dateline><name type="place">à Paris </name>, <date>le 4 de la lune de Zilhagé, 1716. </date></dateline>
        </closer>
      </div>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-ly">
      <div type="letter">
        <p> 不久，我們就能再見面。</p>
        <closer>
          <salute>祝事事順心</salute>
          <signed>謝甯</signed>
        </closer>
      </div>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-mo">
      <div type="chapter">
        <p> 自己想吃人，又怕被別人吃了，都用著疑心极深的眼光，面面相覷。…… </p>
        <closer>
          <dateline>
            <name type="place">南京</name>
            <date>1918–1919</date>
          </dateline>
        </closer>
      </div>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-closer-egXML-fk" source="#DSCO-eg-53">
      <div type="chapter">
        <p><!-- ... --> and his heart was going like mad and yes I said yes I will Yes.</p>
        <closer>
          <dateline>
            <name type="place">Trieste-Zürich-Paris,</name>
            <date>1914–1921</date>
          </dateline>
        </closer>
      </div>
    </egXML>
    <!-- James Joyce, Ulysses -->
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <!-- Fix for bug 3232950.  -->
    <!--<ptr target="#DSCO"/>-->
    <ptr target="#DSOC"/>
    <ptr target="#DSDTB"/>
  </listRef>
```

^b20

