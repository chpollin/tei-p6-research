---
type: representation
source-type: document
source: '[[00_sources/tei-p5-front-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 front
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/front.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# front

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12008. Git blob: `6b3e5420d4cfb77271c2f7e067f5b482f54240f5`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="textstructure" xml:id="gi-front" ident="front">
  <gloss versionDate="2005-01-14" xml:lang="en">front matter</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">전면부 내용</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">正文前資訊</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">texte préliminaire</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Vorspann (front)</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">paratexto inicial</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">peritesto iniziale</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains any prefatory matter
  (headers, abstracts, title page, prefaces, dedications, etc.) found at the
  start of a document, before the main body.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">주 본문 앞에 나타나는 문서의 시작부에서 발견되는 서문
  자료(헤더, 제목 페이지, 머리말, 헌정사 등)를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含位於文件最前端、正文之前的項目
  (標頭、題名頁、前言、獻詞等) 。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">本文より前、文書の始めにある序文としてあるもの(標題、タイトル、序文、 献辞など)。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient tout ce qui est au début
  du document, avant le corps du texte : page de titre, dédicaces, préfaces,
  etc.</desc>
  <desc versionDate="2017-06-19" xml:lang="de">enthält alle dem Textkörper vorangestellten Texte (Überschriften, Abstracts, Titelseite,
  Vorworte, Widmungen, usw.) zu Beginn eines Dokuments.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene cualquier material
  paratextual (encabezamiento, frontispicio, prefacio, dedicatoria, etc.) que
  aparece delante del inicio del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene qualsiasi materiale
  peritestuale (intestazioni, frontespizio, prefazioni, dediche, etc.) che si
  trovi prima dell'inizio del testo vero e proprio</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
  </classes>
  <content>
    <sequence>
      <!-- 
           we start with allowing a group of mixed-up p-like elements.
           when we are done with them, we can start considering
           div-like elements, and the things that
           can occur after them.
      -->
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.frontPart"/>
        <classRef key="model.pLike"/>
        <classRef key="model.pLike.front"/>
        <classRef key="model.global"/>
      </alternate>
      <sequence minOccurs="0">
        <alternate>
          <!-- 1. has a div1Like, after optional front parts -->
          <sequence>
            <classRef key="model.div1Like"/>
            <alternate minOccurs="0" maxOccurs="unbounded">
              <classRef key="model.div1Like"/>
              <classRef key="model.frontPart"/>
              <classRef key="model.global"/>
            </alternate>
          </sequence>
          <!-- 1. has a divLike, after optional front parts -->
          <sequence>
            <classRef key="model.divLike"/>
            <alternate minOccurs="0" maxOccurs="unbounded">
              <classRef key="model.divLike"/>
              <classRef key="model.frontPart"/>
              <classRef key="model.global"/>
            </alternate>
          </sequence>
        </alternate>
        <!-- and some bottoms, mebbe -->
        <sequence minOccurs="0">
          <classRef key="model.divBottom"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.divBottom"/>
            <classRef key="model.global"/>
          </alternate>
        </sequence>
      </sequence>
    </sequence>
  </content>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-zr" source="#COEDADD-eg-89">
      <front>
        <epigraph>
          <quote>Nam Sibyllam quidem Cumis ego ipse oculis meis vidi in ampulla
          pendere, et cum illi pueri dicerent: <q xml:lang="grc">Σίβυλλα τί
          θέλεις</q>; respondebat illa: <q xml:lang="grc">ὰποθανεῖν θέλω.</q>
          </quote>
        </epigraph>
        <div type="dedication">
          <p>For Ezra Pound <q xml:lang="it">il miglior fabbro.</q>
          </p>
        </div>
      </front>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-ik" source="#fr-ex-Perec-vie">
      <front>
        <div type="dedication">
          <p>à la mémoire de Raymond Queneau</p>
        </div>
        <div type="avertissement">
          <p>L'amitié, l'histoire et la littérature m'ont fourni quelques-uns
          des.personnages de ce livre. Toute autre ressemblance avec des
          individus vivants ou ayant réellement ou fictivement existé ne
          saurait être que coïncidence.</p>
          <epigraph>
            <quote>Regarde de tous tes yeux, regarde <bibl>(Jules Verne, Michel
            Strogoff )</bibl>
            </quote>
          </epigraph>
        </div>
        <div type="preambule">
          <head>PRÉAMBULE</head>
          <epigraph>
            <quote>
              <q>L'œil suit les chemins qui lui ont été ménagés dans l'oeuvre
              <bibl>(Paul Klee, Pädagosisches Skizzenbuch)</bibl>
              </q>
            </quote>
          </epigraph>
          <p> Au départ, l'art du puzzle semble un art bref, un art mince, tout
          entier contenu dans un maigre enseignement de la Gestalttheorie :
          ...</p>
        </div>
      </front>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-xb" source="#fr-ex-Hugo-miserables">
      <front>
        <div type="preface">
          <head>Préface</head>
          <p>Tant qu'il existera, par le fait des lois et des moeurs, une
          damnation sociale créant artificiellement, en pleine civilisation,
          des enfers, et compliquant d'une fatalité humaine la destinée qui
          est divine ; tant que les trois problèmes du siècle, la dégradation
          de l'homme par le prolétariat, la déchéance de la femme par la faim,
          l'atrophie de l'enfant par la nuit, ne seront pas résolus; tant que,
          dans certaines régions, l'asphyxie sociale sera possible; en
          d'autres termes, et à un point de vue plus étendu encore, tant qu'il
          aura sur la terre ignorance et misère, des livres de la nature de
          celui-ci pourront ne pas être inutiles.</p>
          <closer>
            <dateline>
              <name type="place">Hauteville-House</name>
              <date>1er janvier 1862</date>
            </dateline>
          </closer>
        </div>
      </front>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-bm" source="#biblzh-tw_n56-57">
      <front>
        <epigraph>
          <quote>小燕子其實也無所愛，只是沉浸在朦朧而飄忽的夏夜夢里罷了。 </quote>
        </epigraph>
        <div type="dedication">
          <p>《憶》第三十五首</p>
        </div>
      </front>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-eq">
      <front>
        <div type="dedication">
          <p>聲明啟事</p>
        </div>
        <div type="preface">
          <head>作者聲明</head>
          <p>書中所有情節內容皆為虛構，若有雷同，純屬巧合。</p>
        </div>
      </front>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-to" source="#hallWell">
      <front>
        <div type="dedication">
          <p>To our three selves</p>
        </div>
        <div type="preface">
          <head>Author's Note</head>
          <p>All the characters in this book are purely imaginary, and if the
          author has used names that may suggest a reference to living persons
          she has done so inadvertently. ...</p>
        </div>
      </front>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en"> 
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-qu">
      <front>
        <div type="abstract">
          <div>
            <head> BACKGROUND:</head>
            <p>Food insecurity can put children at greater risk of obesity because
            of altered food choices and nonuniform consumption patterns.</p>
          </div>
          <div>
            <head> OBJECTIVE:</head>
            <p>We examined the association between obesity and both child-level
            food insecurity and personal food insecurity in US children.</p>
          </div>
          <div>
            <head> DESIGN:</head>
            <p>Data from 9,701 participants in the National Health and Nutrition
            Examination Survey, 2001-2010, aged 2 to 11 years were analyzed.
            Child-level food insecurity was assessed with the US Department of
            Agriculture's Food Security Survey Module based on eight
            child-specific questions. Personal food insecurity was assessed with
            five additional questions. Obesity was defined, using physical
            measurements, as body mass index (calculated as kg/m2) greater than
            or equal to the age- and sex-specific 95th percentile of the Centers
            for Disease Control and Prevention growth charts. Logistic
            regressions adjusted for sex, race/ethnic group, poverty level, and
            survey year were conducted to describe associations between obesity
            and food insecurity.</p>
          </div>
          <div>
            <head> RESULTS:</head>
            <p>Obesity was significantly associated with personal food insecurity
            for children aged 6 to 11 years (odds ratio=1.81; 95% CI 1.33 to
            2.48), but not in children aged 2 to 5 years (odds ratio=0.88; 95%
            CI 0.51 to 1.51). Child-level food insecurity was not associated
            with obesity among 2- to 5-year-olds or 6- to 11-year-olds.</p>
          </div>
          <div>
            <head> CONCLUSIONS:</head>
            <p>Personal food insecurity is associated with an increased risk of
            obesity only in children aged 6 to 11 years. Personal
            food-insecurity measures may give different results than aggregate
            food-insecurity measures in children.</p>
          </div>
        </div>
      </front>
    </egXML>
  </exemplum>
  <remarks ident="front-remarks" versionDate="2015-01-30" xml:lang="en">
    <p>Because cultural conventions differ as to which elements are grouped as
    front matter and which as back matter, the content models for the
    <gi>front</gi> and <gi>back</gi> elements are identical.</p>
  </remarks>
  <remarks ident="front-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Aufgrund von unterschiedlichen kulturellen Konventionen, die Angaben in Vorspann und Nachspann
    betreffend, sind die Inhaltsmodelle für die Elemente <gi>front</gi> und <gi>back</gi>
    identisch.</p>
  </remarks>
  <listRef>
    <ptr target="#DSTITL"/>
    <ptr target="#DS"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">front matter</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">전면부 내용</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">正文前資訊</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">texte préliminaire</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Vorspann (front)</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">paratexto inicial</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">peritesto iniziale</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains any prefatory matter
  (headers, abstracts, title page, prefaces, dedications, etc.) found at the
  start of a document, before the main body.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">주 본문 앞에 나타나는 문서의 시작부에서 발견되는 서문
  자료(헤더, 제목 페이지, 머리말, 헌정사 등)를 포함한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含位於文件最前端、正文之前的項目
  (標頭、題名頁、前言、獻詞等) 。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">本文より前、文書の始めにある序文としてあるもの(標題、タイトル、序文、 献辞など)。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient tout ce qui est au début
  du document, avant le corps du texte : page de titre, dédicaces, préfaces,
  etc.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2017-06-19" xml:lang="de">enthält alle dem Textkörper vorangestellten Texte (Überschriften, Abstracts, Titelseite,
  Vorworte, Widmungen, usw.) zu Beginn eines Dokuments.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene cualquier material
  paratextual (encabezamiento, frontispicio, prefacio, dedicatoria, etc.) que
  aparece delante del inicio del texto.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene qualsiasi materiale
  peritestuale (intestazioni, frontespizio, prefazioni, dediche, etc.) che si
  trovi prima dell'inizio del testo vero e proprio</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declaring"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <!-- 
           we start with allowing a group of mixed-up p-like elements.
           when we are done with them, we can start considering
           div-like elements, and the things that
           can occur after them.
      -->
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.frontPart"/>
        <classRef key="model.pLike"/>
        <classRef key="model.pLike.front"/>
        <classRef key="model.global"/>
      </alternate>
      <sequence minOccurs="0">
        <alternate>
          <!-- 1. has a div1Like, after optional front parts -->
          <sequence>
            <classRef key="model.div1Like"/>
            <alternate minOccurs="0" maxOccurs="unbounded">
              <classRef key="model.div1Like"/>
              <classRef key="model.frontPart"/>
              <classRef key="model.global"/>
            </alternate>
          </sequence>
          <!-- 1. has a divLike, after optional front parts -->
          <sequence>
            <classRef key="model.divLike"/>
            <alternate minOccurs="0" maxOccurs="unbounded">
              <classRef key="model.divLike"/>
              <classRef key="model.frontPart"/>
              <classRef key="model.global"/>
            </alternate>
          </sequence>
        </alternate>
        <!-- and some bottoms, mebbe -->
        <sequence minOccurs="0">
          <classRef key="model.divBottom"/>
          <alternate minOccurs="0" maxOccurs="unbounded">
            <classRef key="model.divBottom"/>
            <classRef key="model.global"/>
          </alternate>
        </sequence>
      </sequence>
    </sequence>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-zr" source="#COEDADD-eg-89">
      <front>
        <epigraph>
          <quote>Nam Sibyllam quidem Cumis ego ipse oculis meis vidi in ampulla
          pendere, et cum illi pueri dicerent: <q xml:lang="grc">Σίβυλλα τί
          θέλεις</q>; respondebat illa: <q xml:lang="grc">ὰποθανεῖν θέλω.</q>
          </quote>
        </epigraph>
        <div type="dedication">
          <p>For Ezra Pound <q xml:lang="it">il miglior fabbro.</q>
          </p>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-ik" source="#fr-ex-Perec-vie">
      <front>
        <div type="dedication">
          <p>à la mémoire de Raymond Queneau</p>
        </div>
        <div type="avertissement">
          <p>L'amitié, l'histoire et la littérature m'ont fourni quelques-uns
          des.personnages de ce livre. Toute autre ressemblance avec des
          individus vivants ou ayant réellement ou fictivement existé ne
          saurait être que coïncidence.</p>
          <epigraph>
            <quote>Regarde de tous tes yeux, regarde <bibl>(Jules Verne, Michel
            Strogoff )</bibl>
            </quote>
          </epigraph>
        </div>
        <div type="preambule">
          <head>PRÉAMBULE</head>
          <epigraph>
            <quote>
              <q>L'œil suit les chemins qui lui ont été ménagés dans l'oeuvre
              <bibl>(Paul Klee, Pädagosisches Skizzenbuch)</bibl>
              </q>
            </quote>
          </epigraph>
          <p> Au départ, l'art du puzzle semble un art bref, un art mince, tout
          entier contenu dans un maigre enseignement de la Gestalttheorie :
          ...</p>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-xb" source="#fr-ex-Hugo-miserables">
      <front>
        <div type="preface">
          <head>Préface</head>
          <p>Tant qu'il existera, par le fait des lois et des moeurs, une
          damnation sociale créant artificiellement, en pleine civilisation,
          des enfers, et compliquant d'une fatalité humaine la destinée qui
          est divine ; tant que les trois problèmes du siècle, la dégradation
          de l'homme par le prolétariat, la déchéance de la femme par la faim,
          l'atrophie de l'enfant par la nuit, ne seront pas résolus; tant que,
          dans certaines régions, l'asphyxie sociale sera possible; en
          d'autres termes, et à un point de vue plus étendu encore, tant qu'il
          aura sur la terre ignorance et misère, des livres de la nature de
          celui-ci pourront ne pas être inutiles.</p>
          <closer>
            <dateline>
              <name type="place">Hauteville-House</name>
              <date>1er janvier 1862</date>
            </dateline>
          </closer>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-bm" source="#biblzh-tw_n56-57">
      <front>
        <epigraph>
          <quote>小燕子其實也無所愛，只是沉浸在朦朧而飄忽的夏夜夢里罷了。 </quote>
        </epigraph>
        <div type="dedication">
          <p>《憶》第三十五首</p>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-eq">
      <front>
        <div type="dedication">
          <p>聲明啟事</p>
        </div>
        <div type="preface">
          <head>作者聲明</head>
          <p>書中所有情節內容皆為虛構，若有雷同，純屬巧合。</p>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-to" source="#hallWell">
      <front>
        <div type="dedication">
          <p>To our three selves</p>
        </div>
        <div type="preface">
          <head>Author's Note</head>
          <p>All the characters in this book are purely imaginary, and if the
          author has used names that may suggest a reference to living persons
          she has done so inadvertently. ...</p>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="en"> 
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-front-egXML-qu">
      <front>
        <div type="abstract">
          <div>
            <head> BACKGROUND:</head>
            <p>Food insecurity can put children at greater risk of obesity because
            of altered food choices and nonuniform consumption patterns.</p>
          </div>
          <div>
            <head> OBJECTIVE:</head>
            <p>We examined the association between obesity and both child-level
            food insecurity and personal food insecurity in US children.</p>
          </div>
          <div>
            <head> DESIGN:</head>
            <p>Data from 9,701 participants in the National Health and Nutrition
            Examination Survey, 2001-2010, aged 2 to 11 years were analyzed.
            Child-level food insecurity was assessed with the US Department of
            Agriculture's Food Security Survey Module based on eight
            child-specific questions. Personal food insecurity was assessed with
            five additional questions. Obesity was defined, using physical
            measurements, as body mass index (calculated as kg/m2) greater than
            or equal to the age- and sex-specific 95th percentile of the Centers
            for Disease Control and Prevention growth charts. Logistic
            regressions adjusted for sex, race/ethnic group, poverty level, and
            survey year were conducted to describe associations between obesity
            and food insecurity.</p>
          </div>
          <div>
            <head> RESULTS:</head>
            <p>Obesity was significantly associated with personal food insecurity
            for children aged 6 to 11 years (odds ratio=1.81; 95% CI 1.33 to
            2.48), but not in children aged 2 to 5 years (odds ratio=0.88; 95%
            CI 0.51 to 1.51). Child-level food insecurity was not associated
            with obesity among 2- to 5-year-olds or 6- to 11-year-olds.</p>
          </div>
          <div>
            <head> CONCLUSIONS:</head>
            <p>Personal food insecurity is associated with an increased risk of
            obesity only in children aged 6 to 11 years. Personal
            food-insecurity measures may give different results than aggregate
            food-insecurity measures in children.</p>
          </div>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="front-remarks" versionDate="2015-01-30" xml:lang="en">
    <p>Because cultural conventions differ as to which elements are grouped as
    front matter and which as back matter, the content models for the
    <gi>front</gi> and <gi>back</gi> elements are identical.</p>
  </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="front-remarks" versionDate="2017-06-19" xml:lang="de">
    <p>Aufgrund von unterschiedlichen kulturellen Konventionen, die Angaben in Vorspann und Nachspann
    betreffend, sind die Inhaltsmodelle für die Elemente <gi>front</gi> und <gi>back</gi>
    identisch.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DSTITL"/>
    <ptr target="#DS"/>
  </listRef>
```

^b27

