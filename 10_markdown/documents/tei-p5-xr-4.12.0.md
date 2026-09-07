---
type: representation
source-type: document
source: '[[00_sources/tei-p5-xr-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 xr
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/xr.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# xr

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12712. Git blob: `fa66297da95f9398ebc17c4174bde1e67484d966`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="dictionaries" xml:id="gi-xr" ident="xr">
  <gloss versionDate="2005-01-14" xml:lang="en">cross-reference phrase</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">교차 참조 구</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">交互參照</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">renvoi</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">sintagma de referencia cruzada</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">frase di riferimento incrociato</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a phrase, sentence, or icon referring the reader to some other location in this or
    another text.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">현재 또는 다른 텍스트에서 다른 위치를 지시하는 구, 문장, 또는 아이콘을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一字詞、句子、或圖象，用以參照到相同文本或不同文本中的其他位置。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">利用者に、他の場所を表す句、文、図形を示す。</desc>
  <desc versionDate="2009-05-27" xml:lang="fr">contient une expression, une phrase ou une icône qui
    invite le lecteur à se référer à un autre endroit, dans le même texte ou dans un autre texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene un sintagma, oración o icono referido al lector
    hacia alguna otro punto de este u otro texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un sintagma, una frase o un'icona che rimanda il
    lettore ad un altra porzione di questo o altro testo.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
  <content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <classRef key="model.inter"/>
        <elementRef key="usg"/>
        <elementRef key="lbl"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
  <attList>
    <attDef ident="type" mode="change" usage="rec">
      <desc versionDate="2005-01-14" xml:lang="en">indicates the type of cross reference, using any convenient typology.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">다양한 유형으로 교차 참조 유형을 나타낸다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類方法指出交互參照的種類。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">相互参照の種類を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">indique le type de renvoi, en utilisant n'importe
        quelle typologie adaptée.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el tipo de referencia cruzada aplicando una
        tipología funcional.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il tipo di riferimento incrociato secondo una
        tipologia funzionale</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="syn">
          <gloss versionDate="2007-07-04" xml:lang="en">synonym</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">유의어</gloss>
          <gloss versionDate="2009-05-27" xml:lang="fr">synonyme</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sinonimo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">referencia cruzada a información sinónima</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">cross reference for synonym information</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">유의어 정보에 대한 교차 참조</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類方法指出交互參照的種類。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">referencia cruzada para la información de un
            sinónimo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">同義情報向けの相互参照。</desc>
          <desc versionDate="2009-05-27" xml:lang="fr">renvoi à des informations concernant un synonyme</desc>
          <desc versionDate="2007-01-21" xml:lang="it">riferimento incrociato per informazione sui
            sinomimi</desc>
        </valItem>
        <valItem ident="etym">
          <gloss versionDate="2007-07-04" xml:lang="en">etymological</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">어원적</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">étymologique</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">etimologico</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">información etimológica</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">etymological information</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">어원 정보</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">詞源資訊</desc>
          <desc versionDate="2008-04-06" xml:lang="es">información etimológica</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">語源情報。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">informations étymologiques</desc>
          <desc versionDate="2007-01-21" xml:lang="it">informazione etimologica.</desc>
        </valItem>
        <valItem ident="cf">
          <gloss versionDate="2007-07-04" xml:lang="en">compare or consult</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">비교 또는 참고</gloss>
          <gloss versionDate="2009-05-27" xml:lang="fr">comparer ou consulter</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">confronta o consulta</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">término relativo o similar</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">related or similar term</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">관련된 또는 유사한 용어</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">相關或相似的字詞</desc>
          <desc versionDate="2008-04-06" xml:lang="es">término relacionado o similar</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">関連語または似た言葉。</desc>
          <desc versionDate="2009-05-27" xml:lang="fr">terme connexe ou semblable</desc>
          <desc versionDate="2007-01-21" xml:lang="it">termine collegato o simile.</desc>
        </valItem>
        <valItem ident="illus">
          <gloss versionDate="2007-07-04" xml:lang="en">illustration</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">그림</gloss>
          <gloss versionDate="2009-05-27" xml:lang="fr">illustration</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">illustrazione</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">ilustración de un objeto</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">illustration of an object</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">물체의 그림</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">物體圖像</desc>
          <desc versionDate="2008-04-06" xml:lang="es">ilustración de un objeto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">対象の絵。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">illustration d'un objet</desc>
          <desc versionDate="2007-01-21" xml:lang="it">illustrazione di un oggetto.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-uc">
      <entry>
        <form>
          <orth>lavage</orth>
        </form>
        <etym>[Fr. &lt; <mentioned>laver</mentioned>; L. <mentioned>lavare</mentioned>, to wash;
            <xr>see <ref>lather</ref>
               </xr>]. </etym>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-lu" source="#fr-ex-TLFI">
      <entry>
        <form><orth>publier</orth> ... </form>
        <etym>Emprunté au <lang>latin</lang>
               <mentioned>publicare</mentioned>
               <def>mettre à la disposition du public ; montrer au public ; publier (un livre)</def> ,
              <label>dérivé de </label>
               <mentioned>publicus</mentioned>, <xr>v.
            <ref>public1</ref>
               </xr>. La forme <mentioned>puplier</mentioned>, <mentioned>poplier</mentioned>
               <label>attesté en </label>
               <lang>anc. fr.</lang>
               <xr> (v. <ref>supra, <bibl>Grand
                  dictionnaire de la langue française</bibl>. et.
              <bibl>Tobler-Lommatzsch</bibl>
                  </ref>.)</xr> à côté de<mentioned> publier</mentioned>,
            que l'on trouve à partir de la <date>2e moitié du XIIIe s.</date>
               <bibl>[ms. de la <date>fin XIIIe s.</date>] </bibl>
               <bibl>(Légende de Girart de
              Roussillon, 64 dans Tobler-Lommatzsch),</bibl> est une <label>altération
              d'après</label>
               <mentioned> peuple</mentioned>.</etym>
      </entry>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-wv">
      <entry>
        <form>
          <orth>clef</orth>
        </form>
        <xr type="syn">SYN. <ref>clé</ref>
            </xr>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-rm">
      <entry>
        <form>
          <orth>癲</orth>
        </form>
        <etym>詩經．大雅．雲漢：<mentioned>瘨</mentioned>，病、使困苦； <xr>參見 <ref>癲</ref>
               </xr>。 </etym>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-qs">
      <entry>
        <form>
          <orth>lawful</orth>
        </form>
        <xr type="syn">同義詞：請見 <ref>legal</ref>
            </xr>
      </entry>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-wb">
      <entry>
        <form>
          <orth>lawful</orth>
        </form>
        <xr type="syn">SYN. see <ref>legal</ref>
            </xr>
      </entry>
    </egXML>
  </exemplum>
  <remarks ident="xr-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data and phrase-level elements; usually contains a
        <gi>ref</gi> or a <gi>ptr</gi> element.</p>
    <p>This element encloses both the actual indication of the location referred to, which may be
      tagged using the <gi>ref</gi> or <gi>ptr</gi> elements, and any accompanying material which
      gives more information about why the reader is being referred there.</p>
  </remarks>
  <remarks ident="xr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères et des éléments de niveau expression ;
      habituellement un élément <gi>ref</gi> ou un élément<gi>ptr</gi>.</p>
    <p>Cet élément contient à la fois l'indication réelle de l'emplacement mentionné, qui peut être
      balisée par les éléments <gi>ref</gi> ou<gi>ptr</gi>, et tous types d'indications
      complémentaires explicitant la raison pour laquelle le lecteur est renvoyé à cet endroit. </p>
  </remarks>
  <remarks ident="xr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 文字列や句レベルの要素をとるかもしれない。一般には、要素 <gi>ref</gi>または<gi>ptr</gi>を含む。 </p>
    <p> 当該要素は、要素<gi>ref</gi>や<gi>ptr</gi>で表される参照場所と、利 用者が参照する理由に関する詳細な情報を示す関連資料を含むことになる。 </p>
  </remarks>
  <listRef>
    <ptr target="#DITPXR"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">cross-reference phrase</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">교차 참조 구</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">交互參照</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">renvoi</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">sintagma de referencia cruzada</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">frase di riferimento incrociato</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a phrase, sentence, or icon referring the reader to some other location in this or
    another text.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">현재 또는 다른 텍스트에서 다른 위치를 지시하는 구, 문장, 또는 아이콘을 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一字詞、句子、或圖象，用以參照到相同文本或不同文本中的其他位置。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">利用者に、他の場所を表す句、文、図形を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-05-27" xml:lang="fr">contient une expression, une phrase ou une icône qui
    invite le lecteur à se référer à un autre endroit, dans le même texte ou dans un autre texte.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene un sintagma, oración o icono referido al lector
    hacia alguna otro punto de este u otro texto.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un sintagma, una frase o un'icona che rimanda il
    lettore ad un altra porzione di questo o altro testo.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.lexicographic"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.entryPart"/>
    <memberOf key="model.entryPart.top"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    
      <alternate minOccurs="0" maxOccurs="unbounded">
        <textNode/>
        <classRef key="model.gLike"/>
        <classRef key="model.phrase"/>
        <classRef key="model.inter"/>
        <elementRef key="usg"/>
        <elementRef key="lbl"/>
        <classRef key="model.global"/>
      </alternate>
    
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the type of cross reference, using any convenient typology.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다양한 유형으로 교차 참조 유형을 나타낸다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類方法指出交互參照的種類。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">相互参照の種類を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">indique le type de renvoi, en utilisant n'importe
        quelle typologie adaptée.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el tipo de referencia cruzada aplicando una
        tipología funcional.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il tipo di riferimento incrociato secondo una
        tipologia funzionale</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="syn">
          <gloss versionDate="2007-07-04" xml:lang="en">synonym</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">유의어</gloss>
          <gloss versionDate="2009-05-27" xml:lang="fr">synonyme</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">sinonimo</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">referencia cruzada a información sinónima</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">cross reference for synonym information</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">유의어 정보에 대한 교차 참조</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">用合適的分類方法指出交互參照的種類。</desc>
          <desc versionDate="2008-04-06" xml:lang="es">referencia cruzada para la información de un
            sinónimo</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">同義情報向けの相互参照。</desc>
          <desc versionDate="2009-05-27" xml:lang="fr">renvoi à des informations concernant un synonyme</desc>
          <desc versionDate="2007-01-21" xml:lang="it">riferimento incrociato per informazione sui
            sinomimi</desc>
        </valItem>
        <valItem ident="etym">
          <gloss versionDate="2007-07-04" xml:lang="en">etymological</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">어원적</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">étymologique</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">etimologico</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">información etimológica</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">etymological information</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">어원 정보</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">詞源資訊</desc>
          <desc versionDate="2008-04-06" xml:lang="es">información etimológica</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">語源情報。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">informations étymologiques</desc>
          <desc versionDate="2007-01-21" xml:lang="it">informazione etimologica.</desc>
        </valItem>
        <valItem ident="cf">
          <gloss versionDate="2007-07-04" xml:lang="en">compare or consult</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">비교 또는 참고</gloss>
          <gloss versionDate="2009-05-27" xml:lang="fr">comparer ou consulter</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">confronta o consulta</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">término relativo o similar</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">related or similar term</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">관련된 또는 유사한 용어</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">相關或相似的字詞</desc>
          <desc versionDate="2008-04-06" xml:lang="es">término relacionado o similar</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">関連語または似た言葉。</desc>
          <desc versionDate="2009-05-27" xml:lang="fr">terme connexe ou semblable</desc>
          <desc versionDate="2007-01-21" xml:lang="it">termine collegato o simile.</desc>
        </valItem>
        <valItem ident="illus">
          <gloss versionDate="2007-07-04" xml:lang="en">illustration</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko">그림</gloss>
          <gloss versionDate="2009-05-27" xml:lang="fr">illustration</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">illustrazione</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">ilustración de un objeto</gloss>
          <desc versionDate="2007-06-27" xml:lang="en">illustration of an object</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">물체의 그림</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">物體圖像</desc>
          <desc versionDate="2008-04-06" xml:lang="es">ilustración de un objeto</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">対象の絵。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">illustration d'un objet</desc>
          <desc versionDate="2007-01-21" xml:lang="it">illustrazione di un oggetto.</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-uc">
      <entry>
        <form>
          <orth>lavage</orth>
        </form>
        <etym>[Fr. &lt; <mentioned>laver</mentioned>; L. <mentioned>lavare</mentioned>, to wash;
            <xr>see <ref>lather</ref>
               </xr>]. </etym>
      </entry>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-lu" source="#fr-ex-TLFI">
      <entry>
        <form><orth>publier</orth> ... </form>
        <etym>Emprunté au <lang>latin</lang>
               <mentioned>publicare</mentioned>
               <def>mettre à la disposition du public ; montrer au public ; publier (un livre)</def> ,
              <label>dérivé de </label>
               <mentioned>publicus</mentioned>, <xr>v.
            <ref>public1</ref>
               </xr>. La forme <mentioned>puplier</mentioned>, <mentioned>poplier</mentioned>
               <label>attesté en </label>
               <lang>anc. fr.</lang>
               <xr> (v. <ref>supra, <bibl>Grand
                  dictionnaire de la langue française</bibl>. et.
              <bibl>Tobler-Lommatzsch</bibl>
                  </ref>.)</xr> à côté de<mentioned> publier</mentioned>,
            que l'on trouve à partir de la <date>2e moitié du XIIIe s.</date>
               <bibl>[ms. de la <date>fin XIIIe s.</date>] </bibl>
               <bibl>(Légende de Girart de
              Roussillon, 64 dans Tobler-Lommatzsch),</bibl> est une <label>altération
              d'après</label>
               <mentioned> peuple</mentioned>.</etym>
      </entry>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-wv">
      <entry>
        <form>
          <orth>clef</orth>
        </form>
        <xr type="syn">SYN. <ref>clé</ref>
            </xr>
      </entry>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-rm">
      <entry>
        <form>
          <orth>癲</orth>
        </form>
        <etym>詩經．大雅．雲漢：<mentioned>瘨</mentioned>，病、使困苦； <xr>參見 <ref>癲</ref>
               </xr>。 </etym>
      </entry>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-qs">
      <entry>
        <form>
          <orth>lawful</orth>
        </form>
        <xr type="syn">同義詞：請見 <ref>legal</ref>
            </xr>
      </entry>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-xr-egXML-wb">
      <entry>
        <form>
          <orth>lawful</orth>
        </form>
        <xr type="syn">SYN. see <ref>legal</ref>
            </xr>
      </entry>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="xr-remarks" versionDate="2005-01-14" xml:lang="en">
    <p rend="dataDesc">May contain character data and phrase-level elements; usually contains a
        <gi>ref</gi> or a <gi>ptr</gi> element.</p>
    <p>This element encloses both the actual indication of the location referred to, which may be
      tagged using the <gi>ref</gi> or <gi>ptr</gi> elements, and any accompanying material which
      gives more information about why the reader is being referred there.</p>
  </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="xr-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Peut contenir des caractères et des éléments de niveau expression ;
      habituellement un élément <gi>ref</gi> ou un élément<gi>ptr</gi>.</p>
    <p>Cet élément contient à la fois l'indication réelle de l'emplacement mentionné, qui peut être
      balisée par les éléments <gi>ref</gi> ou<gi>ptr</gi>, et tous types d'indications
      complémentaires explicitant la raison pour laquelle le lecteur est renvoyé à cet endroit. </p>
  </remarks>
```

^b32

### Block 33

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="xr-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 文字列や句レベルの要素をとるかもしれない。一般には、要素 <gi>ref</gi>または<gi>ptr</gi>を含む。 </p>
    <p> 当該要素は、要素<gi>ref</gi>や<gi>ptr</gi>で表される参照場所と、利 用者が参照する理由に関する詳細な情報を示す関連資料を含むことになる。 </p>
  </remarks>
```

^b33

### Block 34

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#DITPXR"/>
  </listRef>
```

^b34

