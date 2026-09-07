---
type: representation
source-type: document
source: '[[00_sources/tei-p5-email-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 email
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/email.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# email

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 3468. Git blob: `0b4d2f16aad74c02e3be8a62c81db7c9216daa95`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-email" ident="email">
  <gloss versionDate="2007-07-04" xml:lang="en">electronic mail address</gloss>
  <gloss versionDate="2007-12-20" xml:lang="ko">전자우편 주소</gloss>
  <gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
  <gloss versionDate="2008-04-06" xml:lang="es">dirección de correo electrónico</gloss>
  <gloss versionDate="2008-03-30" xml:lang="fr">adresse de courrier électronique</gloss>
  <gloss versionDate="2007-11-06" xml:lang="it">indirizzo di posta elettronica</gloss>
  <desc versionDate="2007-02-15" xml:lang="en">contains an email address identifying a location to which
        email messages can be delivered.</desc>
  <desc versionDate="2007-12-20" xml:lang="ko">전자우편 메시지가 전달되는 위치를 식별하는 전자우편 주소를 포함한다.</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個電子郵件位址，標明電子郵件訊息可傳送的位置。</desc>
  <desc versionDate="2008-04-05" xml:lang="ja">eメールを届けるeメールアドレスを示す。</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient l'adresse de courriel identifiant un
        emplacement où un courriel peut être envoyé.</desc>
  <desc versionDate="2007-11-06" xml:lang="it">localizza un indirizzo di posta elettronica al quale possono essere inviati dei messaggi di posta elettronica.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una dirección de correo electrónico indentificando el lugar dónde los mensajes electrónicos pueden ser enviados.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.addressLike"/>
  </classes>
  <content>
    <macroRef key="macro.phraseSeq"/>
  </content>
  <exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-email-egXML-or" source="#NONE">
      <email>membership@tei-c.org</email>
    </egXML>
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-email-egXML-pk">
      <email>membership@tei-c.org</email>
    </egXML>
  </exemplum>
  <remarks ident="email-remarks" versionDate="2007-02-15" xml:lang="en">
    <p>The format of a modern Internet email address is defined in
            <ref target="https://tools.ietf.org/html/rfc2822">RFC 2822</ref>
        </p>
  </remarks>
  <remarks ident="email-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le format d'une adresse de courrier électronique internet moderne est défini dans la
            <ref target="https://tools.ietf.org/html/rfc2822">RFC 2822</ref>
        </p>
  </remarks>
  <remarks ident="email-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
            インターネット上で使用されるメールアドレスの書式については、
            <ref target="https://tools.ietf.org/html/rfc2822">RFC 2822</ref>
            を参照のこと。
        </p>
  </remarks>
  <listRef>
    <ptr target="#CONAAD"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2007-07-04" xml:lang="en">electronic mail address</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2007-12-20" xml:lang="ko">전자우편 주소</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/gloss[3]`.

```xml
<gloss versionDate="2007-05-02" xml:lang="zh-TW"/>
```

^b3

### Block 4

XML location: `/elementSpec[1]/gloss[4]`.

```xml
<gloss versionDate="2008-04-06" xml:lang="es">dirección de correo electrónico</gloss>
```

^b4

### Block 5

XML location: `/elementSpec[1]/gloss[5]`.

```xml
<gloss versionDate="2008-03-30" xml:lang="fr">adresse de courrier électronique</gloss>
```

^b5

### Block 6

XML location: `/elementSpec[1]/gloss[6]`.

```xml
<gloss versionDate="2007-11-06" xml:lang="it">indirizzo di posta elettronica</gloss>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2007-02-15" xml:lang="en">contains an email address identifying a location to which
        email messages can be delivered.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2007-12-20" xml:lang="ko">전자우편 메시지가 전달되는 위치를 식별하는 전자우편 주소를 포함한다.</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含一個電子郵件位址，標明電子郵件訊息可傳送的位置。</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2008-04-05" xml:lang="ja">eメールを届けるeメールアドレスを示す。</desc>
```

^b10

### Block 11

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient l'adresse de courriel identifiant un
        emplacement où un courriel peut être envoyé.</desc>
```

^b11

### Block 12

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2007-11-06" xml:lang="it">localizza un indirizzo di posta elettronica al quale possono essere inviati dei messaggi di posta elettronica.</desc>
```

^b12

### Block 13

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una dirección de correo electrónico indentificando el lugar dónde los mensajes electrónicos pueden ser enviados.</desc>
```

^b13

### Block 14

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.cmc"/>
    <memberOf key="model.addressLike"/>
  </classes>
```

^b14

### Block 15

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.phraseSeq"/>
  </content>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="und">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-email-egXML-or" source="#NONE">
      <email>membership@tei-c.org</email>
    </egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-email-egXML-pk">
      <email>membership@tei-c.org</email>
    </egXML>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/remarks[1]`.

```xml
<remarks ident="email-remarks" versionDate="2007-02-15" xml:lang="en">
    <p>The format of a modern Internet email address is defined in
            <ref target="https://tools.ietf.org/html/rfc2822">RFC 2822</ref>
        </p>
  </remarks>
```

^b18

### Block 19

XML location: `/elementSpec[1]/remarks[2]`.

```xml
<remarks ident="email-remarks" versionDate="2007-06-12" xml:lang="fr">
    <p>Le format d'une adresse de courrier électronique internet moderne est défini dans la
            <ref target="https://tools.ietf.org/html/rfc2822">RFC 2822</ref>
        </p>
  </remarks>
```

^b19

### Block 20

XML location: `/elementSpec[1]/remarks[3]`.

```xml
<remarks ident="email-remarks" versionDate="2008-04-05" xml:lang="ja">
    <p>
            インターネット上で使用されるメールアドレスの書式については、
            <ref target="https://tools.ietf.org/html/rfc2822">RFC 2822</ref>
            を参照のこと。
        </p>
  </remarks>
```

^b20

### Block 21

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONAAD"/>
  </listRef>
```

^b21

