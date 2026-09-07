---
type: representation
source-type: document
source: '[[00_sources/tei-p5-correction-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 correction
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/correction.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# correction

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12623. Git blob: `5da26b678f80e380af29e5c8b0f53dc1a27fe307`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-correction" ident="correction">
  <gloss versionDate="2005-01-14" xml:lang="en">correction principles</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">règles de correction</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">수정 원리</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">更正原則</gloss>
  <gloss versionDate="2006-10-18" xml:lang="de">Korrekturverfahren</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">principios de corrección</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">principi di correzione</gloss>
  <gloss versionDate="2024-02-28" xml:lang="ja">修正の原則</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">states how and under what circumstances corrections have been made in the text.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">établit comment et dans quelles circonstances des
    corrections ont été apportées au texte.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 수정의 상황과 방법에 대해 설명한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">說明文本中的更正是在什麼情況下、如何產生的。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">テキスト中に施された修正の状況や方法を示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">gibt an, wie und unter welchen Bedingungen Korrekturen an
    dem Text vorgenommen wurden.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">describe cómo y en qué casos se han hecho correcciones en
    el texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">dichiara quante correzioni sono state apportate al testo
    e in quali circostanze.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>    
  </content>
  <constraintSpec ident="correction-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:correction"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="status" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates the degree of correction applied to the text.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique le degré de correction apporté au texte.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">텍스트에 적용된 수정의 정도를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出文本更正的程度。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該テキストに施された修正の実行状況を示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">gibt Auskunft über das Ausmaß von Korrekturen, die an
        dem Text vorgenommen wurden.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el grado de corrección aplicado al texto</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il gradi di corrzione apportata al testo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="closed">
        <valItem ident="high">
          <desc versionDate="2007-06-27" xml:lang="en">the text has been thoroughly checked and proofread.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte a été entièrement vérifié et corrigé.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 철저하게 검사되고 교정되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本以被徹底檢查校對過。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto se ha revisado y se ha corregido
            minuciosamente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、十分に検査・校正されている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è stato controllato accuratamente.</desc>
        </valItem>
        <valItem ident="medium">
          <desc versionDate="2007-06-27" xml:lang="en">the text has been checked at least once.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte a au moins été vérifié une fois.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 적어도 한번 검사되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本被檢查過至少一次。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto se ha revisado por lo menos una vez.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、少なくとも一度は検査されている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è stato controllato almeno una
          volta.</desc>
        </valItem>
        <valItem ident="low">
          <desc versionDate="2007-06-27" xml:lang="en">the text has not been checked.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte n’a pas été vérifié.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 검사되지 않았다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本從未被檢查過。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto no se ha revisado.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、検査されていない。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo non è stato controllato.</desc>
        </valItem>
        <valItem ident="unknown">
          <desc versionDate="2007-06-27" xml:lang="en">the correction status of the text is unknown.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le niveau de correction du texte est inconnu.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 교정 상태를 알 수 없다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">更正狀態不明</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el estatus de la corrección del texto es
            desconocido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストに施された修正の精度は、不明である。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">lo stadio di correzione non è noto.</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="method" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates the method adopted to indicate corrections within the text.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique la méthode adoptée pour signaler les
        corrections dans le texte.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 수정사항을 표시하기 위해 채택한 방법을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">說明標示更正所採取的方法。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該テキストに施された修正の方法を示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">Bezeichnet die Methode, die angewandt wurde um
        Korrekturen im Text zu kennzeichnen.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el método seguido para indicar las
        correcciones al interno del texto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il metodo adottato per indicare le correzioni
        all'interno di un testo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>silent</defaultVal>
      <valList type="closed">
        <valItem ident="silent">
          <desc versionDate="2007-06-27" xml:lang="en">corrections have been made silently</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">les corrections ont été faites sans être
            marquées.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수정사항이 표시되지 않았다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">直接在文本中更正</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las correcciones se han hecho silenciosamente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">修正の跡は残されていない。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le correzioni sono state apportate
            silenziosamente</desc>
        </valItem>
        <valItem ident="markup">
          <desc versionDate="2007-07-05" xml:lang="en">corrections have been represented using markup</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수정사항이 마크업을 사용해 표사되었다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las correcciones se han representado mediante el
            marcado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">修正箇所は、タグで示されている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les corrections ont été notées par un codage</desc>
          <desc versionDate="2007-11-06" xml:lang="it">sono state rappresentate delle correzioni tramite
            annotazione</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correction-egXML-ee">
      <correction>
        <p>Errors in transcription controlled by using the WordPerfect spelling checker, with a user
          defined dictionary of 500 extra words taken from Chambers Twentieth Century
        Dictionary.</p>
      </correction>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correction-egXML-fq">
      <correction>
        <p>Les erreurs de transcriptions ont été détectées et corrigées à l'aide du correcteur
            Cordial 2006 - Synapse</p>
      </correction>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correction-egXML-op">
      <correction>
        <p>抄寫錯誤由WordPerfect拼寫檢查系統控制，該系統使用Chambers Twentieth Century Dictionary裡內含之使用者自訂的500個詞條。</p>
      </correction>
    </egXML>
  </exemplum>
  <remarks ident="correction-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>May be used to note the results of proof reading the text against its original, indicating
      (for example) whether discrepancies have been silently rectified, or recorded using the
      editorial tags described in section <ptr target="#COED"/>.</p>
  </remarks>
  <remarks ident="correction-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Utilisé pour noter le résultat de la comparaison du texte et de l'original en indiquant par
      exemple si les différences ont été faites sans être marquées, ou si elles ont été marquées en
      utilisant les balises éditoriales décrites dans la section <ptr target="#COED"/>.</p>
  </remarks>
  <remarks ident="correction-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Puede ser utilizado para observar los resultados de la corrección de las lecturas del texto
      en contraposición con su original, indicando (por ejemplo) si las discrepancias se han
      rectificado silenciosamente, o se han registrado usando las etiquetas editoriales descritas en
      la sección <ptr target="#COED"/>.</p>
  </remarks>
  <remarks ident="correction-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 元資料を元に行われた校正結果を示すために使われるかもしれない。例え ば、相違点は密かに修正されているのか、または<ptr target="#COED"/>
      にある編集用のタグを使用して記録されているのか、など。 </p>
  </remarks>
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
<gloss versionDate="2005-01-14" xml:lang="en">correction principles</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">règles de correction</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">수정 원리</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">更正原則</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2006-10-18" xml:lang="de">Korrekturverfahren</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">principios de corrección</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/gloss[7]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">principi di correzione</gloss>
```

^b7

### Block 8

XML location: `/elementSpec[1]/gloss[8]`.

```xml
<gloss versionDate="2024-02-28" xml:lang="ja">修正の原則</gloss>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">states how and under what circumstances corrections have been made in the text.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">établit comment et dans quelles circonstances des
    corrections ont été apportées au texte.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 수정의 상황과 방법에 대해 설명한다.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明文本中的更正是在什麼情況下、如何產生的。</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">テキスト中に施された修正の状況や方法を示す。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt an, wie und unter welchen Bedingungen Korrekturen an
    dem Text vorgenommen wurden.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">describe cómo y en qué casos se han hecho correcciones en
    el texto.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">dichiara quante correzioni sono state apportate al testo
    e in quali circostanze.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
```

^b17

### Block 18

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>    
  </content>
```

^b18

### Block 19

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="correction-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:correction"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the degree of correction applied to the text.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique le degré de correction apporté au texte.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트에 적용된 수정의 정도를 표시한다.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出文本更正的程度。</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストに施された修正の実行状況を示す。</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt Auskunft über das Ausmaß von Korrekturen, die an
        dem Text vorgenommen wurden.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el grado de corrección aplicado al texto</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il gradi di corrzione apportata al testo.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="high">
          <desc versionDate="2007-06-27" xml:lang="en">the text has been thoroughly checked and proofread.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte a été entièrement vérifié et corrigé.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 철저하게 검사되고 교정되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本以被徹底檢查校對過。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto se ha revisado y se ha corregido
            minuciosamente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、十分に検査・校正されている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è stato controllato accuratamente.</desc>
        </valItem>
        <valItem ident="medium">
          <desc versionDate="2007-06-27" xml:lang="en">the text has been checked at least once.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte a au moins été vérifié une fois.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 적어도 한번 검사되었다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本被檢查過至少一次。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto se ha revisado por lo menos una vez.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、少なくとも一度は検査されている。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo è stato controllato almeno una
          volta.</desc>
        </valItem>
        <valItem ident="low">
          <desc versionDate="2007-06-27" xml:lang="en">the text has not been checked.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le texte n’a pas été vérifié.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트가 검사되지 않았다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">該文本從未被檢查過。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el texto no se ha revisado.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは、検査されていない。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">il testo non è stato controllato.</desc>
        </valItem>
        <valItem ident="unknown">
          <desc versionDate="2007-06-27" xml:lang="en">the correction status of the text is unknown.</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">le niveau de correction du texte est inconnu.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 교정 상태를 알 수 없다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">更正狀態不明</desc>
          <desc versionDate="2008-04-06" xml:lang="es">el estatus de la corrección del texto es
            desconocido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストに施された修正の精度は、不明である。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">lo stadio di correzione non è noto.</desc>
        </valItem>
      </valList>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the method adopted to indicate corrections within the text.</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique la méthode adoptée pour signaler les
        corrections dans le texte.</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 수정사항을 표시하기 위해 채택한 방법을 나타낸다.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明標示更正所採取的方法。</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストに施された修正の方法を示す。</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">Bezeichnet die Methode, die angewandt wurde um
        Korrekturen im Text zu kennzeichnen.</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el método seguido para indicar las
        correcciones al interno del texto.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il metodo adottato per indicare le correzioni
        all'interno di un testo.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>silent</defaultVal>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="silent">
          <desc versionDate="2007-06-27" xml:lang="en">corrections have been made silently</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">les corrections ont été faites sans être
            marquées.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수정사항이 표시되지 않았다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">直接在文本中更正</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las correcciones se han hecho silenciosamente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">修正の跡は残されていない。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">le correzioni sono state apportate
            silenziosamente</desc>
        </valItem>
        <valItem ident="markup">
          <desc versionDate="2007-07-05" xml:lang="en">corrections have been represented using markup</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">수정사항이 마크업을 사용해 표사되었다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">las correcciones se han representado mediante el
            marcado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">修正箇所は、タグで示されている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">les corrections ont été notées par un codage</desc>
          <desc versionDate="2007-11-06" xml:lang="it">sono state rappresentate delle correzioni tramite
            annotazione</desc>
        </valItem>
      </valList>
```

^b40

### Block 41

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correction-egXML-ee">
      <correction>
        <p>Errors in transcription controlled by using the WordPerfect spelling checker, with a user
          defined dictionary of 500 extra words taken from Chambers Twentieth Century
        Dictionary.</p>
      </correction>
    </egXML>
  </exemplum>
```

^b41

### Block 42

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correction-egXML-fq">
      <correction>
        <p>Les erreurs de transcriptions ont été détectées et corrigées à l'aide du correcteur
            Cordial 2006 - Synapse</p>
      </correction>
    </egXML>
  </exemplum>
```

^b42

### Block 43

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-correction-egXML-op">
      <correction>
        <p>抄寫錯誤由WordPerfect拼寫檢查系統控制，該系統使用Chambers Twentieth Century Dictionary裡內含之使用者自訂的500個詞條。</p>
      </correction>
    </egXML>
  </exemplum>
```

^b43

### Block 44

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="correction-remarks" versionDate="2005-01-14" xml:lang="en">
    <p>May be used to note the results of proof reading the text against its original, indicating
      (for example) whether discrepancies have been silently rectified, or recorded using the
      editorial tags described in section <ptr target="#COED"/>.</p>
  </remarks>
```

^b44

### Block 45

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="correction-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Utilisé pour noter le résultat de la comparaison du texte et de l'original en indiquant par
      exemple si les différences ont été faites sans être marquées, ou si elles ont été marquées en
      utilisant les balises éditoriales décrites dans la section <ptr target="#COED"/>.</p>
  </remarks>
```

^b45

### Block 46

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="correction-remarks" versionDate="2008-04-06" xml:lang="es">
    <p>Puede ser utilizado para observar los resultados de la corrección de las lecturas del texto
      en contraposición con su original, indicando (por ejemplo) si las discrepancias se han
      rectificado silenciosamente, o se han registrado usando las etiquetas editoriales descritas en
      la sección <ptr target="#COED"/>.</p>
  </remarks>
```

^b46

### Block 47

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="correction-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p> 元資料を元に行われた校正結果を示すために使われるかもしれない。例え ば、相違点は密かに修正されているのか、または<ptr target="#COED"/>
      にある編集用のタグを使用して記録されているのか、など。 </p>
  </remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b48

