---
type: representation
source-type: document
source: '[[00_sources/tei-p5-postscript-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 postscript
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/postscript.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# postscript

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 5287. Git blob: `ece7edf531003ba44a7e338f320208bdadadb28a`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-postscript" ident="postscript">
  <desc versionDate="2007-08-04" xml:lang="en">contains a postscript, e.g. to a letter.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어 편지의, 추신.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">contiene una posdata, p.ej. en una carta.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">追伸を示す。例えば、手紙の場合など。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">contient un post-scriptum, par exemple au bas d' une lettre.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">contiene un post scriptum, come nel caso di una lettera.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält einen Nachtrag (Postskriptum), z. B. zu einem Brief.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divBottomPart"/>
  </classes>
  <content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
	<classRef key="model.global"/>
	<classRef key="model.divTopPart"/>
      </alternate>
      <classRef key="model.common"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
	<classRef key="model.global"/>
	<classRef key="model.common"/>
      </alternate>
      <sequence minOccurs="0" maxOccurs="unbounded">
	<classRef key="model.divBottomPart"/>
	<classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="en" versionDate="2025-05-29">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postscript-egXML-fq" source="#NONE">
      <div type="letter">
        <opener>
          <dateline>
            <placeName>Rimaone</placeName>
            <date when="2006-11-21">21 Nov 06</date>
          </dateline>
          <salute>Dear Susan,</salute>
        </opener>
        <p>Thank you very much for the assistance splitting those
	logs. I'm sorry about the misunderstanding as to the size of
	the task. I really was not asking for help, only to borrow the
	axe. Hope you had fun in any case.</p>
        <closer>
          <salute>Sincerely yours,</salute>
          <signed>Seymour</signed>
        </closer>
        <postscript>
          <label>P.S.</label>
          <p>The collision occurred on <date when="2001-07-06">06 Jul 01</date>.</p>
        </postscript>
      </div>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postscript-egXML-eu" source="#fr-ex-Weil-Atares">
      <div type="letter">
        <opener>
          <dateline>
            <date when="1942">Printemps 1942 </date>
          </dateline>
          <salute>Cher ami, </salute>
        </opener>
        <p>Le printemps vient maintenant. J'espère que là où tu es le climat à cette saison n'est
            pas encore pénible. C'est le moment des travaux des champs ; peut-être arrivera-t-on à
            quelque chose pour toi. S'il n'y a pas moyen de te faire venir en France, faut-il faire
            des démarches pour essayer de te faire quitter l'Europe ? Écris-le-moi. </p>
        <p>[...] </p>
        <closer>
          <salute> Crois à mon amitié fraternelle. </salute>
          <signed>Simone Weil </signed>
        </closer>
        <postscript>
          <label>P.S.</label>
          <p>Voici la traduction de quelques vers grecs d'Eschyle. Ils sont prononcés par
              Prométhée, le dieu qui, d'après les croyances des Grecs, avait sauvé les hommes de la
              destruction, avait volé le feu pour le leur donner et leur avait appris le langage, le
              nombre, l'astronomie, les métiers et les arts. Il en fut puni et fut cloué sur un
              rocher. La tragédie d'Eschyle commence par la scène où on le cloue ; il se tait
              pendant ce temps, puis, quand ses bourreaux sont partis, il dit : [...]</p>
        </postscript>
      </div>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postscript-egXML-rv" source="#biblzh-tw_n58">
      <div type="letter">
        <opener>
          <dateline>
            <date when="1911-03-26">辛亥三月二十六</date>
          </dateline>
          <salute>意映卿卿如晤：</salute>
        </opener>
        <p>吾今以此書與汝永別矣！吾作此書，淚珠和筆墨齊下，不能竟書，而欲擱筆！又恐汝不察吾衷，謂吾忍舍汝而死，謂吾不知汝之不欲吾死也，故遂忍悲為汝言之。...</p>
        <closer>
          <signed>夜四鼓<name>意洞</name>手書</signed>
        </closer>
      </div>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#DSDTB"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-08-04" xml:lang="en">contains a postscript, e.g. to a letter.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어 편지의, 추신.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">contiene una posdata, p.ej. en una carta.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">追伸を示す。例えば、手紙の場合など。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">contient un post-scriptum, par exemple au bas d' une lettre.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">contiene un post scriptum, come nel caso di una lettera.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält einen Nachtrag (Postskriptum), z. B. zu einem Brief.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.written"/>
    <memberOf key="model.divBottomPart"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <alternate minOccurs="0" maxOccurs="unbounded">
	<classRef key="model.global"/>
	<classRef key="model.divTopPart"/>
      </alternate>
      <classRef key="model.common"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
	<classRef key="model.global"/>
	<classRef key="model.common"/>
      </alternate>
      <sequence minOccurs="0" maxOccurs="unbounded">
	<classRef key="model.divBottomPart"/>
	<classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en" versionDate="2025-05-29">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postscript-egXML-fq" source="#NONE">
      <div type="letter">
        <opener>
          <dateline>
            <placeName>Rimaone</placeName>
            <date when="2006-11-21">21 Nov 06</date>
          </dateline>
          <salute>Dear Susan,</salute>
        </opener>
        <p>Thank you very much for the assistance splitting those
	logs. I'm sorry about the misunderstanding as to the size of
	the task. I really was not asking for help, only to borrow the
	axe. Hope you had fun in any case.</p>
        <closer>
          <salute>Sincerely yours,</salute>
          <signed>Seymour</signed>
        </closer>
        <postscript>
          <label>P.S.</label>
          <p>The collision occurred on <date when="2001-07-06">06 Jul 01</date>.</p>
        </postscript>
      </div>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postscript-egXML-eu" source="#fr-ex-Weil-Atares">
      <div type="letter">
        <opener>
          <dateline>
            <date when="1942">Printemps 1942 </date>
          </dateline>
          <salute>Cher ami, </salute>
        </opener>
        <p>Le printemps vient maintenant. J'espère que là où tu es le climat à cette saison n'est
            pas encore pénible. C'est le moment des travaux des champs ; peut-être arrivera-t-on à
            quelque chose pour toi. S'il n'y a pas moyen de te faire venir en France, faut-il faire
            des démarches pour essayer de te faire quitter l'Europe ? Écris-le-moi. </p>
        <p>[...] </p>
        <closer>
          <salute> Crois à mon amitié fraternelle. </salute>
          <signed>Simone Weil </signed>
        </closer>
        <postscript>
          <label>P.S.</label>
          <p>Voici la traduction de quelques vers grecs d'Eschyle. Ils sont prononcés par
              Prométhée, le dieu qui, d'après les croyances des Grecs, avait sauvé les hommes de la
              destruction, avait volé le feu pour le leur donner et leur avait appris le langage, le
              nombre, l'astronomie, les métiers et les arts. Il en fut puni et fut cloué sur un
              rocher. La tragédie d'Eschyle commence par la scène où on le cloue ; il se tait
              pendant ce temps, puis, quand ses bourreaux sont partis, il dit : [...]</p>
        </postscript>
      </div>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-postscript-egXML-rv" source="#biblzh-tw_n58">
      <div type="letter">
        <opener>
          <dateline>
            <date when="1911-03-26">辛亥三月二十六</date>
          </dateline>
          <salute>意映卿卿如晤：</salute>
        </opener>
        <p>吾今以此書與汝永別矣！吾作此書，淚珠和筆墨齊下，不能竟書，而欲擱筆！又恐汝不察吾衷，謂吾忍舍汝而死，謂吾不知汝之不欲吾死也，故遂忍悲為汝言之。...</p>
        <closer>
          <signed>夜四鼓<name>意洞</name>手書</signed>
        </closer>
      </div>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSDTB"/>
  </listRef>
```

^b13

