---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.transcriptional-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.transcriptional
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.transcriptional.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.transcriptional

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 18158. Git blob: `a72ccee706d4b016a972c9690da162e1ebea97c2`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:rng="http://relaxng.org/ns/structure/1.0" module="tei" type="atts" ident="att.transcriptional">
  <desc versionDate="2007-09-03" xml:lang="en">provides attributes specific to elements encoding authorial or
  scribal intervention in a text when
  transcribing manuscript or similar sources.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">원고 또는 유사 원본을 전사할 때 텍스트의 저작 또는 필사 간섭을 부호화하는 요소에 특징적으로 사용되는 속성을 제시한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">proporciona a los atributos específicos a los elementos que codifican la intervención authorial o scribal en un texto al transcribir el manuscrito o las fuentes similares.</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">手書き資料や同様の資料を転記する場合、著者や筆写者に関する調整を記録
  する要素に付与される属性を示す。</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">fournit des attributs spécifiques au codage d'éléments
relatifs à l'intervention de l'auteur ou du copiste dans un texte lors de la
transcription de sources manuscrites ou assimilées.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">assegna degli attributi propri degli elementi che descrivono il carattere di un intervento dell'autore o del trascrittore di un testo nella redazione di un manoscritto o di altra fonte simile.</desc>
  <classes>
    <memberOf key="att.editLike"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.written"/>
  </classes>
  <attList>
    <attDef ident="status" usage="opt">
      <desc versionDate="2007-09-03" xml:lang="en">indicates the effect of the intervention, for example in
      the case of a deletion, strikeouts
      which include too much or too little text, or in the case of an
      addition, an insertion which duplicates some of the text
      already present.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">간섭의 효과를 나타낸다. 예를 들어, 삭제의 경우 너무 많은 또는 너무 적은 텍스트를 포함한 지우기, 또는 추가의 경우, 이미 존재하는 텍스트 일부의 중복 삽입 등.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">indica el resultado de una intervención, por ejemplo en el caso de una cancelación, una tachadura que incluyen demasiado o demasiado poco texto, o en el caso de una adición o una inserción que duplica información ya presente en el texto.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該調整の影響を示す。例えば、削除の際、取消線の範囲が多すぎた
      り少なすぎたりする場合や、追加の際、既にあるテキストの部分をコピー
      して挿入したりする場合。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">indique la conséquence de l'intervention, par
exemple dans le cas d'un effacement, une biffure, qui inclut trop ou pas assez de
texte, ou dans le cas d'un ajout, une insertion, qui reproduit une portion du
texte déjà présent.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">indica l'effetto dell'intervento, per esempio in caso di cancellazione, quando questa comprenda troppo testo o troppo poco, o in caso di aggiunta, quando questa riproduce parte del testo già presente.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>unremarkable</defaultVal>
      <!--      <valDesc>any description of flaws in the marking of a deletion, e.g.
      <val>excess left</val>, <val>excess right</val>, <val>short left</val>, <val>short
      right</val>.</valDesc> -->
      <valList type="open">
        <valItem ident="duplicate">
          <desc versionDate="2007-09-03" xml:lang="en">all of the text indicated as an addition duplicates
	  some text that is in the original, whether the duplication
	  is word-for-word or less exact.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">중복이 단어 대 단어로 된 것이지, 아니면 중복이 비교적 덜 정확하게 된 것인지 간에, 삽입으로 표시된 모든 텍스트는 원본의 일부 텍스트를 중복한 것임.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">todo el texto indicado como adición duplica un fragmento de texto presente en el original, siendo la duplicación palabra por palabra o algo menos exacta.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは全て、元資料にあるテキストのコピーを追加するも
      のである。その程度は、語単位であったりそれより小さいこともある。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">tout le texte indiqué comme étant une addition reprend le texte de l'original, que la duplication soit identique mot pour mot ou moins exacte.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">l'intero testo identificato come aggiunta riproduce parte del testo già presente nell'originale, indipendentemente dal fatto che la riproduzione sia esatta (parola per parola) o meno.</desc>
        </valItem>
        <valItem ident="duplicate-partial">
          <desc versionDate="2007-09-03" xml:lang="en">part of the text indicated as an addition duplicates
	  some text that is in the original</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">일부 텍스트가 원본의 일부 텍스트를 중복</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la parte del texto marcado como adición duplica un fragmento de texto presente en el original</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストの部分は、元資料にあるテキストのコピーを追加する
      ものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la partie du texte indiquée comme
étant un ajout est redondante avec un texte présent dans l'original.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo identificato come aggiunta riproduce parte del testo già presente nell'originale.</desc>
        </valItem>
        <valItem ident="excessStart">
          <desc versionDate="2007-09-03" xml:lang="en">some text at the beginning of the deletion is marked
          as deleted even though it clearly should not be
          deleted.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있지 않았어야 하는데도, 삭제부의 시작에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto del principio de una cancelación se marca como suprimido aunque este no lo haya sido claramente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分の始点は、例えそれが明白な削除ではなくとも、マー
      クされている。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte situé au début de la supression est indiqué comme supprimé bien qu'à l'évidence il ne devrait pas l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo all'inizio della cancellazione è identificata come cancellata anche se chiaramente non dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="excessEnd">
          <desc versionDate="2007-09-03" xml:lang="en">some text at the end of the deletion is marked as
          deleted even though it clearly should not be
          deleted.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있지 않았어야 하는데도, 삭제부의 끝에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto del final de una cancelación se marca como suprimido aunque este no lo haya sido claramente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分の終点は、例えそれが明白な削除ではなくとも、マー
      クされている。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte situé à la fin de la supression est indiqué comme supprimé bien qu'à l'évidence il ne devrait pas l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo alla fine della cancellazione è identificata come cancellata anche se chiaramente non dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="shortStart">
          <desc versionDate="2007-09-03" xml:lang="en">some text at the beginning of the deletion is not
          marked as deleted even though it clearly should be.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있어야 하는데도, 삭제부의 시작에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있지 않다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto del inicio de la cancelación no se marca como suprimido aunque claramente haya sido suprimido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分の始点は、例えそれが明白な削除ではなくとも、マー
      クされていない。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte situé au début de la supression n'est pas indiqué comme supprimé bien qu'à l'évidence il devrait l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo all'inizio della cancellazione non è identificata come cancellata anche se chiaramente dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="shortEnd">
          <desc versionDate="2007-09-03" xml:lang="en">some text at the end of the deletion is not marked as
          deleted even though it clearly should be.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있어야 하는데도, 삭제부의 끝에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있지 않다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto del final de la cancelación no se marca como suprimido aunque claramente haya sido suprimido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分の終点は、例えそれが明白な削除ではなくとも、マー
      クされていない。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte situé à la fin de la supression n'est pas indiqué comme supprimé bien qu'à l'évidence il devrait l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo alla fine della cancellazione non è identificata come cancellata anche se chiaramente dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="partial">
          <desc versionDate="2007-09-03" xml:lang="en">some text in the deletion is not marked as deleted
	  even though it clearly should be.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있어야 하는데도, 삭제부에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있지 않다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto de la cancelación no se marca como suprimido aunque claramente haya sido suprimido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分は、例えそれが明白な削除ではなくとも、マークされ
      ていない。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte dans la supression n'est pas indiqué comme disparu bien qu'à l'évidence il devrait l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo all'interno della cancellazione non è identificata come cancellata anche se chiaramente dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="unremarkable">
          <desc versionDate="2007-09-03" xml:lang="en">the deletion is not faulty.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">삭제가 잘못된 것이 아니다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la cancelación no es defectuosa.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分は、間違いではない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">l'indication de suppression n'est pas
erronée.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la cancellazione non è erronea.</desc>
        </valItem>
      </valList>
      <remarks ident="att.transcriptional-attr.status-remarks" versionDate="2007-09-03" xml:lang="en">
        <p>Status information on each deletion is needed rather rarely
	except in critical editions from authorial manuscripts; status
	information on additions is even less common.</p>
        <p>Marking a deletion or addition as faulty is inescapably an
        interpretive act; the usual test applied in practice is the
	linguistic acceptability of the text with and without the
        letters or words in question.</p>
      </remarks>
      <remarks ident="att.transcriptional-attr.status-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Il est rarement nécessaire de donner de l'information sur le statut de chaque
                        suppression sauf dans le cas des éditions critiques de manuscrits d'auteur,
                        l'information sur le statut des additions étant encore plus rare.</p>
        <p>L'indication d'une suppression ou d'une addition comme erronée est indéniablement un acte
                        d'interprétation ; le test habituel appliqué dans la pratique est
                        l'acceptabilité linguistique du texte avec et sans les lettres ou mots en
                        question. </p>
      </remarks>
      <remarks ident="att.transcriptional-attr.status-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>La información del estado de cada cancelación se necesita raramente, excepto en las ediciones críticas de los manuscritos de autor; la información del estado sobre las adiciones es incluso menos común.</p>
        <p>El marcaje de una cancelación o una adición como defectuoso es ineludible en un acto interpretativo; el test generalmente aplicado en la práctica es la aceptabilidad lingüística del texto con y sin las letras o las palabras en cuestión.</p>
      </remarks>
      <remarks ident="att.transcriptional-attr.status-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	各削除部分に関する状態情報は、著者の自筆原稿からの校勘版を除い
      て、滅多に必要にはならない。追加に関する状態情報も、一般的ではな
      い。
      </p>
        <p>
	削除部分や追加を間違いとして記録することは、必然的に解釈が含ま
      れてしまう。実際には、問題となる文字や単語の有無によって、当該テ
      キストが言語学的に問題ないかどうかで判断される。
      </p>
      </remarks>
    </attDef>
    <attDef ident="cause">
      <desc versionDate="2011-10-31" xml:lang="en">documents the presumed cause for the intervention.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <!--<valList type="semi">
        <valItem ident="fix">
          <desc versionDate="2011-10-31" xml:lang="en">repeated for the purpose of fixation</desc>
        </valItem>
        <valItem ident="unclear">
          <desc versionDate="2011-10-31" xml:lang="en">repeated to clarify a previously illegible or badly written text
   or mark</desc>
        </valItem>
      </valList>-->
    </attDef>
    <!-- MDH 2014-06-22: Removing usage="mwa" per http://sourceforge.net/p/tei/bugs/299/ and 
                  http://sourceforge.net/p/tei/bugs/676/ . If no problems apparent in future, remove. -->
    <attDef ident="seq">
      <gloss versionDate="2007-09-03" xml:lang="en">sequence</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">연쇄</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">secuencia</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">séquence</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">sequenza</gloss>
      <desc versionDate="2007-09-03" xml:lang="en">assigns a sequence number related to the order in which
      the encoded features carrying this attribute are believed to have occurred.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 속성을 포함하는 부호화된 자질이 발생했다고 가정되는 순서와 관련된 번호를 할당한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">asigna un número de serie relacionado con el orden en el cual se cree que se han sucedido las características codificadas que llevan este atributo.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該属性が示す素性が出現すると想定されている順番の、番号を示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">assigne un numéro séquentiel relatif à l'ordre
dans lequel les traits encodés portant cet attribut sont supposés être apparus.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">stabilisce un numero sequenziale relativo all'ordine in cui si ritiene che ricorrano i tratti codificati ai quali è assegnato tale attributo.</desc>
      <datatype maxOccurs="1"><dataRef key="teidata.count"/></datatype>
    </attDef>
  </attList>
  <listRef>

    <ptr target="#PHAD"/>

  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-03" xml:lang="en">provides attributes specific to elements encoding authorial or
  scribal intervention in a text when
  transcribing manuscript or similar sources.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">원고 또는 유사 원본을 전사할 때 텍스트의 저작 또는 필사 간섭을 부호화하는 요소에 특징적으로 사용되는 속성을 제시한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona a los atributos específicos a los elementos que codifican la intervención authorial o scribal en un texto al transcribir el manuscrito o las fuentes similares.</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">手書き資料や同様の資料を転記する場合、著者や筆写者に関する調整を記録
  する要素に付与される属性を示す。</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">fournit des attributs spécifiques au codage d'éléments
relatifs à l'intervention de l'auteur ou du copiste dans un texte lors de la
transcription de sources manuscrites ou assimilées.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">assegna degli attributi propri degli elementi che descrivono il carattere di un intervento dell'autore o del trascrittore di un testo nella redazione di un manoscritto o di altra fonte simile.</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.editLike"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.written"/>
  </classes>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-09-03" xml:lang="en">indicates the effect of the intervention, for example in
      the case of a deletion, strikeouts
      which include too much or too little text, or in the case of an
      addition, an insertion which duplicates some of the text
      already present.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">간섭의 효과를 나타낸다. 예를 들어, 삭제의 경우 너무 많은 또는 너무 적은 텍스트를 포함한 지우기, 또는 추가의 경우, 이미 존재하는 텍스트 일부의 중복 삽입 등.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">indica el resultado de una intervención, por ejemplo en el caso de una cancelación, una tachadura que incluyen demasiado o demasiado poco texto, o en el caso de una adición o una inserción que duplica información ya presente en el texto.</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該調整の影響を示す。例えば、削除の際、取消線の範囲が多すぎた
      り少なすぎたりする場合や、追加の際、既にあるテキストの部分をコピー
      して挿入したりする場合。</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">indique la conséquence de l'intervention, par
exemple dans le cas d'un effacement, une biffure, qui inclut trop ou pas assez de
texte, ou dans le cas d'un ajout, une insertion, qui reproduit une portion du
texte déjà présent.</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica l'effetto dell'intervento, per esempio in caso di cancellazione, quando questa comprenda troppo testo o troppo poco, o in caso di aggiunta, quando questa riproduce parte del testo già presente.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>unremarkable</defaultVal>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="duplicate">
          <desc versionDate="2007-09-03" xml:lang="en">all of the text indicated as an addition duplicates
	  some text that is in the original, whether the duplication
	  is word-for-word or less exact.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">중복이 단어 대 단어로 된 것이지, 아니면 중복이 비교적 덜 정확하게 된 것인지 간에, 삽입으로 표시된 모든 텍스트는 원본의 일부 텍스트를 중복한 것임.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">todo el texto indicado como adición duplica un fragmento de texto presente en el original, siendo la duplicación palabra por palabra o algo menos exacta.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストは全て、元資料にあるテキストのコピーを追加するも
      のである。その程度は、語単位であったりそれより小さいこともある。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">tout le texte indiqué comme étant une addition reprend le texte de l'original, que la duplication soit identique mot pour mot ou moins exacte.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">l'intero testo identificato come aggiunta riproduce parte del testo già presente nell'originale, indipendentemente dal fatto che la riproduzione sia esatta (parola per parola) o meno.</desc>
        </valItem>
        <valItem ident="duplicate-partial">
          <desc versionDate="2007-09-03" xml:lang="en">part of the text indicated as an addition duplicates
	  some text that is in the original</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">일부 텍스트가 원본의 일부 텍스트를 중복</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la parte del texto marcado como adición duplica un fragmento de texto presente en el original</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該テキストの部分は、元資料にあるテキストのコピーを追加する
      ものである。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la partie du texte indiquée comme
étant un ajout est redondante avec un texte présent dans l'original.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo identificato come aggiunta riproduce parte del testo già presente nell'originale.</desc>
        </valItem>
        <valItem ident="excessStart">
          <desc versionDate="2007-09-03" xml:lang="en">some text at the beginning of the deletion is marked
          as deleted even though it clearly should not be
          deleted.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있지 않았어야 하는데도, 삭제부의 시작에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto del principio de una cancelación se marca como suprimido aunque este no lo haya sido claramente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分の始点は、例えそれが明白な削除ではなくとも、マー
      クされている。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte situé au début de la supression est indiqué comme supprimé bien qu'à l'évidence il ne devrait pas l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo all'inizio della cancellazione è identificata come cancellata anche se chiaramente non dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="excessEnd">
          <desc versionDate="2007-09-03" xml:lang="en">some text at the end of the deletion is marked as
          deleted even though it clearly should not be
          deleted.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있지 않았어야 하는데도, 삭제부의 끝에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto del final de una cancelación se marca como suprimido aunque este no lo haya sido claramente.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分の終点は、例えそれが明白な削除ではなくとも、マー
      クされている。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte situé à la fin de la supression est indiqué comme supprimé bien qu'à l'évidence il ne devrait pas l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo alla fine della cancellazione è identificata come cancellata anche se chiaramente non dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="shortStart">
          <desc versionDate="2007-09-03" xml:lang="en">some text at the beginning of the deletion is not
          marked as deleted even though it clearly should be.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있어야 하는데도, 삭제부의 시작에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있지 않다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto del inicio de la cancelación no se marca como suprimido aunque claramente haya sido suprimido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分の始点は、例えそれが明白な削除ではなくとも、マー
      クされていない。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte situé au début de la supression n'est pas indiqué comme supprimé bien qu'à l'évidence il devrait l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo all'inizio della cancellazione non è identificata come cancellata anche se chiaramente dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="shortEnd">
          <desc versionDate="2007-09-03" xml:lang="en">some text at the end of the deletion is not marked as
          deleted even though it clearly should be.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있어야 하는데도, 삭제부의 끝에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있지 않다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto del final de la cancelación no se marca como suprimido aunque claramente haya sido suprimido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分の終点は、例えそれが明白な削除ではなくとも、マー
      クされていない。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte situé à la fin de la supression n'est pas indiqué comme supprimé bien qu'à l'évidence il devrait l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo alla fine della cancellazione non è identificata come cancellata anche se chiaramente dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="partial">
          <desc versionDate="2007-09-03" xml:lang="en">some text in the deletion is not marked as deleted
	  even though it clearly should be.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">분명히 그렇게 되어 있어야 하는데도, 삭제부에 있는 어떤 텍스트가 삭제된 것으로 표지되어 있지 않다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">un fragmento de texto de la cancelación no se marca como suprimido aunque claramente haya sido suprimido.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分は、例えそれが明白な削除ではなくとも、マークされ
      ていない。</desc>
          <desc versionDate="2009-05-28" xml:lang="fr">un passage du texte dans la supression n'est pas indiqué comme disparu bien qu'à l'évidence il devrait l'être.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">una parte del testo all'interno della cancellazione non è identificata come cancellata anche se chiaramente dovrebbe esserlo.</desc>
        </valItem>
        <valItem ident="unremarkable">
          <desc versionDate="2007-09-03" xml:lang="en">the deletion is not faulty.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">삭제가 잘못된 것이 아니다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la cancelación no es defectuosa.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該削除部分は、間違いではない。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">l'indication de suppression n'est pas
erronée.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la cancellazione non è erronea.</desc>
        </valItem>
      </valList>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="att.transcriptional-attr.status-remarks" versionDate="2007-09-03" xml:lang="en">
        <p>Status information on each deletion is needed rather rarely
	except in critical editions from authorial manuscripts; status
	information on additions is even less common.</p>
        <p>Marking a deletion or addition as faulty is inescapably an
        interpretive act; the usual test applied in practice is the
	linguistic acceptability of the text with and without the
        letters or words in question.</p>
      </remarks>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="att.transcriptional-attr.status-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Il est rarement nécessaire de donner de l'information sur le statut de chaque
                        suppression sauf dans le cas des éditions critiques de manuscrits d'auteur,
                        l'information sur le statut des additions étant encore plus rare.</p>
        <p>L'indication d'une suppression ou d'une addition comme erronée est indéniablement un acte
                        d'interprétation ; le test habituel appliqué dans la pratique est
                        l'acceptabilité linguistique du texte avec et sans les lettres ou mots en
                        question. </p>
      </remarks>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="att.transcriptional-attr.status-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>La información del estado de cada cancelación se necesita raramente, excepto en las ediciones críticas de los manuscritos de autor; la información del estado sobre las adiciones es incluso menos común.</p>
        <p>El marcaje de una cancelación o una adición como defectuoso es ineludible en un acto interpretativo; el test generalmente aplicado en la práctica es la aceptabilidad lingüística del texto con y sin las letras o las palabras en cuestión.</p>
      </remarks>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="att.transcriptional-attr.status-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
	各削除部分に関する状態情報は、著者の自筆原稿からの校勘版を除い
      て、滅多に必要にはならない。追加に関する状態情報も、一般的ではな
      い。
      </p>
        <p>
	削除部分や追加を間違いとして記録することは、必然的に解釈が含ま
      れてしまう。実際には、問題となる文字や単語の有無によって、当該テ
      キストが言語学的に問題ないかどうかで判断される。
      </p>
      </remarks>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2011-10-31" xml:lang="en">documents the presumed cause for the intervention.</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[1]`.

```xml
<gloss versionDate="2007-09-03" xml:lang="en">sequence</gloss>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">연쇄</gloss>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">secuencia</gloss>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">séquence</gloss>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[3]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">sequenza</gloss>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2007-09-03" xml:lang="en">assigns a sequence number related to the order in which
      the encoded features carrying this attribute are believed to have occurred.</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 속성을 포함하는 부호화된 자질이 발생했다고 가정되는 순서와 관련된 번호를 할당한다.</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">asigna un número de serie relacionado con el orden en el cual se cree que se han sucedido las características codificadas que llevan este atributo.</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該属性が示す素性が出現すると想定されている順番の、番号を示す。</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">assigne un numéro séquentiel relatif à l'ordre
dans lequel les traits encodés portant cet attribut sont supposés être apparus.</desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">stabilisce un numero sequenziale relativo all'ordine in cui si ritiene che ricorrano i tratti codificati ai quali è assegnato tale attributo.</desc>
```

^b33

### Block 34

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype maxOccurs="1"><dataRef key="teidata.count"/></datatype>
```

^b34

### Block 35

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>

    <ptr target="#PHAD"/>

  </listRef>
```

^b35

