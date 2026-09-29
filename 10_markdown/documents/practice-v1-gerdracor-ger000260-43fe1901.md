---
type: representation
source-type: document
source: '[[00_sources/documents/practice-v1-gerdracor-ger000260-43fe1901.xml]]'
converter: tools.ingest_practice_v1 v1; complete original plus JSON-escaped exact
  source fragments
channel: collection
metadata:
  title: GerDraCor play ger000260 (tei/leisewitz-die-pfandung.xml)
  creator: DraCor project (GerDraCor)
  date: '2026-01-24'
  format: application/xml
  identifier: https://github.com/dracor-org/gerdracor/blob/43fe19012bae4784689ce7ad5855dfdd643364e5/tei/leisewitz-die-pfandung.xml
  license: CC0-1.0
  confidential: false
created: '2026-09-11'
updated: '2026-09-11'
---

# GerDraCor play ger000260 (tei/leisewitz-die-pfandung.xml)

Source: `tei/leisewitz-die-pfandung.xml` in `dracor-org/gerdracor` at commit `43fe19012bae4784689ce7ad5855dfdd643364e5`.
Source SHA-256: `8de253b51577965f68bde96715c53552d9564ea04d1a103617350b98cfea1f9d`, 7607 bytes.
Rights: CC0-1.0. German Drama Corpus (GerDraCor), CC0 1.0; the file names its digital source and original print source.
License evidence: README.md and CITATION.cff at the pinned commit; publicationStmt/availability/licence in the file.

The complete original is inert source text and is never executed. The
separator newline before its closing fence is not part of the original.
Reading blocks are exact source byte intervals encoded as JSON strings;
their line and byte locators refer to the original.

## Complete original

```xml
<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet type="text/css" href="../css/tei.css"?>
<?xml-model href="https://dracor.org/schema.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="ger000260" xml:lang="de">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Die Pfandung</title>
        <author>
          <persName>
            <forename>Johann</forename>
            <forename>Anton</forename>
            <surname>Leisewitz</surname>
          </persName>
          <idno type="wikidata">Q64063</idno>
          <idno type="pnd">118571370</idno>
        </author>
      </titleStmt>
      <publicationStmt>
        <publisher xml:id="dracor">DraCor</publisher>
        <idno type="URL">https://dracor.org</idno>
        <availability>
          <licence target="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</licence>
        </availability>
      </publicationStmt>
      <sourceDesc>
        <bibl type="digitalSource">
          <name>TextGrid Repository</name>
          <idno type="URL">http://www.textgridrep.org/textgrid:rfxg.0</idno>
          <availability>
            <licence target="http://creativecommons.org/licenses/by/3.0/de/legalcode">CC-BY-3.0</licence>
          </availability>
          <bibl type="originalSource">
            <author>Johann Anton Leisewitz</author>: <title level="a">Die Pfandung</title>. In:
              <title level="s">Sturm und Drang. Dichtungen und theoretische Texte</title>.
            Ausgewählt und mit einem Nachwort versehen von <editor>Heinz Nicolai</editor>. Band
              <biblScope unit="volume">II</biblScope>. <pubPlace>München</pubPlace>:
              <publisher>Winkler</publisher>
            <date>1971</date>, S. <biblScope unit="page" from="1591" to="1592">1591–1592</biblScope>.</bibl>
        </bibl>
      </sourceDesc>
    </fileDesc>
    <profileDesc>
      <particDesc>
        <listPerson>
          <person xml:id="der_mann" sex="MALE">
            <persName>Der Mann</persName>
          </person>
          <person xml:id="die_frau" sex="FEMALE">
            <persName>Die Frau</persName>
          </person>
        </listPerson>
      </particDesc>
      <textClass>
        <keywords>
          <term type="genreTitle"/>
        </keywords>
      </textClass>
    </profileDesc>
    <revisionDesc>
      <listChange>
        <change when="2017-01-06">(dlina) file conversion from source</change>
        <change when="2017-08-04">(ff) structural cleanup</change>
        <change when="2018-01-02">(ff) formalities; add gender info</change>
      </listChange>
    </revisionDesc>
  </teiHeader>
  <standOff>
    <listEvent>
      <event type="print" when="1774">
        <desc/>
      </event>
    </listEvent>
    <listRelation>
      <relation name="wikidata" active="https://dracor.org/entity/ger000260" passive="http://www.wikidata.org/entity/Q56449035"/>
    </listRelation>
  </standOff>
  <text>
    <pb n="1591"/>
    <front>
      <titlePage>
        <docAuthor>Johann Anton Leisewitz</docAuthor>
        <docTitle>
          <titlePart type="main">Die Pfandung</titlePart>
        </docTitle>
      </titlePage>
    </front>
    <body>
      <div type="scene">
        <stage>Ein Bauer und seine Frau. Abends in ihrer Schlafkammer.</stage>
        <sp who="#der_mann">
          <speaker>Der Mann.</speaker>
          <p>Frau, liegst du? so tu ich das Licht aus. Dehne dich zu guter Letzt noch einmal recht
            in deinem Bette. Morgen wird's gepfandet. Der Fürst hat's verpraßt.</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau.</speaker>
          <p>Lieber Gott!</p>
        </sp>
        <sp who="#der_mann">
          <speaker>Der Mann</speaker>
          <stage>indem er sich niederlegt.</stage>
          <p>Bedenk einmal das wenige, was wir ihm gegeben haben, gegen das Geld, was er
            durchbringt; so reicht es kaum zu einem Trunke seines köstlichen Weins zu.</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau.</speaker>
          <p>Das ist erschrecklich, wegen eines Trunkes zwei Leute unglücklich zu machen! Und das
            tut einer, der nicht einmal durstig ist! Die Fürsten können ja nie recht durstig
            sein.</p>
        </sp>
        <sp who="#der_mann">
          <speaker>Der Mann.</speaker>
          <p>Aber wahrhaftig! wenn auch in dem Kirchengebet das kommt: »Unsern durchlauchtigen
            Landesherrn und sein hohes Haus«, so kann ich nicht mitbeten. Das hieße Gott spotten,
            und er läßt sich nicht spotten.</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau.</speaker>
          <p>Freilich nicht! – Ach! ich bin in diesem Bette geboren, und, Wilhelm, Wilhelm! es ist
            unser Brautbett!</p>
        </sp>
        <sp who="#der_mann">
          <speaker>Der Mann</speaker>
          <stage>springt auf.</stage>
          <p>Bedächte ich nicht meine arme Seele, so nähm ich mein Strumpfband, betete ein gläubig
            Vaterunser, und hinge mich an diesen Bettpfosten.</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau</speaker>
          <stage>schlägt ein Kreuz.</stage>
          <p>Gott sei mit uns! – Da hättest du dich schön gerächt!</p>
        </sp>
        <sp who="#der_mann">
          <speaker>Der Mann.</speaker>
          <p>Meinst du nicht? – Wenn ich so stürbe, so würdest du doch wenigstens einmal
            seufzen!</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau.</speaker>
          <p>Ach Mann!</p>
        </sp>
        <sp who="#der_mann">
          <speaker>Der Mann.</speaker>
          <p>Und unser Junge würde schreien! Nicht?</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau.</speaker>
          <p>Gewiß!</p>
        </sp>
        <sp who="#der_mann">
          <speaker>Der Mann.</speaker>
          <p>Gut! An jenem Tage ich, dieses Seufzen und <pb n="1592"/> Schreien auf einer Seite –
            der Fürst auf der andern! Ich dächte, ich wäre gerächt.</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau.</speaker>
          <p>Wenn du an jenen Tag denkst, wie kannst du so reden? Da seid ihr, der Fürst und du, ja
            einander gleich.</p>
        </sp>
        <sp who="#der_mann">
          <speaker>Der Mann.</speaker>
          <p>Das wolle Gott nicht! Siehe, ich gehe aus der Welt, wie ich über Feld gehe, allein, als
            ein armer Mann. Aber der Fürst geht heraus, wie er reist, in einem großen Gefolge. Denn
            alle Flüche, Gewinsel und Seufzer, die er auf sich lud, folgen ihm nach.</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau.</speaker>
          <p>Desto besser! – So sieh doch dies Leben als einen heißen Erntetag an! – Darauf schmeckt
            die Ruhe so süß; und dort ist Ruhe von Ewigkeit zu Ewigkeit.</p>
        </sp>
        <sp who="#der_mann">
          <speaker>Der Mann</speaker>
          <stage>legt sich wieder nieder.</stage>
          <p>Amen! Du hast recht, Frau. Laß sie das Bette nehmen, die Unsterblichkeit können sie mir
            doch nicht nehmen! Schlaf wohl.</p>
        </sp>
        <sp who="#die_frau">
          <speaker>Die Frau.</speaker>
          <p>Und der Fürst und der Vogt sind ja auch unsterblich. – Gute Nacht! Ach, morgen abend
            sagen wir uns die auf der Erde!</p>
        </sp>
      </div>
    </body>
  </text>
</TEI>

```

## Selected source reading blocks

### r1 schema association processing instruction

Locator: lines 3-3, bytes 96-220, processing-instruction, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<?xml-model href=\"https://dracor.org/schema.rng\" type=\"application/xml\" schematypens=\"http://relaxng.org/ns/structure/1.0\"?>" ^r1

### r2 file licence

Locator: lines 22-24, bytes 823-958, element, occurrence 1 of 2 of the start marker.

Exact source fragment as a JSON string: "<availability>\n          <licence target=\"https://creativecommons.org/publicdomain/zero/1.0/\">CC0 1.0</licence>\n        </availability>" ^r2

### r3 participant description

Locator: lines 44-53, bytes 1957-2254, element, occurrence 1 of 1 of the start marker.

Exact source fragment as a JSON string: "<particDesc>\n        <listPerson>\n          <person xml:id=\"der_mann\" sex=\"MALE\">\n            <persName>Der Mann</persName>\n          </person>\n          <person xml:id=\"die_frau\" sex=\"FEMALE\">\n            <persName>Die Frau</persName>\n          </person>\n        </listPerson>\n      </particDesc>" ^r3

### r4 first speech

Locator: lines 91-95, bytes 3365-3623, element, occurrence 1 of 9 of the start marker.

Exact source fragment as a JSON string: "<sp who=\"#der_mann\">\n          <speaker>Der Mann.</speaker>\n          <p>Frau, liegst du? so tu ich das Licht aus. Dehne dich zu guter Letzt noch einmal recht\n            in deinem Bette. Morgen wird's gepfandet. Der Fürst hat's verpraßt.</p>\n        </sp>" ^r4

