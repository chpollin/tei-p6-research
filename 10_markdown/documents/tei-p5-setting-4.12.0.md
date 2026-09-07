---
type: representation
source-type: document
source: '[[00_sources/tei-p5-setting-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 setting
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/setting.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# setting

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3641. Git blob: `d8502f30e4dc054d76409897884fcb4334d10776`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="corpus" xml:id="gi-setting" ident="setting">
  <desc versionDate="2005-01-14" xml:lang="en">describes one particular setting in which a language
  interaction takes place.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">언어 상호작용이 발생하는 특정 무대를 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述語言互動發生的一個特定背景。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">言語交流が行われたひとつの状況設定を示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">précise un contexte particulier dans lequel a lieu
      une interaction linguistique.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe una realización particular en la que una interacción lingüística tiene lugar.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">descrive la particolare ambientazione di una interazione linguistica.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed"/>
  </classes>
  <content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.nameLike.agent"/>
        <classRef key="model.dateLike"/>
        <classRef key="model.settingPart"/>
      </alternate>
    </alternate>
  </content>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-setting-egXML-ln">
      <setting>
        <placeName>New York City, US</placeName>
        <date>1989</date>
        <locale>on a park bench</locale>
        <activity>feeding birds</activity>
      </setting>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-setting-egXML-fy" source="#fr-ex-Rohmer-Maud">
      <setting>
        <name> Clermont-Ferrand</name>
        <date>Mi-décembre</date>
        <locale>Ceyrat</locale>
        <activity>mise en marche de la voiture</activity>
      </setting>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-setting-egXML-ic" source="#biblzh-tw_n26">
      <setting>
        <name>台灣，台北</name>
        <date>1970</date>
        <locale>-新公園的長凳上</locale>
        <activity>躺臥</activity>
      </setting>
    </egXML>
  </exemplum>
  <remarks ident="setting-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>If the <att>who</att> attribute is not supplied, the setting is
    assumed to be that of all participants in the language
    interaction.</p>
  </remarks>
  <remarks ident="setting-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Si l'attribut <att>who</att> n'est pas fourni, le cadre est celui construit par
                l’échange entre les interlocuteurs en présence.</p>
  </remarks>
  <remarks ident="setting-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>who</att>がない場合、当該状況設定は、当該言語交流には、参
    加者全てが関わっているとされる。
    </p>
  </remarks>
  <listRef>
    <ptr target="#CCAHSE"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">describes one particular setting in which a language
  interaction takes place.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">언어 상호작용이 발생하는 특정 무대를 기술한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述語言互動發生的一個特定背景。</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">言語交流が行われたひとつの状況設定を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise un contexte particulier dans lequel a lieu
      une interaction linguistique.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe una realización particular en la que una interacción lingüística tiene lugar.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">descrive la particolare ambientazione di una interazione linguistica.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.ascribed"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
      <alternate minOccurs="0" maxOccurs="unbounded">
        <classRef key="model.nameLike.agent"/>
        <classRef key="model.dateLike"/>
        <classRef key="model.settingPart"/>
      </alternate>
    </alternate>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-setting-egXML-ln">
      <setting>
        <placeName>New York City, US</placeName>
        <date>1989</date>
        <locale>on a park bench</locale>
        <activity>feeding birds</activity>
      </setting>
    </egXML>
  </exemplum>
```

^b10

### Block 11

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-setting-egXML-fy" source="#fr-ex-Rohmer-Maud">
      <setting>
        <name> Clermont-Ferrand</name>
        <date>Mi-décembre</date>
        <locale>Ceyrat</locale>
        <activity>mise en marche de la voiture</activity>
      </setting>
    </egXML>
  </exemplum>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-setting-egXML-ic" source="#biblzh-tw_n26">
      <setting>
        <name>台灣，台北</name>
        <date>1970</date>
        <locale>-新公園的長凳上</locale>
        <activity>躺臥</activity>
      </setting>
    </egXML>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="setting-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>If the <att>who</att> attribute is not supplied, the setting is
    assumed to be that of all participants in the language
    interaction.</p>
  </remarks>
```

^b13

### Block 14

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="setting-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Si l'attribut <att>who</att> n'est pas fourni, le cadre est celui construit par
                l’échange entre les interlocuteurs en présence.</p>
  </remarks>
```

^b14

### Block 15

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="setting-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    属性<att>who</att>がない場合、当該状況設定は、当該言語交流には、参
    加者全てが関わっているとされる。
    </p>
  </remarks>
```

^b15

### Block 16

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHSE"/>
  </listRef>
```

^b16

