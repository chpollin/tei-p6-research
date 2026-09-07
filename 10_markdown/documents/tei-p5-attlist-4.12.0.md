---
type: representation
source-type: document
source: '[[00_sources/tei-p5-attlist-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 attList
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/attList.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# attList

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 10191. Git blob: `c03465cde81fe112d418a33cacb37751a7e6003b`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="gi-attList" ident="attList">
  <gloss versionDate="2020-12-20" xml:lang="en">attribute list</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">liste d'attributs</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains documentation for all the attributes associated with this element, as a series of <gi>attDef</gi> elements.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">일련의 <gi>attDef</gi> 요소로서, 이 요소와 연관된 모든 속성에 대한 기록을 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含所有和此元素相關的屬性記錄，使用一連串的元素<gi>attDef</gi>。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">当該要素に関する全ての属性に関する文書を、一連の要素<gi>attDef</gi> で示す。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">contient la documentation pour tous les attributs associés à cet élément comme une série d'éléments <gi>attDef</gi>.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene documentación relativa a todos los atributos asociados con este elemento bajo forma de series de elementos attDef.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene la documentazione relativa agli attributi associati all'elemento in questione sotto forma di una serie di elementi attDef.</desc>
  <classes>
    <memberOf key="att.global"/>
    </classes>
  <content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <elementRef key="attRef"/>
      <elementRef key="attDef"/>
      <elementRef key="attList"/>
    </alternate>
  </content>
  <constraintSpec ident="no_duplicate_attrs" scheme="schematron" xml:lang="en">
    <desc>Because it is illegal in XML to have two attributes with the
    same name on the same element instance, it is illegal in TEI to
    have two <gi>attDef</gi> elements with the same values of
    <att>ns</att> and <att>ident</att> in a single <gi>attList</gi>,
    unless the parent <gi>attList</gi> has an <att>org</att> of
    <val>choice</val>. This applies regardless of the <att>mode</att>
    of each <gi>attDef</gi>.</desc>
    <constraint>
      <sch:rule context="tei:attList[ not( ancestor::tei:attList ) ]">
        <!--
            Set up a dummy string that contains at least 1 character that
            is not legal in a URI, and thus cannot be a namespace.
        -->
        <sch:let name="notanamespace" value="'☮🄯'"/>
        <!-- generate a sequence of my <attDef> descendants -->
        <sch:let name="defs" value="descendant::tei:attDef"/>
        <!--
            get a sequence of @ns & @ident combinations of those
            <attDef>s, except ignore those whose parent is an
            <attList> that is an alternation, and for which we have
            already recorded this @ident. Thus if we see
            <attList org="choice">
              <attDef ident="klaatu"/>
              <attDef ident="bodsworth"/>
              <attDef ident="rugglesby"/>
              <attDef ident="klaatu"/>
            </attList>
            The sequence should be ('klaatu','bodsworth','rugglesby','').
        -->
        <sch:let name="nsidents" value="for $ad in $defs return                    if ( $ad[                           parent::tei:attList[ @org eq 'choice']                           and                           preceding-sibling::tei:attDef[                             @ident eq $ad/@ident                             and                             ( @ns, $notanamespace )[1] eq ( $ad/@ns, $notanamespace )[1]                             ]                           ]                       )                    then ''                    else normalize-space( if ($ad/@ns) then 'Q{'||$ad/@ns||'}'||$ad/@ident else $ad/@ident )                  "/>
        <!-- get a sequence of any that occur 2+ times: -->
        <sch:let name="dups" value="for $a in $nsidents return ( $nsidents[ . eq $a ][2] )"/>
        <!-- remove any duplicates from the list of duplicates (-: -->
        <sch:let name="distinct_dups" value="distinct-values( $dups )"/>
        <!--
            if there are any values in list of distinct duplicates (other than null),
            warn user about them:
        -->
        <sch:assert test="count( $distinct_dups[ . ne ''] ) eq 0">
          Within the attribute list defined in "<sch:value-of select="ancestor::*[@ident][1]/@ident"/>",
          the following attributes have been defined multiple times: <sch:value-of select="$distinct_dups"/>.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="org">
      <gloss versionDate="2007-07-04" xml:lang="en">organization</gloss>
      <gloss versionDate="2007-12-20" xml:lang="ko">조직</gloss>
      <gloss versionDate="2008-04-06" xml:lang="es">organización</gloss>
      <gloss versionDate="2007-06-12" xml:lang="fr">conditions d'utilisation</gloss>
      <gloss versionDate="2007-11-06" xml:lang="it">organizzazione</gloss>
      <desc versionDate="2023-02-07" xml:lang="en">specifies whether only one (<val>choice</val>) or all (<val>group</val>) of the attributes in the list are available.</desc>
      <desc versionDate="2007-12-20" xml:lang="ko">목록의 모든 속성이 이용가능하거나(org="group") 그 중 하나만 이용가능한지를 명시한다.</desc>
      <desc versionDate="2007-05-02" xml:lang="zh-TW">標明是否列表中的全部屬性皆可使用 (org="group") 、或是僅可使用其中一個 (org="choice")。</desc>
      <desc versionDate="2008-04-05" xml:lang="ja">リスト中の属性が全て使用できるか(org="group")、またはその1つだけ が使用できるか(org="choice")を示す。</desc>
      <desc versionDate="2007-06-12" xml:lang="fr">précise si les attributs dans la liste sont tous disponibles (org="group") ou seulement l'un d'entre eux (org="choice").</desc>
      <desc versionDate="2023-03-20" xml:lang="es">indica si solo uno (<val>choice</val>) o todos (<val>group</val>) los atributos de la lista están disponibles.</desc>
      <desc versionDate="2023-03-21" xml:lang="it">indica se gli attributi contenuti nella lista sono tutti disponibili (<val>group</val>) o se ne è disponibile solo uno (<val>choice</val>).</desc>
      <datatype><dataRef key="teidata.enumerated"/></datatype>
      <defaultVal>group</defaultVal>
      <valList type="closed">
        <valItem ident="group">
          <desc versionDate="2007-06-27" xml:lang="en">grouped</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">그룹화된</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">集合使用</desc>
          <desc versionDate="2008-04-06" xml:lang="es">agrupado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">全て。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">tous les attributs de la liste sont disponibles.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">raggruppati.</desc>
        </valItem>
        <valItem ident="choice">
          <desc versionDate="2007-06-27" xml:lang="en">alternated</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">교체가능한</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">擇一使用</desc>
          <desc versionDate="2008-04-06" xml:lang="es">alternado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">ひとつを選択。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">un seul des attributs de la liste est disponible.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alternati.</desc>
        </valItem>
      </valList>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attList-egXML-td">
      <attList>
        <attDef ident="type" usage="opt">
          <desc>type of schema</desc>
          <datatype>
            <dataRef key="teidata.enumerated"/>
          </datatype>
        </attDef>
      </attList>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attList-egXML-yz">
      <attList>
        <attDef ident="type" usage="opt">
          <desc>type de schéma</desc>
          <datatype>
            <dataRef key="teidata.enumerated"/>
          </datatype>
        </attDef>
      </attList>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attList-egXML-te">
      <attList>
        <attDef ident="type" usage="opt">
          <desc>文件模型的種類</desc>
          <datatype>
            <dataRef key="teidata.enumerated"/>
          </datatype>
        </attDef>
      </attList>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attList-egXML-gp">
      <attList org="choice">
        <attDef ident="active">
          <desc versionDate="2005-07-24" xml:lang="en">identifies the <soCalled>active</soCalled> participants in a non-mutual relationship, or all the participants in a mutual one.</desc>
          <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
        </attDef>
        <attDef ident="mutual" usage="opt">
          <desc versionDate="2005-07-24" xml:lang="en">supplies a list
            of participants amongst all of whom the relationship holds
            equally.</desc>
          <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
        </attDef>
      </attList>
    </egXML>
  </exemplum>
  <listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TDCLA"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2020-12-20" xml:lang="en">attribute list</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">liste d'attributs</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains documentation for all the attributes associated with this element, as a series of <gi>attDef</gi> elements.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">일련의 <gi>attDef</gi> 요소로서, 이 요소와 연관된 모든 속성에 대한 기록을 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含所有和此元素相關的屬性記錄，使用一連串的元素<gi>attDef</gi>。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">当該要素に関する全ての属性に関する文書を、一連の要素<gi>attDef</gi> で示す。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">contient la documentation pour tous les attributs associés à cet élément comme une série d'éléments <gi>attDef</gi>.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene documentación relativa a todos los atributos asociados con este elemento bajo forma de series de elementos attDef.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene la documentazione relativa agli attributi associati all'elemento in questione sotto forma di una serie di elementi attDef.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <alternate minOccurs="1" maxOccurs="unbounded">
      <elementRef key="attRef"/>
      <elementRef key="attDef"/>
      <elementRef key="attList"/>
    </alternate>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="no_duplicate_attrs" scheme="schematron" xml:lang="en">
    <desc>Because it is illegal in XML to have two attributes with the
    same name on the same element instance, it is illegal in TEI to
    have two <gi>attDef</gi> elements with the same values of
    <att>ns</att> and <att>ident</att> in a single <gi>attList</gi>,
    unless the parent <gi>attList</gi> has an <att>org</att> of
    <val>choice</val>. This applies regardless of the <att>mode</att>
    of each <gi>attDef</gi>.</desc>
    <constraint>
      <sch:rule context="tei:attList[ not( ancestor::tei:attList ) ]">
        <!--
            Set up a dummy string that contains at least 1 character that
            is not legal in a URI, and thus cannot be a namespace.
        -->
        <sch:let name="notanamespace" value="'☮🄯'"/>
        <!-- generate a sequence of my <attDef> descendants -->
        <sch:let name="defs" value="descendant::tei:attDef"/>
        <!--
            get a sequence of @ns & @ident combinations of those
            <attDef>s, except ignore those whose parent is an
            <attList> that is an alternation, and for which we have
            already recorded this @ident. Thus if we see
            <attList org="choice">
              <attDef ident="klaatu"/>
              <attDef ident="bodsworth"/>
              <attDef ident="rugglesby"/>
              <attDef ident="klaatu"/>
            </attList>
            The sequence should be ('klaatu','bodsworth','rugglesby','').
        -->
        <sch:let name="nsidents" value="for $ad in $defs return                    if ( $ad[                           parent::tei:attList[ @org eq 'choice']                           and                           preceding-sibling::tei:attDef[                             @ident eq $ad/@ident                             and                             ( @ns, $notanamespace )[1] eq ( $ad/@ns, $notanamespace )[1]                             ]                           ]                       )                    then ''                    else normalize-space( if ($ad/@ns) then 'Q{'||$ad/@ns||'}'||$ad/@ident else $ad/@ident )                  "/>
        <!-- get a sequence of any that occur 2+ times: -->
        <sch:let name="dups" value="for $a in $nsidents return ( $nsidents[ . eq $a ][2] )"/>
        <!-- remove any duplicates from the list of duplicates (-: -->
        <sch:let name="distinct_dups" value="distinct-values( $dups )"/>
        <!--
            if there are any values in list of distinct duplicates (other than null),
            warn user about them:
        -->
        <sch:assert test="count( $distinct_dups[ . ne ''] ) eq 0">
          Within the attribute list defined in "<sch:value-of select="ancestor::*[@ident][1]/@ident"/>",
          the following attributes have been defined multiple times: <sch:value-of select="$distinct_dups"/>.
        </sch:assert>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">organization</gloss>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">조직</gloss>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">organización</gloss>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">conditions d'utilisation</gloss>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">organizzazione</gloss>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2023-02-07" xml:lang="en">specifies whether only one (<val>choice</val>) or all (<val>group</val>) of the attributes in the list are available.</desc>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">목록의 모든 속성이 이용가능하거나(org="group") 그 중 하나만 이용가능한지를 명시한다.</desc>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">標明是否列表中的全部屬性皆可使用 (org="group") 、或是僅可使用其中一個 (org="choice")。</desc>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">リスト中の属性が全て使用できるか(org="group")、またはその1つだけ が使用できるか(org="choice")を示す。</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">précise si les attributs dans la liste sont tous disponibles (org="group") ou seulement l'un d'entre eux (org="choice").</desc>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[6]`.

```xml
<desc versionDate="2023-03-20" xml:lang="es">indica si solo uno (<val>choice</val>) o todos (<val>group</val>) los atributos de la lista están disponibles.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[7]`.

```xml
<desc versionDate="2023-03-21" xml:lang="it">indica se gli attributi contenuti nella lista sono tutti disponibili (<val>group</val>) o se ne è disponibile solo uno (<val>choice</val>).</desc>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.enumerated"/></datatype>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attDef[1]/defaultVal[1]`.

```xml
<defaultVal>group</defaultVal>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="closed">
        <valItem ident="group">
          <desc versionDate="2007-06-27" xml:lang="en">grouped</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">그룹화된</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">集合使用</desc>
          <desc versionDate="2008-04-06" xml:lang="es">agrupado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">全て。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">tous les attributs de la liste sont disponibles.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">raggruppati.</desc>
        </valItem>
        <valItem ident="choice">
          <desc versionDate="2007-06-27" xml:lang="en">alternated</desc>
          <desc versionDate="2007-12-20" xml:lang="ko">교체가능한</desc>
          <desc versionDate="2007-05-02" xml:lang="zh-TW">擇一使用</desc>
          <desc versionDate="2008-04-06" xml:lang="es">alternado</desc>
          <desc versionDate="2008-04-05" xml:lang="ja">ひとつを選択。</desc>
          <desc versionDate="2008-03-30" xml:lang="fr">un seul des attributs de la liste est disponible.</desc>
          <desc versionDate="2007-01-21" xml:lang="it">alternati.</desc>
        </valItem>
      </valList>
```

^b27

### Block 28

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attList-egXML-td">
      <attList>
        <attDef ident="type" usage="opt">
          <desc>type of schema</desc>
          <datatype>
            <dataRef key="teidata.enumerated"/>
          </datatype>
        </attDef>
      </attList>
    </egXML>
  </exemplum>
```

^b28

### Block 29

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attList-egXML-yz">
      <attList>
        <attDef ident="type" usage="opt">
          <desc>type de schéma</desc>
          <datatype>
            <dataRef key="teidata.enumerated"/>
          </datatype>
        </attDef>
      </attList>
    </egXML>
  </exemplum>
```

^b29

### Block 30

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attList-egXML-te">
      <attList>
        <attDef ident="type" usage="opt">
          <desc>文件模型的種類</desc>
          <datatype>
            <dataRef key="teidata.enumerated"/>
          </datatype>
        </attDef>
      </attList>
    </egXML>
  </exemplum>
```

^b30

### Block 31

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-attList-egXML-gp">
      <attList org="choice">
        <attDef ident="active">
          <desc versionDate="2005-07-24" xml:lang="en">identifies the <soCalled>active</soCalled> participants in a non-mutual relationship, or all the participants in a mutual one.</desc>
          <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
        </attDef>
        <attDef ident="mutual" usage="opt">
          <desc versionDate="2005-07-24" xml:lang="en">supplies a list
            of participants amongst all of whom the relationship holds
            equally.</desc>
          <datatype maxOccurs="unbounded"><dataRef key="teidata.pointer"/></datatype>
        </attDef>
      </attList>
    </egXML>
  </exemplum>
```

^b31

### Block 32

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDTAG"/>
    <ptr target="#TDCLA"/>
  </listRef>
```

^b32

