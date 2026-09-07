---
type: representation
source-type: document
source: '[[00_sources/tei-p5-metsym-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 metSym
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/metSym.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# metSym

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8653. Git blob: `e4f947d3b4a35b654977787bfa75c59559e728ba`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="verse" xml:id="gi-metSym" ident="metSym">
  <gloss versionDate="2007-07-04" xml:lang="en">metrical notation symbol</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">Symbole de notation métrique.</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">운율 표기법 기호</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">símbolo métrico de la notación</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">simbolo di notazione metrica</gloss>
  <desc versionDate="2017-02-07" xml:lang="en">documents the intended significance of a particular character or character sequence within a
    metrical notation, either explicitly or in terms of other <gi>metSym</gi> elements in the same <gi>metDecl</gi>.</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">documente le sens propre à un caractère particulier ou à
    une suite de caractères dans une notation métrique, exprimés soit explicitement, soit dans les
    termes d’autres éléments inclus dans le même élément <gi>metDecl</gi>.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">직접적으로 또는 동일 metDecl에서 다른 기호 요소로, 운율 표기법 내에서 특별한 문자 또는
    문자열의 의도된 의미를 기록한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">說明在標記韻律模式時使用的特定符號或符號序列所代表的意義，可以是明確的文字闡釋，或是加以解釋同ㄧ個韻律宣告中其他韻律符號元素的內容。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">明示的に、または要素metDecl中の他の記号要素により、韻律表記法の中に
    ある重要な特定文字または文字列を記録する。</desc>
  <desc versionDate="2018-07-18" xml:lang="de">gibt die beabsichtigte Kennzeichnung durch ein bestimmtes
    Zeichen oder eine Zeichenfolge innerhalb einer metrischen Notation an, entweder explizit oder
    über <gi>metSym</gi>-Elemente innerhalb des gleichen <gi>metDecl</gi>-Elements.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">documenta la significación ideada para un carácter
    concreto o secuencia de caracteres al interno de una anotación métrica, o explícitamente o en
    términos de otros elementos simbólicos de la metDecl.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">documenta il valore previsto di un particolare carattere
    o sequenza di caratteri all'interno di una annotazione metrica, in modo eslpicito o secondo
    altri elementi all'interno di metDecl.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
  <attList>
    <attDef ident="value" usage="req">
      <desc versionDate="2005-01-14" xml:lang="en">specifies the character or character sequence being documented.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique le caractère ou l'ordre des caractères
        documentés.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">기록된 문자 또는 문자열을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明所紀錄的符號或符號序列。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">記録される文字または文字列を示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">dokumentiert die spezifizierten Zeichen oder
        Zeichenfolgen.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica el caracter o serie de caracteres que se está
        documentando.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica il carattere o la sequenza di caratteri
        documentata.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
    </attDef>
    <attDef ident="terminal" usage="opt">
      <desc versionDate="2005-10-09" xml:lang="en">specifies whether the symbol is defined in terms of other symbols (<att>terminal</att>
        is set to <val>false</val>) or in prose (<att>terminal</att> is set to <val>true</val>).</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique si le symbole est défini à l’aide d’autres
        symboles, (l'attribut <att>terminal</att> a pour valeur <val>false</val>), ou rédigé en
        texte libre, (l'attribut <att>terminal</att> a pour valeur <val>true</val>).</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">기호가 다른 기호(<att>terminal</att>은 <val>false</val>로 설정)
        또는 산문체(<att>terminal</att>은 <val>true</val>로 설정)로 정의되는지 아닌지를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明該符號是否以其他符號來定義
        (<att>terminal</att>為<val>false</val>) 或以散文描述 (<att>terminal</att>為<val>true</val>)</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該記号が、他の記号、または散文で定義されているかどうかを示す。
          前者の場合には、属性<att>terminal</att>に値<val>false</val>が、
        後者の場合には、属性<att>terminal</att>に値<val>true</val>が付与 される。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">gibt an, ob das Symbol definiert mittels anderer
        Symbole (<att>terminal</att> gesetzt ist auf <val>false</val>) oder in Prosa
        (<att>terminal</att> auf <val>true</val>).</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica si el símbolo se define mediante otros
        símbolos (<att>terminal</att> es <val>false</val>) o en prosa (<att>terminal</att> es
          <val>true</val>).</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se il simbolo è definito con altri simboli
          (<att>terminal</att> definito dal valore <val>false</val>) o con una descrizione
          (<att>terminal</att> definito dal valore <val>true</val>).</desc>
      <datatype><dataRef key="teidata.truthValue"/></datatype>
      <defaultVal>true</defaultVal>
      <remarks ident="metSym-attr.terminal-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the element contains a prose definition of its
          meaning; the value <val>false</val> indicates that the element contains a definition of
          its meaning given using symbols defined elsewhere in the same <gi>metDecl</gi>
        element.</p>
      </remarks>
      <remarks ident="metSym-attr.terminal-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que l'élément contient une définition de son sens
          rédigée en texte libre ; la valeur <val>false</val> indique que l'élément contient une
          définition du sens donné qui utilise des symboles définis ailleurs dans le même élément
            <gi>metDecl</gi>.</p>
      </remarks>
      <remarks ident="metSym-attr.terminal-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、当該要素の意味が散文により定義されて いることを示す。属性値<val>false</val>は、当該要素の意味が、要素
            <gi>metDecl</gi>にある記号で定義されていることを示す。 </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metSym-egXML-mo">
      <metSym value="x">a stressed syllable</metSym>
      <metSym value="o">an unstressed syllable</metSym>
      <metSym value="A" terminal="false">xoo</metSym>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metSym-egXML-li">
      <metSym value="x">syllabe tonique</metSym>
      <metSym value="o">syllabe atone</metSym>
      <metSym value="A" terminal="false">xoo</metSym>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metSym-egXML-uz">
      <metSym value="仄">抑聲</metSym>
      <metSym value="平">揚聲</metSym>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#HDMN"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">metrical notation symbol</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">Symbole de notation métrique.</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">운율 표기법 기호</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">símbolo métrico de la notación</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">simbolo di notazione metrica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2017-02-07" xml:lang="en">documents the intended significance of a particular character or character sequence within a
    metrical notation, either explicitly or in terms of other <gi>metSym</gi> elements in the same <gi>metDecl</gi>.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">documente le sens propre à un caractère particulier ou à
    une suite de caractères dans une notation métrique, exprimés soit explicitement, soit dans les
    termes d’autres éléments inclus dans le même élément <gi>metDecl</gi>.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">직접적으로 또는 동일 metDecl에서 다른 기호 요소로, 운율 표기법 내에서 특별한 문자 또는
    문자열의 의도된 의미를 기록한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">說明在標記韻律模式時使用的特定符號或符號序列所代表的意義，可以是明確的文字闡釋，或是加以解釋同ㄧ個韻律宣告中其他韻律符號元素的內容。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">明示的に、または要素metDecl中の他の記号要素により、韻律表記法の中に
    ある重要な特定文字または文字列を記録する。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2018-07-18" xml:lang="de">gibt die beabsichtigte Kennzeichnung durch ein bestimmtes
    Zeichen oder eine Zeichenfolge innerhalb einer metrischen Notation an, entweder explizit oder
    über <gi>metSym</gi>-Elemente innerhalb des gleichen <gi>metDecl</gi>-Elements.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">documenta la significación ideada para un carácter
    concreto o secuencia de caracteres al interno de una anotación métrica, o explícitamente o en
    términos de otros elementos simbólicos de la metDecl.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">documenta il valore previsto di un particolare carattere
    o sequenza di caratteri all'interno di una annotazione metrica, in modo eslpicito o secondo
    altri elementi all'interno di metDecl.</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq.limited"/>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies the character or character sequence being documented.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique le caractère ou l'ordre des caractères
        documentés.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기록된 문자 또는 문자열을 명시한다.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明所紀錄的符號或符號序列。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">記録される文字または文字列を示す。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">dokumentiert die spezifizierten Zeichen oder
        Zeichenfolgen.</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica el caracter o serie de caracteres que se está
        documentando.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica il carattere o la sequenza di caratteri
        documentata.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.word"/></datatype>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-10-09" xml:lang="en">specifies whether the symbol is defined in terms of other symbols (<att>terminal</att>
        is set to <val>false</val>) or in prose (<att>terminal</att> is set to <val>true</val>).</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique si le symbole est défini à l’aide d’autres
        symboles, (l'attribut <att>terminal</att> a pour valeur <val>false</val>), ou rédigé en
        texte libre, (l'attribut <att>terminal</att> a pour valeur <val>true</val>).</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">기호가 다른 기호(<att>terminal</att>은 <val>false</val>로 설정)
        또는 산문체(<att>terminal</att>은 <val>true</val>로 설정)로 정의되는지 아닌지를 명시한다.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明該符號是否以其他符號來定義
        (<att>terminal</att>為<val>false</val>) 或以散文描述 (<att>terminal</att>為<val>true</val>)</desc>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該記号が、他の記号、または散文で定義されているかどうかを示す。
          前者の場合には、属性<att>terminal</att>に値<val>false</val>が、
        後者の場合には、属性<att>terminal</att>に値<val>true</val>が付与 される。</desc>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">gibt an, ob das Symbol definiert mittels anderer
        Symbole (<att>terminal</att> gesetzt ist auf <val>false</val>) oder in Prosa
        (<att>terminal</att> auf <val>true</val>).</desc>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica si el símbolo se define mediante otros
        símbolos (<att>terminal</att> es <val>false</val>) o en prosa (<att>terminal</att> es
          <val>true</val>).</desc>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se il simbolo è definito con altri simboli
          (<att>terminal</att> definito dal valore <val>false</val>) o con una descrizione
          (<att>terminal</att> definito dal valore <val>true</val>).</desc>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.truthValue"/></datatype>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/defaultVal[1]`.

```xml
<defaultVal>true</defaultVal>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="metSym-attr.terminal-remarks" versionDate="2007-04-22" xml:lang="en">
        <p>The value <val>true</val> indicates that the element contains a prose definition of its
          meaning; the value <val>false</val> indicates that the element contains a definition of
          its meaning given using symbols defined elsewhere in the same <gi>metDecl</gi>
        element.</p>
      </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="metSym-attr.terminal-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La valeur <val>true</val> indique que l'élément contient une définition de son sens
          rédigée en texte libre ; la valeur <val>false</val> indique que l'élément contient une
          définition du sens donné qui utilise des symboles définis ailleurs dans le même élément
            <gi>metDecl</gi>.</p>
      </remarks>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="metSym-attr.terminal-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> 属性値<val>true</val>は、当該要素の意味が散文により定義されて いることを示す。属性値<val>false</val>は、当該要素の意味が、要素
            <gi>metDecl</gi>にある記号で定義されていることを示す。 </p>
      </remarks>
```

^b38

### Block 39

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metSym-egXML-mo">
      <metSym value="x">a stressed syllable</metSym>
      <metSym value="o">an unstressed syllable</metSym>
      <metSym value="A" terminal="false">xoo</metSym>
    </egXML>
  </exemplum>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metSym-egXML-li">
      <metSym value="x">syllabe tonique</metSym>
      <metSym value="o">syllabe atone</metSym>
      <metSym value="A" terminal="false">xoo</metSym>
    </egXML>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metSym-egXML-uz">
      <metSym value="仄">抑聲</metSym>
      <metSym value="平">揚聲</metSym>
    </egXML>
  </exemplum>
```

^b41

### Block 42

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HDMN"/>
  </listRef>
```

^b42

