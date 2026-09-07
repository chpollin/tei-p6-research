---
type: representation
source-type: document
source: '[[00_sources/tei-p5-note-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 note
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Specs/note.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# note

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 8889. Git blob: `13282a3e75d2b7fbdde20fc635cafb805f3a90dd`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<elementSpec xmlns="http://www.tei-c.org/ns/1.0" module="core" xml:id="gi-note" ident="note">
  <gloss versionDate="2017-06-25" xml:lang="en">note</gloss>
  <gloss versionDate="2017-06-25" xml:lang="de">Anmerkung</gloss>
  <desc versionDate="2005-01-14" xml:lang="en">contains a note or annotation.</desc>
  <desc versionDate="2009-01-06" xml:lang="fr">contient une note ou une annotation.</desc>
  <desc versionDate="2007-05-04" xml:lang="es">contiene una nota o aclaración</desc>
  <desc versionDate="2007-05-02" xml:lang="zh-TW">包含附註或註釋。</desc>
  <desc versionDate="2007-01-21" xml:lang="it">contiene una nota o un'annotazione.</desc>
  <desc versionDate="2006-10-28" xml:lang="ja">注釈・コメント。</desc>
  <desc versionDate="2017-06-25" xml:lang="de">enthält eine Anmerkung oder Annotation.</desc>
  <classes>
    <memberOf key="att.global"/>
    <memberOf key="att.anchoring"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.annotationLike"/>
    <memberOf key="model.annotationPart.body"/>
    <memberOf key="model.correspActionPart"/>
    <memberOf key="model.correspContextPart"/>
    <memberOf key="model.correspDescPart"/>
    <memberOf key="model.noteLike"/>
  </classes>
  <content>
    <macroRef key="macro.specialPara"/>
  </content>
  <exemplum xml:lang="en">
    <p>In the following example, the translator has supplied a footnote
      containing an explanation of the term translated as "painterly":</p>
<egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-yp" source="#NOTE-eg">And yet it is not only
in the great line of Italian renaissance art, but even in the
painterly <note place="bottom" type="gloss" resp="#MDMH"><term xml:lang="de">Malerisch</term>. This word has, in the German, two
distinct meanings, one objective, a quality residing in the object,
the other subjective, a mode of apprehension and creation.  To avoid
confusion, they have been distinguished in English as
<mentioned>picturesque</mentioned> and
<mentioned>painterly</mentioned> respectively.</note> style of the
Dutch genre painters of the seventeenth century that drapery has this
psychological significance. 
  <!-- elsewhere in the document -->
  
  <respStmt xml:id="MDMH">
    <resp>translation from German to English</resp>
    <name>Hottinger, Marie Donald Mackie</name>
  </respStmt>  
</egXML>
    <p>For this example to be valid, the
      code <ident>MDMH</ident> must be defined elsewhere, for example by
      means of a responsibility statement in the associated TEI header.</p>
  </exemplum>
  
  <exemplum versionDate="2017-06-26" xml:lang="de">
    <p>Im folgenden Beispiel hat der Übersetzer eine Fußnote mit einer Erklärung des als "painterly"
      übersetzten Begriffs "Malerisch" bereitgestellt:</p>
     <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-cp" source="#NOTE-eg">And yet it is not only
        in the great line of Italian renaissance art, but even in the
        painterly <note place="bottom" type="gloss" resp="#MDMH-1"><term xml:lang="de">Malerisch</term>. This word has, in the German, two
          distinct meanings, one objective, a quality residing in the object,
          the other subjective, a mode of apprehension and creation.  To avoid
          confusion, they have been distinguished in English as
          <mentioned>picturesque</mentioned> and
          <mentioned>painterly</mentioned> respectively.</note> style of the
        Dutch genre painters of the seventeenth century that drapery has this
        psychological significance. 
        
        <!-- elsewhere in the document -->
     
       <respStmt xml:id="MDMH-1">
         <resp>translation from German to English</resp>
         <name>Hottinger, Marie Donald Mackie</name>
       </respStmt>
     </egXML>
    <p>Damit dieses Beispiel valide ist, muss der Code <ident>MDMH-1</ident>
      an anderer Stelle definiert werden, beispielsweise durch die Angabe der Verantwortlichkeit im 
    <gi>respStmt</gi>-Element des zugehörigen TEI-Headers.</p>
    
  </exemplum>
  <exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-se" source="#fr-ex-Perec-esp">
      <p>J'écris dans la<lb/> marge...<lb/> Je vais<lb/> à la ligne.<lb/> Je renvoie à une
            note<note type="gloss" place="foot"> J'aime beaucoup les renvois en bas de page, même si
            je n'ai rien de particulier à y préciser.</note>en bas de page.</p>
    </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-ab"> 爾時王園精舍有比丘尼，名曰毘梨<note type="gloss">毘梨，秦言雄也。</note>時彼國人一切共為俱蜜頭星會 </egXML>
  </exemplum>
  <exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-ws" source="#biblzh-tw_n14">此片的膠片已不存在，但《明星月報》刊登的艾霞電影腳本大綱，仍可供我們咀嚼艾霞的創作旨趣。<note n="35" anchored="true">
        此時電影很少有完整的腳本，多是類似早期新劇的「幕表」
    ，也就是大綱，因為是默片，台詞也很簡單，主要依靠導演指示，演員臨場作戲。</note>從她的文字風格語主題特色裡，...</egXML>
  </exemplum>
  <exemplum xml:lang="en">
    <p>The global <att>n</att> attribute may be used to supply the symbol or number used to mark the
      note's point of attachment in the source text, as in the
    following example: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-tz">Mevorakh b. Saadya's mother, the matriarch of the
        family during the second half of the eleventh century, <note n="126" anchored="true"> The
          alleged mention of Judah Nagid's mother in a letter from 1071 is, in fact, a reference to
          Judah's children; cf. above, nn. 111 and 54. </note> is well known from Geniza documents
        published by Jacob Mann.</egXML>
    <p>However, if notes are numbered in sequence and their
      numbering can be reconstructed automatically by processing software, it may well be considered
      unnecessary to record the note numbers.</p>
  </exemplum>
  <exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Das globale <att>n</att>-Attribut kann verwendet werden, um das Symbol oder die Nummer anzugeben,
      die verwendet wird, um den Bezugspunkt der Anmerkung im Quelltext zu markieren, wie im folgenden
      Beispiel:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-tx">Mevorakh b. Saadya's mother, the matriarch of the
      family during the second half of the eleventh century, <note n="126" anchored="true"> The
        alleged mention of Judah Nagid's mother in a letter from 1071 is, in fact, a reference to
        Judah's children; cf. above, nn. 111 and 54. </note> is well known from Geniza documents
      published by Jacob Mann.</egXML>
    <p>Wenn jedoch Anmerkungen sequenziell nummeriert sind und deren Nummerierung durch die
      elektronische Verarbeitung automatisch rekonstruiert werden kann, kann es als unnötig angesehen
      werden, die Nummerierung anzugeben.</p>
  </exemplum>
  <exemplum versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut global <att>n</att> indique le
      symbole ou le nombre utilisé pour marquer le point d'insertion
      dans le texte source, comme dans l'exemple suivant :</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-kn" xml:lang="en">Mevorakh b. Saadya's
      mother, the matriarch of the family during the second half of the
      eleventh century, <note n="126" anchored="true"> The alleged
        mention of Judah Nagid's mother in a letter from 1071 is, in fact,
        a reference to Judah's children; cf. above, nn. 111 and
        54. </note> is well known from Geniza documents published by Jacob
      Mann.</egXML> 
    <p>Cependant, si les notes sont ordonnées et numérotées
      et qu’on veuille reconstruire automatiquement leur numérotation
      par un traitement informatique, il est inutile d’enregistrer le
      numéro des notes.</p>
  </exemplum>
  <listRef>
    <ptr target="#CONONO" type="div2"/>
    <ptr target="#HD27"/>
    <ptr target="#COBICON"/>
    <ptr target="#DITPNO"/>
  </listRef>
</elementSpec>
```

## Source blocks

### Block 1

XML location: `/elementSpec[1]/gloss[1]`.

```xml
<gloss versionDate="2017-06-25" xml:lang="en">note</gloss>
```

^b1

### Block 2

XML location: `/elementSpec[1]/gloss[2]`.

```xml
<gloss versionDate="2017-06-25" xml:lang="de">Anmerkung</gloss>
```

^b2

### Block 3

XML location: `/elementSpec[1]/desc[1]`.

```xml
<desc versionDate="2005-01-14" xml:lang="en">contains a note or annotation.</desc>
```

^b3

### Block 4

XML location: `/elementSpec[1]/desc[2]`.

```xml
<desc versionDate="2009-01-06" xml:lang="fr">contient une note ou une annotation.</desc>
```

^b4

### Block 5

XML location: `/elementSpec[1]/desc[3]`.

```xml
<desc versionDate="2007-05-04" xml:lang="es">contiene una nota o aclaración</desc>
```

^b5

### Block 6

XML location: `/elementSpec[1]/desc[4]`.

```xml
<desc versionDate="2007-05-02" xml:lang="zh-TW">包含附註或註釋。</desc>
```

^b6

### Block 7

XML location: `/elementSpec[1]/desc[5]`.

```xml
<desc versionDate="2007-01-21" xml:lang="it">contiene una nota o un'annotazione.</desc>
```

^b7

### Block 8

XML location: `/elementSpec[1]/desc[6]`.

```xml
<desc versionDate="2006-10-28" xml:lang="ja">注釈・コメント。</desc>
```

^b8

### Block 9

XML location: `/elementSpec[1]/desc[7]`.

```xml
<desc versionDate="2017-06-25" xml:lang="de">enthält eine Anmerkung oder Annotation.</desc>
```

^b9

### Block 10

XML location: `/elementSpec[1]/classes[1]`.

```xml
<classes>
    <memberOf key="att.global"/>
    <memberOf key="att.anchoring"/>
    <memberOf key="att.cmc"/>
    <memberOf key="att.placement"/>
    <memberOf key="att.pointing"/>
    <memberOf key="att.typed"/>
    <memberOf key="att.written"/>
    <memberOf key="model.annotationLike"/>
    <memberOf key="model.annotationPart.body"/>
    <memberOf key="model.correspActionPart"/>
    <memberOf key="model.correspContextPart"/>
    <memberOf key="model.correspDescPart"/>
    <memberOf key="model.noteLike"/>
  </classes>
```

^b10

### Block 11

XML location: `/elementSpec[1]/content[1]`.

```xml
<content>
    <macroRef key="macro.specialPara"/>
  </content>
```

^b11

### Block 12

XML location: `/elementSpec[1]/exemplum[1]`.

```xml
<exemplum xml:lang="en">
    <p>In the following example, the translator has supplied a footnote
      containing an explanation of the term translated as "painterly":</p>
<egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-yp" source="#NOTE-eg">And yet it is not only
in the great line of Italian renaissance art, but even in the
painterly <note place="bottom" type="gloss" resp="#MDMH"><term xml:lang="de">Malerisch</term>. This word has, in the German, two
distinct meanings, one objective, a quality residing in the object,
the other subjective, a mode of apprehension and creation.  To avoid
confusion, they have been distinguished in English as
<mentioned>picturesque</mentioned> and
<mentioned>painterly</mentioned> respectively.</note> style of the
Dutch genre painters of the seventeenth century that drapery has this
psychological significance. 
  <!-- elsewhere in the document -->
  
  <respStmt xml:id="MDMH">
    <resp>translation from German to English</resp>
    <name>Hottinger, Marie Donald Mackie</name>
  </respStmt>  
</egXML>
    <p>For this example to be valid, the
      code <ident>MDMH</ident> must be defined elsewhere, for example by
      means of a responsibility statement in the associated TEI header.</p>
  </exemplum>
```

^b12

### Block 13

XML location: `/elementSpec[1]/exemplum[2]`.

```xml
<exemplum versionDate="2017-06-26" xml:lang="de">
    <p>Im folgenden Beispiel hat der Übersetzer eine Fußnote mit einer Erklärung des als "painterly"
      übersetzten Begriffs "Malerisch" bereitgestellt:</p>
     <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-cp" source="#NOTE-eg">And yet it is not only
        in the great line of Italian renaissance art, but even in the
        painterly <note place="bottom" type="gloss" resp="#MDMH-1"><term xml:lang="de">Malerisch</term>. This word has, in the German, two
          distinct meanings, one objective, a quality residing in the object,
          the other subjective, a mode of apprehension and creation.  To avoid
          confusion, they have been distinguished in English as
          <mentioned>picturesque</mentioned> and
          <mentioned>painterly</mentioned> respectively.</note> style of the
        Dutch genre painters of the seventeenth century that drapery has this
        psychological significance. 
        
        <!-- elsewhere in the document -->
     
       <respStmt xml:id="MDMH-1">
         <resp>translation from German to English</resp>
         <name>Hottinger, Marie Donald Mackie</name>
       </respStmt>
     </egXML>
    <p>Damit dieses Beispiel valide ist, muss der Code <ident>MDMH-1</ident>
      an anderer Stelle definiert werden, beispielsweise durch die Angabe der Verantwortlichkeit im 
    <gi>respStmt</gi>-Element des zugehörigen TEI-Headers.</p>
    
  </exemplum>
```

^b13

### Block 14

XML location: `/elementSpec[1]/exemplum[3]`.

```xml
<exemplum versionDate="2008-04-06" xml:lang="fr">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-se" source="#fr-ex-Perec-esp">
      <p>J'écris dans la<lb/> marge...<lb/> Je vais<lb/> à la ligne.<lb/> Je renvoie à une
            note<note type="gloss" place="foot"> J'aime beaucoup les renvois en bas de page, même si
            je n'ai rien de particulier à y préciser.</note>en bas de page.</p>
    </egXML>
  </exemplum>
```

^b14

### Block 15

XML location: `/elementSpec[1]/exemplum[4]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-ab"> 爾時王園精舍有比丘尼，名曰毘梨<note type="gloss">毘梨，秦言雄也。</note>時彼國人一切共為俱蜜頭星會 </egXML>
  </exemplum>
```

^b15

### Block 16

XML location: `/elementSpec[1]/exemplum[5]`.

```xml
<exemplum xml:lang="zh-TW">
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-ws" source="#biblzh-tw_n14">此片的膠片已不存在，但《明星月報》刊登的艾霞電影腳本大綱，仍可供我們咀嚼艾霞的創作旨趣。<note n="35" anchored="true">
        此時電影很少有完整的腳本，多是類似早期新劇的「幕表」
    ，也就是大綱，因為是默片，台詞也很簡單，主要依靠導演指示，演員臨場作戲。</note>從她的文字風格語主題特色裡，...</egXML>
  </exemplum>
```

^b16

### Block 17

XML location: `/elementSpec[1]/exemplum[6]`.

```xml
<exemplum xml:lang="en">
    <p>The global <att>n</att> attribute may be used to supply the symbol or number used to mark the
      note's point of attachment in the source text, as in the
    following example: </p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-tz">Mevorakh b. Saadya's mother, the matriarch of the
        family during the second half of the eleventh century, <note n="126" anchored="true"> The
          alleged mention of Judah Nagid's mother in a letter from 1071 is, in fact, a reference to
          Judah's children; cf. above, nn. 111 and 54. </note> is well known from Geniza documents
        published by Jacob Mann.</egXML>
    <p>However, if notes are numbered in sequence and their
      numbering can be reconstructed automatically by processing software, it may well be considered
      unnecessary to record the note numbers.</p>
  </exemplum>
```

^b17

### Block 18

XML location: `/elementSpec[1]/exemplum[7]`.

```xml
<exemplum versionDate="2017-06-25" xml:lang="de">
    <p>Das globale <att>n</att>-Attribut kann verwendet werden, um das Symbol oder die Nummer anzugeben,
      die verwendet wird, um den Bezugspunkt der Anmerkung im Quelltext zu markieren, wie im folgenden
      Beispiel:</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-tx">Mevorakh b. Saadya's mother, the matriarch of the
      family during the second half of the eleventh century, <note n="126" anchored="true"> The
        alleged mention of Judah Nagid's mother in a letter from 1071 is, in fact, a reference to
        Judah's children; cf. above, nn. 111 and 54. </note> is well known from Geniza documents
      published by Jacob Mann.</egXML>
    <p>Wenn jedoch Anmerkungen sequenziell nummeriert sind und deren Nummerierung durch die
      elektronische Verarbeitung automatisch rekonstruiert werden kann, kann es als unnötig angesehen
      werden, die Nummerierung anzugeben.</p>
  </exemplum>
```

^b18

### Block 19

XML location: `/elementSpec[1]/exemplum[8]`.

```xml
<exemplum versionDate="2007-06-12" xml:lang="fr">
    <p>L'attribut global <att>n</att> indique le
      symbole ou le nombre utilisé pour marquer le point d'insertion
      dans le texte source, comme dans l'exemple suivant :</p>
    <egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="gi-note-egXML-kn" xml:lang="en">Mevorakh b. Saadya's
      mother, the matriarch of the family during the second half of the
      eleventh century, <note n="126" anchored="true"> The alleged
        mention of Judah Nagid's mother in a letter from 1071 is, in fact,
        a reference to Judah's children; cf. above, nn. 111 and
        54. </note> is well known from Geniza documents published by Jacob
      Mann.</egXML> 
    <p>Cependant, si les notes sont ordonnées et numérotées
      et qu’on veuille reconstruire automatiquement leur numérotation
      par un traitement informatique, il est inutile d’enregistrer le
      numéro des notes.</p>
  </exemplum>
```

^b19

### Block 20

XML location: `/elementSpec[1]/listRef[1]`.

```xml
<listRef>
    <ptr target="#CONONO" type="div2"/>
    <ptr target="#HD27"/>
    <ptr target="#COBICON"/>
    <ptr target="#DITPNO"/>
  </listRef>
```

^b20

