---
type: representation
source-type: document
source: '[[00_sources/tei-p5-address-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 address
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/address.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# address

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 11359. Git blob: `372e0410c7df77f0db6dab286c84b95990cf5686`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-address" ident="address">
  <gloss versionDate="2016-11-24" xml:lang="en">address</gloss>
  <gloss versionDate="2016-11-24" xml:lang="de">Adresse</gloss>
  <desc versionDate="2007-02-15" xml:lang="en">contains a postal address, for example of a publisher, an organization, or an individual.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 출판사, 기관, 개인의 우편 주소를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含出版者、機構、或是個人的郵寄地址或其他地址。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">郵便配達情報を示す。例えば、出版者、組織、個人の住所など。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une adresse postale ou d'un autre type, par exemple l'adresse d'un éditeur, d'un organisme ou d'une personne.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una dirección postal, por ejemplo de un editor, una institución, etc.</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene un indirizzo (postale), ad esempio di un editore, di un'organizzazione, di un individuo.</desc>
  <desc versionDate="2016-11-24" xml:lang="de">enthält eine Postadresse, z. B. eines Verlegers, einer Organisation oder einer Einzelperson.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.addressLike"/>
    <memberOf key="model.divBottomPart"/>
    <memberOf key="model.divTopPart"/>
    <memberOf key="model.publicationStmtPart.detail"/>
  </classes>
  <content>
    <sequence>
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.addrPart"/>
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
  <attList>
    <attDef ident="type" mode="change">
      <desc versionDate="2026-01-13" xml:lang="en">characterizes the
      address in some sense, using any convenient classification
      scheme or typology.</desc>
      <valList type="semi">
        <!-- This list is probably somewhat US-centric; updates welcome. -->
        <valItem ident="billing">
          <desc versionDate="2026-01-13" xml:lang="en">the address to
          which a bill for goods or services should be sent.</desc>
        </valItem>
        <valItem ident="delivery">
          <desc versionDate="2026-01-13" xml:lang="en">the address to
          which packages should be sent via a private delivery service.</desc>
        </valItem>
        <valItem ident="mailing">
          <desc versionDate="2026-01-13" xml:lang="en">the address to
          which mail should be sent via a public postal service.</desc>
        </valItem>
        <valItem ident="military">
          <desc versionDate="2026-01-15" xml:lang="en">the address to
          which mail to deployed military personnel should be sent.</desc>
        </valItem>
        <valItem ident="physical">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          a building irrespective of where mail to its occupants
          should be sent (for example, for the fire
          department).</desc>
        </valItem>
      </valList>
    </attDef>
    <attDef ident="role" usage="opt">
      <desc versionDate="2026-01-02" xml:lang="en">specifies further information about the purpose of the address.</desc>
      <datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
      <valList type="open">
        <valItem ident="sender">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          the sender of a piece of correspondence.</desc>
        </valItem>
        <valItem ident="return">
          <desc versionDate="2026-01-13" xml:lang="en">the address to
          which undeliverable mail should be returned.</desc>
        </valItem>
        <valItem ident="recipient ">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          the intended recipient of a piece of correspondence.</desc>
        </valItem>
        <valItem ident="work">
          <desc versionDate="2026-01-15" xml:lang="en">the address to
          which work-related mail should be sent, typically that of
          the recipient’s employer.</desc>
        </valItem>
        <valItem ident="home">
          <desc versionDate="2026-01-15" xml:lang="en">the address to
          which non-work-related mail should be sent, typically the
          domicile of the recipient.</desc>
        </valItem>
        <valItem ident="start">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          the beginning of a route, for example of a race.</desc>
        </valItem>
        <valItem ident="finish">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          the end of a route, for example of a race.</desc>
        </valItem>
        <valItem ident="pickup">
          <desc versionDate="2026-01-13" xml:lang="en">the address at
          which a person or package is picked up, for example by a
          taxi or delivery service.</desc>
        </valItem>
        <valItem ident="dropOff">
          <desc versionDate="2026-01-13" xml:lang="en">the address at
          which a person or package is dropped off, for example by a
          taxi or delivery service.</desc>
        </valItem>
      </valList>
      <remarks ident="address-attr.role-remarks" xml:lang="en" versionDate="2026-02-16">
        <p>Whereas <att>type</att> is used to differentiate the kind
        of address (e.g. a street address vs. a post office box, or a
        physical address vs. a mailing address), <att>role</att> is
        used to differentiate the purpose of the address, for example
        within a correspondence ecosystem (e.g. the address of the
        sender vs. that of the intended recipient, or a college
        student's permanent address vs. address while at school).</p>
      </remarks>
    </attDef>
  </attList>
  <exemplum xml:lang="en">
    <p>Using just the elements defined by the core module, an address could be represented as follows:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-rj" source="#NONE">
      <address>
        <street>via Marsala 24</street>
        <postCode>40126</postCode>
        <name>Bologna</name>
        <name>Italy</name>
      </address>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>When a schema includes the names and dates module more specific elements such as country or settlement would be preferable over generic <gi>name</gi>:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-ua" source="#NONE">
      <address>
        <street>via Marsala 24</street>
        <postCode>40126</postCode>
        <settlement>Bologna</settlement>
        <country>Italy</country>
      </address>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-tn" source="#NONE">
      <address>
        <addrLine>Centre d'Études Supérieures de la Renaissance</addrLine>
        <addrLine>59, rue Néricault-Destouches</addrLine>
        <addrLine> 37013 TOURS</addrLine>
        <addrLine>France</addrLine>
      </address>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-kz" source="#NONE">
      <address>
        <street>邯郸路220号</street>
        <postCode>200433</postCode>
        <name>上海市</name>
        <name n="I">中華人民共和國</name>
      </address>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-ln" source="#NONE">
      <address>
        <addrLine>沙田</addrLine>
        <addrLine>新界</addrLine>
        <addrLine>香港特別行政區</addrLine>
        <addrLine>中華人民共和國</addrLine>
      </address>
    </egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-hr" source="#NONE">
      <address>
        <addrLine>Computing Center, MC 135</addrLine>
        <addrLine>P.O. Box 6998</addrLine>
        <addrLine>Chicago, IL 60680</addrLine>
        <addrLine>USA</addrLine>
      </address>
    </egXML>
  </exemplum>
  <exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-zn" source="#NONE">
      <address>
        <country key="FR"/>
        <settlement type="city">Lyon</settlement>
        <postCode>69002</postCode>
        <district type="arrondissement">IIème</district>
        <district type="quartier">Perrache</district>
        <street><num>30</num>, Cours de Verdun</street>
      </address>
    </egXML>
  </exemplum>
  <remarks ident="address-remarks" versionDate="2007-12-16" xml:lang="en">
    <p rend="dataDesc">This element should be used for postal
    addresses only. Within it, the generic element <gi>addrLine</gi>
    may be used as an alternative to any of the more specialized
    elements available from the <ident type="class">model.addrPart</ident> class, such as
    <gi>street</gi>, <gi>postCode</gi> etc.</p>
  </remarks>
  <remarks ident="address-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Cet élément ne doit être utilisé que pour
    donner une adresse postale. A l'intérieur de cet élément,
    l'élément générique <gi>addrLine</gi> peut être utilisé comme
    élément alternatif aux éléments plus spécialisés de la classe
    <ident type="class">model.addrPart</ident> class, tels que
    <gi>street</gi>, <gi>postCode</gi> etc.</p>
  </remarks>
  <remarks ident="address-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 当該要素は、郵便配達情報にのみ使用されるべきで
    ある。 子要素として要素<gi>addrLine</gi>は、クラスmodel.addrPartに
    ある要 素の代わりとして、例えば、要素<gi>street</gi>や要素
    <gi>postcode</gi>として使用することができる。 </p>
  </remarks>
  <remarks ident="address-remarks" versionDate="2016-11-24" xml:lang="de">
    <p rend="dataDesc">Dieses Element sollte ausschließlich für
    postalische Addressen verwendet werden. Innerhalb des Elements
    kann das generische <gi>addrLine</gi>-Element als Alternative zu
    den spezielleren Elementen aus der <ident type="class">model.addrPart</ident>-Klasse, wie <gi>street</gi>
    (Straße), <gi>postCode</gi> (Postleitzahl), etc. verwendet
    werden.</p>
  </remarks>
  <listRef>
    <ptr target="#CONAAD"/>
    <ptr target="#HD24"/>
    <ptr target="#COBICOI"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="en">address</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2016-11-24" xml:lang="de">Adresse</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-02-15" xml:lang="en">contains a postal address, for example of a publisher, an organization, or an individual.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">예를 들어, 출판사, 기관, 개인의 우편 주소를 포함한다.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含出版者、機構、或是個人的郵寄地址或其他地址。</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">郵便配達情報を示す。例えば、出版者、組織、個人の住所など。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une adresse postale ou d'un autre type, par exemple l'adresse d'un éditeur, d'un organisme ou d'une personne.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una dirección postal, por ejemplo de un editor, una institución, etc.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene un indirizzo (postale), ad esempio di un editore, di un'organizzazione, di un individuo.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[8]`.

```xml
<desc versionDate="2016-11-24" xml:lang="de">enthält eine Postadresse, z. B. eines Verlegers, einer Organisation oder einer Einzelperson.</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.canonical"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.typed"/>
    <memberOf key="model.addressLike"/>
    <memberOf key="model.divBottomPart"/>
    <memberOf key="model.divTopPart"/>
    <memberOf key="model.publicationStmtPart.detail"/>
  </classes>
```

^b11

### Block 12

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <sequence>
      <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      <sequence minOccurs="1" maxOccurs="unbounded">
        <classRef key="model.addrPart"/>
        <classRef key="model.global" minOccurs="0" maxOccurs="unbounded"/>
      </sequence>
    </sequence>
  </content>
```

^b12

### Block 13

XML location: `/elementSpec[1]/attList[1]/attDef[1]/desc[1]`.

```xml
<desc versionDate="2026-01-13" xml:lang="en">characterizes the
      address in some sense, using any convenient classification
      scheme or typology.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/attList[1]/attDef[1]/valList[1]`.

```xml
<valList type="semi">
        <!-- This list is probably somewhat US-centric; updates welcome. -->
        <valItem ident="billing">
          <desc versionDate="2026-01-13" xml:lang="en">the address to
          which a bill for goods or services should be sent.</desc>
        </valItem>
        <valItem ident="delivery">
          <desc versionDate="2026-01-13" xml:lang="en">the address to
          which packages should be sent via a private delivery service.</desc>
        </valItem>
        <valItem ident="mailing">
          <desc versionDate="2026-01-13" xml:lang="en">the address to
          which mail should be sent via a public postal service.</desc>
        </valItem>
        <valItem ident="military">
          <desc versionDate="2026-01-15" xml:lang="en">the address to
          which mail to deployed military personnel should be sent.</desc>
        </valItem>
        <valItem ident="physical">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          a building irrespective of where mail to its occupants
          should be sent (for example, for the fire
          department).</desc>
        </valItem>
      </valList>
```

^b14

### Block 15

XML location: `/elementSpec[1]/attList[1]/attDef[2]/desc[1]`.

```xml
<desc versionDate="2026-01-02" xml:lang="en">specifies further information about the purpose of the address.</desc>
```

^b15

### Block 16

XML location: `/elementSpec[1]/attList[1]/attDef[2]/datatype[1]`.

```xml
<datatype maxOccurs="unbounded"><dataRef key="teidata.enumerated"/></datatype>
```

^b16

### Block 17

XML location: `/elementSpec[1]/attList[1]/attDef[2]/valList[1]`.

```xml
<valList type="open">
        <valItem ident="sender">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          the sender of a piece of correspondence.</desc>
        </valItem>
        <valItem ident="return">
          <desc versionDate="2026-01-13" xml:lang="en">the address to
          which undeliverable mail should be returned.</desc>
        </valItem>
        <valItem ident="recipient ">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          the intended recipient of a piece of correspondence.</desc>
        </valItem>
        <valItem ident="work">
          <desc versionDate="2026-01-15" xml:lang="en">the address to
          which work-related mail should be sent, typically that of
          the recipient’s employer.</desc>
        </valItem>
        <valItem ident="home">
          <desc versionDate="2026-01-15" xml:lang="en">the address to
          which non-work-related mail should be sent, typically the
          domicile of the recipient.</desc>
        </valItem>
        <valItem ident="start">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          the beginning of a route, for example of a race.</desc>
        </valItem>
        <valItem ident="finish">
          <desc versionDate="2026-01-13" xml:lang="en">the address of
          the end of a route, for example of a race.</desc>
        </valItem>
        <valItem ident="pickup">
          <desc versionDate="2026-01-13" xml:lang="en">the address at
          which a person or package is picked up, for example by a
          taxi or delivery service.</desc>
        </valItem>
        <valItem ident="dropOff">
          <desc versionDate="2026-01-13" xml:lang="en">the address at
          which a person or package is dropped off, for example by a
          taxi or delivery service.</desc>
        </valItem>
      </valList>
```

^b17

### Block 18

XML location: `/elementSpec[1]/attList[1]/attDef[2]/remarks[1]`.

```xml
<remarks ident="address-attr.role-remarks" xml:lang="en" versionDate="2026-02-16">
        <p>Whereas <att>type</att> is used to differentiate the kind
        of address (e.g. a street address vs. a post office box, or a
        physical address vs. a mailing address), <att>role</att> is
        used to differentiate the purpose of the address, for example
        within a correspondence ecosystem (e.g. the address of the
        sender vs. that of the intended recipient, or a college
        student's permanent address vs. address while at school).</p>
      </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>Using just the elements defined by the core module, an address could be represented as follows:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-rj" source="#NONE">
      <address>
        <street>via Marsala 24</street>
        <postCode>40126</postCode>
        <name>Bologna</name>
        <name>Italy</name>
      </address>
    </egXML>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum xml:lang="en">
    <p>When a schema includes the names and dates module more specific elements such as country or settlement would be preferable over generic <gi>name</gi>:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-ua" source="#NONE">
      <address>
        <street>via Marsala 24</street>
        <postCode>40126</postCode>
        <settlement>Bologna</settlement>
        <country>Italy</country>
      </address>
    </egXML>
  </exemplum>
```

^b20

### Block 21

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-tn" source="#NONE">
      <address>
        <addrLine>Centre d'Études Supérieures de la Renaissance</addrLine>
        <addrLine>59, rue Néricault-Destouches</addrLine>
        <addrLine> 37013 TOURS</addrLine>
        <addrLine>France</addrLine>
      </address>
    </egXML>
  </exemplum>
```

^b21

### Block 22

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-kz" source="#NONE">
      <address>
        <street>邯郸路220号</street>
        <postCode>200433</postCode>
        <name>上海市</name>
        <name n="I">中華人民共和國</name>
      </address>
    </egXML>
  </exemplum>
```

^b22

### Block 23

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-ln" source="#NONE">
      <address>
        <addrLine>沙田</addrLine>
        <addrLine>新界</addrLine>
        <addrLine>香港特別行政區</addrLine>
        <addrLine>中華人民共和國</addrLine>
      </address>
    </egXML>
  </exemplum>
```

^b23

### Block 24

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-hr" source="#NONE">
      <address>
        <addrLine>Computing Center, MC 135</addrLine>
        <addrLine>P.O. Box 6998</addrLine>
        <addrLine>Chicago, IL 60680</addrLine>
        <addrLine>USA</addrLine>
      </address>
    </egXML>
  </exemplum>
```

^b24

### Block 25

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum xml:lang="mul">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-address-egXML-zn" source="#NONE">
      <address>
        <country key="FR"/>
        <settlement type="city">Lyon</settlement>
        <postCode>69002</postCode>
        <district type="arrondissement">IIème</district>
        <district type="quartier">Perrache</district>
        <street><num>30</num>, Cours de Verdun</street>
      </address>
    </egXML>
  </exemplum>
```

^b25

### Block 26

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="address-remarks" versionDate="2007-12-16" xml:lang="en">
    <p rend="dataDesc">This element should be used for postal
    addresses only. Within it, the generic element <gi>addrLine</gi>
    may be used as an alternative to any of the more specialized
    elements available from the <ident type="class">model.addrPart</ident> class, such as
    <gi>street</gi>, <gi>postCode</gi> etc.</p>
  </remarks>
```

^b26

### Block 27

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="address-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p rend="dataDesc">Cet élément ne doit être utilisé que pour
    donner une adresse postale. A l'intérieur de cet élément,
    l'élément générique <gi>addrLine</gi> peut être utilisé comme
    élément alternatif aux éléments plus spécialisés de la classe
    <ident type="class">model.addrPart</ident> class, tels que
    <gi>street</gi>, <gi>postCode</gi> etc.</p>
  </remarks>
```

^b27

### Block 28

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="address-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p rend="dataDesc"> 当該要素は、郵便配達情報にのみ使用されるべきで
    ある。 子要素として要素<gi>addrLine</gi>は、クラスmodel.addrPartに
    ある要 素の代わりとして、例えば、要素<gi>street</gi>や要素
    <gi>postcode</gi>として使用することができる。 </p>
  </remarks>
```

^b28

### Block 29

XML location: `/elementSpec[1]/remarks[4]`.

```xml
<remarks ident="address-remarks" versionDate="2016-11-24" xml:lang="de">
    <p rend="dataDesc">Dieses Element sollte ausschließlich für
    postalische Addressen verwendet werden. Innerhalb des Elements
    kann das generische <gi>addrLine</gi>-Element als Alternative zu
    den spezielleren Elementen aus der <ident type="class">model.addrPart</ident>-Klasse, wie <gi>street</gi>
    (Straße), <gi>postCode</gi> (Postleitzahl), etc. verwendet
    werden.</p>
  </remarks>
```

^b29

### Block 30

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONAAD"/>
    <ptr target="#HD24"/>
    <ptr target="#COBICOI"/>
  </listRef>
```

^b30

