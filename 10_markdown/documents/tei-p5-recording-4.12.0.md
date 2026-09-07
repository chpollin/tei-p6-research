---
type: representation
source-type: document
source: '[[00_sources/tei-p5-recording-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 recording
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/recording.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# recording

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12153. Git blob: `c7fdd06fbde89d9ae0f1942877aa6a06ad93f6e6`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="spoken" xml:id="gi-recording" ident="recording">
  <gloss versionDate="2005-01-14" xml:lang="en">recording event</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">enregistrement</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">녹음 사건</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">影音錄製</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Aufnahmevorgang</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">acontecimiento de grabación</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">registrazione</gloss>
  <desc versionDate="2012-12-27" xml:lang="en">provides details of an audio or video recording event
used as the source of a spoken text, either directly or from
a public broadcast.</desc>
  <desc versionDate="2009-04-17" xml:lang="fr">décrit en détail l’événement audio ou vidéo utilisé comme source de la parole transcrite, que ce soit un enregistrement direct ou une émission diffusée.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트 원본으로 사용된 ,직접 또는 공공 방송에서 입수한 오디오 또는 비디오 녹음 사건에 대한 상세 항목.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含口說文本的影像或聲音來源錄製細節，該來源可以是直接錄製或是經由公開播放的管道取得。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">発話テキストの元資料として使われる、直接または放送から事象を録音、録
  画したものの詳細を示す。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">liefert Angaben zur Ton- oder
  Videoaufnahme, die als Quelle eines gesprochenen Textes dient und
  entweder direkt aufgenommen wurde oder von einem öffentlichen Sender
  stammt.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">detalla un acontecimiento de audio o video registrado usado como fuente de un texto hablado, no obtenido directamente ni de una emisión pública.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">fornisce i dettagli di una registrazione audio o video usata come fonte di un testo orale, sia diretta sia da messa in onda pubblica.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.duration"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.recordingPart"/>
        <classRef key="model.pLike"/>
    </alternate>
  </content>
  <constraintSpec ident="recording-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:recording"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">the kind of recording.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">type de l’enregistrement.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">녹음 종류</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">錄製類型</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">録音、録画の種類。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">Art der Aufnahme.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">tipo de grabación</desc>
      <desc versionDate="2007-01-21" xml:lang="it">tipo di registrazione.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>audio</defaultVal>
      <valList type="closed">
        <valItem ident="audio">
          <desc versionDate="2007-06-27" xml:lang="en">audio recording</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">enregistrement audio</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">오디오 녹음</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">聲音錄製</desc>
          <desc versionDate="2008-04-06" xml:lang="es">grabación de audio</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">録音。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">registrazione audio.</desc>
        </valItem>
        <valItem ident="video">
          <desc versionDate="2007-06-27" xml:lang="en">audio and video recording</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">enregistrement audio et vidéo</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">오디오와 비디오 녹화</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">聲音及影像錄製</desc>
          <desc versionDate="2008-04-06" xml:lang="es">grabación de audio y video</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">録音、録画。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">registrazione audio e video.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-ys">
      <recording type="audio" dur="P30M">
        <equipment>
          <p>Recorded on a Sony TR444 walkman by unknown participants; remastered 
	  to digital tape at <placeName>Borehamwood Studios</placeName> by
	  <orgName>Transcription Services Inc</orgName>.</p>
        </equipment>
      </recording>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-sn">
      <recording type="audio" dur="P30M">
        <p><orgName>Harmonia Mundi</orgName> S.A., enregistré à <placeName>Boughton Aluph Saints
              Church</placeName>, <date>septembre 1977</date>.</p>
      </recording>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-fm" source="#fr-ex-Teleph_sonne">
      <recording type="audio" dur="P10M">
        <equipment>
          <p>podcast</p>
        </equipment>
        <broadcast>
          <bibl>
            <title>Questions sur la souffrance et la santé au travail : pénibilité, stress,
              dépression, harcèlement, maladies et accidents...</title>
            <author>France Inter</author>
            <respStmt>
              <resp>Présentateur</resp>
              <name>Alain Bédouet</name>
            </respStmt>
            <respStmt>
              <resp>Personne interrogée</resp>
              <name>Marie Pezé</name>
            </respStmt>
            <series>
              <title>Le Téléphone sonne</title>
            </series>
             <note>Marie Pezé est Docteur en psychologie, psychanalyste, expert judiciaire ; dirige
                la consultation « souffrance et travail » à l’Hôpital de Nanterre (92), auteure de
                  <title>ils ne mourraient pas tous mais tous étaient frappés</title>, Editions
                Pearson.</note>
            <note>Première diffusion le <date when="2008-09-24"> mercredi 24 septembre
            2008</date>
                  </note>
          </bibl>
        </broadcast>
      </recording>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-ut">
      <recording type="audio" dur="P30M">
        <equipment>
          <p>以Sony TR444 walkman錄成，參與者不明；<orgName>中國廣播公司</orgName>在<placeName>中廣電台</placeName>以數位磁帶重製。</p>
        </equipment>
      </recording>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-qq">
      <recording type="audio" dur="P10M">
        <equipment>
          <p>將FM廣播重錄成數位磁帶</p>
        </equipment>
        <broadcast>
          <bibl>
            <title>鬼話連篇</title>
            <author>中國廣播公司</author>
            <respStmt>
              <resp>男主持人</resp>
              <name>司馬中原</name>
            </respStmt>
            <respStmt>
              <resp>女主持人</resp>
              <name>常勤芬</name>
            </respStmt>
            <series>
              <title>鬼吹燈</title>
            </series>
            <note>首播於<date when="1989-11-27">1989年11月27日</date>
                  </note>
          </bibl>
        </broadcast>
      </recording>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-kb">
      <recording type="audio" dur="P10M">
        <equipment>
          <p>Recorded from FM Radio to digital tape</p>
        </equipment>
        <broadcast>
          <bibl>
            <title>Interview on foreign policy</title>
            <author>BBC Radio 5</author>
            <respStmt>
              <resp>interviewer</resp>
              <name>Robin Day</name>
            </respStmt>
            <respStmt>
              <resp>interviewee</resp>
              <name>Margaret Thatcher</name>
            </respStmt>
            <series>
              <title>The World Tonight</title>
            </series>
            <note>First broadcast on
        <date when="1989-11-27">27 Nov 89</date>
                  </note>
          </bibl>
        </broadcast>
      </recording>
    </egXML>
  </exemplum>
  <remarks ident="recording-remarks" versionDate="2007-04-09" xml:lang="en">
    <p>The <att>dur</att> attribute is used to indicate the original
    duration of the recording.</p>
    <!--
    I've put the remark above in to replicate what was here:
     <attDef ident="dur" usage="opt">
      <desc>the original duration of the recording.</desc>
      <desc versionDate="2006-10-28" xml:lang="ja">録音・録画の時間．</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">durée originale de l’enregistrement.</desc>
      <datatype>
        <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0" name="data.duration"/>
      </datatype>
    </attDef>
    I put this comment here partly because I did not want to discard
    the Japanese & French versions. But I have to admit, this description
    seems ambiguous to me: is it the duration of the original recording, or
    the original duration of the recording before ... what?  - - Syd
-->
  </remarks>
  <remarks ident="recording-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>dur</att> est employé pour indiquer la durée originale de
                l'enregistrement.</p>
  </remarks>
  <remarks ident="recording-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>dur</att>は、当該録音、録画の、元の長さを示すために使用さ
    れる。
    </p>
    <!--
    I've put the remark above in to replicate what was here:
     <attDef ident="dur" usage="opt">
      <desc>the original duration of the recording.</desc>
      <desc versionDate="2006-10-28" xml:lang="ja">録音・録画の時間。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">durée originale de l’enregistrement.</desc>
      <datatype>
        <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0" name="data.duration"/>
      </datatype>
    </attDef>
    I put this comment here partly because I did not want to discard
    the Japanese & French versions. But I have to admit, this description
    seems ambiguous to me: is it the duration of the original recording, or
    the original duration of the recording before ... what?  - - Syd
-->
  </remarks>
  <listRef>
    <ptr target="#HD32"/>
    <ptr target="#CCAS2"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">recording event</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">enregistrement</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">녹음 사건</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">影音錄製</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Aufnahmevorgang</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">acontecimiento de grabación</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">registrazione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2012-12-27" xml:lang="en">provides details of an audio or video recording event
used as the source of a spoken text, either directly or from
a public broadcast.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-04-17" xml:lang="fr">décrit en détail l’événement audio ou vidéo utilisé comme source de la parole transcrite, que ce soit un enregistrement direct ou une émission diffusée.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">구어 텍스트 원본으로 사용된 ,직접 또는 공공 방송에서 입수한 오디오 또는 비디오 녹음 사건에 대한 상세 항목.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含口說文本的影像或聲音來源錄製細節，該來源可以是直接錄製或是經由公開播放的管道取得。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">発話テキストの元資料として使われる、直接または放送から事象を録音、録
  画したものの詳細を示す。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">liefert Angaben zur Ton- oder
  Videoaufnahme, die als Quelle eines gesprochenen Textes dient und
  entweder direkt aufgenommen wurde oder von einem öffentlichen Sender
  stammt.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">detalla un acontecimiento de audio o video registrado usado como fuente de un texto hablado, no obtenido directamente ni de una emisión pública.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">fornisce i dettagli di una registrazione audio o video usata come fonte di un testo orale, sia diretta sia da messa in onda pubblica.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="att.duration"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b16

### Block 17

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="0" maxOccurs="unbounded">
      <classRef key="model.recordingPart"/>
        <classRef key="model.pLike"/>
    </alternate>
  </content>
```

^b17

### Block 18

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="recording-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:recording"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">the kind of recording.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">type de l’enregistrement.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">녹음 종류</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">錄製類型</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">録音、録画の種類。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">Art der Aufnahme.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">tipo de grabación</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">tipo di registrazione.</desc>
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
<defaultVal>audio</defaultVal>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="audio">
          <desc versionDate="2007-06-27" xml:lang="en">audio recording</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">enregistrement audio</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">오디오 녹음</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">聲音錄製</desc>
          <desc versionDate="2008-04-06" xml:lang="es">grabación de audio</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">録音。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">registrazione audio.</desc>
        </valItem>
        <valItem ident="video">
          <desc versionDate="2007-06-27" xml:lang="en">audio and video recording</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">enregistrement audio et vidéo</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">오디오와 비디오 녹화</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">聲音及影像錄製</desc>
          <desc versionDate="2008-04-06" xml:lang="es">grabación de audio y video</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">録音、録画。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">registrazione audio e video.</desc>
        </valItem>
      </valList>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-ys">
      <recording type="audio" dur="P30M">
        <equipment>
          <p>Recorded on a Sony TR444 walkman by unknown participants; remastered 
	  to digital tape at <placeName>Borehamwood Studios</placeName> by
	  <orgName>Transcription Services Inc</orgName>.</p>
        </equipment>
      </recording>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-sn">
      <recording type="audio" dur="P30M">
        <p><orgName>Harmonia Mundi</orgName> S.A., enregistré à <placeName>Boughton Aluph Saints
              Church</placeName>, <date>septembre 1977</date>.</p>
      </recording>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-fm" source="#fr-ex-Teleph_sonne">
      <recording type="audio" dur="P10M">
        <equipment>
          <p>podcast</p>
        </equipment>
        <broadcast>
          <bibl>
            <title>Questions sur la souffrance et la santé au travail : pénibilité, stress,
              dépression, harcèlement, maladies et accidents...</title>
            <author>France Inter</author>
            <respStmt>
              <resp>Présentateur</resp>
              <name>Alain Bédouet</name>
            </respStmt>
            <respStmt>
              <resp>Personne interrogée</resp>
              <name>Marie Pezé</name>
            </respStmt>
            <series>
              <title>Le Téléphone sonne</title>
            </series>
             <note>Marie Pezé est Docteur en psychologie, psychanalyste, expert judiciaire ; dirige
                la consultation « souffrance et travail » à l’Hôpital de Nanterre (92), auteure de
                  <title>ils ne mourraient pas tous mais tous étaient frappés</title>, Editions
                Pearson.</note>
            <note>Première diffusion le <date when="2008-09-24"> mercredi 24 septembre
            2008</date>
                  </note>
          </bibl>
        </broadcast>
      </recording>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-ut">
      <recording type="audio" dur="P30M">
        <equipment>
          <p>以Sony TR444 walkman錄成，參與者不明；<orgName>中國廣播公司</orgName>在<placeName>中廣電台</placeName>以數位磁帶重製。</p>
        </equipment>
      </recording>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-qq">
      <recording type="audio" dur="P10M">
        <equipment>
          <p>將FM廣播重錄成數位磁帶</p>
        </equipment>
        <broadcast>
          <bibl>
            <title>鬼話連篇</title>
            <author>中國廣播公司</author>
            <respStmt>
              <resp>男主持人</resp>
              <name>司馬中原</name>
            </respStmt>
            <respStmt>
              <resp>女主持人</resp>
              <name>常勤芬</name>
            </respStmt>
            <series>
              <title>鬼吹燈</title>
            </series>
            <note>首播於<date when="1989-11-27">1989年11月27日</date>
                  </note>
          </bibl>
        </broadcast>
      </recording>
    </egXML>
  </exemplum>
```

^b34

### Block 35

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-recording-egXML-kb">
      <recording type="audio" dur="P10M">
        <equipment>
          <p>Recorded from FM Radio to digital tape</p>
        </equipment>
        <broadcast>
          <bibl>
            <title>Interview on foreign policy</title>
            <author>BBC Radio 5</author>
            <respStmt>
              <resp>interviewer</resp>
              <name>Robin Day</name>
            </respStmt>
            <respStmt>
              <resp>interviewee</resp>
              <name>Margaret Thatcher</name>
            </respStmt>
            <series>
              <title>The World Tonight</title>
            </series>
            <note>First broadcast on
        <date when="1989-11-27">27 Nov 89</date>
                  </note>
          </bibl>
        </broadcast>
      </recording>
    </egXML>
  </exemplum>
```

^b35

### Block 36

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="recording-remarks" versionDate="2007-04-09" xml:lang="en">
    <p>The <att>dur</att> attribute is used to indicate the original
    duration of the recording.</p>
    <!--
    I've put the remark above in to replicate what was here:
     <attDef ident="dur" usage="opt">
      <desc>the original duration of the recording.</desc>
      <desc versionDate="2006-10-28" xml:lang="ja">録音・録画の時間．</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">durée originale de l’enregistrement.</desc>
      <datatype>
        <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0" name="data.duration"/>
      </datatype>
    </attDef>
    I put this comment here partly because I did not want to discard
    the Japanese & French versions. But I have to admit, this description
    seems ambiguous to me: is it the duration of the original recording, or
    the original duration of the recording before ... what?  - - Syd
-->
  </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="recording-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut <att>dur</att> est employé pour indiquer la durée originale de
                l'enregistrement.</p>
  </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="recording-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>dur</att>は、当該録音、録画の、元の長さを示すために使用さ
    れる。
    </p>
    <!--
    I've put the remark above in to replicate what was here:
     <attDef ident="dur" usage="opt">
      <desc>the original duration of the recording.</desc>
      <desc versionDate="2006-10-28" xml:lang="ja">録音・録画の時間。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">durée originale de l’enregistrement.</desc>
      <datatype>
        <rng:ref xmlns:rng="http://relaxng.org/ns/structure/1.0" name="data.duration"/>
      </datatype>
    </attDef>
    I put this comment here partly because I did not want to discard
    the Japanese & French versions. But I have to admit, this description
    seems ambiguous to me: is it the duration of the original recording, or
    the original duration of the recording before ... what?  - - Syd
-->
  </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD32"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b39

