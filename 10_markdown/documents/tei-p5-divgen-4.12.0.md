---
type: representation
source-type: document
source: '[[00_sources/tei-p5-divgen-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 divGen
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/divGen.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# divGen

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 12694. Git blob: `880fa61ad7303fcf60ed3e302f37f342e62b21c3`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-divGen" ident="divGen">
  <gloss versionDate="2005-01-14" xml:lang="en">automatically generated text division</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">자동적으로 생성된 텍스트 구역</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW">自動產生的文字區段</gloss>
  <gloss versionDate="2009-01-06" xml:lang="fr">division de texte générée automatiquement</gloss>
  <gloss versionDate="2007-05-04" xml:lang="es">división de texto generada automáticamente</gloss>
  <gloss versionDate="2007-01-21" xml:lang="it">partizione testuale generata automaticamente</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">indicates the location at which a textual division generated
        automatically by a text-processing application is to appear.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">텍스트 처리 애플리케이션에 의해 자동적으로 생성된 텍스트 구역이 나타나는 위치를 표시한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">指出文件處理軟體運作下自動產生的文字區段所出現的位置。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">ソフトウェアで自動生成されたテキスト部分の場所を示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">indique l'emplacement où doit apparaître une
        division du texte générée automatiquement par une application de traitement de
        texte.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica la localización en la cual aparece una división textual generada automáticamente por la aplicación  de un procesamiento de texto.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica la posizione in cui deve apparire una partizione testuale generata automaticamente da un'applicazione che elabora testi.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divGenLike"/>
    <memberOf key="model.frontPart"/>
  </classes>
  <content>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
  <attList>
    <attDef ident="type" usage="opt" mode="change">
      <desc versionDate="2005-01-14" xml:lang="en">specifies what type of generated text division (e.g. index,
                table of contents, etc.) is to appear.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">생성된 텍스트 구역의 유형(예, 색인, 목차 등)을 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">具體指明何種文字區段 (如索引、目錄等) 會出現。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">生成されたテキスト部分の種類を示す。例えば、索引、目次など。</desc>
      <desc versionDate="2009-01-06" xml:lang="fr">précise le type de section de
                texte qui apparaîtra par génération automatique (par exemple :  index,
                table des matières, etc.)</desc>
      <desc versionDate="2007-05-04" xml:lang="es">especifica que tipo de divisón de texto generada aparece (p.ej. índice, tabla de contenidos, etc.)</desc>
      <desc versionDate="2007-01-21" xml:lang="it">specifica quale tipo di partizione testuale generata (ad esempio indice, sommario, ecc.) apparirà.</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="index">
          <desc versionDate="2007-06-27" xml:lang="en">an index is to be generated and inserted at this point.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">색인은 이 지점에서 생성되고 삽입된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">索引會產生並置入於此處</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se debe generar e insertar un índice en este punto.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該の場所に生成された索引。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">un index doit être généré et inséré à
                        cet endroit.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un indice sarà generato e inserito in questo punto.</desc>
        </valItem>
        <valItem ident="toc">
          <desc versionDate="2007-06-27" xml:lang="en">a table of contents</desc>
          <desc versionDate="2018-09-08" xml:lang="es">una tabla de contenidos.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">목차</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">目錄</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">目次。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">une table des matières</desc>
          <desc versionDate="2007-01-21" xml:lang="it">sommario.</desc>
        </valItem>
        <valItem ident="figlist">
          <desc versionDate="2007-06-27" xml:lang="en">a list of figures</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">그림 목록</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">圖表列表</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una lista de figuras</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">図目次。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">une liste des figures</desc>
          <desc versionDate="2007-01-21" xml:lang="it">una lista di immagini.</desc>
        </valItem>
        <valItem ident="tablist">
          <desc versionDate="2007-06-27" xml:lang="en">a list of tables</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표 목록</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">表格列表</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una lista de tablas</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">表目次。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">une liste des tableaux</desc>
          <desc versionDate="2007-01-21" xml:lang="it">una lista di tabelle.</desc>
        </valItem>
      </valList>
      <remarks ident="divGen-attr.type-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>Valid values are application-dependent; those shown are of
                    obvious utility in document production, but are by no means
                    exhaustive.</p>
      </remarks>
      <remarks ident="divGen-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Les valeurs de cet attribut dépendent de l'application utilisée ; celles qui
                    sont données ci-dessus sont utiles dans le processus de production du
                    document XML, mais leur liste n'est en aucun cas exhaustive.</p>
      </remarks>
      <remarks ident="divGen-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
                    
                    妥当な値はソフトウェアにより異なる。上記に示された値は、一般的
                    なもので、これで全てではない。
                </p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <p>One use for this element is to allow document preparation
            software to generate an index and insert it in the appropriate place in
            the output.  The example below assumes that the <att>indexName</att>            
            attribute on <gi>index</gi> elements in the text has been used to specify index
            entries for the two generated indexes, named NAMES and THINGS:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-vb">
      <back>
        <div1 type="backmat">
          <head>Bibliography</head>
          <!-- ... -->
        </div1>
        <div1 type="backmat">
          <head>Indices</head>
          <divGen n="Index Nominum" type="NAMES"/>
          <divGen n="Index Rerum" type="THINGS"/>
        </div1>
      </back>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Une utilisation de cet élément est de permettre au logiciel de traiter des documents afin
        de générer en sortie un index et de l' insérer à l'endroit approprié. L'exemple ci-dessous
        suppose que l'attribut <att>indexName</att> sur les éléments <gi>index</gi> dans le texte a
        été employé pour spécifier des entrées d'index pour deux index produits, nommés NAMES and
        THINGS:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-ja">
      <back>
        <div1 type="backmat">
          <head>Bibliographie</head>
          <!-- ... -->
        </div1>
        <div1 type="backmat">
          <head>Indices</head>
          <divGen n="Index Nominum" type="NAMES"/>
          <divGen n="Index Rerum" type="THINGS"/>
        </div1>
      </back>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Un autre usage de <gi>divGen</gi> est de spécifier l'emplacement d'une table des matières
        automatiquement produite.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-ge">
      <front>
        <divGen type="toc"/>
        <div>
          <head>Préface</head>
          <p> ... </p>
        </div>
      </front>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-fs">
      <back>
        <div1 type="backmat">
          <head>參考書目</head>
          <!-- ... -->
        </div1>
        <div1 type="backmat">
          <head>索引</head>
          <divGen n="Index Nominum" type="人名"/>
          <divGen n="Index Rerum" type="事物"/>
        </div1>
      </back>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-fu">
      <front>
        <!--<titlePage>書名頁</titlePage>-->
        <divGen type="toc"/>
        <div>
          <head>序</head>
          <p> ... </p>
        </div>
      </front>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>Another use for <gi>divGen</gi> is to specify the
            location of an automatically produced table of contents:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-eb">
      <front>
        <!--<titlePage>...</titlePage>-->
        <divGen type="toc"/>
        <div>
          <head>Preface</head>
          <p> ... </p>
        </div>
      </front>
    </egXML>
  </exemplum>
  <remarks ident="divGen-remarks" versionDate="2005-06-24" xml:lang="en">
    <p>This element is intended primarily for use in document
            production or manipulation, rather than in the transcription of
            pre-existing materials; it makes it easier to specify the location of
            indices, tables of contents, etc., to be generated by text preparation
            or word processing software.<!-- The <att>n</att> attribute should be used
                to give a title for the text division being generated-->
        </p>
  </remarks>
  <remarks ident="divGen-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément  est  plutôt  utilisé  pendant la production ou la manipulation du document
            TEI, que dans le processus de transcription de documents préexistants ; il
            permet de spécifier à quel endroit du document les index, tables des matières, etc.,
            devront être générés par programme.</p>
  </remarks>
  <remarks ident="divGen-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
            当該要素は、ソフトウェアによる文書処理を想定したもので、既存資料か
            らの転記における利用を想定したものではない。当該要素により、ソフトウェ
            アにより生成された索引、目次などの場所を指定することが容易になる。
            <!-- The <att>n</att> attribute should be used
                to give a title for the text division being generated-->
        </p>
  </remarks>
  <listRef>
    <ptr target="#CONOIX" type="div3"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2005-01-14" xml:lang="en">automatically generated text division</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">자동적으로 생성된 텍스트 구역</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW">自動產生的文字區段</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2009-01-06" xml:lang="fr">division de texte générée automatiquement</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-05-04" xml:lang="es">división de texto generada automáticamente</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-01-21" xml:lang="it">partizione testuale generata automaticamente</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">indicates the location at which a textual division generated
        automatically by a text-processing application is to appear.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">텍스트 처리 애플리케이션에 의해 자동적으로 생성된 텍스트 구역이 나타나는 위치를 표시한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">指出文件處理軟體運作下自動產生的文字區段所出現的位置。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">ソフトウェアで自動生成されたテキスト部分の場所を示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">indique l'emplacement où doit apparaître une
        division du texte générée automatiquement par une application de traitement de
        texte.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica la localización en la cual aparece una división textual generada automáticamente por la aplicación  de un procesamiento de texto.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica la posizione in cui deve apparire una partizione testuale generata automaticamente da un'applicazione che elabora testi.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.divGenLike"/>
    <memberOf key="model.frontPart"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
      <classRef key="model.headLike" minOccurs="0" maxOccurs="unbounded"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">specifies what type of generated text division (e.g. index,
                table of contents, etc.) is to appear.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">생성된 텍스트 구역의 유형(예, 색인, 목차 등)을 명시한다.</desc>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">具體指明何種文字區段 (如索引、目錄等) 會出現。</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">生成されたテキスト部分の種類を示す。例えば、索引、目次など。</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">précise le type de section de
                texte qui apparaîtra par génération automatique (par exemple :  index,
                table des matières, etc.)</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">especifica que tipo de divisón de texto generada aparece (p.ej. índice, tabla de contenidos, etc.)</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">specifica quale tipo di partizione testuale generata (ad esempio indice, sommario, ecc.) apparirà.</desc>
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
        <valItem ident="index">
          <desc versionDate="2007-06-27" xml:lang="en">an index is to be generated and inserted at this point.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">색인은 이 지점에서 생성되고 삽입된다.</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">索引會產生並置入於此處</desc>
          <desc versionDate="2008-04-06" xml:lang="es">se debe generar e insertar un índice en este punto.</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">当該の場所に生成された索引。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">un index doit être généré et inséré à
                        cet endroit.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">un indice sarà generato e inserito in questo punto.</desc>
        </valItem>
        <valItem ident="toc">
          <desc versionDate="2007-06-27" xml:lang="en">a table of contents</desc>
          <desc versionDate="2018-09-08" xml:lang="es">una tabla de contenidos.</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">목차</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">目錄</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">目次。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">une table des matières</desc>
          <desc versionDate="2007-01-21" xml:lang="it">sommario.</desc>
        </valItem>
        <valItem ident="figlist">
          <desc versionDate="2007-06-27" xml:lang="en">a list of figures</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">그림 목록</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">圖表列表</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una lista de figuras</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">図目次。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">une liste des figures</desc>
          <desc versionDate="2007-01-21" xml:lang="it">una lista di immagini.</desc>
        </valItem>
        <valItem ident="tablist">
          <desc versionDate="2007-06-27" xml:lang="en">a list of tables</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">표 목록</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">表格列表</desc>
          <desc versionDate="2008-04-06" xml:lang="es">una lista de tablas</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">表目次。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">une liste des tableaux</desc>
          <desc versionDate="2007-01-21" xml:lang="it">una lista di tabelle.</desc>
        </valItem>
      </valList>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="divGen-attr.type-remarks" versionDate="2005-01-14" xml:lang="en">
        <p>Valid values are application-dependent; those shown are of
                    obvious utility in document production, but are by no means
                    exhaustive.</p>
      </remarks>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[2]`.

```xml
<remarks ident="divGen-attr.type-remarks" versionDate="2007-06-12" xml:lang="fr">
        <p>Les valeurs de cet attribut dépendent de l'application utilisée ; celles qui
                    sont données ci-dessus sont utiles dans le processus de production du
                    document XML, mais leur liste n'est en aucun cas exhaustive.</p>
      </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[3]`.

```xml
<remarks ident="divGen-attr.type-remarks" versionDate="2008-04-05" xml:lang="ja">
        <p>
                    
                    妥当な値はソフトウェアにより異なる。上記に示された値は、一般的
                    なもので、これで全てではない。
                </p>
      </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>One use for this element is to allow document preparation
            software to generate an index and insert it in the appropriate place in
            the output.  The example below assumes that the <att>indexName</att>            
            attribute on <gi>index</gi> elements in the text has been used to specify index
            entries for the two generated indexes, named NAMES and THINGS:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-vb">
      <back>
        <div1 type="backmat">
          <head>Bibliography</head>
          <!-- ... -->
        </div1>
        <div1 type="backmat">
          <head>Indices</head>
          <divGen n="Index Nominum" type="NAMES"/>
          <divGen n="Index Rerum" type="THINGS"/>
        </div1>
      </back>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Une utilisation de cet élément est de permettre au logiciel de traiter des documents afin
        de générer en sortie un index et de l' insérer à l'endroit approprié. L'exemple ci-dessous
        suppose que l'attribut <att>indexName</att> sur les éléments <gi>index</gi> dans le texte a
        été employé pour spécifier des entrées d'index pour deux index produits, nommés NAMES and
        THINGS:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-ja">
      <back>
        <div1 type="backmat">
          <head>Bibliographie</head>
          <!-- ... -->
        </div1>
        <div1 type="backmat">
          <head>Indices</head>
          <divGen n="Index Nominum" type="NAMES"/>
          <divGen n="Index Rerum" type="THINGS"/>
        </div1>
      </back>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <p xmlns:teix="http://www.tei-c.org/ns/Examples">Un autre usage de <gi>divGen</gi> est de spécifier l'emplacement d'une table des matières
        automatiquement produite.</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-ge">
      <front>
        <divGen type="toc"/>
        <div>
          <head>Préface</head>
          <p> ... </p>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-fs">
      <back>
        <div1 type="backmat">
          <head>參考書目</head>
          <!-- ... -->
        </div1>
        <div1 type="backmat">
          <head>索引</head>
          <divGen n="Index Nominum" type="人名"/>
          <divGen n="Index Rerum" type="事物"/>
        </div1>
      </back>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-fu">
      <front>
        <!--<titlePage>書名頁</titlePage>-->
        <divGen type="toc"/>
        <div>
          <head>序</head>
          <p> ... </p>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b32

### Block 33

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <p>Another use for <gi>divGen</gi> is to specify the
            location of an automatically produced table of contents:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-divGen-egXML-eb">
      <front>
        <!--<titlePage>...</titlePage>-->
        <divGen type="toc"/>
        <div>
          <head>Preface</head>
          <p> ... </p>
        </div>
      </front>
    </egXML>
  </exemplum>
```

^b33

### Block 34

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="divGen-remarks" versionDate="2005-06-24" xml:lang="en">
    <p>This element is intended primarily for use in document
            production or manipulation, rather than in the transcription of
            pre-existing materials; it makes it easier to specify the location of
            indices, tables of contents, etc., to be generated by text preparation
            or word processing software.<!-- The <att>n</att> attribute should be used
                to give a title for the text division being generated-->
        </p>
  </remarks>
```

^b34

### Block 35

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="divGen-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Cet élément  est  plutôt  utilisé  pendant la production ou la manipulation du document
            TEI, que dans le processus de transcription de documents préexistants ; il
            permet de spécifier à quel endroit du document les index, tables des matières, etc.,
            devront être générés par programme.</p>
  </remarks>
```

^b35

### Block 36

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="divGen-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
            当該要素は、ソフトウェアによる文書処理を想定したもので、既存資料か
            らの転記における利用を想定したものではない。当該要素により、ソフトウェ
            アにより生成された索引、目次などの場所を指定することが容易になる。
            <!-- The <att>n</att> attribute should be used
                to give a title for the text division being generated-->
        </p>
  </remarks>
```

^b36

### Block 37

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONOIX" type="div3"/>
  </listRef>
```

^b37

