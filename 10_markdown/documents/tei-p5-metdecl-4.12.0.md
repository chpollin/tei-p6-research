---
type: representation
source-type: document
source: '[[00_sources/tei-p5-metdecl-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 metDecl
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/metDecl.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# metDecl

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 19322. Git blob: `a371e93de4e0deab385249a4b4302806dda0b2ab`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="verse" xml:id="gi-metDecl" ident="metDecl">
  <gloss versionDate="2007-07-04" xml:lang="en">metrical notation declaration</gloss>
  <gloss versionDate="2009-01-05" xml:lang="fr">déclaration sur la métrique</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">운율적 표기법 선언</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">declaración de notación métrica</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">dichiarazione di notazione metrica</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">documents the notation employed to represent a metrical pattern when this is specified as
    the value of a <att>met</att>, <att>real</att>, or <att>rhyme</att> attribute on any structural
    element of a metrical text (e.g. <gi>lg</gi>, <gi>l</gi>, or <gi>seg</gi>).</desc>
  <desc versionDate="2009-01-05" xml:lang="fr">documente la notation utilisée pour noter un modèle
    métrique lorsque celui-ci est spécifié comme la valeur des attributs <att>met </att>,
    <att>real</att>, ou <att>rhyme</att>, qui s’appliquent à tout élément de la structure d’un texte
    versifié (par exemple <gi>lg</gi>, <gi>l</gi>, ou <gi>seg</gi>).</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">운율적 텍스트에서 구조적 요소(예, <gi>lg</gi>, <gi>l</gi>, 또는
    <gi>seg</gi>)에 대한 <att>met</att>, <att>real</att>, 또는 <att>rhyme</att> 속성 값으로 명시할 때 운율적 유형을 표시하는
    표기법을 기록한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">在標記韻文時所用到的結構性元素
    (例如<gi>lg</gi>、<gi>l</gi>、或<gi>seg</gi>)
    當中，若使用<att>met</att>、<att>real</att>、或<att>rhyme</att>等屬性的屬性值來表示文章的韻律模式，則在此宣告標記韻律模式的方法。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">韻律パタンを表す表記法を示す。韻文のための要素(例えば、<gi>lg</gi>、<gi>l</gi>、
      <gi>seg</gi>など)にある属性<att>met</att>、<att>real</att>、 <att>rhyme</att>の値として定義される。</desc>
  <desc versionDate="2006-10-18" xml:lang="de">Notation eines metrischen Musters, sofern dies als Wert
    eines Attributs <att>met</att>, <att>real</att>, oder <att>rhyme</att> angegeben ist, für ein
    beliebiges Strukturelement eines metrischen Textes (z.B. <gi>lg</gi>, <gi>l</gi>, oder
    <gi>seg</gi>).</desc>
  <desc versionDate="2007-05-04" xml:lang="es">documenta la notación empleada para representar un patrón
    métrico cuando éste se especifica como el valor de un atributo <att>met</att>, <att>real</att>,
    o <att>rhyme</att> en cualquier elemento estructural de un texto métrico (p.ej. <gi>lg</gi>,
      <gi>l</gi>, or <gi>seg</gi>).</desc>
  <desc versionDate="2007-01-21" xml:lang="it">documenta l'annotazione adottata nella rappresentazione
    di uno schema metrico, specificato come valore di un attributo <att>met</att>, <att>real</att>,
    o <att>rhyme</att> su un qualsiasi elemento strutturale di un testo metrico (ad esempio
    <gi>lg</gi>, <gi>l</gi>, or <gi>seg</gi>).</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
  <content>
    <alternate>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.pLike"/>
        <classRef key="model.noteLike"/>
      </alternate>
      <elementRef key="metSym" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
  <constraintSpec ident="metDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:metDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="type" usage="opt">
      <desc versionDate="2005-01-14" xml:lang="en">indicates whether the notation conveys the abstract metrical form, its actual prosodic realization, or the rhyme scheme, or some combination thereof.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique si la notation traduit la forme métrique abstraite, sa réalisation prosodique, le schéma des rimes, ou une combinaison de ces différents éléments.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">표기법이 추상적 운율 형식, 그 실제 운율적 실현, 또는 운 스키마, 아니면 그것에 관련한
        결합을 포함하는지를 표시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">指出該標記所傳達的為抽象韻律形式、實際韻律實踐、或者押韻形式，或任幾項之結合。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該表記法が抽象的韻律形式、実際の韻律形式、押韻スキーム、これら の組み合わせを表すかどうかを示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">zeigt an, ob die Notation die abstrakte metrische Form, die tatsächliche prosodische Realisierung oder das Reimschema oder eine Kombination dessen wiedergibt.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica si la notación indica la forma métrica abstracta, su realización prosódica real, el esquema rítmico o alguna combinación de todo ello.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica se l'annotazione fornisce la forma metrica estratta, la sua realizzazione prosodica,lo schema delle rime o un loro combinazione.</desc>
      <datatype minOccurs="1" maxOccurs="3"><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>met real</defaultVal>
      <valList type="closed">
        <valItem ident="met">
          <gloss versionDate="2007-05-12" xml:lang="en"><att>met</att> attribute</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko"><att>met</att> 속성</gloss>
          <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性<att>met</att></gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">attribut <att>met</att></gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">attributo met</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">atributo <att>met</att></gloss>
          <desc versionDate="2007-05-12" xml:lang="en">declaration applies to the abstract metrical form recorded on the <att>met</att>
            attribute</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">선언은 <att>met</att> 속성에 기록된 추상적 운율 형식에 적용한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">屬性 <att>met</att>宣告適用於該屬性所紀錄的抽象韻律形式。</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">属性<att>met</att>にある、抽象的韻律形式に該当する。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">la déclaration s'applique à la structure métrique
            abstraite notée par l'attribut <att>met</att>.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione si riferisce alla forma metrica
            astratta contenuta nell'attributo met</desc>
          <desc versionDate="2007-05-04" xml:lang="es">declaración aplicada a la forma métrica abstracta
            codificada en el atributo <att>met</att>.</desc>
        </valItem>
        <valItem ident="real">
          <gloss versionDate="2007-05-12" xml:lang="en"><att>real</att> attribute</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko"><att>real</att> 속성</gloss>
          <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性<att>real</att></gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">attribut <att>real</att></gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">attributo real</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">atributo <att>real</att></gloss>
          <desc versionDate="2007-05-12" xml:lang="en">declaration applies to the actual realization of the conventional metrical structure
            recorded on the <att>real</att> attribute</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">선언은 <att>real</att> 속성에 기록된 관례적 운율 구조의 실제 실현에
            적용한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">屬性<att>real</att>宣告適用於該屬性所紀錄的通用韻律結構之實際實踐</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">属性<att>real</att>にある実際の韻律形式に該当する。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">la déclaration s'applique à la réalisation réelle
            de la structure métrique conventionnelle notée par l'attribut <att>real</att> .</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione si riferisce all'effettiva
            realizzazione della struttura metrica convenzionale contenuta nell'attributo real</desc>
          <desc versionDate="2007-05-04" xml:lang="es">declaración aplicada a la realización concreta de
            una estructura métrica convencional codificada en el atributo <att>real</att>.</desc>
        </valItem>
        <valItem ident="rhyme">
<!-- remove redundant glosses LB 2014-05-21-->
<!--          <gloss versionDate="2007-05-12" xml:lang="en"><att>rhyme</att> attribute</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko"><att>rhyme</att> 속성</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es"><att>rima</att> atributo</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">attribut rime</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">attributo rhyme</gloss>
    -->

      <desc versionDate="2007-05-12" xml:lang="en">declaration applies to the rhyme scheme recorded on the <att>rhyme</att> attribute</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">선언은 <att>rhyme</att> 속성에 기록된 운 스키마에 적용한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la declaración se aplica al esquema de rima
            registrado en el atributo <att>rima</att></desc>
          <desc versionDate="2008-04-05" xml:lang="ja">属性<att>rhyme</att>にある押韻スキームに該当する。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">la déclaration s'applique à la structure métrique
            abstraite <!--A VALIDER : au schéma de rimes décrit dans-->notée par l'attribut
              <att>rhyme</att>.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione si riferisce allo schema rimico
            contenuto nell'attributo rhyme</desc>
        </valItem>
      </valList>
      <remarks ident="metDecl-attr.type-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>By default, the <gi>metDecl</gi> element documents the notation used for metrical pattern
          and realization. It may also be used to document the notation used for rhyme scheme
          information; if not otherwise documented, the rhyme scheme notation defaults to the
          traditional <q>abab</q> notation.</p>
      </remarks>
      <remarks ident="metDecl-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Par défaut, l'élément <gi>metDecl</gi> documente la notation utilisée pour le modèle
          métrique et sa réalisation. Il peut aussi être utilisé pour la notation du schéma de rimes
          ; s'il n'est pas documenté d'une autre manière, la notation du schéma de rimes pourra
          l'être par défaut sous la forme traditionnelle <q>abab</q>. </p>
      </remarks>
      <remarks ident="metDecl-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> デフォルト値として、要素<gi>metDecl</gi>は、韻律パタンや実現形 を表す表記法を記録する。また、押韻スキーム用の表記法も記録する。
          これら表記法が記録されたいない場合には、押韻スキームのデフォルト の表記法は、従来の<q>アバブ(abab)</q>法になる。 </p>
      </remarks>
    </attDef>
    <attDef ident="pattern" usage="opt">
      <gloss versionDate="2007-07-04" xml:lang="en">regular expression pattern</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">정규표현 유형</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">modelo de expresión regular</gloss>
      <gloss versionDate="2008-03-30" xml:lang="fr">modèle d'expression régulière</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">schema di espressioni regolari</gloss>
      <desc versionDate="2005-01-14" xml:lang="en">specifies a regular expression defining any value that is legal for this notation.</desc>
      <desc versionDate="2009-01-05" xml:lang="fr">indique une expression régulière définissant toute
        valeur permise dans cette notation.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">이 표기법에 적법한 임의의 값을 정의하는 정규표현을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明一種固定表示法，用來定義任何合用於此標記的屬性值。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">当該表記法に叶う値を正規表現で示す。</desc>
      <desc versionDate="2006-10-18" xml:lang="de">definiert einen regulären Ausdruck, der einen
        zulässigen Wert für diese Notation vorgibt.</desc>
      <desc versionDate="2007-05-04" xml:lang="es">indica una expresión regular que define cualquier
        valor válido para esta notación.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica un'espressione regolare che definisce
        qualsiasi valore legale per l'annotazione</desc>
      <datatype><dataRef key="teidata.pattern"/></datatype>
      <remarks ident="metDecl-attr.pattern-remarks" versionDate="2013-12-21" xml:lang="en"><p>The value must be a valid regular expression per the World Wide Web Consortium's
        <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref>,
      Appendix F.
</p></remarks>
<remarks ident="metDecl-attr.pattern-remarks" versionDate="2013-12-21" xml:lang="fr"><p>La valeur doit être une expression régulière valide pour le Consortium
  du World Wide Web <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref>, Appendix F.</p></remarks>
         
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metDecl-egXML-vf">
      <metDecl xml:id="ip" type="met" pattern="((SU|US)USUSUSUS/)">
        <metSym value="S">stressed syllable</metSym>
        <metSym value="U">unstressed syllable</metSym>
        <metSym value="/">metrical line boundary</metSym>
      </metDecl>
    </egXML>
    <p>This example is intended for the far more restricted case typified by the Shakespearean
      iambic pentameter. Only metrical patterns containing exactly ten syllables, alternately
      stressed and unstressed, (except for the first two which may be in either order) to each
      metrical line can be expressed using this notation.</p>
  </exemplum>
  <!-- Corrected to show Alexandrine example as suggested by "an expert on French metrics" (see Council list 2012-03-26). -->
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metDecl-egXML-ef">
      <metDecl xml:id="fr_ip" type="met" pattern="(AAAAAT\|AAAAT(A)?)">
        <metSym value="T">syllabe tonique</metSym>
        <metSym value="A">syllabe atone</metSym>
        <metSym value="|">pause métrique</metSym>
      </metDecl>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cette notation décrit ici la division en groupes rythmiques d'un vers composé de douze
        syllabes (alexandrin) comme dans ce vers de Baudelaire : 
          <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metDecl-egXML-ma" source="#fr-ex-Baudelaire-vie"><lg n="1" type="quatrain"><l n="1">J'ai longtemps habité sous de vastes portiques</l></lg></egXML>
      </p>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metDecl-egXML-ce">
      <metDecl xml:id="zh-tw_ip" type="met" pattern="((SU|US)USUSUSUS/)">
        <metSym value="S">仄聲</metSym>
        <metSym value="U">平聲</metSym>
        <metSym value="/">詩行分界線</metSym>
      </metDecl>
    </egXML>
  </exemplum>
  <remarks ident="metDecl-remarks" versionDate="2006-07-02" xml:lang="en">
    <p rend="dataDesc">The encoder may choose whether to define the notation formally or informally.
      However, the two methods may not be mixed. That is, <gi>metDecl</gi> may contain either a
      sequence of <gi>metSym</gi> elements or, alternately, a series of paragraphs or other
      components. If the <att>pattern</att> attribute is specified and <gi>metSym</gi> elements are
      used, then all the codes appearing within the <att>pattern</att> attribute should be
      documented.</p>
    <p>Only usable within the header if the verse module is used.</p>
  </remarks>
  <remarks ident="metDecl-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc"> L'encodeur peut choisir de définir la notation de manière formelle ou pas.
      Toutefois, les deux méthodes ne peuvent pas être combinées. C'est-à-dire, que <gi>metDecl</gi>peut
      contenir soit une suite d'éléments <gi>metSym</gi>, soit une succession de paragraphes ou
      d'autres composants. Si l'attribut <att>pattern</att> est spécifié et que des éléments
        <gi>metSym</gi> sont employés, alors tous les codes qui apparaitront dans l'attribut
        <att>pattern</att>devront être documentés.</p>
    <p>Ne peut être utilisé dans l'en-tête que si le jeu d'éléments pour la poésie est activé.</p>
  </remarks>
  <remarks ident="metDecl-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 符号化する人は、当該表記法が形式的・非形式的に定義するかを選択する ことができる。しかし、この2つを混ぜて使うことはないだろう。つまり、
        要素<gi>metDecl</gi>が、一連の要素<gi>metSym</gi>、または一連の段落
      や他の構成要素をとるかもしれない。属性<att>pattern</att>が定義され、 かつ要素<gi>metSym</gi>が使われている場合には、属性
      <att>pattern</att>中にあるコードは全て記録されるべきである。 </p>
    <p> 当該要素は、韻文モジュールを使う場合にのみ、ヘダー中で使うことがで きる。 </p>
  </remarks>
  <listRef>
    <ptr target="#HDMN"/>
    <ptr target="#VEME"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">metrical notation declaration</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2009-01-05" xml:lang="fr">déclaration sur la métrique</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">운율적 표기법 선언</gloss>
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
<gloss versionDate="2008-04-06" xml:lang="es">declaración de notación métrica</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">dichiarazione di notazione metrica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">documents the notation employed to represent a metrical pattern when this is specified as
    the value of a <att>met</att>, <att>real</att>, or <att>rhyme</att> attribute on any structural
    element of a metrical text (e.g. <gi>lg</gi>, <gi>l</gi>, or <gi>seg</gi>).</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">documente la notation utilisée pour noter un modèle
    métrique lorsque celui-ci est spécifié comme la valeur des attributs <att>met </att>,
    <att>real</att>, ou <att>rhyme</att>, qui s’appliquent à tout élément de la structure d’un texte
    versifié (par exemple <gi>lg</gi>, <gi>l</gi>, ou <gi>seg</gi>).</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">운율적 텍스트에서 구조적 요소(예, <gi>lg</gi>, <gi>l</gi>, 또는
    <gi>seg</gi>)에 대한 <att>met</att>, <att>real</att>, 또는 <att>rhyme</att> 속성 값으로 명시할 때 운율적 유형을 표시하는
    표기법을 기록한다.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">在標記韻文時所用到的結構性元素
    (例如<gi>lg</gi>、<gi>l</gi>、或<gi>seg</gi>)
    當中，若使用<att>met</att>、<att>real</att>、或<att>rhyme</att>等屬性的屬性值來表示文章的韻律模式，則在此宣告標記韻律模式的方法。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">韻律パタンを表す表記法を示す。韻文のための要素(例えば、<gi>lg</gi>、<gi>l</gi>、
      <gi>seg</gi>など)にある属性<att>met</att>、<att>real</att>、 <att>rhyme</att>の値として定義される。</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">Notation eines metrischen Musters, sofern dies als Wert
    eines Attributs <att>met</att>, <att>real</att>, oder <att>rhyme</att> angegeben ist, für ein
    beliebiges Strukturelement eines metrischen Textes (z.B. <gi>lg</gi>, <gi>l</gi>, oder
    <gi>seg</gi>).</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">documenta la notación empleada para representar un patrón
    métrico cuando éste se especifica como el valor de un atributo <att>met</att>, <att>real</att>,
    o <att>rhyme</att> en cualquier elemento estructural de un texto métrico (p.ej. <gi>lg</gi>,
      <gi>l</gi>, or <gi>seg</gi>).</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">documenta l'annotazione adottata nella rappresentazione
    di uno schema metrico, specificato come valore di un attributo <att>met</att>, <att>real</att>,
    o <att>rhyme</att> su un qualsiasi elemento strutturale di un testo metrico (ad esempio
    <gi>lg</gi>, <gi>l</gi>, or <gi>seg</gi>).</desc>
```

^b14

### Block 15

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.declarable"/>
    <memberOf key="model.encodingDescPart"/>
  </classes>
```

^b15

### Block 16

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate>
      <alternate minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.pLike"/>
        <classRef key="model.noteLike"/>
      </alternate>
      <elementRef key="metSym" minOccurs="1" maxOccurs="unbounded"/>
    </alternate>
  </content>
```

^b16

### Block 17

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="metDecl-is-declarable" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:pattern is-a="declarable">
        <sch:param name="tde" value="tei:metDecl"/>
      </sch:pattern>
    </constraint>
  </constraintSpec>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates whether the notation conveys the abstract metrical form, its actual prosodic realization, or the rhyme scheme, or some combination thereof.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique si la notation traduit la forme métrique abstraite, sa réalisation prosodique, le schéma des rimes, ou une combinaison de ces différents éléments.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">표기법이 추상적 운율 형식, 그 실제 운율적 실현, 또는 운 스키마, 아니면 그것에 관련한
        결합을 포함하는지를 표시한다.</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出該標記所傳達的為抽象韻律形式、實際韻律實踐、或者押韻形式，或任幾項之結合。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該表記法が抽象的韻律形式、実際の韻律形式、押韻スキーム、これら の組み合わせを表すかどうかを示す。</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">zeigt an, ob die Notation die abstrakte metrische Form, die tatsächliche prosodische Realisierung oder das Reimschema oder eine Kombination dessen wiedergibt.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica si la notación indica la forma métrica abstracta, su realización prosódica real, el esquema rítmico o alguna combinación de todo ello.</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica se l'annotazione fornisce la forma metrica estratta, la sua realizzazione prosodica,lo schema delle rime o un loro combinazione.</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="1" maxOccurs="3"><dataRef key="teidata.enumerated"/></datatype>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>met real</defaultVal>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="met">
          <gloss versionDate="2007-05-12" xml:lang="en"><att>met</att> attribute</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko"><att>met</att> 속성</gloss>
          <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性<att>met</att></gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">attribut <att>met</att></gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">attributo met</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">atributo <att>met</att></gloss>
          <desc versionDate="2007-05-12" xml:lang="en">declaration applies to the abstract metrical form recorded on the <att>met</att>
            attribute</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">선언은 <att>met</att> 속성에 기록된 추상적 운율 형식에 적용한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">屬性 <att>met</att>宣告適用於該屬性所紀錄的抽象韻律形式。</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">属性<att>met</att>にある、抽象的韻律形式に該当する。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">la déclaration s'applique à la structure métrique
            abstraite notée par l'attribut <att>met</att>.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione si riferisce alla forma metrica
            astratta contenuta nell'attributo met</desc>
          <desc versionDate="2007-05-04" xml:lang="es">declaración aplicada a la forma métrica abstracta
            codificada en el atributo <att>met</att>.</desc>
        </valItem>
        <valItem ident="real">
          <gloss versionDate="2007-05-12" xml:lang="en"><att>real</att> attribute</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko"><att>real</att> 속성</gloss>
          <gloss versionDate="2007-05-02" xml:lang="zh-TW">屬性<att>real</att></gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">attribut <att>real</att></gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">attributo real</gloss>
          <gloss versionDate="2007-05-04" xml:lang="es">atributo <att>real</att></gloss>
          <desc versionDate="2007-05-12" xml:lang="en">declaration applies to the actual realization of the conventional metrical structure
            recorded on the <att>real</att> attribute</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">선언은 <att>real</att> 속성에 기록된 관례적 운율 구조의 실제 실현에
            적용한다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">屬性<att>real</att>宣告適用於該屬性所紀錄的通用韻律結構之實際實踐</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">属性<att>real</att>にある実際の韻律形式に該当する。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">la déclaration s'applique à la réalisation réelle
            de la structure métrique conventionnelle notée par l'attribut <att>real</att> .</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione si riferisce all'effettiva
            realizzazione della struttura metrica convenzionale contenuta nell'attributo real</desc>
          <desc versionDate="2007-05-04" xml:lang="es">declaración aplicada a la realización concreta de
            una estructura métrica convencional codificada en el atributo <att>real</att>.</desc>
        </valItem>
        <valItem ident="rhyme">
<!-- remove redundant glosses LB 2014-05-21-->
<!--          <gloss versionDate="2007-05-12" xml:lang="en"><att>rhyme</att> attribute</gloss>
          <gloss versionDate="2007-12-20" xml:lang="ko"><att>rhyme</att> 속성</gloss>
          <gloss versionDate="2008-04-06" xml:lang="es"><att>rima</att> atributo</gloss>
          <gloss versionDate="2007-06-12" xml:lang="fr">attribut rime</gloss>
          <gloss versionDate="2007-11-06" xml:lang="it">attributo rhyme</gloss>
    -->

      <desc versionDate="2007-05-12" xml:lang="en">declaration applies to the rhyme scheme recorded on the <att>rhyme</att> attribute</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">선언은 <att>rhyme</att> 속성에 기록된 운 스키마에 적용한다.</desc>
          <desc versionDate="2008-04-06" xml:lang="es">la declaración se aplica al esquema de rima
            registrado en el atributo <att>rima</att></desc>
          <desc versionDate="2008-04-05" xml:lang="ja">属性<att>rhyme</att>にある押韻スキームに該当する。</desc>
          <desc versionDate="2007-06-12" xml:lang="fr">la déclaration s'applique à la structure métrique
            abstraite <!--A VALIDER : au schéma de rimes décrit dans-->notée par l'attribut
              <att>rhyme</att>.</desc>
          <desc versionDate="2007-11-06" xml:lang="it">la dichiarazione si riferisce allo schema rimico
            contenuto nell'attributo rhyme</desc>
        </valItem>
      </valList>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="metDecl-attr.type-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>By default, the <gi>metDecl</gi> element documents the notation used for metrical pattern
          and realization. It may also be used to document the notation used for rhyme scheme
          information; if not otherwise documented, the rhyme scheme notation defaults to the
          traditional <q>abab</q> notation.</p>
      </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="metDecl-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Par défaut, l'élément <gi>metDecl</gi> documente la notation utilisée pour le modèle
          métrique et sa réalisation. Il peut aussi être utilisé pour la notation du schéma de rimes
          ; s'il n'est pas documenté d'une autre manière, la notation du schéma de rimes pourra
          l'être par défaut sous la forme traditionnelle <q>abab</q>. </p>
      </remarks>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="metDecl-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p> デフォルト値として、要素<gi>metDecl</gi>は、韻律パタンや実現形 を表す表記法を記録する。また、押韻スキーム用の表記法も記録する。
          これら表記法が記録されたいない場合には、押韻スキームのデフォルト の表記法は、従来の<q>アバブ(abab)</q>法になる。 </p>
      </remarks>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">regular expression pattern</gloss>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">정규표현 유형</gloss>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">modelo de expresión regular</gloss>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">modèle d'expression régulière</gloss>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attDef[2]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">schema di espressioni regolari</gloss>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies a regular expression defining any value that is legal for this notation.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2009-01-05" xml:lang="fr">indique une expression régulière définissant toute
        valeur permise dans cette notation.</desc>
```

^b38

### Block 39

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">이 표기법에 적법한 임의의 값을 정의하는 정규표현을 명시한다.</desc>
```

^b39

### Block 40

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明一種固定表示法，用來定義任何合用於此標記的屬性值。</desc>
```

^b40

### Block 41

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該表記法に叶う値を正規表現で示す。</desc>
```

^b41

### Block 42

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2006-10-18" xml:lang="de">definiert einen regulären Ausdruck, der einen
        zulässigen Wert für diese Notation vorgibt.</desc>
```

^b42

### Block 43

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica una expresión regular que define cualquier
        valor válido para esta notación.</desc>
```

^b43

### Block 44

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[8]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica un'espressione regolare che definisce
        qualsiasi valore legale per l'annotazione</desc>
```

^b44

### Block 45

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pattern"/></datatype>
```

^b45

### Block 46

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="metDecl-attr.pattern-remarks" versionDate="2013-12-21" xml:lang="en"><p>The value must be a valid regular expression per the World Wide Web Consortium's
        <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref>,
      Appendix F.
</p></remarks>
```

^b46

### Block 47

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="metDecl-attr.pattern-remarks" versionDate="2013-12-21" xml:lang="fr"><p>La valeur doit être une expression régulière valide pour le Consortium
  du World Wide Web <ref target="#XSD2">XML Schema Part 2: Datatypes Second Edition</ref>, Appendix F.</p></remarks>
```

^b47

### Block 48

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metDecl-egXML-vf">
      <metDecl xml:id="ip" type="met" pattern="((SU|US)USUSUSUS/)">
        <metSym value="S">stressed syllable</metSym>
        <metSym value="U">unstressed syllable</metSym>
        <metSym value="/">metrical line boundary</metSym>
      </metDecl>
    </egXML>
    <p>This example is intended for the far more restricted case typified by the Shakespearean
      iambic pentameter. Only metrical patterns containing exactly ten syllables, alternately
      stressed and unstressed, (except for the first two which may be in either order) to each
      metrical line can be expressed using this notation.</p>
  </exemplum>
```

^b48

### Block 49

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metDecl-egXML-ef">
      <metDecl xml:id="fr_ip" type="met" pattern="(AAAAAT\|AAAAT(A)?)">
        <metSym value="T">syllabe tonique</metSym>
        <metSym value="A">syllabe atone</metSym>
        <metSym value="|">pause métrique</metSym>
      </metDecl>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Cette notation décrit ici la division en groupes rythmiques d'un vers composé de douze
        syllabes (alexandrin) comme dans ce vers de Baudelaire : 
          <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metDecl-egXML-ma" source="#fr-ex-Baudelaire-vie"><lg n="1" type="quatrain"><l n="1">J'ai longtemps habité sous de vastes portiques</l></lg></egXML>
      </p>
  </exemplum>
```

^b49

### Block 50

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-metDecl-egXML-ce">
      <metDecl xml:id="zh-tw_ip" type="met" pattern="((SU|US)USUSUSUS/)">
        <metSym value="S">仄聲</metSym>
        <metSym value="U">平聲</metSym>
        <metSym value="/">詩行分界線</metSym>
      </metDecl>
    </egXML>
  </exemplum>
```

^b50

### Block 51

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="metDecl-remarks" versionDate="2006-07-02" xml:lang="en">
    <p rend="dataDesc">The encoder may choose whether to define the notation formally or informally.
      However, the two methods may not be mixed. That is, <gi>metDecl</gi> may contain either a
      sequence of <gi>metSym</gi> elements or, alternately, a series of paragraphs or other
      components. If the <att>pattern</att> attribute is specified and <gi>metSym</gi> elements are
      used, then all the codes appearing within the <att>pattern</att> attribute should be
      documented.</p>
    <p>Only usable within the header if the verse module is used.</p>
  </remarks>
```

^b51

### Block 52

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="metDecl-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc"> L'encodeur peut choisir de définir la notation de manière formelle ou pas.
      Toutefois, les deux méthodes ne peuvent pas être combinées. C'est-à-dire, que <gi>metDecl</gi>peut
      contenir soit une suite d'éléments <gi>metSym</gi>, soit une succession de paragraphes ou
      d'autres composants. Si l'attribut <att>pattern</att> est spécifié et que des éléments
        <gi>metSym</gi> sont employés, alors tous les codes qui apparaitront dans l'attribut
        <att>pattern</att>devront être documentés.</p>
    <p>Ne peut être utilisé dans l'en-tête que si le jeu d'éléments pour la poésie est activé.</p>
  </remarks>
```

^b52

### Block 53

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="metDecl-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 符号化する人は、当該表記法が形式的・非形式的に定義するかを選択する ことができる。しかし、この2つを混ぜて使うことはないだろう。つまり、
        要素<gi>metDecl</gi>が、一連の要素<gi>metSym</gi>、または一連の段落
      や他の構成要素をとるかもしれない。属性<att>pattern</att>が定義され、 かつ要素<gi>metSym</gi>が使われている場合には、属性
      <att>pattern</att>中にあるコードは全て記録されるべきである。 </p>
    <p> 当該要素は、韻文モジュールを使う場合にのみ、ヘダー中で使うことがで きる。 </p>
  </remarks>
```

^b53

### Block 54

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#HDMN"/>
    <ptr target="#VEME"/>
  </listRef>
```

^b54

