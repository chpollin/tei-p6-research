---
type: representation
source-type: document
source: '[[00_sources/tei-p5-att.damaged-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 att.damaged
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/att.damaged.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# att.damaged

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12110. Git blob: `dda8e0d1d789c4769d769527b282aad6343fc77b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<classSpec xmlns="http://www.tei-c.org/ns/1.0" module="tei" type="atts" ident="att.damaged">
  <desc versionDate="2007-09-05" xml:lang="en">provides attributes describing the nature of any physical damage affecting a reading.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">독법에 영향을 미치는 물리적 손상의 특성을 기술하는 속성을 제공한다.</desc>
  <desc versionDate="2008-04-21" xml:lang="ja">読みに影響を与える物理的損傷の性格を示す属性を示す。</desc>
  <desc versionDate="2008-04-06" xml:lang="es">proporciona los atributos que describen la naturaleza de
    cualquier daño físico que afecta a una lectura.</desc>
  <desc versionDate="2008-03-30" xml:lang="fr">fournit des attributs décrivant la nature de tout dommage
    physique affectant la lecture.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">fornisce attributi che descrivono la natura di eventuali
    danni fisici che influenzano una lettura</desc>
  <classes>
    
    <memberOf key="att.dimensions"/>
    <memberOf key="att.written"/>
  </classes>
  <attList>
    <attDef ident="agent" usage="opt">
      <desc versionDate="2007-09-03" xml:lang="en">categorizes the cause of the damage, if it can be identified.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">식별될 수 있다면 그 손상의 원인을 분류한다.</desc>
      <desc versionDate="2008-04-21" xml:lang="ja">当該損傷の原因の分類を示す。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">caractérise la raison des dommages, lorsqu'elle peut
        être identifiée.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">classifica la causa del danneggiamento, se
        rintracciabile</desc>
      <desc versionDate="2007-05-04" xml:lang="es">categoriza la causa del daño, si esta puede ser
        identificada.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="rubbing">
          <desc versionDate="2007-09-03" xml:lang="en">damage results from rubbing of the leaf edges</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">손상의 원인이 페이지 모서리의 마모이다.</desc>
          <desc versionDate="2008-04-21" xml:lang="ja">紙の端の擦り切れによる損傷。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le dommage résulte d'un frottement sur les bords
            du feuillet</desc>
          <desc versionDate="2007-11-06" xml:lang="it">dannegiamento per sfregamento dei margini del
            foglio</desc>
          <desc versionDate="2007-05-04" xml:lang="es">el daño se deriva por el roce de los márgenes de
            los folios</desc>
        </valItem>
        <valItem ident="mildew">
          <desc versionDate="2007-09-03" xml:lang="en">damage results from mildew on the leaf surface</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">훼손 원인이 페이지 표면의 곰팡이이다.</desc>
          <desc versionDate="2008-04-21" xml:lang="ja">紙上の白カビによる損傷。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le dommage résulte de moisissure sur la surface
            du feuillet</desc>
          <desc versionDate="2007-11-06" xml:lang="it">danneggiamento per muffa sulla superficie del
            foglio</desc>
          <desc versionDate="2007-05-04" xml:lang="es">daño resultante de la presencia de moho en la
            superficie del folio</desc>
        </valItem>
        <valItem ident="smoke">
          <desc versionDate="2007-09-03" xml:lang="en">damage results from smoke</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">훼손의 원인이 연기이다.</desc>
          <desc versionDate="2008-04-21" xml:lang="ja">煙による損傷。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le dommage résulte de la fumée</desc>
          <desc versionDate="2007-11-06" xml:lang="it">danneggiamento per fumo.</desc>
          <desc versionDate="2007-05-04" xml:lang="es">daños provocados por el humo</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="degree" usage="opt">
      <desc versionDate="2013-11-22" xml:lang="en">provides a coded representation of the degree of damage, either as
 a number between 0 (undamaged) and 1 (very extensively damaged), or
      as one of the codes <val>high</val>, <val>medium</val>, <val>low</val>, 
        or <val>unknown</val>. The <gi>damage</gi> element
        with the <att>degree</att> attribute should only be used where the text may be read with
        some confidence; text supplied from other sources should be tagged as <gi>supplied</gi>.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">다양한 척도에 따라 손상 정도를 나타낸다. <att>degree</att> 속성과 함께
          <gi>damage</gi> 태그는 텍스트가 확인 가능한 곳에서만 사용되어야 한다; 다른 원본에서 가져온 텍스트는 <gi>supplied</gi>를 부착한다.</desc>
      <desc versionDate="2019-01-23" xml:lang="ja">当該損傷部分の程度を0(損傷なし)から1(極度に損傷している)まで間の数値ないし<val>high</val>（強度）、<val>medium</val>（中度）、<val>low</val>（程度）、<val>unknown</val>（未知）のコードによって示す。要素<gi>damage</gi>の属性 <att>degree</att>は、当該損傷部分のテキストが確認できる場合にのみ使用されるべきである。他の資料から補われたテキストの場合には、 要素<gi>supplied</gi>で示されるべきである。</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">indique le degré (la gravité) du dommage subi, selon
        une grille appropriée. L'attribut <att>degree</att> doit être utilisé dans le seul cas où le
        texte peut être lu avec certitude ; le texte restitué en utilisant d'autres sources doit
        être encodé au moyen de l'élément <gi>supplied</gi>.</desc>
      <desc versionDate="2007-01-21" xml:lang="it">indica l'entità del danneggiamento misurato in base a
        una scala funzionale; il marcatore <gi>damage</gi> con l'attributo <att>degree</att>
        dovranno essere utilizzati solo se il testo può essere letto con una certa sicurezza; i
        testi derivanti da altre fonti andranno marcati come <gi>supplied</gi></desc>
      <desc versionDate="2007-05-04" xml:lang="es">&gt;indica el grado del daño medido en base a una
        escala funcional; la etiqueta <gi>damage</gi> (daño) con el atributo <att>degree</att>
        (grado) deberán utilizarse sólo si el texto puede ser leído con una cierta certeza; los
        textos proporcionados por otras fuentes serán etiquetados como <gi>supplied</gi> (suplente)</desc>
      <datatype><dataRef key="teidata.probCert"/></datatype>
      <remarks ident="att.damaged-attr.degree-remarks" versionDate="2013-11-22" xml:lang="en">
        <p>The <gi>damage</gi> element is appropriate where it is
          desired to record the fact of damage although this has not affected the readability of the
          text, for example a weathered inscription. Where the damage has
          rendered the text more or less illegible either the <gi>unclear</gi> tag (for partial
          illegibility) or the <gi>gap</gi> tag (for complete illegibility, with no text supplied)
          should be used, with the information concerning the damage given in the attribute values
          of these tags. See section <ptr target="#PHCOMB"/> for discussion of the use of these tags
          in particular circumstances.</p>
      </remarks>
      <remarks ident="att.damaged-attr.degree-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La balise <gi>damage</gi> avec l'attribut <att>degree</att>ne doit être utilisée qu'à
          l'endroit où le texte peut être lu avec certitude malgré le dommage. Elle convient
          lorsqu'on désire faire état du dommage bien que cela n'affecte en rien la lisibilité du
          texte (comme cela peut être le cas avec des vestiges de matériaux gravés). Là où les
          dommages ont rendu le texte plus ou moins illisible, les balises <gi>unclear</gi> (pour
          l'illisibilité partielle) ou <gi>gap</gi> (pour l'illisibilité complète, sans restitution
          de texte) sont à employer, l'information relative aux dommages étant donnée par les
          valeurs d'attributs de ces balises. Voir <ptr target="#PHCOMB"/> au sujet de l'utilisation
          de ces balises dans des cas particuliers.</p>
      </remarks>
      <remarks ident="att.damaged-attr.degree-remarks" versionDate="2019-01-23" xml:lang="ja">
        <p><gi>damage</gi>要素は、当該テキストの可読性に影響しないが、
          その損傷の程度は記録しておいた方がよいときに適切である(風化した碑文の場合など)。
          当該損傷が、テキストの可読性にある程度影響を与えるような場合には、
          <gi>unclear</gi>タグ(部分的に読めない)や<gi>gap</gi>タグ(完全に読めない)を使用すべきである。
          この場合は、損傷の程度は属性値で示される。特定の場合で、
          これらのタグをどう使用するかについては、 <ptr target="#PHCOMB"/>を参照のこと。</p>
      </remarks>
      <remarks ident="att.damaged-attr.degree-remarks" versionDate="2008-04-06" xml:lang="es">
        <p> La etiqueta <gi>damage</gi> (daño) con el atributo
	<att>degree</att> (grado) debe ser utilizado solamente
          donde el texto se puede leer con certeza a pesar del daño. Es apropiada donde se desee
          registrar el daño, aunque éste no haya afectado a la legibilidad del texto (como puede ser
          el caso de materiales desgastados). Donde el daño ha provocado que el texto sea más o
          menos ilegible conviene usar la etiqueta <gi>unclear</gi> (ilegible) (para la ilegibilidad parcial)
          o la etiqueta <gi>gap</gi> (agujero) (para la ilegibilidad completa, carente del texto
          suministrado), con la información referente al daño en los valores de atributo de estas
          etiquetas. Ver la sección <ptr target="#PHCOMB"/> para la discusión sobre el uso de estas
          etiquetas en circunstancias particulares.</p>
      </remarks>
    </attDef>
    <attDef ident="group" usage="opt">
      <desc versionDate="2007-09-03" xml:lang="en">assigns an arbitrary number to each stretch of damage regarded as forming part of the
        same physical phenomenon.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">동일 물리적 현상의 부분을 형성하는 것으로 간주되는 손상에 대해 각각 임의적 숫자를 할당한다.</desc>
      <desc versionDate="2008-04-21" xml:lang="ja">各損傷部分に、物理的状況を示す、任意の数値を付与する。</desc>
      <desc versionDate="2008-04-06" xml:lang="es">asigna un número arbitrario a cada fragmento del daño
        considerado como parte del mismo fenómeno físico.</desc>
      <desc versionDate="2008-03-30" xml:lang="fr">permet d'assigner un numéro quelconque à chaque
        fragment endommagé considéré comme faisant partie d'un ensemble résultant du même phénomène
        physique</desc>
      <desc versionDate="2007-11-06" xml:lang="it">assegna un numero arbitrario a ognuna delle porzioni
        di danneggiamento considerate parte dello stesso fenomeno fisico</desc>
      <datatype maxOccurs="1"><dataRef key="teidata.count"/></datatype>
    </attDef>
  </attList>
  <listRef>
    <ptr target="#PHDA"/>
    <ptr target="#STECAT"/>
  </listRef>
</classSpec>
```

## Source blocks

### Block 1

XML location: `/classSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-09-05" xml:lang="en">provides attributes describing the nature of any physical damage affecting a reading.</desc>
```

^b1

### Block 2

XML location: `/classSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">독법에 영향을 미치는 물리적 손상의 특성을 기술하는 속성을 제공한다.</desc>
```

^b2

### Block 3

XML location: `/classSpec[1]/desc[3]`.

```xml
<desc versionDate="2008-04-21" xml:lang="ja">読みに影響を与える物理的損傷の性格を示す属性を示す。</desc>
```

^b3

### Block 4

XML location: `/classSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">proporciona los atributos que describen la naturaleza de
    cualquier daño físico que afecta a una lectura.</desc>
```

^b4

### Block 5

XML location: `/classSpec[1]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">fournit des attributs décrivant la nature de tout dommage
    physique affectant la lecture.</desc>
```

^b5

### Block 6

XML location: `/classSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">fornisce attributi che descrivono la natura di eventuali
    danni fisici che influenzano una lettura</desc>
```

^b6

### Block 7

XML location: `/classSpec[1]/classes[1]`.

```xml
<classes>
    
    <memberOf key="att.dimensions"/>
    <memberOf key="att.written"/>
  </classes>
```

^b7

### Block 8

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-09-03" xml:lang="en">categorizes the cause of the damage, if it can be identified.</desc>
```

^b8

### Block 9

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">식별될 수 있다면 그 손상의 원인을 분류한다.</desc>
```

^b9

### Block 10

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-04-21" xml:lang="ja">当該損傷の原因の分類を示す。</desc>
```

^b10

### Block 11

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">caractérise la raison des dommages, lorsqu'elle peut
        être identifiée.</desc>
```

^b11

### Block 12

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">classifica la causa del danneggiamento, se
        rintracciabile</desc>
```

^b12

### Block 13

XML location: `/classSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">categoriza la causa del daño, si esta puede ser
        identificada.</desc>
```

^b13

### Block 14

XML location: `/classSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b14

### Block 15

XML location: `/classSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="rubbing">
          <desc versionDate="2007-09-03" xml:lang="en">damage results from rubbing of the leaf edges</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">손상의 원인이 페이지 모서리의 마모이다.</desc>
          <desc versionDate="2008-04-21" xml:lang="ja">紙の端の擦り切れによる損傷。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le dommage résulte d'un frottement sur les bords
            du feuillet</desc>
          <desc versionDate="2007-11-06" xml:lang="it">dannegiamento per sfregamento dei margini del
            foglio</desc>
          <desc versionDate="2007-05-04" xml:lang="es">el daño se deriva por el roce de los márgenes de
            los folios</desc>
        </valItem>
        <valItem ident="mildew">
          <desc versionDate="2007-09-03" xml:lang="en">damage results from mildew on the leaf surface</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">훼손 원인이 페이지 표면의 곰팡이이다.</desc>
          <desc versionDate="2008-04-21" xml:lang="ja">紙上の白カビによる損傷。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le dommage résulte de moisissure sur la surface
            du feuillet</desc>
          <desc versionDate="2007-11-06" xml:lang="it">danneggiamento per muffa sulla superficie del
            foglio</desc>
          <desc versionDate="2007-05-04" xml:lang="es">daño resultante de la presencia de moho en la
            superficie del folio</desc>
        </valItem>
        <valItem ident="smoke">
          <desc versionDate="2007-09-03" xml:lang="en">damage results from smoke</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">훼손의 원인이 연기이다.</desc>
          <desc versionDate="2008-04-21" xml:lang="ja">煙による損傷。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">le dommage résulte de la fumée</desc>
          <desc versionDate="2007-11-06" xml:lang="it">danneggiamento per fumo.</desc>
          <desc versionDate="2007-05-04" xml:lang="es">daños provocados por el humo</desc>
        </valItem>
      </valList>
```

^b15

### Block 16

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2013-11-22" xml:lang="en">provides a coded representation of the degree of damage, either as
 a number between 0 (undamaged) and 1 (very extensively damaged), or
      as one of the codes <val>high</val>, <val>medium</val>, <val>low</val>, 
        or <val>unknown</val>. The <gi>damage</gi> element
        with the <att>degree</att> attribute should only be used where the text may be read with
        some confidence; text supplied from other sources should be tagged as <gi>supplied</gi>.</desc>
```

^b16

### Block 17

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">다양한 척도에 따라 손상 정도를 나타낸다. <att>degree</att> 속성과 함께
          <gi>damage</gi> 태그는 텍스트가 확인 가능한 곳에서만 사용되어야 한다; 다른 원본에서 가져온 텍스트는 <gi>supplied</gi>를 부착한다.</desc>
```

^b17

### Block 18

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2019-01-23" xml:lang="ja">当該損傷部分の程度を0(損傷なし)から1(極度に損傷している)まで間の数値ないし<val>high</val>（強度）、<val>medium</val>（中度）、<val>low</val>（程度）、<val>unknown</val>（未知）のコードによって示す。要素<gi>damage</gi>の属性 <att>degree</att>は、当該損傷部分のテキストが確認できる場合にのみ使用されるべきである。他の資料から補われたテキストの場合には、 要素<gi>supplied</gi>で示されるべきである。</desc>
```

^b18

### Block 19

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">indique le degré (la gravité) du dommage subi, selon
        une grille appropriée. L'attribut <att>degree</att> doit être utilisé dans le seul cas où le
        texte peut être lu avec certitude ; le texte restitué en utilisant d'autres sources doit
        être encodé au moyen de l'élément <gi>supplied</gi>.</desc>
```

^b19

### Block 20

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica l'entità del danneggiamento misurato in base a
        una scala funzionale; il marcatore <gi>damage</gi> con l'attributo <att>degree</att>
        dovranno essere utilizzati solo se il testo può essere letto con una certa sicurezza; i
        testi derivanti da altre fonti andranno marcati come <gi>supplied</gi></desc>
```

^b20

### Block 21

XML location: `/classSpec[1]/attList[1]/attDef[2]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">&gt;indica el grado del daño medido en base a una
        escala funcional; la etiqueta <gi>damage</gi> (daño) con el atributo <att>degree</att>
        (grado) deberán utilizarse sólo si el texto puede ser leído con una cierta certeza; los
        textos proporcionados por otras fuentes serán etiquetados como <gi>supplied</gi> (suplente)</desc>
```

^b21

### Block 22

XML location: `/classSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.probCert"/></datatype>
```

^b22

### Block 23

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="att.damaged-attr.degree-remarks" versionDate="2013-11-22" xml:lang="en">
        <p>The <gi>damage</gi> element is appropriate where it is
          desired to record the fact of damage although this has not affected the readability of the
          text, for example a weathered inscription. Where the damage has
          rendered the text more or less illegible either the <gi>unclear</gi> tag (for partial
          illegibility) or the <gi>gap</gi> tag (for complete illegibility, with no text supplied)
          should be used, with the information concerning the damage given in the attribute values
          of these tags. See section <ptr target="#PHCOMB"/> for discussion of the use of these tags
          in particular circumstances.</p>
      </remarks>
```

^b23

### Block 24

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[2]`.

```xml
<remarks ident="att.damaged-attr.degree-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>La balise <gi>damage</gi> avec l'attribut <att>degree</att>ne doit être utilisée qu'à
          l'endroit où le texte peut être lu avec certitude malgré le dommage. Elle convient
          lorsqu'on désire faire état du dommage bien que cela n'affecte en rien la lisibilité du
          texte (comme cela peut être le cas avec des vestiges de matériaux gravés). Là où les
          dommages ont rendu le texte plus ou moins illisible, les balises <gi>unclear</gi> (pour
          l'illisibilité partielle) ou <gi>gap</gi> (pour l'illisibilité complète, sans restitution
          de texte) sont à employer, l'information relative aux dommages étant donnée par les
          valeurs d'attributs de ces balises. Voir <ptr target="#PHCOMB"/> au sujet de l'utilisation
          de ces balises dans des cas particuliers.</p>
      </remarks>
```

^b24

### Block 25

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[3]`.

```xml
<remarks ident="att.damaged-attr.degree-remarks" versionDate="2019-01-23" xml:lang="ja">
        <p><gi>damage</gi>要素は、当該テキストの可読性に影響しないが、
          その損傷の程度は記録しておいた方がよいときに適切である(風化した碑文の場合など)。
          当該損傷が、テキストの可読性にある程度影響を与えるような場合には、
          <gi>unclear</gi>タグ(部分的に読めない)や<gi>gap</gi>タグ(完全に読めない)を使用すべきである。
          この場合は、損傷の程度は属性値で示される。特定の場合で、
          これらのタグをどう使用するかについては、 <ptr target="#PHCOMB"/>を参照のこと。</p>
      </remarks>
```

^b25

### Block 26

XML location: `/classSpec[1]/attList[1]/attDef[2]/remarks[4]`.

```xml
<remarks ident="att.damaged-attr.degree-remarks" versionDate="2008-04-06" xml:lang="es">
        <p> La etiqueta <gi>damage</gi> (daño) con el atributo
	<att>degree</att> (grado) debe ser utilizado solamente
          donde el texto se puede leer con certeza a pesar del daño. Es apropiada donde se desee
          registrar el daño, aunque éste no haya afectado a la legibilidad del texto (como puede ser
          el caso de materiales desgastados). Donde el daño ha provocado que el texto sea más o
          menos ilegible conviene usar la etiqueta <gi>unclear</gi> (ilegible) (para la ilegibilidad parcial)
          o la etiqueta <gi>gap</gi> (agujero) (para la ilegibilidad completa, carente del texto
          suministrado), con la información referente al daño en los valores de atributo de estas
          etiquetas. Ver la sección <ptr target="#PHCOMB"/> para la discusión sobre el uso de estas
          etiquetas en circunstancias particulares.</p>
      </remarks>
```

^b26

### Block 27

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[1]`.

```xml
<desc versionDate="2007-09-03" xml:lang="en">assigns an arbitrary number to each stretch of damage regarded as forming part of the
        same physical phenomenon.</desc>
```

^b27

### Block 28

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">동일 물리적 현상의 부분을 형성하는 것으로 간주되는 손상에 대해 각각 임의적 숫자를 할당한다.</desc>
```

^b28

### Block 29

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[3]`.

```xml
<desc versionDate="2008-04-21" xml:lang="ja">各損傷部分に、物理的状況を示す、任意の数値を付与する。</desc>
```

^b29

### Block 30

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[4]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">asigna un número arbitrario a cada fragmento del daño
        considerado como parte del mismo fenómeno físico.</desc>
```

^b30

### Block 31

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[5]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">permet d'assigner un numéro quelconque à chaque
        fragment endommagé considéré comme faisant partie d'un ensemble résultant du même phénomène
        physique</desc>
```

^b31

### Block 32

XML location: `/classSpec[1]/attList[1]/attDef[3]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">assegna un numero arbitrario a ognuna delle porzioni
        di danneggiamento considerate parte dello stesso fenomeno fisico</desc>
```

^b32

### Block 33

XML location: `/classSpec[1]/attList[1]/attDef[3]/datatype[1]`.

```xml
<datatype maxOccurs="1"><dataRef key="teidata.count"/></datatype>
```

^b33

### Block 34

XML location: `/classSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#PHDA"/>
    <ptr target="#STECAT"/>
  </listRef>
```

^b34

