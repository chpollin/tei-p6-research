---
type: representation
source-type: document
source: '[[00_sources/tei-p5-additional-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 additional
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/additional.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# additional

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 4992. Git blob: `14fb06d10406def56560aa8c1356f0eabb69b886`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="msdescription" xml:id="ADDITIONAL" ident="additional">
  <gloss versionDate="2007-06-12" xml:lang="en">additional</gloss>
  <gloss versionDate="2022-04-18" xml:lang="ja">当該手書き資料等に関する書誌情報などの付随情報をまとめる。または当該資料の複製に関するキュレーション情報や管理情報をまとめる。</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">informations complémentaires</gloss>
  <desc versionDate="2019-01-17" xml:lang="en" xml:id="additional.desc">groups additional information, combining
    bibliographic information about a manuscript or other object, or surrogate copies of
it, with curatorial or administrative information.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고의 사본에 관한 서지 정보와 관리 정보를 결합한 부가적 정보를 모아 놓는다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">匯集附加資訊，結合手稿的書目資訊、或是手稿的代替副本，包含管理或行政資訊。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料に関する書誌情報などの付随情報まとめる。または当該資料 の複製に関する管理情報をまとめる。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">regroupe les informations complémentaires sur le manuscrit, incluant une bibliographie, des indications sur ses reproductions, ou des informations sur sa conservation et sur sa gestion.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">agrupa información adicional, combinando informaciones bibliográficas relativas al manuscrito o a copias adicionales del mismo con informaciones de carácter conservacional o administrativo.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">raggruppa ulteriori informazioni combinando informazioni bibliografiche relative al manoscritto o a copie surrogate dello stesso con informazioni di carattere curatoriale o amministrativo.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate>
      <sequence>
	<elementRef key="adminInfo" minOccurs="0"/>
	<elementRef key="surrogates" minOccurs="0"/>
	<elementRef key="listBibl" minOccurs="0"/>
      </sequence>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONAL-egXML-fd" source="#UND">
      <additional>
        <adminInfo>
          <recordHist>
            <p>
              <!-- record history here -->
            </p>
          </recordHist>
          <custodialHist>
            <p>
              <!-- custodial history here -->
            </p>
          </custodialHist>
        </adminInfo>
        <surrogates>
          <p>
            <!-- information about surrogates here -->
          </p>
        </surrogates>
        <listBibl>
          <bibl>
            <!-- ... -->
          </bibl>
          <!-- full bibliography here -->
        </listBibl>
      </additional>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONAL-egXML-dm" source="#UND">
      <additional>
        <adminInfo>
          <recordHist>
            <p>
              <!-- ... -->
            </p>
          </recordHist>
          <custodialHist>
            <p>
              <!-- ... -->
            </p>
          </custodialHist>
        </adminInfo>
        <surrogates>
          <p>
            <!-- ... -->
          </p>
        </surrogates>
        <listBibl>
          <bibl>
            <!-- ... -->
          </bibl>
        </listBibl>
      </additional>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONAL-egXML-qs" source="#UND">
      <additional>
        <adminInfo>
          <recordHist>
            <p>
              <!-- 檔案歷史紀錄 -->
            </p>
          </recordHist>
          <custodialHist>
            <p>
              <!-- 保管歷史紀錄 -->
            </p>
          </custodialHist>
        </adminInfo>
        <surrogates>
          <p>
            <!-- 代用品資訊 -->
          </p>
        </surrogates>
        <listBibl>
          <bibl>
            <!-- ... -->
          </bibl>
          <!-- 完整參考書目 -->
        </listBibl>
      </additional>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#msad"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="en">additional</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2022-04-18" xml:lang="ja">当該手書き資料等に関する書誌情報などの付随情報をまとめる。または当該資料の複製に関するキュレーション情報や管理情報をまとめる。</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">informations complémentaires</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2019-01-17" xml:lang="en" xml:id="additional.desc">groups additional information, combining
    bibliographic information about a manuscript or other object, or surrogate copies of
it, with curatorial or administrative information.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 원고의 사본에 관한 서지 정보와 관리 정보를 결합한 부가적 정보를 모아 놓는다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">匯集附加資訊，結合手稿的書目資訊、或是手稿的代替副本，包含管理或行政資訊。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該手書き資料に関する書誌情報などの付随情報まとめる。または当該資料 の複製に関する管理情報をまとめる。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">regroupe les informations complémentaires sur le manuscrit, incluant une bibliographie, des indications sur ses reproductions, ou des informations sur sa conservation et sur sa gestion.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">agrupa información adicional, combinando informaciones bibliográficas relativas al manuscrito o a copias adicionales del mismo con informaciones de carácter conservacional o administrativo.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">raggruppa ulteriori informazioni combinando informazioni bibliografiche relative al manoscritto o a copie surrogate dello stesso con informazioni di carattere curatoriale o amministrativo.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <sequence>
	<elementRef key="adminInfo" minOccurs="0"/>
	<elementRef key="surrogates" minOccurs="0"/>
	<elementRef key="listBibl" minOccurs="0"/>
      </sequence>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONAL-egXML-fd" source="#UND">
      <additional>
        <adminInfo>
          <recordHist>
            <p>
              <!-- record history here -->
            </p>
          </recordHist>
          <custodialHist>
            <p>
              <!-- custodial history here -->
            </p>
          </custodialHist>
        </adminInfo>
        <surrogates>
          <p>
            <!-- information about surrogates here -->
          </p>
        </surrogates>
        <listBibl>
          <bibl>
            <!-- ... -->
          </bibl>
          <!-- full bibliography here -->
        </listBibl>
      </additional>
    </egXML>
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONAL-egXML-dm" source="#UND">
      <additional>
        <adminInfo>
          <recordHist>
            <p>
              <!-- ... -->
            </p>
          </recordHist>
          <custodialHist>
            <p>
              <!-- ... -->
            </p>
          </custodialHist>
        </adminInfo>
        <surrogates>
          <p>
            <!-- ... -->
          </p>
        </surrogates>
        <listBibl>
          <bibl>
            <!-- ... -->
          </bibl>
        </listBibl>
      </additional>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ADDITIONAL-egXML-qs" source="#UND">
      <additional>
        <adminInfo>
          <recordHist>
            <p>
              <!-- 檔案歷史紀錄 -->
            </p>
          </recordHist>
          <custodialHist>
            <p>
              <!-- 保管歷史紀錄 -->
            </p>
          </custodialHist>
        </adminInfo>
        <surrogates>
          <p>
            <!-- 代用品資訊 -->
          </p>
        </surrogates>
        <listBibl>
          <bibl>
            <!-- ... -->
          </bibl>
          <!-- 完整參考書目 -->
        </listBibl>
      </additional>
    </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#msad"/>
  </listRef>
```

^b16

