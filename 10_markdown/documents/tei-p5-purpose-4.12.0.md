---
type: representation
source-type: document
source: '[[00_sources/tei-p5-purpose-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 purpose
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/purpose.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# purpose

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8896. Git blob: `7ba455c3761b9c98618deeb14597062c5e8b99e1`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="corpus" xml:id="gi-purpose" ident="purpose">
  <desc versionDate="2005-01-14" xml:lang="en">characterizes a single purpose or communicative function of the
text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 단일 목적 또는 의사소통 기능의 특성을 기술한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">描述該文本的一項目的或溝通功能</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該テキストの目的や伝達に関する機能の性質を示す。</desc>
  <desc versionDate="2009-04-16" xml:lang="fr">caractérise une intention ou une fonction de
      communication uniques du texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">caracteriza una única finalidad o función comunicatica del texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">ndica un singolo scopo o funzione comunicativa del testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies a particular kind of purpose.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">특별한 종류의 목적을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明一項特定類型的目的。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">目的の種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise une intention particulière</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica un tipo particular de finalidad</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica un tipo particolare di scopo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="semi">
        <valItem ident="persuade">
          <desc versionDate="2007-06-27" xml:lang="en">didactic, advertising, propaganda, etc.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">설교, 광고, 선전 등</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">教導、廣告、宣傳等</desc>
          <desc versionDate="2008-04-06" xml:lang="es">didáctico, publicidad, propaganda, etc.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">教育、広報、宣伝など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">didactique, publicité, propagande,
etc.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">didattico pubblicitario, propagandistico, ecc.</desc>
        </valItem>
        <valItem ident="express">
          <desc versionDate="2007-06-27" xml:lang="en">self expression, confessional, etc.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">자기 표현, 신앙 고백 등</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">自我表達、自白等</desc>
          <desc versionDate="2008-04-06" xml:lang="es">expresión de uno mismo, confesonario, etc.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">自己表現、独白など。</desc>
          <desc versionDate="2009-04-16" xml:lang="fr">expression personnelle, confessionnel, etc.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">autobiografico, confessionale, ecc.</desc>
        </valItem>
        <valItem ident="inform">
          <desc versionDate="2007-06-27" xml:lang="en">convey information, educate, etc.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">제보, 교육 등</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">傳達訊息、教育等</desc>
          <desc versionDate="2008-04-06" xml:lang="es">informativo, educativo, etc.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">情報伝達、教育など。</desc>
          <desc versionDate="2009-04-16" xml:lang="fr">informatif, éducatif,
etc.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">informativo, educativo, ecc.</desc>
        </valItem>
        <valItem ident="entertain">
          <desc versionDate="2007-06-27" xml:lang="en">amuse, entertain, etc.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">여흥, 오락 등</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">消遣、娛樂等</desc>
          <desc versionDate="2008-04-06" xml:lang="es">divertimento, entretenimiento, etc.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">娯楽、エンターテイメントなど。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">amusement, divertissement, etc.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">di intrattenimento, ricreativo, ecc.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="degree" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the extent to which this purpose predominates.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 목적이 유효한 범위를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明該目的所佔的重要性程度。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該目的が及ぶ範囲を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise à quel degré cette intention
        prédomine.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica el alcance en que predomina este propósito.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il grado in cui lo scopo predomina.</desc>
      <datatype><dataRef key="teidata.certainty"/></datatype>
      <remarks ident="purpose-attr.degree-remarks" versionDate="2013-10-23" xml:lang="en">
        <p>Values should be interpreted as follows.
	<list type="gloss"><label><val>high</val></label><item>this purpose is predominant</item><label><val>medium</val></label><item>this purpose is intermediate</item><label><val>low</val></label><item>this purpose is weak</item><label><val>unknown</val></label><item>extent unknown</item></list>
	           </p>
      </remarks>
      <remarks ident="purpose-attr.degree-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Ces valeurs peuvent être interprêtées ainsi : <list type="gloss"><label><val>high</val></label><item>ce but est prédominant</item><label><val>medium</val></label><item>ce but est intermédiaire</item><label><val>low</val></label><item>ce but est faible</item><label><val>unknown</val></label><item>degré inconnu</item></list>
                    </p>
      </remarks>
      <remarks ident="purpose-attr.degree-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        以下の値をとるべきである。
        <list type="gloss"><label><val>high</val></label><item>主要。</item><label><val>medium</val></label><item>中間。</item><label><val>low</val></label><item>弱い。</item><label><val>unknown</val></label><item>不明。</item></list>
	           </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-purpose-egXML-ho" source="#UND">
      <purpose type="persuade" degree="high"/>
      <purpose type="entertain" degree="low"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-purpose-egXML-pq" source="#UND">
      <purpose type="persuade" degree="high"/>
      <purpose type="entertain" degree="low"/>
    </egXML>
  </exemplum>
  <remarks ident="purpose-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Usually empty, unless some further clarification of the type
attribute is needed, in which case it may contain running prose</p>
  </remarks>
  <remarks ident="purpose-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Habituellement vide, sauf si une clarification complémentaire sur le
                type de l'attribut est nécessaire : dans ce cas il peut contenir du texte non
                structuré. </p>
  </remarks>
  <remarks ident="purpose-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    当該属性typeが示すより詳細な分類が必要でなければ、一般には空白であ
  る。この場合、散文をとることがある。
  </p>
  </remarks>
  <listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">characterizes a single purpose or communicative function of the
text.</desc>
```

^b1

### Block 2

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 단일 목적 또는 의사소통 기능의 특성을 기술한다.</desc>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">描述該文本的一項目的或溝通功能</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストの目的や伝達に関する機能の性質を示す。</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-04-16" xml:lang="fr">caractérise une intention ou une fonction de
      communication uniques du texte.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">caracteriza una única finalidad o función comunicatica del texto.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">ndica un singolo scopo o funzione comunicativa del testo.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
  </classes>
```

^b8

### Block 9

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b9

### Block 10

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies a particular kind of purpose.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">특별한 종류의 목적을 명시한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明一項特定類型的目的。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">目的の種類を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise une intention particulière</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica un tipo particular de finalidad</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica un tipo particolare di scopo.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <valItem ident="persuade">
          <desc versionDate="2007-06-27" xml:lang="en">didactic, advertising, propaganda, etc.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">설교, 광고, 선전 등</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">教導、廣告、宣傳等</desc>
          <desc versionDate="2008-04-06" xml:lang="es">didáctico, publicidad, propaganda, etc.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">教育、広報、宣伝など。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">didactique, publicité, propagande,
etc.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">didattico pubblicitario, propagandistico, ecc.</desc>
        </valItem>
        <valItem ident="express">
          <desc versionDate="2007-06-27" xml:lang="en">self expression, confessional, etc.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">자기 표현, 신앙 고백 등</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">自我表達、自白等</desc>
          <desc versionDate="2008-04-06" xml:lang="es">expresión de uno mismo, confesonario, etc.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">自己表現、独白など。</desc>
          <desc versionDate="2009-04-16" xml:lang="fr">expression personnelle, confessionnel, etc.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">autobiografico, confessionale, ecc.</desc>
        </valItem>
        <valItem ident="inform">
          <desc versionDate="2007-06-27" xml:lang="en">convey information, educate, etc.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">제보, 교육 등</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">傳達訊息、教育等</desc>
          <desc versionDate="2008-04-06" xml:lang="es">informativo, educativo, etc.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">情報伝達、教育など。</desc>
          <desc versionDate="2009-04-16" xml:lang="fr">informatif, éducatif,
etc.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">informativo, educativo, ecc.</desc>
        </valItem>
        <valItem ident="entertain">
          <desc versionDate="2007-06-27" xml:lang="en">amuse, entertain, etc.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">여흥, 오락 등</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">消遣、娛樂等</desc>
          <desc versionDate="2008-04-06" xml:lang="es">divertimento, entretenimiento, etc.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">娯楽、エンターテイメントなど。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">amusement, divertissement, etc.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">di intrattenimento, ricreativo, ecc.</desc>
        </valItem>
      </valList>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the extent to which this purpose predominates.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 목적이 유효한 범위를 명시한다.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明該目的所佔的重要性程度。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該目的が及ぶ範囲を示す。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise à quel degré cette intention
        prédomine.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica el alcance en que predomina este propósito.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il grado in cui lo scopo predomina.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.certainty"/></datatype>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="purpose-attr.degree-remarks" versionDate="2013-10-23" xml:lang="en">
        <p>Values should be interpreted as follows.
	<list type="gloss"><label><val>high</val></label><item>this purpose is predominant</item><label><val>medium</val></label><item>this purpose is intermediate</item><label><val>low</val></label><item>this purpose is weak</item><label><val>unknown</val></label><item>extent unknown</item></list>
	           </p>
      </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="purpose-attr.degree-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Ces valeurs peuvent être interprêtées ainsi : <list type="gloss"><label><val>high</val></label><item>ce but est prédominant</item><label><val>medium</val></label><item>ce but est intermédiaire</item><label><val>low</val></label><item>ce but est faible</item><label><val>unknown</val></label><item>degré inconnu</item></list>
                    </p>
      </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="purpose-attr.degree-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
        以下の値をとるべきである。
        <list type="gloss"><label><val>high</val></label><item>主要。</item><label><val>medium</val></label><item>中間。</item><label><val>low</val></label><item>弱い。</item><label><val>unknown</val></label><item>不明。</item></list>
	           </p>
      </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-purpose-egXML-ho" source="#UND">
      <purpose type="persuade" degree="high"/>
      <purpose type="entertain" degree="low"/>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-purpose-egXML-pq" source="#UND">
      <purpose type="persuade" degree="high"/>
      <purpose type="entertain" degree="low"/>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="purpose-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">Usually empty, unless some further clarification of the type
attribute is needed, in which case it may contain running prose</p>
  </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="purpose-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Habituellement vide, sauf si une clarification complémentaire sur le
                type de l'attribut est nécessaire : dans ce cas il peut contenir du texte non
                structuré. </p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="purpose-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc">
    当該属性typeが示すより詳細な分類が必要でなければ、一般には空白であ
  る。この場合、散文をとることがある。
  </p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CCAHTD"/>
  </listRef>
```

^b35

