---
type: representation
source-type: document
source: '[[00_sources/tei-p5-normalization-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 normalization
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/normalization.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# normalization

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9811. Git blob: `841ddee522e0a4529bbbdb75c79ff1018fdd31ee`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="header" xml:id="gi-normalization" ident="normalization">
  <gloss versionDate="2009-01-05" xml:lang="en">normalization</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">normalisation</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates the extent of normalization or regularization of the original source carried out in converting it to electronic form.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">indique l'extension de la normalisation ou de la régularisation effectuée sur le texte source dans sa conversion vers sa forme électronique.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전자 형식으로 변환할 때 수행된 원본 텍스트의 표준화 또는 규칙화의 정도를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出來源文件轉換成電子文本時規格化或標準化的程度。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">元資料が電子形式に変換される際に施される正規化の程度を示す。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">gibt an, in welchem Ausmaß das Original bei der
    Umwandlung in elektronische Form normalisiert und vereinheitlicht wurde.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica el grado de normalización o de regularización
    aplicado a la fuente original en el proceso de conversión a formato electrónico.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica il grado di normalizzazione o regolarizzazione
    della fonte effettuato nella conversione a documento elettronico.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
  <content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
  <constraintSpec ident="normalization-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:normalization"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <!--
<attDef ident="source" usage="opt">
      <desc versionDate="2013-12-21" xml:lang="en">indicates a bibliographic description or other resource documenting the principles
        underlying the normalization carried out.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique l’autorité pour toute normalisation
        effectuée.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">수행된 표준화를 행한 기준 을 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出任何規格化所實行的依據。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">正規化を施した責任者を示す．</desc>
      <desc versionDate="2006-10-18" xml:lang="de">nennt die für die Normalisierung verantwortliche
        Instanz</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica la autoridad de cualquier normalización
        llevada a cabo.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'autorità per ogni normalizzazione eseguita.</desc>
      <datatype><dataRef key="teidata.pointer"/></datatype>
    </attDef>
-->

    <attDef ident="method" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates the method adopted to indicate normalizations within the text.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique la méthode adoptée pour signaler les
        normalisations dans le texte.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">텍스트의 표준화를 표시하기 위해 채택한 방법론을 제시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出標示規格化所採取的方法。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該テキストに施された正規化の方法を示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de"> bezeichnet die Methode, die angewandt wurde um
        Normalisierungen im Text kenntlich zu machen.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el método adoptado para indicar
        normalizaciones al interno del texto.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica il metodo adottato per indicare le
        normalizzazioni all'interno di un testo.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>silent</defaultVal>
      <valList type="closed">
        <valItem ident="silent">
          <desc versionDate="2007-06-27" xml:lang="en">normalization made silently</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">normalisation effectuée sans être mentionnée.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표준화가 드러나게 표시되지 않았다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">直接在文本中實行規格化</desc>
          <desc versionDate="2008-04-06" xml:lang="es">normalización hecha silenciosamente</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">正規化は、何も記さずに施された。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la normalizzazione è stata apportata
            silenziosamente</desc>
        </valItem>
        <valItem ident="markup">
          <desc versionDate="2007-10-16" xml:lang="en">normalization represented using markup</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표준화가 마크업을 사용하여 표시되었다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">normalización representada mediante el marcado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">正規化は、マークアップで示されている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la normalisation a été décrite en employant un
            codage</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la normalizzazione è stata rappresentata mediante
            marcatori editoriali</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-normalization-egXML-vt">
      <editorialDecl>
        <normalization method="markup">
          <p>Where both upper- and lower-case i, j, u, v, and vv have been normalized, to modern
            20th century typographical practice, the <gi>choice</gi> element has been used to
            enclose <gi>orig</gi> and <gi>reg</gi> elements giving the original and new values
            respectively. ... </p>
        </normalization>
        <normalization method="silent">
          <p>Spacing between words and following punctuation has been regularized to zero spaces;
            spacing between words has been regularized to one space.</p>
        </normalization>
        <normalization source="http://www.dict.sztaki.hu/webster">
          <p>Spelling converted throughout to Modern American usage, based on Websters 9th
            Collegiate dictionary.</p>
        </normalization>
      </editorialDecl>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-normalization-egXML-vq" source="#fr-ex-Acad">
      <editorialDecl>
        <normalization method="markup">
          <p>Là où les majuscules et les minuscules i, j, u, v et vv ont été normalisées selon la
              pratique typographique moderne, l'élément<gi> choice</gi> a été employé en association
              avec <gi>orig</gi> et <gi>reg</gi>pour fournir à la fois les formes originales et les
              formes nouvelles , respectivement ... </p>
        </normalization>
        <normalization method="silent">
          <p> L'espace entre chaque mot a été régularisé à un espace. Un signe de ponctuation
              simple est suivi d'un espace, un signe de ponctuation double est précédé et suivi d'un
              espace.</p>
        </normalization>
        <normalization source="http://www.academie-francaise.fr/langue/orthographe/plan.html">
          <p>Normalisation effectuée selon le Rapport Du Conseil Supérieur De La Langue Française
              publié dans les documents administratifs du Journal officiel du 6 décembre 1990</p>
        </normalization>
      </editorialDecl>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-normalization-egXML-xt">
      <editorialDecl>
        <normalization method="markup">
          <p>當大寫與小寫的 i, j, u, v, 以及vv已經標準化，符合二十世紀現代印刷術，<gi>choice</gi>元素就用來包含 <gi>orig</gi> 還有
              <gi>reg</gi> 兩個元素，並賦予新的意義。… </p>
        </normalization>
        <normalization method="silent">
          <p>字與字後的標點符號之間規定沒有空格；字與字間規定留一個空格。</p>
        </normalization>
        <normalization source="http://www.dict.sztaki.hu/webster">
          <p>拼字源於Websters 9th Collegiate字典的現代美語用法</p>
        </normalization>
      </editorialDecl>
    </egXML>
  </exemplum>
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
<gloss versionDate="2009-01-05" xml:lang="en">normalization</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">normalisation</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the extent of normalization or regularization of the original source carried out in converting it to electronic form.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique l'extension de la normalisation ou de la régularisation effectuée sur le texte source dans sa conversion vers sa forme électronique.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전자 형식으로 변환할 때 수행된 원본 텍스트의 표준화 또는 규칙화의 정도를 표시한다.</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出來源文件轉換成電子文本時規格化或標準化的程度。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">元資料が電子形式に変換される際に施される正規化の程度を示す。</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt an, in welchem Ausmaß das Original bei der
    Umwandlung in elektronische Form normalisiert und vereinheitlicht wurde.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el grado de normalización o de regularización
    aplicado a la fuente original en el proceso de conversión a formato electrónico.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il grado di normalizzazione o regolarizzazione
    della fonte effettuato nella conversione a documento elettronico.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.editorialDeclPart"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <classRef key="model.pLike" minOccurs="1" maxOccurs="unbounded"/>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="normalization-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:normalization"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the method adopted to indicate normalizations within the text.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique la méthode adoptée pour signaler les
        normalisations dans le texte.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트의 표준화를 표시하기 위해 채택한 방법론을 제시한다.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出標示規格化所採取的方法。</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該テキストに施された正規化の方法を示す。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de"> bezeichnet die Methode, die angewandt wurde um
        Normalisierungen im Text kenntlich zu machen.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el método adoptado para indicar
        normalizaciones al interno del texto.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica il metodo adottato per indicare le
        normalizzazioni all'interno di un testo.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>silent</defaultVal>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="silent">
          <desc versionDate="2007-06-27" xml:lang="en">normalization made silently</desc>
          <desc versionDate="2009-01-05" xml:lang="fr">normalisation effectuée sans être mentionnée.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표준화가 드러나게 표시되지 않았다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">直接在文本中實行規格化</desc>
          <desc versionDate="2008-04-06" xml:lang="es">normalización hecha silenciosamente</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">正規化は、何も記さずに施された。</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la normalizzazione è stata apportata
            silenziosamente</desc>
        </valItem>
        <valItem ident="markup">
          <desc versionDate="2007-10-16" xml:lang="en">normalization represented using markup</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표준화가 마크업을 사용하여 표시되었다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">normalización representada mediante el marcado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">正規化は、マークアップで示されている。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">la normalisation a été décrite en employant un
            codage</desc>
          <desc versionDate="2007-01-21" xml:lang="it">la normalizzazione è stata rappresentata mediante
            marcatori editoriali</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-normalization-egXML-vt">
      <editorialDecl>
        <normalization method="markup">
          <p>Where both upper- and lower-case i, j, u, v, and vv have been normalized, to modern
            20th century typographical practice, the <gi>choice</gi> element has been used to
            enclose <gi>orig</gi> and <gi>reg</gi> elements giving the original and new values
            respectively. ... </p>
        </normalization>
        <normalization method="silent">
          <p>Spacing between words and following punctuation has been regularized to zero spaces;
            spacing between words has been regularized to one space.</p>
        </normalization>
        <normalization source="http://www.dict.sztaki.hu/webster">
          <p>Spelling converted throughout to Modern American usage, based on Websters 9th
            Collegiate dictionary.</p>
        </normalization>
      </editorialDecl>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-normalization-egXML-vq" source="#fr-ex-Acad">
      <editorialDecl>
        <normalization method="markup">
          <p>Là où les majuscules et les minuscules i, j, u, v et vv ont été normalisées selon la
              pratique typographique moderne, l'élément<gi> choice</gi> a été employé en association
              avec <gi>orig</gi> et <gi>reg</gi>pour fournir à la fois les formes originales et les
              formes nouvelles , respectivement ... </p>
        </normalization>
        <normalization method="silent">
          <p> L'espace entre chaque mot a été régularisé à un espace. Un signe de ponctuation
              simple est suivi d'un espace, un signe de ponctuation double est précédé et suivi d'un
              espace.</p>
        </normalization>
        <normalization source="http://www.academie-francaise.fr/langue/orthographe/plan.html">
          <p>Normalisation effectuée selon le Rapport Du Conseil Supérieur De La Langue Française
              publié dans les documents administratifs du Journal officiel du 6 décembre 1990</p>
        </normalization>
      </editorialDecl>
    </egXML>
  </exemplum>
```

^b26

### Block 27

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-normalization-egXML-xt">
      <editorialDecl>
        <normalization method="markup">
          <p>當大寫與小寫的 i, j, u, v, 以及vv已經標準化，符合二十世紀現代印刷術，<gi>choice</gi>元素就用來包含 <gi>orig</gi> 還有
              <gi>reg</gi> 兩個元素，並賦予新的意義。… </p>
        </normalization>
        <normalization method="silent">
          <p>字與字後的標點符號之間規定沒有空格；字與字間規定留一個空格。</p>
        </normalization>
        <normalization source="http://www.dict.sztaki.hu/webster">
          <p>拼字源於Websters 9th Collegiate字典的現代美語用法</p>
        </normalization>
      </editorialDecl>
    </egXML>
  </exemplum>
```

^b27

### Block 28

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD53"/>
    <ptr target="#CCAS2"/>
  </listRef>
```

^b28

