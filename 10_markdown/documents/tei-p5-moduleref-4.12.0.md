---
type: representation
source-type: document
source: '[[00_sources/tei-p5-moduleref-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 moduleRef
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/moduleRef.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# moduleRef

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 9714. Git blob: `f97c3c6f8a5341148700e25d2e3449c1487a80ce`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" xmlns:sch="http://purl.oclc.org/dsdl/schematron" module="tagdocs" xml:id="MODULEREF" ident="moduleRef">
  <gloss versionDate="2007-07-04" xml:lang="en">module reference</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">모듈 참조</gloss>
  <gloss versionDate="2008-04-06" xml:lang="es">referencia de módulo</gloss>
  <gloss versionDate="2007-06-12" xml:lang="fr">référence de module</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">riferimento al modulo</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">references a module which is to be incorporated into a schema.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">하나의 스키마로 통합된 모듈을 참조한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">參照一個被併入某一模型的模組。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">スキーマに組み入れられるモジュールを参照する。</desc>
  <desc versionDate="2007-06-12" xml:lang="fr">référence un module qui doit être incorporé dans un schéma.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">indica un módulo que se ha de incluir al interno de un esquema.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">indica un modulo da includere all'interno di uno schema.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="model.oddRef"/>
  </classes>
  <content>
    <elementRef key="content" minOccurs="0"/>
  </content>
  <constraintSpec ident="modref" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:moduleRef">
        <sch:report test="* and @key">
          Child elements of &lt;<sch:name/>&gt; are only allowed when an external module is being loaded.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
  <attList>
    <attDef ident="prefix" usage="opt">
      <desc versionDate="2011-09-21" xml:lang="en">specifies a default prefix which will be prepended to all patterns from the imported module.</desc>
      <datatype minOccurs="0" maxOccurs="1"><dataRef key="teidata.xmlName"/></datatype>
      <constraintSpec scheme="schematron" ident="not-same-prefix" xml:lang="en">
        <constraint>
          <sch:rule context="tei:moduleRef">
            <sch:report test="//*[ not( generate-id(.) eq generate-id( current() ) ) ]/@prefix = @prefix">
              The @prefix attribute of &lt;<sch:name/>&gt; should not
              match that of any other element (it would defeat the
              purpose).</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <constraintSpec scheme="schematron" ident="not-except-and-include" xml:lang="en">
        <constraint>
          <sch:rule context="tei:moduleRef">
            <sch:report test="@except and @include">It is an error to supply both the @include and @except attributes.</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
      <remarks ident="moduleRef-attr.prefix-remarks" versionDate="2011-09-21" xml:lang="en">
        <p>Use of this attribute avoids name collisions (and
        thus invalid schemas) when the external schema being
        mixed in with TEI uses a name the TEI or some other
        included external schema already uses for a
        pattern.</p>
      </remarks>
    </attDef>
    <attList org="choice">
      <attDef ident="include">
        <desc versionDate="2011-09-21" xml:lang="en">supplies a list of the elements which are to be copied from the
specified module into the schema being defined.</desc>
        <datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.xmlName"/></datatype>
      </attDef>
      <attDef ident="except">
        <desc versionDate="2011-09-21" xml:lang="en">supplies a list of the elements which are not to be copied from the specified module into the schema being defined.</desc>
        <datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.xmlName"/></datatype>
      </attDef>
    </attList>
    <attList org="choice">
      <attDef ident="key" usage="opt">
        <desc versionDate="2007-01-01" xml:lang="en">the name of a TEI module</desc>
        <desc versionDate="2008-04-06" xml:lang="es">el nombre de un módulo de TEI</desc>
        <desc versionDate="2008-03-30" xml:lang="fr">le nom d'un module TEI.</desc>
        <desc versionDate="2007-11-06" xml:lang="it">nome di un modulo TEI.</desc>
        <datatype><dataRef key="teidata.xmlName"/></datatype>
      </attDef>
      <attDef ident="url" usage="opt">
        <gloss versionDate="2007-01-01" xml:lang="en">uniform resource locator</gloss>
        <gloss versionDate="2008-04-06" xml:lang="es">localizador de recurso uniforme</gloss>
        <gloss versionDate="2008-03-30" xml:lang="fr">URL</gloss>
        <gloss versionDate="2007-11-06" xml:lang="it">URL</gloss>
        <desc versionDate="2007-01-01" xml:lang="en">refers to a non-TEI module of RELAX NG code by external location</desc>
        <desc versionDate="2008-04-06" xml:lang="es">se refiere a un módulo no-de-TEI del código de RELAX NG mediante una localización externa</desc>
        <desc versionDate="2008-03-30" xml:lang="fr">fait référence à un module non TEI de code RELAX NG par une localisation externe.</desc>
        <desc versionDate="2007-11-06" xml:lang="it">indica la collocazione esterna di un modulo non TEI che utilizza il codice RELAX NG.</desc>
        <datatype><dataRef key="teidata.pointer"/></datatype>
      </attDef>
    </attList>
  </attList>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-lm" source="#UND">
      <moduleRef key="linking"/>
    </egXML>
    <p>This includes all objects available  from  the linking module.</p>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-fk" source="#UND">
      <moduleRef key="linking"/>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples"> Cela implante le module<gi> linking </gi>.</p>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-sw" source="#UND">
      <moduleRef key="linking" except="linkGrp link"/>
    </egXML>
    <p>This includes all elements available  from  the linking module
    except for the <gi>link</gi> and <gi>linkGrp</gi> elements.</p>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-tc" source="#UND">
      <moduleRef key="linking" include="linkGrp link"/>
    </egXML>
    <p>This includes only the <gi>link</gi> and <gi>linkGrp</gi>
    elements from the linking module.</p>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-bj" source="#UND">
      <moduleRef key="linking"/>
    </egXML>
  </exemplum>
  <remarks ident="moduleRef-remarks" versionDate="2010-05-09" xml:lang="en">
    <p>If neither <att>include</att> nor <att>except</att> is
    supplied, the effect of this element is to make all the declarations
    contained by the referenced module available to the schema being
    compiled. If both attributes are supplied, an ODD
processor should signal an error. </p>
    <p>A TEI module is identified by the name supplied as value for
    the <att>ident</att> attribute on a <gi>moduleSpec</gi>
    element. The <att>source</att> attribute may be used to specify an
    online source from which the specification of that module may be
    read. A URI may alternatively be supplied in the case of a non-TEI
    module, and this is expected to be written as a RELAX NG schema.
    </p><p>If the <att>url</att> attribute is used, the <gi>content</gi> element may also be supplied as 
    a child of this element. Its content (which is assumed to be a fragment of RELAX NG code) will be copied
    along with the content of the resource indicated by the  <att>url</att> attribute into the 
      target RELAX NG schema. </p>
  </remarks>
  <remarks ident="moduleRef-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les modules sont identifiés par le nom fourni comme valeur de l'attribut
                <att>ident</att> dans l'élément <gi>moduleSpec</gi> où ils sont déclarés. Un URI
                peut aussi être indiqué dans le cas d'un module non TEI et l'on s'attend à ce qu'il
                soit écrit comme un schéma RELAX NG. </p>
    <p>La fonction de cet élément est de rendre toutes les déclarations contenues par le module
                référencé disponibles pour le schéma que l'on compile.</p>
  </remarks>
  <remarks ident="moduleRef-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    モジュールは、要素<gi>module</gi>の属性<att>ident</att>の値として
  ある名前で指定される。TEIでないモジュールの場合は、URIはで示される。
  このモジュールは、Relax NGスキーマで定義されていることが望まれる。
    </p>
    <p>
    当該要素により、参照されたモジュールの全宣言が、当該スキーマにおい
  て使用可能になることでが期待される。
  </p>
  </remarks>
  <listRef>
    <ptr target="#TDmodules"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">module reference</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">모듈 참조</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">referencia de módulo</gloss>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2007-06-12" xml:lang="fr">référence de module</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">riferimento al modulo</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">references a module which is to be incorporated into a schema.</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">하나의 스키마로 통합된 모듈을 참조한다.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">參照一個被併入某一模型的模組。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">スキーマに組み入れられるモジュールを参照する。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-06-12" xml:lang="fr">référence un module qui doit être incorporé dans un schéma.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">indica un módulo que se ha de incluir al interno de un esquema.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">indica un modulo da includere all'interno di uno schema.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="model.oddRef"/>
  </classes>
```

^b13

### Block 14

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <elementRef key="content" minOccurs="0"/>
  </content>
```

^b14

### Block 15

XML location: `/elementSpec[1]/constraintSpec[1]`.

```xml
<constraintSpec ident="modref" scheme="schematron" xml:lang="en">
    <constraint>
      <sch:rule context="tei:moduleRef">
        <sch:report test="* and @key">
          Child elements of &lt;<sch:name/>&gt; are only allowed when an external module is being loaded.
        </sch:report>
      </sch:rule>
    </constraint>
  </constraintSpec>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-09-21" xml:lang="en">specifies a default prefix which will be prepended to all patterns from the imported module.</desc>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="1"><dataRef key="teidata.xmlName"/></datatype>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[1]/constraintSpec[1]`.

```xml
<constraintSpec scheme="schematron" ident="not-same-prefix" xml:lang="en">
        <constraint>
          <sch:rule context="tei:moduleRef">
            <sch:report test="//*[ not( generate-id(.) eq generate-id( current() ) ) ]/@prefix = @prefix">
              The @prefix attribute of &lt;<sch:name/>&gt; should not
              match that of any other element (it would defeat the
              purpose).</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b18

### Block 19

XML location: `/elementSpec[1]/attList[1]/attDef[1]/constraintSpec[2]`.

```xml
<constraintSpec scheme="schematron" ident="not-except-and-include" xml:lang="en">
        <constraint>
          <sch:rule context="tei:moduleRef">
            <sch:report test="@except and @include">It is an error to supply both the @include and @except attributes.</sch:report>
          </sch:rule>
        </constraint>
      </constraintSpec>
```

^b19

### Block 20

XML location: `/elementSpec[1]/attList[1]/attDef[1]/remarks[1]`.

```xml
<remarks ident="moduleRef-attr.prefix-remarks" versionDate="2011-09-21" xml:lang="en">
        <p>Use of this attribute avoids name collisions (and
        thus invalid schemas) when the external schema being
        mixed in with TEI uses a name the TEI or some other
        included external schema already uses for a
        pattern.</p>
      </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2011-09-21" xml:lang="en">supplies a list of the elements which are to be copied from the
specified module into the schema being defined.</desc>
```

^b21

### Block 22

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[1]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.xmlName"/></datatype>
```

^b22

### Block 23

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2011-09-21" xml:lang="en">supplies a list of the elements which are not to be copied from the specified module into the schema being defined.</desc>
```

^b23

### Block 24

XML location: `/elementSpec[1]/attList[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype minOccurs="0" maxOccurs="unbounded"><dataRef key="teidata.xmlName"/></datatype>
```

^b24

### Block 25

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2007-01-01" xml:lang="en">the name of a TEI module</desc>
```

^b25

### Block 26

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[1]/desc[2]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">el nombre de un módulo de TEI</desc>
```

^b26

### Block 27

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[1]/desc[3]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">le nom d'un module TEI.</desc>
```

^b27

### Block 28

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[1]/desc[4]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">nome di un modulo TEI.</desc>
```

^b28

### Block 29

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[1]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.xmlName"/></datatype>
```

^b29

### Block 30

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/gloss[1]`.

```xml
<gloss versionDate="2007-01-01" xml:lang="en">uniform resource locator</gloss>
```

^b30

### Block 31

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/gloss[2]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">localizador de recurso uniforme</gloss>
```

^b31

### Block 32

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/gloss[3]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">URL</gloss>
```

^b32

### Block 33

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/gloss[4]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">URL</gloss>
```

^b33

### Block 34

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2007-01-01" xml:lang="en">refers to a non-TEI module of RELAX NG code by external location</desc>
```

^b34

### Block 35

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/desc[2]`.

```xml
<desc versionDate="2008-04-06" xml:lang="es">se refiere a un módulo no-de-TEI del código de RELAX NG mediante una localización externa</desc>
```

^b35

### Block 36

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/desc[3]`.

```xml
<desc versionDate="2008-03-30" xml:lang="fr">fait référence à un module non TEI de code RELAX NG par une localisation externe.</desc>
```

^b36

### Block 37

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/desc[4]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">indica la collocazione esterna di un modulo non TEI che utilizza il codice RELAX NG.</desc>
```

^b37

### Block 38

XML location: `/elementSpec[1]/attList[1]/attList[2]/attDef[2]/datatype[1]`.

```xml
<datatype><dataRef key="teidata.pointer"/></datatype>
```

^b38

### Block 39

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-lm" source="#UND">
      <moduleRef key="linking"/>
    </egXML>
    <p>This includes all objects available  from  the linking module.</p>
  </exemplum>
```

^b39

### Block 40

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-fk" source="#UND">
      <moduleRef key="linking"/>
    </egXML>
    <p xmlns:teix="http://www.tei-c.org/ns/Examples"> Cela implante le module<gi> linking </gi>.</p>
  </exemplum>
```

^b40

### Block 41

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-sw" source="#UND">
      <moduleRef key="linking" except="linkGrp link"/>
    </egXML>
    <p>This includes all elements available  from  the linking module
    except for the <gi>link</gi> and <gi>linkGrp</gi> elements.</p>
  </exemplum>
```

^b41

### Block 42

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-tc" source="#UND">
      <moduleRef key="linking" include="linkGrp link"/>
    </egXML>
    <p>This includes only the <gi>link</gi> and <gi>linkGrp</gi>
    elements from the linking module.</p>
  </exemplum>
```

^b42

### Block 43

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="MODULEREF-egXML-bj" source="#UND">
      <moduleRef key="linking"/>
    </egXML>
  </exemplum>
```

^b43

### Block 44

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="moduleRef-remarks" versionDate="2010-05-09" xml:lang="en">
    <p>If neither <att>include</att> nor <att>except</att> is
    supplied, the effect of this element is to make all the declarations
    contained by the referenced module available to the schema being
    compiled. If both attributes are supplied, an ODD
processor should signal an error. </p>
    <p>A TEI module is identified by the name supplied as value for
    the <att>ident</att> attribute on a <gi>moduleSpec</gi>
    element. The <att>source</att> attribute may be used to specify an
    online source from which the specification of that module may be
    read. A URI may alternatively be supplied in the case of a non-TEI
    module, and this is expected to be written as a RELAX NG schema.
    </p><p>If the <att>url</att> attribute is used, the <gi>content</gi> element may also be supplied as 
    a child of this element. Its content (which is assumed to be a fragment of RELAX NG code) will be copied
    along with the content of the resource indicated by the  <att>url</att> attribute into the 
      target RELAX NG schema. </p>
  </remarks>
```

^b44

### Block 45

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="moduleRef-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Les modules sont identifiés par le nom fourni comme valeur de l'attribut
                <att>ident</att> dans l'élément <gi>moduleSpec</gi> où ils sont déclarés. Un URI
                peut aussi être indiqué dans le cas d'un module non TEI et l'on s'attend à ce qu'il
                soit écrit comme un schéma RELAX NG. </p>
    <p>La fonction de cet élément est de rendre toutes les déclarations contenues par le module
                référencé disponibles pour le schéma que l'on compile.</p>
  </remarks>
```

^b45

### Block 46

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="moduleRef-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
    モジュールは、要素<gi>module</gi>の属性<att>ident</att>の値として
  ある名前で指定される。TEIでないモジュールの場合は、URIはで示される。
  このモジュールは、Relax NGスキーマで定義されていることが望まれる。
    </p>
    <p>
    当該要素により、参照されたモジュールの全宣言が、当該スキーマにおい
  て使用可能になることでが期待される。
  </p>
  </remarks>
```

^b46

### Block 47

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#TDmodules"/>
  </listRef>
```

^b47

