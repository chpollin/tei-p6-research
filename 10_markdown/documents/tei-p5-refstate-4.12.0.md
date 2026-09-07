---
type: representation
source-type: document
source: '[[00_sources/tei-p5-refstate-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 refState
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/refState.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# refState

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 7830. Git blob: `c2c014970788810b4f57039172ec014fdbbb97d0`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="header" xml:id="gi-refState" ident="refState">
  <gloss versionDate="2007-07-04" xml:lang="en">reference state</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">참조 상태</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">estado de la referencia</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">état de la référence</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">stato del riferimento</gloss>
  <gloss xml:lang="zh-TW" versionDate="2007-05-02">分界狀態</gloss>
  <desc versionDate="2007-06-09" xml:lang="en">specifies one component of a canonical reference defined by the milestone method.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">이정표 방법으로 정의된 표준 참조의 한 성분을 명시한다.</desc>
  <desc versionDate="2008-04-06" xml:lang="es">especifica un componente de una referencia canónica
    definida por el método milestone</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">標石要素の手法として定義されている標準的な参照の構成要素をひとつ示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">spécifie un composant d’une référence canonique définie
    par la méthode du bornage.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">specifica una componente di un riferimento canonico
    definito dal metodo milestone</desc>
  <desc xml:lang="zh-TW" versionDate="2007-05-02">標明分界方法所定義的權威參照標準裡其中一個組件。</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.milestoneUnit"/>
  </classes>
  <content><empty/></content>
  <attList>
    <!-- MDH 2012-07-15: Attribute @unit moved to att.milestoneUnit; milestone and refState are now members of 
     that attribute class. This centralizes the definition of the attribute and its suggested values. 
     SF ticket http://purl.org/tei/bugs/3537452. -->
    <attDef ident="length" usage="opt">
      <desc versionDate="2007-06-09" xml:lang="en">specifies the fixed length of the reference component.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">참조 성분의 고정 길이를 명시한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">especifica la longitud fija del componente de
        referencia.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">参照構成要素の固定長を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">spécifie la longueur fixe du composant de la
        référence.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">specifica la lunghezza stabilita della componente di
        riferimento</desc>
      <datatype><dataRef key="teidata.count"/></datatype>
      <remarks ident="refState-attr.length-remarks" versionDate="2007-06-09" xml:lang="en">
        <p>When constructing a reference, if the reference component found is of numeric type, the
          length is made up by inserting leading zeros; if it is not, by inserting trailing blanks.
          In either case, reference components are truncated if necessary at the right hand side. </p>
        <p>When seeking a reference, the length indicates the number of characters which should be
          compared. Values longer than this will be regarded as matching, if they start correctly. If no value is provided, the length is unlimited and
        goes to the next delimiter or to the end of the value.
        </p>
      </remarks>
      <remarks ident="refState-attr.length-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Lorsqu'une référence est construite, si le composant de cette référence est de type
          numérique, la longueur est obtenue en ajoutant au début des 0 ; sinon, en ajoutant en fin
          de chaîne des blancs. Dans les deux cas, les composants des références sont tronqués sur
          la droite si c'est nécessaire.</p>
        <p>Lorsqu'on cherche une référence, la longueur indique le nombre des caractères devant être
          comparés. Des valeurs plus longues seront considérées comme correspondant au modèle, si
          elles commencent de façon identique. Si aucune valeur n'est fournie,
        la longueur est illimitée et va jusqu'au prochain délimiteur ou jusqu'à la fin de la valeur.</p>
      </remarks>
      <remarks ident="refState-attr.length-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Al construir una referencia, si el componente de la referencia es de tipo numérico, la
          longitud es compuesta insertando ceros; si no lo es, insertando espacios a la derecha. En
          cualquier caso, los componentes de la referencia se truncan en caso de necesidad por el
          lado derecho. </p>
        <p>En una referencia, la longitud indica el número de caracteres que deban ser comparados.
          Los valores más largos a estos se considerarán puntualmente acceptado si comienzan
          correctamente. </p>
      </remarks>
      <remarks ident="refState-attr.length-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 参照構成要素が数値型の場合、当該長さの先頭にゼロの列が付く。数 値型でない場合、最後に空白が付く。必要であれば、参照構成要素の 値は丸められることがある。 </p>
        <p> 参照を求める際、当該長さは、比べられる文字の数を示す。この値よ りも長い場合、開始点が正しければ、マッチすると判断されるだろう。 </p>
      </remarks>
    </attDef>
    <attDef ident="delim" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">delimiter</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">구분 문자</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">delimitador</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">délimiteur</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">delimitatore</gloss>
      <desc versionDate="2007-06-09" xml:lang="en">supplies a delimiting string following the reference component.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">참조 성분 뒤에 구분 문자열을 제공한다.</desc>
      <desc versionDate="2008-04-06" xml:lang="es">suministra la cadena de delimitación que sigue el
        componente de referencia.</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">参照構成要素の開始を表すデリミタを示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">fournit une suite de caractères de délimitation après
        le composant de référence.</desc>
      <desc versionDate="2007-11-06" xml:lang="it">fornisce una stringa di delimitazione in base alla
        componente di riferimento</desc>
      <datatype><dataRef key="teidata.text"/></datatype>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refState-egXML-uq" source="#UND">
      <refState unit="book" delim=":"/>
      <refState unit="line" length="4"/>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refState-egXML-av" source="#UND">
      <refState unit="livre" delim=":"/>
      <refState unit="line" length="4"/>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HD54M"/>
    <ptr target="#HD54"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">reference state</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">참조 상태</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">estado de la referencia</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">état de la référence</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">stato del riferimento</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss xml:lang="zh-TW" versionDate="2007-05-02">分界狀態</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-06-09" xml:lang="en">specifies one component of a canonical reference defined by the milestone method.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이정표 방법으로 정의된 표준 참조의 한 성분을 명시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">especifica un componente de una referencia canónica
    definida por el método milestone</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">標石要素の手法として定義されている標準的な参照の構成要素をひとつ示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie un composant d’une référence canonique définie
    par la méthode du bornage.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">specifica una componente di un riferimento canonico
    definito dal metodo milestone</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc xml:lang="zh-TW" versionDate="2007-05-02">標明分界方法所定義的權威參照標準裡其中一個組件。</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.edition"/>
    <memberOf key="att.milestoneUnit"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content><empty/></content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-06-09" xml:lang="en">specifies the fixed length of the reference component.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참조 성분의 고정 길이를 명시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">especifica la longitud fija del componente de
        referencia.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">参照構成要素の固定長を示す。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">spécifie la longueur fixe du composant de la
        référence.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">specifica la lunghezza stabilita della componente di
        riferimento</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.count"/></datatype>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="refState-attr.length-remarks" versionDate="2007-06-09" xml:lang="en">
        <p>When constructing a reference, if the reference component found is of numeric type, the
          length is made up by inserting leading zeros; if it is not, by inserting trailing blanks.
          In either case, reference components are truncated if necessary at the right hand side. </p>
        <p>When seeking a reference, the length indicates the number of characters which should be
          compared. Values longer than this will be regarded as matching, if they start correctly. If no value is provided, the length is unlimited and
        goes to the next delimiter or to the end of the value.
        </p>
      </remarks>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="refState-attr.length-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Lorsqu'une référence est construite, si le composant de cette référence est de type
          numérique, la longueur est obtenue en ajoutant au début des 0 ; sinon, en ajoutant en fin
          de chaîne des blancs. Dans les deux cas, les composants des références sont tronqués sur
          la droite si c'est nécessaire.</p>
        <p>Lorsqu'on cherche une référence, la longueur indique le nombre des caractères devant être
          comparés. Des valeurs plus longues seront considérées comme correspondant au modèle, si
          elles commencent de façon identique. Si aucune valeur n'est fournie,
        la longueur est illimitée et va jusqu'au prochain délimiteur ou jusqu'à la fin de la valeur.</p>
      </remarks>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="refState-attr.length-remarks" versionDate="2008-04-06" xml:lang="es">
        <p>Al construir una referencia, si el componente de la referencia es de tipo numérico, la
          longitud es compuesta insertando ceros; si no lo es, insertando espacios a la derecha. En
          cualquier caso, los componentes de la referencia se truncan en caso de necesidad por el
          lado derecho. </p>
        <p>En una referencia, la longitud indica el número de caracteres que deban ser comparados.
          Los valores más largos a estos se considerarán puntualmente acceptado si comienzan
          correctamente. </p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[4]`.

```xml
<remarks ident="refState-attr.length-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 参照構成要素が数値型の場合、当該長さの先頭にゼロの列が付く。数 値型でない場合、最後に空白が付く。必要であれば、参照構成要素の 値は丸められることがある。 </p>
        <p> 参照を求める際、当該長さは、比べられる文字の数を示す。この値よ りも長い場合、開始点が正しければ、マッチすると判断されるだろう。 </p>
      </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">delimiter</gloss>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">구분 문자</gloss>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">delimitador</gloss>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">délimiteur</gloss>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">delimitatore</gloss>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-06-09" xml:lang="en">supplies a delimiting string following the reference component.</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">참조 성분 뒤에 구분 문자열을 제공한다.</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">suministra la cadena de delimitación que sigue el
        componente de referencia.</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">参照構成要素の開始を表すデリミタを示す。</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">fournit une suite de caractères de délimitation après
        le composant de référence.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">fornisce una stringa di delimitazione in base alla
        componente di riferimento</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.text"/></datatype>
```

^b38

### Block 39

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refState-egXML-uq" source="#UND">
      <refState unit="book" delim=":"/>
      <refState unit="line" length="4"/>
    </egXML>
  </exemplum>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-refState-egXML-av" source="#UND">
      <refState unit="livre" delim=":"/>
      <refState unit="line" length="4"/>
    </egXML>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HD54M"/>
    <ptr target="#HD54"/>
  </listRef>
```

^b41

