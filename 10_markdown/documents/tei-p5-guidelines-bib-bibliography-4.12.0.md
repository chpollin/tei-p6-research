---
type: representation
source-type: document
source: '[[00_sources/tei-p5-guidelines-bib-bibliography-4.12.0.xml]]'
converter: tools.ingest_guidelines v1; complete XML plus verbatim blocks of prose,
  specifications and support files
channel: collection
metadata:
  title: TEI P5 4.12.0 Bibliography
  creator: TEI Consortium
  date: '2026-07-28'
  format: application/xml
  identifier: https://github.com/TEIC/TEI/blob/113e933e21f016e2655518321e9d10214b8d9fcb/P5/Source/Guidelines/en/BIB-Bibliography.xml
  license: CC-BY-3.0
  confidential: false
created: '2026-09-07'
updated: '2026-09-07'
---

# Bibliography

Copyright TEI Consortium. Source used under CC-BY-3.0; upstream also offers BSD-2-Clause.
License records: `LICENSE.md` and `P5/COPYING.txt` at commit `113e933e21f016e2655518321e9d10214b8d9fcb`.

The complete XML is preserved as inert text. The source blocks repeat exact XML
units in document order, including examples, lists, tables and constraints. The
locator identifies each unit inside this file; the complete XML preserves its
surrounding structure. Includes and processing instructions remain unexecuted.
The Guidelines coverage projection locates their separate source dependencies.
Presence of a representation establishes neither distillation nor verification.

Source byte length: 306948. Git blob: `ef21229349b3433890c4dec49735fc452b51ce41`.

## Complete XML source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- © TEI Consortium. Dual-licensed under CC-by and BSD2 licenses; see the file COPYING.txt for details. -->
<?xml-model href="https://jenkins.tei-c.org/job/TEIP5-dev/lastSuccessfulBuild/artifact/P5/release/xml/tei/odd/p5.nvdl" type="application/xml" schematypens="http://purl.oclc.org/dsdl/nvdl/ns/structure/1.0"?>
<div xmlns="http://www.tei-c.org/ns/1.0" xml:id="BIB">
  <head>Bibliography</head>
  <div>
    <head>Works Cited in Examples in these Guidelines</head>
    <listBibl>
      <bibl xml:id="biblzh-tw_n20" xml:lang="zh-TW">阿城，《棋王》。</bibl>
      <bibl xml:id="fr-ex-Acad" xml:lang="fr"><author>Académie française</author>,
          <title>Rectifications de l'orthographe - J.O. du 06-12-1990</title>, <ref target="http://www.academie-francaise.fr/langue/orthographe/plan.html">En ligne</ref>,
          <date>consulté le 05-03-2010</date>.</bibl>
      <bibl xml:id="DROTH-eg-57">
        <author>Adams, Douglas</author>. <title level="m">The Hitchhiker's Guide to the
          Galaxy</title>, <pubPlace>New York</pubPlace>: <publisher>Pocket Books</publisher>,
          <date>1979</date>, <biblScope unit="chap">chapter 31</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Abes" xml:lang="fr"><author>Agence bibliographique de l'enseignement
          supérieur</author>, <title>ABES</title>:<ref target="http://www.abes.fr/abes/page%2C570%2Cmentions-legales.html">Site internet
        </ref>par l'<editor>ABES</editor>,<date>consulté le 05-03-2010</date>.</bibl>
      <bibl xml:id="biblzh-tw_n44" xml:lang="zh-TW">阿拉伯短劍，國史館：嚴家淦總統文物。</bibl>
      <bibl xml:id="VEMEana-eg-23"><author>Alighieri, Dante</author>. <title level="a">Doglia mi
          reca ne lo core ardire</title>, <title level="m">Rime</title>, <biblScope unit="part">XLIX</biblScope>.</bibl>
      <bibl xml:id="CONARS-eg-102"><author>Allinson, E.P.</author> and <author>B. Penrose</author>.
          <title level="m">Philadelphia 1681-1887</title> (<date>1887</date>), <biblScope unit="pp">p. 138</biblScope>.</bibl>
      <bibl xml:id="COBICOR-eg-246"><title level="m">American National Standard for Bibliographic
          References, ANSI Z39.29-1977</title>, <pubPlace>New York</pubPlace>: <publisher> American
          National Standards Institute</publisher> (<date>1977</date>). </bibl>
      <bibl xml:id="CONADA-eg-144">
        <!-- T. M. Andersson, A Preface to the Nibelungenlied         -->
        <!-- (Stanford:  Stanford University Press, 1987) p. 4        -->
        <author>Andersson, Theodore M.</author>. <title> A Preface to the Nibelungenlied</title>,
          <publisher>Stanford University Press</publisher> (<date>1987</date>).</bibl>
      <bibl xml:id="COEDADD-eg-91">
        <author>Andrews, Mr.</author>. <title level="a">Song</title>, <title level="m">Chambers's
          Edinburgh Journal Series 1</title>
        <biblScope unit="volume">9</biblScope>:<biblScope unit="issue">463</biblScope> (<date>12
          December 1840</date>), <biblScope unit="page">376</biblScope>. <ptr target="https://dvpp.uvic.ca/poems/chambers_series/1840/pom_5242_song.html"/>
      </bibl>
      <bibl xml:id="fr-ex-Antigone" xml:lang="fr"><author>Anouilh, Jean</author>, <title>
          Antigone</title>, <date>1842</date>.</bibl>
      <bibl xml:id="WHITMS2">
        <title>[As in Visions of] </title> Single leaf of Notes for a poem about night "visions,"
        possibly related to the untitled 1855 poem that Whitman eventually titled "The Sleepers."
        Fragments of an unidentified newspaper clipping about the Puget Sound area have been pasted
        to the leaf. The Trent Collection of Walt Whitman Manuscripts, Duke University Rare Book,
        Manuscript, and Special Collections Library. <ptr target="http://www.whitmanarchive.org/resources/sleepers/duk.00258.001.jpg"/>
      </bibl>
      <bibl xml:id="DIC-CR">
        <editor>Atkins et al. </editor>
        <title>Collins Robert French-English English-French Dictionary</title>.
          <pubPlace>London</pubPlace>: <publisher>Collins</publisher> (<date>1978</date>). </bibl>
      <bibl xml:id="TSSASE-eg-20">
        <author>Atkinson, J. Maxwell</author> and <author>John Heritage</author>. <title level="m">Structures of social action: Studies in conversation analysis</title>,
          <pubPlace>Cambridge</pubPlace> and <pubPlace>Paris</pubPlace>: <publisher>Cambridge
          University Press</publisher>, <series>Editions de la Maison des Sciences de
          l'Homme</series> (<date>1984</date>), <biblScope unit="pp">ix-xvi</biblScope>.</bibl>
      <bibl xml:id="CONARS-eg-101"><author>Austen, Jane</author>. <title level="m">Pride and
          Prejudice</title>. (<date>1813</date>), <biblScope unit="chap">chapter
        1</biblScope>.</bibl>

      <!--B-->

      <bibl xml:id="biblzh-tw_n25" xml:lang="zh-TW">白先勇，〈金大班的最後一夜〉，《台北人》。</bibl>
      <bibl xml:id="biblzh-tw_n26" xml:lang="zh-TW">白先勇，《孽子》。</bibl>
      <bibl xml:id="biblzh-tw_n59" xml:lang="zh-TW">白居易，《憶江南》。</bibl>
      <bibl xml:id="OTrim1.1">
        <title>Amheida I: Ostraka from Trimithis Volume 1: Texts from the 2004–2007 Seasons</title>,
          <editor>Bagnall, R. S. and G. R. Ruffini, with contributions by R. Cribiore and G.
          Vittmann</editor> (<date>2012</date>). </bibl>
      <bibl xml:id="NZETC01">
        <author>Baker, James K.</author>. <title>Night in Tarras</title>. In <title level="j">Hilltop: A Literary Paper</title>, vol 1 no 2. Wellington: Victoria University College
        Literary Society. (<date>1949</date>). </bibl>
      <bibl xml:id="fr-ex-Balzac-Chouans" xml:lang="fr"><author>Balzac, Honoré de</author>,
          <title>Les Chouans</title>, <date>1845</date>.</bibl>
      <bibl xml:id="fr-ex-Balzac_Goriot" xml:lang="fr"><author>Balzac, Honoré de</author>,
          <author>Le Père Goriot</author>, <date>1843</date>.</bibl>
      <bibl xml:id="fr-ex-Balzac_Vie" xml:lang="fr"><author>Balzac, Honoré de</author>, <title>Petites misères de la
          vie conjugale</title>, <date>1850</date>.</bibl>
      <bibl xml:id="COVE-eg-286"><author>Barbauld, Lucy Aikin</author>. <title>The Works of Anna
          Laetitia Barbauld</title> (<date>1826</date>).</bibl>
      <bibl xml:id="DS-eg-04">
        <author>Barker, Jane</author>. <title>The Lining to the Patch-Work Screen</title>
          (<date>1726</date>). </bibl>
      <bibl xml:id="COEDADD-eg-93">
        <title>Base de datos paleográfica da lírica galego-portuguesa (PalMed)</title>. Versión 1.2.
          <pubPlace>Santiago de Compostela</pubPlace>: <publisher>Centro Ramón Piñeiro para a
          Investigación en Humanidades</publisher>. <ptr target="http://www.cirp.gal/palmed"/>.
          <citedRange>f. B126r, column a, l. 21-32.</citedRange>
      </bibl>
      <bibl xml:id="fr-ex-Bataille_Arbre" xml:lang="fr"><author>Bataille, Michel</author> ,
          <title>L'Arbre de Noël</title>, <date>1967</date>.</bibl>
      <bibl xml:id="fr-ex-Baudelaire-chats" xml:lang="fr">
        <title level="a">Les Chats</title>, in : <author>Baudelaire, Charles</author>, <title level="m">Les Fleurs du mal</title>, <date>1861</date>.</bibl>
      <bibl xml:id="fr-ex-Baudelaire-vie" xml:lang="fr">
        <title level="a">La Vie antérieure</title>, in : <author>Baudelaire, Charles</author>,
          <title level="m">Les Fleurs du mal</title>, <date>1861</date>.</bibl>
      <bibl xml:id="biblzh-tw_n30-31" xml:lang="zh-TW">電影《霸王別姬》，1993年。</bibl>
      <bibl xml:id="fr-ex-Beck_Morin" xml:lang="fr"><author>Beck, Béatrice</author>, <title>Léon
          Morin, prêtre</title>, <date>1952</date>.</bibl>
      <bibl xml:id="DRCAST-eg-16"><author>Beckett, Samuel</author>. <title level="m">Waiting for
          Godot</title>, <pubPlace>London</pubPlace>: <publisher>Faber and Faber</publisher>
          (<date>1956</date>).</bibl>
      <bibl xml:id="CO-eg-02"><author>Beckett, Samuel</author>. <title level="m">Murphy</title>
          (<date>1963</date>), chap 2. </bibl>
      <bibl xml:id="fr-ex-Becque-ee" xml:lang="fr"><author>Becque, Henry</author>, <title>La
          Parisienne</title>. <ref target="http://www.cnrtl.fr/corpus/frantext/frantext.php">Edition
          électronique</ref> par l'<editor>ATILF</editor> et le <editor>CNRTL</editor>, d'après
        l'édition de Fasquelle (Paris, 1922). </bibl>
      <bibl xml:id="github-mix-mix">
        <author>Bowers, Jack</author>
        <title>Mixtepec-Mixtec Project Personography</title>
        <ptr target="https://raw.githubusercontent.com/iljackb/Mixtepec_Mixtec/master/MIX-People.xml#element(JS/6)"/>
        <date type="accessed" when="2023-05-08"/>
      </bibl>
      <bibl xml:id="PH-eg-05">
        <author>Beerbohm, Max</author>. Autograph manuscript of <title>The Golden Drugget</title>,
        Pierpont Morgan MA 3391. in <ptr target="#KLINKENBORG"/> 123. </bibl>
      <bibl xml:id="DRPRO-eg-10"><author>Behn, Aphra</author>. <title level="m">The Rover</title>,
          (<date>1697</date>).</bibl>
      <bibl xml:id="divEGs">
        <author>Beeton, Isabella</author>. <title>The book of Household Management</title>,
          <pubPlace>London</pubPlace>: <publisher>S.O. Beeton</publisher>
        (<date>1861</date>).</bibl>
      <bibl xml:id="fr-ex-Belloc_Kepas" xml:lang="fr"><author>Belloc, Denis</author>,
          <title>Képas</title>, <date>1989</date>.</bibl>
      <bibl xml:id="fr-ex-Belloc_Neons" xml:lang="fr">
        <author>Belloc, Denis</author>, <title>Néons</title>, <date>1987</date>.</bibl>
      <bibl xml:id="bentham"><author>Bentham, Jeremy</author>. <title level="m">The Book of
          Fallacies.</title> (<date>1824</date>).</bibl>
      <bibl xml:id="TCAPLR-eg-11">
        <title>Beowulf and The fight at Finnsburg</title>; edited, with introduction, bibliography,
        notes, glossary, and appendices, by <editor>Fr. Klaeber</editor>. <pubPlace>Boston, New York
          [etc.] </pubPlace>
        <publisher>D.C. Heath &amp; Co.</publisher> (<date>1922</date>). </bibl>
      <bibl xml:id="fr-ex-Bibliog_Renaissance_Ital" xml:lang="fr">
        <title>Bibliographie dans le cadre de la semaine italienne du 11 au 18 mars 2006</title>, ,
          <ref target="http://www.mediatheque-rueilmalmaison.fr/musique_cinema_arts_et_loisirs/arts_les_dossiers/la_renaissance_italienne_article1154.html?artsuite=5">document électronique</ref>.</bibl>
      <bibl xml:id="fr-ex-BnF-Reliures" xml:lang="fr"><author>Bibliothèque nationale de
          France</author>, <title> Projet de description des reliures remarquables de la Réserve des
          livres rares selon le modèle de la TEI manuscrits</title>.</bibl>
      <bibl xml:id="fr-ex-Billetdoux" xml:lang="fr"><author>Billetdoux, Marie</author>, <title>Un
          peu de désir sinon je meurs</title>, <date>2006</date>.</bibl>
      <bibl xml:id="VE-eg-04">
        <author>Blake, William</author>. <title level="a">London</title>, in <title level="m">Songs
          of Experience</title> (<date>1791</date>). </bibl>
      <bibl xml:id="SG132-neg-1">
        <author>Blake, William</author>. <title level="a">The Sick Rose</title>, in <title level="m">Songs of Experience</title> (<date>1794</date>). </bibl>
      <bibl xml:id="en-blake-tyger">
        <author>Blake, William</author>. <title level="a">The Tyger</title>, in <title level="m">Songs of Experience</title> (<date>1794</date>). </bibl>
      <bibl xml:id="SASE-eg-33"><author>Bloomfield, Leonard</author>. <title level="a">Literate and
          Illiterate Speech</title>, <title level="j">American Speech</title>, <biblScope unit="issue">2</biblScope>, (<date>1927</date>), <biblScope unit="pp">pp.
          432-441</biblScope>.</bibl>
      <bibl xml:id="COLI-eg-171"><author>Borges, Jorge Luis</author>, tr. <editor role="tr">R.
          Simms</editor>. <title level="a">The Analytical Language of John Wilkins</title>. In
          <editor>Emir Rodriguez Monegal</editor> and <editor>Alistair Reid</editor>, eds. <title level="m">Borges: A reader</title>, <publisher>Dutton Adult</publisher>
        (<date>1981</date>), <biblScope unit="pp">p.141</biblScope>.</bibl>
      <bibl xml:id="FTFOR-eg-10"><author>Borges, Jorge Luis</author>. <title level="a">Avatars of
          the Tortoise</title> In <editor role="tr">James E. Irby</editor> tr. <title level="m">Labyrinths: Selected Stories and Other Writings</title>, <pubPlace>New York</pubPlace>:
          <publisher>New Directions</publisher>, (<date>1962</date>), <biblScope unit="pp">pp.202-203</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Bouiller_Rapport" xml:lang="fr"><author>Bouillier, Grégoire</author>,
          <title>Rapport sur moi</title>, <date> 2002</date>.</bibl>
      <bibl xml:id="fr-ex-Mouchette" xml:lang="fr"><author>Bresson, Robert</author>, <title level="a">Mouchette : script</title>, <title level="j">l'Avant-scène cinéma</title>,
          <num>n° 80</num>, <date>avril 1968</date>.</bibl>
      <bibl xml:id="SA-eg-02"> Extract from <title>British National Corpus</title> (<ptr target="http://www.natcorp.ox.ac.uk"/>) Text KB7, sentence 13730.</bibl>
      <bibl xml:id="COPA-eg-1">
        <author>Brontë, Charlotte</author>. <title level="m">Jane Eyre: An Autobiography</title>,
          <edition>Third edition; reprint</edition><pubPlace>London</pubPlace>
        <publisher>Service &amp; Paton</publisher>, <date>1897</date>; <publisher>Project
          Gutenberg</publisher>, <date>1 December 2020</date>. <biblScope unit="chap">chapter
          XII</biblScope>. <ptr target="https://www.gutenberg.org/files/1260/1260-h/1260-h.htm"/>
      </bibl>
      <bibl xml:id="PH-eg-15">
        <author>Browning, Robert</author>. <title>Letter to George Moulton-Barrett</title>, Pierpont
        Morgan MA 310, (<ptr target="#KLINKENBORG"/> 23). </bibl>
      <bibl xml:id="fr-ex-Belloy" xml:lang="fr"><author>Buirette de Belloy, Pierre Laurent</author>,
          <title level="m">Gabrielle de Vergy</title>, <date>1777</date>.</bibl>
      <bibl xml:id="DS-eg-06">
        <author>Bunyan, John</author>. <title>The Pilgrim's Progress from this world to that which
          is to come...</title>, <pubPlace>London</pubPlace> (<date>1678</date>). </bibl>
      <bibl xml:id="STGA-eg-4"><author>Burgess, Anthony</author>. <title level="m">A Clockwork
          Orange</title>. (<date>1962</date>), <biblScope unit="part">opening</biblScope>.</bibl>
      <bibl xml:id="usenet-sgml-tei"><title level="a">
        <ref target="https://www.usenetarchives.com/view.php?id=comp.text.sgml&amp;mid=PDI5MzIxLjkwMDkzMDEzMzBAbWFudXRpdXMuZWNzLnNvdG9uLmFjLnVrPg">Burnard SGML reading list</ref></title>, 
        <title level="m">COMP.TEXT.SGML</title>, <date from="1990-09-30" to="1990-10-11">September 30 to October 11, 1990</date> in <title level="m">Usenet Archives</title>
        (<publisher>UsenetArchives.com</publisher>, <date>2024</date>).
      </bibl>
      <bibl xml:id="Burnard-db"><author>Burnard, Lou</author>. <title level="a">Principles of
          Database Design</title> in <editor>S. Rahtz.</editor> ed. <title level="m">Information
          Technology in the Humanities: tools, techniques and applications</title>, <publisher>Ellis
          Horwood Ltd</publisher>, <series>Ellis Horwood Series in Computers and Their
          Applications</series>, (<date>1987</date>), <biblScope unit="pp">p. 54</biblScope>.</bibl>
      <bibl xml:id="fr-ex-TEI-simpl" xml:lang="fr"><author>Burnard, Lou</author>,
          <author>Sperberg-McQueen, C. M.</author>, <title>
          <ref target="http://www.gutenberg.eu.org/publications/autres/TEILITE/">La TEI simplifiée,
            une introduction au codage des textes électroniques en vue de leur échange — version de
            travail </ref>
        </title>, <date>1996</date>.</bibl>
      <bibl xml:id="COXR-eg-164">
        <author>Burton, Robert</author>. <title level="m">Anatomy of Melancholy</title>
          (<date>1621</date>), <edition>16th ed.</edition> reprinted <date>1846</date>, <biblScope unit="pp">p. 743</biblScope>.</bibl>
      <bibl xml:id="COLI-eg-172"><author>Butler, Samuel</author>. <title level="m">The Way of All
          Flesh</title> (<date>1903</date>), <biblScope unit="chap">chapter 37</biblScope>.</bibl>
      <bibl xml:id="VESTR-eg-5"><author>Byron, George Gordon</author>. <title>Don Juan</title>
          (<date>1819</date>), <biblScope unit="part">I.xxii</biblScope>.</bibl>
      <bibl xml:id="VEST-eg-5"><author>Byron, George Gordon</author>. <title level="a">Vision of
          Judgment</title> In <editor>E.H. Coleridge</editor> ed. <title level="m">The Poetical
          Works of Lord Byron</title>, <biblScope unit="part">viii</biblScope>, 1922.</bibl>

      <!--C-->

      <bibl xml:id="NDPER-eg-17"><title level="m">C 60/16 Fine Roll 6 HENRY III (28 October 1221-27
          October 1222)</title>, <biblScope unit="part">membrane 5, entry 154</biblScope>.</bibl>
      <bibl xml:id="biblzh-tw_n46" xml:lang="zh-TW">CBETA</bibl>
      <bibl xml:id="caedmon"><title>Cædmon's Hymn</title> in Bede's Historia Ecclesiastica (MS Kk.
        5. 16, Cambridge, University Library).</bibl>
      <bibl xml:id="MasCab">
        <title>Cabaret</title>. A musical play, with book by Joe Masteroff, lyrics by Fred Ebb, and
        music by John Kaner. Based on the play by John van Druten and stories by Christopher
        Isherwood. <date>1966</date></bibl>
      <bibl xml:id="COEDREG-eg-74">Edward Barkley, describing how Essex drove the Irish from the
        plains into the woods to freeze or famish in winter; quoted by <author>Canny, Nicholas
          P.</author>
        <title level="a">The Ideology of English Colonization: From Ireland to America</title>. In
          <editor>Stanley N. Katz</editor> and <editor>John M. Murrin</editor> eds. <title level="m">Colonial America: Essays in Politics and Social Development</title>, <edition>3d
          ed</edition>
        <pubPlace>New York</pubPlace>: <publisher>Knopf</publisher>, (<date>1983</date>), <biblScope unit="pp">p.53</biblScope>. <!--<note>Canny's footnote reads<quote
            rend="inline">See Devereux, <title level="m">Lives of
            Devereux</title>, I, 30-31, for Essex to Burghley, July 20, 1573, and
            ibid, 37-39, for Essex to Privy Council, Sept. 29, 1573. Barkley to
            Burghley, May 14, 1574, S.p.63/46, no. 15, P.R.O.</quote> </note>-->
      </bibl>
      <bibl xml:id="AI-BIBL-3">
        <author>Carroll, Lewis</author>. <title level="m">Through the Looking Glass, and what Alice
          found there</title>. (<date>1871</date>). </bibl>
      <bibl xml:id="fr-ex-catechisme" xml:lang="fr"><title>Catéchisme de l'Eglise
        catholique</title>, <date>1968</date>.</bibl>
      <bibl xml:id="VESA-eg-1">
        <author>Cavendish, Margaret</author>. <title level="a">Nature's Pictures</title>.
          <pubPlace>London</pubPlace>, <date>1656</date>. <publisher>Women Writers Online. Women
          Writers Project, Northeastern University</publisher>. <date>29 Mar.
        2015</date><!--  <ref target="https://www.wwp.northeastern.edu/texts/cavendish.natpix.html"
            >https://www.wwp.northeastern.edu/texts/cavendish.natpix.html</ref>
             temporarily removed until #1564 is resolved, i.e. WWP puts this somewhere that is not
             behind paywall. -->.</bibl>
      <bibl xml:id="fr-ex-TLFI" xml:lang="fr"><author>Centre national de la recherche scientifique
          (France). UMR 7118 ATILF</author>, <title><ref target="http://atilf.atilf.fr/tlf.htm">Le
            Trésor de la Langue Française Informatisé (TLFI)</ref></title>,
        <date>2004</date>.</bibl>
      <bibl xml:id="TSBAPA-eg-24"> Example recoded from <author>Chafe, W. </author>
        <title level="a">Adequacy, user-friendliness, and practicality in transcribing</title> In
          <editor>Leech, G.</editor>, <editor>G. Myers</editor>, <editor>J. Thomas</editor> eds.
          <title level="m">Spoken English on Computer: Transcription, Markup and
          Applications</title>. <pubPlace>Harlow</pubPlace>: <publisher>Longman</publisher>,
          <date>1995</date>.</bibl>
      <bibl xml:id="CORS5-eg-01">
        <author>Chandler, Lloyd.</author>
        <title level="a">Conversation with Death</title> (also known as <title level="a">Oh,
          Death</title>). In <title level="j">Journal of Folklore Research</title>, <biblScope unit="issue">41.2/3</biblScope>, (<date>2004</date>), <biblScope unit="pp">pp.
          125-126</biblScope>. </bibl>
      <bibl xml:id="Python"><author>Chapman, Graham</author>, <author>Cleese, John</author>,
          <author>Gilliam, Terry</author>, <author>Idle, Eric</author>, <author>Jones,
          Terry</author>. <title>The complete Monty Pythons Flying Circus</title>. </bibl>
      <bibl xml:id="pythonBrian"><author>Chapman, Graham</author>, <author>Cleese, John</author>,
          <author>Gilliam, Terry</author>, <author>Idle, Eric</author>, <author>Jones,
          Terry</author>. <title>Monty Python's Life of Brian</title> (<date>1979</date>).
        <!-- <ref target="www.youtube.com/watch?v=-xLUEMj6cwA"/>--></bibl>
      <bibl xml:id="PH-eg-11">
        <author>Chaucer, Geoffrey</author>. <title>Canterbury Tales</title>, f52r, in Holkham MS. </bibl>
      <bibl xml:id="VEST-eg-4">
        <author>Chaucer, Geoffrey</author>. <title level="a">The Tale of Sir Topas</title>, <title level="m">The Canterbury Tales</title>, In <editor>F. N. Robinson</editor> ed. <title level="m">The Works of Geoffrey Chaucer</title>, <edition>2nd edition</edition>
        <pubPlace>Boston</pubPlace>: <publisher>Houghton Mifflin Co.</publisher>,
        <date>1957</date>.</bibl>
      <bibl xml:id="biblzh-tw_n50" xml:lang="zh-TW">陳政彥，〈戰後臺灣現代詩論戰史研究〉，2007。</bibl>
      <bibl xml:id="CholNup">
        <author>Cholières, Nicolas de</author>, <title>La Forest Nuptiale</title>
        (<date>1600</date>). </bibl>
      <bibl xml:id="FS-eg-01">
        <author>Chomsky, Noam</author> and <author>Morris Halle</author>. <title>The Sound Pattern
          of English</title>. New York: Harper &amp; Row (<date>1968</date>), <biblScope unit="pp">p. 415</biblScope>. </bibl>
      <bibl xml:id="fr-ex-simjar" xml:lang="fr"><author>Claude Simon</author>
        <title>Le jardin des plantes</title>, <date>1997</date>, p 284</bibl>
      <bibl xml:id="AI-BIBL-1">
        <author>Cleaver, Eldridge</author>. <title level="m">Soul on Ice</title>. <pubPlace>New
          York</pubPlace> (<date>1968</date>). </bibl>
      <bibl xml:id="DSFRONT-eg-69">
        <title level="a">Cloud of Unknowing</title> In <editor>Hodgson, Phyllis</editor> ed. <title level="m">The Cloud of Unknowing and The Book of Privy Counselling</title>,
          <pubPlace>London</pubPlace>: <publisher>Oxford University Press</publisher>, <series>Early
          English Text Society</series>, <biblScope unit="vol">218</biblScope>, (<date>1944</date>). </bibl>
      <bibl xml:id="NDPER-eg-18"><author>Clover, Carol J.</author><title level="m">The Medieval
          Saga</title>, <pubPlace>Ithaca</pubPlace>: <publisher>Cornell University Press</publisher>
          (<date>1982</date>). </bibl>
      <bibl xml:id="DRPERF-eg-13">
        <author>Cocteau, Jean</author>. <title level="m">La Machine Infernale</title>.</bibl>
      <bibl xml:id="CONONO-eg-189"><author>Coleridge, Samuel Taylor</author>. <title level="m">The
          Rime of the Ancient Mariner</title>. In <author>Wordsworth, William</author> and
          <author>Samuel Taylor Coleridge</author>. <title level="m">Lyrical Ballads</title>
          (<date>1798</date>). </bibl>
      <bibl xml:id="VEST-eg-3"><author>Coleridge, Samuel Taylor</author>. <title level="a">Frost at
          Midnight</title> In <editor>E.H. Coleridge</editor> ed. <title level="m">Poetical
          Works</title>, <pubPlace>Oxford</pubPlace>: <publisher>Oxford University
        Press</publisher>, (<date>1967</date>), <biblScope unit="pp">p.240</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Colette-Ecole" xml:lang="fr"><author>Colette</author>, <title>Colette à
          l'école</title>, <date>1900</date>.</bibl>
      <bibl xml:id="DIC-CED">
        <title>Collins English Dictionary</title>, <edition>12th edition</edition>
        <pubPlace>Glasgow</pubPlace>: <publisher>Collins</publisher> (<date when="2014">2014</date>). </bibl>
      <bibl xml:id="DIC-CP">
        <title>Collins Pocket Dictionary of the English language</title>.
          <pubPlace>London</pubPlace>: <publisher>Collins</publisher>. </bibl>
      <bibl xml:id="DSOC-eg-34">
        <author>Collins, Wilkie</author>. <title level="m">The Moonstone</title>,
          <publisher>Penguin</publisher>, <biblScope unit="part">6th narrative</biblScope>.</bibl>
      <bibl xml:id="SA-BIBL-2">
        <author>Comenius, John Amos</author>. <title level="m">Orbis Pictus: a facsimile of the
          first English edition of 1659</title> (ed. <editor><forename>John</forename>
          <forename>E.</forename>
          <surname>Sadler</surname>
        </editor>) <publisher>Oxford University Press</publisher> (<date>1968</date>). </bibl>
      <bibl xml:id="NDORG-eg-34"><author>Cope, Thomas Pym</author>. <title level="m">Philadelphia
          merchant: the diary of Thomas P. Cope, 1800-1851</title>, <editor>Eliza Cope
          Harrison</editor> ed.</bibl>
      <bibl xml:id="fr-ex-Corneille_Place-Royale" xml:lang="fr"><author>Corneille, Pierre</author>,
          <title>La Place Royale ou L'Amoureux extravagant</title>, <date>1637</date>.</bibl>
      <bibl xml:id="fr-ex-Corneille_Theodore" xml:lang="fr"><author>Corneille, Pierre</author>,
          <title>Théodore, vierge et martyre : tragédie chrétienne</title>,
        <title>1646</title>.</bibl>
      <bibl xml:id="RESPONS-eg-02">
        <author>Cowley, Hannah</author>. <title level="m">The Runaway</title> (<date when="1813">1813</date>). </bibl>
      <bibl xml:id="DS-eg-02">
        <author>Crashaw, Richard</author>, ed. <editor>J.R. Tutin</editor>. <title level="m">The
          Poems of Richard Crashaw</title>. <edition>Muses Library Edition</edition>:
          (<date>1900</date>). </bibl>
      <bibl xml:id="CREELEY">
        <author>Creeley, Robert</author>
        <title>A counterpoint</title> in <title>For Love: Poems 1950-1960</title>
        (<date>1962</date>). </bibl>
      <bibl xml:id="biblzh-tw_n17" xml:lang="zh-TW">崔西．雪佛蘭。《戴珍珠耳環的少女》。台北：皇冠，2003。</bibl>

      <!--D-->

      <bibl xml:id="CONARS-eg-109"><author>Dallas, George Mifflin</author>. <title>Unpublished
          letter</title> cited in <editor>Russell F. Weigley</editor>, <editor>Nicholas B.
          Wainwright</editor>, <editor>Edwin Wolf</editor> eds. <title level="m">Philadelphia: A 300
          Year History</title>, <pubPlace>New York</pubPlace> and <pubPlace>London</pubPlace>:
          <publisher>W. W. Norton &amp; Company</publisher>, <date>1982</date>, <biblScope unit="pp">p. 349</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Danhauser" xml:lang="fr"><author>Danhauser, Adolphe-Leopold</author>,
          <title>Théorie de la musique</title>, <date>1872</date>.</bibl>
      <bibl xml:id="beagle">
        <author>Darwin, Charles</author>. <title>Narrative of the Surveying Voyages of His Majesty's
          ships Adventure and Beagle... volume 3 : Journal and Remarks (The Voyage of the
          Beagle)</title>, chap 3. <date>1839</date>. </bibl>
      <bibl xml:id="fr-ex-Daudet_lundi" xml:lang="fr"><author>Daudet, Alphonse</author>, <title>Les
          contes du lundi</title>, <date>1873</date>. </bibl>
      <bibl xml:id="WD-TWac">
        <author>Davenant, William</author>. <title level="m">The vvitts. A comedie, presented at the
          private house in Blacke Fryers, by his Majesties servants. The author VVilliam D'avenant,
          servant to Her Majestie.</title>
        <pubPlace>London</pubPlace>, <date>1636</date>. [STC S109311]</bibl>
      <bibl xml:id="PH-eg-02">
        <title>De Nutrimento et Nutribili, Tractatus 1</title>, fol 217r col b of Merton College
        Oxford MS O.2.1; in <ptr target="#PARKES"/> pl. 16.</bibl>
      <bibl xml:id="PH-eg-12">
        <title>Dean of Sarum Churchwardens' presentments</title>, 1731, Hurst; Wiltshire Record
        Office; transcribed by Donald A. Spaeth. </bibl>
      <bibl xml:id="defoeMoll"><author>Defoe, Daniel</author>. <title level="m">The Fortunes and
          Misfortunes of the Famous Moll Flanders</title> (<date>1722</date>).</bibl>
      <bibl xml:id="COLI-eg-176"><author>Defoe, Daniel</author>. <title level="m">Robinson
          Crusoe</title> (<date>1719</date>).</bibl>
      <bibl xml:id="AI-BIBL-2">
        <author>Defoe, Daniel</author>. <title level="m">Journal of the Plague Year</title>.
          <pubPlace>London</pubPlace> (<date>1722</date>). </bibl>
      <bibl xml:id="DR-eg-04">
        <author>Dekker, Thomas</author> and <author>Thomas Middleton</author>. <title>The Honest
          Whore, Part One</title> (<date>1604</date>). </bibl>
      <bibl xml:id="deloneyThom"><author>Deloney, Thomas</author>. <title>Thomas of Reading or the
          Sixe Worthie Yeomen of the West</title> (<date>1612</date>).</bibl>
      <bibl xml:id="fr-ex-Dennery-notations" xml:lang="fr"><author>Dennery, Annie</author>. <title level="a">Du mélos à la note : Les notations musicales au Moyen Age</title>, <title level="j">Médiévales</title>, <num>n° 3</num>
        <date>1983</date>.</bibl>
      <bibl xml:id="COHQHE-eg-14"><author>Dickens, Charles</author>. <title level="m">A Christmas
          Carol in Prose, Being a Ghost Story of Christmas</title>, <publisher>Chapman and
          Hall</publisher>, (<date>1843</date>), <biblScope unit="pp">p. 5, p.
        12</biblScope>.</bibl>
      <bibl xml:id="CONARS-eg-103"><author>Dickens, Charles</author>. <title level="m">Little
          Dorrit</title>, (<date>1857</date>).</bibl>
      <bibl xml:id="VEST-eg-1"><author>Dickinson, Emily</author>. <title level="a">1755</title> In
          <editor>Arthur Eastman</editor> et al. eds. <title level="m">The Norton Anthology of
          Poetry</title>, <pubPlace>New York</pubPlace>: <publisher>W.W. Norton</publisher>,
          <date>1970</date>, <biblScope unit="part">p.859</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Diderot-Corresp_SV" xml:lang="fr"><author>Diderot, Denis</author>,
          <title>Lettres à Sophie Volland</title>, <date>26 sept. 1762</date>.</bibl>
      <bibl xml:id="biblzh-tw_n40" xml:lang="zh-TW"> 〈第三屆第一次大會第一次會議記錄〉，臺灣省諮議會。</bibl>
      <bibl xml:id="DSOC-eg-33"><author>Disraeli, Benjamin</author>. <title level="m">Coningsby</title> (<date>1844</date>), <biblScope unit="part">preface</biblScope>.</bibl>
      <bibl xml:id="COHQQ-eg-26"><author>Doyle, Arthur Conan</author>. <title level="a">The
          Red-headed league</title>. In <title level="m">The Adventures of Sherlock Holmes</title>
          (<date>1892</date>).</bibl>
      <bibl xml:id="DSGRP-eg-57">
        <author>Doyle, Arthur Conan</author>. <title level="m">The Original Illustrated Sherlock
          Holmes</title>, <publisher>Castle Books</publisher>, <date>1989</date>.</bibl>
      <bibl xml:id="WD-BOUS"><title>Drawing of a leaden plaque bearing an inquiry by Hermon from the
          oracular precinct at Dodona</title>. Catalogue no 725; LSAG 230.13. Image from <ptr target="http://poinikastas.csad.ox.ac.uk/"/></bibl>
      <bibl xml:id="fr-ex-Babel" xml:lang="fr"><author>Dubois, Jacques</author>, <author>Nyssen,
          Hubert</author> (dir. de collection), <title>Babel</title>, <publisher>Actes
          sud</publisher>,<date>1989-...</date>.</bibl>
      <bibl xml:id="fr-ex-Dubois_Dict_Ling" xml:lang="fr"><author>Dubois, Jean</author>,
          <title>Dictionnaire de linguistique</title>, <date>1974</date>.</bibl>
      <bibl xml:id="PH-eg-04">
        <author>Dudo of St Quentin</author>. <title>De moribus et actis primorum Normannie
          ducum</title>, fol 4v of British Library MS Harley 3742; in <ptr target="#PARKES"/> pl
        6(i). </bibl>
      <bibl xml:id="fr-ex-Dufournaud" xml:lang="fr"><author>Dufournaud, Nicole</author>,
          <title>Numérisation des Titres de famille</title>, <ref target="http://nicole.dufournaud.net/these/adla/titresfamille/lebastard/2E3002/2E3002-0001.tei">édition électronique</ref>, <date>2002</date>. </bibl>
      <bibl xml:id="fr-ex-Duhamel-Pasquier" xml:lang="fr"><author>Duhamel, Georges</author>,
          <title>Chronique des Pasquier</title>, <date>1933-1945</date>.</bibl>
      <bibl xml:id="eg-rhyme-dutt">
        <author>Dutt, Toru</author>. <title level="a">Lakshman</title> In <title level="m">Ancient
          Ballads and Legends of Hindustan</title>, <publisher>Kegan Paul, Trench &amp;
          Co.</publisher>, (<date>1882</date>) </bibl>
      <bibl xml:id="VERH-eg-25"><author>Dylan, Bob</author>. <title level="a">All Along the
          Watchtower</title> In <title level="m">John Wesley Harding</title>
        (<date>1967</date>).</bibl>
      <bibl xml:id="pos4st"><author>Dylan, Bob</author>. <title level="a">Positively 4th
          Street</title> In <title level="m">Highway 61 Revisited</title>
        (<date>1965</date>).</bibl>

      <!--E-->

      <bibl xml:id="PH-eg-08">
        <title>Eddic poems</title>, in Reykjavík, Landsbókasafn Íslands, Lbs 1562 4to. </bibl>
      <bibl xml:id="CONAAB-eg-151"><title level="a">Editorial</title>, <title level="j">.EXE
          magazine</title>, <biblScope unit="issue">6.11 </biblScope> (<date>1992</date>),
          <biblScope unit="pp">p. 2</biblScope>.</bibl>
      <bibl xml:id="COHQQ-eg-28"><author>Eliot, George</author>. <title level="m">Middlemarch</title> (<date>1871</date>), <biblScope unit="chap"> I.1</biblScope>.</bibl>
      <bibl xml:id="SAID-DIRECT-eg-1">
        <author>Eliot, George</author>. <title level="m">Middlemarch</title> (<date>1871</date>),
          <biblScope unit="chap">I.XXI</biblScope>. </bibl>
      <bibl xml:id="DSAE-eg-38">
        <author>Eliot, George</author>. <title level="m">Daniel Deronda</title> (<date>1876</date>),
          <biblScope unit="chap">III.1</biblScope>.</bibl>
      <bibl xml:id="COEDADD-eg-89"><author>Eliot, Thomas Stearns</author>. <title level="m">The
          waste land: a facsimile and transcript of the original drafts including the annotations of
          Ezra Pound</title>, <editor>Eliot, Valerie</editor> ed. <publisher>Faber and Faber
          Ltd.</publisher> (<date>1971</date>), <biblScope unit="pp">p. 37</biblScope>.</bibl>
      <bibl xml:id="SVG-11">
        <title level="m">Scalable Vector Graphics (SVG) 1.1 (Second Edition)</title>. Editors
          <editor>Erik Dahlström</editor>, <editor>Jon Ferraiolo</editor>, <editor><seg xml:lang="ja">藤沢 淳</seg></editor>, <editor>Anthony Grasso</editor>, <editor>Dean
          Jackson</editor>, <editor>Chris Lilley</editor>, <editor>Cameron McCormack</editor>
        <editor>Doug Schepers</editor>, <editor>Jonathan Watt</editor> and <editor>Patrick
          Dengler</editor>. <publisher>World Wide Web Consortium (W3C)</publisher> (<date>22 June
          2010</date>). Available from <ptr target="https://www.w3.org/TR/SVG11/"/>. </bibl>
      <bibl xml:id="fr-ex-Ernaux-perdre" xml:lang="fr"><author>Ernaux, Annie</author>, <title>Se
          perdre</title>, <date>1988</date>.</bibl>
      <bibl xml:id="fr-ex-Ernaux-photo" xml:lang="fr"><author>Ernaux, Annie</author>, <title>L'usage
          de la photo</title>, <date>2005</date>.</bibl>
      <bibl xml:id="fr-ex-Etudes_Litt" xml:lang="fr">
        <title>
          <ref target="http://www.etudes-litteraires.com/figures-de-style/deictique.php">Études
            littéraires</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>

      <!--F-->

      <bibl xml:id="fr-ex-Constant-Journal" xml:lang="fr"><author>Fallet , René</author>, <title>Le
          Triporteur</title>, <date>1951</date>.</bibl>
      <bibl xml:id="FieldScreen"><author>Field, Syd</author>
        <title>Screenplay: the Foundations of Screenwriting</title> (<date>1998</date>).</bibl>
      <bibl xml:id="DSDIV3-eg-22"><author>Fielding, Henry</author>. <title level="a">The History of
          the Adventures of Joseph Andrews and his Friend, Mr. Abraham Abrams</title>
          (<date>1742</date>).</bibl>
      <bibl xml:id="DRCAST-eg-18">
        <author>Fielding, Henry</author>. <title level="m">Tragedy of Tragedies</title>,
          (<date>1737</date>).</bibl>
      <bibl xml:id="DS-eg-05">
        <author>Fish, Stanley</author>. <title>Is there a text in this class? The authority of
          interpretive communities</title>. <publisher>Harvard University Press</publisher>
          (<date>1980</date>). </bibl>
      <bibl xml:id="SAAG-eg-72"><author>Fisher, M. F. K. </author><title level="a">I Was Really Very
          Hungry</title> In <title level="m">As They Were</title>, <publisher> Knopf</publisher>
          (<date>1982</date>), <biblScope unit="pp">p. 43</biblScope>.</bibl>
      <bibl xml:id="fitrub">
        <!-- tip o the hat to John Lavignino -->
        <author>FitzGerald, Edward</author>. <title>The Rubáiyát of Omar Khayyám, translated into
          English Verse</title> (<date>1859</date>), <biblScope>stanza 25</biblScope>. </bibl>
      <bibl xml:id="fr-ex-Flaubert_Sal" xml:lang="fr"><author>Flaubert, Gustave</author>,
          <title>Salammbô</title>, <date>1862</date>.</bibl>
      <bibl xml:id="fr-ex-Flaubert_Tent" xml:lang="fr"><author>Flaubert, Gustave</author>, <title>
          La Tentation de saint Antoine</title>, <date>1874</date>.</bibl>
      <bibl xml:id="FTGRA-eg-18"><author>Foley James D.</author>, <author>Andries van Dam</author>,
          <author>Steven K. Feiner</author> and <author>John F. Hughes</author>. <title level="m">Computer Graphics: Principles and Practice</title>, <edition>2nd edition </edition>
        <pubPlace>Reading</pubPlace>: <publisher>Addison-Wesley</publisher>, <biblScope unit="pp">p.259</biblScope>.</bibl>
      <bibl xml:id="DSAE-eg-38a"><author>Forster, E.M.</author>, <title level="m">Howards
          End</title>. <publisher>Edward Arnold.</publisher> (<date>1910</date>). </bibl>
      <bibl xml:id="fr-ex-la-bas-si-jy-suis" xml:lang="fr">
        <title>
          <ref target="http://sites.radiofrance.fr/franceinter/em/labassijysuis">France inter,
            Là-bas si j'y suis</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
      <bibl xml:id="fr-ex-Teleph_sonne" xml:lang="fr">
        <title>
          <ref target="http://sites.radiofrance.fr/franceinter/em/letelephonesonne/contact.php">France inter, Le téléphone sonne</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
      <bibl xml:id="fr-ex-franglais" xml:lang="fr">
        <title>
          <ref target="http://franglais.ini.hu/">Franglais et franricain</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
      <bibl xml:id="FR1B"><author>Fry, Christopher</author>, <title>The firstborn</title>
          (<date>1948</date>).</bibl>
      <bibl xml:id="biblzh-tw_n34" xml:lang="zh-TW">福春嫁女</bibl>
      <bibl xml:id="DS-eg-03">
        <editor>Fussell, Paul</editor>. <title>The Norton Book of Travel</title>. <publisher> W. W.
          Norton</publisher> (<date>1987</date>). </bibl>

      <!--G -->

      <bibl xml:id="COEDADD-eg-83"><author>Galilei, Galileo</author>, <title level="m">Sidereus
          Nuncius</title>, <pubPlace>Venetiis</pubPlace>: <publisher>Apud Thomam
          Baglionum</publisher>, <date>1610</date>, quoted by <author>Tufte, Edward R.</author>,
          <title level="m">Envisioning Information</title>, <pubPlace>Cheshire</pubPlace>:
          <publisher>Graphics Press</publisher> (<date>1990</date>), <biblScope unit="pp">p.
          97</biblScope>. </bibl>
      <bibl xml:id="fr-ex-Galland_Mille" xml:lang="fr"><author>Galland, Antoine</author>,<title> Les
          Mille et une nuits</title>, <date>1704</date>.</bibl>
      <bibl xml:id="GalswStr"><author>Galsworthy, John</author>, <title level="m">Strife</title>. In
          <title>Plays, vol 1.</title> (<date>1909</date>). <!-- check --></bibl>
      <bibl xml:id="COEDADD-eg-84"><author>Gaskell, Elizabeth Cleghorn</author>. <title level="m">The Grey Woman</title>, MS.</bibl>
      <bibl xml:id="TSTPPR-eg-58"><author>Gavioli, Laura</author> and <author>Gillian
          Mansfield</author>. <title level="m">The PIXI corpora: bookshop encounters in English and
          Italian</title>, <pubPlace>Bologna</pubPlace>: <publisher>Cooperativa Libraria
          Universitaria Editrice</publisher> (<date>1990</date>), <biblScope unit="pp">p.74</biblScope>.</bibl>
      <bibl xml:id="COVE-eg-285"><author>Gay, John</author>. <title>The Beggar's Opera</title>
          (<date>1728</date>).</bibl>
      <bibl xml:id="COHTG-eg-43"><author>Gazdar, Gerald</author> and <author>Mellish,
          Christopher</author>. <title level="m">Natural language processing in Prolog</title>.
          <publisher>Addison-Wesley</publisher> (<date>1989</date>), <biblScope unit="pp">p.5</biblScope>.</bibl>
      <bibl xml:id="FS-BIBL-3">
        <author>Gazdar, Gerald</author>, <author>Ewan Klein, Geoffrey Pullum, and Ivan Sag</author>:
          <title level="m">Generalized Phrase Structure Grammar</title>, <publisher>Harvard
          University Press</publisher> (<date>1985</date>).</bibl>
      <bibl xml:id="GerStra">
        <author>Gershwin, Ira</author>
        <title>By Strauss</title> (from <title>An American in Paris</title>, <date>1953</date>). </bibl>
      <bibl xml:id="PHegsurp2"><editor>Gianfraco Contini</editor>, <title>Poeti del
        Duecento</title>, Milano-Napoli:Ricciardi I, (<date>1960</date>). pp 155-64.</bibl>
      <bibl xml:id="STGA-eg-11"><author>Gibbon, Edward</author>, <title level="m">The History of the
          Decline and Fall of the Roman Empire</title>, (<date>1789</date>), <biblScope unit="chap">chapter 58</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Gide-Journ_fx" xml:lang="fr"><author>Gide, André</author>, <title>Le
          Journal des Faux-Monnayeurs</title>, <date>1927</date>.</bibl>
      <bibl xml:id="fr-ex-Gide_Journal" xml:lang="fr"><author>Gide, André</author>, <title>Journal :
          1889-1939</title>, <date>1939</date>.</bibl>
      <bibl xml:id="DRPAL-eg-46">
        <author>Gilbert, William Schwenck</author> and <author>Sullivan, Arthur</author>. <title level="m">HMS Pinafore</title> (<date>1878</date>), <biblScope unit="part">I</biblScope>.</bibl>
      <bibl xml:id="COVE-eg-284"><author>Gilbert, William Schwenck</author> and <author>Sullivan,
          Arthur</author>. <title level="m">The Mikado</title> (<date>1885</date>).</bibl>
      <bibl xml:id="VEST-eg-2"><author>Ginsberg, Allen</author>. <title level="a">My alba</title>,
          <title level="m">Reality Sandwiches</title>, <pubPlace>San Francisco</pubPlace>:
          <publisher>City Lights</publisher>, (<date>1963</date>).</bibl>
      <bibl xml:id="fr-ex-Giono-Regain" xml:lang="fr"><author>Giono, Jean</author>,
          <title>Regain</title>, <date>1930</date>.</bibl>
      <bibl xml:id="fr-ex-Guerre-Troie" xml:lang="fr"><author>Giraudoux, Jean</author>, <title>La
          guerre de Troie n'aura pas lieu</title>, <date>1935</date>.</bibl>
      <bibl xml:id="fr-ex-Godefroy" xml:lang="fr">
        <author>Godefroy, Frédéric</author>, <title>Dictionnaire de l'ancienne langue française et
          de tous ses dialectes du IXe au XVe siècle</title>, <date>1881</date>.</bibl>
      <bibl xml:id="DRDIV-eg-31"><author>Goethe, Johann Wolfgang von</author>, tr. <editor role="tr">Philip Wayne</editor>. <title level="m">Faust</title>, <biblScope unit="part">Part
          1</biblScope>, <pubPlace>London</pubPlace>: Penguin. (<date>1949</date>).</bibl>
      <bibl xml:id="VE-eg-03">
        <author>Goethe, Johann Wolfgang von</author>. <title>Auf dem See</title>
        (<date>1775</date>). </bibl>
      <bibl xml:id="G2S">
        <author>[Goldsmith, Oliver]</author>, <title>The History of Little GOODY TWO-SHOES;
          Otherwise called, Mrs. MARGERY TWO-SHOES...</title> (Printed for J. Newbery,
          <date>1766</date>). </bibl>
      <bibl xml:id="HDUDECL-TG">
        <author>Grallert, Till</author>, <title>Tools for the Computational Normalisation and
          Analysis of Food Prices and Food Riots in the Eastern Mediterranean (Bilād al-Shām) in the
          19th and 20th Centuries</title>. <publisher>Zenodo</publisher>, <date>2021</date>. <ptr target="https://doi.org/10.5281/zenodo.5159020"/>. </bibl>
      <bibl xml:id="PH-eg-07">
        <author>Graves, Robert</author>. <title>Rough draft of letter to Desmond Flower</title>.
          <date>17 Dec 1938</date>. (from <title level="m">Diary of Robert Graves 1935-39 and
          ancillary materials</title>, compiled by Beryl Graves, C.G. Petter, L.R. Roberts,
        University of Victoria Libraries).</bibl>
      <bibl xml:id="DSBACK-eg-86">
        <author>Greene, Robert</author>. <title level="m">Groatsworth of Wit Bought with a Million
          of Repentance</title> (<date>1592</date>).</bibl>
      <bibl xml:id="DS-eg-01">
        <author>Gregory of Tours</author>. <title level="m">Ecclesiastical History of the
          Franks</title> (translated by Lewis Thorpe). </bibl>
      <bibl xml:id="fr-ex-Greimas_Courtes" xml:lang="fr"><author>Greimas, Algirdas Julien</author>
        et <author>Courtés, Joseph</author>, <title>Sémiotique : dictionnaire raisonné de la théorie
          du langage</title>, <date>1979</date>. </bibl>
      <bibl xml:id="COXR-eg-166"><author>Grune, Dick</author> and <author>Ceriel J. H.
          Jacobs</author>. <title level="m">Parsing Techniques: A Practical Guide</title>,
          <pubPlace>New York</pubPlace> and <pubPlace>London</pubPlace>: <publisher>Ellis
          Horwood</publisher>, <date>1990</date>, <biblScope unit="pp">p. 24</biblScope>.</bibl>
      <bibl xml:id="DIC-DNT">
        <editor>Guerard, Françoise</editor>. <title>Le Dictionnaire de Notre Temps</title>, ed.
          <pubPlace>Paris</pubPlace>: <publisher>Hachette</publisher>, <date>1990</date>
      </bibl>

      <!--H-->

      <bibl xml:id="hallWell"><author>Hall, Radclyffe</author>. <title>The well of
          loneliness</title>. (<date>1928</date>).</bibl>
      <bibl xml:id="CONAAB-eg-150"><author>Halliday, M.A.K. </author> and <author>R.
        Hassan</author>. <title level="m">Language, Context and Text: Aspects of Language in a
          Social-Semiotic Perspective</title>, <pubPlace>Oxford</pubPlace>: <publisher>Oxford
          University Press</publisher>, <date>1990</date>, <biblScope unit="pp">p.
        104</biblScope>.</bibl>
      <bibl xml:id="COHQQ-eg-29"><author>Hanks, Patrick</author>. <title level="a">Definitions and
          Explanations</title>. In <editor>J. M. Sinclair</editor> ed. <title level="m">Looking Up.
          </title><publisher>Collins</publisher>, <date>1987</date>, <biblScope unit="pp">p. 121
        </biblScope>.</bibl>
      <bibl xml:id="eebo87070"><title>Hannam's last farewell to the world:: being a full and true
          relation of the notorious life and shamfull death of Mr. Richard Hannam...</title>
          (<date>1656</date>).</bibl>
      <bibl xml:id="DR-eg-01">
        <author>Hansberry, Lorraine</author>. <title>A raisin in the sun. </title>
          (<date>1959</date>). </bibl>
      <bibl xml:id="harveyFour"><author>Harvey, Gabriel</author>. <title>Four letters and certain
          sonnets specially touching Robert Greene...</title> (<date>1592</date>).</bibl>
      <bibl xml:id="CO-eg-05"><author>Harvey, William</author>. <title>Exercitatio Anatomica De Motu
          Cordis Et Sanguinis In Animalibus</title>, <date>1949</date> (Third edition, second
        printing), <biblScope unit="page">p. 74</biblScope>. <ptr target="https://archive.org/details/in.ernet.dli.2015.115852/page/n98/mode/1up"/></bibl>
      <bibl xml:id="leviathan"><author>Hobbes, Thomas</author>. <title>Leviathan</title>
          (<date>1681</date>).</bibl>
      <bibl xml:id="biblzh-tw_n3" xml:lang="zh-TW">《紅樓夢》第六回：賈寶玉初試云雨情 劉姥姥一進榮國府</bibl>
      <bibl xml:id="biblzh-tw_n43" xml:lang="zh-TW">〈紅頭嶼踏查報告〉，國立台灣大學圖書館：田代文庫。</bibl>
      <bibl xml:id="fr-ex-Fleurs" xml:lang="fr"><author>Hoola Van Nooten,
          Berthe</author><title>Fleurs, fruits et feuillages choisis de l'île de Java peints d'après
          nature</title>, troisième édition par <publisher>C. Muquardt</publisher>, Bruxelles,
          <date>1880</date>.</bibl>
      <bibl xml:id="DIC-OALD">
        <editor>Hornby, A.S. et al</editor>. <title>Oxford Advanced Learner's Dictionary of Current
          English</title>. <publisher>Oxford University Press</publisher> (<date>1974</date>). </bibl>
      <bibl xml:id="biblzh-tw_n5" xml:lang="zh-TW">黃晨淳編著，《希臘羅馬神話故事》，p76。</bibl>
      <bibl xml:id="fr-ex-Hugo-Notre-Dame" xml:lang="fr"><author>Hugo, Victor</author>,
          <title>Notre-Dame de Paris</title>, <date>1845</date>.</bibl>
      <bibl xml:id="fr-ex-Hugo-Nuit" xml:lang="fr">
        <title level="a">Souvenir de la nuit du 4</title>, in : <author>Hugo, Victor</author>,
          <title level="m">Les Contemplations</title>, <date>1853</date>. </bibl>
      <bibl xml:id="fr-ex-Hugo-miserables" xml:lang="fr"><author>Hugo, Victor</author>, <title>Les
          Misérables</title>, <date>1862</date>.</bibl>
      <bibl xml:id="fr-ex-Hugo-Fen" xml:lang="fr">
        <title level="a">A la fenêtre pendant la nuit</title>, in : <author>Hugo, Victor </author>,
          <title level="m">Les Contemplations</title>, <date>1856</date>. </bibl>
      <bibl xml:id="fr-ex-Huizinga_Aut" xml:lang="fr"><author>Huizinga, Johan</author>,
          <title>L'Automne du Moyen-Âge</title>, <date>1919</date>.</bibl>

      <!--I-->

      <bibl xml:id="COBICOR-eg-248"><title level="m">ISO 690:1987: Information and documentation –
          Bibliographic references – Content, form and structure </title>
        <biblScope unit="part">clause 4.1</biblScope>, <biblScope unit="pp">p.2</biblScope>.</bibl>
      <bibl xml:id="ISO24611"><title level="m">ISO 24611:2012 Language resource management —
          Morpho-syntactic annotation framework (MAF)</title>. <author>International Organization
          for Standardization</author>. <date>2012</date>.</bibl>
      <bibl xml:id="DR-eg-02">
        <author>Ibsen, Henrik</author>, <editor role="tr"> tr. William and Charles Archer</editor>.
          <title>Peer Gynt</title> (<date>1875</date>).</bibl>
      <bibl xml:id="PH-ib01">
        <author>Ibsen, Henrik</author>
        <title>Den episke Brand</title> KBK Collin 2869, 4º I, fol. 11v. </bibl>
      <bibl xml:id="PH-ib04">
        <author>Ibsen, Henrik</author>
        <title>Digte</title> NBO Ms.4º 1110a, p. 36. </bibl>
      <bibl xml:id="PH-ib05">
        <author>Ibsen, Henrik</author>
        <title>Brand</title>, The Royal Library, Denmark. KBK Collin 262, 4°, I.1.1, fol.
        [4]v</bibl>
      <bibl xml:id="DRSTA-eg-40"><author>Ibsen, Henrik</author>, tr. <editor role="tr">R.
          Farquharson Sharp</editor> and <editor role="tr">Eleanor Marx-Aveling. </editor>
        <title level="m">A Doll's House</title> In <title level="m">A Doll's House; and Two Other
          Plays by Henrik Ibsen</title>, <series>Everyman's library: the drama <biblScope unit="vol">494</biblScope>
        </series>, <pubPlace>London</pubPlace>: <publisher>J. M. Dent &amp; Sons</publisher>,
          <date>1910</date>.</bibl>
      <bibl xml:id="DROTH-eg-58"><author>Idle, Eric</author>, <author>Michael Palin</author>,
          <author>Graham Chapman</author>, <author>John Cleese</author>, <author>Terry
          Gilliam</author>. <title level="m">The Complete Monty Python's Flying Circus: All the
          Words</title>, <publisher>Pantheon Books</publisher>, (<date>1989</date>), <biblScope unit="vol">2</biblScope>, <biblScope unit="pp">p.230</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Melanges_Imbs" xml:lang="fr"><author>Imbs, Paul</author>, <author>Martin,
          Robert</author>, <author>Straka, Georges</author>, <title>Mélanges de linguistique
          française et de philologie et littérature médiévales offerts à Monsieur Paul
          Imbs</title>, <date>1973 </date>.</bibl>
      <bibl xml:id="fr-ex-Cyrus" xml:lang="fr"><author>Institut de Littérature Française Moderne de
          l’Université de Neuchâtel</author>, <title>Présentation du projet Cyrus</title>, <ref target="http://www.artamene.org/projet.php">En ligne</ref>, <date>consulté le
          05-03-2010</date>.</bibl>
      <bibl xml:id="fr-ex-Ionesco-chauve" xml:lang="fr"><author>Ionesco, Eugène</author>, <title>La
          cantatrice chauve</title>, <date>1950</date>.</bibl>
      <bibl xml:id="biblzh-tw_n61" xml:lang="zh-TW">羅貫中，《三國演義》。</bibl>

      <!--J-->

      <bibl xml:id="TEI-L_b092ac32.2101">
        <author>Jakacki, Diane</author>. <title level="a">Schema question: further constraining
          @subtype based on @type</title>. <date when="2021-01-18T12:21:11-05:00">January 18,
          2021</date>. <title level="s">TEI (Text Encoding Initiative) public discussion
          list</title>, <ptr target="https://listserv.brown.edu/cgi-bin/wa?A2=TEI-L;b092ac32.2101"/>. </bibl>
      <bibl xml:id="DRDIV-eg-32"><author>Jarry, Alfred</author>, tr. <editor role="tr">Simon Watson
          Taylor</editor> and <editor role="tr">Cyril Connolly</editor>. <title level="m">The Ubu
          plays</title>, <pubPlace>London</pubPlace>: <publisher>Methuen</publisher>,
          <date>1968</date>.</bibl>
      <bibl xml:id="fr-ex-rousscon" xml:lang="fr"><author>Jean-Jacques Rousseau</author>
        <title>Les confessions</title> vol 6</bibl>
      <bibl xml:id="DSAE-eg-36"><author>Jerome, Jerome K. </author>
        <title level="m">Three men in a boat</title> (<date>1889</date>), <biblScope unit="chap">chapter 6</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Campe" xml:lang="fr"><author>Joachim Heinrich
          Campe</author><title>Wörterbuch der Deutschen Sprache. Erster Theil. A - bis - E.</title>,
          <date>1807</date>.</bibl>
      <bibl xml:id="GibAut"><author>John, Lord Sheffield</author>, <title level="m">The
          Auto-biography of Edward Gibbon esq.</title>, (<date>1846</date>), <biblScope unit="pp">222</biblScope>.</bibl>
      <bibl xml:id="JonsBart"><author>Jonson, Ben</author>. <title level="m">Bartholomew
          Fair</title>. </bibl>
      <bibl xml:id="DRSP-eg-37"><author>Jonson, Ben</author>. <title level="m">Volpone</title>,
          <editor>J. B. Bamborough</editor> ed. <publisher>Macmillan</publisher>, <date>1963</date>,
          <biblScope unit="pp">p.14</biblScope>.</bibl>
      <bibl xml:id="DRPAL-eg-44"><author>Jonson, Ben</author>. <title level="m">The Alchemist
        </title>, <editor>Douglas Brown</editor> ed. <pubPlace>London</pubPlace>:
          <publisher>Benn</publisher>, <date>1966</date>, <biblScope unit="part">I.1,
          </biblScope><biblScope unit="pp">p.9</biblScope>.</bibl>
      <bibl xml:id="DSCO-eg-53"><author>Joyce, James</author>. <title level="m">Ulysses</title>:
          <publisher>The Bodley Head</publisher>, <date>1960</date>. <biblScope unit="pp">p.
          933</biblScope>.</bibl>
      <bibl xml:id="WD-BASHO">
        <author>Judith Patt</author>, <author>Michiko Warkentyne</author> and <author>Barry
          Till</author>. <title>Haiku: Japanese Art and Poetry</title>. <date>2010</date>.
          <publisher>Pomegranate Communications, Inc. San Francisco. <ptr target="http://www.pomegranate.com"/>.</publisher>
      </bibl>

      <!--K-->

      <bibl xml:id="Karstadt-Distinctiones-Thomistarum"><author>Karlstadt, Andreas
          Bodenstein</author>. <title>Distinctiones Thomistarum</title>.
          <pubPlace>Wittenberg</pubPlace>
        <date>1507</date>. In <editor>Harald Bollbuck</editor> ed. <series>Kritische Gesamtausgabe
          Karlstadt</series>
        <biblScope unit="volume">I</biblScope>, available: <ptr target="http://diglib.hab.de/edoc/ed000216/start.htm"/>
      </bibl>
      <bibl xml:id="REF-cb-eg-1"><author>Kersey, John</author>. <title level="m">Dictionarium
          Anglo-Brittannicum: Or, a General English Dictionary</title>. <pubPlace>London</pubPlace>:
          <publisher>J. Wilde</publisher>, <date>1715</date>. <edition>2nd ed.</edition></bibl>
      <bibl xml:id="fr-ex-Kilian-Neige" xml:lang="fr"><author>Kilian, Wilfrid</author>, <title><ref target="http://jubil.upmc.fr/sdx/pl/toc.xsp?id=GH_000484_001&amp;fmt=upmc&amp;idtoc=GH_000484_001-pleadetoc&amp;base=fa">Neige et glaciers ; notes prises au cours de géologie de la Faculté des Sciences de
            Grenoble par M. Alamelle</ref></title>, <date>1891-1895</date>.</bibl>
      <bibl xml:id="MLK01"><author>King, Martin Luther</author>. <title>Letter from Birmingham City
          Jail</title>. <pubPlace>Philadelphia, PA</pubPlace>: <publisher>American Friends Service
          Committee</publisher> (<date>1963</date>).</bibl>
      <bibl xml:id="COHQHF-eg-5"><author>Kipling, Rudyard</author>. <title level="a">The mother
          hive</title>. In <title level="m">Actions and Reactions</title>,
          <pubPlace>London</pubPlace>: <publisher>Macmillan</publisher>, (<date>1909</date>).</bibl>
      <bibl xml:id="COHQHD-eg-18">
        <author>Kipling, Rudyard</author>. <title level="m">Stalky &amp; Co.</title>,
          <pubPlace>London</pubPlace>: <publisher>Macmillan</publisher> (<date>1899</date>). </bibl>
      <bibl xml:id="COHQQ-eg-27"><author>Kipling, Rudyard</author>. <title level="m">Kim</title>,
          <publisher>Macmillan</publisher>, (<date>1901</date>), <biblScope unit="pp">p.
          9</biblScope>.</bibl>
      <bibl xml:id="KNUTHMAD"><author>Knuth, Donald Ervin</author>. <title level="a">The Potrzebie
          System of Weights and Measures</title>, <title level="j">Mad Magazine</title><biblScope unit="issue">33</biblScope><date when="1957-06">June 1957</date>. </bibl>
      <bibl xml:id="fr-ex-Koltes_Quai_Vol" xml:lang="fr"><author>Koltès,
          Bernard-Marie</author>,<title> Quai ouest</title>, <date>1985</date>. </bibl>
      <bibl xml:id="PHegsurp"><author>Krummrey, Hans</author>, <author>Panciera, Silvio</author>
        <title>Criteri di edizione e segni diacritici</title>, Tituli 2 (<date>1980</date>),
        205-215.</bibl>
      <bibl xml:id="KYD"><author>Kyd, Thomas</author>. <title>Spanish Tragedy</title>
          (<date>1592</date>).</bibl>

      <!--L-->

      <bibl xml:id="RphCnd"><author>Lacy, M. Rophino</author>, <title level="m">Cinderella, 
          Or the Fairy-Queen and the Glass Slipper: A Comic Opera, In Three Acts</title>.
        <title level="s">Lacy's Acting Edition</title>, <biblScope unit="volume">volume 18</biblScope>:
        <biblScope unit="number">No. 0262</biblScope>, <pubPlace>London</pubPlace>: 
          <publisher>Thomas Hailes Lacy</publisher>, <biblScope unit="page">pp. 209–268</biblScope>. 
        <date notBefore="1849">undated</date>.</bibl>
      <bibl xml:id="fr-ex-Lafayette-Cleves" xml:lang="fr"><author>La Fayette, Marie-Madeleine Pioche
          de La Vergne, comtesse de</author>, <title>La Princesse de Clèves</title>,
          <date>1678</date>.</bibl>
      <bibl xml:id="VESE-eg-13"><author>La Fontaine, Jean de</author>. <title level="a">L'Astrologue
          qui se laisse tomber dans un puits</title> In <title level="m">Fables Choisies</title>,
          <series>Classiques Larousse</series>, <pubPlace>Paris</pubPlace>: <publisher>Librairie
          Larousse</publisher>, <biblScope unit="vol">1</biblScope>, <date>1940</date>.</bibl>
      <bibl xml:id="VESE-eg-13x"><author>La Fontaine, Jean de</author>. <title level="a">Le corbeau
          et le renard</title> In <title level="m">Fables Choisies</title>, <series>Classiques
          Larousse</series>, <pubPlace>Paris</pubPlace>: <publisher>Librairie Larousse</publisher>,
          <biblScope unit="vol">1</biblScope>, <date>1940</date>.</bibl>
      <bibl xml:id="fr-ex-ATILF" xml:lang="fr"><author>Laboratoire ATILF</author>
        <title>
          <ref target="http://www.atilf.fr/">Analyse et traitement informatique de la langue
            française (ATILF)</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
      <bibl xml:id="CONARS-eg-108">
        <author>Laclos, Pierre Choderlos de</author>. <title level="m">Les Liaisons
          dangereuses</title> (<date>1772</date>), <date>1963</date>, <biblScope unit="pp">p.
          13</biblScope>.</bibl>
      <bibl xml:id="CONARS-eg-111"><author>Ladurie, Emmanuel Le Roy</author>. <title level="m">Montaillou</title>, <pubPlace>Middlesex</pubPlace>: <publisher>Penguin Books</publisher>,
          <date>1980</date>, <biblScope unit="pp">p. 3</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Lamartine" xml:lang="fr"><author>Lamartine, Alphonse de</author>,
          <title>Méditations poétiques</title>, <date>1820</date>.</bibl>
      <bibl xml:id="fr-ex-manus-Saint-Petersbourg" xml:lang="fr"><author>Lamothe, Alexandre
          de</author>
        <title level="a">Principaux manuscrits latins et français conservés dans la Bibliothèque
          impériale et dans celle de l'Ermitage à Saint-Pétersbourg</title>, <ref target="http://www.persee.fr/web/revues/home/prescript/article/bec_0373-6237_1864_num_25_1_445928">édition numérique</ref>, <title level="s">Bibliothèque de l'école nationale des
          chartes</title>, <date>1864</date>. </bibl>
      <bibl xml:id="COHQQ-eg-33"><author>Langendoen, D. Terence</author> and <author>Paul M.
          Postal</author>. <title level="m">Vastness of Natural Languages</title>,
          <pubPlace>Oxford</pubPlace>: Basil Blackwell, <date>1984</date>, <biblScope unit="pp">p.
          24</biblScope>, <biblScope unit="note">note 12</biblScope>.</bibl>
      <bibl xml:id="LANGENPOST"><author>Langendoen, D. Terence and Paul Postal</author>. <title>The
          vastness of natural languages</title>, <publisher>Blackwell, </publisher>, <biblScope unit="pp">1</biblScope>, <date>1984</date>.</bibl>
      <bibl xml:id="VESE-eg-9">
        <author>Langland, William</author>. <title level="m">The Vision of Piers Plowman</title>. In
          <editor>A.V.C. Schmidt</editor> ed. <title level="m">Langland: Vision of Piers Plowman:
          "B" Text</title>, <biblScope unit="part">opening</biblScope>.</bibl>
      <bibl xml:id="punctuseg"><title>Latin liturgical manuscript: Bod MS. Lat liturg. b.
        19</title>, folio 4r. Taken from the digitized image described at <ptr target="https://www.diamm.ac.uk/sources/522/"/>.</bibl>
      <bibl xml:id="fr-ex-Lavrentev-TEI-BFM" xml:lang="fr"><author>Lavrentev, Alexei</author>,
            <title><ref target="http://ccfm.ens-lsh.fr/IMG/pdf/BFM-Mss_Encodage-XML.pdf">Manuel
            d’encodage XML-TEI étendu des transcriptions de manuscrits dans le projet
            BFM-Manuscrits</ref></title>, dernier enregistrement le <date>26 juin
        2008</date>.</bibl>
      <bibl xml:id="PH-eg-06">
        <author>Lawrence, David Herbert</author>. Autograph manuscript of <title>Eloi, Eloi, lama
          sabachthani</title>, Pierpont Morgan MA 1892; in <ptr target="#KLINKENBORG"/> p.129. </bibl>
      <bibl xml:id="PH-eg-01">
        <author>Layamon</author>. <title>Brut</title>, fol 65v of Bodleian MS. Rawlinson Poetry 32;
        in <ptr target="#PARKES"/> 12(ii). </bibl>
      <bibl xml:id="fr-ex-Grand-Robert" xml:lang="fr"><title>Le Grand Robert de la langue
          française</title>, <date>2004</date>. </bibl>
      <bibl xml:id="NH-eg-03"><author>LeTourneau, Mark S. </author>
        <title level="m">English Grammar</title>, <date>2001</date>, <pubPlace>New York</pubPlace>:
          <publisher>Harcourt</publisher>
        <biblScope>p. 89</biblScope>.</bibl>
      <bibl xml:id="SACS1-eg-48">
        <editor>Leech, G.</editor>, <editor>G. Myers</editor>, <editor>J. Thomas</editor> eds.
          <title level="m">Spoken English on Computer: Transcription, Markup and
          Applications</title>. <pubPlace>Harlow</pubPlace>: <publisher>Longman</publisher>,
          <date>1995</date>.</bibl>
      <bibl xml:id="COHTG-eg-42"><author>Leech, Geoffrey</author> and <author>Mick Short</author>.
          <title level="m">Style in Fiction</title>, <pubPlace>London</pubPlace>:
          <publisher>Longman</publisher>, <date>1981</date>, <biblScope unit="pp">p.272</biblScope>.</bibl>
      <bibl xml:id="COEDADD-eg-92">
        <author>Lennon, John</author> and <author>McCartney, Paul</author>. <title level="a">She
          Loves You</title>. <title level="m">The Beatles Anthology 1</title>.
          <publisher>Capitol</publisher>, <date>1995</date>. </bibl>
      <bibl xml:id="fr-ex-Lery" xml:lang="fr"><author>Léry, Jean de</author>, <title>Histoire faict
          en la terre de Brésil</title>, <date>1580</date>.</bibl>
      <bibl xml:id="AI-BIBL-4">
        <author>Lessing, Doris</author>. <title level="m">Martha Quest</title>. <date>1952</date>,
          <biblScope unit="pp">pp. 52-53</biblScope>. </bibl>
      <bibl xml:id="SERAFIN2"><title>Letter of Mikołaj Orlik to Mikołaj Serafin, Gródek, January 13
          [1438]</title>. Edited by <editor>Skolimowska et al.</editor> Available from <ptr target="https://teipublisher.com/exist/apps/serafin/letters/serafin02.xml"/></bibl>
      <bibl xml:id="DRCAST-eg-21"><author>Lewis, Leopold Davis</author>. <title level="m">The
          Bells</title>, (<date>1871</date>), translated from <author>Erckmann-Chatrian</author>,
          <title level="m">Le Juif Polonais</title>.</bibl>
      <bibl xml:id="COHQHE-eg-10">
        <author>Lewis, Wyndham</author>. <title level="m">Tarr</title> (1928),
          <publisher>Jupiter</publisher>, <date>1968</date>, <biblScope unit="pp">p. 17</biblScope>. </bibl>
      <bibl xml:id="biblzh-tw_n65" xml:lang="zh-TW">李白，《黃鶴樓送孟浩然之廣陵》。</bibl>
      <bibl xml:id="biblzh-tw_n37" xml:lang="zh-TW">李白，《靜夜思》。</bibl>
      <bibl xml:id="biblzh-tw_n23-24" xml:lang="zh-TW">《梁山伯與祝英台》</bibl>
      <bibl xml:id="biblzh-tw_n29" xml:lang="zh-TW">電影《梁山伯與祝英台》，舊版。</bibl>
      <bibl xml:id="biblzh-tw_n41" xml:lang="zh-TW">〈歷代漢文大藏經概述〉，李圓淨，原載《南行》第六期（南行學社編印）。</bibl>
      <bibl xml:id="bib4handnoteyi" xml:lang="en">
	<author>Libelt, Karol</author>.
	<title level="m" xml:lang="pl">Wykłady Humboldta na uniwersytecie Berlińskim: notaty prelekcyj tych po uczniu Jego Karolu Libelcie</title>,
	<publisher xml:lang="de">Deutsches Textarchiv</publisher>,
	<date>2024-04-02</date>.
	<idno type="URN">urn:nbn:de:kobv:b4-30960-7</idno>,
	<ptr target="https://www.deutschestextarchiv.de/book/download_xml/libelt_hs6623ii_1828"/>
	<date type="accessed" when="2024-12-04"/>
      </bibl>
      <bibl xml:id="DRPRO-eg-7"><author>Lillo, George</author>. <title level="m">The London
          Merchant</title> (<date>1731</date>), <biblScope unit="part">epilogue</biblScope>.</bibl>
      <bibl xml:id="biblzh-tw_n58" xml:lang="zh-TW">林覺民，《與妻訣別書》。</bibl>
      <bibl xml:id="STGA-eg-9"><author>Lincoln, Abraham</author>. <title level="a">Second Inaugural
          Address</title>, <date>4 March 1865</date>. In <editor>H. S. Commager</editor>, ed.,
          <title level="m">Documents of American History</title>, <edition> 5th ed
          </edition><series>Crofts American history series</series>. <pubPlace>New York</pubPlace>:
          <publisher>Appleton-Century-Crofts</publisher>, <date>1949</date>, <biblScope unit="pp">p.442</biblScope>. </bibl>
      <bibl xml:id="biblzh-tw_n51-55" xml:lang="zh-TW">劉康，《對話的喧囂：巴赫汀文化理論評述》，台北：麥田，2005，二版。</bibl>
      <bibl xml:id="biblzh-tw_n49" xml:lang="zh-TW">劉康，《對話的喧聲：巴赫汀文化理論述評》，台北：麥田，2005，頁20-23。</bibl>
      <bibl xml:id="DIC-LDOCE">
        <title>Longman Dictionary of Contemporary English</title>. <pubPlace>Harlow,
          Essex</pubPlace>: <publisher>Longman</publisher> (<date>1978</date>). </bibl>
      <bibl xml:id="fr-ex-Roman-Rose" xml:lang="fr"><author>Lorris, Guillaume de</author> et
          <author>Meun, Jean de</author><title>Le Roman de la Rose</title>, <date>1230,
          1270-1285</date>.</bibl>
      <bibl xml:id="FTGRA-eg-16"><author>Lowe, David</author>. <title level="m">Lost
        Chicago</title>, <pubPlace>Boston</pubPlace>: <publisher>Houghton Mifflin</publisher>,
          (<date>1978</date>), <biblScope unit="pp">p.30</biblScope>.
        <!--<biblScope unit="part">top. Ex libris Wendy Plotkin</biblScope>--></bibl>
      <bibl xml:id="lowellAut"><author>Lowell, Amy</author>. <title>Autumn
          haze</title>.(<date>1919</date>). </bibl>
      <bibl xml:id="fr-ex-Lichtig" xml:lang="fr"><author>Lucie Lichtig</author>, <title level="a">M.
          Klein de Joseph Losey : script</title>, . <title level="j">l'Avant-scène cinéma</title>,
          <num>n° 175</num>, <date>nov. 1976</date>. </bibl>
      <bibl xml:id="SASE-eg-41"><author>Luther, Martin</author> [tr]. <title level="m">Die gantze
          Heilige Schrifft Deudsch, Wittenberg 1545. Letzte zu Luthers Lebzeiten erchienene Ausgabe,
          hsg. Hans Volz unter Mitarbeit von Heinz Blanke. Textredaktion Friedrich Kur</title>,
          <pubPlace>München</pubPlace>: <publisher>Rogner &amp; Bernhard</publisher>,
          <date>1972</date>.</bibl>
      <bibl xml:id="biblzh-tw_n2" xml:lang="zh-TW">《論語》卷七：憲問第十四。</bibl>
      <bibl xml:id="biblzh-tw_n6" xml:lang="zh-TW"> 羅貫中，《三國演義》。</bibl>
      <bibl xml:id="biblzh-tw_n9" xml:lang="zh-TW">魯迅，《狂人日記 》。</bibl>
      <bibl xml:id="biblzh-tw_n15" xml:lang="zh-TW">魯迅，《狂人日記》。</bibl>
      <bibl xml:id="biblzh-tw_n16" xml:lang="zh-TW">魯迅，《狂人日記》。</bibl>

      <!--M-->

      <bibl xml:id="VERH-eg-27"><author>MacNeice, Louis</author>. <title level="a">The Sunlight on
          the Garden</title> In <editor>E.R. Dodds, </editor>
        <title level="m">The collected poems of Louis MacNeice</title>, <pubPlace>London</pubPlace>:
          <publisher>Faber</publisher>, <date>1966</date>.</bibl>
      <bibl xml:id="TSBA-eg-19"> Examples from <author>MacWhinney, Brian</author>, <biblScope unit="part">88, 87</biblScope>, cited by <author>Johansson, S. </author>
        <title level="a">The approach of the Text Encoding Initiative to the encoding of spoken
          discourse</title> In <editor>Leech, G.</editor>, <editor>G. Myers</editor>, <editor>J.
          Thomas</editor> eds. <title level="m">Spoken English on Computer: Transcription, Markup
          and Applications</title>. <pubPlace>Harlow</pubPlace>: <publisher>Longman</publisher>,
          <date>1995</date>.</bibl>
      <bibl xml:id="MS-eg-001">
        <author>Madan, Falconer, et al</author>, <title>A summary catalogue of western manuscripts
          in the Bodleian Library at Oxford which have not hitherto been catalogued ... </title>
        <pubPlace>Oxford</pubPlace>, <date>1895-1953</date>. <biblScope> 5: 515</biblScope>.
          <note>Cited in <bibl>Driscoll, M.J. <title level="a">P5-MS: A general purpose tagset for
              manuscript description</title> in <title level="j">Digital Medievalist</title>:
              <biblScope>2.1</biblScope>, <date>(2006)</date></bibl></note>
      </bibl>
      <bibl xml:id="fr-ex-Maingeneau_Analyser" xml:lang="fr"><author>Maingeneau, Dominique</author>,
          <title>Analyser les textes de communication</title>, <date>2007</date>.</bibl>
      <bibl xml:id="CONARS-eg-106">Any issue of the <title level="j">Malawi Daily Times.
        </title></bibl>
      <bibl xml:id="fr-ex-Zazie" xml:lang="fr"><author>Malle, Louis</author>, <title level="a">Zazie
          dans le métro : script</title>, <title level="j">l'Avant-scène cinéma</title>, <num>n°
          104</num>, <date>juin 1970</date>.</bibl>
      <bibl xml:id="fr-ex-Manu_Shan" xml:lang="fr">
        <author>Manuélian, Hélène</author>, <author>Schang, Emmanuel</author>, <title>XML, DTD et
          TEI pour un dictionnaire étymologique des créoles</title>, <ref target="http://www.dicorevue.fr/bilingues/10-07_deca_5.html/">édition électronique</ref>,
          <date>12 Octobre 2007</date>. </bibl>
      <bibl xml:id="PH-BIBL-1">
        <title level="a">The Manere of Good Lyuynge</title>: fol. 126v of Bodleian MS Laud Misc 517;
        in <ptr target="#PARKES"/>, p.8. </bibl>
      <bibl xml:id="STGA-eg-10"><title>Marbury v. Madison</title>, <biblScope unit="part">1 Cranch,
          137</biblScope> (<date>1803</date>), rpt. In <editor>H. S. Commager</editor>, ed., <title level="m">Documents of American History</title>, <edition> 5th ed</edition>
        <series>Crofts American history series</series>. <pubPlace>New York</pubPlace>:
          <publisher>Appleton-Century-Crofts</publisher>, <date>1949</date>,
          <biblScope>p.192</biblScope>.</bibl>
      <bibl xml:id="COEDADD-eg-85"><author>Marvell, Andrew</author>. <title level="m">An Horatian
          Ode</title>, Bod. MS Eng. Poet d.49.</bibl>
      <bibl xml:id="fr-ex-Mauriac-Marquise" xml:lang="fr"><author>Mauriac, Claude</author>, <title>
          La Marquise sortit à cinq heures</title>, <date>1961</date>.</bibl>
      <bibl xml:id="fr-ex-Mauss_Sociologie" xml:lang="fr"><author>Mauss, Marcel</author>,
          <title>Sociologie et anthropologie</title>, <date>1950</date>.</bibl>
      <bibl xml:id="NDGEOGste-Falls"><author>McCarthy, Niall</author>, <title level="a">No
          Parachute: The Highest Falls People Survived</title>, <title level="m">Statista</title>,
          <date when="2020-11-18">November 18, 2020</date>. <ptr target="https://www.statista.com/chart/19708/known-occasions-where-people-survived-falls/"/>. </bibl>
      <!-- See also https://en.wikipedia.org/wiki/Highest_falls_survived_without_a_parachute -->
      <bibl xml:id="SOURCE-eg-01"><author>McCarty, Willard</author>. <title level="a">Introduction</title> in <title level="m">Collaborative Research in the Digital
          Humanities</title>: A volume in honour of Harold Short on the occasion of his 65th
        birthday, September 2010, ed. <editor>Marilyn Deegan</editor> and <editor>Willard
          McCarty</editor>. <pubPlace>London</pubPlace>: <publisher>Ashgate</publisher>
          (<date>2012</date>).</bibl>
      <bibl xml:id="DSHD-eg-30"><author>Melville, Herman</author>, <title level="m">Moby
          Dick</title>. (<date>1851</date>).</bibl>
      <bibl xml:id="fr-ex-Mendes-France" xml:lang="fr"><author>Mendès-France, Pierre</author>,
          <title> Œuvres complètes</title>, <date>1984-1985</date>.</bibl>
      <bibl xml:id="biblzh-tw_n1" xml:lang="zh-TW">《孟子》〈三十三〉。 </bibl>
      <bibl xml:id="DRPERF-eg-12">
        <author>Miller, Henry</author>. <title level="a">Death of a Salesman</title> in
          <editor>Atkinson, Brooks, </editor>
        <title level="m">New Voices in the American Theatre</title>, <pubPlace>New York</pubPlace>:
          <publisher>Modern Library</publisher>, <date>1955</date>, <biblScope unit="pp">p.113</biblScope>.</bibl>
      <bibl xml:id="COHQHE-eg-11">
        <author>Milne, A. A. </author>
        <title level="m">The House at Pooh Corner</title>. <pubPlace>London</pubPlace>:
          <publisher>Methuen &amp; Co.</publisher>, <date>1928</date>, <biblScope unit="pp">p.
          83</biblScope>.</bibl>
      <bibl xml:id="CO-eg-06">
        <author>Milton, John</author>. <title>Paradise Lost: A poem in X books</title>
          (<date>1667</date>), <biblScope>I, 1-10</biblScope>. </bibl>
      <bibl xml:id="miltPo"><author>Milton, John</author>. <title>Poems of Mr John Milton, both
          English and Latin...</title> (<date>1645</date>). </bibl>
      <bibl xml:id="fr-ex-Moliere_Ecole" xml:lang="fr"><author>Molière</author>, <title>L'École des
          femmes</title>,<date> 1663</date>.</bibl>
      <bibl xml:id="fr-ex-Moliere_Med" xml:lang="fr"><author>Molière</author>, <title>Le Médecin
          malgré lui</title>, <date>1667</date>.</bibl>
      <bibl xml:id="fr-ex-Moliere_Med_Vol" xml:lang="fr"><author>Molière</author>, <title>Le Médecin
          volant</title>, <date>1673</date>.</bibl>
      <bibl xml:id="fr-ex-Montaigne_Essais" xml:lang="fr"><author>Montaigne, Michel de</author>,
          <title>Essais</title>, <date>1592</date>.</bibl>
      <bibl xml:id="fr-ex-Montesquieu" xml:lang="fr"><author>Montesquieu, Charles-Louis de Secondat,
          baron de la Brède et de</author>, <title> Lettres persanes</title>,
        <date>1721</date>.</bibl>
      <bibl xml:id="fr-ex-Montherlant-Pitie" xml:lang="fr"><author>Montherlant, Henry de </author>,
          <title>Pitié pour les femmes</title>, <date>1936</date>.</bibl>
      <bibl xml:id="PH-eg-03">
        <author>Moore, George</author>. Autograph manuscript of <title>Memoirs of my dead
          life</title>, Pierpont Morgan MA 3421; in <ptr target="#KLINKENBORG"/></bibl>
      <bibl xml:id="PH-eg-09">
        <author>Moore, Thomas</author>. Autograph manuscript of the second version of <title>Lalla
          Rookh</title>, Pierpont Morgan MA 310; in <ptr target="#KLINKENBORG"/> 23. </bibl>
      <bibl xml:id="CO-eg-04">
        <author>Moreland, Floyd L.</author> and <author>Rita M. Fleischer</author>. <title>Latin: An
          Intensive Course, </title> (<date>1977</date>) <biblScope>p.53</biblScope>. </bibl>
      <bibl xml:id="COBICOR-eg-251">
        <title>Des Minnesangs Frühling</title>, <editor>Moser, Hugo</editor>, <editor>Helmut
          Tervooren</editor> eds. <edition>36., neugestaltete und erweiterte Auflage</edition>
        <biblScope unit="vol">I Texte</biblScope>, <pubPlace>Stuttgart</pubPlace>: <publisher>S.
          Hirzel Verlag</publisher>, <date>1977</date>.</bibl>
      <bibl xml:id="msph1sup-wtrmrk"><author>Mošin, Vladimir A</author>. <title level="m">Anchor
          Watermarks</title>. <pubPlace>Amsterdam</pubPlace>: <publisher>Paper Publications Society
          (Labarre Foundation)</publisher>, <date>1973</date>. <series>Monumenta Chartæ Papyraceæ
          Historiam Illustrantia</series>; <biblScope unit="volume" n="13">v. 13</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Mrejen_Eau" xml:lang="fr"><author>Mréjen, Valérie</author>, <title>Eau
          sauvage</title>, <date>2004</date>.</bibl>
      <bibl xml:id="SA-eg-04">
        <title level="a">Zuigan calls himself "Master"</title>. <author>Mumon Ekai</author>. (In
          <title level="m">The Gateless Gate</title>, Case 12.) </bibl>
      <bibl xml:id="fr-ex-Hydraul" xml:lang="fr"><editor>Mustafa Siddik Altinakar</editor>,
          <editor>René Walther</editor> (éds.), <title>Hydraulique fluviale. Tome 16, Écoulement et
          phénomènes de transport dans les canaux à géométrie simple </title>,
        <date>2008</date>.</bibl>
      <bibl xml:id="fr-ex-Tunis" xml:lang="fr"><editor>Mégnin, Michel</editor> (éd.), <title>Tunis
          1900 Lehnert &amp; Landrock photographes</title>,<date>2005</date>.</bibl>
      <bibl xml:id="PNIN1">
        <author>Nabokov, Vladimir</author>
        <title>Pnin</title> (1953) <biblScope>, p.14 </biblScope><!--of 1967 Avon pb reprinting-->
      </bibl>
      <bibl xml:id="DIC-NPEG">
        <title>The New Penguin English Dictionary</title>. <pubPlace>London</pubPlace>:
          <publisher>Penguin Books</publisher> (<date>1986</date>). </bibl>
      <bibl xml:id="NZPaV01NgaK"> Derived from <author>New Zealand Parliament, Legislative
          Council</author>. <title>Nga Korero Paramete: 1881-1885</title> (<series><title>New
            Zealand Electronic Text Collection</title></series>). <date>2008</date>
        <pubPlace>Wellington, New Zealand</pubPlace>. <ptr target="https://nzetc.victoria.ac.nz/tei-source/NZPaV01NgaK.xml"/>. </bibl>
      <bibl xml:id="NJAL">
        <title level="m">Njal's saga</title>. tr. <editor>Magnus Magnusson and Hermann
          Palsson</editor>. <publisher>Penguin</publisher>. (<date>1960</date>), <biblScope>chapter
          12, p.60</biblScope>.</bibl>
      <bibl xml:id="DR-eg-07">
        <author>O'Casey, Sean</author>. <title>Time to go</title> (<date>1951</date>). </bibl>
      <bibl xml:id="fr-ex-Ollagnier_Main" xml:lang="fr"><author>Ollagnier, Jeanne</author>,
          <title>Main</title>, <date>2008</date>.</bibl>
      <bibl xml:id="ND-eg-99"> Herodotus. <title>On Libya</title>, from the
        <title>Histories</title>. </bibl>
      <bibl xml:id="CH-eg-01">
        <title>[Letter of Capt. E. Hopkins. Providence, 10 Sep 1764] </title>
      </bibl>
      <bibl xml:id="WHITMS1">"[I am a curse]" in <title>Original Manuscript Drafts for the Song of
          Myself</title>, Collection MSS3829, part of the Papers of Walt Whitman, Clifton Waller
        Barrett Library of American Literature, Albert and Shirley Small Special Collections
        Library, University of Virginia. </bibl>
      <bibl xml:id="fr-ex-Ormesson-douane" xml:lang="fr"><author>Ormesson, Jean d'</author>, <title level="m">La Douane de mer</title>, <date>1993</date>.</bibl>
      <bibl xml:id="SA-eg-03">
        <author>Orwell, George</author>. <title>Nineteen-Eighty-Four</title>.
          <pubPlace>London</pubPlace>: <publisher>Gollancz</publisher> (<date>1949</date>). </bibl>
      <bibl xml:lang="ja" xml:id="ja-ritsuryo-weights">
        <author>大隅亜希子</author>. <date when="1996">1996</date>. <title level="a">律令制下における権衡普及の実態:
          海産物の貢納単位を中心として</title>. <title level="j">史論</title>
        <biblScope unit="issue">49</biblScope>. <biblScope unit="pp">pp. 22–44</biblScope>. <ptr target="http://id.nii.ac.jp/1632/00015761/"/>. </bibl>
      <bibl xml:id="PH-eg-16">
        <author>Owen, Wilfred</author>. <title>Dulce et decorum est</title>, from autograph
        manuscript in the English Faculty Library, Oxford University. </bibl>
      <bibl xml:id="COEDADD-eg-90">
        <author>Owenson, Sydney</author>. <title level="m">The Wild Irish Girl</title>. Ed.
          <editor>Kathryn Kirkpatrick</editor>. <pubPlace>Oxford</pubPlace>: <publisher>Oxford
          University Press</publisher>, <date>1999</date>, <biblScope unit="page">p. 17</biblScope>. </bibl>

      <!--P-->

      <bibl xml:id="biblzh-tw_n39" xml:lang="zh-TW">擺夷文經，中央研究院歷史語言研究所 。 </bibl>
      <bibl xml:id="fr-ex-Pascal_Pensees" xml:lang="fr"><author>Pascal, Blaise</author>, <title level="a">Le Mémorial</title>, in <title level="m">Pensées</title>,<date>1670</date>.</bibl>
      <bibl xml:id="TSSASE-eg-37">
        <author>Payne, J. </author>
        <title level="a">Report on the compatibility of J P French's spoken corpus transcription
          conventions with the TEI guidelines for transcription of spoken texts</title>, <title level="m">Working Paper</title>, <date>Dec 1992</date>, NERC WP8/WP4 122.</bibl>
      <bibl xml:id="CODR-eg-296">
        <author>Peacock, Thomas Love</author>. <title level="m">Gryll Grange</title>
          (<date>1861</date>), <biblScope unit="chap">chapter 1</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Pennac_Marchande" xml:lang="fr"><author>Pennac, Daniel </author>,
          <title>La Petite marchande de prose</title>, <date>1978</date>.</bibl>
      <bibl xml:id="fr-ex-Perec-esp" xml:lang="fr"><author>Perec, Georges</author>, <title>Espèces
          d'espaces</title>, <date>1974</date>.</bibl>
      <bibl xml:id="fr-ex-Perec-vie" xml:lang="fr"><author>Perec, Georges</author>, <title>La Vie
          mode d'emploi : romans</title>, <date>1978</date>.</bibl>
      <bibl xml:id="fr-ex-Perec-choses" xml:lang="fr"><author>Perec, Georges </author>, <title>Les
          Choses</title>, <date>1965</date>.</bibl>
      <bibl xml:id="GDFT-eg-12"><title level="a">Partial family tree for Bertrand Russell</title>
        based on an example in <author>Pereira, Fernando C.N.</author> and <author>Stuart M.
          Shieber</author>, <title level="m">Prolog and Natural Language Analysis</title>,
          <pubPlace>Stanford</pubPlace>: <publisher>Center for the Study of Language and
          Information</publisher>. (<date>1987</date>), <biblScope unit="pp">p.22</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Pernoud-femme" xml:lang="fr"><author>Pernoud, Régine</author>, <title>La
          Femme au temps des Cathédrales</title>, <date>1982</date>.</bibl>
      <bibl xml:id="vcard"><author>Perreault, Simon</author>, <title>vCard Format
          Specification</title>
        <publisher>Internet Engineering Task Force (IETF)</publisher> (<date>2011</date>). <ptr target="https://datatracker.ietf.org/doc/html/rfc6350"/>.</bibl>
      <bibl xml:id="DIC-PLC">
        <title>Petit Larousse en Couleurs</title>. <pubPlace>Paris</pubPlace>:
          <publisher>Larousse</publisher>, (<date>1990</date>). </bibl>
      <bibl xml:id="PHILIPOTT">
        <author>Philipott, Thomas</author>
        <title>Poems.</title> (<date>1646</date>). </bibl>
      <bibl xml:id="NH-eg-02">
        <author>Pinsky, Robert</author>. <title level="a">Essays on Psychiatrists</title> in <title level="m">Sadness and Happiness</title> (<date>1975</date>). </bibl>
      <bibl xml:id="toWhom-eg-1"><author>Pix, Mary</author>. <title>The False Friend</title>
          (<date>1699</date>).</bibl>
      <bibl xml:id="PHOM-eg-secl"><author>Plautus, Titus Macchius</author>. <title>Asinaria, or the
          Comedy of Asses</title>. Edited and translated by <author>Wolfgang de Melo</author>. Loeb
        Classical Library 60. <pubPlace>Cambridge, MA</pubPlace>: <publisher>Harvard University
          Press</publisher> (<date>2011</date>).</bibl>
      <bibl xml:id="DRSP-eg-34"><author>Plautus, Titus Macchius</author>. <title level="m">Menaechmi</title>.</bibl>
      <bibl xml:id="fr-ex-Polac" xml:lang="fr"><author>Polac, Michel</author>, <title level="a">Un
          fils unique : script</title>, <title level="j">l'Avant-scène cinéma</title>, <num>n°
          99</num>, <date>janvier. 1970</date>.</bibl>
      <bibl xml:id="COHQHE-eg-12">
        <author>Pope, Alexander</author>. <title level="a">The Rape of the Lock</title>
          (<date>1714</date>) <biblScope unit="part">III.7</biblScope>.</bibl>
      <bibl xml:id="VEMEsamp-eg-14"><author>Pope, Alexander</author>. <title level="m">An Essay on
          Criticism</title> (<date>1711</date>).</bibl>
      <bibl xml:id="SAPTEG-eg-3"><author>Pope, Alexander</author>. <title>Dunciad Variorum</title>
          (<date>1729</date>), <biblScope unit="part">III.284</biblScope>.</bibl>
      <bibl xml:id="NDPLAC-eg-55">From letter 'JK' found in <title level="j">Poulson's Daily
          Advertiser, </title>
        <date>8 Oct 1835</date>.</bibl>
      <bibl xml:id="fr-ex-Proust-Swann" xml:lang="fr"><author>Proust, Marcel</author>, <title>A la
          recherche du temps perdu : Du côté de chez Swann</title>, <date>1913</date>.</bibl>
      <bibl xml:id="COHQQ-eg-23"><author>Queneau, Raymond</author>. <title level="m">Exercices de
          style</title>. <pubPlace>Paris</pubPlace>: <publisher>Gallimard</publisher>,
          (<date>1947</date>), <biblScope>p. 192</biblScope>.</bibl>

      <!--Q-->

      <bibl xml:id="biblzh-tw_n52" xml:lang="zh-TW">瓊瑤，《還珠格格》。</bibl>
      <bibl xml:id="fr-ex-Queneau_Journ" xml:lang="fr"><author>Queneau, Raymond</author> ,
          <title>Journaux</title>, <date>1914-1965</date>.</bibl>

      <!--R-->

      <bibl xml:id="fr-ex-garg" xml:lang="fr"><author>Rabelais, François</author>.
          <title>Gargantua</title> Lyon, <date>1542</date></bibl>
      <bibl xml:id="rab3" xml:lang="fr"><author>Rabelais, François</author>
        <title>Tiers livre des faictz et dictz Heroïques du noble Pantagruel...</title>
          (<date>1546</date>), adapted from the website at <ptr target="http://www.bvh.univ-tours.fr/Epistemon/"/></bibl>
      <bibl xml:id="fr-ex-Renard_Journal" xml:lang="fr"><author>Renard, Jules</author>,
          <title>Journal : 1887-1910</title>, <date>1910</date>.</bibl>
      <bibl xml:id="COBICOI-eg-264">Reference from the bibliography in <author>Reps, Thomas
          William</author> and <author>Teitelbaum, Tim</author> eds. <title level="m">The
          Synthesizer Generator: A system for constructing language-based editors</title>,
          <pubPlace>New York</pubPlace> and <pubPlace>Berlin</pubPlace>:
          <publisher>Springer-Verlag</publisher>, <date>1989</date>, <biblScope unit="pp">p.304</biblScope>.</bibl>
      <bibl xml:id="biblzh-tw_n45" xml:lang="zh-TW">日本法隆寺貝葉心經 (Wikipedia Sept 2008).</bibl>
      <bibl xml:id="COHTGEG-eg-02"><author>Richardson, Samuel</author>. <title level="m">Clarissa;
          or the History of a Young Lady</title> (<date>1748</date>), <biblScope unit="vol">2</biblScope> Letter XIV.</bibl>
      <bibl xml:id="DIC-PR">
        <editor>Robert, Paul</editor>. <title>Le Petit Robert</title>. <pubPlace>Paris</pubPlace>:
          <publisher>Dictionnaires Le Robert</publisher> (<date>1967</date>). </bibl>
      <bibl xml:id="fr-ex-Rohmer-Maud" xml:lang="fr"><author>Rohmer, Eric</author>, <title level="a">Ma nuit chez Maud : script</title>, <title level="j">l'Avant-scène cinéma</title>,
          <num>n°98</num>, <date>2001</date>.</bibl>
      <bibl xml:id="fr-ex-Knock" xml:lang="fr"><author>Romains, Jules</author>, <title>
          Knock</title>, <date>1923</date>. </bibl>
      <bibl xml:id="fr-ex-Cyrano" xml:lang="fr"><author>Rostand, Edmond</author>, <title>Cyrano de
          Bergerac</title>, <date>1898</date>.</bibl>
      <bibl xml:id="fr-ex-Roubaud_Boucle" xml:lang="fr"><author>Roubaud, Jacques</author>, <title>La
          Boucle</title>, <date>1993</date>.</bibl>
      <bibl xml:id="COHQQ-eg-35"><author>Rowling, J. K.</author>
        <title level="a">The Sorting Hat</title>. In <title level="m">Harry Potter and the
          Sorcerer's Stone</title>, <pubPlace>New York</pubPlace>: <publisher>Scholastic,
          Inc.</publisher> (<date>1999</date>), <biblScope unit="chap">chapter 7</biblScope>,
          <biblScope unit="pp">p. 121</biblScope>.</bibl>

      <!--S-->

      <bibl xml:id="AI-eg-01">
        <title level="m">The Saga of the Volsungs: the Norse epic of Sigurd the Dragon
          Slayer</title>. trans. <editor role="tr">Jesse L. Byock</editor>. <publisher>University of
          California Press</publisher> (<date>1990</date>). </bibl>
      <bibl xml:id="fr-ex-Sanctoral-ee" xml:lang="fr"><title>Le Sanctoral du lectionnaire de
          l'office dominicain (ms. Rome, Sainte-Sabine XIV L 1, f.142r et 189r-230v, Ecclesiasticum
          officium secundum ordinem fratrum praedicatorum)</title>, <ref target="http://elec.enc.sorbonne.fr/sanctoral/">édition électronique</ref> par
          l'<editor>Ecole nationale des chartes</editor>, d'après l'édition d'<editor>Anne-Élisabeth
          Urfels-Capot</editor> (Paris : Ecole nationale des chartes, 2007).</bibl>
      <bibl xml:id="WD-VERT-IND" xml:lang="ja">
        <author>崎山理</author>. <date>1985</date>
        <title level="a">インドネシア語</title>. <title level="s">講座日本語学</title>
        <edition>11</edition>. <title level="m">外国語との対照II</title>.
          <pubPlace>東京</pubPlace>:<publisher>明治書院</publisher>
        <biblScope unit="pp">61-80</biblScope>
      </bibl>
      <bibl xml:id="biblzh-tw_n7" xml:lang="zh-TW">三毛，〈沙漠中的飯店〉，《撒哈拉的故事》。 </bibl>
      <bibl xml:id="biblzh-tw_n48" xml:lang="zh-TW"> 《三家詩鈔》，華培昌，藏於國家圖書館。</bibl>
      <bibl xml:id="COHTG-eg-44"><author>Sapir, Edward</author>. <title level="m"> Language: an
          introduction to the study of speech</title>, <pubPlace>New York</pubPlace>:
          <publisher>Harcourt, Brace and World</publisher>, <date>1921</date>, <biblScope unit="pp">p.79</biblScope>.</bibl>
      <bibl xml:id="DRPERF-eg-13.1"><author>Selby, Charles</author>. <title level="m">A Day in Paris. A farce in one act</title>, <pubPlace>London</pubPlace>: <publisher> T.H. Lacy</publisher>. (Lacy's Acting Edition, volume 69, No. 1025)</bibl>
      <bibl xml:id="fr-ex-Shakes-Richard-III" xml:lang="fr"><author>Shakespeare William</author>,
          <title>Richard III</title>, <date>1597</date>.</bibl>
      <bibl xml:id="FHENRY5"><author>Shakespeare, William</author>. <title level="m">Henry V</title>
        In <title level="m">Mr. William Shakespeares Comedies, Histories, &amp; Tragedies</title>,
          <pubPlace>London</pubPlace>: <publisher>Jaggard and Blount</publisher>,
        <date>1623</date>.</bibl>
      <bibl xml:id="THENRY5"><author>Shakespeare, William</author>. <title level="m">Henry V</title>
        In <title level="m">The Works of Shakespeare in seven volumes</title>, ed. <editor>Lewis
          Theobald</editor>, <pubPlace>London</pubPlace>: <publisher>Bettesworth, Hitch, Tonson et
          al</publisher>, (<date>1733</date>).</bibl>
      <bibl xml:id="CO-eg-07"><author>Shakespeare, William</author>. <title level="m">Antony and
          Cleopatra</title>, <biblScope unit="part">IV.4, 14-21</biblScope>. </bibl>
      <bibl xml:id="STGA-eg-6"><author>Shakespeare, William</author>. <title level="m">Merchant of
          Venice</title>, <biblScope unit="part">I.ii, speech 5 (Portia)</biblScope>.</bibl>
      <bibl xml:id="DR-eg-05"><author>Shakespeare, William</author>. <title level="m">Macbeth</title>, <biblScope unit="part">Act V, Scene 1</biblScope>.</bibl>
      <bibl xml:id="COEDCOR-eg-64"><author>Shakespeare, William</author>. <title level="m">Antony
          and Cleopatra</title> (<date>1623</date>), <biblScope unit="part">V.
        ii</biblScope>.</bibl>
      <bibl xml:id="CODR-eg-293"><author>Shakespeare, William</author>. <title level="a">Hamlet</title> In <editor>Stanley Wells</editor> and <editor>Gary Taylor</editor> eds.
          <title>The Complete Works</title>, <pubPlace>Oxford</pubPlace>: <publisher>Clarendon
          Press</publisher>, <date>1986</date>, <biblScope unit="part">I.i</biblScope>.</bibl>
      <bibl xml:id="CODR-eg-294"><author>Shakespeare, William</author>. <title level="m">Hamlet</title>, <pubPlace>London</pubPlace>:<publisher> Valentine Simmes</publisher>.
          (<date>1603</date>), <biblScope unit="part">I.i</biblScope>.</bibl>
      <bibl xml:id="CODR-eg-295"><author>Shakespeare, William</author>. <title level="a">The Tempest
        </title> In <title level="m">Mr. William Shakespeares Comedies, Histories, &amp;
          Tragedies</title>, <pubPlace>London</pubPlace>: <publisher>Jaggard and Blount</publisher>,
          (<date>1623</date>).</bibl>
      <bibl xml:id="TwN"><author>Shakespeare, William</author>. <title level="a">Twelfth Night, or
          What you Will </title> In <title level="m">Mr. William Shakespeares Comedies, Histories,
          &amp; Tragedies</title>, <pubPlace>London</pubPlace>: <publisher>Jaggard and
          Blount</publisher>, (<date>1623</date>).</bibl>
      <bibl xml:id="l-td-eg-1"><author>Shakespeare, William</author>, <title level="m">The
          Sonnets</title> (<date>1609</date>), <biblScope unit="part">18</biblScope>.</bibl>
      <bibl xml:id="VEST-eg-6"><author>Shakespeare, William</author>, <title level="m">The
          Sonnets</title> (<date>1609</date>), <biblScope unit="part">130</biblScope>.</bibl>
      <bibl xml:id="biblzh-tw_n33" xml:lang="zh-TW">莎士比亞，《終成眷屬 》。</bibl>
      <bibl xml:id="biblzh-tw_n35-36" xml:lang="zh-TW">莎士比亞，《馬克白》。</bibl>
      <bibl xml:id="SAWS"><title level="m">Sharing Ancient Wisdoms</title>, <date>2013</date>,
        available: <ptr target="http://www.ancientwisdoms.ac.uk/"/>.</bibl>
      <bibl xml:id="DR-eg-08"><author>Shaw, George Bernard</author>. <title level="a">Heartbreak
          House: a fantasia in the Russian manner on English themes</title>, 
        <title level="m">Heartbreak House, Great Catherine, and playlets of the war</title>. 
        <pubPlace>London</pubPlace>: <publisher>Constable &amp; co.</publisher>, <date>1919</date>.</bibl>
      <bibl xml:id="DRSP-eg-35"><author>Shaw, George Bernard</author>. <title level="a">Pygmalion</title>, 
        <title level="m">Androcles and the Lion; Overruled; Pygmalion</title>.
        <pubPlace>London</pubPlace>: <publisher>Constable &amp; co.</publisher>,  <date>1916</date>.</bibl>
      <bibl xml:id="SASE-eg-32"><author>Shields, David</author>. <title level="m">Dead
          Languages</title>, <publisher>HarperCollins Canada</publisher>/<publisher>Perennial
          Rack</publisher>, rpt. <date>1990</date>, <biblScope unit="pp">p.10</biblScope>.</bibl>
      <bibl xml:id="COHQHF-eg-8"><editor>Sinclair, John</editor> ed. <title level="m">Collins
          COBUILD English Language Dictionary</title>. <pubPlace>London</pubPlace> and
          <pubPlace>Glasgow</pubPlace>: <publisher>Collins</publisher>, (<date>1987</date>),
          <biblScope unit="pp">p. 337</biblScope> s.v. croissant.</bibl>
      <bibl xml:id="biblzh-tw_n32" xml:lang="zh-TW">京劇《四郎探母》，1947年梅蘭芳演出。</bibl>
      <bibl xml:id="DSBACK-eg-83"><author>Smith, Adam</author>. <title level="m">An Inquiry into the
          Nature and Causes of the Wealth of Nations</title>, <pubPlace>London</pubPlace>.
          (<date>1776</date>), <biblScope unit="part">index to vol. 1</biblScope>.</bibl>
      <bibl xml:id="PH-eg-10">
        <author>Smith, Sydney</author>. <title>Autograph letter</title>. In Pierpont Morgan library;
          <ptr target="#KLINKENBORG"/> 11. </bibl>
      <bibl xml:id="SMITHWM">
        <author>Smith, William</author>. <title level="m">A New Classical Dictionary of Greek and
          Roman Biography, Mythology, and Geography, Partly Based Upon the Dictionary of Greek and
          Roman Biography and Mythology</title>, <pubPlace>New York</pubPlace>: <publisher>Harper
          &amp; Brothers, Publishers</publisher>, <date>1860</date>, <biblScope unit="pp">1026</biblScope>. </bibl>
      <bibl xml:id="PH-eg-14">
        <author>Southey, Robert</author>. Autograph manuscript of <title>The Life of Cowper</title>.
        In Pierpont Morgan MA 412 (<ptr target="#KLINKENBORG"/> 15).</bibl>
      <bibl xml:id="DRCAST-eg-23"><author>Soyinka, Akinwande Oluwole Wole</author>. <title level="m">Madmen and Specialists</title>, <pubPlace>London</pubPlace>:
          <publisher>Methuen</publisher> (<date>1971</date>).</bibl>
      <bibl xml:id="VE-eg-01">
        <author>Spenser, Edmund</author>. <title level="m">The Faerie Queene: Disposed into twelue
          bookes, Fashioning XII. Morall vertues.</title> (<date>1596</date>). </bibl>
      <bibl xml:id="COHQHE-eg-13">
        <author>Sterne, Laurence</author>. <title level="m">The Life and Opinions of Tristram
          Shandy, Gentleman</title>. (<date>1760</date>).</bibl>
      <bibl xml:id="STOW">
        <author>Stow, John </author><title>A survey of the cities of London and Westminster:
          containing the original, antiquity, increase, modern estate and government of those
          cities. Written at first in the year MDXCVIII. By John Stow, citizen and native of London.
          ... Now lastly, corrected, improved, and very much enlarged: ... by John Strype, ... In
          six books. ... </title> (London c.1525 - London 1605). </bibl>
      <bibl xml:id="NYT1992"><author>Sudetic, Chuck </author><title>Serbs Tighten Grip On Eastern
          Bosnia. </title><title>New York Times, </title>
        <date>April 20, 1992</date>.
        <!--http://www.nytimes.com/1992/04/20/world/serbs-tighten-grip-on-eastern-bosnia.html--></bibl>
      <bibl xml:id="SUE"><title>SUEtheTrex, Twitter biography</title>. <ptr target="https://twitter.com/SUEtheTrex"/>. Accessed <date when="2020-03-25">March 25th,
          2020</date>.</bibl>
      <bibl xml:id="NDDATEA-eg-169"><editor>Sutherland, L.S.</editor> and <editor>L.G.
          Mitchell</editor> eds. <title level="m">The Eighteenth century</title>, <series>The
          History of the University of Oxford <biblScope unit="vol">V</biblScope>
        </series>, <biblScope unit="pp">p.178</biblScope>.</bibl>
      <bibl xml:id="biblzh-tw_n28" xml:lang="zh-TW">蘇童，《妻妾成群》。</bibl>
      <bibl xml:id="biblzh-tw_n63" xml:lang="zh-TW">蘇軾，《定風波》。</bibl>
      <bibl xml:id="COEDCOR-eg-71">
        <author>Swift, Jonathan</author>. <title level="m">Travels into Several Remote Nations of
          the World, in Four Parts. By Lemuel Gulliver... </title> (<date>1735</date>).</bibl>
      <bibl xml:id="swiftLaw"><author>Swift, Jonathan</author>. <title>Law is a bottomless pit, or
          the history of John Bull</title> (<date>1712</date>).</bibl>
      <bibl xml:id="HD-eg-swinb">
        <author>Swinburne, Algernon Charles</author>. <title level="m">Poems and Ballads (First
          Series)</title>. <pubPlace>London</pubPlace>: <publisher>Chatto &amp; Windus</publisher>.
          (<date>1904</date>). </bibl>
      <bibl xml:id="CONARS-eg-110"><author>Swinnerton, Frank Arthur</author>. <title level="m">The
          Georgian Literary Scene 1910-1935</title>, <date>1938</date>, <pubPlace>London</pubPlace>:
          <publisher>J. M. Dent</publisher>, <biblScope unit="pp">p. 195</biblScope>.</bibl>


      <!--T-->

      <bibl xml:id="biblzh-tw_n12" xml:lang="zh-TW">台灣，《結婚入盟誓》，1997年5月。</bibl>
      <bibl xml:id="biblzh-tw_n18" xml:lang="zh-TW">台灣區三碼與三加二碼郵遞區號</bibl>
      <bibl xml:id="biblzh-tw_n47" xml:lang="zh-TW">《台灣叢書》，伊能嘉矩著，藏於國立台灣大學圖書館。(http://catalog.ndap.org.tw/?URN=2155366 (Aug 2008)).</bibl>
      <bibl xml:id="biblzh-tw_n27" xml:lang="zh-TW">唐．白居易．琵琶行</bibl>
      <bibl xml:id="DIBO-egXML-lex0">
        <author>Tasovac, T.</author>, <author>Romary, L.</author>, <author>Banski, P.</author>, <author>Bowers, J.</author>, <author>de Does, J.</author>, 
        <author>Depuydt, K.</author>, <author>Erjavec, T.</author>, <author>Geyken, A.</author>, <author>Herold, A.</author>, <author>Hildenbrandt, V.</author>, 
        <author>Khemakhem, M.</author>, <author>Lehečka, B.</author>, <author>Petrović, S.</author>, <author>Salgado, A.</author> and <author>Witt, A. </author>
        <title level="m" type="main">TEI Lex-0: A baseline encoding for lexicographic data.</title>. <title level="m" type="sub">Version 0.9.3</title>.
        <publisher>DARIAH Working Group on Lexical Resources.</publisher>, <date>2018</date> 
        <ptr target="https://dariah-eric.github.io/lexicalresources/pages/TEILex0/TEILex0.html"/>.
      </bibl>
      <bibl xml:id="TAYLOR">
        <author>Taylor, John</author>
        <title>The Cold Tearme or, The Frozen age, Or, The Metamorphosis of the Riuer of
          Thames.</title> London, 1621. [STC (2nd ed.) 23910]. </bibl>
      <bibl xml:id="TEI-Consortium-CFP2022">
        <author><orgName>TEI Consortium</orgName></author>
        <title>Call for Papers - TEI 2022</title> Newcastle, 2022. <ptr target="https://web.archive.org/web/20220516140643/https://conferences.ncl.ac.uk/tei2022/cfp/"/></bibl>
      <bibl xml:id="COPA-eg-02">
        <title level="a">The Castle of the Fly</title>, in <title>Russian Fairy Tales,</title>
        translated by Norbert Guterman from the collections of Aleksandr Afanas'ev, illustrations by
        Alexander Alexeieff, folkloristic commentary by Roman Jakobson (New York: Pantheon Books,
        1947, rpt. [n.d.]), p. 25. </bibl>
      <bibl xml:id="DSHD-eg-31"><title level="j">The Daily Telegraph</title>, <date>21 Dec
          1992</date>.</bibl>
      <bibl xml:id="COHQQ-eg-30"><title level="j">The Guardian, </title>
        <date>26 Oct 1992</date>, <biblScope unit="pp">p. 2</biblScope></bibl>
      <bibl xml:id="DSDIV3X-eg-29"><title level="j">The Guardian, </title>
        <date>21 Dec 1992</date>, <biblScope unit="pp">p. 2</biblScope>.</bibl>
      <bibl xml:id="SASE-eg-40"><title>The Holy Bible, conteyning the Old Testament and the new...
          appointed to be read in Churches.</title> (<date>1611</date>), <biblScope>Genesis
          1:1</biblScope>.</bibl>
      <bibl xml:id="NDDATEA-eg-170"><!-- never used --><title level="j">The Independent, </title>
        <date>26 Oct 1775</date>, <biblScope unit="part">headline</biblScope>.</bibl>
      <bibl xml:id="COHQQ-eg-34"><author>Thurber, James</author>. <title level="m">The 13
          Clocks</title> (<date>1950</date>). </bibl>
      <bibl xml:id="COHQQ-eg-31"><author>Tolkien, J. R. R.</author>
        <title level="m">The Monsters and the Critics</title>. <pubPlace>London</pubPlace>:
          <publisher>George Allen &amp; Unwin</publisher> (<date>1983</date>).</bibl>
      <bibl xml:id="CO-eg-01">
        <author>Townsend, Sue</author>. <title level="m">The growing pains of Adrian Mole</title>
          (<date>1984</date>), <biblScope unit="pp">p.43</biblScope>. </bibl>
      <bibl xml:id="DSCO-eg-51">
        <author>Trollope, Anthony</author>. <title level="m">An Autobiography</title>
          (<date>1883</date>).</bibl>
      <bibl xml:id="NDORG-eg-38">
        <author>Trollope, Anthony</author>. <title level="m">North America</title>
          (<date>1862</date>). </bibl>
      <bibl xml:id="fr-ex-Angl" xml:lang="fr"><author>Truffaut, François</author> et
          <author>Gruault, Jean</author>, <title level="a">Les deux Anglaises et le continent :
          script</title>, <title level="j">l'Avant-scène cinéma</title>, <num>n° 121</num>,
          <date>nov. 1971</date>. </bibl>
      <bibl xml:id="COBITY-eg-240"><author>Tufte, Edward R.</author>, <title level="m">Envisioning
          Information</title>, <pubPlace>Cheshire</pubPlace>: <publisher>Graphics Press</publisher>.
          (<date>1990</date>).</bibl>

      <!--U-->
      <bibl xml:id="URF-UBSGlobal"><title>Ukraine Relief Fund</title>
        <author><orgName>UBS</orgName></author>
        <ptr target="https://web.archive.org/web/20220307150159/https://www.ubs.com/global/en/ubs-society/philanthropy/optimus-foundation/ukrainerelief.html"/>. </bibl>
      <bibl xml:id="SA-eg-01"><title>United States Code</title> Title 17, Section 107, found at <ptr target="http://www.copyright.gov/title17/92chap1.html#107"/>. </bibl>
      <bibl xml:id="MENTIOND-eg-1">
        <author>United States District Court for the Middle District of Pennsylvania</author>.
          <title>Kitzmiller v. Dover Area School District et al.</title>: <date>2005</date>.
          <idno>04cv2688</idno>, <biblScope unit="pp">p. 33</biblScope>. Available from <ptr target="http://ncse.com/files/pub/legal/kitzmiller/highlights/2005-12-20_Kitzmiller_decision.pdf"/> and transcribed at <ptr target="http://en.wikisource.org/wiki/Kitzmiller_v._Dover_Area_School_District_et_al."/>. </bibl>

      <!--V-->

      <bibl xml:id="fr-ex-Teste" xml:lang="fr"><author>Valéry, Paul</author>, <title>Monsieur
          Teste</title>, <date>1929</date>. </bibl>
      <bibl xml:id="VE-eg-02">
        <author>Vergil (Publius Vergilius Naso)</author>. <title level="m">Aeneid</title>,
          <biblScope>I.1</biblScope>. </bibl>
      <bibl xml:id="fr-ex-Verne-Ballon" xml:lang="fr"><author>Verne, Jules</author>, <title> Cinq
          semaines en ballon</title>, <date>1863</date>.</bibl>
      <bibl xml:id="fr-ex-Verne_Chasse" xml:lang="fr"><author>Verne, Jules</author>, <title>La
          Chasse au météore</title>, <date>1908</date>.</bibl>
      <bibl xml:id="fr-ex-Verne_Vingt" xml:lang="fr"><author>Verne, Jules</author>,<title> Vingt
          mille lieues sous les mers</title>, <date>1870</date>.</bibl>
      <bibl xml:id="VINGE">
        <author>Vinge, Vernor</author>
        <title>Across realtime</title>
        <biblScope>ch 10</biblScope> (<date>1986</date>). </bibl>
      <bibl xml:id="fr-ex-Viton-dictionnaire" xml:lang="fr"><author>Viton de Saint-Allais, Nicolas
        </author>, <title>Dictionnaire encyclopédique de la noblesse de France</title>,
          <date>1816</date>.</bibl>
      <bibl xml:id="PH-eg-13">
        <title>Vóluspá</title> recto of folio 5 of the unique manuscript of the Elder Edda. Codex
        Regius, ed. L. F. A. Wimmer and F. Jónsson (Copenhagen <date>1891</date>). </bibl>

      <!--W-->

      <bibl xml:id="CO-eg-03">
        <editor>Wanklyn, M.D.G. </editor> et al. <title>Gloucester Port Books, 1575-1765</title>.
        Available from <ptr target="http://discover.ukdataservice.ac.uk/catalogue?sn=3218"/>.</bibl>
      <bibl xml:id="DSAE-eg-39"><!-- Adapted from sajc000021.xml; not available from website   -->
        <author>Wanton, Joseph</author>. <title>Unpublished letter to Nicholas Brown and Co</title>,
          <date>1761</date>
        <publisher>Brown University Steering Committee on Slavery and Justice: Repository of
          Historical Documents. </publisher> (<ptr target="http://library.brown.edu/cds/slaveryandjustice/"/>). </bibl>
      <bibl xml:id="COLI-eg-175">
        <author>Warriner, John E. </author>
        <title level="m">English Composition and Grammar</title> (<date>1988</date>), <biblScope unit="pp">p.280</biblScope>.</bibl>
      <bibl xml:id="DIC-W7">
        <title>Webster's Seventh Collegiate Dictionary</title>. <pubPlace>Springfield, Mass. </pubPlace>
        <publisher>G. &amp; C. Merriam Co.</publisher> (<date>1975</date>). </bibl>
      <bibl xml:id="biblzh-tw_n8" xml:lang="zh-TW">魏飴，《小說鑑賞入門》，台北：萬卷樓，1999。</bibl>
      <bibl xml:id="fr-ex-Weil-Atares" xml:lang="fr"><author>Weil, Simone</author>, <title level="a"> Lettres à Antonio Atarès</title>, in <title level="m">Oeuvres
          complètes</title><date>1988-</date>.</bibl>
      <bibl xml:id="COHQQ-eg-25">
        <author>Williams, Nigel</author>. <title level="m">The Wimbledon Poisoner</title>
          (<date>1990</date>), <biblScope unit="pp">p. 204</biblScope>.</bibl>
      <bibl xml:id="fr-ex-Winock-Jeanne" xml:lang="fr"><author>Winock, Michel</author>,
          <title>Jeanne et les siens : récit</title>, <date>2003</date>.</bibl>
      <bibl xml:id="NOTE-eg">
        <author>Wölfflin, Heinrich</author>, trans. <editor role="translator">Hottinger, Marie
          Donald Mackie</editor> (<date>1932</date>). <title>Principles of art history: the problem
          of the development of style in later art.</title>. Originally published as <title xml:lang="de">Kunstgeschichtliche Grundbegriffe</title> (1915).</bibl>
      <bibl xml:id="CONADA-eg-143">
        <author>Woolf, Virginia</author>. <title level="m">Mrs Dalloway</title> (<date>1925</date>),
          <biblScope unit="pp">p.64, p.65</biblScope>.</bibl>
      <bibl xml:id="NH-eg-01">
        <author>Wordsworth, William</author>. <title level="a">Scorn not the sonnet</title> in
          <title level="m">Poetical Works</title> (<date>1827</date>). </bibl>
      <bibl xml:id="CO-eg-08">
        <author>Wordsworth, William</author>. <title>The Prelude</title> (<date>1850</date>). </bibl>
      <bibl xml:id="VESTR-eg-1">
        <editor>Wrenn C. L.</editor> ed. <title level="m">Beowulf: with the Finnesburg
          fragment</title>, <pubPlace>London</pubPlace>: <publisher>Harrap</publisher>
          (<date>1953</date>).</bibl>

      <bibl xml:id="biblzh-tw_n22" xml:lang="zh-TW">吳承恩，《西遊記》。</bibl>

      <bibl xml:id="DRPRO-eg-6">
        <author>Wycherley, William</author>. <title level="m">The Country Wife</title>
          (<date>1675</date>).</bibl>
      <!--X-->

      <bibl xml:id="biblzh-tw_n10" xml:lang="zh-TW">夏宇，〈甜蜜的復仇〉，《備忘錄》。</bibl>
      <bibl xml:id="biblzh-tw_n21" xml:lang="zh-TW">蕭紅，《呼蘭河傳》。</bibl>

      <!--Y-->

      <bibl xml:id="biblzh-tw_n42" xml:lang="zh-TW">幼莘貢俚賀曉濤之新婚賀詞</bibl>
      <bibl xml:id="biblzh-tw_n60" xml:lang="zh-TW">余秋雨</bibl>
      <bibl xml:id="biblzh-tw_n62-64" xml:lang="zh-TW">元曲。馬致遠，《天淨沙：秋思》。</bibl>

      <!--Z-->

      <bibl xml:id="biblzh-tw_n4" xml:lang="zh-TW">張錯， 《西洋文學術與手冊》，台北：書林，2005。頁201。</bibl>

      <bibl xml:id="biblzh-tw_n19" xml:lang="zh-TW">珍．奧斯丁，《傲慢與偏見》。</bibl>

      <bibl xml:id="biblzh-tw_n11" xml:lang="zh-TW">中國青年守則</bibl>
      <bibl xml:id="biblzh-tw_n13" xml:lang="zh-TW">中國學位論文全文數據庫</bibl>
      <bibl xml:id="biblzh-tw_n14" xml:lang="zh-TW">周慧玲，《表演中國：女明星表演文化視覺政治1910-1945》，2004。</bibl>
      <bibl xml:id="biblzh-tw_n56-57" xml:lang="zh-TW">朱自清， 《憶》跋。</bibl>
      <bibl xml:id="LZ">
        <author>Zimman, Lal</author>. <title>Lal Zimman</title>
        <ptr target="http://lalzimman.com/bio.html"/>, accessed <date when="2021-02-01">February 1,
          2021</date>. </bibl>
      <bibl xml:id="ZUPKO">
        <author>Zupko, Ronald Edward</author>
        <title level="m">British Weights &amp; Measures: A History from Antiquity to the Seventeenth
          Century</title>. <pubPlace>Madison</pubPlace>: <publisher>University of Wisconsin
          Press</publisher>, <biblScope unit="pp">141-151</biblScope>. </bibl>

      <!--Other-->
      <bibl xml:id="NONE">No source, made up for these <title>Guidelines</title>.</bibl>
      <bibl xml:id="SELF">Example is copied from the source of these <title>Guidelines</title>.</bibl>
      <bibl xml:id="UND">Undetermined.</bibl>

    </listBibl>
  </div>
  <div>
    <head>Works Cited Elsewhere in the Text of these Guidelines</head>
    <listBibl>
      <bibl xml:id="BIB_smiley">
        <author>Scott E. Fahlman</author>
        <title>"Joke" Conversation Thread in which the :-) Was Invented</title>
        <ptr target="http://www.cs.cmu.edu/~sef/Orig-Smiley.htm"/>
        <date type="accessed" when="2023-12-08"/>
      </bibl>
      <biblStruct xml:id="KNUTH">
        <monogr>
          <author>
            <surname>Knuth</surname>
            <forename>Donald E.</forename>
          </author>
          <title level="m">Literate Programming</title>
          <title level="s">CSLI Lecture Notes 27</title>
          <idno type="ISBN">0-937073-80-6</idno>
          <imprint>
            <pubPlace>Stanford, California</pubPlace>
            <publisher>Center for the Study of Language and Information</publisher>
            <date>1992</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="mazz-NDPERSbp">
        <analytic>
          <author>
            <surname>Mazzolini</surname>
            <forename>Renato</forename>
            <forename>G.</forename>
          </author>
          <title level="a">Colonialism and the Emergence of Racial Theories</title>
          <idno type="DOI">10.1017/9781107705647.032</idno>
        </analytic>
        <monogr>
          <title level="m">Reproduction: Antiquity to the Present Day</title>
          <editor>
            <forename>Nick</forename>
            <surname>Hopwood</surname>
          </editor>
          <editor>
            <forename>Rebecca</forename>
            <surname>Flemming</surname>
          </editor>
          <editor>
            <forename>Lauren</forename>
            <surname>Kassell</surname>
          </editor>
          <imprint>
            <pubPlace>Cambridge</pubPlace>
            <publisher>Cambridge University Press</publisher>
            <date>2018</date>
          </imprint>
          <biblScope unit="page">361-374</biblScope>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="rubin-NDPERSEpc">
        <analytic>
          <author>
            <surname>Rubin</surname>
            <forename>Gayle</forename>
          </author>
          <title level="a">The Traffic in Women: Notes on the <q>Political Economy</q> of
            Sex</title>
          <ptr target="https://philpapers.org/archive/RUBtti.pdf"/>
        </analytic>
        <monogr>
          <title level="m">Toward an Anthropology of Women</title>
          <editor>
            <forename>Rayna</forename>
            <forename>R.</forename>
            <surname>Reiter</surname>
          </editor>
          <imprint>
            <pubPlace>New York</pubPlace>
            <publisher>Monthly Review Press</publisher>
            <date>1975</date>
          </imprint>
          <biblScope unit="page">157–210, 165</biblScope>
        </monogr>
      </biblStruct>
      <!--
                                          <biblStruct xml:id="CO-BIBL-2">
                                          <monogr>
                                          <author><forename>A.</forename>
                                          <forename>G.</forename>
                                          <surname>Petty</surname>
                                          </author>
                                          <title level="m">English literary hands from Chaucer to Dryden</title>
                                          <imprint>
                                          <pubPlace>London</pubPlace>
                                          <publisher>Edward Arnold</publisher>
                                          <date>1977</date>
                                          <biblScope unit="pp">22-25</biblScope>
                                          </imprint>
                                          </monogr>
                                          </biblStruct> -->
      <biblStruct xml:id="PETTY">
        <monogr>
          <author>
            <forename>A. G.</forename>
            <surname>Petty</surname>
          </author>
          <title level="m">English literary hands from Chaucer to Dryden</title>
          <imprint>
            <pubPlace>London</pubPlace>
            <publisher>Edward Arnold</publisher>
            <date>1977</date>
          </imprint>
          <biblScope unit="pp"> 22–25</biblScope>
        </monogr>
      </biblStruct>

      <biblStruct xml:id="STTS_IBK">
        <monogr>
          <author>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </author>
          <author>
            <forename>Thomas</forename>
            <surname>Bartz</surname>
          </author>
          <author>
            <forename>Angelika</forename>
            <surname>Storrer</surname>
          </author>
          <author>
            <forename>Swantje</forename>
            <surname>Westpfahl</surname>
          </author>
          <title>Tagset and guidelines for the PoS tagging of language data from genres of
            computer-mediated communication / social media</title>
          <ptr target="https://nbn-resolving.org/urn:nbn:de:bsz:mh39-50650"/>
          <imprint>
            <date>2015-09-13</date>
            <distributor><ref target="https://sites.google.com/site/empirist2015/">EmpiriST
                2015</ref> Task Force: Michael Beißwenger, Kay-Michael Würzner, Sabine Bartsch,
              Stefan Evert</distributor>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="TEIcmc2012">
        <analytic>
          <author>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </author>
          <author>
            <forename>Maria</forename>
            <surname>Ermakova</surname>
          </author>
          <author>
            <forename>Alexander</forename>
            <surname>Geyken</surname>
          </author>
          <author>
            <forename>Lothar</forename>
            <surname>Lemnitzer</surname>
          </author>
          <author>
            <forename>Angelika</forename>
            <surname>Storrer</surname>
          </author>
          <title level="a">A TEI Schema for the Representation of Computer-mediated Communication</title>
          <ptr type="URL" target="http://journals.openedition.org/jtei/476"/>
          <ptr type="DOI" target="https://doi.org/10.4000/jtei.476"/>
        </analytic>
        <monogr>
          <title level="j">Journal of the Text Encoding Initiative</title>
          <imprint>
            <date when="2012-10-15">15 October 2012</date>
          </imprint>
          <biblScope unit="issue">3</biblScope>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="BIB_CMC_Core">
        <analytic>
          <author>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </author>
          <author>
            <forename>Harald</forename>
            <surname>Lüngen</surname>
          </author>
          <title>CMC-core: a schema for the representation of CMC corpora in TEI</title>
          <ptr target="https://journals.openedition.org/corpus/4553"/>
        </analytic>
        <monogr>
          <title level="j">Corpus 20 (Special issue "Traitements, standardisation et analyse des
            corpus de communication médiée par les réseaux sociaux)</title>
          <editor>Céline Poudat</editor>
          <editor>Ciara R. Wigham</editor>
          <editor>Loïc Liégeois</editor>
          <imprint>
            <date>2020</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="BIB_scilog1">
        <analytic>
          <author>Gerry and demolog</author>
          <title>Blog comments to "Scheinzwerge oder Viele Probleme werden größer, wenn man sie
            anpackt (Griechenland)"</title>
          <ref type="url" target="https://scilogs.spektrum.de/wild-dueck-blog/scheinzwerge-oder-viele-probleme-werden-groesser-wenn-man-sie-anpackt-griechenland/">https://scilogs.spektrum.de/wild-dueck-blog/scheinzwerge-oder-viele-probleme-werden-groesser-wenn-man-sie-anpackt-griechenland/</ref>
          <date>29-30 July 2015</date>
        </analytic>
        <monogr>
          <title>WILD DUECK BLOG</title>
          <author>Gunter Dück</author>
          <imprint>
            <pubPlace><ref type="url" target="https://scilogs.spektrum.de/wild-dueck-blog/"/>https://scilogs.spektrum.de/wild-dueck-blog/</pubPlace>
          </imprint>
        </monogr>
        <series>SciLogs</series>
      </biblStruct>

      <bibl xml:id="BIB_WPTalkEiffel">Jossi et al. (2006-): <hi rend="italic">Talk:Eiffel
          (programming language)/Archive_1.</hi> URL: <ref target="https://en.wikipedia.org/wiki/Talk:Eiffel_(programming_language)/Archive_1">https://en.wikipedia.org/wiki/Talk:Eiffel_(programming_language)/Archive_1</ref>. English
        Wikipedia talk page, Wikimedia Foundation.</bibl>

      <bibl xml:id="BIB_WPTalkAstronomicalObject">MiszaBot I et al. (2011-): <hi rend="italic">Talk:Astronomical object.</hi> URL: <ref target="https://en.wikipedia.org/wiki/Talk:Astronomical_object">https://en.wikipedia.org/wiki/Talk:Astronomical_object</ref>. English Wikipedia talk
        page, Wikimedia Foundation.</bibl>

      <bibl xml:id="BIB_WPTalkFKM">OnkelSchuppig et al. (2001-): <hi rend="italic">Diskussion:FKM-Richtlinie</hi>. URL: <ref target="https://de.wikipedia.org/wiki/Diskussion:FKM-Richtlinie">https://de.wikipedia.org/wiki/Diskussion:FKM-Richtlinie</ref>. German Wikipedia talk
        page, Wikimedia Foundation.</bibl>

            <biblStruct xml:id="BIB_MoCoDa2">
        <monogr>
          <title>Mobile Communication Database 2 (MoCoDa2)</title>
          <editor>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </editor>
          <editor>
            <forename>Evelyn</forename>
            <surname>Ziegler</surname>
          </editor>
          <editor>
            <forename>Marcel</forename>
            <surname>Fladrich</surname>
          </editor>
          <editor>
            <forename>Wolfgang</forename>
            <surname>Imo</surname>
          </editor>
          <editor>
            <forename>Katharina</forename>
            <surname>König</surname>
          </editor>
          <imprint>
            <pubPlace>
              <ref type="url" target="https://db.mocoda2.de/c/home">https://db.mocoda2.de/c/home</ref>
            </pubPlace>
            <date type="visited">visited 30 March 2022</date>
          </imprint>
        </monogr>
      </biblStruct>

      <biblStruct xml:id="BIB_DCK">
        <monogr>
          <title>Dortmund Chat Corpus</title>
          <editor>
            <forename>Angelika</forename>
            <surname>Storrer</surname>
          </editor>
          <editor>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </editor>
          <imprint>
            <pubPlace>
              <ref type="pid" target="http://hdl.handle.net/10932/00-03B0-14FA-A8D0-0F01-F">http://hdl.handle.net/10932/00-03B0-14FA-A8D0-0F01-F</ref>
            </pubPlace>
            <date>2017</date>
            <distributor>Leibniz-Institut für Deutsche Sprache</distributor>
          </imprint>
        </monogr>
      </biblStruct>

      <biblStruct xml:id="BIB_CoMeRe">
        <analytic>
          <author>
            <forename>Chanier</forename>
            <surname>Thierry</surname>
          </author>
          <author>
            <forename>Poudat</forename>
            <surname>Céline</surname>
          </author>
          <author>
            <forename>Sagot</forename>
            <surname>Benoit</surname>
          </author>
          <author>
            <forename>Antoniadis</forename>
            <surname>Georges</surname>
          </author>
          <author>
            <forename>Wigham</forename>
            <surname>Ciara R.</surname>
          </author>
          <author>
            <forename>Hriba</forename>
            <surname>Linda</surname>
          </author>
          <author>
            <forename>Longhi</forename>
            <surname>Julien</surname>
          </author>
          <author>
            <forename>Seddah</forename>
            <surname>Djamé</surname>
          </author>
          <title>The CoMeRe corpus for French: structuring and annotating heterogeneous CMC
            genres</title>
        </analytic>
        <monogr>
          <title>JLCL (Journal of Language Technology and Computational Linguistics) (Special issue
            on « Building And Annotating Corpora Of Computer-Mediated Discourse: Issues and
            Challenges at the Interface of Corpus and Computational Linguistics)</title>
          <imprint>
            <pubPlace><ref type="url">http://www.jlcl.org/2014_Heft2/Heft2-2014.pdf</ref></pubPlace>
            <date>2014</date>
          </imprint>
          <biblScope unit="volume">2</biblScope>
          <biblScope unit="pp">1-31</biblScope>
        </monogr>
      </biblStruct>

      <biblStruct xml:id="BIB_Cotgrove">
        <monogr>
          <editor>
            <forename>Louis Alexander</forename>
            <surname>Cotgrove</surname>
          </editor>
          <title>Nottinghamer Korpus Deutscher YouTube-Sprache (The NottDeuYTSch Corpus)</title>
          <imprint>
            <pubPlace>
              <ref type="url" target="http://hdl.handle.net/11372/LRT-4806">http://hdl.handle.net/11372/LRT-4806</ref>
            </pubPlace>
            <distributor>LINDAT/CLARIAH-CZ</distributor>
            <date>2018</date>
          </imprint>
        </monogr>

      </biblStruct>

      <biblStruct xml:id="BIB_ChanierWigham2015">
        <analytic>
          <author>
            <forename>Ciara</forename>
            <surname>Wigham</surname>
          </author>
          <author>
            <forename>Thierry</forename>
            <surname>Chanier</surname>
          </author>
          <title>Interactions between text chat and audio modalities for L2 communication and
            feedback in the synthetic world Second Life</title>
          <idno type="DOI">10.1080/09588221.2013.851702</idno>
        </analytic>
        <monogr>
          <title>Computer Assisted Language Learning</title>
          <imprint>
            <date>2015</date>
          </imprint>
          <biblScope unit="volume">23</biblScope>
          <biblScope unit="issue">3</biblScope>
        </monogr>
      </biblStruct>

      <biblStruct xml:id="AB-eg-01">
        <analytic>
          <author>
            <forename>Lou</forename>
            <surname>Burnard</surname>
          </author>
          <title level="a">Report of Workshop on Text Encoding Guidelines</title>
        </analytic>
        <monogr>
          <title level="j">Literary &amp; Linguistic Computing</title>
          <imprint>
            <biblScope unit="vol">3</biblScope>
            <date>1988</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="Burnard1995b">
        <analytic>
          <author>
            <forename>Lou</forename>
            <surname>Burnard</surname>
          </author>
          <author>
            <forename>C.</forename>
            <forename>Michael</forename>
            <surname>Sperberg-McQueen</surname>
          </author>
          <title level="a">The Design of the TEI Encoding Scheme</title>
          <idno type="DOI">10.1007/BF01830314</idno>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <biblScope unit="vol">29</biblScope>
            <biblScope unit="issue">1</biblScope>
            <date>1995</date>
            <biblScope unit="pp">17–39</biblScope>
          </imprint>
        </monogr>
        <note>Reprinted in <ptr target="#Ide1995b"/>, pp. 17-40</note>
      </biblStruct>
      <biblStruct xml:id="TD-BIBL-01">
        <analytic>
          <author>
            <forename>Lou</forename>
            <surname>Burnard</surname>
          </author>
          <author>
            <forename>Sebastian</forename>
            <surname>Rahtz</surname>
          </author>
          <title level="m">RelaxNG with Son of ODD</title>
          <ptr target="http://www.mulberrytech.com/Extreme/Proceedings/html/2004/Burnard01/EML2004Burnard01.pdf"/>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2004</title>
          <imprint>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="PARKES">
        <monogr>
          <author>
            <forename>M.</forename>
            <forename>B.</forename>
            <surname>Parkes</surname>
          </author>
          <title level="m">English Cursive Book Hands 1250–1500</title>
          <imprint>
            <pubPlace>Oxford</pubPlace>
            <publisher>Clarendon Press</publisher>
            <date>1969</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="KLINKENBORG">
        <monogr>
          <title>British Literary Manuscripts. Series 2: from 1800 to 1914</title>
          <author>
            <surname>Klinkenborg</surname>
            <forename>Verlyn</forename>
          </author>
          <author>
            <surname>Cahoon</surname>
            <forename>Herbert</forename>
          </author>
          <imprint>
            <pubPlace> New York</pubPlace>
            <publisher>Pierpont Morgan Library</publisher>
            <date>1981</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XPTRFMWK">
        <monogr>
          <editor>
            <forename>Paul</forename>
            <surname>Grosso</surname>
          </editor>
          <editor>
            <forename>Eve</forename>
            <surname>Maler</surname>
          </editor>
          <editor>
            <forename>Jonathan</forename>
            <surname>Marsh</surname>
          </editor>
          <editor>
            <forename>Norman</forename>
            <surname>Walsh</surname>
          </editor>
          <title level="m">XPointer Framework</title>
          <ptr target="https://www.w3.org/TR/xptr-framework/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2003-03-25">25 March 2003</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XPTRELEM">
        <monogr>
          <editor>
            <forename>Paul</forename>
            <surname>Grosso</surname>
          </editor>
          <editor>
            <forename>Eve</forename>
            <surname>Maler</surname>
          </editor>
          <editor>
            <forename>Jonathan</forename>
            <surname>Marsh</surname>
          </editor>
          <editor>
            <forename>Norman</forename>
            <surname>Walsh</surname>
          </editor>
          <title level="m">XPointer element() Scheme</title>
          <ptr target="https://www.w3.org/TR/xptr-element/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2003-03-25">25 March 2003</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XHTML">
        <monogr>
          <title level="m">XHTML™ 1.0 The Extensible HyperText Markup Language (Second
            Edition)</title>
          <ptr target="https://www.w3.org/TR/xhtml/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2000-01-26">26 January 2000</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="HTML4">
        <monogr>
          <editor>
            <forename>Dave</forename>
            <surname>Ragget</surname>
          </editor>
          <editor>
            <forename>Arnaud</forename>
            <surname>Le Hors</surname>
          </editor>
          <editor>
            <forename>Ian</forename>
            <surname>Jacobs</surname>
          </editor>
          <title level="m"> HTML 4.01 Specification</title>
          <ptr target="https://www.w3.org/TR/html401/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="1999-12-24">24 December 1999</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="MATHML">
        <monogr>
          <editor>
            <forename>David</forename>
            <surname>Carlisle</surname>
          </editor>
          <editor>
            <forename>Patrick</forename>
            <surname>Ion</surname>
          </editor>
          <editor>
            <forename>Robert</forename>
            <surname>Miner</surname>
          </editor>
          <editor>
            <forename>Nico</forename>
            <surname>Poppelier</surname>
          </editor>
          <title level="m">Mathematical Markup Language (MathML) Version 2.0 (Second
            edition)</title>
          <ptr target="https://www.w3.org/TR/MathML2/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2003-10-21">21 October 2003</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XSD2">
        <monogr>
          <editor>
            <forename>Paul V.</forename>
            <surname>Biron</surname>
          </editor>
          <editor>
            <forename>Ashok</forename>
            <surname>Malhotra</surname>
          </editor>
          <title level="m">XML Schema Part 2: Datatypes Second Edition</title>
          <ptr target="https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2004-10-28">28 October 2004</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XSL11">
        <monogr>
          <editor>
            <forename>Anders</forename>
            <surname>Berglund</surname>
          </editor>
          <title level="m">Extensible Stylesheet Language (XSL) Version 1.1</title>
          <ptr target="https://www.w3.org/TR/xsl11/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2006-12-05">5 December 2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XSLT">
        <monogr>
          <editor>
            <forename>James</forename>
            <surname>Clark</surname>
          </editor>
          <title level="m">XSL Transformations (XSLT) Version 1.0</title>
          <ptr target="https://www.w3.org/TR/xslt/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="1999-11-16">16 November 1999</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XSLT2">
        <monogr>
          <editor>
            <forename>Michael</forename>
            <surname>Kay</surname>
          </editor>
          <title level="m">XSL Transformations (XSLT) Version 2.0</title>
          <ptr target="https://www.w3.org/TR/xslt20/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2007-01-23">23 January 2007</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XSLT3">
        <monogr>
          <editor>
            <forename>Michael</forename>
            <surname>Kay</surname>
          </editor>
          <title level="m">XSL Transformations (XSLT) Version 3.0</title>
          <ptr target="https://www.w3.org/TR/xslt-30/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2017-06-08">8 June 2017</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XMLREC">
        <monogr>
          <editor>
            <forename>Tim</forename>
            <surname>Bray</surname>
          </editor>
          <editor>
            <forename>Jean</forename>
            <surname>Paoli</surname>
          </editor>
          <editor>
            <forename>C. M.</forename>
            <surname>Sperberg-McQueen</surname>
          </editor>
          <editor>
            <forename>Eve</forename>
            <surname>Maler</surname>
          </editor>
          <editor>
            <forename>François</forename>
            <surname>Yergau</surname>
          </editor>
          <title level="m">Extensible Markup Language (XML) Version 1.0 (Fourth edition)</title>
          <ptr target="https://www.w3.org/TR/REC-xml/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2006-08-16">16 August 2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CSS21">
        <monogr>
          <editor>
            <forename>Bert</forename>
            <surname>Bos</surname>
          </editor>
          <editor>
            <forename>Tantek</forename>
            <surname>Çelik</surname>
          </editor>
          <editor>
            <forename>Ian</forename>
            <surname>Hickson</surname>
          </editor>
          <editor>
            <forename>Håkon Wium</forename>
            <surname>Lie</surname>
          </editor>
          <title level="m">Cascading Style Sheets Level 2 Revision 1</title>
          <ptr target="https://www.w3.org/TR/CSS2/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2011-06-07">7 June 2011</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CSS1">
        <monogr>
          <editor>
            <forename>Håkon Wium</forename>
            <surname>Lie</surname>
          </editor>
          <editor>
            <forename>Bert</forename>
            <surname>Bos</surname>
          </editor>
          <title level="m">Cascading Style Sheets, Level 1</title>
          <ptr target="https://www.w3.org/TR/REC-CSS1/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="1999-01-11">11 January 1999</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CSSWM">
        <monogr>
          <editor>
            <name>fantasai</name>
          </editor>
          <editor>
            <forename>Koji</forename>
            <surname>Ishi</surname>
          </editor>
          <title level="m">CSS Writing Modes Level 3 (W3C Candidate Recommendation)</title>
          <ptr target="https://www.w3.org/TR/css-writing-modes-3/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2015-12-15">15 December 2015</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CSSTM">
        <monogr>
          <editor>
            <forename>Simon</forename>
            <surname>Fraser</surname>
          </editor>
          <editor>
            <forename>Dean</forename>
            <surname>Jackson</surname>
          </editor>
          <editor>
            <forename>Edward</forename>
            <surname>O'Connor</surname>
          </editor>
          <editor>
            <forename>Dirk</forename>
            <surname>Schulze</surname>
          </editor>
          <title level="m">CSS Transforms Module Level 1 (W3C Working Draft)</title>
          <ptr target="https://www.w3.org/TR/css-transforms/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2013-11-26">26 November 2013</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="RDFPrimer">
        <monogr>
          <editor>
            <forename>Frank</forename>
            <surname>Manola</surname>
          </editor>
          <editor>
            <forename>Eric</forename>
            <surname>Miller</surname>
          </editor>
          <editor>
            <forename>Brian</forename>
            <surname>McBride</surname>
          </editor>
          <title>RDF 1.1 Primer</title>
          <ptr target="https://www.w3.org/TR/rdf11-primer/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2014-06-24">24 June 2014</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XMLBASE">
        <monogr>
          <editor>
            <forename>Jonathan</forename>
            <surname>Marsh</surname>
          </editor>
          <editor>
            <forename>Richard</forename>
            <surname>Tobin</surname>
          </editor>
          <title level="m">XML Base (Second Edition)</title>
          <ptr target="https://www.w3.org/TR/xmlbase/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2009-01-28">28 January 2009</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XPATH">
        <monogr>
          <editor>
            <forename>James</forename>
            <surname>Clark</surname>
          </editor>
          <editor>
            <forename>Steve</forename>
            <surname>DeRose</surname>
          </editor>
          <title level="m">XML Path Language (XPath) Version 1.0</title>
          <ptr target="https://www.w3.org/TR/xpath/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="1999-11-16">16 November 1999</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XPATH2">
        <monogr>
          <editor>
            <forename>Anders</forename>
            <surname>Berglund</surname>
          </editor>
          <editor>
            <forename>Scot</forename>
            <surname>Boag</surname>
          </editor>
          <editor>
            <forename>Mary F.</forename>
            <surname>Fernández</surname>
          </editor>
          <editor>
            <forename>Michael</forename>
            <surname>Kay</surname>
          </editor>
          <editor>
            <forename>Jonathan</forename>
            <surname>Robie</surname>
          </editor>
          <editor>
            <forename>Jérôme</forename>
            <surname> Siméon</surname>
          </editor>
          <title level="m">XML Path Language (XPath) 2.0</title>
          <ptr target="https://www.w3.org/TR/xpath20/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2007-01-23">23 January 2007</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XPATH30">
        <monogr>
          <editor>
            <forename>Jonathan</forename>
            <surname>Robie</surname>
          </editor>
          <editor>
            <forename>Don</forename>
            <surname>Chamberlin</surname>
          </editor>
          <editor>
            <forename>Michael</forename>
            <surname>Dyck</surname>
          </editor>
          <editor>
            <forename>Jon</forename>
            <surname>Snelson</surname>
          </editor>
          <title level="m">XML Path Language (XPath) 3.0</title>
          <ptr target="https://www.w3.org/TR/xpath-30/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2014-04-08">8 April 2014</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="XPATH31">
        <monogr>
          <editor>
            <forename>Jonathan</forename>
            <surname>Robie</surname>
          </editor>
          <editor>
            <forename>Michael</forename>
            <surname>Dyck</surname>
          </editor>
          <editor>
            <forename>Josh</forename>
            <surname>Spiegel</surname>
          </editor>
          <title level="m">XML Path Language (XPath) 3.1</title>
          <ptr target="https://www.w3.org/TR/xpath-31/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2017-03-21">21 March 2017</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="NAMESPACES">
        <monogr>
          <editor>
            <forename>Tim</forename>
            <surname>Bray</surname>
          </editor>
          <editor>
            <forename>Dave</forename>
            <surname>Hollander</surname>
          </editor>
          <editor>
            <forename>Andrew</forename>
            <surname>Laymon</surname>
          </editor>
          <editor>
            <forename>Richard</forename>
            <surname>Tobin</surname>
          </editor>
          <title level="m">Namespaces in XML 1.0 (second edition)</title>
          <ptr target="https://www.w3.org/TR/xml-names/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2006-08-16">16 August 2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="SG-BIBL-1">
        <monogr>
          <author>
            <forename>Eric</forename>
            <surname>van der Vlist</surname>
          </author>
          <title level="m">RELAX NG</title>
          <ptr target="http://books.xmlschemata.org/relaxng/page2.html"/>
          <imprint>
            <publisher>O'Reilly</publisher>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="SG-BIBL-2">
        <analytic>
          <author>
            <surname>Renear</surname>
            <forename>A.</forename>
          </author>
          <author>
            <surname>Mylonas</surname>
            <forename>E.</forename>
          </author>
          <author>
            <surname>Durand</surname>
            <forename>D. </forename>
          </author>
          <title level="a">Refining our notion of what text really is: the problem of overlapping
            hierarchies</title>
        </analytic>
        <monogr>
          <editor>
            <forename>Nancy</forename>
            <surname>Ide</surname>
          </editor>
          <editor>
            <forename>Susan</forename>
            <surname>Hockey</surname>
          </editor>
          <title level="m">Research in Humanities Computing</title>
          <imprint>
            <publisher>Oxford University Press</publisher>
            <date>1996</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="WADM">
        <monogr>
          <editor>
            <forename>Robert</forename>
            <surname>Sanderson</surname>
          </editor>
          <editor>
            <forename>Paolo</forename>
            <surname>Ciccarese</surname>
          </editor>
          <editor>
            <forename>Benjamin</forename>
            <surname>Young</surname>
          </editor>
          <title>Web Annotation Data Model</title>
          <ptr target="https://www.w3.org/TR/annotation-model/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2017-02-23">23 February 2017</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="WAV">
        <monogr>
          <editor>
            <forename>Robert</forename>
            <surname>Sanderson</surname>
          </editor>
          <editor>
            <forename>Paolo</forename>
            <surname>Ciccarese</surname>
          </editor>
          <editor>
            <forename>Benjamin</forename>
            <surname>Young</surname>
          </editor>
          <title>Web Annotation Vocabulary</title>
          <ptr target="https://www.w3.org/TR/annotation-vocab/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2017-02-23">23 February 2017</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CH-BIBL-3">
        <monogr>
          <title>The Unicode Standard, Version 5.0</title>
          <ptr target="https://www.unicode.org/"/>
          <author>Unicode Consortium</author>
          <imprint>
            <publisher>Addison-Wesley Professional</publisher>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CH-BIBL-4">
        <monogr>
          <editor>
            <forename>Addison</forename>
            <surname>Phillips</surname>
          </editor>
          <editor>
            <forename>Mark</forename>
            <surname>Davis</surname>
          </editor>
          <title level="m">Tags for Identifying Languages</title>
          <idno>RFC 4646</idno>
          <imprint>
            <date>2006</date>
            <publisher>IETF</publisher>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CH-BIBL-5">
        <monogr>
          <editor>
            <forename>Addison</forename>
            <surname>Phillips</surname>
          </editor>
          <editor>
            <forename>Mark</forename>
            <surname>Davis</surname>
          </editor>
          <title level="m">Matching of Language Tags</title>
          <idno>RFC 4647</idno>
          <imprint>
            <date>2006</date>
            <publisher>IETF</publisher>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="WD-bibl-01">
        <monogr>
          <author>
            <forename>Mark</forename>
            <surname>Davis</surname>
          </author>
          <author>
            <forename>Ken</forename>
            <surname>Whistler</surname>
          </author>
          <author>
            <forename>Asmus</forename>
            <surname>Freytag</surname>
          </author>
          <title level="m">Unicode Character Database</title>
          <ptr target="https://www.unicode.org/Public/UNIDATA/UCD.html"/>
          <imprint>
            <publisher>Unicode Consortium</publisher>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="FD-BIBL-1">Fernando C. N. Pereira, <title>Grammars and logics of partial
                                           information</title>, SRI International Technical Note 420 (Menlo Park, CA: SRI
                                           International, 1987).</bibl> -->
      <biblStruct xml:id="FS-BIBL-1">
        <monogr>
          <author>
            <forename>Fernando</forename>
            <forename>C.</forename>
            <forename>N.</forename>
            <surname>Pereira</surname>
          </author>
          <title level="m"> Grammars and logics of partial information</title>
          <imprint>
            <pubPlace>Menlo Park, CA</pubPlace>
            <publisher>SRI International</publisher>
            <date>1987</date>
          </imprint>
        </monogr>
        <series>
          <title level="s">SRI International Technical Note</title>
          <biblScope unit="vol">420</biblScope>
        </series>
      </biblStruct>
      <biblStruct xml:id="FS-BIBL-5">
        <monogr>
          <author>
            <forename>Bob</forename>
            <surname>Carpenter</surname>
          </author>
          <title level="m"> The logic of typed feature structures</title>
          <imprint>
            <pubPlace>Cambridge</pubPlace>
            <publisher>Cambridge University Press</publisher>
            <date>1992</date>
          </imprint>
        </monogr>
        <series>
          <title level="s">Cambridge Tracts in Theoretical Computer Science</title>
          <biblScope unit="vol">32</biblScope>
        </series>
      </biblStruct>
      <biblStruct xml:id="FS-BIBL-2">
        <monogr>
          <author>
            <forename>Stuart</forename>
            <surname>Shieber</surname>
          </author>
          <title level="m">An Introduction to Unification-based Approaches to Grammar</title>
          <idno>CSLI Lecture Notes 4</idno>
          <imprint>
            <publisher>Center for the Study of Language and Information</publisher>
            <pubPlace>Palo Alto, CA</pubPlace>
            <date>1986</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="HD-BIBL-1">
        <monogr>
          <title level="m">Anglo-American Cataloguing Rules</title>
          <edition>Second Edition, 2002 revision, 2005 update</edition>
          <imprint>
            <pubPlace>Chicago</pubPlace>
            <publisher>American Library Association</publisher>
            <pubPlace>Ottawa</pubPlace>
            <publisher>Canadian Library Association</publisher>
            <date>2002–2005</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!--   <bibl xml:id="HD-BIBL-2">
                                           <title>Computation into Criticism</title> (Oxford, 1987).</bibl>-->
      <biblStruct xml:id="HD-BIBL-2">
        <monogr>
          <author>
            <forename>John</forename>
            <surname>Burrows</surname>
          </author>
          <title level="m">Computation into Criticism: A Study of Jane Austen's Novel and an
            Experiment in Method</title>
          <imprint>
            <pubPlace>Oxford</pubPlace>
            <publisher>Clarendon Press</publisher>
            <date>1987</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!--  <bibl xml:id="CO-BIBL-1">
                                           <title>Sociolinguistics/Soziolinguistik (An international handbook of the science of
                                           language and society. Ein internationales Handbuch zur Wissenschaft von Sprache und
                                           Gesellschaft)</title> (Berlin, New York: De Gruyter, 1988), I, pp. 271 and 274.</bibl> -->
      <biblStruct xml:id="CO-BIBL-1">
        <monogr>
          <editor>
            <forename>Klaus</forename>
            <surname>Mattheier</surname>
          </editor>
          <editor>
            <forename>Ulrich</forename>
            <surname>Ammon</surname>
          </editor>
          <editor>
            <forename>Peter</forename>
            <surname>Trudgill</surname>
          </editor>
          <title level="m" xml:lang="en" type="main">Sociolinguistics</title>
          <title level="m" xml:lang="de" type="main">Soziolinguistik</title>
          <title level="m" xml:lang="en" type="sub">An international handbook of the science of
            language and society</title>
          <title level="m" xml:lang="de" type="sub">Ein internationales Handbuch zur Wissenschaft
            von Sprache und Gesellschaft</title>
          <imprint>
            <pubPlace>Berlin</pubPlace>
            <pubPlace>New York</pubPlace>
            <publisher>De Gruyter</publisher>
            <date>1988</date>
            <biblScope unit="vol">I</biblScope>
            <biblScope unit="pp">271 and 274</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="TS-BIBL-1">
        <monogr>
          <editor>
            <forename>J.</forename>
            <forename>A.</forename>
            <surname>Edwards</surname>
          </editor>
          <editor>
            <forename>M.</forename>
            <forename>D.</forename>
            <surname>Lampert</surname>
          </editor>
          <title level="m">Talking Language: Transcription and Coding of Spoken Discourse</title>
          <imprint>
            <pubPlace>Hillsdale, N.J.</pubPlace>
            <publisher>Lawrence Erlbaum Associates</publisher>
            <date>1993</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CH-eg-02">
        <monogr>
          <author>
            <forename>Asmus</forename>
            <surname>Freytag</surname>
          </author>
          <title level="m">The Unicode Character Property Model</title>
          <title level="s">Unicode Technical Report #23</title>
          <ptr target="https://www.unicode.org/reports/tr23/"/>
          <imprint>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="WDBIDI">
        <monogr>
          <author>
            <forename>Mark</forename>
            <surname>Davis</surname>
          </author>
          <author>
            <forename>Aharon</forename>
            <surname>Lanin</surname>
          </author>
          <author>
            <forename>Andrew</forename>
            <surname>Glass</surname>
          </author>
          <title level="m">Unicode Bidirectional Algorithm</title>
          <title level="s">Unicode Standard Annex #9</title>
          <ptr target="https://www.unicode.org/reports/tr9/"/>
          <imprint>
            <date>2017-05-04</date>
          </imprint>
          <biblScope>r. 37</biblScope>
        </monogr>
      </biblStruct>
      <!--   <bibl xml:id="TS-BIBL-2">Stig Johansson, <title level="a">Encoding a Corpus in
                                           Machine-Readable Form,</title> in <title>Computational Approaches to the Lexicon: An
                                           Overview,</title> ed. B. T. S. Atkins et al. (Oxford: Oxford University Press,
                                           forthcoming).</bibl> -->
      <biblStruct xml:id="TS-BIBL-2">
        <analytic>
          <author>
            <forename>Stig</forename>
            <surname>Johansson</surname>
          </author>
          <title level="a">Encoding a Corpus in Machine-Readable Form</title>
        </analytic>
        <monogr>
          <editor>
            <!--<forename>Beryl</forename>
                                                <forename>T.</forename>-->
            <forename>Sue</forename>
            <surname>Atkins</surname>
          </editor>
          <editor>
            <forename>Antonio</forename>
            <surname>Zampolli</surname>
          </editor>
          <title level="m">Computational Approaches to the Lexicon: An Overview</title>
          <imprint>
            <pubPlace>Oxford</pubPlace>
            <publisher>Oxford University Press</publisher>
            <date>1994</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="TS-BIBL-3">Stig Johansson et al. 
                                           <title>Working Paper on Spoken Texts,</title>
                                           document TEI AI2 W1, 1991</bibl> -->
      <biblStruct xml:id="TS-BIBL-3">
        <monogr>
          <author>
            <forename>Stig</forename>
            <surname>Johansson</surname>
          </author>
          <author>
            <forename>Lou</forename>
            <surname>Burnard</surname>
          </author>
          <author>
            <forename>Jane</forename>
            <surname>Edwards</surname>
          </author>
          <author>
            <forename>And</forename>
            <surname>Rosta</surname>
          </author>
          <title level="m">Working Paper on Spoken Texts</title>
          <title type="sub">TEI document TEI AI2 W1</title>
          <imprint>
            <date>1991</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="TS-BIBL-4">
                                           <author>Brian MacWhinney</author>
                                           <title>CHAT Manual</title> ([Pittsburgh]: Dept of Psychology, Carnegie-Mellon
                                           University, 1988), pp. 87ff.</bibl> -->
      <biblStruct xml:id="TS-BIBL-4">
        <monogr>
          <author>
            <forename>Brian</forename>
            <surname>MacWhinney</surname>
          </author>
          <title level="m">CHAT Manual</title>
          <imprint>
            <pubPlace>Pittsburgh</pubPlace>
            <publisher>Dept of Psychology, Carnegie-Mellon University</publisher>
            <date>1988</date>
            <biblScope unit="pp">87ff</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="TS-BIBL-7">
        <monogr>
          <author>
            <forename>Bengt</forename>
            <surname>Loman</surname>
          </author>
          <author>
            <forename>Nils</forename>
            <surname>Jørgensen</surname>
          </author>
          <title level="m">Manual for analys och beskrivning av makrosyntagmer</title>
          <imprint>
            <pubPlace>Lund</pubPlace>
            <publisher>Studentlitteratur</publisher>
            <date>1971</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="DI-BIBL-1">
        <analytic>
          <author>
            <forename>Robert</forename>
            <forename>A.</forename>
            <surname>Amsler</surname>
          </author>
          <author>
            <forename>Frank</forename>
            <forename>W.</forename>
            <surname>Tompa</surname>
          </author>
          <title level="a">An SGML-Based Standard for English Monolingual Dictionaries</title>
        </analytic>
        <monogr>
          <title level="m" type="main">Information in Text</title>
          <title level="m" type="sub">Fourth Annual Conference of the U[niversity of] W[aterloo]
            Centre for the New Oxford English Dictionary</title>
          <meeting>Fourth Annual Conference of the U[niversity of] W[aterloo] Centre for the New
            Oxford English Dictionary, October 26-28, 1988, Waterloo, Canada</meeting>
          <imprint>
            <pubPlace>Waterloo, Canada</pubPlace>
            <date when="1988-10">October 1988</date>
            <biblScope unit="pp">61-79</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="DI-BIBL-2">Nicoletta Calzolari et al., <title level="a">Computational Model of
                                           the Dictionary Entry: Preliminary Report</title>, Acquilex: Esprit Basic Research
                                           Action No. 3030, Six-Month Deliverable, Pisa, April 1990</bibl> -->
      <biblStruct xml:id="DI-BIBL-2">
        <monogr>
          <author>
            <forename>N.</forename>
            <surname>Calzolari</surname>
          </author>
          <author>
            <forename>C.</forename>
            <surname>Peters</surname>
          </author>
          <author>
            <forename>A.</forename>
            <surname>Roventini</surname>
          </author>
          <title level="m" type="main">Computational Model of the Dictionary Entry: Preliminary
            Report</title>
          <title level="m" type="sub">Acquilex: Esprit Basic Research Action No. 3030, Six-Month
            Deliverable</title>
          <imprint>
            <pubPlace>Pisa</pubPlace>
            <date when="1990-04">April 1990</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="DI-BIBL-3">John Fought and Carol Van Ess-Dykema, <title level="a">Toward an
                                           SGML Document Type Definition for Bilingual Dictionaries, </title> TEI working paper
                                           TEI AIW20 (available from the TEI).</bibl> -->
      <biblStruct xml:id="DI-BIBL-3">
        <monogr>
          <author>
            <forename>John</forename>
            <surname>Fought</surname>
          </author>
          <author>
            <forename>Carol</forename>
            <surname>Van Ess-Dykema</surname>
          </author>
          <title level="m">Toward an SGML Document Type Definition for Bilingual
            Dictionaries</title>
          <title type="sub">TEI working paper TEI AIW20</title>
          <imprint>
            <publisher>available from the TEI.</publisher>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="DI-BIBL-4">Nancy Ide and Jean Veronis, 
                                           <title level="a">Encoding Print Dictionaries</title>, 
                                           <title>Computers and the Humanities</title> 29: 
                                           167–195, 1995</bibl> -->
      <biblStruct xml:id="DI-BIBL-4">
        <analytic>
          <author>
            <forename>Nancy</forename>
            <surname>Ide</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <surname>Veronis</surname>
          </author>
          <title level="a">Encoding Print Dictionaries</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <biblScope unit="vol">29</biblScope>
            <date>1995</date>
            <biblScope unit="pp">167-195</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="DI-BIBL-5">
        <analytic>
          <author>
            <forename>Nancy</forename>
            <surname>Ide</surname>
          </author>
          <author>
            <forename>Jacques</forename>
            <surname>Le Maitre</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <surname>Veronis</surname>
          </author>
          <title level="a">Outline of a Model for Lexical Databases</title>
        </analytic>
        <monogr>
          <title level="j">Information Processing and Management</title>
          <imprint>
            <biblScope unit="vol">29</biblScope>
            <biblScope unit="issue">2</biblScope>
            <date>1993</date>
            <biblScope unit="pp">159-186</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="DI-BIBL-6">
        <analytic>
          <author>
            <forename>Nancy</forename>
            <surname>Ide</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <surname>Veronis</surname>
          </author>
          <author>
            <forename>Susan</forename>
            <surname>Warwick-Amstrong</surname>
          </author>
          <author>
            <forename>Nicoletta</forename>
            <surname>Calzolari</surname>
          </author>
          <title level="a">Principles for Encoding machine readable dictionaries</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of the Fifth EURALEX International Congress,
            EURALEX'92</title>
          <meeting>Fifth EURALEX International Congress, EURALEX'92, University of Tampere,
            Finland</meeting>
          <imprint>
            <date>1992</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="DI-BIBL-7">The DANLEX Group, <title level="a">Descriptive tools for electronic
                                           processing of dictionary data, </title> in <title>Lexicographica, Series
                                           Maior</title> (Tübingen: Niemeyer, 1987).</bibl> -->
      <biblStruct xml:id="DI-BIBL-7">
        <analytic>
          <author>
            <forename>The</forename>
            <surname>DANLEX Group</surname>
          </author>
          <title level="a">Descriptive tools for electronic processing of dictionary data</title>
        </analytic>
        <monogr>
          <title level="j">Lexicographica, Series Maior</title>
          <imprint>
            <pubPlace>Tübingen</pubPlace>
            <publisher>Niemeyer</publisher>
            <date>1987</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="DI-BIBL-8">A. Tutin and Jean Véronis, J. (1998). <title level="a">Electronic
                                           dictionary encoding: customizing the TEI Guidelines</title>, in <title>Proceedings
                                           of the Eighth Euralex International Congress</title>, 1998</bibl> -->
      <biblStruct xml:id="DI-BIBL-8">
        <analytic>
          <author>
            <forename>Agnès</forename>
            <surname>Tutin</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <surname>Veronis</surname>
          </author>
          <title level="a">Electronic dictionary encoding: customizing the TEI Guidelines</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of the Eighth Euralex International Congress</title>
          <meeting>Eighth Euralex International Congress</meeting>
          <imprint>
            <date>1998</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="DI-BIBL-9">
        <analytic>
          <author>
            <forename>N.</forename>
            <surname>Ide</surname>
          </author>
          <author>
            <forename>A.</forename>
            <surname>Kilgarriff</surname>
          </author>
          <author>
            <forename>L.</forename>
            <surname>Romary</surname>
          </author>
          <title level="a">A Formal Model of Dictionary Structure and Content</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Euralex 2000</title>
          <meeting>Euralex 2000</meeting>
          <imprint>
            <pubPlace>Stuttgart</pubPlace>
            <date>2000</date>
            <biblScope unit="pp">113-126</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="SA-BIBL-1">
        <analytic>
          <author>
            <forename>William</forename>
            <forename>A.</forename>
            <surname>Gale</surname>
          </author>
          <author>
            <forename>Kenneth</forename>
            <forename>W.</forename>
            <surname>Church</surname>
          </author>
          <title level="a">Program for aligning sentences in bilingual corpora</title>
        </analytic>
        <monogr>
          <title level="j">Computational Linguistics</title>
          <imprint>
            <biblScope unit="vol">19</biblScope>
            <date>1993</date>
            <biblScope unit="pp">75-102</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="AI-BIBL-5">
        <analytic>
          <author>
            <forename>G.</forename>
            <forename>N.</forename>
            <surname>Leech</surname>
          </author>
          <author>
            <forename>R.</forename>
            <forename>G.</forename>
            <surname>Garside</surname>
          </author>
          <title level="a">Running a Grammar Factory</title>
        </analytic>
        <monogr>
          <editor>
            <forename>S.</forename>
            <surname>Johansson</surname>
          </editor>
          <editor>
            <forename>A.-B.</forename>
            <surname>Stenstrøm</surname>
          </editor>
          <title level="m">English Computer Corpora: Selected Papers and Research Guide</title>
          <imprint>
            <pubPlace>Berlin</pubPlace>
            <publisher>de Gruyter</publisher>
            <pubPlace>New York</pubPlace>
            <publisher>Mouton</publisher>
            <date>1991</date>
            <biblScope unit="pp">pp. 15-32.</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="AI-BIBL-6">
                                           <author>I. Marshall</author>
                                           <title level="a">Choice of Grammatical Word Class without Global Syntactic Analysis:
                                           Tagging Words in the LOB Corpus,</title> in <title>Computers and the
                                           Humanities</title> 17 (1983): 139–50.</bibl> -->
      <biblStruct xml:id="AI-BIBL-6">
        <analytic>
          <author>
            <forename>I.</forename>
            <surname>Marshall</surname>
          </author>
          <title level="a">Choice of Grammatical Word Class without Global Syntactic Analysis:
            Tagging Words in the LOB Corpus</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <biblScope unit="vol">17</biblScope>
            <date>1983</date>
            <biblScope unit="pp">139-50</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="AI-BIBL-7">
                                           <author>R. G. Garside, G. N. Leech, and G. R. Sampson</author>
                                           <title>The Computational Analysis of English: a Corpus-Based Approach</title> (Oxford:
                                           Oxford University Press, 1991).</bibl> -->
      <biblStruct xml:id="AI-BIBL-7">
        <monogr>
          <author>
            <forename>R.</forename>
            <forename>G.</forename>
            <surname>Garside</surname>
          </author>
          <author>
            <forename>G.</forename>
            <forename>N.</forename>
            <surname>Leech</surname>
          </author>
          <author>
            <forename>G.</forename>
            <forename>R.</forename>
            <surname>Sampson</surname>
          </author>
          <title level="m">The Computational Analysis of English: a Corpus-Based Approach</title>
          <imprint>
            <pubPlace>Oxford</pubPlace>
            <publisher>Oxford University Press</publisher>
            <date>1991</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="GD-BIBL-1">
                                           <author>Gary Chartrand and Linda Lesniak</author>, <title>Graphs and Digraphs</title>
                                           (Menlo Park, CA: Wadsworth, 1986).</bibl> -->
      <biblStruct xml:id="GD-BIBL-1">
        <monogr>
          <author>
            <forename>Gary</forename>
            <surname>Chartrand</surname>
          </author>
          <author>
            <forename>Linda</forename>
            <surname>Lesniak</surname>
          </author>
          <title level="m">Graphs and Digraphs</title>
          <imprint>
            <pubPlace>Menlo Park, CA</pubPlace>
            <publisher>Wadsworth</publisher>
            <date>1986</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="GD-BIBL-2">R. Jackendoff, <title>X-Bar Syntax: A study of phrase
                                           structure</title>, in Linguistic Inquiry Monograph 2, 1977, </bibl> -->
      <biblStruct xml:id="GD-BIBL-2">
        <analytic>
          <author>
            <forename>R.</forename>
            <surname>Jackendoff</surname>
          </author>
          <title level="a">X-Bar Syntax: A study of phrase structure</title>
        </analytic>
        <monogr>
          <title level="j">Linguistic Inquiry Monograph</title>
          <imprint>
            <biblScope unit="vol">2</biblScope>
            <date>1977</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="CC-BIBL-1">
                                           <author>M. Kytö and M. Rissanen</author>
                                           <title level="a">The Helsinki Corpus of English Texts,</title> in <title>Corpus
                                           Linguistics: hard and soft</title>, <editor>M. Kytö, O. Ihalainen, and M.
                                           Rissanen</editor> eds. (Amsterdam: Rodopi, 1988).</bibl> -->
      <biblStruct xml:id="CC-BIBL-1">
        <analytic>
          <author>
            <forename>M.</forename>
            <surname>Kytö</surname>
          </author>
          <author>
            <forename>M.</forename>
            <surname>Rissanen</surname>
          </author>
          <title level="a">The Helsinki Corpus of English Texts</title>
        </analytic>
        <monogr>
          <editor>
            <forename>M.</forename>
            <surname>Kytö</surname>
          </editor>
          <editor>
            <forename>O.</forename>
            <surname>Ihalainen</surname>
          </editor>
          <editor>
            <forename>M.</forename>
            <surname>Rissanen</surname>
          </editor>
          <title level="m">Corpus Linguistics: hard and soft</title>
          <imprint>
            <pubPlace>Amsterdam</pubPlace>
            <publisher>Rodopi</publisher>
            <date>1988</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="NH-BIBL-1">
                                           <ref
                                           target="http://www.mulberrytech.com/Extreme/Proceedings/html/2004/DeRose01/EML2004DeRose01.html"
                                          >DeRose, 2004</ref>
                                           </bibl> -->
      <biblStruct xml:id="NH-BIBL-1">
        <analytic>
          <author>
            <forename>Steven</forename>
            <surname>DeRose</surname>
          </author>
          <title level="a">Markup overlap: a review and a horse</title>
          <ptr target="http://www.mulberrytech.com/Extreme/Proceedings/html/2004/DeRose01/EML2004DeRose01.html"/>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2004</title>
          <imprint>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="NH-BIBL-01">
        <monogr>
          <author>
            <forename>Andreas</forename>
            <surname>Witt</surname>
          </author>
          <title level="m" xml:lang="de">Multiple Informationsstrukturierung mit
            Auszeichnungssprachen. XML-basierte Methoden und deren Nutzen für die
            Sprachtechnologie</title>
          <imprint>
            <date>2002</date>
          </imprint>
        </monogr>
        <note>Ph D thesis, Bielefeld University</note>
        <note>See also <ptr target="http://xml.coverpages.org/Witt-allc2002.html"/>
        </note>
      </biblStruct>
      <!-- <bibl xml:id="NH-BIBL-2">
                                           <ref
                                           target="http://www.mulberrytech.com/Extreme/Proceedings/html/2005/Witt01/EML2005Witt01.xml"
                                          >Witt et.al. 2005</ref> -->
      <biblStruct xml:id="NH-BIBL-2">
        <analytic>
          <author>
            <forename>Mirco</forename>
            <surname>Hilbert</surname>
          </author>
          <author>
            <forename>Oliver</forename>
            <surname>Schonefeld</surname>
          </author>
          <author>
            <forename>Andreas</forename>
            <surname>Witt</surname>
          </author>
          <title level="a">Making CONCUR work</title>
          <ptr target="http://www.mulberrytech.com/Extreme/Proceedings/html/2005/Witt01/EML2005Witt01.xml"/>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2005</title>
          <imprint>
            <date>2005</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="NH-BIBL-3">
                                           <ref target="http://www.eppt.org/~emil/publications/dke04-concurrent.pdf">Dekhtyar and
                                           Iacob 2005</ref>
                                           </bibl> -->
      <biblStruct xml:id="NH-BIBL-3">
        <monogr>
          <author>
            <forename>Alex</forename>
            <surname>Dekhtyar</surname>
          </author>
          <author>
            <forename>Ionut</forename>
            <forename>E.</forename>
            <surname>Iacob</surname>
          </author>
          <title level="m">A framework for management of concurrent XML markup</title>
          <!-- MDH 2014-01-22 Note: This is a 404 and the website appears to be down. Replaced with another source.-->
          <!--<ptr target="http://www.eppt.org/~emil/publications/dke04-concurrent.pdf"/>-->
          <ptr target="http://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=1104&amp;context=csse_fac"/>
          <imprint>
            <date>2005</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="NH-BIBL-4">
                                           <ref target="http://www.research.att.com/~divesh/papers/jlssw2004-mct.pdf">Jagadish et
                                           al. 2004</ref>
                                           </bibl> -->
      <biblStruct xml:id="NH-BIBL-4">
        <monogr>
          <author>
            <forename>H.</forename>
            <forename>V.</forename>
            <surname>Jagadish</surname>
          </author>
          <author>
            <forename>Laks</forename>
            <forename>V.</forename>
            <forename>S.</forename>
            <surname>Lakshmanan</surname>
          </author>
          <author>
            <forename>Monica</forename>
            <surname>Scannapieco</surname>
          </author>
          <author>
            <forename>Divesh</forename>
            <surname>Srivastava</surname>
          </author>
          <author>
            <forename>Nuwee</forename>
            <surname>Wiwatwattana</surname>
          </author>
          <title level="m">Colorful XML: one hierarchy isn't enough</title>
          <!-- MDH 2014-01-22 Note: Old URL redirects to new location, so ptr updated.  -->
          <!-- MDH 2015-12-28 Note: New URL server disappeared from the web, so now linking to archive.org copy.  -->
          <!--<ptr target="http://www.research.att.com/~divesh/papers/jlssw2004-mct.pdf"/>-->
          <!--<ptr target="http://www2.research.att.com/~divesh/papers/jlssw2004-mct.pdf"/>-->
          <ptr target="http://web.archive.org/web/20150706093254/http://www2.research.att.com/~divesh/papers/jlssw2004-mct.pdf"/>
          <imprint>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="NH-BIBL-5">
                                           <ref target="http://www.idealliance.org/papers/extreme/proceedings/html/2007/Chatti01/EML2007Chatti01.html"> Chatti 2006</ref>
                                           </bibl> -->
      <biblStruct xml:id="NH-BIBL-5">
        <analytic>
          <author>
            <forename>Noureddine</forename>
            <surname>Chatti</surname>
          </author>
          <author>
            <forename>Suha</forename>
            <surname>Kaouk</surname>
          </author>
          <author>
            <forename>Sylvie</forename>
            <surname>Calabretto</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <forename>Marie</forename>
            <surname>Pinon</surname>
          </author>
          <title level="a">MultiX: an XML based formalism to encode multistructured
            documents</title>
          <!-- MDH 2014-01-22 Note: old URL was 404, replaced with new location.  -->
          <!--<ptr target="http://www.idealliance.org/papers/extreme/proceedings/html/2007/Chatti01/EML2007Chatti01.html"/>-->
          <ptr target="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.115.1525&amp;rep=rep1&amp;type=pdf"/>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2007</title>
          <imprint>
            <date>2007</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="NH-BIBL-6">Durusau et.al. 2002</bibl> -->
      <biblStruct xml:id="NH-BIBL-6">
        <analytic>
          <author>
            <forename>Patrick</forename>
            <surname>Durusau</surname>
          </author>
          <author>
            <forename>Matthew</forename>
            <forename>Brook</forename>
            <surname>O'Donnell</surname>
          </author>
          <title level="a">Coming down from the trees: next step in the evolution of markup?</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2002</title>
          <imprint>
            <date>2002</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!--<bibl xml:id="NH-BIBL-7">Tennison and Piez 2002</bibl> -->
      <biblStruct xml:id="NH-BIBL-7">
        <analytic>
          <author>
            <forename>Jeni</forename>
            <surname>Tennison</surname>
          </author>
          <author>
            <forename>Wendell</forename>
            <surname>Piez</surname>
          </author>
          <title level="a">The layered markup and annotation language</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages Conference</title>
          <imprint>
            <date>2002</date>
          </imprint>
        </monogr>
      </biblStruct>
      <!-- <bibl xml:id="NH-BIBL-8">Sperberg-McQueen and Huitfeldt 2002, 2001, Sperberg-McQueen 2006</bibl> -->
      <biblStruct xml:id="NH-BIBL-8">
        <monogr>
          <author>
            <forename>Claus</forename>
            <surname>Huitfeldt</surname>
          </author>
          <author>
            <forename>C.</forename>
            <forename>Michael</forename>
            <surname>Sperberg-McQueen</surname>
          </author>
          <title level="m">TexMECS: An experimental markup meta-language for complex
            documents</title>
          <ptr target="http://mlcd.blackmesatech.com/mlcd/2003/Papers/texmecs.html"/>
          <imprint>
            <date>2001</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="FS-BIBL-01">
        <analytic>
          <author>
            <forename>D. Terence</forename>
            <surname>Langendoen</surname>
          </author>
          <author>
            <forename>Gary F. </forename>
            <surname>Simons</surname>
          </author>
          <title level="a">A rationale for the TEI recommendations for feature-structure
            markup,</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <biblScope unit="vol">29</biblScope>
            <date>1995</date>
            <biblScope unit="pp">167-195</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="BS-5605">
        <monogr>
          <author>British Standards Institute</author>
          <title level="m">BS 5605:1990: Recommendations for Citing and Referencing Published
            Material</title>
          <imprint>
            <date>1990</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="BS-6371">
        <monogr>
          <author>British Standards Institute</author>
          <title level="m">BS 6371:1983: Recommendations for Citation of Unpublished
            Documents</title>
          <imprint>
            <date>1983</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="DIN-1505-2">
        <monogr>
          <author>Deutsches Institut für Normung</author>
          <title level="m">DIN 1505-2: Titelangaben von Dokumenten; Zitierregeln</title>
          <imprint>
            <date>1984</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="RAK">
        <monogr>
          <author>Die Deutsche Bibliothek</author>
          <title level="m">Regeln für die alphabetische Katalogisierung in wissenschaftlichen
            Bibliotheken RAK-WB</title>
          <imprint>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="ISO-690">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO 690:1987: Information and documentation – Bibliographic references – Content,
            form and structure</title>
          <imprint>
            <date>1987</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="ISO-8601">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO 8601:2004: Data elements and interchange formats — Information interchange —
            Representation of dates and times</title>
          <imprint>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="ISO-12620">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO 12620:2009: Terminology and other language and content resources –
            Specification of data categories and management of a Data Category Registry for language
            resources</title>
          <ptr target="http://www.iso.org/iso/catalogue_detail?csnumber=37243"/>
          <imprint>
            <date>2009</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="ISO-19136">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO 19136:2007: Geographic information — Geography Markup Language (GML)</title>
          <imprint>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="ISO-19757-3">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO/IEC 19757-3:2006: Information technology — Document Schema Definition Languages
            (DSDL) – Part 3: Rule-based validation – Schematron</title>
          <imprint>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="RICA">
        <monogr>
          <author>Istituto Centrale per il Catalogo Unico</author>
          <title level="m">Regole italiane di catalogazione per autori</title>
          <imprint>
            <date>1979</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="ANSI-NISO-Z39.29">
        <monogr>
          <author>National Information Standards Organization</author>
          <title>ANSI/NISO Z39.29 – 2005 (R2010) Bibliographic References</title>
          <imprint>
            <date>2010</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="ISBD">
        <monogr>
          <title level="m">ISBD: International Standard Bibliographic Description</title>
          <imprint>
            <pubPlace>Berlin, München</pubPlace>
            <pubPlace>De Gruyter Saur</pubPlace>
            <date>2011</date>
          </imprint>
        </monogr>
        <series>
          <title>IFLA Series on Bibliographic Control</title>
          <biblScope unit="vol">44</biblScope>
        </series>
      </biblStruct>
      <biblStruct xml:id="GOST-7.0.5">
        <monogr>
          <author>Федеральное агентство по техническому регулированию и метрологии
            (РОССТАНДАРТ)</author>
          <title level="m">ГОСТ Р 7.0.5-2008: Система стандартов по информации, библиотечному и
            издательскому делу. Библиографическая ссылка. Общие требования и правила
            составления</title>
          <imprint>
            <date>2008</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="GOST-7.1">
        <monogr>
          <author>Федеральное агентство по техническому регулированию и метрологии
            (РОССТАНДАРТ)</author>
          <title level="m">ГОСТ 7.1—2003. Система стандартов по информации, библиотечному и
            издательскому делу. Библиографическая запись. Библоиграфическое описание. Общие
            требования и правила составления</title>
          <imprint>
            <date>2003</date>
          </imprint>
        </monogr>
      </biblStruct>
      <biblStruct xml:id="CO-BIBL-2">
        <monogr>
          <author>DCMI Usage Board</author>
          <title>Dublin Core™ Metadata Element Set, Version 1.1: Reference Description</title>
          <ptr target="https://www.dublincore.org/specifications/dublin-core/dces/"/>
          <imprint>
            <date>2012-06-14</date>
          </imprint>
        </monogr>
      </biblStruct>
    </listBibl>
  </div>
  <div xml:id="BIB-RDG">
    <head>Reading List</head>
    <p rend="display">The following lists of readings in markup theory and the TEI derive from work
      originally prepared by Susan Schreibman and Kevin Hawkins for the TEI Education Special
      Interest Group, recoded in TEI P5 by Sabine Krott and Eva Radermacher. They should be regarded
      only as a snapshot of work in progress, to which further contributions and corrections are
      welcomed (see further <ptr target="http://www.tei-c.org/Support/Learn/tei_bibliography.xml"/>).</p>
    <div>
      <head>Theory of Markup and XML</head>
      <listBibl>
        <biblStruct xml:id="XX-1">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeld</surname>
            </author>
            <title level="a">Concurrent Document Hierarchies in MECS and SGML</title>
          </analytic>
          <monogr>
            <title level="j">Literary and Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">14</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1999</date>
              <biblScope unit="pp">29-42</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="XX-2">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Rabbit/duck grammars: a validation method for overlapping
              structures</title>
            <ptr target="http://conferences.idealliance.org/extreme/html/2006/SperbergMcQueen01/EML2006SperbergMcQueen01.html"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of Extreme Markup Languages 2006</title>
            <imprint>
              <date>2006</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Barnardetal1995">
          <analytic>
            <author>
              <forename>David</forename>
              <forename>T.</forename>
              <surname>Barnard</surname>
            </author>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Jean-Pierre</forename>
              <surname>Gaspart</surname>
            </author>
            <author>
              <forename>Lynne</forename>
              <forename>A.</forename>
              <surname>Price</surname>
            </author>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Giovanni</forename>
              <forename>Battista</forename>
              <surname>Varile</surname>
            </author>
            <title level="a">Hierarchical Encoding of Text: Technical Problems and SGML
              Solutions</title>
            <idno type="DOI">10.1007/BF01830617</idno>
            <ptr target="http://www.tei-c.org/Vault/ML/mlw18.ps"/>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">29</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1995</date>
              <biblScope unit="pp">211–231</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Barnardetal1996">
          <analytic>
            <author>
              <forename>David</forename>
              <forename>T.</forename>
              <surname>Barnard</surname>
            </author>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Lessons learned from using SGML in the Text Encoding Initiative</title>
            <idno type="DOI">10.1016/0920-5489(95)00035-6</idno>
          </analytic>
          <monogr>
            <title level="j">Computer Standards &amp; Interfaces</title>
            <imprint>
              <biblScope unit="vol">18</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1996</date>
              <biblScope unit="pp">3–10</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard1991">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">What is SGML and how does it help?</title>
            <ptr target="http://www.tei-c.org/Vault/ED/EDW25/"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Daniel</forename>
              <surname>Greenstein</surname>
            </editor>
            <title level="m">Modelling Historical Data: Towards a Standard for Encoding and
              Exchanging Machine-readable Texts</title>
            <imprint>
              <pubPlace>St Katherinen</pubPlace>
              <publisher>Max-Planck-Institut für Geschichte In Kommission bei Scripta Mercaturae
                Verlag</publisher>
              <date>1991</date>
              <biblScope unit="pp">81–91</biblScope>
            </imprint>
          </monogr>
          <series>
            <title level="s">Halbgraue Reihe zur Historischen Fachinformatik</title>
            <respStmt>
              <resp>Herausg. von</resp>
              <persName>
                <forename>Manfred</forename>
                <surname>Thaller</surname>
              </persName>
            </respStmt>
            <biblScope>serie A</biblScope>
            <biblScope unit="vol">11</biblScope>
          </series>
          <!--note>last accessed August 12, 2007</note-->
          <note>Revised version published as <ptr target="#Burnard1995a"/></note>
        </biblStruct>
        <biblStruct xml:id="Burnard1995a">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">SGML on the Web: Too Little Too Soon or Too Much Too Late?</title>
            <ptr target="http://users.ox.ac.uk/~lou/Belux/"/>
          </analytic>
          <monogr>
            <title level="j">Computers &amp; Texts</title>
            <imprint>
              <biblScope unit="vol">15</biblScope>
              <date>1995</date>
              <biblScope unit="pp">12–15</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Burnard1995c">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">What is SGML and How Does It Help?</title>
            <idno type="DOI">10.1007/BF01830315</idno>
            <ptr target="http://xml.coverpages.org/burnardw25-index.html"/>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">29</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1995</date>
              <biblScope unit="pp">41–50</biblScope>
            </imprint>
          </monogr>
          <note>Reprinted in <ptr target="#Ide1995b"/>, pp. 41-50</note>
        </biblStruct>
        <biblStruct xml:id="Ide1995b">
          <monogr>
            <editor>
              <forename>Nancy</forename>
              <surname>Ide</surname>
            </editor>
            <editor>
              <forename>Jean</forename>
              <surname>Veronis</surname>
            </editor>
            <title level="m">The Text Encoding Initiative: Background and Contexts</title>
            <imprint>
              <pubPlace>Dordrecht</pubPlace>
              <pubPlace>Boston</pubPlace>
              <publisher>Kluwer Academic Publisher</publisher>
              <date>1995</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard1999a">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">Is Humanities Computing an Academic Discipline? or, Why Humanities
              Computing Matters</title>
            <ptr target="http://www.iath.virginia.edu/hcs/burnard.html"/>
            <ptr target="http://www.iath.virginia.edu/hcs/"/>
            <imprint>
              <date>1999</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 29, 2007</note-->
          <note>Presented at an interdisciplinary seminar at the Institute for Advanced Technology
            in the Humanities, University of Virginia, November 1999.</note>
        </biblStruct>
        <biblStruct xml:id="Burnard1999b">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Using SGML for Linguistic Analysis: The Case of the BNC</title>
            <ptr target="http://users.ox.ac.uk/~lou/papers/sgml96.sgm"/>
          </analytic>
          <monogr>
            <title level="j">Markup Languages Theory and Practice</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <date>1999</date>
              <pubPlace>Cambridge, Massachusettes</pubPlace>
              <publisher>MIT Press</publisher>
              <biblScope unit="pp">31–51</biblScope>
            </imprint>
          </monogr>
          <note>Also published in <ptr target="#Moser2001a"/>, pp. 53–72</note>
        </biblStruct>
        <biblStruct xml:id="Moser2001a">
          <monogr>
            <editor>
              <forename>Stephan</forename>
              <surname>Moser</surname>
            </editor>
            <editor>
              <forename>Peter</forename>
              <surname>Stahl</surname>
            </editor>
            <editor>
              <forename>Werner</forename>
              <surname>Wegstein</surname>
            </editor>
            <editor>
              <forename>Norbert</forename>
              <forename>Richard</forename>
              <surname>Wolf</surname>
            </editor>
            <title level="m">Maschinelle Verarbeitung Altdeutscher Texte V (Beiträge zum Fünften
              Internationalen Symposion, Würzburg, 4–6 März 1997)</title>
            <imprint>
              <pubPlace>Tübingen</pubPlace>
              <publisher>Niemeyer</publisher>
              <date>2001</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnardetal1999">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Elizabeth</forename>
              <surname>Lalou</surname>
            </author>
            <author>
              <forename>Peter</forename>
              <surname>Robinson</surname>
            </author>
            <title level="a">Vers un Standard Européen de Description des Manuscrits: Le Projet
              Master</title>
          </analytic>
          <monogr>
            <title level="j" type="main">Documents Numeriques</title>
            <title level="j" type="sub">Les Documents Anciens</title>
            <imprint>
              <biblScope unit="vol">3</biblScope>
              <biblScope unit="issue">1–2</biblScope>
              <date>1999</date>
              <pubPlace>Paris</pubPlace>
              <publisher>Hermes Science Publications</publisher>
              <biblScope unit="pp">151-169</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard1999">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">XML: The Dream and the Reality</title>
            <ptr target="http://users.ox.ac.uk/~lou/papers/euro99.xml"/>
            <imprint>
              <date>1999</date>
            </imprint>
          </monogr>
          <note>Closing plenary address at the XML Europe Conference, Granada, May 1999</note>
        </biblStruct>
        <biblStruct xml:id="Burnardetal2000">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Claudia</forename>
              <surname>Claridge</surname>
            </author>
            <author>
              <forename>Josef</forename>
              <surname>Schmied</surname>
            </author>
            <author>
              <forename>Rainer</forename>
              <surname>Siemund</surname>
            </author>
            <title level="a">Encoding the Lampeter Corpus</title>
            <ptr target="http://users.ox.ac.uk/~lou/papers/glasgie.xml"/>
          </analytic>
          <monogr>
            <title level="m">DRH98: Selected Papers from Digital Resources for the
              Humanities</title>
            <imprint>
              <pubPlace>London</pubPlace>
              <publisher>Office for Humanities Communication</publisher>
              <date>2000</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Burnard2000">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">From Two Cultures to Digital Culture: The Rise of the Digital
              Demotic</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/twocults.html"/>
            <imprint>
              <date>2000</date>
            </imprint>
          </monogr>
          <note>Presented at CLIP, Alicante</note>
          <!--note>last accessed on August 12, 2007</note-->
          <note> Published in Italian as <ptr target="#Burnard2001a"/>
          </note>
        </biblStruct>
        <biblStruct xml:id="Burnard2001a">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Dalle «Due Culture» Alla Cultura Digitale: La Nascita del Demotico
              Digitale</title>
            <respStmt>
              <resp>Translated by</resp>
              <persName>
                <forename>Federico</forename>
                <surname>Pellizi</surname>
              </persName>
            </respStmt>
          </analytic>
          <monogr>
            <title level="j" type="main">Il Verri</title>
            <title level="j" type="sub">Nella Rete</title>
            <imprint>
              <biblScope unit="vol">16</biblScope>
              <date>2001</date>
              <pubPlace>Milano</pubPlace>
              <publisher>Monogramma</publisher>
              <biblScope unit="pp">9–22</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard2001b">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">On the Hermeneutic Implications of Text Encoding</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/herman.htm"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Domenico</forename>
              <surname>Fiormonte</surname>
            </editor>
            <editor>
              <forename>Jonathan</forename>
              <surname>Usher</surname>
            </editor>
            <title level="m">New Media and the Humanities: Research and Applications</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Humanities Computing Unit</publisher>
              <date>2001</date>
              <biblScope unit="pp">31–38</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed on August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Burnard2005a">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Encoding Standards for the Electronic Edition</title>
            <ptr target="http://nl.ijs.si/e-zrc/bib/eziss-Burnard.pdf"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Matija</forename>
              <surname>Ogrin</surname>
            </editor>
            <title level="m" xml:lang="sl" type="main">Znanstvene Izdaje in Elektronski
              Medij</title>
            <title level="m" xml:lang="en" type="sub">Scholarly Editions and the Digital
              Medium</title>
            <imprint>
              <pubPlace>Ljubljana</pubPlace>
              <publisher>Studia Litteraria ZRC ZAZU</publisher>
              <date>2005</date>
              <biblScope unit="pp">12–67</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Burnard2005b">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Metadata for corpus work</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/metadata.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Martin</forename>
              <surname>Wynne</surname>
            </editor>
            <title level="m">Developing Linguistic Corpora: A Guide to Good Practice</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Oxbow Books</publisher>
              <date>2005</date>
              <biblScope unit="pp">30–46</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Burnardetaleds2006">
          <monogr>
            <editor>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </editor>
            <editor>
              <forename>Katherine</forename>
              <forename>O'Brien</forename>
              <surname>O'Keefe</surname>
            </editor>
            <editor>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </editor>
            <title level="m">Electronic Textual Editing</title>
            <ptr target="http://www.tei-c.org/Vault/ETE/"/>
            <imprint>
              <pubPlace>New York</pubPlace>
              <publisher>Modern Languages Association</publisher>
              <date>2006</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Buzzetti2002">
          <analytic>
            <author>
              <forename>Dino</forename>
              <surname>Buzzetti</surname>
            </author>
            <title level="a">Digital Representation and the Text Model</title>
            <ptr target="http://muse.jhu.edu/journals/new_literary_history/v033/33.1buzzetti.html"/>
          </analytic>
          <monogr>
            <title level="j">New Literary History</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2002</date>
              <biblScope unit="pp">61–88</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Caton2001">
          <analytic>
            <author>
              <forename>Paul</forename>
              <surname>Caton</surname>
            </author>
            <title level="a">Markup's Current Imbalance</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory and Practice</title>
            <imprint>
              <biblScope unit="vol">3</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2001</date>
              <biblScope unit="pp">1–13</biblScope>
            </imprint>
          </monogr>
          <note>This paper was proceeded by reports at the Joint Annual Conference of the
            Association for Computers and the Humanities and the Association for Literary and
            Linguistic Computing in 1999 (Charlottesville, Virginia) and Extreme Markup Languages
            2000 (Montreal, Canada)</note>
        </biblStruct>
        <biblStruct xml:id="ChenandYu2003">
          <analytic>
            <author>
              <forename>Ruey-Shun</forename>
              <surname>Chen</surname>
            </author>
            <author>
              <forename>Shien-Chiang</forename>
              <surname>Yu</surname>
            </author>
            <title level="a">Developing an XML Framework for Metadata System</title>
            <ptr target="http://dl.acm.org/citation.cfm?id=963653"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of the 1st International Symposium on Information and
              Communication Technologies</title>
            <imprint>
              <pubPlace>Dublin</pubPlace>
              <date>2003</date>
              <biblScope unit="pp">267–272</biblScope>
            </imprint>
          </monogr>
          <series>
            <title level="s">ACM International Conference Proceeding Series</title>
            <biblScope unit="vol">49</biblScope>
          </series>
          <!--note>last accessed August 12, 2007</note-->
          <note>This paper was presented in a session entitled "Electronic Document
            Technology."</note>
        </biblStruct>
        <biblStruct xml:id="Coombs1986">
          <monogr>
            <author>
              <forename>James</forename>
              <forename>H.</forename>
              <surname>Coombs</surname>
            </author>
            <title level="m">Information Management System for Scholars</title>
            <idno>Technical Memorandum TM 69–2</idno>
            <imprint>
              <pubPlace>Providence</pubPlace>
              <publisher>Brown Computer Center</publisher>
              <date>1986</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Coombsetal1987">
          <analytic>
            <author>
              <forename>James</forename>
              <forename>H.</forename>
              <surname>Coombs</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>Steven</forename>
              <forename>J.</forename>
              <surname>DeRose</surname>
            </author>
            <title level="a">Markup Systems and The Future of Scholarly Text Processing</title>
            <idno type="DOI">10.1145/32206.32209</idno>
            <ptr target="http://xml.coverpages.org/coombs-hallgren.html"/>
            <ptr target="http://xml.coverpages.org/coombs.html"/>
          </analytic>
          <monogr>
            <title level="j">Communications of the ACM</title>
            <imprint>
              <biblScope unit="vol">30</biblScope>
              <biblScope unit="issue">11</biblScope>
              <date>1987</date>
              <biblScope unit="pp">933–947</biblScope>
            </imprint>
          </monogr>
          <note>Reprinted with new commentary in <ptr target="#Landow1993a"/>, pp 85–118</note>
        </biblStruct>
        <biblStruct xml:id="Landow1993a">
          <monogr>
            <editor>
              <forename>George</forename>
              <forename>P.</forename>
              <surname>Landow</surname>
            </editor>
            <editor>
              <forename>Paul</forename>
              <surname>Delany</surname>
            </editor>
            <title level="m">The Digital Word: Text-based Computing in the Humanities</title>
            <imprint>
              <pubPlace>Cambridge, MA</pubPlace>
              <publisher>MIT Press</publisher>
              <date>1993</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Cover2005">
          <monogr>
            <author>
              <forename>Robin</forename>
              <surname>Cover</surname>
            </author>
            <title level="m">Markup Languages and (Non-) Hierarchies</title>
            <ptr target="http://xml.coverpages.org/hierarchies.html"/>
            <imprint>
              <date>2005</date>
            </imprint>
          </monogr>
          <note>Technology report from the Cover Pages</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="DeRose1995">
          <monogr>
            <author>
              <forename>Steven</forename>
              <forename>J.</forename>
              <surname>DeRose</surname>
            </author>
            <title level="m">Structured Information: Navigation, Access, and Control</title>
            <ptr target="http://xml.coverpages.org/deroseStructure.html"/>
            <imprint>
              <date>1995</date>
            </imprint>
          </monogr>
          <note>Paper presented at the Berkeley Finding Aid Conference, April 4–6, 1995</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="DeRoseetal1990">
          <analytic>
            <author>
              <forename>Steven</forename>
              <forename>J.</forename>
              <surname>DeRose</surname>
            </author>
            <author>
              <forename>David</forename>
              <forename>G.</forename>
              <surname>Durand</surname>
            </author>
            <author>
              <forename>Elli</forename>
              <surname>Mylonas</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">What is Text, Really?</title>
          </analytic>
          <monogr>
            <title level="j">Journal of Computing in Higher Education</title>
            <imprint>
              <biblScope unit="vol">1</biblScope>
              <biblScope unit="issue">2</biblScope>
              <date>1990</date>
              <biblScope unit="pp">3–26</biblScope>
            </imprint>
          </monogr>
          <note>Republished (<ptr target="#DeRose1997a"/>) as a "classic reprint" with invited
            commentary and authors' replies in the ACM/SIGDOC</note>
        </biblStruct>
        <biblStruct xml:id="DeRose1997a">
          <analytic>
            <author>
              <forename>Steven</forename>
              <forename>J.</forename>
              <surname>DeRose</surname>
            </author>
            <author>
              <forename>David</forename>
              <forename>G.</forename>
              <surname>Durand</surname>
            </author>
            <author>
              <forename>Elli</forename>
              <surname>Mylonas</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">What is Text, Really?</title>
            <idno type="DOI">10.1145/264842.264843</idno>
          </analytic>
          <monogr>
            <title level="j">Journal of Computer Documentation</title>
            <imprint>
              <biblScope unit="vol">21</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1997</date>
              <biblScope unit="pp">1–24</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Goldfarb1981">
          <analytic>
            <author>
              <forename>Charles</forename>
              <forename>F.</forename>
              <surname>Goldfarb</surname>
            </author>
            <title level="a">A Generalized Approach to Document Markup</title>
            <ptr target="http://users.nyct.net/~aray/notes/igm.html"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of the ACM SIGPLAN SIGOA Symposium on Text
              Manipulation</title>
            <imprint>
              <pubPlace>New York</pubPlace>
              <publisher>ACM</publisher>
              <date>1981</date>
              <biblScope>68–73</biblScope>
            </imprint>
          </monogr>
          <note>Adapted as "Annex A. Introduction to Generalized Markup" in ISO 8879</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Graham1999">
          <analytic>
            <author>
              <forename>Tony</forename>
              <surname>Graham</surname>
            </author>
            <title level="a">Unicode: What Is It and How Do I Use It?</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory &amp; Practice</title>
            <imprint>
              <biblScope unit="vol">1</biblScope>
              <biblScope unit="issue">4</biblScope>
              <date>1999</date>
              <biblScope unit="pp">75</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Hockey1996">
          <analytic>
            <author>
              <forename>Susan</forename>
              <surname>Hockey</surname>
            </author>
            <title level="a">Creating and Using Electronic Editions</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Richard</forename>
              <forename>J.</forename>
              <surname>Finneran</surname>
            </editor>
            <title level="m">The Literary Text in the Digital Age</title>
            <imprint>
              <pubPlace>Ann Arbor, MI</pubPlace>
              <publisher>University of Michigan Press</publisher>
              <date>1996</date>
              <biblScope unit="pp">1–22</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Hockeyetal1999">
          <monogr>
            <author>
              <forename>Susan</forename>
              <surname>Hockey</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>Jerome</forename>
              <forename>J.</forename>
              <surname>McGann</surname>
            </author>
            <title level="m">What is Text? A Debate on the Philosophical and Epistemological Nature
              of Text in the Light of Humanities Computing Research</title>
            <ptr target="http://www2.iath.virginia.edu/ach-allc.99/proceedings/hockey-renear2.html"/>
            <imprint>
              <date>1999</date>
            </imprint>
          </monogr>
          <note>Panel presented at ACH/ALLC 1999</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Hockey2000">
          <monogr>
            <author>
              <forename>Susan</forename>
              <surname>Hockey</surname>
            </author>
            <title level="m">Electronic Texts in the Humanities</title>
            <imprint>
              <pubPlace>New York, NY</pubPlace>
              <publisher>Oxford University Press</publisher>
              <date>2000</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Huitfeldt1994a">
          <analytic>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <title level="a">Multi-dimensional Texts in a One-dimensional Medium</title>
            <idno type="DOI">10.1007/BF01830270</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">28</biblScope>
              <biblScope unit="issue">4/5</biblScope>
              <date>1994</date>
              <biblScope unit="pp">235–241</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Huitfeldt1994b">
          <analytic>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <title level="a">Toward a Machine-Readable Version of Wittgenstein's Nachlaß: Some
              Editorial Problems</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Hans</forename>
              <forename>Gerhard</forename>
              <surname>Senger</surname>
            </editor>
            <title level="m">Philosophische Editionen. Erwartungen an sie — Wirkungen durch
              sie</title>
            <imprint>
              <pubPlace>Tübingen</pubPlace>
              <publisher>Max Niemeyer Verlag</publisher>
              <date>1994</date>
              <biblScope unit="pp">37–43</biblScope>
            </imprint>
          </monogr>
          <series>
            <title level="s">Beihefte zu editio</title>
            <biblScope unit="vol">6</biblScope>
          </series>
        </biblStruct>
        <biblStruct xml:id="Lamport1987">
          <analytic>
            <author>
              <forename>Leslie</forename>
              <surname>Lamport</surname>
            </author>
            <title level="a">Document Production: Visual or Logical?</title>
            <ptr target="http://research.microsoft.com/en-us/um/people/lamport/pubs/pubs.html#document-production"/>
          </analytic>
          <monogr>
            <title level="j">Notices of the American Mathematical Society</title>
            <imprint>
              <biblScope unit="vol">34</biblScope>
              <date>1987</date>
              <biblScope unit="pp">621–624</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <note>Republished as <ptr target="#Lamport1988a"/></note>
        </biblStruct>
        <biblStruct xml:id="Lamport1988a">
          <analytic>
            <author>
              <forename>Leslie</forename>
              <surname>Lamport</surname>
            </author>
            <title level="a">Document Production: Visual or Logical?</title>
            <ptr target="http://www.tug.org/TUGboat/Articles/tb09-1/tb20lamport.pdf"/>
          </analytic>
          <monogr>
            <title level="j">TUGboat</title>
            <imprint>
              <biblScope unit="vol">9</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1988</date>
              <biblScope unit="pp">8-10</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <!--
<biblStruct xml:id="LancashireandSperbergMcQueen1995">
<monogr>
<author><forename>Ian</forename>
<surname>Lancashire</surname>
</author>
<author><forename>C.</forename>
<forename>Michael</forename>
<surname>Sperberg-McQueen</surname>
</author>
<author>et al.</author>
<title>Discussion on the mailing list HUMANIST, November 1995–January 1996</title>
<imprint>
<date>1995–1996</date>
</imprint>
</monogr>
<idno type="url">http://www.princeton.edu/~mccarty/humanist/</idno>-->
        <!--note>last accessed August 12, 2007</note-->
        <!--</biblStruct>-->
        <biblStruct xml:id="Lavagnino1996">
          <analytic>
            <author>
              <forename>John</forename>
              <surname>Lavagnino</surname>
            </author>
            <title level="a">Completeness and Adequacy in Text Encoding</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Richard</forename>
              <forename>J.</forename>
              <surname>Finneran</surname>
            </editor>
            <title level="m">The Literary Text in the Digital Age</title>
            <imprint>
              <pubPlace>Ann Arbor, MI</pubPlace>
              <publisher>University of Michigan Press</publisher>
              <date>1996</date>
              <biblScope unit="pp">63–76</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Lightfoot1979">
          <monogr>
            <author>
              <forename>Charles</forename>
              <surname>Lightfoot</surname>
            </author>
            <title level="m">Generic Textual Element Identification—A Primer</title>
            <imprint>
              <pubPlace>Arlington</pubPlace>
              <publisher>Graphic Communications Computer Association</publisher>
              <date>1979</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Lubell1999">
          <analytic>
            <author>
              <forename>Joshua</forename>
              <surname>Lubell</surname>
            </author>
            <title level="a">Structured Markup on the Web: A Tale of Two Sites</title>
            <ptr target="http://www.mel.nist.gov/msidlibrary/doc/mlang/markuplang.htm"/>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory &amp; Practice</title>
            <imprint>
              <biblScope unit="vol">1</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1999</date>
              <biblScope unit="pp">7–22</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="McEneryetal1998">
          <monogr>
            <author>
              <forename>Tony</forename>
              <surname>McEnery</surname>
            </author>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Andrew</forename>
              <surname>Wilson</surname>
            </author>
            <author>
              <forename>Paul</forename>
              <surname>Baker</surname>
            </author>
            <title level="m">Validation of Linguistic Corpora</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/ELRA/WP3/"/>
            <imprint>
              <date>1998</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <note>Report commissioned by ELRA</note>
        </biblStruct>
        <biblStruct xml:id="McGann1997">
          <analytic>
            <author>
              <forename>Jerome</forename>
              <surname>McGann</surname>
            </author>
            <title level="a">The Rationale of Hypertext</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Kathryn</forename>
              <surname>Sutherland</surname>
            </editor>
            <title level="m">Electronic Text: Investigations in Method and Theory</title>
            <imprint>
              <pubPlace>New York, NY</pubPlace>
              <publisher>Clarendon Press Oxford</publisher>
              <date>1997</date>
              <biblScope unit="pp">19–46</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="McGann2001">
          <monogr>
            <author>
              <forename>Jerome</forename>
              <surname>McGann</surname>
            </author>
            <title level="m">Radiant Textuality: Literature After the World Wide Web</title>
            <imprint>
              <pubPlace>New York, NY</pubPlace>
              <publisher>Palgrave Macmillian</publisher>
              <date>2001</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="McGann2004">
          <analytic>
            <author>
              <forename>Jerome</forename>
              <surname>McGann</surname>
            </author>
            <title level="a">Marking Texts of Many Dimensions</title>
            <ptr target="http://www.digitalhumanities.org/companion/"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Susan</forename>
              <surname>Schreibman</surname>
            </editor>
            <editor>
              <forename>Ray</forename>
              <surname>Siemens</surname>
            </editor>
            <editor>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </editor>
            <title level="m">A Companion to Digital Humanities</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Blackwell</publisher>
              <date>2004</date>
              <biblScope unit="pp">198–217</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Morrisonetalnodate">
          <monogr>
            <author>
              <forename>Alan</forename>
              <surname>Morrison</surname>
            </author>
            <author>
              <forename>Michael</forename>
              <surname>Popham</surname>
            </author>
            <author>
              <forename>Karen</forename>
              <surname>Wikander</surname>
            </author>
            <title level="m">Creating and Documenting Electronic Texts: A Guide to Good
              Practice</title>
            <ptr type="winita" target="http://ota.ox.ac.uk/documents/creating/cdet/"/>
            <imprint>
              <date>(no date)</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Pichler1995">
          <analytic>
            <author>
              <forename>Alois</forename>
              <surname>Pichler</surname>
            </author>
            <title level="a">Advantages of a Machine-Readable Version of Wittgenstein's
              Nachlaß</title>
            <ptr type="winita" target="http://hdl.handle.net/1956/1875"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Kjell</forename>
              <forename>S.</forename>
              <surname>Johannessen</surname>
            </editor>
            <editor>
              <forename>Tore</forename>
              <surname>Nordenstam</surname>
            </editor>
            <title level="m">Culture and Value: Philosophy and the Cultural Sciences. Beiträge des
              18. Internationalen Wittgenstein Symposiums 13–20. August 1995 Kirchberg am
              Wechsel</title>
            <imprint>
              <pubPlace>Kirchberg am Wechsel</pubPlace>
              <publisher>Die Österreichische Ludwig Wittgenstein Gesellschaft</publisher>
              <date>1995</date>
              <biblScope unit="pp">770–776</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <!--idno type="handle">1956/1875</idno-->
        </biblStruct>
        <biblStruct xml:id="Piez2001">
          <analytic>
            <author>
              <forename>Wendell</forename>
              <surname>Piez</surname>
            </author>
            <title level="a">Beyond the 'Descriptive vs. Procedural' Distinction</title>
            <ptr target="http://conferences.idealliance.org/extreme/html/2001/Piez01/EML2001Piez01.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>B.</forename>
              <forename>Tommie</forename>
              <surname>Usdin</surname>
            </editor>
            <editor>
              <forename>Steven</forename>
              <forename>R.</forename>
              <surname>Newcomb</surname>
            </editor>
            <title level="m">Proceedings of Extreme Markup Languages 2001: Montreal, Canada</title>
            <imprint>
              <date>2001</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Popham1996">
          <analytic>
            <author>
              <forename>Michael</forename>
              <surname>Popham</surname>
            </author>
            <title level="a">What Is Markup and Why Does It Matter</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Michael</forename>
              <surname>Popham</surname>
            </editor>
            <editor>
              <forename>Lorna</forename>
              <surname>Hughes</surname>
            </editor>
            <title level="m">Computers and Teaching in the Humanities: Selected Papers from the
              CATH94 Conference held in Glasgow University September 9th-12th 1994</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>CTI Centre for Textual Studies</publisher>
              <date>1996</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Quin1996">
          <analytic>
            <author>
              <forename>Liam</forename>
              <surname>Quin</surname>
            </author>
            <title level="a">Suggestive Markup: Explicit Relationships in Descriptive and
              Prescriptive DTDs</title>
            <ptr target="https://www.holoweb.net/liam/papers/1996-sgml96-SuggestiveMarkup/"/>
          </analytic>
          <monogr>
            <editor>
              <forename>B.</forename>
              <forename>Tommie</forename>
              <surname>Usdin</surname>
            </editor>
            <editor>
              <forename>Deborah</forename>
              <forename>A.</forename>
              <surname>Lapeyre</surname>
            </editor>
            <title level="m">SGML'96 Conference Proceedings</title>
            <imprint>
              <pubPlace>Alexandria, VA</pubPlace>
              <publisher>Graphic Communications Association</publisher>
              <date>1996</date>
              <biblScope unit="pp">405–418</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Raymondetal1996">
          <analytic>
            <author>
              <forename>Darrell</forename>
              <surname>Raymond</surname>
            </author>
            <author>
              <forename>Frank</forename>
              <surname>Tompa</surname>
            </author>
            <author>
              <forename>Derick</forename>
              <surname>Wood</surname>
            </author>
            <title level="a">From Data Representation to Data Model: Meta-Semantic Issues in the
              Evolution of SGML</title>
            <ptr target="https://cs.uwaterloo.ca/~fwtompa/.papers/sgml.ps                                                         http://www.sciencedirect.com/science/article/pii/0920548996000335                                                         http://dl.acm.org/citation.cfm?id=1648954"/>
          </analytic>
          <monogr>
            <title level="j">Computer Standards &amp; Interfaces</title>
            <imprint>
              <biblScope unit="vol">18</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1996</date>
              <biblScope unit="pp">25–36</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Renearetal1996">
          <analytic>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Durand</surname>
            </author>
            <author>
              <forename>Elli</forename>
              <surname>Mylonas</surname>
            </author>
            <title level="a">Refining our Notion of What Text Really Is: The Problem of Overlapping
              Hierarchies</title>
            <ptr target="http://cds.library.brown.edu/resources/stg/monographs/ohco.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Susan</forename>
              <surname>Hockey</surname>
            </editor>
            <editor>
              <forename>Nancy</forename>
              <surname>Ide</surname>
            </editor>
            <title level="m">Research in Humanities Computing 4: Selected Papers from the 1992
              ALLC/ACH Conference</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Oxford University Press</publisher>
              <date>1996</date>
              <biblScope unit="pp">263–280</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Renear1997">
          <analytic>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Out of Praxis: Three (Meta)Theories of Textuality</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Kathryn</forename>
              <surname>Sutherland</surname>
            </editor>
            <title level="m">Electronic Text: Investigations in Method and Theory</title>
            <imprint>
              <pubPlace>New York, NY</pubPlace>
              <publisher>Clarendon Press Oxford</publisher>
              <date>1997</date>
              <biblScope unit="pp">107–126</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Renear2000">
          <analytic>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">The Descriptive/Procedural Distinction is Flawed</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory and Practice</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <biblScope unit="issue">4</biblScope>
              <date>2000</date>
              <biblScope unit="pp">411–420</biblScope>
            </imprint>
          </monogr>
          <!--<note>This is a slightly revised version of a paper presented at Extreme Markup
                                              Languages 2000 (Montreal, Canada). An earlier version was published in that
                                              conference's proceedings, and still earlier versions were presented in May
                                              1998 at the HIT Center at the University of Bergen and in July 1998 at the
                                              Oxford University Humanities Computing Unit.</note>-->
        </biblStruct>
        <biblStruct xml:id="Renearetal2002">
          <analytic>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Dubin</surname>
            </author>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Towards a Semantics for XML Markup</title>
            <idno type="DOI">10.1145/585058.585081</idno>
          </analytic>
          <monogr>
            <editor>
              <forename>Richard</forename>
              <surname>Furuta</surname>
            </editor>
            <editor>
              <forename>Jonathan</forename>
              <forename>I.</forename>
              <surname>Maletic</surname>
            </editor>
            <editor>
              <forename>Ethan</forename>
              <forename>V.</forename>
              <surname>Munson</surname>
            </editor>
            <title level="m">Proceedings of the 2002 ACM Symposium on Document Engineering</title>
            <imprint>
              <pubPlace>McLean, VA</pubPlace>
              <publisher>Association for Computing Machinery</publisher>
              <date>2002</date>
              <biblScope unit="pp">119–126</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Renearetal2003a">
          <analytic>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>Christopher</forename>
              <surname>Phillippe</surname>
            </author>
            <author>
              <forename>Pat</forename>
              <surname>Lawton</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Dubin</surname>
            </author>
            <title level="a">An XML Document Corresponds to Which FRBR Group 1 Entity?</title>
            <!-- MDH 2014-01-22 Note: This had two ptrs. The first ptr was a 301, so I've updated it; second was 404, so I've deleted it.  -->
            <ptr target="http://conferences.idealliance.org/extreme/html/2003/Lawton01/EML2003Lawton01.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>B.</forename>
              <forename>Tommie</forename>
              <surname>Usdin</surname>
            </editor>
            <editor>
              <forename>Steven</forename>
              <forename>R.</forename>
              <surname>Newcomb</surname>
            </editor>
            <title level="m">Proceedings of Extreme Markup Languages 2003: Montreal, Canada</title>
            <imprint>
              <date>2003</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Renearetal2003b">
          <analytic>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Dubin</surname>
            </author>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <title level="a">XML Semantics and Digital Libraries</title>
            <ptr target="http://dl.acm.org/citation.cfm?id=827192"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of the 3rd ACM/IEEE–CS Joint Conference on Digital
              Libraries</title>
            <imprint>
              <pubPlace>Los Alamitos, CA</pubPlace>
              <publisher>IEEE Computer Society</publisher>
              <date>2003</date>
              <biblScope unit="pp">303–305</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Renear2004">
          <analytic>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Text Encoding</title>
            <ptr target="http://www.digitalhumanities.org/companion/"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Susan</forename>
              <surname>Schreibman</surname>
            </editor>
            <editor>
              <forename>Ray</forename>
              <surname>Siemans</surname>
            </editor>
            <editor>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </editor>
            <title level="m">A Companion to Digital Humanities</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Blackwell</publisher>
              <date>2004</date>
              <biblScope unit="pp">218–239</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="SalmonAlt2006">
          <analytic>
            <author>
              <forename>Susanne</forename>
              <surname>Salmon-Alt</surname>
            </author>
            <title level="a">Data Structures for Etymology: Towards an Etymological Lexical
              Network</title>
            <ptr target="http://hal.archives-ouvertes.fr/docs/00/11/09/71/PDF/etymology_final_bulag.pdf"/>
          </analytic>
          <monogr>
            <title level="j" type="main">BULAG: revue internationale annuelle</title>
            <title level="j" type="sub">Numéro Etymologie</title>
            <imprint>
              <biblScope unit="vol">31</biblScope>
              <date>2006</date>
              <pubPlace>Besançon</pubPlace>
              <publisher>Presses Universitaires de Franche-Comté</publisher>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Schreibman2002a">
          <analytic>
            <author>
              <forename>Susan</forename>
              <surname>Schreibman</surname>
            </author>
            <title level="a">Computer-mediated Texts and Textuality: Theory and Practice</title>
            <idno type="DOI">10.1023/A:1016178200469</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">36</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2002</date>
              <biblScope unit="pp">283–293</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Schreibman2002b">
          <analytic>
            <author>
              <forename>Susan</forename>
              <surname>Schreibman</surname>
            </author>
            <title level="a">The Text Ported</title>
            <idno type="DOI">10.1093/llc/17.1.77</idno>
          </analytic>
          <monogr>
            <title level="j">Literary and Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">17</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2002</date>
              <biblScope unit="pp">77–87</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="SGMLUsersGroup1990">
          <monogr>
            <author>
              <orgName>SGML Users' Group</orgName>
            </author>
            <title level="m">A Brief History of the Development of SGML</title>
            <ptr target="http://www.sgmlsource.com/history/sgmlhist.htm"/>
            <imprint>
              <date>1990</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="ShipmanandMarshall1999">
          <analytic>
            <author>
              <forename>Frank</forename>
              <forename>M.</forename>
              <surname>Shipman</surname>
              <genName>III</genName>
            </author>
            <author>
              <forename>Catherine</forename>
              <forename>C.</forename>
              <surname>Marshall</surname>
            </author>
            <title level="a">Formality Considered Harmful: Experiences, Emerging Themes, and
              Directions on the Use of Formal Representations in Interactive Systems</title>
            <idno type="DOI">10.1023/A:1008716330212</idno>
            <ptr target="http://www.csdl.tamu.edu/~shipman/papers/cscw.pdf"/>
          </analytic>
          <monogr>
            <title level="j">Computer-Supported Cooperative Work</title>
            <imprint>
              <biblScope unit="vol">8</biblScope>
              <biblScope unit="issue">4</biblScope>
              <date>1999</date>
              <biblScope unit="pp">333–352</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="SperbergMcQueenandHuitfeldt1999">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <title level="a">Concurrent document hierarchies in MECS and SGML</title>
            <idno type="DOI">10.1093/llc/14.1.29</idno>
          </analytic>
          <monogr>
            <title level="j">Literary and Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">14</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1999</date>
              <biblScope unit="pp">29–42</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="SperbergMcQueenetal2000">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Meaning and Interpretation in Markup</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory and Practice</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2000</date>
              <biblScope unit="pp">215–234</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="SperbergMcQueenetal2002">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Dubin</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Drawing Inferences on the Basis of Markup</title>
            <!--         MDH 2014-01-22 Note: There were two ptrs; the first was a 301 redirect, so I've updated it, and the second was a 404, so I've deleted it.   -->
            <ptr target="http://conferences.idealliance.org/extreme/html/2002/CMSMcQ01/EML2002CMSMcQ01.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>B.</forename>
              <forename>Tommie</forename>
              <surname>Usdin</surname>
            </editor>
            <editor>
              <forename>Steven</forename>
              <forename>R.</forename>
              <surname>Newcomb</surname>
            </editor>
            <title level="m">Proceedings of Extreme Markup Languages 2002: Montreal, Canada</title>
            <imprint>
              <date>2002</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Sukovic2002">
          <analytic>
            <author>
              <forename>Suzana</forename>
              <surname>Sukovic</surname>
            </author>
            <title level="a">Beyond the Scriptorium: The Role of the Library in Text
              Encoding</title>
            <ptr target="http://www.dlib.org/dlib/january02/sukovic/01sukovic.html"/>
          </analytic>
          <monogr>
            <title level="j">D-Lib</title>
            <imprint>
              <biblScope unit="vol">8</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2002</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="UniversityofNebraskaLincolnLibraries2003">
          <monogr>
            <author>
              <orgName>University of Nebraska — Lincoln Libraries</orgName>
            </author>
            <title level="m">A Basic Guide to Text Encoding</title>
            <!--         MDH: 2014-01-22 Note: This is a 404 as of this date.    -->
            <!-- MDH: 2016-09-01 Note: Found an alternative URL, which I'll substitute
                                                 for now; I presume it's the same document. -->
            <!--<ptr target="http://libr.unl.edu:2000/guide_site/teien.html"/>-->
            <ptr target="http://cdrh.unl.edu/book/export/html/2428"/>
            <imprint>
              <date>2003</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Unsworth2001">
          <monogr>
            <author>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </author>
            <title level="m">Knowledge Representation in Humanities Computing</title>
            <ptr target="http://people.brandeis.edu/~unsworth/KR/"/>
            <imprint>
              <date>2001</date>
            </imprint>
          </monogr>
          <note>Lecture I in the eHumanities NEH Lecture Series on Technology &amp; the Humanities,
            Washington, DC, April 3, 2001</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Unsworth2000">
          <monogr>
            <author>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </author>
            <title level="m">Scholarly Primitives: What Methods Do Humanities Researchers Have in
              Common, How Might Our Tools Reflect This?</title>
            <ptr target="http://people.brandeis.edu/~unsworth/Kings.5-00/primitives.html"/>
            <imprint>
              <date>2000</date>
            </imprint>
          </monogr>
          <note> Part of a Symposium on "Humanities Computing: Formal Methods, Experimental
            Practice" sponsored by King's College, London</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Vitalietal2000">
          <analytic>
            <author>
              <forename>Fabio</forename>
              <surname>Vitali</surname>
            </author>
            <author>
              <forename>Luca</forename>
              <surname>Bompani</surname>
            </author>
            <author>
              <forename>Paolo</forename>
              <surname>Ciancarini</surname>
            </author>
            <title level="a">Hypertext Functionalities with XML</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory &amp; Practice</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <biblScope unit="issue">4</biblScope>
              <date>2000</date>
              <biblScope unit="pp">389</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Watson1992">
          <monogr>
            <author>
              <forename>Dennis</forename>
              <forename>G.</forename>
              <surname>Watson</surname>
            </author>
            <title level="m">Brief History of Document Markup</title>
            <ptr target="http://chnm.gmu.edu/digitalhistory/links/pdf/chapter3/3.19a.pdf"/>
            <imprint>
              <date>1992</date>
            </imprint>
          </monogr>
          <note>Circular 1086. Florida Cooperative Extension Service, Institute of Food and
            Agricultural Sciences, University of Florida</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Weelnodate">
          <analytic>
            <author>
              <forename>Adriaan</forename>
              <nameLink>van der</nameLink>
              <surname>Weel</surname>
            </author>
            <title level="a">The Concept of Markup</title>
            <ptr target="https://docmh.com/adriaan-van-der-weel-digital-text-and-the-gutenberg-heritage-pdf"/>
          </analytic>
          <monogr>
            <title level="m">Digital Text and the Gutenberg Heritage</title>
            <imprint>
              <date>(no date)</date>
              <biblScope unit="chap">3</biblScope>
            </imprint>
          </monogr>
          <note>in preparation; draft only</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="WeltyandIde1999">
          <analytic>
            <author>
              <forename>Christopher</forename>
              <surname>Welty</surname>
            </author>
            <author>
              <forename>Nancy</forename>
              <surname>Ide</surname>
            </author>
            <title level="a">Using the Right Tools: Enhancing Retrieval from Marked-up
              Documents</title>
            <idno type="DOI">10.1023/A:1001800717376</idno>
            <ptr target="http://link.springer.com/article/10.1023/A%3A1001800717376"/>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1–2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">59–84</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
      </listBibl>
    </div>
    <div>
      <head>TEI</head>
      <listBibl>
        <biblStruct xml:id="Bauman1996">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <title level="a">Keying NAMEs: the WWP Approach</title>
            <ptr target="http://www.wwp.brown.edu/about/history/archive/newsletter/vol02num03/nameKey-home.html"/>
          </analytic>
          <monogr>
            <title level="j">Brown University Women Writers Project Newsletter</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1996</date>
              <biblScope unit="pp">3–6</biblScope>
              <biblScope unit="pp">10–11</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="BaumanandFlanders2004">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <author>
              <forename>Julia</forename>
              <surname>Flanders</surname>
            </author>
            <title level="a">Odd Customizations</title>
            <ptr target="http://conferences.idealliance.org/extreme/html/2004/Bauman01/EML2004Bauman01.html"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of Extreme Markup Languages 2004</title>
            <imprint>
              <date>2004</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Bauman1995">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <title level="a">Tables of Contents TEI-style</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </editor>
            <title level="j" type="main">TEXT Technology: The Journal of Computer Text
              Processing</title>
            <title level="j" type="sub">Electronic Texts and the Text Encoding Initiative. A Special
              Issue of TEXT Technology</title>
            <imprint>
              <biblScope unit="vol">5</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1995</date>
              <pubPlace>Madison, SD</pubPlace>
              <publisher>College of Liberal Arts, Dakota State University</publisher>
              <biblScope unit="pp">235–247</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="BaumanandCatapano1999">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <author>
              <forename>Terry</forename>
              <surname>Catapano</surname>
            </author>
            <title level="a">TEI and the Encoding of the Physical Structure of Books</title>
            <idno type="DOI">10.1023/A:1001769103586</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1–2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">113–127</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Bauman2005">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <title level="a">TEI HORSEing Around</title>
            <ptr target="http://conferences.idealliance.org/extreme/html/2005/Bauman01/EML2005Bauman01.html"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of the Extreme Markup Languages 2005</title>
            <imprint>
              <date>2005</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Brown1994">
          <analytic>
            <author>
              <forename>Malcolm</forename>
              <forename>B.</forename>
              <surname>Brown</surname>
            </author>
            <title level="a">What is the TEI?</title>
          </analytic>
          <monogr>
            <title level="j">Information Technology and Libraries</title>
            <imprint>
              <biblScope unit="vol">13</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1994</date>
              <biblScope unit="pp">8</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard1992">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">The Text Encoding Initiative: A Progress Report</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Gerhard</forename>
              <surname>Leitner</surname>
            </editor>
            <title level="m">New Directions in Corpus Linguistics</title>
            <imprint>
              <pubPlace>Berlin</pubPlace>
              <publisher>Mouton de Gruyter</publisher>
              <date>1992</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard1993">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Rolling your own with the TEI</title>
          </analytic>
          <monogr>
            <title level="j">Information Services and Use</title>
            <imprint>
              <biblScope unit="vol">13</biblScope>
              <biblScope unit="issue">2</biblScope>
              <date>1993</date>
              <pubPlace>Amsterdam</pubPlace>
              <publisher>IOS Press</publisher>
              <biblScope unit="pp">141–154</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard1994">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">The TEI: Towards an Extensible Standard for the Encoding of
              Texts</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Seamus</forename>
              <surname>Ross</surname>
            </editor>
            <editor>
              <forename>Edward</forename>
              <surname>Higgs</surname>
            </editor>
            <title level="m">Electronic Information Resources and Historians</title>
            <imprint>
              <pubPlace>London</pubPlace>
              <publisher>British Academy</publisher>
              <date>1994</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard1995">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">The Text Encoding Initiative: An Overview</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Geoffrey</forename>
              <surname>Leech</surname>
            </editor>
            <editor>
              <forename>Greg</forename>
              <surname>Myers</surname>
            </editor>
            <editor>
              <forename>Jenny</forename>
              <surname>Thomas</surname>
            </editor>
            <title level="m">Spoken English on Computer: Transcription, Mark-up and
              Application</title>
            <imprint>
              <pubPlace>London</pubPlace>
              <publisher>Longman</publisher>
              <date>1995</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Burnard1997">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">The Text Encoding Initiative's Recommendations for the Encoding of
              Language Corpora: Theory and Practice</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/Soria/"/>
            <imprint>
              <date>1997</date>
            </imprint>
          </monogr>
          <note>Prepared for a seminar on Etiquetación y extracción de información de grandes corpus
            textuales within the Curso Industrias de la Lengua (14–18 de Julio de 1997). Sponsored
            by the Fundacion Duques de Soria.</note>
        </biblStruct>
        <biblStruct xml:id="BurnardandPopham1999">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Michael</forename>
              <surname>Popham</surname>
            </author>
            <title level="a">Putting Our Headers Together: A Report on the TEI Header Meeting 12
              September 1997</title>
            <idno type="DOI">10.1023/A:1001710828622</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <pubPlace>Dordrecht, Boston</pubPlace>
              <publisher>Kluwer Academic Publishers</publisher>
              <biblScope unit="pp">39–47</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="AB-eg-02">
          <monogr>
            <title>An Agreement to Establish a Consortium for the Maintenance of the Text Encoding
              Initiative</title>
            <ptr target="http://www.tei-c.org/About/consortium.html"/>
            <imprint>
              <date>March 1999</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="AB-eg-03">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">Text Encoding for Interchange: A New Consortium</title>
            <ptr target="http://www.ariadne.ac.uk/issue24/tei"/>
            <imprint>
              <date>2000</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Ciottied2005">
          <monogr>
            <editor>
              <forename>Fabio</forename>
              <surname>Ciotti</surname>
            </editor>
            <title level="m">Il Manuale TEI Lite: Introduzione Alla Codifica Elettronica Dei Testi
              Letterari</title>
            <imprint>
              <pubPlace>Milano</pubPlace>
              <publisher>Sylvestre Bonnard</publisher>
              <date>2005</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Chang2001">
          <analytic>
            <author>
              <forename>Sheau-Hwang</forename>
              <surname>Chang</surname>
            </author>
            <title level="a">The Implications of TEI</title>
          </analytic>
          <monogr>
            <title level="j">OCLC Systems and Services</title>
            <imprint>
              <biblScope unit="vol">17</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2001</date>
              <biblScope unit="pp">101–103</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Cournane1997">
          <monogr>
            <author>
              <forename>Mavis</forename>
              <surname>Cournane</surname>
            </author>
            <title level="m">The Application of SGML/TEI to the Processing of Complex, Multi-lingual
              Text</title>
            <note>PhD Dissertation</note>
            <imprint>
              <pubPlace>Cork, Ireland</pubPlace>
              <publisher>University College Cork</publisher>
              <date>1997</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="DigitalLibraryFederation1998">
          <monogr>
            <author>
              <orgName>Digital Library Federation</orgName>
            </author>
            <title level="m">TEI and XML in Digital Libraries: Meeting June 30 and July 1, 1998,
              Library of Congress, Summary/Proceedings</title>
            <!-- MDH 2014-09-05: commented out the link because this document is not public any more.  -->
            <!--<ptr target="http://www.lib.umich.edu/digital-library-production-service-dlps/tei-and-xml-digital-libraries"/>-->
            <imprint>
              <date>1998</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="DigitalLibraryFederation2007">
          <monogr>
            <author>
              <orgName>Digital Library Federation</orgName>
            </author>
            <title level="m" type="main">TEI Text Encoding in Libraries: Guidelines for Best
              Encoding Practices</title>
            <title level="m" type="sub">Version 3.0 (October 2011)</title>
            <ptr target="http://www.tei-c.org/SIG/Libraries/teiinlibraries/main-driver.html"/>
            <imprint>
              <date>2011</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Finney2006">
          <analytic>
            <author>
              <forename>Timothy</forename>
              <forename>J.</forename>
              <surname>Finney</surname>
            </author>
            <title level="a">Manuscript Markup</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Larry</forename>
              <forename>W.</forename>
              <surname>Hurtado</surname>
            </editor>
            <title level="m">The Freer Biblical Manuscripts: Fresh Studies of an American Treasure
              Trove</title>
            <imprint>
              <pubPlace>Atlanta, GA</pubPlace>
              <publisher>Society of Biblical Literature</publisher>
              <date>2006</date>
              <biblScope unit="pp">263-288</biblScope>
            </imprint>
          </monogr>
          <series>
            <title level="s">Text-critical studies</title>
            <biblScope unit="vol">6</biblScope>
          </series>
        </biblStruct>
        <biblStruct xml:id="GibsonandRuotolo2003">
          <analytic>
            <author>
              <forename>Matthew</forename>
              <surname>Gibson</surname>
            </author>
            <author>
              <forename>Christine</forename>
              <surname>Ruotolo</surname>
            </author>
            <title level="a">Beyond the Web: TEI, the Digital Library, and the Ebook
              Revolution</title>
            <idno type="DOI">10.1023/A:1021895322291</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">37</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2003</date>
              <biblScope unit="pp">57–63</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Loiseaunodate">
          <monogr>
            <author>
              <forename>Sylvain</forename>
              <surname>Loiseau</surname>
            </author>
            <title level="m">Les standards : autour d'XML et de la TEI</title>
            <ptr target="http://www.revue-texto.net/Corpus/Manufacture/standards/sommaire.html"/>
            <imprint>
              <date>2002</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 5, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="MarkoandKelleher2001">
          <analytic>
            <author>
              <forename>Lynn</forename>
              <surname>Marko</surname>
            </author>
            <author>
              <forename>Christina</forename>
              <surname>Kelleher Powell</surname>
            </author>
            <title level="a">Descriptive Metadata Strategy for TEI Headers: A University of Michigan
              Library Case Study</title>
            <idno type="DOI">10.1108/10650750110402585</idno>
          </analytic>
          <monogr>
            <title level="j">OCLC Systems &amp; Services</title>
            <imprint>
              <biblScope unit="vol">17</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2001</date>
              <biblScope unit="pp">117-20</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Mertz2003">
          <monogr>
            <author>
              <forename>David</forename>
              <surname>Mertz</surname>
            </author>
            <title level="m" type="main">XML Matters: TEI — the Text Encoding Initiative</title>
            <title level="m" type="sub"> An XML Dialect for Archival and Complex Documents</title>
            <ptr target="http://www.ibm.com/developerworks/xml/library/x-matters30/index.html"/>
            <imprint>
              <date>2003</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Morrison1999">
          <analytic>
            <author>
              <forename>Alan</forename>
              <surname>Morrison</surname>
            </author>
            <title level="a">Delivering Electronic Texts Over the Web: The Current and Planned
              Practices of the Oxford Text Archive</title>
            <idno type="DOI">10.1023/A:1001726011322</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">193-198</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="MylonasandRenear1999">
          <analytic>
            <author>
              <forename>Elli</forename>
              <surname>Mylonas</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">The Text Encoding Initiative at 10: Not Just an Interchange Format
              Anymore — But a New Research Community</title>
            <idno type="DOI">10.1023/A:1001832310939</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">1-9</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Nellhaus2001">
          <analytic>
            <author>
              <forename>Tobin</forename>
              <surname>Nellhaus</surname>
            </author>
            <title level="a">XML, TEI, Digital Libraries in the Humanities</title>
            <ptr target="http://muse.jhu.edu/journals/portal_libraries_and_the_academy/v001/1.3nellhaus.html"/>
          </analytic>
          <monogr>
            <title level="j">Portal: Libraries and the Academy</title>
            <imprint>
              <biblScope unit="vol">1</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2001</date>
              <biblScope unit="pp">267-277</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
        <biblStruct xml:id="Rahtz2003">
          <monogr>
            <author>
              <forename>Sebastian</forename>
              <surname>Rahtz</surname>
            </author>
            <title level="m">Building TEI DTDs and Schemas on demand</title>
            <!--     Original Oxford site now gone; Internet Archive source used instead.       -->
            <ptr target="https://web.archive.org/web/20150706100318/http://tei.oucs.ox.ac.uk/Talks/2003-05-06-xmleurope2003/xmleurope2003.pdf"/>
            <imprint>
              <date>2003</date>
            </imprint>
          </monogr>
          <note>Paper presented at XML Europe 2003, London, March 2003</note>
        </biblStruct>
        <biblStruct xml:id="Rahtzetal2004">
          <monogr>
            <author>
              <forename>Sebastian</forename>
              <surname>Rahtz</surname>
            </author>
            <author>
              <forename>Norman</forename>
              <surname>Walsh</surname>
            </author>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">A unified model for text markup: TEI, Docbook, and beyond</title>
            <ptr target="http://www.tei-c.org/Activities/Workgroups/META/xmleurope2004.pdf"/>
            <imprint>
              <date>2004</date>
            </imprint>
          </monogr>
          <note>Paper presented at XML Europe 2004, Amsterdam, April 2004</note>
        </biblStruct>
        <biblStruct xml:id="Renear1995">
          <analytic>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Theory and Metatheory in the Development of Text Encoding</title>
            <ptr target="http://uhra.herts.ac.uk/bitstream/handle/2299/7302/904841.pdf?sequence=2"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Michael</forename>
              <forename>A.</forename>
              <forename>R.</forename>
              <surname>Biggs</surname>
            </editor>
            <editor>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </editor>
            <title level="m">Philosophy and Electronic Publishing</title>
            <imprint>
              <date>1995</date>
            </imprint>
          </monogr>
          <note>Interactive seminar for the Monist</note>
          <!--note>last accessed December 19, 2006</note-->
        </biblStruct>
        <biblStruct xml:id="Robinsonnodate">
          <monogr>
            <author>
              <forename>Peter</forename>
              <surname>Robinson</surname>
            </author>
            <title level="m">Making a Digital Edition with TEI and Anastasia</title>
            <ptr target="http://sd-editions.com/AnaServer?teidoc+0+start.anv"/>
            <imprint>
              <date>(no date)</date>
            </imprint>
          </monogr>
          <!--note>last accessed January 26, 2005</note-->
        </biblStruct>
        <biblStruct xml:id="Seaman1995">
          <monogr>
            <author>
              <forename>David</forename>
              <surname>Seaman</surname>
            </author>
            <title level="m">The Electronic Text Center Introduction to TEI and Guide to Document
              Preparation</title>
            <ptr target="https://web.archive.org/web/20140804000849/etext.lib.virginia.edu/standards/tei/uvatei.html"/>
            <imprint>
              <date>1995</date>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Simons1999">
          <analytic>
            <author>
              <forename>Gary</forename>
              <forename>F.</forename>
              <surname>Simons</surname>
            </author>
            <title level="a">Using Architectural Forms to Map TEI Data into an Object-Oriented
              Database</title>
            <idno type="DOI">10.1023/A:1001765030032</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">85-101</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Smith1999">
          <analytic>
            <author>
              <forename>David</forename>
              <surname>Smith</surname>
            </author>
            <title level="a">Textual Variation and Version Control in the TEI</title>
            <idno type="DOI">10.1023/A:1001795210724</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">103-112</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="SperbergMcQueen1991">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Text in the Electronic Age: Textual Study and Text Encoding, with
              Examples from Medieval Texts</title>
            <idno type="DOI">10.1093/llc/6.1.34</idno>
          </analytic>
          <monogr>
            <title level="j">Literary &amp; Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">6</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1991</date>
              <biblScope unit="pp">34-46</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="SperbergMcQueen1994">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">The Text Encoding Initiative: Electronic Text Markup for
              Research</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Brett</forename>
              <surname>Sutton</surname>
            </editor>
            <title level="m">Literary Texts in an Electronic Age</title>
            <imprint>
              <pubPlace>Urbana-Champaign, IL</pubPlace>
              <publisher>University of Illinois at Urbana-Champaign, Graduate School of Library and
                Information Science</publisher>
              <date>1994</date>
              <biblScope unit="pp">35–55</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="SperbergMcQueen1996">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Textual Criticism and the Text Encoding Initiative</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Richard</forename>
              <forename>J.</forename>
              <surname>Finneran</surname>
            </editor>
            <title level="m">The Literary Text in the Digital Age</title>
            <imprint>
              <pubPlace>Ann Arbor, MI</pubPlace>
              <publisher>University of Michigan Press</publisher>
              <date>1996</date>
              <biblScope unit="pp">37–62</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="Vanhoutte2004">
          <analytic>
            <author>
              <forename>Edward</forename>
              <surname>Vanhoutte</surname>
            </author>
            <title level="a">An Introduction to the TEI and the TEI Consortium</title>
            <idno type="DOI">10.1093/llc/19.1.9</idno>
          </analytic>
          <monogr>
            <title level="j">Literary &amp; Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">19</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2004</date>
              <biblScope unit="pp">9</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
        <biblStruct xml:id="RFC4151">
          <monogr>
            <editor>
              <forename>T.</forename>
              <surname>Kindberg</surname>
            </editor>
            <editor>
              <forename>S.</forename>
              <surname>Hawke</surname>
            </editor>
            <title level="m">The 'tag' URI Scheme</title>
            <ptr target="https://www.ietf.org/rfc/rfc4151.txt"/>
            <idno>RFC 4151</idno>
            <imprint>
              <date>2005</date>
              <publisher>IETF</publisher>
            </imprint>
          </monogr>
        </biblStruct>
      </listBibl>
      <!--

<listBibl>

<bibl>Boot, P. and Stronks, E. (<date
when="2002-01-18">2002</date>). <title>Emblem Project Utrecht</title>
(EPU): <ref
target="http://www.let.uu.nl/emblems/html/techbiblio.html"><title>EPU
Guidelines for encoding the bibliography</title></ref> and <ref
target="http://www.let.uu.nl/emblems/html/techcoding.html"><title>EPU
Guidelines for encoding emblem books</title></ref>. Utrecht
University.</bibl>

<bibl>Charlong, L. (1998). <ref
target="http://ultratext.hil.unb.ca/Texts/guidelines/text_guide2.htm"><title>Standards
and procedures followed at the Electronic Text Centre</title></ref>. 
University of New
Brunswick Libraries, Canada. Last updated: <date 
when="1998-11-25">25 November 1998</date>. </bibl>

<bibl>Chesnutt, David R., Hockey, Susan M., Sperberg-McQueen,
C.M. (<date when="1999">1999</date>) <ref
target="http://mep.cla.sc.edu/MepGuide.html"><title>Markup Guidelines for
Documentary Editions</title></ref>. Model Editions Partnership.</bibl>

<bibl>Driscoll, M.J. ed (2000). <ref
target="http://www.hum.ku.dk/ami/handbook/"><title>Encoding
Old Norse-Icelandic primary sources using TEI-conformant SGML/XML: A
handbook</title></ref>. Last updated <date when="2000-07">July 
2000</date>.</bibl>

<bibl>Elliott, T. et al (2001). <ref
target="http://www.stoa.org/markup/epidoc02.html"><title>EpiDoc:
Guidelines for structured markup of epigraphic
texts</title></ref>. Last updated <date when="2001-01-15">15
January 2001</date>.</bibl>

<bibl>Finney, T. J. (2001). <ref
target="http://rosetta.atla-certr.org/TC/TC-leiden.html"><title>Converting
Leiden-style editions to TEI Lite XML</title></ref> (<ref
target="../Sample_Manuals/leiden.html">local copy</ref>). Last updated
<date when="2001-06-19">19 June 2001</date>.</bibl>

<bibl>Flanders, J., Mah, C., Caton, P. <ref 
target="http://www.wwp.brown.edu/encoding/training/index.html"><title>Brown 
University Women Writers Project Training Materials</title></ref> 
(includes links to detailed tutorials on
<ref target="http://www.wwp.brown.edu/encoding/training/teiheader/teiHeader.html"
><title>The TEI Header</title></ref>;
<ref target="http://www.wwp.brown.edu/encoding/training/titlepage/titlepage.html"
><title>Encoding Title Pages</title></ref>;
<ref target="http://www.wwp.brown.edu/encoding/training/lg/page1.html"
><title>LG (line group) Encoding Guide</title></ref>;
<ref target="http://www.wwp.brown.edu/encoding/training/DocAn.html"
><title>Document Analysis</title></ref>;
<ref target="http://www.wwp.brown.edu/encoding/training/TOCs/TOCs.html"
><title>Tables of Contents</title></ref>;
<ref target="http://www.wwp.brown.edu/encoding/training/castlist/castlist.html"
><title>Castlists</title></ref>;
<ref target="http://www.wwp.brown.edu/encoding/training/fw/index.html"
><title>Forme Work</title></ref>). Brown University, USA. Last
updated <date when="2001-09-14">14 September 2001</date>.
</bibl>

<bibl>Gorman, Peter C., ed (<date when="2000">2000</date>). <ref 
target="http://www.library.wisc.edu/help/tech/TEI/guidelines.html"><title>Guidelines 
for markup of electronic texts</title></ref>. University of 
Wisconsin-Madison. </bibl>

<bibl>Heiden, S.; Guillot, C; Lavrentiev, A. (2005) <ref
target="http://bfm.ens-lsh.fr/IMG/pdf/Manuel_Encodage_TEI.pdf">Manuel
d'encodage XML-TEI des textes de la Base de Francais Médiéval</ref></bibl>

<bibl>HTML Writers Guild (2000). <ref
target="http://gutenberg.hwg.org/teidtds.html"><title>An introduction to 
the Text Encoding
Initiative (TEI) DTD</title></ref> (Project Gutenberg's Introduction to using
TEI). Last updated <date when="2001-02-17">17 February 2001</date>.</bibl>

<bibl>Kushigian, N. and Payne, C. <ref 
target="http://www.lib.ucdavis.edu/English/BWRP/BWRPveg.htm"><title>British 
Women Romantic Poets Project: Encoding
Guidelines</title></ref>. University of California, Davis. </bibl>

<bibl>Light, R. (<date when="1996">1996</date>). <ref
target="http://www.cimi.org/public_docs/tagging_guide/tg.htm"><title>CIMI
Tagging Guide for the SGML DTD</title></ref>. </bibl>

<bibl>Mahoney, Anne et al (2000). <ref
target="http://www.stoa.org/markup/how_markup.shtml"><title>Introduction
to Structured Markup: How to markup a text</title></ref>. Last
updated <date when="2001-06-27">27 June 2001</date>.</bibl>

<bibl>Menota Project (2001). <ref
target="http://www.hit.uib.no/menota/handbok/innhold.html"><title>H&#x00E5;ndbok
for koding av nordiske middelaldertekster</title></ref>. Last
updated <date when="2001-06-10">10 June 2001</date>.
<ref target="http://www.hit.uib.no/menota/guidelines/">Preliminary
English version</ref>. Last updated <date>January 2002</date>.</bibl>

<bibl>Mueller, Martin (<date when="2002">2002</date>). 
<ref 
target="http://bistro.northwestern.edu/AnaServer?tei+0+frame.anv"><title>A
very gentle introduction to the TEI markup language</title></ref>
(<ref target="../Sample_Manuals/mueller-index.htm">local copy</ref>).</bibl>

<bibl>Perathoner, Marcello (<date when="2003">July 2003</date>).
<ref target="http://www.gnutenberg.de/catalog/pg-guidep4 add">The Project Gnutenberg
<title>Guide to encoding</title></ref>  (<ref
target="../Sample_Manuals/pg-guide-tei.zip">local copy</ref>).</bibl>

<bibl>Proffitt, Merillee et al (updated <date when="2002">8 Oct 2002</date>).
<ref target="http://sunsite.berkeley.edu/Scriptorium/dstoc.html">
<title>Digital Scriptorium transcription DTD: A TEI-Based Tag set for
Manuscript Transcription</title></ref>  (<ref
target="../Sample_Manuals/dsguide1.html">local copy</ref>).</bibl>

<bibl>Scholze, Hannelore and Goldstrassa, Thomas (<date 
when="2001">2001</date>).
<ref
target="http://www2.hu-berlin.de/literatur/projekte/loreley/Teilite/index.htm"><title>TEI
Lite – Vernetzung von
Verführungsszenarien</title></ref>. Prokect Loreley,
Humboldt-Universität zu Berlin.</bibl>

<bibl>Seaman, D. (<date when="1995">1995</date>).
<ref target="https://web.archive.org/web/20140804000849/etext.lib.virginia.edu/standards/tei/uvatei.html"><title>The 
Electronic Text
Center Introduction to TEI and Guide to Document 
Preparation</title></ref>. Electronic
Text Center, University of Virginia, USA. Last updated: Spring 1995.</bibl>

<bibl>Smith, Natalia, Sexton, Jill and McKim, Joshua.
<ref target="http://docsouth.unc.edu/guidelines/encoding.html">
<title>Encoding Guidelines for the Documenting the American
South database</title></ref>. Last updated <date when="2000-05">May 
2000</date>.
</bibl>

<bibl>Sperberg-McQueen, C.M. et al (<date
when="1996">1996</date>). <title>Rules
for use of TEI Lite in CIC E-Text
Projects</title>. <ref target="../Sample_Manuals/cictei.htm">Local
copy</ref>.</bibl>

<bibl>Vanhoutte, Edward (1997). <ref
target="http://www.kantl.be/ctb/vanhoutte/pub/1998/sgmleditie.htm"><title>...en
doende denkt dan nog. SGML, TEI en
editiewetenschap</title></ref>. Last updated <date 
when="2001-03-26">26 March 2001</date>.</bibl>

<bibl>Vanhoutte, Edward (2001). <ref
target="http://www.kantl.be/ctb/vanhoutte/pub/2000/headerproposal.htm"><title>It's
all in the Head(er): From minimal to optimal use of the TEI
Header</title></ref> (<ref
target="../Sample_Manuals/headerproposal.htm">local copy</ref>). Last
updated <date when="2001-03">March 2001</date>.</bibl>

<bibl>Vanhoutte, Edward and  Ron Van den Branden (2003). <ref
target="http://www.kantl.be/ctb/project/dalf/index.htm">DALF guidelines
for the description and encoding of modern correspondence
material, version 1.0 </ref>
</bibl>

<bibl>van der Weel, Adriaan et al (<date when="2000">2000</date>). <ref
target="http://www.etcl.nl/teiguide/default.htm"><title>The ETCL's
Use of TEI: A Rationale of Standardization</title></ref>. 
Electronic Text Centre, University of Leiden.
</bibl>

<bibl>Willett, P.
<ref 
target="http://www.indiana.edu/~letrs/vwwp/vwwp-about.html"><title>Victorian 
Women
Writers Project Encoding Guidelines</title></ref>. Last updated:
<date when="2000-05-02">02 May 2000</date>.</bibl>

<bibl>Willett, P. et al (1999). <ref
target="http://www.clir.org/diglib/standards/tei.htm"><title>TEI
Text Encoding in Libraries Guidelines for Best Encoding
Practices</title></ref> (<ref
target="../Sample_Manuals/bestpractice.htm">local copy</ref>).
Version 1.0 (<date when="1999-07-30">30 July 1999</date>).</bibl>

<bibl>Willett, P. et al (<date when="2001">2001</date>). <ref
target="http://www.letrs.indiana.edu/web/w/wrightmrc/guidelines.html"><title>CIC 
Wright 19th century American Fiction Project: Encoding 
Guidelines</title></ref> (includes extensive tutorial 
material).</bibl>

<bibl>Williams, J.P. and Powell, C. (1996, 1998).
American Verse Project: <title>HTI Style Guide for
American Verse Project and Middle English Texts</title>. Humanities Text
Initiative, University of Michigan. <ref
target="../Sample_Manuals/amv-manual.html">Local copy</ref> last updated
<date when="1998-01-29">29 January 1998</date>.</bibl>

<bibl>Wurzer, Andreas (<date when="1998">1998</date>). <ref
target="http://hagen.let.rug.nl/hypertext/teip3.html"><title>Linking
with TEI P3</title></ref>.</bibl>
</listBibl>
                                      -->
    </div>
  </div>
</div>

```

## Source blocks

### Block 1

XML location: `/div[1]/head[1]`.

```xml
<head>Bibliography</head>
```

^b1

### Block 2

XML location: `/div[1]/div[1]/head[1]`.

```xml
<head>Works Cited in Examples in these Guidelines</head>
```

^b2

### Block 3

XML location: `/div[1]/div[1]/listBibl[1]/bibl[1]`.

```xml
<bibl xml:id="biblzh-tw_n20" xml:lang="zh-TW">阿城，《棋王》。</bibl>
```

^b3

### Block 4

XML location: `/div[1]/div[1]/listBibl[1]/bibl[2]`.

```xml
<bibl xml:id="fr-ex-Acad" xml:lang="fr"><author>Académie française</author>,
          <title>Rectifications de l'orthographe - J.O. du 06-12-1990</title>, <ref target="http://www.academie-francaise.fr/langue/orthographe/plan.html">En ligne</ref>,
          <date>consulté le 05-03-2010</date>.</bibl>
```

^b4

### Block 5

XML location: `/div[1]/div[1]/listBibl[1]/bibl[3]`.

```xml
<bibl xml:id="DROTH-eg-57">
        <author>Adams, Douglas</author>. <title level="m">The Hitchhiker's Guide to the
          Galaxy</title>, <pubPlace>New York</pubPlace>: <publisher>Pocket Books</publisher>,
          <date>1979</date>, <biblScope unit="chap">chapter 31</biblScope>.</bibl>
```

^b5

### Block 6

XML location: `/div[1]/div[1]/listBibl[1]/bibl[4]`.

```xml
<bibl xml:id="fr-ex-Abes" xml:lang="fr"><author>Agence bibliographique de l'enseignement
          supérieur</author>, <title>ABES</title>:<ref target="http://www.abes.fr/abes/page%2C570%2Cmentions-legales.html">Site internet
        </ref>par l'<editor>ABES</editor>,<date>consulté le 05-03-2010</date>.</bibl>
```

^b6

### Block 7

XML location: `/div[1]/div[1]/listBibl[1]/bibl[5]`.

```xml
<bibl xml:id="biblzh-tw_n44" xml:lang="zh-TW">阿拉伯短劍，國史館：嚴家淦總統文物。</bibl>
```

^b7

### Block 8

XML location: `/div[1]/div[1]/listBibl[1]/bibl[6]`.

```xml
<bibl xml:id="VEMEana-eg-23"><author>Alighieri, Dante</author>. <title level="a">Doglia mi
          reca ne lo core ardire</title>, <title level="m">Rime</title>, <biblScope unit="part">XLIX</biblScope>.</bibl>
```

^b8

### Block 9

XML location: `/div[1]/div[1]/listBibl[1]/bibl[7]`.

```xml
<bibl xml:id="CONARS-eg-102"><author>Allinson, E.P.</author> and <author>B. Penrose</author>.
          <title level="m">Philadelphia 1681-1887</title> (<date>1887</date>), <biblScope unit="pp">p. 138</biblScope>.</bibl>
```

^b9

### Block 10

XML location: `/div[1]/div[1]/listBibl[1]/bibl[8]`.

```xml
<bibl xml:id="COBICOR-eg-246"><title level="m">American National Standard for Bibliographic
          References, ANSI Z39.29-1977</title>, <pubPlace>New York</pubPlace>: <publisher> American
          National Standards Institute</publisher> (<date>1977</date>). </bibl>
```

^b10

### Block 11

XML location: `/div[1]/div[1]/listBibl[1]/bibl[9]`.

```xml
<bibl xml:id="CONADA-eg-144">
        <!-- T. M. Andersson, A Preface to the Nibelungenlied         -->
        <!-- (Stanford:  Stanford University Press, 1987) p. 4        -->
        <author>Andersson, Theodore M.</author>. <title> A Preface to the Nibelungenlied</title>,
          <publisher>Stanford University Press</publisher> (<date>1987</date>).</bibl>
```

^b11

### Block 12

XML location: `/div[1]/div[1]/listBibl[1]/bibl[10]`.

```xml
<bibl xml:id="COEDADD-eg-91">
        <author>Andrews, Mr.</author>. <title level="a">Song</title>, <title level="m">Chambers's
          Edinburgh Journal Series 1</title>
        <biblScope unit="volume">9</biblScope>:<biblScope unit="issue">463</biblScope> (<date>12
          December 1840</date>), <biblScope unit="page">376</biblScope>. <ptr target="https://dvpp.uvic.ca/poems/chambers_series/1840/pom_5242_song.html"/>
      </bibl>
```

^b12

### Block 13

XML location: `/div[1]/div[1]/listBibl[1]/bibl[11]`.

```xml
<bibl xml:id="fr-ex-Antigone" xml:lang="fr"><author>Anouilh, Jean</author>, <title>
          Antigone</title>, <date>1842</date>.</bibl>
```

^b13

### Block 14

XML location: `/div[1]/div[1]/listBibl[1]/bibl[12]`.

```xml
<bibl xml:id="WHITMS2">
        <title>[As in Visions of] </title> Single leaf of Notes for a poem about night "visions,"
        possibly related to the untitled 1855 poem that Whitman eventually titled "The Sleepers."
        Fragments of an unidentified newspaper clipping about the Puget Sound area have been pasted
        to the leaf. The Trent Collection of Walt Whitman Manuscripts, Duke University Rare Book,
        Manuscript, and Special Collections Library. <ptr target="http://www.whitmanarchive.org/resources/sleepers/duk.00258.001.jpg"/>
      </bibl>
```

^b14

### Block 15

XML location: `/div[1]/div[1]/listBibl[1]/bibl[13]`.

```xml
<bibl xml:id="DIC-CR">
        <editor>Atkins et al. </editor>
        <title>Collins Robert French-English English-French Dictionary</title>.
          <pubPlace>London</pubPlace>: <publisher>Collins</publisher> (<date>1978</date>). </bibl>
```

^b15

### Block 16

XML location: `/div[1]/div[1]/listBibl[1]/bibl[14]`.

```xml
<bibl xml:id="TSSASE-eg-20">
        <author>Atkinson, J. Maxwell</author> and <author>John Heritage</author>. <title level="m">Structures of social action: Studies in conversation analysis</title>,
          <pubPlace>Cambridge</pubPlace> and <pubPlace>Paris</pubPlace>: <publisher>Cambridge
          University Press</publisher>, <series>Editions de la Maison des Sciences de
          l'Homme</series> (<date>1984</date>), <biblScope unit="pp">ix-xvi</biblScope>.</bibl>
```

^b16

### Block 17

XML location: `/div[1]/div[1]/listBibl[1]/bibl[15]`.

```xml
<bibl xml:id="CONARS-eg-101"><author>Austen, Jane</author>. <title level="m">Pride and
          Prejudice</title>. (<date>1813</date>), <biblScope unit="chap">chapter
        1</biblScope>.</bibl>
```

^b17

### Block 18

XML location: `/div[1]/div[1]/listBibl[1]/bibl[16]`.

```xml
<bibl xml:id="biblzh-tw_n25" xml:lang="zh-TW">白先勇，〈金大班的最後一夜〉，《台北人》。</bibl>
```

^b18

### Block 19

XML location: `/div[1]/div[1]/listBibl[1]/bibl[17]`.

```xml
<bibl xml:id="biblzh-tw_n26" xml:lang="zh-TW">白先勇，《孽子》。</bibl>
```

^b19

### Block 20

XML location: `/div[1]/div[1]/listBibl[1]/bibl[18]`.

```xml
<bibl xml:id="biblzh-tw_n59" xml:lang="zh-TW">白居易，《憶江南》。</bibl>
```

^b20

### Block 21

XML location: `/div[1]/div[1]/listBibl[1]/bibl[19]`.

```xml
<bibl xml:id="OTrim1.1">
        <title>Amheida I: Ostraka from Trimithis Volume 1: Texts from the 2004–2007 Seasons</title>,
          <editor>Bagnall, R. S. and G. R. Ruffini, with contributions by R. Cribiore and G.
          Vittmann</editor> (<date>2012</date>). </bibl>
```

^b21

### Block 22

XML location: `/div[1]/div[1]/listBibl[1]/bibl[20]`.

```xml
<bibl xml:id="NZETC01">
        <author>Baker, James K.</author>. <title>Night in Tarras</title>. In <title level="j">Hilltop: A Literary Paper</title>, vol 1 no 2. Wellington: Victoria University College
        Literary Society. (<date>1949</date>). </bibl>
```

^b22

### Block 23

XML location: `/div[1]/div[1]/listBibl[1]/bibl[21]`.

```xml
<bibl xml:id="fr-ex-Balzac-Chouans" xml:lang="fr"><author>Balzac, Honoré de</author>,
          <title>Les Chouans</title>, <date>1845</date>.</bibl>
```

^b23

### Block 24

XML location: `/div[1]/div[1]/listBibl[1]/bibl[22]`.

```xml
<bibl xml:id="fr-ex-Balzac_Goriot" xml:lang="fr"><author>Balzac, Honoré de</author>,
          <author>Le Père Goriot</author>, <date>1843</date>.</bibl>
```

^b24

### Block 25

XML location: `/div[1]/div[1]/listBibl[1]/bibl[23]`.

```xml
<bibl xml:id="fr-ex-Balzac_Vie" xml:lang="fr"><author>Balzac, Honoré de</author>, <title>Petites misères de la
          vie conjugale</title>, <date>1850</date>.</bibl>
```

^b25

### Block 26

XML location: `/div[1]/div[1]/listBibl[1]/bibl[24]`.

```xml
<bibl xml:id="COVE-eg-286"><author>Barbauld, Lucy Aikin</author>. <title>The Works of Anna
          Laetitia Barbauld</title> (<date>1826</date>).</bibl>
```

^b26

### Block 27

XML location: `/div[1]/div[1]/listBibl[1]/bibl[25]`.

```xml
<bibl xml:id="DS-eg-04">
        <author>Barker, Jane</author>. <title>The Lining to the Patch-Work Screen</title>
          (<date>1726</date>). </bibl>
```

^b27

### Block 28

XML location: `/div[1]/div[1]/listBibl[1]/bibl[26]`.

```xml
<bibl xml:id="COEDADD-eg-93">
        <title>Base de datos paleográfica da lírica galego-portuguesa (PalMed)</title>. Versión 1.2.
          <pubPlace>Santiago de Compostela</pubPlace>: <publisher>Centro Ramón Piñeiro para a
          Investigación en Humanidades</publisher>. <ptr target="http://www.cirp.gal/palmed"/>.
          <citedRange>f. B126r, column a, l. 21-32.</citedRange>
      </bibl>
```

^b28

### Block 29

XML location: `/div[1]/div[1]/listBibl[1]/bibl[27]`.

```xml
<bibl xml:id="fr-ex-Bataille_Arbre" xml:lang="fr"><author>Bataille, Michel</author> ,
          <title>L'Arbre de Noël</title>, <date>1967</date>.</bibl>
```

^b29

### Block 30

XML location: `/div[1]/div[1]/listBibl[1]/bibl[28]`.

```xml
<bibl xml:id="fr-ex-Baudelaire-chats" xml:lang="fr">
        <title level="a">Les Chats</title>, in : <author>Baudelaire, Charles</author>, <title level="m">Les Fleurs du mal</title>, <date>1861</date>.</bibl>
```

^b30

### Block 31

XML location: `/div[1]/div[1]/listBibl[1]/bibl[29]`.

```xml
<bibl xml:id="fr-ex-Baudelaire-vie" xml:lang="fr">
        <title level="a">La Vie antérieure</title>, in : <author>Baudelaire, Charles</author>,
          <title level="m">Les Fleurs du mal</title>, <date>1861</date>.</bibl>
```

^b31

### Block 32

XML location: `/div[1]/div[1]/listBibl[1]/bibl[30]`.

```xml
<bibl xml:id="biblzh-tw_n30-31" xml:lang="zh-TW">電影《霸王別姬》，1993年。</bibl>
```

^b32

### Block 33

XML location: `/div[1]/div[1]/listBibl[1]/bibl[31]`.

```xml
<bibl xml:id="fr-ex-Beck_Morin" xml:lang="fr"><author>Beck, Béatrice</author>, <title>Léon
          Morin, prêtre</title>, <date>1952</date>.</bibl>
```

^b33

### Block 34

XML location: `/div[1]/div[1]/listBibl[1]/bibl[32]`.

```xml
<bibl xml:id="DRCAST-eg-16"><author>Beckett, Samuel</author>. <title level="m">Waiting for
          Godot</title>, <pubPlace>London</pubPlace>: <publisher>Faber and Faber</publisher>
          (<date>1956</date>).</bibl>
```

^b34

### Block 35

XML location: `/div[1]/div[1]/listBibl[1]/bibl[33]`.

```xml
<bibl xml:id="CO-eg-02"><author>Beckett, Samuel</author>. <title level="m">Murphy</title>
          (<date>1963</date>), chap 2. </bibl>
```

^b35

### Block 36

XML location: `/div[1]/div[1]/listBibl[1]/bibl[34]`.

```xml
<bibl xml:id="fr-ex-Becque-ee" xml:lang="fr"><author>Becque, Henry</author>, <title>La
          Parisienne</title>. <ref target="http://www.cnrtl.fr/corpus/frantext/frantext.php">Edition
          électronique</ref> par l'<editor>ATILF</editor> et le <editor>CNRTL</editor>, d'après
        l'édition de Fasquelle (Paris, 1922). </bibl>
```

^b36

### Block 37

XML location: `/div[1]/div[1]/listBibl[1]/bibl[35]`.

```xml
<bibl xml:id="github-mix-mix">
        <author>Bowers, Jack</author>
        <title>Mixtepec-Mixtec Project Personography</title>
        <ptr target="https://raw.githubusercontent.com/iljackb/Mixtepec_Mixtec/master/MIX-People.xml#element(JS/6)"/>
        <date type="accessed" when="2023-05-08"/>
      </bibl>
```

^b37

### Block 38

XML location: `/div[1]/div[1]/listBibl[1]/bibl[36]`.

```xml
<bibl xml:id="PH-eg-05">
        <author>Beerbohm, Max</author>. Autograph manuscript of <title>The Golden Drugget</title>,
        Pierpont Morgan MA 3391. in <ptr target="#KLINKENBORG"/> 123. </bibl>
```

^b38

### Block 39

XML location: `/div[1]/div[1]/listBibl[1]/bibl[37]`.

```xml
<bibl xml:id="DRPRO-eg-10"><author>Behn, Aphra</author>. <title level="m">The Rover</title>,
          (<date>1697</date>).</bibl>
```

^b39

### Block 40

XML location: `/div[1]/div[1]/listBibl[1]/bibl[38]`.

```xml
<bibl xml:id="divEGs">
        <author>Beeton, Isabella</author>. <title>The book of Household Management</title>,
          <pubPlace>London</pubPlace>: <publisher>S.O. Beeton</publisher>
        (<date>1861</date>).</bibl>
```

^b40

### Block 41

XML location: `/div[1]/div[1]/listBibl[1]/bibl[39]`.

```xml
<bibl xml:id="fr-ex-Belloc_Kepas" xml:lang="fr"><author>Belloc, Denis</author>,
          <title>Képas</title>, <date>1989</date>.</bibl>
```

^b41

### Block 42

XML location: `/div[1]/div[1]/listBibl[1]/bibl[40]`.

```xml
<bibl xml:id="fr-ex-Belloc_Neons" xml:lang="fr">
        <author>Belloc, Denis</author>, <title>Néons</title>, <date>1987</date>.</bibl>
```

^b42

### Block 43

XML location: `/div[1]/div[1]/listBibl[1]/bibl[41]`.

```xml
<bibl xml:id="bentham"><author>Bentham, Jeremy</author>. <title level="m">The Book of
          Fallacies.</title> (<date>1824</date>).</bibl>
```

^b43

### Block 44

XML location: `/div[1]/div[1]/listBibl[1]/bibl[42]`.

```xml
<bibl xml:id="TCAPLR-eg-11">
        <title>Beowulf and The fight at Finnsburg</title>; edited, with introduction, bibliography,
        notes, glossary, and appendices, by <editor>Fr. Klaeber</editor>. <pubPlace>Boston, New York
          [etc.] </pubPlace>
        <publisher>D.C. Heath &amp; Co.</publisher> (<date>1922</date>). </bibl>
```

^b44

### Block 45

XML location: `/div[1]/div[1]/listBibl[1]/bibl[43]`.

```xml
<bibl xml:id="fr-ex-Bibliog_Renaissance_Ital" xml:lang="fr">
        <title>Bibliographie dans le cadre de la semaine italienne du 11 au 18 mars 2006</title>, ,
          <ref target="http://www.mediatheque-rueilmalmaison.fr/musique_cinema_arts_et_loisirs/arts_les_dossiers/la_renaissance_italienne_article1154.html?artsuite=5">document électronique</ref>.</bibl>
```

^b45

### Block 46

XML location: `/div[1]/div[1]/listBibl[1]/bibl[44]`.

```xml
<bibl xml:id="fr-ex-BnF-Reliures" xml:lang="fr"><author>Bibliothèque nationale de
          France</author>, <title> Projet de description des reliures remarquables de la Réserve des
          livres rares selon le modèle de la TEI manuscrits</title>.</bibl>
```

^b46

### Block 47

XML location: `/div[1]/div[1]/listBibl[1]/bibl[45]`.

```xml
<bibl xml:id="fr-ex-Billetdoux" xml:lang="fr"><author>Billetdoux, Marie</author>, <title>Un
          peu de désir sinon je meurs</title>, <date>2006</date>.</bibl>
```

^b47

### Block 48

XML location: `/div[1]/div[1]/listBibl[1]/bibl[46]`.

```xml
<bibl xml:id="VE-eg-04">
        <author>Blake, William</author>. <title level="a">London</title>, in <title level="m">Songs
          of Experience</title> (<date>1791</date>). </bibl>
```

^b48

### Block 49

XML location: `/div[1]/div[1]/listBibl[1]/bibl[47]`.

```xml
<bibl xml:id="SG132-neg-1">
        <author>Blake, William</author>. <title level="a">The Sick Rose</title>, in <title level="m">Songs of Experience</title> (<date>1794</date>). </bibl>
```

^b49

### Block 50

XML location: `/div[1]/div[1]/listBibl[1]/bibl[48]`.

```xml
<bibl xml:id="en-blake-tyger">
        <author>Blake, William</author>. <title level="a">The Tyger</title>, in <title level="m">Songs of Experience</title> (<date>1794</date>). </bibl>
```

^b50

### Block 51

XML location: `/div[1]/div[1]/listBibl[1]/bibl[49]`.

```xml
<bibl xml:id="SASE-eg-33"><author>Bloomfield, Leonard</author>. <title level="a">Literate and
          Illiterate Speech</title>, <title level="j">American Speech</title>, <biblScope unit="issue">2</biblScope>, (<date>1927</date>), <biblScope unit="pp">pp.
          432-441</biblScope>.</bibl>
```

^b51

### Block 52

XML location: `/div[1]/div[1]/listBibl[1]/bibl[50]`.

```xml
<bibl xml:id="COLI-eg-171"><author>Borges, Jorge Luis</author>, tr. <editor role="tr">R.
          Simms</editor>. <title level="a">The Analytical Language of John Wilkins</title>. In
          <editor>Emir Rodriguez Monegal</editor> and <editor>Alistair Reid</editor>, eds. <title level="m">Borges: A reader</title>, <publisher>Dutton Adult</publisher>
        (<date>1981</date>), <biblScope unit="pp">p.141</biblScope>.</bibl>
```

^b52

### Block 53

XML location: `/div[1]/div[1]/listBibl[1]/bibl[51]`.

```xml
<bibl xml:id="FTFOR-eg-10"><author>Borges, Jorge Luis</author>. <title level="a">Avatars of
          the Tortoise</title> In <editor role="tr">James E. Irby</editor> tr. <title level="m">Labyrinths: Selected Stories and Other Writings</title>, <pubPlace>New York</pubPlace>:
          <publisher>New Directions</publisher>, (<date>1962</date>), <biblScope unit="pp">pp.202-203</biblScope>.</bibl>
```

^b53

### Block 54

XML location: `/div[1]/div[1]/listBibl[1]/bibl[52]`.

```xml
<bibl xml:id="fr-ex-Bouiller_Rapport" xml:lang="fr"><author>Bouillier, Grégoire</author>,
          <title>Rapport sur moi</title>, <date> 2002</date>.</bibl>
```

^b54

### Block 55

XML location: `/div[1]/div[1]/listBibl[1]/bibl[53]`.

```xml
<bibl xml:id="fr-ex-Mouchette" xml:lang="fr"><author>Bresson, Robert</author>, <title level="a">Mouchette : script</title>, <title level="j">l'Avant-scène cinéma</title>,
          <num>n° 80</num>, <date>avril 1968</date>.</bibl>
```

^b55

### Block 56

XML location: `/div[1]/div[1]/listBibl[1]/bibl[54]`.

```xml
<bibl xml:id="SA-eg-02"> Extract from <title>British National Corpus</title> (<ptr target="http://www.natcorp.ox.ac.uk"/>) Text KB7, sentence 13730.</bibl>
```

^b56

### Block 57

XML location: `/div[1]/div[1]/listBibl[1]/bibl[55]`.

```xml
<bibl xml:id="COPA-eg-1">
        <author>Brontë, Charlotte</author>. <title level="m">Jane Eyre: An Autobiography</title>,
          <edition>Third edition; reprint</edition><pubPlace>London</pubPlace>
        <publisher>Service &amp; Paton</publisher>, <date>1897</date>; <publisher>Project
          Gutenberg</publisher>, <date>1 December 2020</date>. <biblScope unit="chap">chapter
          XII</biblScope>. <ptr target="https://www.gutenberg.org/files/1260/1260-h/1260-h.htm"/>
      </bibl>
```

^b57

### Block 58

XML location: `/div[1]/div[1]/listBibl[1]/bibl[56]`.

```xml
<bibl xml:id="PH-eg-15">
        <author>Browning, Robert</author>. <title>Letter to George Moulton-Barrett</title>, Pierpont
        Morgan MA 310, (<ptr target="#KLINKENBORG"/> 23). </bibl>
```

^b58

### Block 59

XML location: `/div[1]/div[1]/listBibl[1]/bibl[57]`.

```xml
<bibl xml:id="fr-ex-Belloy" xml:lang="fr"><author>Buirette de Belloy, Pierre Laurent</author>,
          <title level="m">Gabrielle de Vergy</title>, <date>1777</date>.</bibl>
```

^b59

### Block 60

XML location: `/div[1]/div[1]/listBibl[1]/bibl[58]`.

```xml
<bibl xml:id="DS-eg-06">
        <author>Bunyan, John</author>. <title>The Pilgrim's Progress from this world to that which
          is to come...</title>, <pubPlace>London</pubPlace> (<date>1678</date>). </bibl>
```

^b60

### Block 61

XML location: `/div[1]/div[1]/listBibl[1]/bibl[59]`.

```xml
<bibl xml:id="STGA-eg-4"><author>Burgess, Anthony</author>. <title level="m">A Clockwork
          Orange</title>. (<date>1962</date>), <biblScope unit="part">opening</biblScope>.</bibl>
```

^b61

### Block 62

XML location: `/div[1]/div[1]/listBibl[1]/bibl[60]`.

```xml
<bibl xml:id="usenet-sgml-tei"><title level="a">
        <ref target="https://www.usenetarchives.com/view.php?id=comp.text.sgml&amp;mid=PDI5MzIxLjkwMDkzMDEzMzBAbWFudXRpdXMuZWNzLnNvdG9uLmFjLnVrPg">Burnard SGML reading list</ref></title>, 
        <title level="m">COMP.TEXT.SGML</title>, <date from="1990-09-30" to="1990-10-11">September 30 to October 11, 1990</date> in <title level="m">Usenet Archives</title>
        (<publisher>UsenetArchives.com</publisher>, <date>2024</date>).
      </bibl>
```

^b62

### Block 63

XML location: `/div[1]/div[1]/listBibl[1]/bibl[61]`.

```xml
<bibl xml:id="Burnard-db"><author>Burnard, Lou</author>. <title level="a">Principles of
          Database Design</title> in <editor>S. Rahtz.</editor> ed. <title level="m">Information
          Technology in the Humanities: tools, techniques and applications</title>, <publisher>Ellis
          Horwood Ltd</publisher>, <series>Ellis Horwood Series in Computers and Their
          Applications</series>, (<date>1987</date>), <biblScope unit="pp">p. 54</biblScope>.</bibl>
```

^b63

### Block 64

XML location: `/div[1]/div[1]/listBibl[1]/bibl[62]`.

```xml
<bibl xml:id="fr-ex-TEI-simpl" xml:lang="fr"><author>Burnard, Lou</author>,
          <author>Sperberg-McQueen, C. M.</author>, <title>
          <ref target="http://www.gutenberg.eu.org/publications/autres/TEILITE/">La TEI simplifiée,
            une introduction au codage des textes électroniques en vue de leur échange — version de
            travail </ref>
        </title>, <date>1996</date>.</bibl>
```

^b64

### Block 65

XML location: `/div[1]/div[1]/listBibl[1]/bibl[63]`.

```xml
<bibl xml:id="COXR-eg-164">
        <author>Burton, Robert</author>. <title level="m">Anatomy of Melancholy</title>
          (<date>1621</date>), <edition>16th ed.</edition> reprinted <date>1846</date>, <biblScope unit="pp">p. 743</biblScope>.</bibl>
```

^b65

### Block 66

XML location: `/div[1]/div[1]/listBibl[1]/bibl[64]`.

```xml
<bibl xml:id="COLI-eg-172"><author>Butler, Samuel</author>. <title level="m">The Way of All
          Flesh</title> (<date>1903</date>), <biblScope unit="chap">chapter 37</biblScope>.</bibl>
```

^b66

### Block 67

XML location: `/div[1]/div[1]/listBibl[1]/bibl[65]`.

```xml
<bibl xml:id="VESTR-eg-5"><author>Byron, George Gordon</author>. <title>Don Juan</title>
          (<date>1819</date>), <biblScope unit="part">I.xxii</biblScope>.</bibl>
```

^b67

### Block 68

XML location: `/div[1]/div[1]/listBibl[1]/bibl[66]`.

```xml
<bibl xml:id="VEST-eg-5"><author>Byron, George Gordon</author>. <title level="a">Vision of
          Judgment</title> In <editor>E.H. Coleridge</editor> ed. <title level="m">The Poetical
          Works of Lord Byron</title>, <biblScope unit="part">viii</biblScope>, 1922.</bibl>
```

^b68

### Block 69

XML location: `/div[1]/div[1]/listBibl[1]/bibl[67]`.

```xml
<bibl xml:id="NDPER-eg-17"><title level="m">C 60/16 Fine Roll 6 HENRY III (28 October 1221-27
          October 1222)</title>, <biblScope unit="part">membrane 5, entry 154</biblScope>.</bibl>
```

^b69

### Block 70

XML location: `/div[1]/div[1]/listBibl[1]/bibl[68]`.

```xml
<bibl xml:id="biblzh-tw_n46" xml:lang="zh-TW">CBETA</bibl>
```

^b70

### Block 71

XML location: `/div[1]/div[1]/listBibl[1]/bibl[69]`.

```xml
<bibl xml:id="caedmon"><title>Cædmon's Hymn</title> in Bede's Historia Ecclesiastica (MS Kk.
        5. 16, Cambridge, University Library).</bibl>
```

^b71

### Block 72

XML location: `/div[1]/div[1]/listBibl[1]/bibl[70]`.

```xml
<bibl xml:id="MasCab">
        <title>Cabaret</title>. A musical play, with book by Joe Masteroff, lyrics by Fred Ebb, and
        music by John Kaner. Based on the play by John van Druten and stories by Christopher
        Isherwood. <date>1966</date></bibl>
```

^b72

### Block 73

XML location: `/div[1]/div[1]/listBibl[1]/bibl[71]`.

```xml
<bibl xml:id="COEDREG-eg-74">Edward Barkley, describing how Essex drove the Irish from the
        plains into the woods to freeze or famish in winter; quoted by <author>Canny, Nicholas
          P.</author>
        <title level="a">The Ideology of English Colonization: From Ireland to America</title>. In
          <editor>Stanley N. Katz</editor> and <editor>John M. Murrin</editor> eds. <title level="m">Colonial America: Essays in Politics and Social Development</title>, <edition>3d
          ed</edition>
        <pubPlace>New York</pubPlace>: <publisher>Knopf</publisher>, (<date>1983</date>), <biblScope unit="pp">p.53</biblScope>. <!--<note>Canny's footnote reads<quote
            rend="inline">See Devereux, <title level="m">Lives of
            Devereux</title>, I, 30-31, for Essex to Burghley, July 20, 1573, and
            ibid, 37-39, for Essex to Privy Council, Sept. 29, 1573. Barkley to
            Burghley, May 14, 1574, S.p.63/46, no. 15, P.R.O.</quote> </note>-->
      </bibl>
```

^b73

### Block 74

XML location: `/div[1]/div[1]/listBibl[1]/bibl[72]`.

```xml
<bibl xml:id="AI-BIBL-3">
        <author>Carroll, Lewis</author>. <title level="m">Through the Looking Glass, and what Alice
          found there</title>. (<date>1871</date>). </bibl>
```

^b74

### Block 75

XML location: `/div[1]/div[1]/listBibl[1]/bibl[73]`.

```xml
<bibl xml:id="fr-ex-catechisme" xml:lang="fr"><title>Catéchisme de l'Eglise
        catholique</title>, <date>1968</date>.</bibl>
```

^b75

### Block 76

XML location: `/div[1]/div[1]/listBibl[1]/bibl[74]`.

```xml
<bibl xml:id="VESA-eg-1">
        <author>Cavendish, Margaret</author>. <title level="a">Nature's Pictures</title>.
          <pubPlace>London</pubPlace>, <date>1656</date>. <publisher>Women Writers Online. Women
          Writers Project, Northeastern University</publisher>. <date>29 Mar.
        2015</date><!--  <ref target="https://www.wwp.northeastern.edu/texts/cavendish.natpix.html"
            >https://www.wwp.northeastern.edu/texts/cavendish.natpix.html</ref>
             temporarily removed until #1564 is resolved, i.e. WWP puts this somewhere that is not
             behind paywall. -->.</bibl>
```

^b76

### Block 77

XML location: `/div[1]/div[1]/listBibl[1]/bibl[75]`.

```xml
<bibl xml:id="fr-ex-TLFI" xml:lang="fr"><author>Centre national de la recherche scientifique
          (France). UMR 7118 ATILF</author>, <title><ref target="http://atilf.atilf.fr/tlf.htm">Le
            Trésor de la Langue Française Informatisé (TLFI)</ref></title>,
        <date>2004</date>.</bibl>
```

^b77

### Block 78

XML location: `/div[1]/div[1]/listBibl[1]/bibl[76]`.

```xml
<bibl xml:id="TSBAPA-eg-24"> Example recoded from <author>Chafe, W. </author>
        <title level="a">Adequacy, user-friendliness, and practicality in transcribing</title> In
          <editor>Leech, G.</editor>, <editor>G. Myers</editor>, <editor>J. Thomas</editor> eds.
          <title level="m">Spoken English on Computer: Transcription, Markup and
          Applications</title>. <pubPlace>Harlow</pubPlace>: <publisher>Longman</publisher>,
          <date>1995</date>.</bibl>
```

^b78

### Block 79

XML location: `/div[1]/div[1]/listBibl[1]/bibl[77]`.

```xml
<bibl xml:id="CORS5-eg-01">
        <author>Chandler, Lloyd.</author>
        <title level="a">Conversation with Death</title> (also known as <title level="a">Oh,
          Death</title>). In <title level="j">Journal of Folklore Research</title>, <biblScope unit="issue">41.2/3</biblScope>, (<date>2004</date>), <biblScope unit="pp">pp.
          125-126</biblScope>. </bibl>
```

^b79

### Block 80

XML location: `/div[1]/div[1]/listBibl[1]/bibl[78]`.

```xml
<bibl xml:id="Python"><author>Chapman, Graham</author>, <author>Cleese, John</author>,
          <author>Gilliam, Terry</author>, <author>Idle, Eric</author>, <author>Jones,
          Terry</author>. <title>The complete Monty Pythons Flying Circus</title>. </bibl>
```

^b80

### Block 81

XML location: `/div[1]/div[1]/listBibl[1]/bibl[79]`.

```xml
<bibl xml:id="pythonBrian"><author>Chapman, Graham</author>, <author>Cleese, John</author>,
          <author>Gilliam, Terry</author>, <author>Idle, Eric</author>, <author>Jones,
          Terry</author>. <title>Monty Python's Life of Brian</title> (<date>1979</date>).
        <!-- <ref target="www.youtube.com/watch?v=-xLUEMj6cwA"/>--></bibl>
```

^b81

### Block 82

XML location: `/div[1]/div[1]/listBibl[1]/bibl[80]`.

```xml
<bibl xml:id="PH-eg-11">
        <author>Chaucer, Geoffrey</author>. <title>Canterbury Tales</title>, f52r, in Holkham MS. </bibl>
```

^b82

### Block 83

XML location: `/div[1]/div[1]/listBibl[1]/bibl[81]`.

```xml
<bibl xml:id="VEST-eg-4">
        <author>Chaucer, Geoffrey</author>. <title level="a">The Tale of Sir Topas</title>, <title level="m">The Canterbury Tales</title>, In <editor>F. N. Robinson</editor> ed. <title level="m">The Works of Geoffrey Chaucer</title>, <edition>2nd edition</edition>
        <pubPlace>Boston</pubPlace>: <publisher>Houghton Mifflin Co.</publisher>,
        <date>1957</date>.</bibl>
```

^b83

### Block 84

XML location: `/div[1]/div[1]/listBibl[1]/bibl[82]`.

```xml
<bibl xml:id="biblzh-tw_n50" xml:lang="zh-TW">陳政彥，〈戰後臺灣現代詩論戰史研究〉，2007。</bibl>
```

^b84

### Block 85

XML location: `/div[1]/div[1]/listBibl[1]/bibl[83]`.

```xml
<bibl xml:id="CholNup">
        <author>Cholières, Nicolas de</author>, <title>La Forest Nuptiale</title>
        (<date>1600</date>). </bibl>
```

^b85

### Block 86

XML location: `/div[1]/div[1]/listBibl[1]/bibl[84]`.

```xml
<bibl xml:id="FS-eg-01">
        <author>Chomsky, Noam</author> and <author>Morris Halle</author>. <title>The Sound Pattern
          of English</title>. New York: Harper &amp; Row (<date>1968</date>), <biblScope unit="pp">p. 415</biblScope>. </bibl>
```

^b86

### Block 87

XML location: `/div[1]/div[1]/listBibl[1]/bibl[85]`.

```xml
<bibl xml:id="fr-ex-simjar" xml:lang="fr"><author>Claude Simon</author>
        <title>Le jardin des plantes</title>, <date>1997</date>, p 284</bibl>
```

^b87

### Block 88

XML location: `/div[1]/div[1]/listBibl[1]/bibl[86]`.

```xml
<bibl xml:id="AI-BIBL-1">
        <author>Cleaver, Eldridge</author>. <title level="m">Soul on Ice</title>. <pubPlace>New
          York</pubPlace> (<date>1968</date>). </bibl>
```

^b88

### Block 89

XML location: `/div[1]/div[1]/listBibl[1]/bibl[87]`.

```xml
<bibl xml:id="DSFRONT-eg-69">
        <title level="a">Cloud of Unknowing</title> In <editor>Hodgson, Phyllis</editor> ed. <title level="m">The Cloud of Unknowing and The Book of Privy Counselling</title>,
          <pubPlace>London</pubPlace>: <publisher>Oxford University Press</publisher>, <series>Early
          English Text Society</series>, <biblScope unit="vol">218</biblScope>, (<date>1944</date>). </bibl>
```

^b89

### Block 90

XML location: `/div[1]/div[1]/listBibl[1]/bibl[88]`.

```xml
<bibl xml:id="NDPER-eg-18"><author>Clover, Carol J.</author><title level="m">The Medieval
          Saga</title>, <pubPlace>Ithaca</pubPlace>: <publisher>Cornell University Press</publisher>
          (<date>1982</date>). </bibl>
```

^b90

### Block 91

XML location: `/div[1]/div[1]/listBibl[1]/bibl[89]`.

```xml
<bibl xml:id="DRPERF-eg-13">
        <author>Cocteau, Jean</author>. <title level="m">La Machine Infernale</title>.</bibl>
```

^b91

### Block 92

XML location: `/div[1]/div[1]/listBibl[1]/bibl[90]`.

```xml
<bibl xml:id="CONONO-eg-189"><author>Coleridge, Samuel Taylor</author>. <title level="m">The
          Rime of the Ancient Mariner</title>. In <author>Wordsworth, William</author> and
          <author>Samuel Taylor Coleridge</author>. <title level="m">Lyrical Ballads</title>
          (<date>1798</date>). </bibl>
```

^b92

### Block 93

XML location: `/div[1]/div[1]/listBibl[1]/bibl[91]`.

```xml
<bibl xml:id="VEST-eg-3"><author>Coleridge, Samuel Taylor</author>. <title level="a">Frost at
          Midnight</title> In <editor>E.H. Coleridge</editor> ed. <title level="m">Poetical
          Works</title>, <pubPlace>Oxford</pubPlace>: <publisher>Oxford University
        Press</publisher>, (<date>1967</date>), <biblScope unit="pp">p.240</biblScope>.</bibl>
```

^b93

### Block 94

XML location: `/div[1]/div[1]/listBibl[1]/bibl[92]`.

```xml
<bibl xml:id="fr-ex-Colette-Ecole" xml:lang="fr"><author>Colette</author>, <title>Colette à
          l'école</title>, <date>1900</date>.</bibl>
```

^b94

### Block 95

XML location: `/div[1]/div[1]/listBibl[1]/bibl[93]`.

```xml
<bibl xml:id="DIC-CED">
        <title>Collins English Dictionary</title>, <edition>12th edition</edition>
        <pubPlace>Glasgow</pubPlace>: <publisher>Collins</publisher> (<date when="2014">2014</date>). </bibl>
```

^b95

### Block 96

XML location: `/div[1]/div[1]/listBibl[1]/bibl[94]`.

```xml
<bibl xml:id="DIC-CP">
        <title>Collins Pocket Dictionary of the English language</title>.
          <pubPlace>London</pubPlace>: <publisher>Collins</publisher>. </bibl>
```

^b96

### Block 97

XML location: `/div[1]/div[1]/listBibl[1]/bibl[95]`.

```xml
<bibl xml:id="DSOC-eg-34">
        <author>Collins, Wilkie</author>. <title level="m">The Moonstone</title>,
          <publisher>Penguin</publisher>, <biblScope unit="part">6th narrative</biblScope>.</bibl>
```

^b97

### Block 98

XML location: `/div[1]/div[1]/listBibl[1]/bibl[96]`.

```xml
<bibl xml:id="SA-BIBL-2">
        <author>Comenius, John Amos</author>. <title level="m">Orbis Pictus: a facsimile of the
          first English edition of 1659</title> (ed. <editor><forename>John</forename>
          <forename>E.</forename>
          <surname>Sadler</surname>
        </editor>) <publisher>Oxford University Press</publisher> (<date>1968</date>). </bibl>
```

^b98

### Block 99

XML location: `/div[1]/div[1]/listBibl[1]/bibl[97]`.

```xml
<bibl xml:id="NDORG-eg-34"><author>Cope, Thomas Pym</author>. <title level="m">Philadelphia
          merchant: the diary of Thomas P. Cope, 1800-1851</title>, <editor>Eliza Cope
          Harrison</editor> ed.</bibl>
```

^b99

### Block 100

XML location: `/div[1]/div[1]/listBibl[1]/bibl[98]`.

```xml
<bibl xml:id="fr-ex-Corneille_Place-Royale" xml:lang="fr"><author>Corneille, Pierre</author>,
          <title>La Place Royale ou L'Amoureux extravagant</title>, <date>1637</date>.</bibl>
```

^b100

### Block 101

XML location: `/div[1]/div[1]/listBibl[1]/bibl[99]`.

```xml
<bibl xml:id="fr-ex-Corneille_Theodore" xml:lang="fr"><author>Corneille, Pierre</author>,
          <title>Théodore, vierge et martyre : tragédie chrétienne</title>,
        <title>1646</title>.</bibl>
```

^b101

### Block 102

XML location: `/div[1]/div[1]/listBibl[1]/bibl[100]`.

```xml
<bibl xml:id="RESPONS-eg-02">
        <author>Cowley, Hannah</author>. <title level="m">The Runaway</title> (<date when="1813">1813</date>). </bibl>
```

^b102

### Block 103

XML location: `/div[1]/div[1]/listBibl[1]/bibl[101]`.

```xml
<bibl xml:id="DS-eg-02">
        <author>Crashaw, Richard</author>, ed. <editor>J.R. Tutin</editor>. <title level="m">The
          Poems of Richard Crashaw</title>. <edition>Muses Library Edition</edition>:
          (<date>1900</date>). </bibl>
```

^b103

### Block 104

XML location: `/div[1]/div[1]/listBibl[1]/bibl[102]`.

```xml
<bibl xml:id="CREELEY">
        <author>Creeley, Robert</author>
        <title>A counterpoint</title> in <title>For Love: Poems 1950-1960</title>
        (<date>1962</date>). </bibl>
```

^b104

### Block 105

XML location: `/div[1]/div[1]/listBibl[1]/bibl[103]`.

```xml
<bibl xml:id="biblzh-tw_n17" xml:lang="zh-TW">崔西．雪佛蘭。《戴珍珠耳環的少女》。台北：皇冠，2003。</bibl>
```

^b105

### Block 106

XML location: `/div[1]/div[1]/listBibl[1]/bibl[104]`.

```xml
<bibl xml:id="CONARS-eg-109"><author>Dallas, George Mifflin</author>. <title>Unpublished
          letter</title> cited in <editor>Russell F. Weigley</editor>, <editor>Nicholas B.
          Wainwright</editor>, <editor>Edwin Wolf</editor> eds. <title level="m">Philadelphia: A 300
          Year History</title>, <pubPlace>New York</pubPlace> and <pubPlace>London</pubPlace>:
          <publisher>W. W. Norton &amp; Company</publisher>, <date>1982</date>, <biblScope unit="pp">p. 349</biblScope>.</bibl>
```

^b106

### Block 107

XML location: `/div[1]/div[1]/listBibl[1]/bibl[105]`.

```xml
<bibl xml:id="fr-ex-Danhauser" xml:lang="fr"><author>Danhauser, Adolphe-Leopold</author>,
          <title>Théorie de la musique</title>, <date>1872</date>.</bibl>
```

^b107

### Block 108

XML location: `/div[1]/div[1]/listBibl[1]/bibl[106]`.

```xml
<bibl xml:id="beagle">
        <author>Darwin, Charles</author>. <title>Narrative of the Surveying Voyages of His Majesty's
          ships Adventure and Beagle... volume 3 : Journal and Remarks (The Voyage of the
          Beagle)</title>, chap 3. <date>1839</date>. </bibl>
```

^b108

### Block 109

XML location: `/div[1]/div[1]/listBibl[1]/bibl[107]`.

```xml
<bibl xml:id="fr-ex-Daudet_lundi" xml:lang="fr"><author>Daudet, Alphonse</author>, <title>Les
          contes du lundi</title>, <date>1873</date>. </bibl>
```

^b109

### Block 110

XML location: `/div[1]/div[1]/listBibl[1]/bibl[108]`.

```xml
<bibl xml:id="WD-TWac">
        <author>Davenant, William</author>. <title level="m">The vvitts. A comedie, presented at the
          private house in Blacke Fryers, by his Majesties servants. The author VVilliam D'avenant,
          servant to Her Majestie.</title>
        <pubPlace>London</pubPlace>, <date>1636</date>. [STC S109311]</bibl>
```

^b110

### Block 111

XML location: `/div[1]/div[1]/listBibl[1]/bibl[109]`.

```xml
<bibl xml:id="PH-eg-02">
        <title>De Nutrimento et Nutribili, Tractatus 1</title>, fol 217r col b of Merton College
        Oxford MS O.2.1; in <ptr target="#PARKES"/> pl. 16.</bibl>
```

^b111

### Block 112

XML location: `/div[1]/div[1]/listBibl[1]/bibl[110]`.

```xml
<bibl xml:id="PH-eg-12">
        <title>Dean of Sarum Churchwardens' presentments</title>, 1731, Hurst; Wiltshire Record
        Office; transcribed by Donald A. Spaeth. </bibl>
```

^b112

### Block 113

XML location: `/div[1]/div[1]/listBibl[1]/bibl[111]`.

```xml
<bibl xml:id="defoeMoll"><author>Defoe, Daniel</author>. <title level="m">The Fortunes and
          Misfortunes of the Famous Moll Flanders</title> (<date>1722</date>).</bibl>
```

^b113

### Block 114

XML location: `/div[1]/div[1]/listBibl[1]/bibl[112]`.

```xml
<bibl xml:id="COLI-eg-176"><author>Defoe, Daniel</author>. <title level="m">Robinson
          Crusoe</title> (<date>1719</date>).</bibl>
```

^b114

### Block 115

XML location: `/div[1]/div[1]/listBibl[1]/bibl[113]`.

```xml
<bibl xml:id="AI-BIBL-2">
        <author>Defoe, Daniel</author>. <title level="m">Journal of the Plague Year</title>.
          <pubPlace>London</pubPlace> (<date>1722</date>). </bibl>
```

^b115

### Block 116

XML location: `/div[1]/div[1]/listBibl[1]/bibl[114]`.

```xml
<bibl xml:id="DR-eg-04">
        <author>Dekker, Thomas</author> and <author>Thomas Middleton</author>. <title>The Honest
          Whore, Part One</title> (<date>1604</date>). </bibl>
```

^b116

### Block 117

XML location: `/div[1]/div[1]/listBibl[1]/bibl[115]`.

```xml
<bibl xml:id="deloneyThom"><author>Deloney, Thomas</author>. <title>Thomas of Reading or the
          Sixe Worthie Yeomen of the West</title> (<date>1612</date>).</bibl>
```

^b117

### Block 118

XML location: `/div[1]/div[1]/listBibl[1]/bibl[116]`.

```xml
<bibl xml:id="fr-ex-Dennery-notations" xml:lang="fr"><author>Dennery, Annie</author>. <title level="a">Du mélos à la note : Les notations musicales au Moyen Age</title>, <title level="j">Médiévales</title>, <num>n° 3</num>
        <date>1983</date>.</bibl>
```

^b118

### Block 119

XML location: `/div[1]/div[1]/listBibl[1]/bibl[117]`.

```xml
<bibl xml:id="COHQHE-eg-14"><author>Dickens, Charles</author>. <title level="m">A Christmas
          Carol in Prose, Being a Ghost Story of Christmas</title>, <publisher>Chapman and
          Hall</publisher>, (<date>1843</date>), <biblScope unit="pp">p. 5, p.
        12</biblScope>.</bibl>
```

^b119

### Block 120

XML location: `/div[1]/div[1]/listBibl[1]/bibl[118]`.

```xml
<bibl xml:id="CONARS-eg-103"><author>Dickens, Charles</author>. <title level="m">Little
          Dorrit</title>, (<date>1857</date>).</bibl>
```

^b120

### Block 121

XML location: `/div[1]/div[1]/listBibl[1]/bibl[119]`.

```xml
<bibl xml:id="VEST-eg-1"><author>Dickinson, Emily</author>. <title level="a">1755</title> In
          <editor>Arthur Eastman</editor> et al. eds. <title level="m">The Norton Anthology of
          Poetry</title>, <pubPlace>New York</pubPlace>: <publisher>W.W. Norton</publisher>,
          <date>1970</date>, <biblScope unit="part">p.859</biblScope>.</bibl>
```

^b121

### Block 122

XML location: `/div[1]/div[1]/listBibl[1]/bibl[120]`.

```xml
<bibl xml:id="fr-ex-Diderot-Corresp_SV" xml:lang="fr"><author>Diderot, Denis</author>,
          <title>Lettres à Sophie Volland</title>, <date>26 sept. 1762</date>.</bibl>
```

^b122

### Block 123

XML location: `/div[1]/div[1]/listBibl[1]/bibl[121]`.

```xml
<bibl xml:id="biblzh-tw_n40" xml:lang="zh-TW"> 〈第三屆第一次大會第一次會議記錄〉，臺灣省諮議會。</bibl>
```

^b123

### Block 124

XML location: `/div[1]/div[1]/listBibl[1]/bibl[122]`.

```xml
<bibl xml:id="DSOC-eg-33"><author>Disraeli, Benjamin</author>. <title level="m">Coningsby</title> (<date>1844</date>), <biblScope unit="part">preface</biblScope>.</bibl>
```

^b124

### Block 125

XML location: `/div[1]/div[1]/listBibl[1]/bibl[123]`.

```xml
<bibl xml:id="COHQQ-eg-26"><author>Doyle, Arthur Conan</author>. <title level="a">The
          Red-headed league</title>. In <title level="m">The Adventures of Sherlock Holmes</title>
          (<date>1892</date>).</bibl>
```

^b125

### Block 126

XML location: `/div[1]/div[1]/listBibl[1]/bibl[124]`.

```xml
<bibl xml:id="DSGRP-eg-57">
        <author>Doyle, Arthur Conan</author>. <title level="m">The Original Illustrated Sherlock
          Holmes</title>, <publisher>Castle Books</publisher>, <date>1989</date>.</bibl>
```

^b126

### Block 127

XML location: `/div[1]/div[1]/listBibl[1]/bibl[125]`.

```xml
<bibl xml:id="WD-BOUS"><title>Drawing of a leaden plaque bearing an inquiry by Hermon from the
          oracular precinct at Dodona</title>. Catalogue no 725; LSAG 230.13. Image from <ptr target="http://poinikastas.csad.ox.ac.uk/"/></bibl>
```

^b127

### Block 128

XML location: `/div[1]/div[1]/listBibl[1]/bibl[126]`.

```xml
<bibl xml:id="fr-ex-Babel" xml:lang="fr"><author>Dubois, Jacques</author>, <author>Nyssen,
          Hubert</author> (dir. de collection), <title>Babel</title>, <publisher>Actes
          sud</publisher>,<date>1989-...</date>.</bibl>
```

^b128

### Block 129

XML location: `/div[1]/div[1]/listBibl[1]/bibl[127]`.

```xml
<bibl xml:id="fr-ex-Dubois_Dict_Ling" xml:lang="fr"><author>Dubois, Jean</author>,
          <title>Dictionnaire de linguistique</title>, <date>1974</date>.</bibl>
```

^b129

### Block 130

XML location: `/div[1]/div[1]/listBibl[1]/bibl[128]`.

```xml
<bibl xml:id="PH-eg-04">
        <author>Dudo of St Quentin</author>. <title>De moribus et actis primorum Normannie
          ducum</title>, fol 4v of British Library MS Harley 3742; in <ptr target="#PARKES"/> pl
        6(i). </bibl>
```

^b130

### Block 131

XML location: `/div[1]/div[1]/listBibl[1]/bibl[129]`.

```xml
<bibl xml:id="fr-ex-Dufournaud" xml:lang="fr"><author>Dufournaud, Nicole</author>,
          <title>Numérisation des Titres de famille</title>, <ref target="http://nicole.dufournaud.net/these/adla/titresfamille/lebastard/2E3002/2E3002-0001.tei">édition électronique</ref>, <date>2002</date>. </bibl>
```

^b131

### Block 132

XML location: `/div[1]/div[1]/listBibl[1]/bibl[130]`.

```xml
<bibl xml:id="fr-ex-Duhamel-Pasquier" xml:lang="fr"><author>Duhamel, Georges</author>,
          <title>Chronique des Pasquier</title>, <date>1933-1945</date>.</bibl>
```

^b132

### Block 133

XML location: `/div[1]/div[1]/listBibl[1]/bibl[131]`.

```xml
<bibl xml:id="eg-rhyme-dutt">
        <author>Dutt, Toru</author>. <title level="a">Lakshman</title> In <title level="m">Ancient
          Ballads and Legends of Hindustan</title>, <publisher>Kegan Paul, Trench &amp;
          Co.</publisher>, (<date>1882</date>) </bibl>
```

^b133

### Block 134

XML location: `/div[1]/div[1]/listBibl[1]/bibl[132]`.

```xml
<bibl xml:id="VERH-eg-25"><author>Dylan, Bob</author>. <title level="a">All Along the
          Watchtower</title> In <title level="m">John Wesley Harding</title>
        (<date>1967</date>).</bibl>
```

^b134

### Block 135

XML location: `/div[1]/div[1]/listBibl[1]/bibl[133]`.

```xml
<bibl xml:id="pos4st"><author>Dylan, Bob</author>. <title level="a">Positively 4th
          Street</title> In <title level="m">Highway 61 Revisited</title>
        (<date>1965</date>).</bibl>
```

^b135

### Block 136

XML location: `/div[1]/div[1]/listBibl[1]/bibl[134]`.

```xml
<bibl xml:id="PH-eg-08">
        <title>Eddic poems</title>, in Reykjavík, Landsbókasafn Íslands, Lbs 1562 4to. </bibl>
```

^b136

### Block 137

XML location: `/div[1]/div[1]/listBibl[1]/bibl[135]`.

```xml
<bibl xml:id="CONAAB-eg-151"><title level="a">Editorial</title>, <title level="j">.EXE
          magazine</title>, <biblScope unit="issue">6.11 </biblScope> (<date>1992</date>),
          <biblScope unit="pp">p. 2</biblScope>.</bibl>
```

^b137

### Block 138

XML location: `/div[1]/div[1]/listBibl[1]/bibl[136]`.

```xml
<bibl xml:id="COHQQ-eg-28"><author>Eliot, George</author>. <title level="m">Middlemarch</title> (<date>1871</date>), <biblScope unit="chap"> I.1</biblScope>.</bibl>
```

^b138

### Block 139

XML location: `/div[1]/div[1]/listBibl[1]/bibl[137]`.

```xml
<bibl xml:id="SAID-DIRECT-eg-1">
        <author>Eliot, George</author>. <title level="m">Middlemarch</title> (<date>1871</date>),
          <biblScope unit="chap">I.XXI</biblScope>. </bibl>
```

^b139

### Block 140

XML location: `/div[1]/div[1]/listBibl[1]/bibl[138]`.

```xml
<bibl xml:id="DSAE-eg-38">
        <author>Eliot, George</author>. <title level="m">Daniel Deronda</title> (<date>1876</date>),
          <biblScope unit="chap">III.1</biblScope>.</bibl>
```

^b140

### Block 141

XML location: `/div[1]/div[1]/listBibl[1]/bibl[139]`.

```xml
<bibl xml:id="COEDADD-eg-89"><author>Eliot, Thomas Stearns</author>. <title level="m">The
          waste land: a facsimile and transcript of the original drafts including the annotations of
          Ezra Pound</title>, <editor>Eliot, Valerie</editor> ed. <publisher>Faber and Faber
          Ltd.</publisher> (<date>1971</date>), <biblScope unit="pp">p. 37</biblScope>.</bibl>
```

^b141

### Block 142

XML location: `/div[1]/div[1]/listBibl[1]/bibl[140]`.

```xml
<bibl xml:id="SVG-11">
        <title level="m">Scalable Vector Graphics (SVG) 1.1 (Second Edition)</title>. Editors
          <editor>Erik Dahlström</editor>, <editor>Jon Ferraiolo</editor>, <editor><seg xml:lang="ja">藤沢 淳</seg></editor>, <editor>Anthony Grasso</editor>, <editor>Dean
          Jackson</editor>, <editor>Chris Lilley</editor>, <editor>Cameron McCormack</editor>
        <editor>Doug Schepers</editor>, <editor>Jonathan Watt</editor> and <editor>Patrick
          Dengler</editor>. <publisher>World Wide Web Consortium (W3C)</publisher> (<date>22 June
          2010</date>). Available from <ptr target="https://www.w3.org/TR/SVG11/"/>. </bibl>
```

^b142

### Block 143

XML location: `/div[1]/div[1]/listBibl[1]/bibl[141]`.

```xml
<bibl xml:id="fr-ex-Ernaux-perdre" xml:lang="fr"><author>Ernaux, Annie</author>, <title>Se
          perdre</title>, <date>1988</date>.</bibl>
```

^b143

### Block 144

XML location: `/div[1]/div[1]/listBibl[1]/bibl[142]`.

```xml
<bibl xml:id="fr-ex-Ernaux-photo" xml:lang="fr"><author>Ernaux, Annie</author>, <title>L'usage
          de la photo</title>, <date>2005</date>.</bibl>
```

^b144

### Block 145

XML location: `/div[1]/div[1]/listBibl[1]/bibl[143]`.

```xml
<bibl xml:id="fr-ex-Etudes_Litt" xml:lang="fr">
        <title>
          <ref target="http://www.etudes-litteraires.com/figures-de-style/deictique.php">Études
            littéraires</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
```

^b145

### Block 146

XML location: `/div[1]/div[1]/listBibl[1]/bibl[144]`.

```xml
<bibl xml:id="fr-ex-Constant-Journal" xml:lang="fr"><author>Fallet , René</author>, <title>Le
          Triporteur</title>, <date>1951</date>.</bibl>
```

^b146

### Block 147

XML location: `/div[1]/div[1]/listBibl[1]/bibl[145]`.

```xml
<bibl xml:id="FieldScreen"><author>Field, Syd</author>
        <title>Screenplay: the Foundations of Screenwriting</title> (<date>1998</date>).</bibl>
```

^b147

### Block 148

XML location: `/div[1]/div[1]/listBibl[1]/bibl[146]`.

```xml
<bibl xml:id="DSDIV3-eg-22"><author>Fielding, Henry</author>. <title level="a">The History of
          the Adventures of Joseph Andrews and his Friend, Mr. Abraham Abrams</title>
          (<date>1742</date>).</bibl>
```

^b148

### Block 149

XML location: `/div[1]/div[1]/listBibl[1]/bibl[147]`.

```xml
<bibl xml:id="DRCAST-eg-18">
        <author>Fielding, Henry</author>. <title level="m">Tragedy of Tragedies</title>,
          (<date>1737</date>).</bibl>
```

^b149

### Block 150

XML location: `/div[1]/div[1]/listBibl[1]/bibl[148]`.

```xml
<bibl xml:id="DS-eg-05">
        <author>Fish, Stanley</author>. <title>Is there a text in this class? The authority of
          interpretive communities</title>. <publisher>Harvard University Press</publisher>
          (<date>1980</date>). </bibl>
```

^b150

### Block 151

XML location: `/div[1]/div[1]/listBibl[1]/bibl[149]`.

```xml
<bibl xml:id="SAAG-eg-72"><author>Fisher, M. F. K. </author><title level="a">I Was Really Very
          Hungry</title> In <title level="m">As They Were</title>, <publisher> Knopf</publisher>
          (<date>1982</date>), <biblScope unit="pp">p. 43</biblScope>.</bibl>
```

^b151

### Block 152

XML location: `/div[1]/div[1]/listBibl[1]/bibl[150]`.

```xml
<bibl xml:id="fitrub">
        <!-- tip o the hat to John Lavignino -->
        <author>FitzGerald, Edward</author>. <title>The Rubáiyát of Omar Khayyám, translated into
          English Verse</title> (<date>1859</date>), <biblScope>stanza 25</biblScope>. </bibl>
```

^b152

### Block 153

XML location: `/div[1]/div[1]/listBibl[1]/bibl[151]`.

```xml
<bibl xml:id="fr-ex-Flaubert_Sal" xml:lang="fr"><author>Flaubert, Gustave</author>,
          <title>Salammbô</title>, <date>1862</date>.</bibl>
```

^b153

### Block 154

XML location: `/div[1]/div[1]/listBibl[1]/bibl[152]`.

```xml
<bibl xml:id="fr-ex-Flaubert_Tent" xml:lang="fr"><author>Flaubert, Gustave</author>, <title>
          La Tentation de saint Antoine</title>, <date>1874</date>.</bibl>
```

^b154

### Block 155

XML location: `/div[1]/div[1]/listBibl[1]/bibl[153]`.

```xml
<bibl xml:id="FTGRA-eg-18"><author>Foley James D.</author>, <author>Andries van Dam</author>,
          <author>Steven K. Feiner</author> and <author>John F. Hughes</author>. <title level="m">Computer Graphics: Principles and Practice</title>, <edition>2nd edition </edition>
        <pubPlace>Reading</pubPlace>: <publisher>Addison-Wesley</publisher>, <biblScope unit="pp">p.259</biblScope>.</bibl>
```

^b155

### Block 156

XML location: `/div[1]/div[1]/listBibl[1]/bibl[154]`.

```xml
<bibl xml:id="DSAE-eg-38a"><author>Forster, E.M.</author>, <title level="m">Howards
          End</title>. <publisher>Edward Arnold.</publisher> (<date>1910</date>). </bibl>
```

^b156

### Block 157

XML location: `/div[1]/div[1]/listBibl[1]/bibl[155]`.

```xml
<bibl xml:id="fr-ex-la-bas-si-jy-suis" xml:lang="fr">
        <title>
          <ref target="http://sites.radiofrance.fr/franceinter/em/labassijysuis">France inter,
            Là-bas si j'y suis</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
```

^b157

### Block 158

XML location: `/div[1]/div[1]/listBibl[1]/bibl[156]`.

```xml
<bibl xml:id="fr-ex-Teleph_sonne" xml:lang="fr">
        <title>
          <ref target="http://sites.radiofrance.fr/franceinter/em/letelephonesonne/contact.php">France inter, Le téléphone sonne</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
```

^b158

### Block 159

XML location: `/div[1]/div[1]/listBibl[1]/bibl[157]`.

```xml
<bibl xml:id="fr-ex-franglais" xml:lang="fr">
        <title>
          <ref target="http://franglais.ini.hu/">Franglais et franricain</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
```

^b159

### Block 160

XML location: `/div[1]/div[1]/listBibl[1]/bibl[158]`.

```xml
<bibl xml:id="FR1B"><author>Fry, Christopher</author>, <title>The firstborn</title>
          (<date>1948</date>).</bibl>
```

^b160

### Block 161

XML location: `/div[1]/div[1]/listBibl[1]/bibl[159]`.

```xml
<bibl xml:id="biblzh-tw_n34" xml:lang="zh-TW">福春嫁女</bibl>
```

^b161

### Block 162

XML location: `/div[1]/div[1]/listBibl[1]/bibl[160]`.

```xml
<bibl xml:id="DS-eg-03">
        <editor>Fussell, Paul</editor>. <title>The Norton Book of Travel</title>. <publisher> W. W.
          Norton</publisher> (<date>1987</date>). </bibl>
```

^b162

### Block 163

XML location: `/div[1]/div[1]/listBibl[1]/bibl[161]`.

```xml
<bibl xml:id="COEDADD-eg-83"><author>Galilei, Galileo</author>, <title level="m">Sidereus
          Nuncius</title>, <pubPlace>Venetiis</pubPlace>: <publisher>Apud Thomam
          Baglionum</publisher>, <date>1610</date>, quoted by <author>Tufte, Edward R.</author>,
          <title level="m">Envisioning Information</title>, <pubPlace>Cheshire</pubPlace>:
          <publisher>Graphics Press</publisher> (<date>1990</date>), <biblScope unit="pp">p.
          97</biblScope>. </bibl>
```

^b163

### Block 164

XML location: `/div[1]/div[1]/listBibl[1]/bibl[162]`.

```xml
<bibl xml:id="fr-ex-Galland_Mille" xml:lang="fr"><author>Galland, Antoine</author>,<title> Les
          Mille et une nuits</title>, <date>1704</date>.</bibl>
```

^b164

### Block 165

XML location: `/div[1]/div[1]/listBibl[1]/bibl[163]`.

```xml
<bibl xml:id="GalswStr"><author>Galsworthy, John</author>, <title level="m">Strife</title>. In
          <title>Plays, vol 1.</title> (<date>1909</date>). <!-- check --></bibl>
```

^b165

### Block 166

XML location: `/div[1]/div[1]/listBibl[1]/bibl[164]`.

```xml
<bibl xml:id="COEDADD-eg-84"><author>Gaskell, Elizabeth Cleghorn</author>. <title level="m">The Grey Woman</title>, MS.</bibl>
```

^b166

### Block 167

XML location: `/div[1]/div[1]/listBibl[1]/bibl[165]`.

```xml
<bibl xml:id="TSTPPR-eg-58"><author>Gavioli, Laura</author> and <author>Gillian
          Mansfield</author>. <title level="m">The PIXI corpora: bookshop encounters in English and
          Italian</title>, <pubPlace>Bologna</pubPlace>: <publisher>Cooperativa Libraria
          Universitaria Editrice</publisher> (<date>1990</date>), <biblScope unit="pp">p.74</biblScope>.</bibl>
```

^b167

### Block 168

XML location: `/div[1]/div[1]/listBibl[1]/bibl[166]`.

```xml
<bibl xml:id="COVE-eg-285"><author>Gay, John</author>. <title>The Beggar's Opera</title>
          (<date>1728</date>).</bibl>
```

^b168

### Block 169

XML location: `/div[1]/div[1]/listBibl[1]/bibl[167]`.

```xml
<bibl xml:id="COHTG-eg-43"><author>Gazdar, Gerald</author> and <author>Mellish,
          Christopher</author>. <title level="m">Natural language processing in Prolog</title>.
          <publisher>Addison-Wesley</publisher> (<date>1989</date>), <biblScope unit="pp">p.5</biblScope>.</bibl>
```

^b169

### Block 170

XML location: `/div[1]/div[1]/listBibl[1]/bibl[168]`.

```xml
<bibl xml:id="FS-BIBL-3">
        <author>Gazdar, Gerald</author>, <author>Ewan Klein, Geoffrey Pullum, and Ivan Sag</author>:
          <title level="m">Generalized Phrase Structure Grammar</title>, <publisher>Harvard
          University Press</publisher> (<date>1985</date>).</bibl>
```

^b170

### Block 171

XML location: `/div[1]/div[1]/listBibl[1]/bibl[169]`.

```xml
<bibl xml:id="GerStra">
        <author>Gershwin, Ira</author>
        <title>By Strauss</title> (from <title>An American in Paris</title>, <date>1953</date>). </bibl>
```

^b171

### Block 172

XML location: `/div[1]/div[1]/listBibl[1]/bibl[170]`.

```xml
<bibl xml:id="PHegsurp2"><editor>Gianfraco Contini</editor>, <title>Poeti del
        Duecento</title>, Milano-Napoli:Ricciardi I, (<date>1960</date>). pp 155-64.</bibl>
```

^b172

### Block 173

XML location: `/div[1]/div[1]/listBibl[1]/bibl[171]`.

```xml
<bibl xml:id="STGA-eg-11"><author>Gibbon, Edward</author>, <title level="m">The History of the
          Decline and Fall of the Roman Empire</title>, (<date>1789</date>), <biblScope unit="chap">chapter 58</biblScope>.</bibl>
```

^b173

### Block 174

XML location: `/div[1]/div[1]/listBibl[1]/bibl[172]`.

```xml
<bibl xml:id="fr-ex-Gide-Journ_fx" xml:lang="fr"><author>Gide, André</author>, <title>Le
          Journal des Faux-Monnayeurs</title>, <date>1927</date>.</bibl>
```

^b174

### Block 175

XML location: `/div[1]/div[1]/listBibl[1]/bibl[173]`.

```xml
<bibl xml:id="fr-ex-Gide_Journal" xml:lang="fr"><author>Gide, André</author>, <title>Journal :
          1889-1939</title>, <date>1939</date>.</bibl>
```

^b175

### Block 176

XML location: `/div[1]/div[1]/listBibl[1]/bibl[174]`.

```xml
<bibl xml:id="DRPAL-eg-46">
        <author>Gilbert, William Schwenck</author> and <author>Sullivan, Arthur</author>. <title level="m">HMS Pinafore</title> (<date>1878</date>), <biblScope unit="part">I</biblScope>.</bibl>
```

^b176

### Block 177

XML location: `/div[1]/div[1]/listBibl[1]/bibl[175]`.

```xml
<bibl xml:id="COVE-eg-284"><author>Gilbert, William Schwenck</author> and <author>Sullivan,
          Arthur</author>. <title level="m">The Mikado</title> (<date>1885</date>).</bibl>
```

^b177

### Block 178

XML location: `/div[1]/div[1]/listBibl[1]/bibl[176]`.

```xml
<bibl xml:id="VEST-eg-2"><author>Ginsberg, Allen</author>. <title level="a">My alba</title>,
          <title level="m">Reality Sandwiches</title>, <pubPlace>San Francisco</pubPlace>:
          <publisher>City Lights</publisher>, (<date>1963</date>).</bibl>
```

^b178

### Block 179

XML location: `/div[1]/div[1]/listBibl[1]/bibl[177]`.

```xml
<bibl xml:id="fr-ex-Giono-Regain" xml:lang="fr"><author>Giono, Jean</author>,
          <title>Regain</title>, <date>1930</date>.</bibl>
```

^b179

### Block 180

XML location: `/div[1]/div[1]/listBibl[1]/bibl[178]`.

```xml
<bibl xml:id="fr-ex-Guerre-Troie" xml:lang="fr"><author>Giraudoux, Jean</author>, <title>La
          guerre de Troie n'aura pas lieu</title>, <date>1935</date>.</bibl>
```

^b180

### Block 181

XML location: `/div[1]/div[1]/listBibl[1]/bibl[179]`.

```xml
<bibl xml:id="fr-ex-Godefroy" xml:lang="fr">
        <author>Godefroy, Frédéric</author>, <title>Dictionnaire de l'ancienne langue française et
          de tous ses dialectes du IXe au XVe siècle</title>, <date>1881</date>.</bibl>
```

^b181

### Block 182

XML location: `/div[1]/div[1]/listBibl[1]/bibl[180]`.

```xml
<bibl xml:id="DRDIV-eg-31"><author>Goethe, Johann Wolfgang von</author>, tr. <editor role="tr">Philip Wayne</editor>. <title level="m">Faust</title>, <biblScope unit="part">Part
          1</biblScope>, <pubPlace>London</pubPlace>: Penguin. (<date>1949</date>).</bibl>
```

^b182

### Block 183

XML location: `/div[1]/div[1]/listBibl[1]/bibl[181]`.

```xml
<bibl xml:id="VE-eg-03">
        <author>Goethe, Johann Wolfgang von</author>. <title>Auf dem See</title>
        (<date>1775</date>). </bibl>
```

^b183

### Block 184

XML location: `/div[1]/div[1]/listBibl[1]/bibl[182]`.

```xml
<bibl xml:id="G2S">
        <author>[Goldsmith, Oliver]</author>, <title>The History of Little GOODY TWO-SHOES;
          Otherwise called, Mrs. MARGERY TWO-SHOES...</title> (Printed for J. Newbery,
          <date>1766</date>). </bibl>
```

^b184

### Block 185

XML location: `/div[1]/div[1]/listBibl[1]/bibl[183]`.

```xml
<bibl xml:id="HDUDECL-TG">
        <author>Grallert, Till</author>, <title>Tools for the Computational Normalisation and
          Analysis of Food Prices and Food Riots in the Eastern Mediterranean (Bilād al-Shām) in the
          19th and 20th Centuries</title>. <publisher>Zenodo</publisher>, <date>2021</date>. <ptr target="https://doi.org/10.5281/zenodo.5159020"/>. </bibl>
```

^b185

### Block 186

XML location: `/div[1]/div[1]/listBibl[1]/bibl[184]`.

```xml
<bibl xml:id="PH-eg-07">
        <author>Graves, Robert</author>. <title>Rough draft of letter to Desmond Flower</title>.
          <date>17 Dec 1938</date>. (from <title level="m">Diary of Robert Graves 1935-39 and
          ancillary materials</title>, compiled by Beryl Graves, C.G. Petter, L.R. Roberts,
        University of Victoria Libraries).</bibl>
```

^b186

### Block 187

XML location: `/div[1]/div[1]/listBibl[1]/bibl[185]`.

```xml
<bibl xml:id="DSBACK-eg-86">
        <author>Greene, Robert</author>. <title level="m">Groatsworth of Wit Bought with a Million
          of Repentance</title> (<date>1592</date>).</bibl>
```

^b187

### Block 188

XML location: `/div[1]/div[1]/listBibl[1]/bibl[186]`.

```xml
<bibl xml:id="DS-eg-01">
        <author>Gregory of Tours</author>. <title level="m">Ecclesiastical History of the
          Franks</title> (translated by Lewis Thorpe). </bibl>
```

^b188

### Block 189

XML location: `/div[1]/div[1]/listBibl[1]/bibl[187]`.

```xml
<bibl xml:id="fr-ex-Greimas_Courtes" xml:lang="fr"><author>Greimas, Algirdas Julien</author>
        et <author>Courtés, Joseph</author>, <title>Sémiotique : dictionnaire raisonné de la théorie
          du langage</title>, <date>1979</date>. </bibl>
```

^b189

### Block 190

XML location: `/div[1]/div[1]/listBibl[1]/bibl[188]`.

```xml
<bibl xml:id="COXR-eg-166"><author>Grune, Dick</author> and <author>Ceriel J. H.
          Jacobs</author>. <title level="m">Parsing Techniques: A Practical Guide</title>,
          <pubPlace>New York</pubPlace> and <pubPlace>London</pubPlace>: <publisher>Ellis
          Horwood</publisher>, <date>1990</date>, <biblScope unit="pp">p. 24</biblScope>.</bibl>
```

^b190

### Block 191

XML location: `/div[1]/div[1]/listBibl[1]/bibl[189]`.

```xml
<bibl xml:id="DIC-DNT">
        <editor>Guerard, Françoise</editor>. <title>Le Dictionnaire de Notre Temps</title>, ed.
          <pubPlace>Paris</pubPlace>: <publisher>Hachette</publisher>, <date>1990</date>
      </bibl>
```

^b191

### Block 192

XML location: `/div[1]/div[1]/listBibl[1]/bibl[190]`.

```xml
<bibl xml:id="hallWell"><author>Hall, Radclyffe</author>. <title>The well of
          loneliness</title>. (<date>1928</date>).</bibl>
```

^b192

### Block 193

XML location: `/div[1]/div[1]/listBibl[1]/bibl[191]`.

```xml
<bibl xml:id="CONAAB-eg-150"><author>Halliday, M.A.K. </author> and <author>R.
        Hassan</author>. <title level="m">Language, Context and Text: Aspects of Language in a
          Social-Semiotic Perspective</title>, <pubPlace>Oxford</pubPlace>: <publisher>Oxford
          University Press</publisher>, <date>1990</date>, <biblScope unit="pp">p.
        104</biblScope>.</bibl>
```

^b193

### Block 194

XML location: `/div[1]/div[1]/listBibl[1]/bibl[192]`.

```xml
<bibl xml:id="COHQQ-eg-29"><author>Hanks, Patrick</author>. <title level="a">Definitions and
          Explanations</title>. In <editor>J. M. Sinclair</editor> ed. <title level="m">Looking Up.
          </title><publisher>Collins</publisher>, <date>1987</date>, <biblScope unit="pp">p. 121
        </biblScope>.</bibl>
```

^b194

### Block 195

XML location: `/div[1]/div[1]/listBibl[1]/bibl[193]`.

```xml
<bibl xml:id="eebo87070"><title>Hannam's last farewell to the world:: being a full and true
          relation of the notorious life and shamfull death of Mr. Richard Hannam...</title>
          (<date>1656</date>).</bibl>
```

^b195

### Block 196

XML location: `/div[1]/div[1]/listBibl[1]/bibl[194]`.

```xml
<bibl xml:id="DR-eg-01">
        <author>Hansberry, Lorraine</author>. <title>A raisin in the sun. </title>
          (<date>1959</date>). </bibl>
```

^b196

### Block 197

XML location: `/div[1]/div[1]/listBibl[1]/bibl[195]`.

```xml
<bibl xml:id="harveyFour"><author>Harvey, Gabriel</author>. <title>Four letters and certain
          sonnets specially touching Robert Greene...</title> (<date>1592</date>).</bibl>
```

^b197

### Block 198

XML location: `/div[1]/div[1]/listBibl[1]/bibl[196]`.

```xml
<bibl xml:id="CO-eg-05"><author>Harvey, William</author>. <title>Exercitatio Anatomica De Motu
          Cordis Et Sanguinis In Animalibus</title>, <date>1949</date> (Third edition, second
        printing), <biblScope unit="page">p. 74</biblScope>. <ptr target="https://archive.org/details/in.ernet.dli.2015.115852/page/n98/mode/1up"/></bibl>
```

^b198

### Block 199

XML location: `/div[1]/div[1]/listBibl[1]/bibl[197]`.

```xml
<bibl xml:id="leviathan"><author>Hobbes, Thomas</author>. <title>Leviathan</title>
          (<date>1681</date>).</bibl>
```

^b199

### Block 200

XML location: `/div[1]/div[1]/listBibl[1]/bibl[198]`.

```xml
<bibl xml:id="biblzh-tw_n3" xml:lang="zh-TW">《紅樓夢》第六回：賈寶玉初試云雨情 劉姥姥一進榮國府</bibl>
```

^b200

### Block 201

XML location: `/div[1]/div[1]/listBibl[1]/bibl[199]`.

```xml
<bibl xml:id="biblzh-tw_n43" xml:lang="zh-TW">〈紅頭嶼踏查報告〉，國立台灣大學圖書館：田代文庫。</bibl>
```

^b201

### Block 202

XML location: `/div[1]/div[1]/listBibl[1]/bibl[200]`.

```xml
<bibl xml:id="fr-ex-Fleurs" xml:lang="fr"><author>Hoola Van Nooten,
          Berthe</author><title>Fleurs, fruits et feuillages choisis de l'île de Java peints d'après
          nature</title>, troisième édition par <publisher>C. Muquardt</publisher>, Bruxelles,
          <date>1880</date>.</bibl>
```

^b202

### Block 203

XML location: `/div[1]/div[1]/listBibl[1]/bibl[201]`.

```xml
<bibl xml:id="DIC-OALD">
        <editor>Hornby, A.S. et al</editor>. <title>Oxford Advanced Learner's Dictionary of Current
          English</title>. <publisher>Oxford University Press</publisher> (<date>1974</date>). </bibl>
```

^b203

### Block 204

XML location: `/div[1]/div[1]/listBibl[1]/bibl[202]`.

```xml
<bibl xml:id="biblzh-tw_n5" xml:lang="zh-TW">黃晨淳編著，《希臘羅馬神話故事》，p76。</bibl>
```

^b204

### Block 205

XML location: `/div[1]/div[1]/listBibl[1]/bibl[203]`.

```xml
<bibl xml:id="fr-ex-Hugo-Notre-Dame" xml:lang="fr"><author>Hugo, Victor</author>,
          <title>Notre-Dame de Paris</title>, <date>1845</date>.</bibl>
```

^b205

### Block 206

XML location: `/div[1]/div[1]/listBibl[1]/bibl[204]`.

```xml
<bibl xml:id="fr-ex-Hugo-Nuit" xml:lang="fr">
        <title level="a">Souvenir de la nuit du 4</title>, in : <author>Hugo, Victor</author>,
          <title level="m">Les Contemplations</title>, <date>1853</date>. </bibl>
```

^b206

### Block 207

XML location: `/div[1]/div[1]/listBibl[1]/bibl[205]`.

```xml
<bibl xml:id="fr-ex-Hugo-miserables" xml:lang="fr"><author>Hugo, Victor</author>, <title>Les
          Misérables</title>, <date>1862</date>.</bibl>
```

^b207

### Block 208

XML location: `/div[1]/div[1]/listBibl[1]/bibl[206]`.

```xml
<bibl xml:id="fr-ex-Hugo-Fen" xml:lang="fr">
        <title level="a">A la fenêtre pendant la nuit</title>, in : <author>Hugo, Victor </author>,
          <title level="m">Les Contemplations</title>, <date>1856</date>. </bibl>
```

^b208

### Block 209

XML location: `/div[1]/div[1]/listBibl[1]/bibl[207]`.

```xml
<bibl xml:id="fr-ex-Huizinga_Aut" xml:lang="fr"><author>Huizinga, Johan</author>,
          <title>L'Automne du Moyen-Âge</title>, <date>1919</date>.</bibl>
```

^b209

### Block 210

XML location: `/div[1]/div[1]/listBibl[1]/bibl[208]`.

```xml
<bibl xml:id="COBICOR-eg-248"><title level="m">ISO 690:1987: Information and documentation –
          Bibliographic references – Content, form and structure </title>
        <biblScope unit="part">clause 4.1</biblScope>, <biblScope unit="pp">p.2</biblScope>.</bibl>
```

^b210

### Block 211

XML location: `/div[1]/div[1]/listBibl[1]/bibl[209]`.

```xml
<bibl xml:id="ISO24611"><title level="m">ISO 24611:2012 Language resource management —
          Morpho-syntactic annotation framework (MAF)</title>. <author>International Organization
          for Standardization</author>. <date>2012</date>.</bibl>
```

^b211

### Block 212

XML location: `/div[1]/div[1]/listBibl[1]/bibl[210]`.

```xml
<bibl xml:id="DR-eg-02">
        <author>Ibsen, Henrik</author>, <editor role="tr"> tr. William and Charles Archer</editor>.
          <title>Peer Gynt</title> (<date>1875</date>).</bibl>
```

^b212

### Block 213

XML location: `/div[1]/div[1]/listBibl[1]/bibl[211]`.

```xml
<bibl xml:id="PH-ib01">
        <author>Ibsen, Henrik</author>
        <title>Den episke Brand</title> KBK Collin 2869, 4º I, fol. 11v. </bibl>
```

^b213

### Block 214

XML location: `/div[1]/div[1]/listBibl[1]/bibl[212]`.

```xml
<bibl xml:id="PH-ib04">
        <author>Ibsen, Henrik</author>
        <title>Digte</title> NBO Ms.4º 1110a, p. 36. </bibl>
```

^b214

### Block 215

XML location: `/div[1]/div[1]/listBibl[1]/bibl[213]`.

```xml
<bibl xml:id="PH-ib05">
        <author>Ibsen, Henrik</author>
        <title>Brand</title>, The Royal Library, Denmark. KBK Collin 262, 4°, I.1.1, fol.
        [4]v</bibl>
```

^b215

### Block 216

XML location: `/div[1]/div[1]/listBibl[1]/bibl[214]`.

```xml
<bibl xml:id="DRSTA-eg-40"><author>Ibsen, Henrik</author>, tr. <editor role="tr">R.
          Farquharson Sharp</editor> and <editor role="tr">Eleanor Marx-Aveling. </editor>
        <title level="m">A Doll's House</title> In <title level="m">A Doll's House; and Two Other
          Plays by Henrik Ibsen</title>, <series>Everyman's library: the drama <biblScope unit="vol">494</biblScope>
        </series>, <pubPlace>London</pubPlace>: <publisher>J. M. Dent &amp; Sons</publisher>,
          <date>1910</date>.</bibl>
```

^b216

### Block 217

XML location: `/div[1]/div[1]/listBibl[1]/bibl[215]`.

```xml
<bibl xml:id="DROTH-eg-58"><author>Idle, Eric</author>, <author>Michael Palin</author>,
          <author>Graham Chapman</author>, <author>John Cleese</author>, <author>Terry
          Gilliam</author>. <title level="m">The Complete Monty Python's Flying Circus: All the
          Words</title>, <publisher>Pantheon Books</publisher>, (<date>1989</date>), <biblScope unit="vol">2</biblScope>, <biblScope unit="pp">p.230</biblScope>.</bibl>
```

^b217

### Block 218

XML location: `/div[1]/div[1]/listBibl[1]/bibl[216]`.

```xml
<bibl xml:id="fr-ex-Melanges_Imbs" xml:lang="fr"><author>Imbs, Paul</author>, <author>Martin,
          Robert</author>, <author>Straka, Georges</author>, <title>Mélanges de linguistique
          française et de philologie et littérature médiévales offerts à Monsieur Paul
          Imbs</title>, <date>1973 </date>.</bibl>
```

^b218

### Block 219

XML location: `/div[1]/div[1]/listBibl[1]/bibl[217]`.

```xml
<bibl xml:id="fr-ex-Cyrus" xml:lang="fr"><author>Institut de Littérature Française Moderne de
          l’Université de Neuchâtel</author>, <title>Présentation du projet Cyrus</title>, <ref target="http://www.artamene.org/projet.php">En ligne</ref>, <date>consulté le
          05-03-2010</date>.</bibl>
```

^b219

### Block 220

XML location: `/div[1]/div[1]/listBibl[1]/bibl[218]`.

```xml
<bibl xml:id="fr-ex-Ionesco-chauve" xml:lang="fr"><author>Ionesco, Eugène</author>, <title>La
          cantatrice chauve</title>, <date>1950</date>.</bibl>
```

^b220

### Block 221

XML location: `/div[1]/div[1]/listBibl[1]/bibl[219]`.

```xml
<bibl xml:id="biblzh-tw_n61" xml:lang="zh-TW">羅貫中，《三國演義》。</bibl>
```

^b221

### Block 222

XML location: `/div[1]/div[1]/listBibl[1]/bibl[220]`.

```xml
<bibl xml:id="TEI-L_b092ac32.2101">
        <author>Jakacki, Diane</author>. <title level="a">Schema question: further constraining
          @subtype based on @type</title>. <date when="2021-01-18T12:21:11-05:00">January 18,
          2021</date>. <title level="s">TEI (Text Encoding Initiative) public discussion
          list</title>, <ptr target="https://listserv.brown.edu/cgi-bin/wa?A2=TEI-L;b092ac32.2101"/>. </bibl>
```

^b222

### Block 223

XML location: `/div[1]/div[1]/listBibl[1]/bibl[221]`.

```xml
<bibl xml:id="DRDIV-eg-32"><author>Jarry, Alfred</author>, tr. <editor role="tr">Simon Watson
          Taylor</editor> and <editor role="tr">Cyril Connolly</editor>. <title level="m">The Ubu
          plays</title>, <pubPlace>London</pubPlace>: <publisher>Methuen</publisher>,
          <date>1968</date>.</bibl>
```

^b223

### Block 224

XML location: `/div[1]/div[1]/listBibl[1]/bibl[222]`.

```xml
<bibl xml:id="fr-ex-rousscon" xml:lang="fr"><author>Jean-Jacques Rousseau</author>
        <title>Les confessions</title> vol 6</bibl>
```

^b224

### Block 225

XML location: `/div[1]/div[1]/listBibl[1]/bibl[223]`.

```xml
<bibl xml:id="DSAE-eg-36"><author>Jerome, Jerome K. </author>
        <title level="m">Three men in a boat</title> (<date>1889</date>), <biblScope unit="chap">chapter 6</biblScope>.</bibl>
```

^b225

### Block 226

XML location: `/div[1]/div[1]/listBibl[1]/bibl[224]`.

```xml
<bibl xml:id="fr-ex-Campe" xml:lang="fr"><author>Joachim Heinrich
          Campe</author><title>Wörterbuch der Deutschen Sprache. Erster Theil. A - bis - E.</title>,
          <date>1807</date>.</bibl>
```

^b226

### Block 227

XML location: `/div[1]/div[1]/listBibl[1]/bibl[225]`.

```xml
<bibl xml:id="GibAut"><author>John, Lord Sheffield</author>, <title level="m">The
          Auto-biography of Edward Gibbon esq.</title>, (<date>1846</date>), <biblScope unit="pp">222</biblScope>.</bibl>
```

^b227

### Block 228

XML location: `/div[1]/div[1]/listBibl[1]/bibl[226]`.

```xml
<bibl xml:id="JonsBart"><author>Jonson, Ben</author>. <title level="m">Bartholomew
          Fair</title>. </bibl>
```

^b228

### Block 229

XML location: `/div[1]/div[1]/listBibl[1]/bibl[227]`.

```xml
<bibl xml:id="DRSP-eg-37"><author>Jonson, Ben</author>. <title level="m">Volpone</title>,
          <editor>J. B. Bamborough</editor> ed. <publisher>Macmillan</publisher>, <date>1963</date>,
          <biblScope unit="pp">p.14</biblScope>.</bibl>
```

^b229

### Block 230

XML location: `/div[1]/div[1]/listBibl[1]/bibl[228]`.

```xml
<bibl xml:id="DRPAL-eg-44"><author>Jonson, Ben</author>. <title level="m">The Alchemist
        </title>, <editor>Douglas Brown</editor> ed. <pubPlace>London</pubPlace>:
          <publisher>Benn</publisher>, <date>1966</date>, <biblScope unit="part">I.1,
          </biblScope><biblScope unit="pp">p.9</biblScope>.</bibl>
```

^b230

### Block 231

XML location: `/div[1]/div[1]/listBibl[1]/bibl[229]`.

```xml
<bibl xml:id="DSCO-eg-53"><author>Joyce, James</author>. <title level="m">Ulysses</title>:
          <publisher>The Bodley Head</publisher>, <date>1960</date>. <biblScope unit="pp">p.
          933</biblScope>.</bibl>
```

^b231

### Block 232

XML location: `/div[1]/div[1]/listBibl[1]/bibl[230]`.

```xml
<bibl xml:id="WD-BASHO">
        <author>Judith Patt</author>, <author>Michiko Warkentyne</author> and <author>Barry
          Till</author>. <title>Haiku: Japanese Art and Poetry</title>. <date>2010</date>.
          <publisher>Pomegranate Communications, Inc. San Francisco. <ptr target="http://www.pomegranate.com"/>.</publisher>
      </bibl>
```

^b232

### Block 233

XML location: `/div[1]/div[1]/listBibl[1]/bibl[231]`.

```xml
<bibl xml:id="Karstadt-Distinctiones-Thomistarum"><author>Karlstadt, Andreas
          Bodenstein</author>. <title>Distinctiones Thomistarum</title>.
          <pubPlace>Wittenberg</pubPlace>
        <date>1507</date>. In <editor>Harald Bollbuck</editor> ed. <series>Kritische Gesamtausgabe
          Karlstadt</series>
        <biblScope unit="volume">I</biblScope>, available: <ptr target="http://diglib.hab.de/edoc/ed000216/start.htm"/>
      </bibl>
```

^b233

### Block 234

XML location: `/div[1]/div[1]/listBibl[1]/bibl[232]`.

```xml
<bibl xml:id="REF-cb-eg-1"><author>Kersey, John</author>. <title level="m">Dictionarium
          Anglo-Brittannicum: Or, a General English Dictionary</title>. <pubPlace>London</pubPlace>:
          <publisher>J. Wilde</publisher>, <date>1715</date>. <edition>2nd ed.</edition></bibl>
```

^b234

### Block 235

XML location: `/div[1]/div[1]/listBibl[1]/bibl[233]`.

```xml
<bibl xml:id="fr-ex-Kilian-Neige" xml:lang="fr"><author>Kilian, Wilfrid</author>, <title><ref target="http://jubil.upmc.fr/sdx/pl/toc.xsp?id=GH_000484_001&amp;fmt=upmc&amp;idtoc=GH_000484_001-pleadetoc&amp;base=fa">Neige et glaciers ; notes prises au cours de géologie de la Faculté des Sciences de
            Grenoble par M. Alamelle</ref></title>, <date>1891-1895</date>.</bibl>
```

^b235

### Block 236

XML location: `/div[1]/div[1]/listBibl[1]/bibl[234]`.

```xml
<bibl xml:id="MLK01"><author>King, Martin Luther</author>. <title>Letter from Birmingham City
          Jail</title>. <pubPlace>Philadelphia, PA</pubPlace>: <publisher>American Friends Service
          Committee</publisher> (<date>1963</date>).</bibl>
```

^b236

### Block 237

XML location: `/div[1]/div[1]/listBibl[1]/bibl[235]`.

```xml
<bibl xml:id="COHQHF-eg-5"><author>Kipling, Rudyard</author>. <title level="a">The mother
          hive</title>. In <title level="m">Actions and Reactions</title>,
          <pubPlace>London</pubPlace>: <publisher>Macmillan</publisher>, (<date>1909</date>).</bibl>
```

^b237

### Block 238

XML location: `/div[1]/div[1]/listBibl[1]/bibl[236]`.

```xml
<bibl xml:id="COHQHD-eg-18">
        <author>Kipling, Rudyard</author>. <title level="m">Stalky &amp; Co.</title>,
          <pubPlace>London</pubPlace>: <publisher>Macmillan</publisher> (<date>1899</date>). </bibl>
```

^b238

### Block 239

XML location: `/div[1]/div[1]/listBibl[1]/bibl[237]`.

```xml
<bibl xml:id="COHQQ-eg-27"><author>Kipling, Rudyard</author>. <title level="m">Kim</title>,
          <publisher>Macmillan</publisher>, (<date>1901</date>), <biblScope unit="pp">p.
          9</biblScope>.</bibl>
```

^b239

### Block 240

XML location: `/div[1]/div[1]/listBibl[1]/bibl[238]`.

```xml
<bibl xml:id="KNUTHMAD"><author>Knuth, Donald Ervin</author>. <title level="a">The Potrzebie
          System of Weights and Measures</title>, <title level="j">Mad Magazine</title><biblScope unit="issue">33</biblScope><date when="1957-06">June 1957</date>. </bibl>
```

^b240

### Block 241

XML location: `/div[1]/div[1]/listBibl[1]/bibl[239]`.

```xml
<bibl xml:id="fr-ex-Koltes_Quai_Vol" xml:lang="fr"><author>Koltès,
          Bernard-Marie</author>,<title> Quai ouest</title>, <date>1985</date>. </bibl>
```

^b241

### Block 242

XML location: `/div[1]/div[1]/listBibl[1]/bibl[240]`.

```xml
<bibl xml:id="PHegsurp"><author>Krummrey, Hans</author>, <author>Panciera, Silvio</author>
        <title>Criteri di edizione e segni diacritici</title>, Tituli 2 (<date>1980</date>),
        205-215.</bibl>
```

^b242

### Block 243

XML location: `/div[1]/div[1]/listBibl[1]/bibl[241]`.

```xml
<bibl xml:id="KYD"><author>Kyd, Thomas</author>. <title>Spanish Tragedy</title>
          (<date>1592</date>).</bibl>
```

^b243

### Block 244

XML location: `/div[1]/div[1]/listBibl[1]/bibl[242]`.

```xml
<bibl xml:id="RphCnd"><author>Lacy, M. Rophino</author>, <title level="m">Cinderella, 
          Or the Fairy-Queen and the Glass Slipper: A Comic Opera, In Three Acts</title>.
        <title level="s">Lacy's Acting Edition</title>, <biblScope unit="volume">volume 18</biblScope>:
        <biblScope unit="number">No. 0262</biblScope>, <pubPlace>London</pubPlace>: 
          <publisher>Thomas Hailes Lacy</publisher>, <biblScope unit="page">pp. 209–268</biblScope>. 
        <date notBefore="1849">undated</date>.</bibl>
```

^b244

### Block 245

XML location: `/div[1]/div[1]/listBibl[1]/bibl[243]`.

```xml
<bibl xml:id="fr-ex-Lafayette-Cleves" xml:lang="fr"><author>La Fayette, Marie-Madeleine Pioche
          de La Vergne, comtesse de</author>, <title>La Princesse de Clèves</title>,
          <date>1678</date>.</bibl>
```

^b245

### Block 246

XML location: `/div[1]/div[1]/listBibl[1]/bibl[244]`.

```xml
<bibl xml:id="VESE-eg-13"><author>La Fontaine, Jean de</author>. <title level="a">L'Astrologue
          qui se laisse tomber dans un puits</title> In <title level="m">Fables Choisies</title>,
          <series>Classiques Larousse</series>, <pubPlace>Paris</pubPlace>: <publisher>Librairie
          Larousse</publisher>, <biblScope unit="vol">1</biblScope>, <date>1940</date>.</bibl>
```

^b246

### Block 247

XML location: `/div[1]/div[1]/listBibl[1]/bibl[245]`.

```xml
<bibl xml:id="VESE-eg-13x"><author>La Fontaine, Jean de</author>. <title level="a">Le corbeau
          et le renard</title> In <title level="m">Fables Choisies</title>, <series>Classiques
          Larousse</series>, <pubPlace>Paris</pubPlace>: <publisher>Librairie Larousse</publisher>,
          <biblScope unit="vol">1</biblScope>, <date>1940</date>.</bibl>
```

^b247

### Block 248

XML location: `/div[1]/div[1]/listBibl[1]/bibl[246]`.

```xml
<bibl xml:id="fr-ex-ATILF" xml:lang="fr"><author>Laboratoire ATILF</author>
        <title>
          <ref target="http://www.atilf.fr/">Analyse et traitement informatique de la langue
            française (ATILF)</ref>
        </title>, <date>consulté le 07-05-2010</date>. </bibl>
```

^b248

### Block 249

XML location: `/div[1]/div[1]/listBibl[1]/bibl[247]`.

```xml
<bibl xml:id="CONARS-eg-108">
        <author>Laclos, Pierre Choderlos de</author>. <title level="m">Les Liaisons
          dangereuses</title> (<date>1772</date>), <date>1963</date>, <biblScope unit="pp">p.
          13</biblScope>.</bibl>
```

^b249

### Block 250

XML location: `/div[1]/div[1]/listBibl[1]/bibl[248]`.

```xml
<bibl xml:id="CONARS-eg-111"><author>Ladurie, Emmanuel Le Roy</author>. <title level="m">Montaillou</title>, <pubPlace>Middlesex</pubPlace>: <publisher>Penguin Books</publisher>,
          <date>1980</date>, <biblScope unit="pp">p. 3</biblScope>.</bibl>
```

^b250

### Block 251

XML location: `/div[1]/div[1]/listBibl[1]/bibl[249]`.

```xml
<bibl xml:id="fr-ex-Lamartine" xml:lang="fr"><author>Lamartine, Alphonse de</author>,
          <title>Méditations poétiques</title>, <date>1820</date>.</bibl>
```

^b251

### Block 252

XML location: `/div[1]/div[1]/listBibl[1]/bibl[250]`.

```xml
<bibl xml:id="fr-ex-manus-Saint-Petersbourg" xml:lang="fr"><author>Lamothe, Alexandre
          de</author>
        <title level="a">Principaux manuscrits latins et français conservés dans la Bibliothèque
          impériale et dans celle de l'Ermitage à Saint-Pétersbourg</title>, <ref target="http://www.persee.fr/web/revues/home/prescript/article/bec_0373-6237_1864_num_25_1_445928">édition numérique</ref>, <title level="s">Bibliothèque de l'école nationale des
          chartes</title>, <date>1864</date>. </bibl>
```

^b252

### Block 253

XML location: `/div[1]/div[1]/listBibl[1]/bibl[251]`.

```xml
<bibl xml:id="COHQQ-eg-33"><author>Langendoen, D. Terence</author> and <author>Paul M.
          Postal</author>. <title level="m">Vastness of Natural Languages</title>,
          <pubPlace>Oxford</pubPlace>: Basil Blackwell, <date>1984</date>, <biblScope unit="pp">p.
          24</biblScope>, <biblScope unit="note">note 12</biblScope>.</bibl>
```

^b253

### Block 254

XML location: `/div[1]/div[1]/listBibl[1]/bibl[252]`.

```xml
<bibl xml:id="LANGENPOST"><author>Langendoen, D. Terence and Paul Postal</author>. <title>The
          vastness of natural languages</title>, <publisher>Blackwell, </publisher>, <biblScope unit="pp">1</biblScope>, <date>1984</date>.</bibl>
```

^b254

### Block 255

XML location: `/div[1]/div[1]/listBibl[1]/bibl[253]`.

```xml
<bibl xml:id="VESE-eg-9">
        <author>Langland, William</author>. <title level="m">The Vision of Piers Plowman</title>. In
          <editor>A.V.C. Schmidt</editor> ed. <title level="m">Langland: Vision of Piers Plowman:
          "B" Text</title>, <biblScope unit="part">opening</biblScope>.</bibl>
```

^b255

### Block 256

XML location: `/div[1]/div[1]/listBibl[1]/bibl[254]`.

```xml
<bibl xml:id="punctuseg"><title>Latin liturgical manuscript: Bod MS. Lat liturg. b.
        19</title>, folio 4r. Taken from the digitized image described at <ptr target="https://www.diamm.ac.uk/sources/522/"/>.</bibl>
```

^b256

### Block 257

XML location: `/div[1]/div[1]/listBibl[1]/bibl[255]`.

```xml
<bibl xml:id="fr-ex-Lavrentev-TEI-BFM" xml:lang="fr"><author>Lavrentev, Alexei</author>,
            <title><ref target="http://ccfm.ens-lsh.fr/IMG/pdf/BFM-Mss_Encodage-XML.pdf">Manuel
            d’encodage XML-TEI étendu des transcriptions de manuscrits dans le projet
            BFM-Manuscrits</ref></title>, dernier enregistrement le <date>26 juin
        2008</date>.</bibl>
```

^b257

### Block 258

XML location: `/div[1]/div[1]/listBibl[1]/bibl[256]`.

```xml
<bibl xml:id="PH-eg-06">
        <author>Lawrence, David Herbert</author>. Autograph manuscript of <title>Eloi, Eloi, lama
          sabachthani</title>, Pierpont Morgan MA 1892; in <ptr target="#KLINKENBORG"/> p.129. </bibl>
```

^b258

### Block 259

XML location: `/div[1]/div[1]/listBibl[1]/bibl[257]`.

```xml
<bibl xml:id="PH-eg-01">
        <author>Layamon</author>. <title>Brut</title>, fol 65v of Bodleian MS. Rawlinson Poetry 32;
        in <ptr target="#PARKES"/> 12(ii). </bibl>
```

^b259

### Block 260

XML location: `/div[1]/div[1]/listBibl[1]/bibl[258]`.

```xml
<bibl xml:id="fr-ex-Grand-Robert" xml:lang="fr"><title>Le Grand Robert de la langue
          française</title>, <date>2004</date>. </bibl>
```

^b260

### Block 261

XML location: `/div[1]/div[1]/listBibl[1]/bibl[259]`.

```xml
<bibl xml:id="NH-eg-03"><author>LeTourneau, Mark S. </author>
        <title level="m">English Grammar</title>, <date>2001</date>, <pubPlace>New York</pubPlace>:
          <publisher>Harcourt</publisher>
        <biblScope>p. 89</biblScope>.</bibl>
```

^b261

### Block 262

XML location: `/div[1]/div[1]/listBibl[1]/bibl[260]`.

```xml
<bibl xml:id="SACS1-eg-48">
        <editor>Leech, G.</editor>, <editor>G. Myers</editor>, <editor>J. Thomas</editor> eds.
          <title level="m">Spoken English on Computer: Transcription, Markup and
          Applications</title>. <pubPlace>Harlow</pubPlace>: <publisher>Longman</publisher>,
          <date>1995</date>.</bibl>
```

^b262

### Block 263

XML location: `/div[1]/div[1]/listBibl[1]/bibl[261]`.

```xml
<bibl xml:id="COHTG-eg-42"><author>Leech, Geoffrey</author> and <author>Mick Short</author>.
          <title level="m">Style in Fiction</title>, <pubPlace>London</pubPlace>:
          <publisher>Longman</publisher>, <date>1981</date>, <biblScope unit="pp">p.272</biblScope>.</bibl>
```

^b263

### Block 264

XML location: `/div[1]/div[1]/listBibl[1]/bibl[262]`.

```xml
<bibl xml:id="COEDADD-eg-92">
        <author>Lennon, John</author> and <author>McCartney, Paul</author>. <title level="a">She
          Loves You</title>. <title level="m">The Beatles Anthology 1</title>.
          <publisher>Capitol</publisher>, <date>1995</date>. </bibl>
```

^b264

### Block 265

XML location: `/div[1]/div[1]/listBibl[1]/bibl[263]`.

```xml
<bibl xml:id="fr-ex-Lery" xml:lang="fr"><author>Léry, Jean de</author>, <title>Histoire faict
          en la terre de Brésil</title>, <date>1580</date>.</bibl>
```

^b265

### Block 266

XML location: `/div[1]/div[1]/listBibl[1]/bibl[264]`.

```xml
<bibl xml:id="AI-BIBL-4">
        <author>Lessing, Doris</author>. <title level="m">Martha Quest</title>. <date>1952</date>,
          <biblScope unit="pp">pp. 52-53</biblScope>. </bibl>
```

^b266

### Block 267

XML location: `/div[1]/div[1]/listBibl[1]/bibl[265]`.

```xml
<bibl xml:id="SERAFIN2"><title>Letter of Mikołaj Orlik to Mikołaj Serafin, Gródek, January 13
          [1438]</title>. Edited by <editor>Skolimowska et al.</editor> Available from <ptr target="https://teipublisher.com/exist/apps/serafin/letters/serafin02.xml"/></bibl>
```

^b267

### Block 268

XML location: `/div[1]/div[1]/listBibl[1]/bibl[266]`.

```xml
<bibl xml:id="DRCAST-eg-21"><author>Lewis, Leopold Davis</author>. <title level="m">The
          Bells</title>, (<date>1871</date>), translated from <author>Erckmann-Chatrian</author>,
          <title level="m">Le Juif Polonais</title>.</bibl>
```

^b268

### Block 269

XML location: `/div[1]/div[1]/listBibl[1]/bibl[267]`.

```xml
<bibl xml:id="COHQHE-eg-10">
        <author>Lewis, Wyndham</author>. <title level="m">Tarr</title> (1928),
          <publisher>Jupiter</publisher>, <date>1968</date>, <biblScope unit="pp">p. 17</biblScope>. </bibl>
```

^b269

### Block 270

XML location: `/div[1]/div[1]/listBibl[1]/bibl[268]`.

```xml
<bibl xml:id="biblzh-tw_n65" xml:lang="zh-TW">李白，《黃鶴樓送孟浩然之廣陵》。</bibl>
```

^b270

### Block 271

XML location: `/div[1]/div[1]/listBibl[1]/bibl[269]`.

```xml
<bibl xml:id="biblzh-tw_n37" xml:lang="zh-TW">李白，《靜夜思》。</bibl>
```

^b271

### Block 272

XML location: `/div[1]/div[1]/listBibl[1]/bibl[270]`.

```xml
<bibl xml:id="biblzh-tw_n23-24" xml:lang="zh-TW">《梁山伯與祝英台》</bibl>
```

^b272

### Block 273

XML location: `/div[1]/div[1]/listBibl[1]/bibl[271]`.

```xml
<bibl xml:id="biblzh-tw_n29" xml:lang="zh-TW">電影《梁山伯與祝英台》，舊版。</bibl>
```

^b273

### Block 274

XML location: `/div[1]/div[1]/listBibl[1]/bibl[272]`.

```xml
<bibl xml:id="biblzh-tw_n41" xml:lang="zh-TW">〈歷代漢文大藏經概述〉，李圓淨，原載《南行》第六期（南行學社編印）。</bibl>
```

^b274

### Block 275

XML location: `/div[1]/div[1]/listBibl[1]/bibl[273]`.

```xml
<bibl xml:id="bib4handnoteyi" xml:lang="en">
	<author>Libelt, Karol</author>.
	<title level="m" xml:lang="pl">Wykłady Humboldta na uniwersytecie Berlińskim: notaty prelekcyj tych po uczniu Jego Karolu Libelcie</title>,
	<publisher xml:lang="de">Deutsches Textarchiv</publisher>,
	<date>2024-04-02</date>.
	<idno type="URN">urn:nbn:de:kobv:b4-30960-7</idno>,
	<ptr target="https://www.deutschestextarchiv.de/book/download_xml/libelt_hs6623ii_1828"/>
	<date type="accessed" when="2024-12-04"/>
      </bibl>
```

^b275

### Block 276

XML location: `/div[1]/div[1]/listBibl[1]/bibl[274]`.

```xml
<bibl xml:id="DRPRO-eg-7"><author>Lillo, George</author>. <title level="m">The London
          Merchant</title> (<date>1731</date>), <biblScope unit="part">epilogue</biblScope>.</bibl>
```

^b276

### Block 277

XML location: `/div[1]/div[1]/listBibl[1]/bibl[275]`.

```xml
<bibl xml:id="biblzh-tw_n58" xml:lang="zh-TW">林覺民，《與妻訣別書》。</bibl>
```

^b277

### Block 278

XML location: `/div[1]/div[1]/listBibl[1]/bibl[276]`.

```xml
<bibl xml:id="STGA-eg-9"><author>Lincoln, Abraham</author>. <title level="a">Second Inaugural
          Address</title>, <date>4 March 1865</date>. In <editor>H. S. Commager</editor>, ed.,
          <title level="m">Documents of American History</title>, <edition> 5th ed
          </edition><series>Crofts American history series</series>. <pubPlace>New York</pubPlace>:
          <publisher>Appleton-Century-Crofts</publisher>, <date>1949</date>, <biblScope unit="pp">p.442</biblScope>. </bibl>
```

^b278

### Block 279

XML location: `/div[1]/div[1]/listBibl[1]/bibl[277]`.

```xml
<bibl xml:id="biblzh-tw_n51-55" xml:lang="zh-TW">劉康，《對話的喧囂：巴赫汀文化理論評述》，台北：麥田，2005，二版。</bibl>
```

^b279

### Block 280

XML location: `/div[1]/div[1]/listBibl[1]/bibl[278]`.

```xml
<bibl xml:id="biblzh-tw_n49" xml:lang="zh-TW">劉康，《對話的喧聲：巴赫汀文化理論述評》，台北：麥田，2005，頁20-23。</bibl>
```

^b280

### Block 281

XML location: `/div[1]/div[1]/listBibl[1]/bibl[279]`.

```xml
<bibl xml:id="DIC-LDOCE">
        <title>Longman Dictionary of Contemporary English</title>. <pubPlace>Harlow,
          Essex</pubPlace>: <publisher>Longman</publisher> (<date>1978</date>). </bibl>
```

^b281

### Block 282

XML location: `/div[1]/div[1]/listBibl[1]/bibl[280]`.

```xml
<bibl xml:id="fr-ex-Roman-Rose" xml:lang="fr"><author>Lorris, Guillaume de</author> et
          <author>Meun, Jean de</author><title>Le Roman de la Rose</title>, <date>1230,
          1270-1285</date>.</bibl>
```

^b282

### Block 283

XML location: `/div[1]/div[1]/listBibl[1]/bibl[281]`.

```xml
<bibl xml:id="FTGRA-eg-16"><author>Lowe, David</author>. <title level="m">Lost
        Chicago</title>, <pubPlace>Boston</pubPlace>: <publisher>Houghton Mifflin</publisher>,
          (<date>1978</date>), <biblScope unit="pp">p.30</biblScope>.
        <!--<biblScope unit="part">top. Ex libris Wendy Plotkin</biblScope>--></bibl>
```

^b283

### Block 284

XML location: `/div[1]/div[1]/listBibl[1]/bibl[282]`.

```xml
<bibl xml:id="lowellAut"><author>Lowell, Amy</author>. <title>Autumn
          haze</title>.(<date>1919</date>). </bibl>
```

^b284

### Block 285

XML location: `/div[1]/div[1]/listBibl[1]/bibl[283]`.

```xml
<bibl xml:id="fr-ex-Lichtig" xml:lang="fr"><author>Lucie Lichtig</author>, <title level="a">M.
          Klein de Joseph Losey : script</title>, . <title level="j">l'Avant-scène cinéma</title>,
          <num>n° 175</num>, <date>nov. 1976</date>. </bibl>
```

^b285

### Block 286

XML location: `/div[1]/div[1]/listBibl[1]/bibl[284]`.

```xml
<bibl xml:id="SASE-eg-41"><author>Luther, Martin</author> [tr]. <title level="m">Die gantze
          Heilige Schrifft Deudsch, Wittenberg 1545. Letzte zu Luthers Lebzeiten erchienene Ausgabe,
          hsg. Hans Volz unter Mitarbeit von Heinz Blanke. Textredaktion Friedrich Kur</title>,
          <pubPlace>München</pubPlace>: <publisher>Rogner &amp; Bernhard</publisher>,
          <date>1972</date>.</bibl>
```

^b286

### Block 287

XML location: `/div[1]/div[1]/listBibl[1]/bibl[285]`.

```xml
<bibl xml:id="biblzh-tw_n2" xml:lang="zh-TW">《論語》卷七：憲問第十四。</bibl>
```

^b287

### Block 288

XML location: `/div[1]/div[1]/listBibl[1]/bibl[286]`.

```xml
<bibl xml:id="biblzh-tw_n6" xml:lang="zh-TW"> 羅貫中，《三國演義》。</bibl>
```

^b288

### Block 289

XML location: `/div[1]/div[1]/listBibl[1]/bibl[287]`.

```xml
<bibl xml:id="biblzh-tw_n9" xml:lang="zh-TW">魯迅，《狂人日記 》。</bibl>
```

^b289

### Block 290

XML location: `/div[1]/div[1]/listBibl[1]/bibl[288]`.

```xml
<bibl xml:id="biblzh-tw_n15" xml:lang="zh-TW">魯迅，《狂人日記》。</bibl>
```

^b290

### Block 291

XML location: `/div[1]/div[1]/listBibl[1]/bibl[289]`.

```xml
<bibl xml:id="biblzh-tw_n16" xml:lang="zh-TW">魯迅，《狂人日記》。</bibl>
```

^b291

### Block 292

XML location: `/div[1]/div[1]/listBibl[1]/bibl[290]`.

```xml
<bibl xml:id="VERH-eg-27"><author>MacNeice, Louis</author>. <title level="a">The Sunlight on
          the Garden</title> In <editor>E.R. Dodds, </editor>
        <title level="m">The collected poems of Louis MacNeice</title>, <pubPlace>London</pubPlace>:
          <publisher>Faber</publisher>, <date>1966</date>.</bibl>
```

^b292

### Block 293

XML location: `/div[1]/div[1]/listBibl[1]/bibl[291]`.

```xml
<bibl xml:id="TSBA-eg-19"> Examples from <author>MacWhinney, Brian</author>, <biblScope unit="part">88, 87</biblScope>, cited by <author>Johansson, S. </author>
        <title level="a">The approach of the Text Encoding Initiative to the encoding of spoken
          discourse</title> In <editor>Leech, G.</editor>, <editor>G. Myers</editor>, <editor>J.
          Thomas</editor> eds. <title level="m">Spoken English on Computer: Transcription, Markup
          and Applications</title>. <pubPlace>Harlow</pubPlace>: <publisher>Longman</publisher>,
          <date>1995</date>.</bibl>
```

^b293

### Block 294

XML location: `/div[1]/div[1]/listBibl[1]/bibl[292]`.

```xml
<bibl xml:id="MS-eg-001">
        <author>Madan, Falconer, et al</author>, <title>A summary catalogue of western manuscripts
          in the Bodleian Library at Oxford which have not hitherto been catalogued ... </title>
        <pubPlace>Oxford</pubPlace>, <date>1895-1953</date>. <biblScope> 5: 515</biblScope>.
          <note>Cited in <bibl>Driscoll, M.J. <title level="a">P5-MS: A general purpose tagset for
              manuscript description</title> in <title level="j">Digital Medievalist</title>:
              <biblScope>2.1</biblScope>, <date>(2006)</date></bibl></note>
      </bibl>
```

^b294

### Block 295

XML location: `/div[1]/div[1]/listBibl[1]/bibl[293]`.

```xml
<bibl xml:id="fr-ex-Maingeneau_Analyser" xml:lang="fr"><author>Maingeneau, Dominique</author>,
          <title>Analyser les textes de communication</title>, <date>2007</date>.</bibl>
```

^b295

### Block 296

XML location: `/div[1]/div[1]/listBibl[1]/bibl[294]`.

```xml
<bibl xml:id="CONARS-eg-106">Any issue of the <title level="j">Malawi Daily Times.
        </title></bibl>
```

^b296

### Block 297

XML location: `/div[1]/div[1]/listBibl[1]/bibl[295]`.

```xml
<bibl xml:id="fr-ex-Zazie" xml:lang="fr"><author>Malle, Louis</author>, <title level="a">Zazie
          dans le métro : script</title>, <title level="j">l'Avant-scène cinéma</title>, <num>n°
          104</num>, <date>juin 1970</date>.</bibl>
```

^b297

### Block 298

XML location: `/div[1]/div[1]/listBibl[1]/bibl[296]`.

```xml
<bibl xml:id="fr-ex-Manu_Shan" xml:lang="fr">
        <author>Manuélian, Hélène</author>, <author>Schang, Emmanuel</author>, <title>XML, DTD et
          TEI pour un dictionnaire étymologique des créoles</title>, <ref target="http://www.dicorevue.fr/bilingues/10-07_deca_5.html/">édition électronique</ref>,
          <date>12 Octobre 2007</date>. </bibl>
```

^b298

### Block 299

XML location: `/div[1]/div[1]/listBibl[1]/bibl[297]`.

```xml
<bibl xml:id="PH-BIBL-1">
        <title level="a">The Manere of Good Lyuynge</title>: fol. 126v of Bodleian MS Laud Misc 517;
        in <ptr target="#PARKES"/>, p.8. </bibl>
```

^b299

### Block 300

XML location: `/div[1]/div[1]/listBibl[1]/bibl[298]`.

```xml
<bibl xml:id="STGA-eg-10"><title>Marbury v. Madison</title>, <biblScope unit="part">1 Cranch,
          137</biblScope> (<date>1803</date>), rpt. In <editor>H. S. Commager</editor>, ed., <title level="m">Documents of American History</title>, <edition> 5th ed</edition>
        <series>Crofts American history series</series>. <pubPlace>New York</pubPlace>:
          <publisher>Appleton-Century-Crofts</publisher>, <date>1949</date>,
          <biblScope>p.192</biblScope>.</bibl>
```

^b300

### Block 301

XML location: `/div[1]/div[1]/listBibl[1]/bibl[299]`.

```xml
<bibl xml:id="COEDADD-eg-85"><author>Marvell, Andrew</author>. <title level="m">An Horatian
          Ode</title>, Bod. MS Eng. Poet d.49.</bibl>
```

^b301

### Block 302

XML location: `/div[1]/div[1]/listBibl[1]/bibl[300]`.

```xml
<bibl xml:id="fr-ex-Mauriac-Marquise" xml:lang="fr"><author>Mauriac, Claude</author>, <title>
          La Marquise sortit à cinq heures</title>, <date>1961</date>.</bibl>
```

^b302

### Block 303

XML location: `/div[1]/div[1]/listBibl[1]/bibl[301]`.

```xml
<bibl xml:id="fr-ex-Mauss_Sociologie" xml:lang="fr"><author>Mauss, Marcel</author>,
          <title>Sociologie et anthropologie</title>, <date>1950</date>.</bibl>
```

^b303

### Block 304

XML location: `/div[1]/div[1]/listBibl[1]/bibl[302]`.

```xml
<bibl xml:id="NDGEOGste-Falls"><author>McCarthy, Niall</author>, <title level="a">No
          Parachute: The Highest Falls People Survived</title>, <title level="m">Statista</title>,
          <date when="2020-11-18">November 18, 2020</date>. <ptr target="https://www.statista.com/chart/19708/known-occasions-where-people-survived-falls/"/>. </bibl>
```

^b304

### Block 305

XML location: `/div[1]/div[1]/listBibl[1]/bibl[303]`.

```xml
<bibl xml:id="SOURCE-eg-01"><author>McCarty, Willard</author>. <title level="a">Introduction</title> in <title level="m">Collaborative Research in the Digital
          Humanities</title>: A volume in honour of Harold Short on the occasion of his 65th
        birthday, September 2010, ed. <editor>Marilyn Deegan</editor> and <editor>Willard
          McCarty</editor>. <pubPlace>London</pubPlace>: <publisher>Ashgate</publisher>
          (<date>2012</date>).</bibl>
```

^b305

### Block 306

XML location: `/div[1]/div[1]/listBibl[1]/bibl[304]`.

```xml
<bibl xml:id="DSHD-eg-30"><author>Melville, Herman</author>, <title level="m">Moby
          Dick</title>. (<date>1851</date>).</bibl>
```

^b306

### Block 307

XML location: `/div[1]/div[1]/listBibl[1]/bibl[305]`.

```xml
<bibl xml:id="fr-ex-Mendes-France" xml:lang="fr"><author>Mendès-France, Pierre</author>,
          <title> Œuvres complètes</title>, <date>1984-1985</date>.</bibl>
```

^b307

### Block 308

XML location: `/div[1]/div[1]/listBibl[1]/bibl[306]`.

```xml
<bibl xml:id="biblzh-tw_n1" xml:lang="zh-TW">《孟子》〈三十三〉。 </bibl>
```

^b308

### Block 309

XML location: `/div[1]/div[1]/listBibl[1]/bibl[307]`.

```xml
<bibl xml:id="DRPERF-eg-12">
        <author>Miller, Henry</author>. <title level="a">Death of a Salesman</title> in
          <editor>Atkinson, Brooks, </editor>
        <title level="m">New Voices in the American Theatre</title>, <pubPlace>New York</pubPlace>:
          <publisher>Modern Library</publisher>, <date>1955</date>, <biblScope unit="pp">p.113</biblScope>.</bibl>
```

^b309

### Block 310

XML location: `/div[1]/div[1]/listBibl[1]/bibl[308]`.

```xml
<bibl xml:id="COHQHE-eg-11">
        <author>Milne, A. A. </author>
        <title level="m">The House at Pooh Corner</title>. <pubPlace>London</pubPlace>:
          <publisher>Methuen &amp; Co.</publisher>, <date>1928</date>, <biblScope unit="pp">p.
          83</biblScope>.</bibl>
```

^b310

### Block 311

XML location: `/div[1]/div[1]/listBibl[1]/bibl[309]`.

```xml
<bibl xml:id="CO-eg-06">
        <author>Milton, John</author>. <title>Paradise Lost: A poem in X books</title>
          (<date>1667</date>), <biblScope>I, 1-10</biblScope>. </bibl>
```

^b311

### Block 312

XML location: `/div[1]/div[1]/listBibl[1]/bibl[310]`.

```xml
<bibl xml:id="miltPo"><author>Milton, John</author>. <title>Poems of Mr John Milton, both
          English and Latin...</title> (<date>1645</date>). </bibl>
```

^b312

### Block 313

XML location: `/div[1]/div[1]/listBibl[1]/bibl[311]`.

```xml
<bibl xml:id="fr-ex-Moliere_Ecole" xml:lang="fr"><author>Molière</author>, <title>L'École des
          femmes</title>,<date> 1663</date>.</bibl>
```

^b313

### Block 314

XML location: `/div[1]/div[1]/listBibl[1]/bibl[312]`.

```xml
<bibl xml:id="fr-ex-Moliere_Med" xml:lang="fr"><author>Molière</author>, <title>Le Médecin
          malgré lui</title>, <date>1667</date>.</bibl>
```

^b314

### Block 315

XML location: `/div[1]/div[1]/listBibl[1]/bibl[313]`.

```xml
<bibl xml:id="fr-ex-Moliere_Med_Vol" xml:lang="fr"><author>Molière</author>, <title>Le Médecin
          volant</title>, <date>1673</date>.</bibl>
```

^b315

### Block 316

XML location: `/div[1]/div[1]/listBibl[1]/bibl[314]`.

```xml
<bibl xml:id="fr-ex-Montaigne_Essais" xml:lang="fr"><author>Montaigne, Michel de</author>,
          <title>Essais</title>, <date>1592</date>.</bibl>
```

^b316

### Block 317

XML location: `/div[1]/div[1]/listBibl[1]/bibl[315]`.

```xml
<bibl xml:id="fr-ex-Montesquieu" xml:lang="fr"><author>Montesquieu, Charles-Louis de Secondat,
          baron de la Brède et de</author>, <title> Lettres persanes</title>,
        <date>1721</date>.</bibl>
```

^b317

### Block 318

XML location: `/div[1]/div[1]/listBibl[1]/bibl[316]`.

```xml
<bibl xml:id="fr-ex-Montherlant-Pitie" xml:lang="fr"><author>Montherlant, Henry de </author>,
          <title>Pitié pour les femmes</title>, <date>1936</date>.</bibl>
```

^b318

### Block 319

XML location: `/div[1]/div[1]/listBibl[1]/bibl[317]`.

```xml
<bibl xml:id="PH-eg-03">
        <author>Moore, George</author>. Autograph manuscript of <title>Memoirs of my dead
          life</title>, Pierpont Morgan MA 3421; in <ptr target="#KLINKENBORG"/></bibl>
```

^b319

### Block 320

XML location: `/div[1]/div[1]/listBibl[1]/bibl[318]`.

```xml
<bibl xml:id="PH-eg-09">
        <author>Moore, Thomas</author>. Autograph manuscript of the second version of <title>Lalla
          Rookh</title>, Pierpont Morgan MA 310; in <ptr target="#KLINKENBORG"/> 23. </bibl>
```

^b320

### Block 321

XML location: `/div[1]/div[1]/listBibl[1]/bibl[319]`.

```xml
<bibl xml:id="CO-eg-04">
        <author>Moreland, Floyd L.</author> and <author>Rita M. Fleischer</author>. <title>Latin: An
          Intensive Course, </title> (<date>1977</date>) <biblScope>p.53</biblScope>. </bibl>
```

^b321

### Block 322

XML location: `/div[1]/div[1]/listBibl[1]/bibl[320]`.

```xml
<bibl xml:id="COBICOR-eg-251">
        <title>Des Minnesangs Frühling</title>, <editor>Moser, Hugo</editor>, <editor>Helmut
          Tervooren</editor> eds. <edition>36., neugestaltete und erweiterte Auflage</edition>
        <biblScope unit="vol">I Texte</biblScope>, <pubPlace>Stuttgart</pubPlace>: <publisher>S.
          Hirzel Verlag</publisher>, <date>1977</date>.</bibl>
```

^b322

### Block 323

XML location: `/div[1]/div[1]/listBibl[1]/bibl[321]`.

```xml
<bibl xml:id="msph1sup-wtrmrk"><author>Mošin, Vladimir A</author>. <title level="m">Anchor
          Watermarks</title>. <pubPlace>Amsterdam</pubPlace>: <publisher>Paper Publications Society
          (Labarre Foundation)</publisher>, <date>1973</date>. <series>Monumenta Chartæ Papyraceæ
          Historiam Illustrantia</series>; <biblScope unit="volume" n="13">v. 13</biblScope>.</bibl>
```

^b323

### Block 324

XML location: `/div[1]/div[1]/listBibl[1]/bibl[322]`.

```xml
<bibl xml:id="fr-ex-Mrejen_Eau" xml:lang="fr"><author>Mréjen, Valérie</author>, <title>Eau
          sauvage</title>, <date>2004</date>.</bibl>
```

^b324

### Block 325

XML location: `/div[1]/div[1]/listBibl[1]/bibl[323]`.

```xml
<bibl xml:id="SA-eg-04">
        <title level="a">Zuigan calls himself "Master"</title>. <author>Mumon Ekai</author>. (In
          <title level="m">The Gateless Gate</title>, Case 12.) </bibl>
```

^b325

### Block 326

XML location: `/div[1]/div[1]/listBibl[1]/bibl[324]`.

```xml
<bibl xml:id="fr-ex-Hydraul" xml:lang="fr"><editor>Mustafa Siddik Altinakar</editor>,
          <editor>René Walther</editor> (éds.), <title>Hydraulique fluviale. Tome 16, Écoulement et
          phénomènes de transport dans les canaux à géométrie simple </title>,
        <date>2008</date>.</bibl>
```

^b326

### Block 327

XML location: `/div[1]/div[1]/listBibl[1]/bibl[325]`.

```xml
<bibl xml:id="fr-ex-Tunis" xml:lang="fr"><editor>Mégnin, Michel</editor> (éd.), <title>Tunis
          1900 Lehnert &amp; Landrock photographes</title>,<date>2005</date>.</bibl>
```

^b327

### Block 328

XML location: `/div[1]/div[1]/listBibl[1]/bibl[326]`.

```xml
<bibl xml:id="PNIN1">
        <author>Nabokov, Vladimir</author>
        <title>Pnin</title> (1953) <biblScope>, p.14 </biblScope><!--of 1967 Avon pb reprinting-->
      </bibl>
```

^b328

### Block 329

XML location: `/div[1]/div[1]/listBibl[1]/bibl[327]`.

```xml
<bibl xml:id="DIC-NPEG">
        <title>The New Penguin English Dictionary</title>. <pubPlace>London</pubPlace>:
          <publisher>Penguin Books</publisher> (<date>1986</date>). </bibl>
```

^b329

### Block 330

XML location: `/div[1]/div[1]/listBibl[1]/bibl[328]`.

```xml
<bibl xml:id="NZPaV01NgaK"> Derived from <author>New Zealand Parliament, Legislative
          Council</author>. <title>Nga Korero Paramete: 1881-1885</title> (<series><title>New
            Zealand Electronic Text Collection</title></series>). <date>2008</date>
        <pubPlace>Wellington, New Zealand</pubPlace>. <ptr target="https://nzetc.victoria.ac.nz/tei-source/NZPaV01NgaK.xml"/>. </bibl>
```

^b330

### Block 331

XML location: `/div[1]/div[1]/listBibl[1]/bibl[329]`.

```xml
<bibl xml:id="NJAL">
        <title level="m">Njal's saga</title>. tr. <editor>Magnus Magnusson and Hermann
          Palsson</editor>. <publisher>Penguin</publisher>. (<date>1960</date>), <biblScope>chapter
          12, p.60</biblScope>.</bibl>
```

^b331

### Block 332

XML location: `/div[1]/div[1]/listBibl[1]/bibl[330]`.

```xml
<bibl xml:id="DR-eg-07">
        <author>O'Casey, Sean</author>. <title>Time to go</title> (<date>1951</date>). </bibl>
```

^b332

### Block 333

XML location: `/div[1]/div[1]/listBibl[1]/bibl[331]`.

```xml
<bibl xml:id="fr-ex-Ollagnier_Main" xml:lang="fr"><author>Ollagnier, Jeanne</author>,
          <title>Main</title>, <date>2008</date>.</bibl>
```

^b333

### Block 334

XML location: `/div[1]/div[1]/listBibl[1]/bibl[332]`.

```xml
<bibl xml:id="ND-eg-99"> Herodotus. <title>On Libya</title>, from the
        <title>Histories</title>. </bibl>
```

^b334

### Block 335

XML location: `/div[1]/div[1]/listBibl[1]/bibl[333]`.

```xml
<bibl xml:id="CH-eg-01">
        <title>[Letter of Capt. E. Hopkins. Providence, 10 Sep 1764] </title>
      </bibl>
```

^b335

### Block 336

XML location: `/div[1]/div[1]/listBibl[1]/bibl[334]`.

```xml
<bibl xml:id="WHITMS1">"[I am a curse]" in <title>Original Manuscript Drafts for the Song of
          Myself</title>, Collection MSS3829, part of the Papers of Walt Whitman, Clifton Waller
        Barrett Library of American Literature, Albert and Shirley Small Special Collections
        Library, University of Virginia. </bibl>
```

^b336

### Block 337

XML location: `/div[1]/div[1]/listBibl[1]/bibl[335]`.

```xml
<bibl xml:id="fr-ex-Ormesson-douane" xml:lang="fr"><author>Ormesson, Jean d'</author>, <title level="m">La Douane de mer</title>, <date>1993</date>.</bibl>
```

^b337

### Block 338

XML location: `/div[1]/div[1]/listBibl[1]/bibl[336]`.

```xml
<bibl xml:id="SA-eg-03">
        <author>Orwell, George</author>. <title>Nineteen-Eighty-Four</title>.
          <pubPlace>London</pubPlace>: <publisher>Gollancz</publisher> (<date>1949</date>). </bibl>
```

^b338

### Block 339

XML location: `/div[1]/div[1]/listBibl[1]/bibl[337]`.

```xml
<bibl xml:lang="ja" xml:id="ja-ritsuryo-weights">
        <author>大隅亜希子</author>. <date when="1996">1996</date>. <title level="a">律令制下における権衡普及の実態:
          海産物の貢納単位を中心として</title>. <title level="j">史論</title>
        <biblScope unit="issue">49</biblScope>. <biblScope unit="pp">pp. 22–44</biblScope>. <ptr target="http://id.nii.ac.jp/1632/00015761/"/>. </bibl>
```

^b339

### Block 340

XML location: `/div[1]/div[1]/listBibl[1]/bibl[338]`.

```xml
<bibl xml:id="PH-eg-16">
        <author>Owen, Wilfred</author>. <title>Dulce et decorum est</title>, from autograph
        manuscript in the English Faculty Library, Oxford University. </bibl>
```

^b340

### Block 341

XML location: `/div[1]/div[1]/listBibl[1]/bibl[339]`.

```xml
<bibl xml:id="COEDADD-eg-90">
        <author>Owenson, Sydney</author>. <title level="m">The Wild Irish Girl</title>. Ed.
          <editor>Kathryn Kirkpatrick</editor>. <pubPlace>Oxford</pubPlace>: <publisher>Oxford
          University Press</publisher>, <date>1999</date>, <biblScope unit="page">p. 17</biblScope>. </bibl>
```

^b341

### Block 342

XML location: `/div[1]/div[1]/listBibl[1]/bibl[340]`.

```xml
<bibl xml:id="biblzh-tw_n39" xml:lang="zh-TW">擺夷文經，中央研究院歷史語言研究所 。 </bibl>
```

^b342

### Block 343

XML location: `/div[1]/div[1]/listBibl[1]/bibl[341]`.

```xml
<bibl xml:id="fr-ex-Pascal_Pensees" xml:lang="fr"><author>Pascal, Blaise</author>, <title level="a">Le Mémorial</title>, in <title level="m">Pensées</title>,<date>1670</date>.</bibl>
```

^b343

### Block 344

XML location: `/div[1]/div[1]/listBibl[1]/bibl[342]`.

```xml
<bibl xml:id="TSSASE-eg-37">
        <author>Payne, J. </author>
        <title level="a">Report on the compatibility of J P French's spoken corpus transcription
          conventions with the TEI guidelines for transcription of spoken texts</title>, <title level="m">Working Paper</title>, <date>Dec 1992</date>, NERC WP8/WP4 122.</bibl>
```

^b344

### Block 345

XML location: `/div[1]/div[1]/listBibl[1]/bibl[343]`.

```xml
<bibl xml:id="CODR-eg-296">
        <author>Peacock, Thomas Love</author>. <title level="m">Gryll Grange</title>
          (<date>1861</date>), <biblScope unit="chap">chapter 1</biblScope>.</bibl>
```

^b345

### Block 346

XML location: `/div[1]/div[1]/listBibl[1]/bibl[344]`.

```xml
<bibl xml:id="fr-ex-Pennac_Marchande" xml:lang="fr"><author>Pennac, Daniel </author>,
          <title>La Petite marchande de prose</title>, <date>1978</date>.</bibl>
```

^b346

### Block 347

XML location: `/div[1]/div[1]/listBibl[1]/bibl[345]`.

```xml
<bibl xml:id="fr-ex-Perec-esp" xml:lang="fr"><author>Perec, Georges</author>, <title>Espèces
          d'espaces</title>, <date>1974</date>.</bibl>
```

^b347

### Block 348

XML location: `/div[1]/div[1]/listBibl[1]/bibl[346]`.

```xml
<bibl xml:id="fr-ex-Perec-vie" xml:lang="fr"><author>Perec, Georges</author>, <title>La Vie
          mode d'emploi : romans</title>, <date>1978</date>.</bibl>
```

^b348

### Block 349

XML location: `/div[1]/div[1]/listBibl[1]/bibl[347]`.

```xml
<bibl xml:id="fr-ex-Perec-choses" xml:lang="fr"><author>Perec, Georges </author>, <title>Les
          Choses</title>, <date>1965</date>.</bibl>
```

^b349

### Block 350

XML location: `/div[1]/div[1]/listBibl[1]/bibl[348]`.

```xml
<bibl xml:id="GDFT-eg-12"><title level="a">Partial family tree for Bertrand Russell</title>
        based on an example in <author>Pereira, Fernando C.N.</author> and <author>Stuart M.
          Shieber</author>, <title level="m">Prolog and Natural Language Analysis</title>,
          <pubPlace>Stanford</pubPlace>: <publisher>Center for the Study of Language and
          Information</publisher>. (<date>1987</date>), <biblScope unit="pp">p.22</biblScope>.</bibl>
```

^b350

### Block 351

XML location: `/div[1]/div[1]/listBibl[1]/bibl[349]`.

```xml
<bibl xml:id="fr-ex-Pernoud-femme" xml:lang="fr"><author>Pernoud, Régine</author>, <title>La
          Femme au temps des Cathédrales</title>, <date>1982</date>.</bibl>
```

^b351

### Block 352

XML location: `/div[1]/div[1]/listBibl[1]/bibl[350]`.

```xml
<bibl xml:id="vcard"><author>Perreault, Simon</author>, <title>vCard Format
          Specification</title>
        <publisher>Internet Engineering Task Force (IETF)</publisher> (<date>2011</date>). <ptr target="https://datatracker.ietf.org/doc/html/rfc6350"/>.</bibl>
```

^b352

### Block 353

XML location: `/div[1]/div[1]/listBibl[1]/bibl[351]`.

```xml
<bibl xml:id="DIC-PLC">
        <title>Petit Larousse en Couleurs</title>. <pubPlace>Paris</pubPlace>:
          <publisher>Larousse</publisher>, (<date>1990</date>). </bibl>
```

^b353

### Block 354

XML location: `/div[1]/div[1]/listBibl[1]/bibl[352]`.

```xml
<bibl xml:id="PHILIPOTT">
        <author>Philipott, Thomas</author>
        <title>Poems.</title> (<date>1646</date>). </bibl>
```

^b354

### Block 355

XML location: `/div[1]/div[1]/listBibl[1]/bibl[353]`.

```xml
<bibl xml:id="NH-eg-02">
        <author>Pinsky, Robert</author>. <title level="a">Essays on Psychiatrists</title> in <title level="m">Sadness and Happiness</title> (<date>1975</date>). </bibl>
```

^b355

### Block 356

XML location: `/div[1]/div[1]/listBibl[1]/bibl[354]`.

```xml
<bibl xml:id="toWhom-eg-1"><author>Pix, Mary</author>. <title>The False Friend</title>
          (<date>1699</date>).</bibl>
```

^b356

### Block 357

XML location: `/div[1]/div[1]/listBibl[1]/bibl[355]`.

```xml
<bibl xml:id="PHOM-eg-secl"><author>Plautus, Titus Macchius</author>. <title>Asinaria, or the
          Comedy of Asses</title>. Edited and translated by <author>Wolfgang de Melo</author>. Loeb
        Classical Library 60. <pubPlace>Cambridge, MA</pubPlace>: <publisher>Harvard University
          Press</publisher> (<date>2011</date>).</bibl>
```

^b357

### Block 358

XML location: `/div[1]/div[1]/listBibl[1]/bibl[356]`.

```xml
<bibl xml:id="DRSP-eg-34"><author>Plautus, Titus Macchius</author>. <title level="m">Menaechmi</title>.</bibl>
```

^b358

### Block 359

XML location: `/div[1]/div[1]/listBibl[1]/bibl[357]`.

```xml
<bibl xml:id="fr-ex-Polac" xml:lang="fr"><author>Polac, Michel</author>, <title level="a">Un
          fils unique : script</title>, <title level="j">l'Avant-scène cinéma</title>, <num>n°
          99</num>, <date>janvier. 1970</date>.</bibl>
```

^b359

### Block 360

XML location: `/div[1]/div[1]/listBibl[1]/bibl[358]`.

```xml
<bibl xml:id="COHQHE-eg-12">
        <author>Pope, Alexander</author>. <title level="a">The Rape of the Lock</title>
          (<date>1714</date>) <biblScope unit="part">III.7</biblScope>.</bibl>
```

^b360

### Block 361

XML location: `/div[1]/div[1]/listBibl[1]/bibl[359]`.

```xml
<bibl xml:id="VEMEsamp-eg-14"><author>Pope, Alexander</author>. <title level="m">An Essay on
          Criticism</title> (<date>1711</date>).</bibl>
```

^b361

### Block 362

XML location: `/div[1]/div[1]/listBibl[1]/bibl[360]`.

```xml
<bibl xml:id="SAPTEG-eg-3"><author>Pope, Alexander</author>. <title>Dunciad Variorum</title>
          (<date>1729</date>), <biblScope unit="part">III.284</biblScope>.</bibl>
```

^b362

### Block 363

XML location: `/div[1]/div[1]/listBibl[1]/bibl[361]`.

```xml
<bibl xml:id="NDPLAC-eg-55">From letter 'JK' found in <title level="j">Poulson's Daily
          Advertiser, </title>
        <date>8 Oct 1835</date>.</bibl>
```

^b363

### Block 364

XML location: `/div[1]/div[1]/listBibl[1]/bibl[362]`.

```xml
<bibl xml:id="fr-ex-Proust-Swann" xml:lang="fr"><author>Proust, Marcel</author>, <title>A la
          recherche du temps perdu : Du côté de chez Swann</title>, <date>1913</date>.</bibl>
```

^b364

### Block 365

XML location: `/div[1]/div[1]/listBibl[1]/bibl[363]`.

```xml
<bibl xml:id="COHQQ-eg-23"><author>Queneau, Raymond</author>. <title level="m">Exercices de
          style</title>. <pubPlace>Paris</pubPlace>: <publisher>Gallimard</publisher>,
          (<date>1947</date>), <biblScope>p. 192</biblScope>.</bibl>
```

^b365

### Block 366

XML location: `/div[1]/div[1]/listBibl[1]/bibl[364]`.

```xml
<bibl xml:id="biblzh-tw_n52" xml:lang="zh-TW">瓊瑤，《還珠格格》。</bibl>
```

^b366

### Block 367

XML location: `/div[1]/div[1]/listBibl[1]/bibl[365]`.

```xml
<bibl xml:id="fr-ex-Queneau_Journ" xml:lang="fr"><author>Queneau, Raymond</author> ,
          <title>Journaux</title>, <date>1914-1965</date>.</bibl>
```

^b367

### Block 368

XML location: `/div[1]/div[1]/listBibl[1]/bibl[366]`.

```xml
<bibl xml:id="fr-ex-garg" xml:lang="fr"><author>Rabelais, François</author>.
          <title>Gargantua</title> Lyon, <date>1542</date></bibl>
```

^b368

### Block 369

XML location: `/div[1]/div[1]/listBibl[1]/bibl[367]`.

```xml
<bibl xml:id="rab3" xml:lang="fr"><author>Rabelais, François</author>
        <title>Tiers livre des faictz et dictz Heroïques du noble Pantagruel...</title>
          (<date>1546</date>), adapted from the website at <ptr target="http://www.bvh.univ-tours.fr/Epistemon/"/></bibl>
```

^b369

### Block 370

XML location: `/div[1]/div[1]/listBibl[1]/bibl[368]`.

```xml
<bibl xml:id="fr-ex-Renard_Journal" xml:lang="fr"><author>Renard, Jules</author>,
          <title>Journal : 1887-1910</title>, <date>1910</date>.</bibl>
```

^b370

### Block 371

XML location: `/div[1]/div[1]/listBibl[1]/bibl[369]`.

```xml
<bibl xml:id="COBICOI-eg-264">Reference from the bibliography in <author>Reps, Thomas
          William</author> and <author>Teitelbaum, Tim</author> eds. <title level="m">The
          Synthesizer Generator: A system for constructing language-based editors</title>,
          <pubPlace>New York</pubPlace> and <pubPlace>Berlin</pubPlace>:
          <publisher>Springer-Verlag</publisher>, <date>1989</date>, <biblScope unit="pp">p.304</biblScope>.</bibl>
```

^b371

### Block 372

XML location: `/div[1]/div[1]/listBibl[1]/bibl[370]`.

```xml
<bibl xml:id="biblzh-tw_n45" xml:lang="zh-TW">日本法隆寺貝葉心經 (Wikipedia Sept 2008).</bibl>
```

^b372

### Block 373

XML location: `/div[1]/div[1]/listBibl[1]/bibl[371]`.

```xml
<bibl xml:id="COHTGEG-eg-02"><author>Richardson, Samuel</author>. <title level="m">Clarissa;
          or the History of a Young Lady</title> (<date>1748</date>), <biblScope unit="vol">2</biblScope> Letter XIV.</bibl>
```

^b373

### Block 374

XML location: `/div[1]/div[1]/listBibl[1]/bibl[372]`.

```xml
<bibl xml:id="DIC-PR">
        <editor>Robert, Paul</editor>. <title>Le Petit Robert</title>. <pubPlace>Paris</pubPlace>:
          <publisher>Dictionnaires Le Robert</publisher> (<date>1967</date>). </bibl>
```

^b374

### Block 375

XML location: `/div[1]/div[1]/listBibl[1]/bibl[373]`.

```xml
<bibl xml:id="fr-ex-Rohmer-Maud" xml:lang="fr"><author>Rohmer, Eric</author>, <title level="a">Ma nuit chez Maud : script</title>, <title level="j">l'Avant-scène cinéma</title>,
          <num>n°98</num>, <date>2001</date>.</bibl>
```

^b375

### Block 376

XML location: `/div[1]/div[1]/listBibl[1]/bibl[374]`.

```xml
<bibl xml:id="fr-ex-Knock" xml:lang="fr"><author>Romains, Jules</author>, <title>
          Knock</title>, <date>1923</date>. </bibl>
```

^b376

### Block 377

XML location: `/div[1]/div[1]/listBibl[1]/bibl[375]`.

```xml
<bibl xml:id="fr-ex-Cyrano" xml:lang="fr"><author>Rostand, Edmond</author>, <title>Cyrano de
          Bergerac</title>, <date>1898</date>.</bibl>
```

^b377

### Block 378

XML location: `/div[1]/div[1]/listBibl[1]/bibl[376]`.

```xml
<bibl xml:id="fr-ex-Roubaud_Boucle" xml:lang="fr"><author>Roubaud, Jacques</author>, <title>La
          Boucle</title>, <date>1993</date>.</bibl>
```

^b378

### Block 379

XML location: `/div[1]/div[1]/listBibl[1]/bibl[377]`.

```xml
<bibl xml:id="COHQQ-eg-35"><author>Rowling, J. K.</author>
        <title level="a">The Sorting Hat</title>. In <title level="m">Harry Potter and the
          Sorcerer's Stone</title>, <pubPlace>New York</pubPlace>: <publisher>Scholastic,
          Inc.</publisher> (<date>1999</date>), <biblScope unit="chap">chapter 7</biblScope>,
          <biblScope unit="pp">p. 121</biblScope>.</bibl>
```

^b379

### Block 380

XML location: `/div[1]/div[1]/listBibl[1]/bibl[378]`.

```xml
<bibl xml:id="AI-eg-01">
        <title level="m">The Saga of the Volsungs: the Norse epic of Sigurd the Dragon
          Slayer</title>. trans. <editor role="tr">Jesse L. Byock</editor>. <publisher>University of
          California Press</publisher> (<date>1990</date>). </bibl>
```

^b380

### Block 381

XML location: `/div[1]/div[1]/listBibl[1]/bibl[379]`.

```xml
<bibl xml:id="fr-ex-Sanctoral-ee" xml:lang="fr"><title>Le Sanctoral du lectionnaire de
          l'office dominicain (ms. Rome, Sainte-Sabine XIV L 1, f.142r et 189r-230v, Ecclesiasticum
          officium secundum ordinem fratrum praedicatorum)</title>, <ref target="http://elec.enc.sorbonne.fr/sanctoral/">édition électronique</ref> par
          l'<editor>Ecole nationale des chartes</editor>, d'après l'édition d'<editor>Anne-Élisabeth
          Urfels-Capot</editor> (Paris : Ecole nationale des chartes, 2007).</bibl>
```

^b381

### Block 382

XML location: `/div[1]/div[1]/listBibl[1]/bibl[380]`.

```xml
<bibl xml:id="WD-VERT-IND" xml:lang="ja">
        <author>崎山理</author>. <date>1985</date>
        <title level="a">インドネシア語</title>. <title level="s">講座日本語学</title>
        <edition>11</edition>. <title level="m">外国語との対照II</title>.
          <pubPlace>東京</pubPlace>:<publisher>明治書院</publisher>
        <biblScope unit="pp">61-80</biblScope>
      </bibl>
```

^b382

### Block 383

XML location: `/div[1]/div[1]/listBibl[1]/bibl[381]`.

```xml
<bibl xml:id="biblzh-tw_n7" xml:lang="zh-TW">三毛，〈沙漠中的飯店〉，《撒哈拉的故事》。 </bibl>
```

^b383

### Block 384

XML location: `/div[1]/div[1]/listBibl[1]/bibl[382]`.

```xml
<bibl xml:id="biblzh-tw_n48" xml:lang="zh-TW"> 《三家詩鈔》，華培昌，藏於國家圖書館。</bibl>
```

^b384

### Block 385

XML location: `/div[1]/div[1]/listBibl[1]/bibl[383]`.

```xml
<bibl xml:id="COHTG-eg-44"><author>Sapir, Edward</author>. <title level="m"> Language: an
          introduction to the study of speech</title>, <pubPlace>New York</pubPlace>:
          <publisher>Harcourt, Brace and World</publisher>, <date>1921</date>, <biblScope unit="pp">p.79</biblScope>.</bibl>
```

^b385

### Block 386

XML location: `/div[1]/div[1]/listBibl[1]/bibl[384]`.

```xml
<bibl xml:id="DRPERF-eg-13.1"><author>Selby, Charles</author>. <title level="m">A Day in Paris. A farce in one act</title>, <pubPlace>London</pubPlace>: <publisher> T.H. Lacy</publisher>. (Lacy's Acting Edition, volume 69, No. 1025)</bibl>
```

^b386

### Block 387

XML location: `/div[1]/div[1]/listBibl[1]/bibl[385]`.

```xml
<bibl xml:id="fr-ex-Shakes-Richard-III" xml:lang="fr"><author>Shakespeare William</author>,
          <title>Richard III</title>, <date>1597</date>.</bibl>
```

^b387

### Block 388

XML location: `/div[1]/div[1]/listBibl[1]/bibl[386]`.

```xml
<bibl xml:id="FHENRY5"><author>Shakespeare, William</author>. <title level="m">Henry V</title>
        In <title level="m">Mr. William Shakespeares Comedies, Histories, &amp; Tragedies</title>,
          <pubPlace>London</pubPlace>: <publisher>Jaggard and Blount</publisher>,
        <date>1623</date>.</bibl>
```

^b388

### Block 389

XML location: `/div[1]/div[1]/listBibl[1]/bibl[387]`.

```xml
<bibl xml:id="THENRY5"><author>Shakespeare, William</author>. <title level="m">Henry V</title>
        In <title level="m">The Works of Shakespeare in seven volumes</title>, ed. <editor>Lewis
          Theobald</editor>, <pubPlace>London</pubPlace>: <publisher>Bettesworth, Hitch, Tonson et
          al</publisher>, (<date>1733</date>).</bibl>
```

^b389

### Block 390

XML location: `/div[1]/div[1]/listBibl[1]/bibl[388]`.

```xml
<bibl xml:id="CO-eg-07"><author>Shakespeare, William</author>. <title level="m">Antony and
          Cleopatra</title>, <biblScope unit="part">IV.4, 14-21</biblScope>. </bibl>
```

^b390

### Block 391

XML location: `/div[1]/div[1]/listBibl[1]/bibl[389]`.

```xml
<bibl xml:id="STGA-eg-6"><author>Shakespeare, William</author>. <title level="m">Merchant of
          Venice</title>, <biblScope unit="part">I.ii, speech 5 (Portia)</biblScope>.</bibl>
```

^b391

### Block 392

XML location: `/div[1]/div[1]/listBibl[1]/bibl[390]`.

```xml
<bibl xml:id="DR-eg-05"><author>Shakespeare, William</author>. <title level="m">Macbeth</title>, <biblScope unit="part">Act V, Scene 1</biblScope>.</bibl>
```

^b392

### Block 393

XML location: `/div[1]/div[1]/listBibl[1]/bibl[391]`.

```xml
<bibl xml:id="COEDCOR-eg-64"><author>Shakespeare, William</author>. <title level="m">Antony
          and Cleopatra</title> (<date>1623</date>), <biblScope unit="part">V.
        ii</biblScope>.</bibl>
```

^b393

### Block 394

XML location: `/div[1]/div[1]/listBibl[1]/bibl[392]`.

```xml
<bibl xml:id="CODR-eg-293"><author>Shakespeare, William</author>. <title level="a">Hamlet</title> In <editor>Stanley Wells</editor> and <editor>Gary Taylor</editor> eds.
          <title>The Complete Works</title>, <pubPlace>Oxford</pubPlace>: <publisher>Clarendon
          Press</publisher>, <date>1986</date>, <biblScope unit="part">I.i</biblScope>.</bibl>
```

^b394

### Block 395

XML location: `/div[1]/div[1]/listBibl[1]/bibl[393]`.

```xml
<bibl xml:id="CODR-eg-294"><author>Shakespeare, William</author>. <title level="m">Hamlet</title>, <pubPlace>London</pubPlace>:<publisher> Valentine Simmes</publisher>.
          (<date>1603</date>), <biblScope unit="part">I.i</biblScope>.</bibl>
```

^b395

### Block 396

XML location: `/div[1]/div[1]/listBibl[1]/bibl[394]`.

```xml
<bibl xml:id="CODR-eg-295"><author>Shakespeare, William</author>. <title level="a">The Tempest
        </title> In <title level="m">Mr. William Shakespeares Comedies, Histories, &amp;
          Tragedies</title>, <pubPlace>London</pubPlace>: <publisher>Jaggard and Blount</publisher>,
          (<date>1623</date>).</bibl>
```

^b396

### Block 397

XML location: `/div[1]/div[1]/listBibl[1]/bibl[395]`.

```xml
<bibl xml:id="TwN"><author>Shakespeare, William</author>. <title level="a">Twelfth Night, or
          What you Will </title> In <title level="m">Mr. William Shakespeares Comedies, Histories,
          &amp; Tragedies</title>, <pubPlace>London</pubPlace>: <publisher>Jaggard and
          Blount</publisher>, (<date>1623</date>).</bibl>
```

^b397

### Block 398

XML location: `/div[1]/div[1]/listBibl[1]/bibl[396]`.

```xml
<bibl xml:id="l-td-eg-1"><author>Shakespeare, William</author>, <title level="m">The
          Sonnets</title> (<date>1609</date>), <biblScope unit="part">18</biblScope>.</bibl>
```

^b398

### Block 399

XML location: `/div[1]/div[1]/listBibl[1]/bibl[397]`.

```xml
<bibl xml:id="VEST-eg-6"><author>Shakespeare, William</author>, <title level="m">The
          Sonnets</title> (<date>1609</date>), <biblScope unit="part">130</biblScope>.</bibl>
```

^b399

### Block 400

XML location: `/div[1]/div[1]/listBibl[1]/bibl[398]`.

```xml
<bibl xml:id="biblzh-tw_n33" xml:lang="zh-TW">莎士比亞，《終成眷屬 》。</bibl>
```

^b400

### Block 401

XML location: `/div[1]/div[1]/listBibl[1]/bibl[399]`.

```xml
<bibl xml:id="biblzh-tw_n35-36" xml:lang="zh-TW">莎士比亞，《馬克白》。</bibl>
```

^b401

### Block 402

XML location: `/div[1]/div[1]/listBibl[1]/bibl[400]`.

```xml
<bibl xml:id="SAWS"><title level="m">Sharing Ancient Wisdoms</title>, <date>2013</date>,
        available: <ptr target="http://www.ancientwisdoms.ac.uk/"/>.</bibl>
```

^b402

### Block 403

XML location: `/div[1]/div[1]/listBibl[1]/bibl[401]`.

```xml
<bibl xml:id="DR-eg-08"><author>Shaw, George Bernard</author>. <title level="a">Heartbreak
          House: a fantasia in the Russian manner on English themes</title>, 
        <title level="m">Heartbreak House, Great Catherine, and playlets of the war</title>. 
        <pubPlace>London</pubPlace>: <publisher>Constable &amp; co.</publisher>, <date>1919</date>.</bibl>
```

^b403

### Block 404

XML location: `/div[1]/div[1]/listBibl[1]/bibl[402]`.

```xml
<bibl xml:id="DRSP-eg-35"><author>Shaw, George Bernard</author>. <title level="a">Pygmalion</title>, 
        <title level="m">Androcles and the Lion; Overruled; Pygmalion</title>.
        <pubPlace>London</pubPlace>: <publisher>Constable &amp; co.</publisher>,  <date>1916</date>.</bibl>
```

^b404

### Block 405

XML location: `/div[1]/div[1]/listBibl[1]/bibl[403]`.

```xml
<bibl xml:id="SASE-eg-32"><author>Shields, David</author>. <title level="m">Dead
          Languages</title>, <publisher>HarperCollins Canada</publisher>/<publisher>Perennial
          Rack</publisher>, rpt. <date>1990</date>, <biblScope unit="pp">p.10</biblScope>.</bibl>
```

^b405

### Block 406

XML location: `/div[1]/div[1]/listBibl[1]/bibl[404]`.

```xml
<bibl xml:id="COHQHF-eg-8"><editor>Sinclair, John</editor> ed. <title level="m">Collins
          COBUILD English Language Dictionary</title>. <pubPlace>London</pubPlace> and
          <pubPlace>Glasgow</pubPlace>: <publisher>Collins</publisher>, (<date>1987</date>),
          <biblScope unit="pp">p. 337</biblScope> s.v. croissant.</bibl>
```

^b406

### Block 407

XML location: `/div[1]/div[1]/listBibl[1]/bibl[405]`.

```xml
<bibl xml:id="biblzh-tw_n32" xml:lang="zh-TW">京劇《四郎探母》，1947年梅蘭芳演出。</bibl>
```

^b407

### Block 408

XML location: `/div[1]/div[1]/listBibl[1]/bibl[406]`.

```xml
<bibl xml:id="DSBACK-eg-83"><author>Smith, Adam</author>. <title level="m">An Inquiry into the
          Nature and Causes of the Wealth of Nations</title>, <pubPlace>London</pubPlace>.
          (<date>1776</date>), <biblScope unit="part">index to vol. 1</biblScope>.</bibl>
```

^b408

### Block 409

XML location: `/div[1]/div[1]/listBibl[1]/bibl[407]`.

```xml
<bibl xml:id="PH-eg-10">
        <author>Smith, Sydney</author>. <title>Autograph letter</title>. In Pierpont Morgan library;
          <ptr target="#KLINKENBORG"/> 11. </bibl>
```

^b409

### Block 410

XML location: `/div[1]/div[1]/listBibl[1]/bibl[408]`.

```xml
<bibl xml:id="SMITHWM">
        <author>Smith, William</author>. <title level="m">A New Classical Dictionary of Greek and
          Roman Biography, Mythology, and Geography, Partly Based Upon the Dictionary of Greek and
          Roman Biography and Mythology</title>, <pubPlace>New York</pubPlace>: <publisher>Harper
          &amp; Brothers, Publishers</publisher>, <date>1860</date>, <biblScope unit="pp">1026</biblScope>. </bibl>
```

^b410

### Block 411

XML location: `/div[1]/div[1]/listBibl[1]/bibl[409]`.

```xml
<bibl xml:id="PH-eg-14">
        <author>Southey, Robert</author>. Autograph manuscript of <title>The Life of Cowper</title>.
        In Pierpont Morgan MA 412 (<ptr target="#KLINKENBORG"/> 15).</bibl>
```

^b411

### Block 412

XML location: `/div[1]/div[1]/listBibl[1]/bibl[410]`.

```xml
<bibl xml:id="DRCAST-eg-23"><author>Soyinka, Akinwande Oluwole Wole</author>. <title level="m">Madmen and Specialists</title>, <pubPlace>London</pubPlace>:
          <publisher>Methuen</publisher> (<date>1971</date>).</bibl>
```

^b412

### Block 413

XML location: `/div[1]/div[1]/listBibl[1]/bibl[411]`.

```xml
<bibl xml:id="VE-eg-01">
        <author>Spenser, Edmund</author>. <title level="m">The Faerie Queene: Disposed into twelue
          bookes, Fashioning XII. Morall vertues.</title> (<date>1596</date>). </bibl>
```

^b413

### Block 414

XML location: `/div[1]/div[1]/listBibl[1]/bibl[412]`.

```xml
<bibl xml:id="COHQHE-eg-13">
        <author>Sterne, Laurence</author>. <title level="m">The Life and Opinions of Tristram
          Shandy, Gentleman</title>. (<date>1760</date>).</bibl>
```

^b414

### Block 415

XML location: `/div[1]/div[1]/listBibl[1]/bibl[413]`.

```xml
<bibl xml:id="STOW">
        <author>Stow, John </author><title>A survey of the cities of London and Westminster:
          containing the original, antiquity, increase, modern estate and government of those
          cities. Written at first in the year MDXCVIII. By John Stow, citizen and native of London.
          ... Now lastly, corrected, improved, and very much enlarged: ... by John Strype, ... In
          six books. ... </title> (London c.1525 - London 1605). </bibl>
```

^b415

### Block 416

XML location: `/div[1]/div[1]/listBibl[1]/bibl[414]`.

```xml
<bibl xml:id="NYT1992"><author>Sudetic, Chuck </author><title>Serbs Tighten Grip On Eastern
          Bosnia. </title><title>New York Times, </title>
        <date>April 20, 1992</date>.
        <!--http://www.nytimes.com/1992/04/20/world/serbs-tighten-grip-on-eastern-bosnia.html--></bibl>
```

^b416

### Block 417

XML location: `/div[1]/div[1]/listBibl[1]/bibl[415]`.

```xml
<bibl xml:id="SUE"><title>SUEtheTrex, Twitter biography</title>. <ptr target="https://twitter.com/SUEtheTrex"/>. Accessed <date when="2020-03-25">March 25th,
          2020</date>.</bibl>
```

^b417

### Block 418

XML location: `/div[1]/div[1]/listBibl[1]/bibl[416]`.

```xml
<bibl xml:id="NDDATEA-eg-169"><editor>Sutherland, L.S.</editor> and <editor>L.G.
          Mitchell</editor> eds. <title level="m">The Eighteenth century</title>, <series>The
          History of the University of Oxford <biblScope unit="vol">V</biblScope>
        </series>, <biblScope unit="pp">p.178</biblScope>.</bibl>
```

^b418

### Block 419

XML location: `/div[1]/div[1]/listBibl[1]/bibl[417]`.

```xml
<bibl xml:id="biblzh-tw_n28" xml:lang="zh-TW">蘇童，《妻妾成群》。</bibl>
```

^b419

### Block 420

XML location: `/div[1]/div[1]/listBibl[1]/bibl[418]`.

```xml
<bibl xml:id="biblzh-tw_n63" xml:lang="zh-TW">蘇軾，《定風波》。</bibl>
```

^b420

### Block 421

XML location: `/div[1]/div[1]/listBibl[1]/bibl[419]`.

```xml
<bibl xml:id="COEDCOR-eg-71">
        <author>Swift, Jonathan</author>. <title level="m">Travels into Several Remote Nations of
          the World, in Four Parts. By Lemuel Gulliver... </title> (<date>1735</date>).</bibl>
```

^b421

### Block 422

XML location: `/div[1]/div[1]/listBibl[1]/bibl[420]`.

```xml
<bibl xml:id="swiftLaw"><author>Swift, Jonathan</author>. <title>Law is a bottomless pit, or
          the history of John Bull</title> (<date>1712</date>).</bibl>
```

^b422

### Block 423

XML location: `/div[1]/div[1]/listBibl[1]/bibl[421]`.

```xml
<bibl xml:id="HD-eg-swinb">
        <author>Swinburne, Algernon Charles</author>. <title level="m">Poems and Ballads (First
          Series)</title>. <pubPlace>London</pubPlace>: <publisher>Chatto &amp; Windus</publisher>.
          (<date>1904</date>). </bibl>
```

^b423

### Block 424

XML location: `/div[1]/div[1]/listBibl[1]/bibl[422]`.

```xml
<bibl xml:id="CONARS-eg-110"><author>Swinnerton, Frank Arthur</author>. <title level="m">The
          Georgian Literary Scene 1910-1935</title>, <date>1938</date>, <pubPlace>London</pubPlace>:
          <publisher>J. M. Dent</publisher>, <biblScope unit="pp">p. 195</biblScope>.</bibl>
```

^b424

### Block 425

XML location: `/div[1]/div[1]/listBibl[1]/bibl[423]`.

```xml
<bibl xml:id="biblzh-tw_n12" xml:lang="zh-TW">台灣，《結婚入盟誓》，1997年5月。</bibl>
```

^b425

### Block 426

XML location: `/div[1]/div[1]/listBibl[1]/bibl[424]`.

```xml
<bibl xml:id="biblzh-tw_n18" xml:lang="zh-TW">台灣區三碼與三加二碼郵遞區號</bibl>
```

^b426

### Block 427

XML location: `/div[1]/div[1]/listBibl[1]/bibl[425]`.

```xml
<bibl xml:id="biblzh-tw_n47" xml:lang="zh-TW">《台灣叢書》，伊能嘉矩著，藏於國立台灣大學圖書館。(http://catalog.ndap.org.tw/?URN=2155366 (Aug 2008)).</bibl>
```

^b427

### Block 428

XML location: `/div[1]/div[1]/listBibl[1]/bibl[426]`.

```xml
<bibl xml:id="biblzh-tw_n27" xml:lang="zh-TW">唐．白居易．琵琶行</bibl>
```

^b428

### Block 429

XML location: `/div[1]/div[1]/listBibl[1]/bibl[427]`.

```xml
<bibl xml:id="DIBO-egXML-lex0">
        <author>Tasovac, T.</author>, <author>Romary, L.</author>, <author>Banski, P.</author>, <author>Bowers, J.</author>, <author>de Does, J.</author>, 
        <author>Depuydt, K.</author>, <author>Erjavec, T.</author>, <author>Geyken, A.</author>, <author>Herold, A.</author>, <author>Hildenbrandt, V.</author>, 
        <author>Khemakhem, M.</author>, <author>Lehečka, B.</author>, <author>Petrović, S.</author>, <author>Salgado, A.</author> and <author>Witt, A. </author>
        <title level="m" type="main">TEI Lex-0: A baseline encoding for lexicographic data.</title>. <title level="m" type="sub">Version 0.9.3</title>.
        <publisher>DARIAH Working Group on Lexical Resources.</publisher>, <date>2018</date> 
        <ptr target="https://dariah-eric.github.io/lexicalresources/pages/TEILex0/TEILex0.html"/>.
      </bibl>
```

^b429

### Block 430

XML location: `/div[1]/div[1]/listBibl[1]/bibl[428]`.

```xml
<bibl xml:id="TAYLOR">
        <author>Taylor, John</author>
        <title>The Cold Tearme or, The Frozen age, Or, The Metamorphosis of the Riuer of
          Thames.</title> London, 1621. [STC (2nd ed.) 23910]. </bibl>
```

^b430

### Block 431

XML location: `/div[1]/div[1]/listBibl[1]/bibl[429]`.

```xml
<bibl xml:id="TEI-Consortium-CFP2022">
        <author><orgName>TEI Consortium</orgName></author>
        <title>Call for Papers - TEI 2022</title> Newcastle, 2022. <ptr target="https://web.archive.org/web/20220516140643/https://conferences.ncl.ac.uk/tei2022/cfp/"/></bibl>
```

^b431

### Block 432

XML location: `/div[1]/div[1]/listBibl[1]/bibl[430]`.

```xml
<bibl xml:id="COPA-eg-02">
        <title level="a">The Castle of the Fly</title>, in <title>Russian Fairy Tales,</title>
        translated by Norbert Guterman from the collections of Aleksandr Afanas'ev, illustrations by
        Alexander Alexeieff, folkloristic commentary by Roman Jakobson (New York: Pantheon Books,
        1947, rpt. [n.d.]), p. 25. </bibl>
```

^b432

### Block 433

XML location: `/div[1]/div[1]/listBibl[1]/bibl[431]`.

```xml
<bibl xml:id="DSHD-eg-31"><title level="j">The Daily Telegraph</title>, <date>21 Dec
          1992</date>.</bibl>
```

^b433

### Block 434

XML location: `/div[1]/div[1]/listBibl[1]/bibl[432]`.

```xml
<bibl xml:id="COHQQ-eg-30"><title level="j">The Guardian, </title>
        <date>26 Oct 1992</date>, <biblScope unit="pp">p. 2</biblScope></bibl>
```

^b434

### Block 435

XML location: `/div[1]/div[1]/listBibl[1]/bibl[433]`.

```xml
<bibl xml:id="DSDIV3X-eg-29"><title level="j">The Guardian, </title>
        <date>21 Dec 1992</date>, <biblScope unit="pp">p. 2</biblScope>.</bibl>
```

^b435

### Block 436

XML location: `/div[1]/div[1]/listBibl[1]/bibl[434]`.

```xml
<bibl xml:id="SASE-eg-40"><title>The Holy Bible, conteyning the Old Testament and the new...
          appointed to be read in Churches.</title> (<date>1611</date>), <biblScope>Genesis
          1:1</biblScope>.</bibl>
```

^b436

### Block 437

XML location: `/div[1]/div[1]/listBibl[1]/bibl[435]`.

```xml
<bibl xml:id="NDDATEA-eg-170"><!-- never used --><title level="j">The Independent, </title>
        <date>26 Oct 1775</date>, <biblScope unit="part">headline</biblScope>.</bibl>
```

^b437

### Block 438

XML location: `/div[1]/div[1]/listBibl[1]/bibl[436]`.

```xml
<bibl xml:id="COHQQ-eg-34"><author>Thurber, James</author>. <title level="m">The 13
          Clocks</title> (<date>1950</date>). </bibl>
```

^b438

### Block 439

XML location: `/div[1]/div[1]/listBibl[1]/bibl[437]`.

```xml
<bibl xml:id="COHQQ-eg-31"><author>Tolkien, J. R. R.</author>
        <title level="m">The Monsters and the Critics</title>. <pubPlace>London</pubPlace>:
          <publisher>George Allen &amp; Unwin</publisher> (<date>1983</date>).</bibl>
```

^b439

### Block 440

XML location: `/div[1]/div[1]/listBibl[1]/bibl[438]`.

```xml
<bibl xml:id="CO-eg-01">
        <author>Townsend, Sue</author>. <title level="m">The growing pains of Adrian Mole</title>
          (<date>1984</date>), <biblScope unit="pp">p.43</biblScope>. </bibl>
```

^b440

### Block 441

XML location: `/div[1]/div[1]/listBibl[1]/bibl[439]`.

```xml
<bibl xml:id="DSCO-eg-51">
        <author>Trollope, Anthony</author>. <title level="m">An Autobiography</title>
          (<date>1883</date>).</bibl>
```

^b441

### Block 442

XML location: `/div[1]/div[1]/listBibl[1]/bibl[440]`.

```xml
<bibl xml:id="NDORG-eg-38">
        <author>Trollope, Anthony</author>. <title level="m">North America</title>
          (<date>1862</date>). </bibl>
```

^b442

### Block 443

XML location: `/div[1]/div[1]/listBibl[1]/bibl[441]`.

```xml
<bibl xml:id="fr-ex-Angl" xml:lang="fr"><author>Truffaut, François</author> et
          <author>Gruault, Jean</author>, <title level="a">Les deux Anglaises et le continent :
          script</title>, <title level="j">l'Avant-scène cinéma</title>, <num>n° 121</num>,
          <date>nov. 1971</date>. </bibl>
```

^b443

### Block 444

XML location: `/div[1]/div[1]/listBibl[1]/bibl[442]`.

```xml
<bibl xml:id="COBITY-eg-240"><author>Tufte, Edward R.</author>, <title level="m">Envisioning
          Information</title>, <pubPlace>Cheshire</pubPlace>: <publisher>Graphics Press</publisher>.
          (<date>1990</date>).</bibl>
```

^b444

### Block 445

XML location: `/div[1]/div[1]/listBibl[1]/bibl[443]`.

```xml
<bibl xml:id="URF-UBSGlobal"><title>Ukraine Relief Fund</title>
        <author><orgName>UBS</orgName></author>
        <ptr target="https://web.archive.org/web/20220307150159/https://www.ubs.com/global/en/ubs-society/philanthropy/optimus-foundation/ukrainerelief.html"/>. </bibl>
```

^b445

### Block 446

XML location: `/div[1]/div[1]/listBibl[1]/bibl[444]`.

```xml
<bibl xml:id="SA-eg-01"><title>United States Code</title> Title 17, Section 107, found at <ptr target="http://www.copyright.gov/title17/92chap1.html#107"/>. </bibl>
```

^b446

### Block 447

XML location: `/div[1]/div[1]/listBibl[1]/bibl[445]`.

```xml
<bibl xml:id="MENTIOND-eg-1">
        <author>United States District Court for the Middle District of Pennsylvania</author>.
          <title>Kitzmiller v. Dover Area School District et al.</title>: <date>2005</date>.
          <idno>04cv2688</idno>, <biblScope unit="pp">p. 33</biblScope>. Available from <ptr target="http://ncse.com/files/pub/legal/kitzmiller/highlights/2005-12-20_Kitzmiller_decision.pdf"/> and transcribed at <ptr target="http://en.wikisource.org/wiki/Kitzmiller_v._Dover_Area_School_District_et_al."/>. </bibl>
```

^b447

### Block 448

XML location: `/div[1]/div[1]/listBibl[1]/bibl[446]`.

```xml
<bibl xml:id="fr-ex-Teste" xml:lang="fr"><author>Valéry, Paul</author>, <title>Monsieur
          Teste</title>, <date>1929</date>. </bibl>
```

^b448

### Block 449

XML location: `/div[1]/div[1]/listBibl[1]/bibl[447]`.

```xml
<bibl xml:id="VE-eg-02">
        <author>Vergil (Publius Vergilius Naso)</author>. <title level="m">Aeneid</title>,
          <biblScope>I.1</biblScope>. </bibl>
```

^b449

### Block 450

XML location: `/div[1]/div[1]/listBibl[1]/bibl[448]`.

```xml
<bibl xml:id="fr-ex-Verne-Ballon" xml:lang="fr"><author>Verne, Jules</author>, <title> Cinq
          semaines en ballon</title>, <date>1863</date>.</bibl>
```

^b450

### Block 451

XML location: `/div[1]/div[1]/listBibl[1]/bibl[449]`.

```xml
<bibl xml:id="fr-ex-Verne_Chasse" xml:lang="fr"><author>Verne, Jules</author>, <title>La
          Chasse au météore</title>, <date>1908</date>.</bibl>
```

^b451

### Block 452

XML location: `/div[1]/div[1]/listBibl[1]/bibl[450]`.

```xml
<bibl xml:id="fr-ex-Verne_Vingt" xml:lang="fr"><author>Verne, Jules</author>,<title> Vingt
          mille lieues sous les mers</title>, <date>1870</date>.</bibl>
```

^b452

### Block 453

XML location: `/div[1]/div[1]/listBibl[1]/bibl[451]`.

```xml
<bibl xml:id="VINGE">
        <author>Vinge, Vernor</author>
        <title>Across realtime</title>
        <biblScope>ch 10</biblScope> (<date>1986</date>). </bibl>
```

^b453

### Block 454

XML location: `/div[1]/div[1]/listBibl[1]/bibl[452]`.

```xml
<bibl xml:id="fr-ex-Viton-dictionnaire" xml:lang="fr"><author>Viton de Saint-Allais, Nicolas
        </author>, <title>Dictionnaire encyclopédique de la noblesse de France</title>,
          <date>1816</date>.</bibl>
```

^b454

### Block 455

XML location: `/div[1]/div[1]/listBibl[1]/bibl[453]`.

```xml
<bibl xml:id="PH-eg-13">
        <title>Vóluspá</title> recto of folio 5 of the unique manuscript of the Elder Edda. Codex
        Regius, ed. L. F. A. Wimmer and F. Jónsson (Copenhagen <date>1891</date>). </bibl>
```

^b455

### Block 456

XML location: `/div[1]/div[1]/listBibl[1]/bibl[454]`.

```xml
<bibl xml:id="CO-eg-03">
        <editor>Wanklyn, M.D.G. </editor> et al. <title>Gloucester Port Books, 1575-1765</title>.
        Available from <ptr target="http://discover.ukdataservice.ac.uk/catalogue?sn=3218"/>.</bibl>
```

^b456

### Block 457

XML location: `/div[1]/div[1]/listBibl[1]/bibl[455]`.

```xml
<bibl xml:id="DSAE-eg-39"><!-- Adapted from sajc000021.xml; not available from website   -->
        <author>Wanton, Joseph</author>. <title>Unpublished letter to Nicholas Brown and Co</title>,
          <date>1761</date>
        <publisher>Brown University Steering Committee on Slavery and Justice: Repository of
          Historical Documents. </publisher> (<ptr target="http://library.brown.edu/cds/slaveryandjustice/"/>). </bibl>
```

^b457

### Block 458

XML location: `/div[1]/div[1]/listBibl[1]/bibl[456]`.

```xml
<bibl xml:id="COLI-eg-175">
        <author>Warriner, John E. </author>
        <title level="m">English Composition and Grammar</title> (<date>1988</date>), <biblScope unit="pp">p.280</biblScope>.</bibl>
```

^b458

### Block 459

XML location: `/div[1]/div[1]/listBibl[1]/bibl[457]`.

```xml
<bibl xml:id="DIC-W7">
        <title>Webster's Seventh Collegiate Dictionary</title>. <pubPlace>Springfield, Mass. </pubPlace>
        <publisher>G. &amp; C. Merriam Co.</publisher> (<date>1975</date>). </bibl>
```

^b459

### Block 460

XML location: `/div[1]/div[1]/listBibl[1]/bibl[458]`.

```xml
<bibl xml:id="biblzh-tw_n8" xml:lang="zh-TW">魏飴，《小說鑑賞入門》，台北：萬卷樓，1999。</bibl>
```

^b460

### Block 461

XML location: `/div[1]/div[1]/listBibl[1]/bibl[459]`.

```xml
<bibl xml:id="fr-ex-Weil-Atares" xml:lang="fr"><author>Weil, Simone</author>, <title level="a"> Lettres à Antonio Atarès</title>, in <title level="m">Oeuvres
          complètes</title><date>1988-</date>.</bibl>
```

^b461

### Block 462

XML location: `/div[1]/div[1]/listBibl[1]/bibl[460]`.

```xml
<bibl xml:id="COHQQ-eg-25">
        <author>Williams, Nigel</author>. <title level="m">The Wimbledon Poisoner</title>
          (<date>1990</date>), <biblScope unit="pp">p. 204</biblScope>.</bibl>
```

^b462

### Block 463

XML location: `/div[1]/div[1]/listBibl[1]/bibl[461]`.

```xml
<bibl xml:id="fr-ex-Winock-Jeanne" xml:lang="fr"><author>Winock, Michel</author>,
          <title>Jeanne et les siens : récit</title>, <date>2003</date>.</bibl>
```

^b463

### Block 464

XML location: `/div[1]/div[1]/listBibl[1]/bibl[462]`.

```xml
<bibl xml:id="NOTE-eg">
        <author>Wölfflin, Heinrich</author>, trans. <editor role="translator">Hottinger, Marie
          Donald Mackie</editor> (<date>1932</date>). <title>Principles of art history: the problem
          of the development of style in later art.</title>. Originally published as <title xml:lang="de">Kunstgeschichtliche Grundbegriffe</title> (1915).</bibl>
```

^b464

### Block 465

XML location: `/div[1]/div[1]/listBibl[1]/bibl[463]`.

```xml
<bibl xml:id="CONADA-eg-143">
        <author>Woolf, Virginia</author>. <title level="m">Mrs Dalloway</title> (<date>1925</date>),
          <biblScope unit="pp">p.64, p.65</biblScope>.</bibl>
```

^b465

### Block 466

XML location: `/div[1]/div[1]/listBibl[1]/bibl[464]`.

```xml
<bibl xml:id="NH-eg-01">
        <author>Wordsworth, William</author>. <title level="a">Scorn not the sonnet</title> in
          <title level="m">Poetical Works</title> (<date>1827</date>). </bibl>
```

^b466

### Block 467

XML location: `/div[1]/div[1]/listBibl[1]/bibl[465]`.

```xml
<bibl xml:id="CO-eg-08">
        <author>Wordsworth, William</author>. <title>The Prelude</title> (<date>1850</date>). </bibl>
```

^b467

### Block 468

XML location: `/div[1]/div[1]/listBibl[1]/bibl[466]`.

```xml
<bibl xml:id="VESTR-eg-1">
        <editor>Wrenn C. L.</editor> ed. <title level="m">Beowulf: with the Finnesburg
          fragment</title>, <pubPlace>London</pubPlace>: <publisher>Harrap</publisher>
          (<date>1953</date>).</bibl>
```

^b468

### Block 469

XML location: `/div[1]/div[1]/listBibl[1]/bibl[467]`.

```xml
<bibl xml:id="biblzh-tw_n22" xml:lang="zh-TW">吳承恩，《西遊記》。</bibl>
```

^b469

### Block 470

XML location: `/div[1]/div[1]/listBibl[1]/bibl[468]`.

```xml
<bibl xml:id="DRPRO-eg-6">
        <author>Wycherley, William</author>. <title level="m">The Country Wife</title>
          (<date>1675</date>).</bibl>
```

^b470

### Block 471

XML location: `/div[1]/div[1]/listBibl[1]/bibl[469]`.

```xml
<bibl xml:id="biblzh-tw_n10" xml:lang="zh-TW">夏宇，〈甜蜜的復仇〉，《備忘錄》。</bibl>
```

^b471

### Block 472

XML location: `/div[1]/div[1]/listBibl[1]/bibl[470]`.

```xml
<bibl xml:id="biblzh-tw_n21" xml:lang="zh-TW">蕭紅，《呼蘭河傳》。</bibl>
```

^b472

### Block 473

XML location: `/div[1]/div[1]/listBibl[1]/bibl[471]`.

```xml
<bibl xml:id="biblzh-tw_n42" xml:lang="zh-TW">幼莘貢俚賀曉濤之新婚賀詞</bibl>
```

^b473

### Block 474

XML location: `/div[1]/div[1]/listBibl[1]/bibl[472]`.

```xml
<bibl xml:id="biblzh-tw_n60" xml:lang="zh-TW">余秋雨</bibl>
```

^b474

### Block 475

XML location: `/div[1]/div[1]/listBibl[1]/bibl[473]`.

```xml
<bibl xml:id="biblzh-tw_n62-64" xml:lang="zh-TW">元曲。馬致遠，《天淨沙：秋思》。</bibl>
```

^b475

### Block 476

XML location: `/div[1]/div[1]/listBibl[1]/bibl[474]`.

```xml
<bibl xml:id="biblzh-tw_n4" xml:lang="zh-TW">張錯， 《西洋文學術與手冊》，台北：書林，2005。頁201。</bibl>
```

^b476

### Block 477

XML location: `/div[1]/div[1]/listBibl[1]/bibl[475]`.

```xml
<bibl xml:id="biblzh-tw_n19" xml:lang="zh-TW">珍．奧斯丁，《傲慢與偏見》。</bibl>
```

^b477

### Block 478

XML location: `/div[1]/div[1]/listBibl[1]/bibl[476]`.

```xml
<bibl xml:id="biblzh-tw_n11" xml:lang="zh-TW">中國青年守則</bibl>
```

^b478

### Block 479

XML location: `/div[1]/div[1]/listBibl[1]/bibl[477]`.

```xml
<bibl xml:id="biblzh-tw_n13" xml:lang="zh-TW">中國學位論文全文數據庫</bibl>
```

^b479

### Block 480

XML location: `/div[1]/div[1]/listBibl[1]/bibl[478]`.

```xml
<bibl xml:id="biblzh-tw_n14" xml:lang="zh-TW">周慧玲，《表演中國：女明星表演文化視覺政治1910-1945》，2004。</bibl>
```

^b480

### Block 481

XML location: `/div[1]/div[1]/listBibl[1]/bibl[479]`.

```xml
<bibl xml:id="biblzh-tw_n56-57" xml:lang="zh-TW">朱自清， 《憶》跋。</bibl>
```

^b481

### Block 482

XML location: `/div[1]/div[1]/listBibl[1]/bibl[480]`.

```xml
<bibl xml:id="LZ">
        <author>Zimman, Lal</author>. <title>Lal Zimman</title>
        <ptr target="http://lalzimman.com/bio.html"/>, accessed <date when="2021-02-01">February 1,
          2021</date>. </bibl>
```

^b482

### Block 483

XML location: `/div[1]/div[1]/listBibl[1]/bibl[481]`.

```xml
<bibl xml:id="ZUPKO">
        <author>Zupko, Ronald Edward</author>
        <title level="m">British Weights &amp; Measures: A History from Antiquity to the Seventeenth
          Century</title>. <pubPlace>Madison</pubPlace>: <publisher>University of Wisconsin
          Press</publisher>, <biblScope unit="pp">141-151</biblScope>. </bibl>
```

^b483

### Block 484

XML location: `/div[1]/div[1]/listBibl[1]/bibl[482]`.

```xml
<bibl xml:id="NONE">No source, made up for these <title>Guidelines</title>.</bibl>
```

^b484

### Block 485

XML location: `/div[1]/div[1]/listBibl[1]/bibl[483]`.

```xml
<bibl xml:id="SELF">Example is copied from the source of these <title>Guidelines</title>.</bibl>
```

^b485

### Block 486

XML location: `/div[1]/div[1]/listBibl[1]/bibl[484]`.

```xml
<bibl xml:id="UND">Undetermined.</bibl>
```

^b486

### Block 487

XML location: `/div[1]/div[2]/head[1]`.

```xml
<head>Works Cited Elsewhere in the Text of these Guidelines</head>
```

^b487

### Block 488

XML location: `/div[1]/div[2]/listBibl[1]/bibl[1]`.

```xml
<bibl xml:id="BIB_smiley">
        <author>Scott E. Fahlman</author>
        <title>"Joke" Conversation Thread in which the :-) Was Invented</title>
        <ptr target="http://www.cs.cmu.edu/~sef/Orig-Smiley.htm"/>
        <date type="accessed" when="2023-12-08"/>
      </bibl>
```

^b488

### Block 489

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[1]`.

```xml
<biblStruct xml:id="KNUTH">
        <monogr>
          <author>
            <surname>Knuth</surname>
            <forename>Donald E.</forename>
          </author>
          <title level="m">Literate Programming</title>
          <title level="s">CSLI Lecture Notes 27</title>
          <idno type="ISBN">0-937073-80-6</idno>
          <imprint>
            <pubPlace>Stanford, California</pubPlace>
            <publisher>Center for the Study of Language and Information</publisher>
            <date>1992</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b489

### Block 490

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[2]`.

```xml
<biblStruct xml:id="mazz-NDPERSbp">
        <analytic>
          <author>
            <surname>Mazzolini</surname>
            <forename>Renato</forename>
            <forename>G.</forename>
          </author>
          <title level="a">Colonialism and the Emergence of Racial Theories</title>
          <idno type="DOI">10.1017/9781107705647.032</idno>
        </analytic>
        <monogr>
          <title level="m">Reproduction: Antiquity to the Present Day</title>
          <editor>
            <forename>Nick</forename>
            <surname>Hopwood</surname>
          </editor>
          <editor>
            <forename>Rebecca</forename>
            <surname>Flemming</surname>
          </editor>
          <editor>
            <forename>Lauren</forename>
            <surname>Kassell</surname>
          </editor>
          <imprint>
            <pubPlace>Cambridge</pubPlace>
            <publisher>Cambridge University Press</publisher>
            <date>2018</date>
          </imprint>
          <biblScope unit="page">361-374</biblScope>
        </monogr>
      </biblStruct>
```

^b490

### Block 491

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[3]`.

```xml
<biblStruct xml:id="rubin-NDPERSEpc">
        <analytic>
          <author>
            <surname>Rubin</surname>
            <forename>Gayle</forename>
          </author>
          <title level="a">The Traffic in Women: Notes on the <q>Political Economy</q> of
            Sex</title>
          <ptr target="https://philpapers.org/archive/RUBtti.pdf"/>
        </analytic>
        <monogr>
          <title level="m">Toward an Anthropology of Women</title>
          <editor>
            <forename>Rayna</forename>
            <forename>R.</forename>
            <surname>Reiter</surname>
          </editor>
          <imprint>
            <pubPlace>New York</pubPlace>
            <publisher>Monthly Review Press</publisher>
            <date>1975</date>
          </imprint>
          <biblScope unit="page">157–210, 165</biblScope>
        </monogr>
      </biblStruct>
```

^b491

### Block 492

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[4]`.

```xml
<biblStruct xml:id="PETTY">
        <monogr>
          <author>
            <forename>A. G.</forename>
            <surname>Petty</surname>
          </author>
          <title level="m">English literary hands from Chaucer to Dryden</title>
          <imprint>
            <pubPlace>London</pubPlace>
            <publisher>Edward Arnold</publisher>
            <date>1977</date>
          </imprint>
          <biblScope unit="pp"> 22–25</biblScope>
        </monogr>
      </biblStruct>
```

^b492

### Block 493

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[5]`.

```xml
<biblStruct xml:id="STTS_IBK">
        <monogr>
          <author>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </author>
          <author>
            <forename>Thomas</forename>
            <surname>Bartz</surname>
          </author>
          <author>
            <forename>Angelika</forename>
            <surname>Storrer</surname>
          </author>
          <author>
            <forename>Swantje</forename>
            <surname>Westpfahl</surname>
          </author>
          <title>Tagset and guidelines for the PoS tagging of language data from genres of
            computer-mediated communication / social media</title>
          <ptr target="https://nbn-resolving.org/urn:nbn:de:bsz:mh39-50650"/>
          <imprint>
            <date>2015-09-13</date>
            <distributor><ref target="https://sites.google.com/site/empirist2015/">EmpiriST
                2015</ref> Task Force: Michael Beißwenger, Kay-Michael Würzner, Sabine Bartsch,
              Stefan Evert</distributor>
          </imprint>
        </monogr>
      </biblStruct>
```

^b493

### Block 494

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[6]`.

```xml
<biblStruct xml:id="TEIcmc2012">
        <analytic>
          <author>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </author>
          <author>
            <forename>Maria</forename>
            <surname>Ermakova</surname>
          </author>
          <author>
            <forename>Alexander</forename>
            <surname>Geyken</surname>
          </author>
          <author>
            <forename>Lothar</forename>
            <surname>Lemnitzer</surname>
          </author>
          <author>
            <forename>Angelika</forename>
            <surname>Storrer</surname>
          </author>
          <title level="a">A TEI Schema for the Representation of Computer-mediated Communication</title>
          <ptr type="URL" target="http://journals.openedition.org/jtei/476"/>
          <ptr type="DOI" target="https://doi.org/10.4000/jtei.476"/>
        </analytic>
        <monogr>
          <title level="j">Journal of the Text Encoding Initiative</title>
          <imprint>
            <date when="2012-10-15">15 October 2012</date>
          </imprint>
          <biblScope unit="issue">3</biblScope>
        </monogr>
      </biblStruct>
```

^b494

### Block 495

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[7]`.

```xml
<biblStruct xml:id="BIB_CMC_Core">
        <analytic>
          <author>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </author>
          <author>
            <forename>Harald</forename>
            <surname>Lüngen</surname>
          </author>
          <title>CMC-core: a schema for the representation of CMC corpora in TEI</title>
          <ptr target="https://journals.openedition.org/corpus/4553"/>
        </analytic>
        <monogr>
          <title level="j">Corpus 20 (Special issue "Traitements, standardisation et analyse des
            corpus de communication médiée par les réseaux sociaux)</title>
          <editor>Céline Poudat</editor>
          <editor>Ciara R. Wigham</editor>
          <editor>Loïc Liégeois</editor>
          <imprint>
            <date>2020</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b495

### Block 496

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[8]`.

```xml
<biblStruct xml:id="BIB_scilog1">
        <analytic>
          <author>Gerry and demolog</author>
          <title>Blog comments to "Scheinzwerge oder Viele Probleme werden größer, wenn man sie
            anpackt (Griechenland)"</title>
          <ref type="url" target="https://scilogs.spektrum.de/wild-dueck-blog/scheinzwerge-oder-viele-probleme-werden-groesser-wenn-man-sie-anpackt-griechenland/">https://scilogs.spektrum.de/wild-dueck-blog/scheinzwerge-oder-viele-probleme-werden-groesser-wenn-man-sie-anpackt-griechenland/</ref>
          <date>29-30 July 2015</date>
        </analytic>
        <monogr>
          <title>WILD DUECK BLOG</title>
          <author>Gunter Dück</author>
          <imprint>
            <pubPlace><ref type="url" target="https://scilogs.spektrum.de/wild-dueck-blog/"/>https://scilogs.spektrum.de/wild-dueck-blog/</pubPlace>
          </imprint>
        </monogr>
        <series>SciLogs</series>
      </biblStruct>
```

^b496

### Block 497

XML location: `/div[1]/div[2]/listBibl[1]/bibl[2]`.

```xml
<bibl xml:id="BIB_WPTalkEiffel">Jossi et al. (2006-): <hi rend="italic">Talk:Eiffel
          (programming language)/Archive_1.</hi> URL: <ref target="https://en.wikipedia.org/wiki/Talk:Eiffel_(programming_language)/Archive_1">https://en.wikipedia.org/wiki/Talk:Eiffel_(programming_language)/Archive_1</ref>. English
        Wikipedia talk page, Wikimedia Foundation.</bibl>
```

^b497

### Block 498

XML location: `/div[1]/div[2]/listBibl[1]/bibl[3]`.

```xml
<bibl xml:id="BIB_WPTalkAstronomicalObject">MiszaBot I et al. (2011-): <hi rend="italic">Talk:Astronomical object.</hi> URL: <ref target="https://en.wikipedia.org/wiki/Talk:Astronomical_object">https://en.wikipedia.org/wiki/Talk:Astronomical_object</ref>. English Wikipedia talk
        page, Wikimedia Foundation.</bibl>
```

^b498

### Block 499

XML location: `/div[1]/div[2]/listBibl[1]/bibl[4]`.

```xml
<bibl xml:id="BIB_WPTalkFKM">OnkelSchuppig et al. (2001-): <hi rend="italic">Diskussion:FKM-Richtlinie</hi>. URL: <ref target="https://de.wikipedia.org/wiki/Diskussion:FKM-Richtlinie">https://de.wikipedia.org/wiki/Diskussion:FKM-Richtlinie</ref>. German Wikipedia talk
        page, Wikimedia Foundation.</bibl>
```

^b499

### Block 500

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[9]`.

```xml
<biblStruct xml:id="BIB_MoCoDa2">
        <monogr>
          <title>Mobile Communication Database 2 (MoCoDa2)</title>
          <editor>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </editor>
          <editor>
            <forename>Evelyn</forename>
            <surname>Ziegler</surname>
          </editor>
          <editor>
            <forename>Marcel</forename>
            <surname>Fladrich</surname>
          </editor>
          <editor>
            <forename>Wolfgang</forename>
            <surname>Imo</surname>
          </editor>
          <editor>
            <forename>Katharina</forename>
            <surname>König</surname>
          </editor>
          <imprint>
            <pubPlace>
              <ref type="url" target="https://db.mocoda2.de/c/home">https://db.mocoda2.de/c/home</ref>
            </pubPlace>
            <date type="visited">visited 30 March 2022</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b500

### Block 501

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[10]`.

```xml
<biblStruct xml:id="BIB_DCK">
        <monogr>
          <title>Dortmund Chat Corpus</title>
          <editor>
            <forename>Angelika</forename>
            <surname>Storrer</surname>
          </editor>
          <editor>
            <forename>Michael</forename>
            <surname>Beißwenger</surname>
          </editor>
          <imprint>
            <pubPlace>
              <ref type="pid" target="http://hdl.handle.net/10932/00-03B0-14FA-A8D0-0F01-F">http://hdl.handle.net/10932/00-03B0-14FA-A8D0-0F01-F</ref>
            </pubPlace>
            <date>2017</date>
            <distributor>Leibniz-Institut für Deutsche Sprache</distributor>
          </imprint>
        </monogr>
      </biblStruct>
```

^b501

### Block 502

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[11]`.

```xml
<biblStruct xml:id="BIB_CoMeRe">
        <analytic>
          <author>
            <forename>Chanier</forename>
            <surname>Thierry</surname>
          </author>
          <author>
            <forename>Poudat</forename>
            <surname>Céline</surname>
          </author>
          <author>
            <forename>Sagot</forename>
            <surname>Benoit</surname>
          </author>
          <author>
            <forename>Antoniadis</forename>
            <surname>Georges</surname>
          </author>
          <author>
            <forename>Wigham</forename>
            <surname>Ciara R.</surname>
          </author>
          <author>
            <forename>Hriba</forename>
            <surname>Linda</surname>
          </author>
          <author>
            <forename>Longhi</forename>
            <surname>Julien</surname>
          </author>
          <author>
            <forename>Seddah</forename>
            <surname>Djamé</surname>
          </author>
          <title>The CoMeRe corpus for French: structuring and annotating heterogeneous CMC
            genres</title>
        </analytic>
        <monogr>
          <title>JLCL (Journal of Language Technology and Computational Linguistics) (Special issue
            on « Building And Annotating Corpora Of Computer-Mediated Discourse: Issues and
            Challenges at the Interface of Corpus and Computational Linguistics)</title>
          <imprint>
            <pubPlace><ref type="url">http://www.jlcl.org/2014_Heft2/Heft2-2014.pdf</ref></pubPlace>
            <date>2014</date>
          </imprint>
          <biblScope unit="volume">2</biblScope>
          <biblScope unit="pp">1-31</biblScope>
        </monogr>
      </biblStruct>
```

^b502

### Block 503

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[12]`.

```xml
<biblStruct xml:id="BIB_Cotgrove">
        <monogr>
          <editor>
            <forename>Louis Alexander</forename>
            <surname>Cotgrove</surname>
          </editor>
          <title>Nottinghamer Korpus Deutscher YouTube-Sprache (The NottDeuYTSch Corpus)</title>
          <imprint>
            <pubPlace>
              <ref type="url" target="http://hdl.handle.net/11372/LRT-4806">http://hdl.handle.net/11372/LRT-4806</ref>
            </pubPlace>
            <distributor>LINDAT/CLARIAH-CZ</distributor>
            <date>2018</date>
          </imprint>
        </monogr>

      </biblStruct>
```

^b503

### Block 504

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[13]`.

```xml
<biblStruct xml:id="BIB_ChanierWigham2015">
        <analytic>
          <author>
            <forename>Ciara</forename>
            <surname>Wigham</surname>
          </author>
          <author>
            <forename>Thierry</forename>
            <surname>Chanier</surname>
          </author>
          <title>Interactions between text chat and audio modalities for L2 communication and
            feedback in the synthetic world Second Life</title>
          <idno type="DOI">10.1080/09588221.2013.851702</idno>
        </analytic>
        <monogr>
          <title>Computer Assisted Language Learning</title>
          <imprint>
            <date>2015</date>
          </imprint>
          <biblScope unit="volume">23</biblScope>
          <biblScope unit="issue">3</biblScope>
        </monogr>
      </biblStruct>
```

^b504

### Block 505

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[14]`.

```xml
<biblStruct xml:id="AB-eg-01">
        <analytic>
          <author>
            <forename>Lou</forename>
            <surname>Burnard</surname>
          </author>
          <title level="a">Report of Workshop on Text Encoding Guidelines</title>
        </analytic>
        <monogr>
          <title level="j">Literary &amp; Linguistic Computing</title>
          <imprint>
            <biblScope unit="vol">3</biblScope>
            <date>1988</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b505

### Block 506

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[15]`.

```xml
<biblStruct xml:id="Burnard1995b">
        <analytic>
          <author>
            <forename>Lou</forename>
            <surname>Burnard</surname>
          </author>
          <author>
            <forename>C.</forename>
            <forename>Michael</forename>
            <surname>Sperberg-McQueen</surname>
          </author>
          <title level="a">The Design of the TEI Encoding Scheme</title>
          <idno type="DOI">10.1007/BF01830314</idno>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <biblScope unit="vol">29</biblScope>
            <biblScope unit="issue">1</biblScope>
            <date>1995</date>
            <biblScope unit="pp">17–39</biblScope>
          </imprint>
        </monogr>
        <note>Reprinted in <ptr target="#Ide1995b"/>, pp. 17-40</note>
      </biblStruct>
```

^b506

### Block 507

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[16]`.

```xml
<biblStruct xml:id="TD-BIBL-01">
        <analytic>
          <author>
            <forename>Lou</forename>
            <surname>Burnard</surname>
          </author>
          <author>
            <forename>Sebastian</forename>
            <surname>Rahtz</surname>
          </author>
          <title level="m">RelaxNG with Son of ODD</title>
          <ptr target="http://www.mulberrytech.com/Extreme/Proceedings/html/2004/Burnard01/EML2004Burnard01.pdf"/>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2004</title>
          <imprint>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b507

### Block 508

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[17]`.

```xml
<biblStruct xml:id="PARKES">
        <monogr>
          <author>
            <forename>M.</forename>
            <forename>B.</forename>
            <surname>Parkes</surname>
          </author>
          <title level="m">English Cursive Book Hands 1250–1500</title>
          <imprint>
            <pubPlace>Oxford</pubPlace>
            <publisher>Clarendon Press</publisher>
            <date>1969</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b508

### Block 509

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[18]`.

```xml
<biblStruct xml:id="KLINKENBORG">
        <monogr>
          <title>British Literary Manuscripts. Series 2: from 1800 to 1914</title>
          <author>
            <surname>Klinkenborg</surname>
            <forename>Verlyn</forename>
          </author>
          <author>
            <surname>Cahoon</surname>
            <forename>Herbert</forename>
          </author>
          <imprint>
            <pubPlace> New York</pubPlace>
            <publisher>Pierpont Morgan Library</publisher>
            <date>1981</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b509

### Block 510

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[19]`.

```xml
<biblStruct xml:id="XPTRFMWK">
        <monogr>
          <editor>
            <forename>Paul</forename>
            <surname>Grosso</surname>
          </editor>
          <editor>
            <forename>Eve</forename>
            <surname>Maler</surname>
          </editor>
          <editor>
            <forename>Jonathan</forename>
            <surname>Marsh</surname>
          </editor>
          <editor>
            <forename>Norman</forename>
            <surname>Walsh</surname>
          </editor>
          <title level="m">XPointer Framework</title>
          <ptr target="https://www.w3.org/TR/xptr-framework/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2003-03-25">25 March 2003</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b510

### Block 511

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[20]`.

```xml
<biblStruct xml:id="XPTRELEM">
        <monogr>
          <editor>
            <forename>Paul</forename>
            <surname>Grosso</surname>
          </editor>
          <editor>
            <forename>Eve</forename>
            <surname>Maler</surname>
          </editor>
          <editor>
            <forename>Jonathan</forename>
            <surname>Marsh</surname>
          </editor>
          <editor>
            <forename>Norman</forename>
            <surname>Walsh</surname>
          </editor>
          <title level="m">XPointer element() Scheme</title>
          <ptr target="https://www.w3.org/TR/xptr-element/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2003-03-25">25 March 2003</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b511

### Block 512

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[21]`.

```xml
<biblStruct xml:id="XHTML">
        <monogr>
          <title level="m">XHTML™ 1.0 The Extensible HyperText Markup Language (Second
            Edition)</title>
          <ptr target="https://www.w3.org/TR/xhtml/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2000-01-26">26 January 2000</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b512

### Block 513

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[22]`.

```xml
<biblStruct xml:id="HTML4">
        <monogr>
          <editor>
            <forename>Dave</forename>
            <surname>Ragget</surname>
          </editor>
          <editor>
            <forename>Arnaud</forename>
            <surname>Le Hors</surname>
          </editor>
          <editor>
            <forename>Ian</forename>
            <surname>Jacobs</surname>
          </editor>
          <title level="m"> HTML 4.01 Specification</title>
          <ptr target="https://www.w3.org/TR/html401/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="1999-12-24">24 December 1999</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b513

### Block 514

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[23]`.

```xml
<biblStruct xml:id="MATHML">
        <monogr>
          <editor>
            <forename>David</forename>
            <surname>Carlisle</surname>
          </editor>
          <editor>
            <forename>Patrick</forename>
            <surname>Ion</surname>
          </editor>
          <editor>
            <forename>Robert</forename>
            <surname>Miner</surname>
          </editor>
          <editor>
            <forename>Nico</forename>
            <surname>Poppelier</surname>
          </editor>
          <title level="m">Mathematical Markup Language (MathML) Version 2.0 (Second
            edition)</title>
          <ptr target="https://www.w3.org/TR/MathML2/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2003-10-21">21 October 2003</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b514

### Block 515

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[24]`.

```xml
<biblStruct xml:id="XSD2">
        <monogr>
          <editor>
            <forename>Paul V.</forename>
            <surname>Biron</surname>
          </editor>
          <editor>
            <forename>Ashok</forename>
            <surname>Malhotra</surname>
          </editor>
          <title level="m">XML Schema Part 2: Datatypes Second Edition</title>
          <ptr target="https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2004-10-28">28 October 2004</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b515

### Block 516

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[25]`.

```xml
<biblStruct xml:id="XSL11">
        <monogr>
          <editor>
            <forename>Anders</forename>
            <surname>Berglund</surname>
          </editor>
          <title level="m">Extensible Stylesheet Language (XSL) Version 1.1</title>
          <ptr target="https://www.w3.org/TR/xsl11/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2006-12-05">5 December 2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b516

### Block 517

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[26]`.

```xml
<biblStruct xml:id="XSLT">
        <monogr>
          <editor>
            <forename>James</forename>
            <surname>Clark</surname>
          </editor>
          <title level="m">XSL Transformations (XSLT) Version 1.0</title>
          <ptr target="https://www.w3.org/TR/xslt/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="1999-11-16">16 November 1999</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b517

### Block 518

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[27]`.

```xml
<biblStruct xml:id="XSLT2">
        <monogr>
          <editor>
            <forename>Michael</forename>
            <surname>Kay</surname>
          </editor>
          <title level="m">XSL Transformations (XSLT) Version 2.0</title>
          <ptr target="https://www.w3.org/TR/xslt20/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2007-01-23">23 January 2007</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b518

### Block 519

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[28]`.

```xml
<biblStruct xml:id="XSLT3">
        <monogr>
          <editor>
            <forename>Michael</forename>
            <surname>Kay</surname>
          </editor>
          <title level="m">XSL Transformations (XSLT) Version 3.0</title>
          <ptr target="https://www.w3.org/TR/xslt-30/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2017-06-08">8 June 2017</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b519

### Block 520

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[29]`.

```xml
<biblStruct xml:id="XMLREC">
        <monogr>
          <editor>
            <forename>Tim</forename>
            <surname>Bray</surname>
          </editor>
          <editor>
            <forename>Jean</forename>
            <surname>Paoli</surname>
          </editor>
          <editor>
            <forename>C. M.</forename>
            <surname>Sperberg-McQueen</surname>
          </editor>
          <editor>
            <forename>Eve</forename>
            <surname>Maler</surname>
          </editor>
          <editor>
            <forename>François</forename>
            <surname>Yergau</surname>
          </editor>
          <title level="m">Extensible Markup Language (XML) Version 1.0 (Fourth edition)</title>
          <ptr target="https://www.w3.org/TR/REC-xml/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2006-08-16">16 August 2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b520

### Block 521

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[30]`.

```xml
<biblStruct xml:id="CSS21">
        <monogr>
          <editor>
            <forename>Bert</forename>
            <surname>Bos</surname>
          </editor>
          <editor>
            <forename>Tantek</forename>
            <surname>Çelik</surname>
          </editor>
          <editor>
            <forename>Ian</forename>
            <surname>Hickson</surname>
          </editor>
          <editor>
            <forename>Håkon Wium</forename>
            <surname>Lie</surname>
          </editor>
          <title level="m">Cascading Style Sheets Level 2 Revision 1</title>
          <ptr target="https://www.w3.org/TR/CSS2/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2011-06-07">7 June 2011</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b521

### Block 522

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[31]`.

```xml
<biblStruct xml:id="CSS1">
        <monogr>
          <editor>
            <forename>Håkon Wium</forename>
            <surname>Lie</surname>
          </editor>
          <editor>
            <forename>Bert</forename>
            <surname>Bos</surname>
          </editor>
          <title level="m">Cascading Style Sheets, Level 1</title>
          <ptr target="https://www.w3.org/TR/REC-CSS1/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="1999-01-11">11 January 1999</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b522

### Block 523

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[32]`.

```xml
<biblStruct xml:id="CSSWM">
        <monogr>
          <editor>
            <name>fantasai</name>
          </editor>
          <editor>
            <forename>Koji</forename>
            <surname>Ishi</surname>
          </editor>
          <title level="m">CSS Writing Modes Level 3 (W3C Candidate Recommendation)</title>
          <ptr target="https://www.w3.org/TR/css-writing-modes-3/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2015-12-15">15 December 2015</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b523

### Block 524

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[33]`.

```xml
<biblStruct xml:id="CSSTM">
        <monogr>
          <editor>
            <forename>Simon</forename>
            <surname>Fraser</surname>
          </editor>
          <editor>
            <forename>Dean</forename>
            <surname>Jackson</surname>
          </editor>
          <editor>
            <forename>Edward</forename>
            <surname>O'Connor</surname>
          </editor>
          <editor>
            <forename>Dirk</forename>
            <surname>Schulze</surname>
          </editor>
          <title level="m">CSS Transforms Module Level 1 (W3C Working Draft)</title>
          <ptr target="https://www.w3.org/TR/css-transforms/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2013-11-26">26 November 2013</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b524

### Block 525

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[34]`.

```xml
<biblStruct xml:id="RDFPrimer">
        <monogr>
          <editor>
            <forename>Frank</forename>
            <surname>Manola</surname>
          </editor>
          <editor>
            <forename>Eric</forename>
            <surname>Miller</surname>
          </editor>
          <editor>
            <forename>Brian</forename>
            <surname>McBride</surname>
          </editor>
          <title>RDF 1.1 Primer</title>
          <ptr target="https://www.w3.org/TR/rdf11-primer/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2014-06-24">24 June 2014</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b525

### Block 526

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[35]`.

```xml
<biblStruct xml:id="XMLBASE">
        <monogr>
          <editor>
            <forename>Jonathan</forename>
            <surname>Marsh</surname>
          </editor>
          <editor>
            <forename>Richard</forename>
            <surname>Tobin</surname>
          </editor>
          <title level="m">XML Base (Second Edition)</title>
          <ptr target="https://www.w3.org/TR/xmlbase/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2009-01-28">28 January 2009</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b526

### Block 527

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[36]`.

```xml
<biblStruct xml:id="XPATH">
        <monogr>
          <editor>
            <forename>James</forename>
            <surname>Clark</surname>
          </editor>
          <editor>
            <forename>Steve</forename>
            <surname>DeRose</surname>
          </editor>
          <title level="m">XML Path Language (XPath) Version 1.0</title>
          <ptr target="https://www.w3.org/TR/xpath/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="1999-11-16">16 November 1999</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b527

### Block 528

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[37]`.

```xml
<biblStruct xml:id="XPATH2">
        <monogr>
          <editor>
            <forename>Anders</forename>
            <surname>Berglund</surname>
          </editor>
          <editor>
            <forename>Scot</forename>
            <surname>Boag</surname>
          </editor>
          <editor>
            <forename>Mary F.</forename>
            <surname>Fernández</surname>
          </editor>
          <editor>
            <forename>Michael</forename>
            <surname>Kay</surname>
          </editor>
          <editor>
            <forename>Jonathan</forename>
            <surname>Robie</surname>
          </editor>
          <editor>
            <forename>Jérôme</forename>
            <surname> Siméon</surname>
          </editor>
          <title level="m">XML Path Language (XPath) 2.0</title>
          <ptr target="https://www.w3.org/TR/xpath20/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2007-01-23">23 January 2007</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b528

### Block 529

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[38]`.

```xml
<biblStruct xml:id="XPATH30">
        <monogr>
          <editor>
            <forename>Jonathan</forename>
            <surname>Robie</surname>
          </editor>
          <editor>
            <forename>Don</forename>
            <surname>Chamberlin</surname>
          </editor>
          <editor>
            <forename>Michael</forename>
            <surname>Dyck</surname>
          </editor>
          <editor>
            <forename>Jon</forename>
            <surname>Snelson</surname>
          </editor>
          <title level="m">XML Path Language (XPath) 3.0</title>
          <ptr target="https://www.w3.org/TR/xpath-30/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2014-04-08">8 April 2014</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b529

### Block 530

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[39]`.

```xml
<biblStruct xml:id="XPATH31">
        <monogr>
          <editor>
            <forename>Jonathan</forename>
            <surname>Robie</surname>
          </editor>
          <editor>
            <forename>Michael</forename>
            <surname>Dyck</surname>
          </editor>
          <editor>
            <forename>Josh</forename>
            <surname>Spiegel</surname>
          </editor>
          <title level="m">XML Path Language (XPath) 3.1</title>
          <ptr target="https://www.w3.org/TR/xpath-31/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2017-03-21">21 March 2017</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b530

### Block 531

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[40]`.

```xml
<biblStruct xml:id="NAMESPACES">
        <monogr>
          <editor>
            <forename>Tim</forename>
            <surname>Bray</surname>
          </editor>
          <editor>
            <forename>Dave</forename>
            <surname>Hollander</surname>
          </editor>
          <editor>
            <forename>Andrew</forename>
            <surname>Laymon</surname>
          </editor>
          <editor>
            <forename>Richard</forename>
            <surname>Tobin</surname>
          </editor>
          <title level="m">Namespaces in XML 1.0 (second edition)</title>
          <ptr target="https://www.w3.org/TR/xml-names/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2006-08-16">16 August 2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b531

### Block 532

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[41]`.

```xml
<biblStruct xml:id="SG-BIBL-1">
        <monogr>
          <author>
            <forename>Eric</forename>
            <surname>van der Vlist</surname>
          </author>
          <title level="m">RELAX NG</title>
          <ptr target="http://books.xmlschemata.org/relaxng/page2.html"/>
          <imprint>
            <publisher>O'Reilly</publisher>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b532

### Block 533

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[42]`.

```xml
<biblStruct xml:id="SG-BIBL-2">
        <analytic>
          <author>
            <surname>Renear</surname>
            <forename>A.</forename>
          </author>
          <author>
            <surname>Mylonas</surname>
            <forename>E.</forename>
          </author>
          <author>
            <surname>Durand</surname>
            <forename>D. </forename>
          </author>
          <title level="a">Refining our notion of what text really is: the problem of overlapping
            hierarchies</title>
        </analytic>
        <monogr>
          <editor>
            <forename>Nancy</forename>
            <surname>Ide</surname>
          </editor>
          <editor>
            <forename>Susan</forename>
            <surname>Hockey</surname>
          </editor>
          <title level="m">Research in Humanities Computing</title>
          <imprint>
            <publisher>Oxford University Press</publisher>
            <date>1996</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b533

### Block 534

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[43]`.

```xml
<biblStruct xml:id="WADM">
        <monogr>
          <editor>
            <forename>Robert</forename>
            <surname>Sanderson</surname>
          </editor>
          <editor>
            <forename>Paolo</forename>
            <surname>Ciccarese</surname>
          </editor>
          <editor>
            <forename>Benjamin</forename>
            <surname>Young</surname>
          </editor>
          <title>Web Annotation Data Model</title>
          <ptr target="https://www.w3.org/TR/annotation-model/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2017-02-23">23 February 2017</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b534

### Block 535

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[44]`.

```xml
<biblStruct xml:id="WAV">
        <monogr>
          <editor>
            <forename>Robert</forename>
            <surname>Sanderson</surname>
          </editor>
          <editor>
            <forename>Paolo</forename>
            <surname>Ciccarese</surname>
          </editor>
          <editor>
            <forename>Benjamin</forename>
            <surname>Young</surname>
          </editor>
          <title>Web Annotation Vocabulary</title>
          <ptr target="https://www.w3.org/TR/annotation-vocab/"/>
          <imprint>
            <publisher>W3C</publisher>
            <date when="2017-02-23">23 February 2017</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b535

### Block 536

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[45]`.

```xml
<biblStruct xml:id="CH-BIBL-3">
        <monogr>
          <title>The Unicode Standard, Version 5.0</title>
          <ptr target="https://www.unicode.org/"/>
          <author>Unicode Consortium</author>
          <imprint>
            <publisher>Addison-Wesley Professional</publisher>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b536

### Block 537

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[46]`.

```xml
<biblStruct xml:id="CH-BIBL-4">
        <monogr>
          <editor>
            <forename>Addison</forename>
            <surname>Phillips</surname>
          </editor>
          <editor>
            <forename>Mark</forename>
            <surname>Davis</surname>
          </editor>
          <title level="m">Tags for Identifying Languages</title>
          <idno>RFC 4646</idno>
          <imprint>
            <date>2006</date>
            <publisher>IETF</publisher>
          </imprint>
        </monogr>
      </biblStruct>
```

^b537

### Block 538

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[47]`.

```xml
<biblStruct xml:id="CH-BIBL-5">
        <monogr>
          <editor>
            <forename>Addison</forename>
            <surname>Phillips</surname>
          </editor>
          <editor>
            <forename>Mark</forename>
            <surname>Davis</surname>
          </editor>
          <title level="m">Matching of Language Tags</title>
          <idno>RFC 4647</idno>
          <imprint>
            <date>2006</date>
            <publisher>IETF</publisher>
          </imprint>
        </monogr>
      </biblStruct>
```

^b538

### Block 539

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[48]`.

```xml
<biblStruct xml:id="WD-bibl-01">
        <monogr>
          <author>
            <forename>Mark</forename>
            <surname>Davis</surname>
          </author>
          <author>
            <forename>Ken</forename>
            <surname>Whistler</surname>
          </author>
          <author>
            <forename>Asmus</forename>
            <surname>Freytag</surname>
          </author>
          <title level="m">Unicode Character Database</title>
          <ptr target="https://www.unicode.org/Public/UNIDATA/UCD.html"/>
          <imprint>
            <publisher>Unicode Consortium</publisher>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b539

### Block 540

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[49]`.

```xml
<biblStruct xml:id="FS-BIBL-1">
        <monogr>
          <author>
            <forename>Fernando</forename>
            <forename>C.</forename>
            <forename>N.</forename>
            <surname>Pereira</surname>
          </author>
          <title level="m"> Grammars and logics of partial information</title>
          <imprint>
            <pubPlace>Menlo Park, CA</pubPlace>
            <publisher>SRI International</publisher>
            <date>1987</date>
          </imprint>
        </monogr>
        <series>
          <title level="s">SRI International Technical Note</title>
          <biblScope unit="vol">420</biblScope>
        </series>
      </biblStruct>
```

^b540

### Block 541

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[50]`.

```xml
<biblStruct xml:id="FS-BIBL-5">
        <monogr>
          <author>
            <forename>Bob</forename>
            <surname>Carpenter</surname>
          </author>
          <title level="m"> The logic of typed feature structures</title>
          <imprint>
            <pubPlace>Cambridge</pubPlace>
            <publisher>Cambridge University Press</publisher>
            <date>1992</date>
          </imprint>
        </monogr>
        <series>
          <title level="s">Cambridge Tracts in Theoretical Computer Science</title>
          <biblScope unit="vol">32</biblScope>
        </series>
      </biblStruct>
```

^b541

### Block 542

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[51]`.

```xml
<biblStruct xml:id="FS-BIBL-2">
        <monogr>
          <author>
            <forename>Stuart</forename>
            <surname>Shieber</surname>
          </author>
          <title level="m">An Introduction to Unification-based Approaches to Grammar</title>
          <idno>CSLI Lecture Notes 4</idno>
          <imprint>
            <publisher>Center for the Study of Language and Information</publisher>
            <pubPlace>Palo Alto, CA</pubPlace>
            <date>1986</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b542

### Block 543

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[52]`.

```xml
<biblStruct xml:id="HD-BIBL-1">
        <monogr>
          <title level="m">Anglo-American Cataloguing Rules</title>
          <edition>Second Edition, 2002 revision, 2005 update</edition>
          <imprint>
            <pubPlace>Chicago</pubPlace>
            <publisher>American Library Association</publisher>
            <pubPlace>Ottawa</pubPlace>
            <publisher>Canadian Library Association</publisher>
            <date>2002–2005</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b543

### Block 544

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[53]`.

```xml
<biblStruct xml:id="HD-BIBL-2">
        <monogr>
          <author>
            <forename>John</forename>
            <surname>Burrows</surname>
          </author>
          <title level="m">Computation into Criticism: A Study of Jane Austen's Novel and an
            Experiment in Method</title>
          <imprint>
            <pubPlace>Oxford</pubPlace>
            <publisher>Clarendon Press</publisher>
            <date>1987</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b544

### Block 545

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[54]`.

```xml
<biblStruct xml:id="CO-BIBL-1">
        <monogr>
          <editor>
            <forename>Klaus</forename>
            <surname>Mattheier</surname>
          </editor>
          <editor>
            <forename>Ulrich</forename>
            <surname>Ammon</surname>
          </editor>
          <editor>
            <forename>Peter</forename>
            <surname>Trudgill</surname>
          </editor>
          <title level="m" xml:lang="en" type="main">Sociolinguistics</title>
          <title level="m" xml:lang="de" type="main">Soziolinguistik</title>
          <title level="m" xml:lang="en" type="sub">An international handbook of the science of
            language and society</title>
          <title level="m" xml:lang="de" type="sub">Ein internationales Handbuch zur Wissenschaft
            von Sprache und Gesellschaft</title>
          <imprint>
            <pubPlace>Berlin</pubPlace>
            <pubPlace>New York</pubPlace>
            <publisher>De Gruyter</publisher>
            <date>1988</date>
            <biblScope unit="vol">I</biblScope>
            <biblScope unit="pp">271 and 274</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b545

### Block 546

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[55]`.

```xml
<biblStruct xml:id="TS-BIBL-1">
        <monogr>
          <editor>
            <forename>J.</forename>
            <forename>A.</forename>
            <surname>Edwards</surname>
          </editor>
          <editor>
            <forename>M.</forename>
            <forename>D.</forename>
            <surname>Lampert</surname>
          </editor>
          <title level="m">Talking Language: Transcription and Coding of Spoken Discourse</title>
          <imprint>
            <pubPlace>Hillsdale, N.J.</pubPlace>
            <publisher>Lawrence Erlbaum Associates</publisher>
            <date>1993</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b546

### Block 547

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[56]`.

```xml
<biblStruct xml:id="CH-eg-02">
        <monogr>
          <author>
            <forename>Asmus</forename>
            <surname>Freytag</surname>
          </author>
          <title level="m">The Unicode Character Property Model</title>
          <title level="s">Unicode Technical Report #23</title>
          <ptr target="https://www.unicode.org/reports/tr23/"/>
          <imprint>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b547

### Block 548

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[57]`.

```xml
<biblStruct xml:id="WDBIDI">
        <monogr>
          <author>
            <forename>Mark</forename>
            <surname>Davis</surname>
          </author>
          <author>
            <forename>Aharon</forename>
            <surname>Lanin</surname>
          </author>
          <author>
            <forename>Andrew</forename>
            <surname>Glass</surname>
          </author>
          <title level="m">Unicode Bidirectional Algorithm</title>
          <title level="s">Unicode Standard Annex #9</title>
          <ptr target="https://www.unicode.org/reports/tr9/"/>
          <imprint>
            <date>2017-05-04</date>
          </imprint>
          <biblScope>r. 37</biblScope>
        </monogr>
      </biblStruct>
```

^b548

### Block 549

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[58]`.

```xml
<biblStruct xml:id="TS-BIBL-2">
        <analytic>
          <author>
            <forename>Stig</forename>
            <surname>Johansson</surname>
          </author>
          <title level="a">Encoding a Corpus in Machine-Readable Form</title>
        </analytic>
        <monogr>
          <editor>
            <!--<forename>Beryl</forename>
                                                <forename>T.</forename>-->
            <forename>Sue</forename>
            <surname>Atkins</surname>
          </editor>
          <editor>
            <forename>Antonio</forename>
            <surname>Zampolli</surname>
          </editor>
          <title level="m">Computational Approaches to the Lexicon: An Overview</title>
          <imprint>
            <pubPlace>Oxford</pubPlace>
            <publisher>Oxford University Press</publisher>
            <date>1994</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b549

### Block 550

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[59]`.

```xml
<biblStruct xml:id="TS-BIBL-3">
        <monogr>
          <author>
            <forename>Stig</forename>
            <surname>Johansson</surname>
          </author>
          <author>
            <forename>Lou</forename>
            <surname>Burnard</surname>
          </author>
          <author>
            <forename>Jane</forename>
            <surname>Edwards</surname>
          </author>
          <author>
            <forename>And</forename>
            <surname>Rosta</surname>
          </author>
          <title level="m">Working Paper on Spoken Texts</title>
          <title type="sub">TEI document TEI AI2 W1</title>
          <imprint>
            <date>1991</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b550

### Block 551

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[60]`.

```xml
<biblStruct xml:id="TS-BIBL-4">
        <monogr>
          <author>
            <forename>Brian</forename>
            <surname>MacWhinney</surname>
          </author>
          <title level="m">CHAT Manual</title>
          <imprint>
            <pubPlace>Pittsburgh</pubPlace>
            <publisher>Dept of Psychology, Carnegie-Mellon University</publisher>
            <date>1988</date>
            <biblScope unit="pp">87ff</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b551

### Block 552

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[61]`.

```xml
<biblStruct xml:id="TS-BIBL-7">
        <monogr>
          <author>
            <forename>Bengt</forename>
            <surname>Loman</surname>
          </author>
          <author>
            <forename>Nils</forename>
            <surname>Jørgensen</surname>
          </author>
          <title level="m">Manual for analys och beskrivning av makrosyntagmer</title>
          <imprint>
            <pubPlace>Lund</pubPlace>
            <publisher>Studentlitteratur</publisher>
            <date>1971</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b552

### Block 553

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[62]`.

```xml
<biblStruct xml:id="DI-BIBL-1">
        <analytic>
          <author>
            <forename>Robert</forename>
            <forename>A.</forename>
            <surname>Amsler</surname>
          </author>
          <author>
            <forename>Frank</forename>
            <forename>W.</forename>
            <surname>Tompa</surname>
          </author>
          <title level="a">An SGML-Based Standard for English Monolingual Dictionaries</title>
        </analytic>
        <monogr>
          <title level="m" type="main">Information in Text</title>
          <title level="m" type="sub">Fourth Annual Conference of the U[niversity of] W[aterloo]
            Centre for the New Oxford English Dictionary</title>
          <meeting>Fourth Annual Conference of the U[niversity of] W[aterloo] Centre for the New
            Oxford English Dictionary, October 26-28, 1988, Waterloo, Canada</meeting>
          <imprint>
            <pubPlace>Waterloo, Canada</pubPlace>
            <date when="1988-10">October 1988</date>
            <biblScope unit="pp">61-79</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b553

### Block 554

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[63]`.

```xml
<biblStruct xml:id="DI-BIBL-2">
        <monogr>
          <author>
            <forename>N.</forename>
            <surname>Calzolari</surname>
          </author>
          <author>
            <forename>C.</forename>
            <surname>Peters</surname>
          </author>
          <author>
            <forename>A.</forename>
            <surname>Roventini</surname>
          </author>
          <title level="m" type="main">Computational Model of the Dictionary Entry: Preliminary
            Report</title>
          <title level="m" type="sub">Acquilex: Esprit Basic Research Action No. 3030, Six-Month
            Deliverable</title>
          <imprint>
            <pubPlace>Pisa</pubPlace>
            <date when="1990-04">April 1990</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b554

### Block 555

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[64]`.

```xml
<biblStruct xml:id="DI-BIBL-3">
        <monogr>
          <author>
            <forename>John</forename>
            <surname>Fought</surname>
          </author>
          <author>
            <forename>Carol</forename>
            <surname>Van Ess-Dykema</surname>
          </author>
          <title level="m">Toward an SGML Document Type Definition for Bilingual
            Dictionaries</title>
          <title type="sub">TEI working paper TEI AIW20</title>
          <imprint>
            <publisher>available from the TEI.</publisher>
          </imprint>
        </monogr>
      </biblStruct>
```

^b555

### Block 556

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[65]`.

```xml
<biblStruct xml:id="DI-BIBL-4">
        <analytic>
          <author>
            <forename>Nancy</forename>
            <surname>Ide</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <surname>Veronis</surname>
          </author>
          <title level="a">Encoding Print Dictionaries</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <biblScope unit="vol">29</biblScope>
            <date>1995</date>
            <biblScope unit="pp">167-195</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b556

### Block 557

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[66]`.

```xml
<biblStruct xml:id="DI-BIBL-5">
        <analytic>
          <author>
            <forename>Nancy</forename>
            <surname>Ide</surname>
          </author>
          <author>
            <forename>Jacques</forename>
            <surname>Le Maitre</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <surname>Veronis</surname>
          </author>
          <title level="a">Outline of a Model for Lexical Databases</title>
        </analytic>
        <monogr>
          <title level="j">Information Processing and Management</title>
          <imprint>
            <biblScope unit="vol">29</biblScope>
            <biblScope unit="issue">2</biblScope>
            <date>1993</date>
            <biblScope unit="pp">159-186</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b557

### Block 558

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[67]`.

```xml
<biblStruct xml:id="DI-BIBL-6">
        <analytic>
          <author>
            <forename>Nancy</forename>
            <surname>Ide</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <surname>Veronis</surname>
          </author>
          <author>
            <forename>Susan</forename>
            <surname>Warwick-Amstrong</surname>
          </author>
          <author>
            <forename>Nicoletta</forename>
            <surname>Calzolari</surname>
          </author>
          <title level="a">Principles for Encoding machine readable dictionaries</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of the Fifth EURALEX International Congress,
            EURALEX'92</title>
          <meeting>Fifth EURALEX International Congress, EURALEX'92, University of Tampere,
            Finland</meeting>
          <imprint>
            <date>1992</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b558

### Block 559

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[68]`.

```xml
<biblStruct xml:id="DI-BIBL-7">
        <analytic>
          <author>
            <forename>The</forename>
            <surname>DANLEX Group</surname>
          </author>
          <title level="a">Descriptive tools for electronic processing of dictionary data</title>
        </analytic>
        <monogr>
          <title level="j">Lexicographica, Series Maior</title>
          <imprint>
            <pubPlace>Tübingen</pubPlace>
            <publisher>Niemeyer</publisher>
            <date>1987</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b559

### Block 560

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[69]`.

```xml
<biblStruct xml:id="DI-BIBL-8">
        <analytic>
          <author>
            <forename>Agnès</forename>
            <surname>Tutin</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <surname>Veronis</surname>
          </author>
          <title level="a">Electronic dictionary encoding: customizing the TEI Guidelines</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of the Eighth Euralex International Congress</title>
          <meeting>Eighth Euralex International Congress</meeting>
          <imprint>
            <date>1998</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b560

### Block 561

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[70]`.

```xml
<biblStruct xml:id="DI-BIBL-9">
        <analytic>
          <author>
            <forename>N.</forename>
            <surname>Ide</surname>
          </author>
          <author>
            <forename>A.</forename>
            <surname>Kilgarriff</surname>
          </author>
          <author>
            <forename>L.</forename>
            <surname>Romary</surname>
          </author>
          <title level="a">A Formal Model of Dictionary Structure and Content</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Euralex 2000</title>
          <meeting>Euralex 2000</meeting>
          <imprint>
            <pubPlace>Stuttgart</pubPlace>
            <date>2000</date>
            <biblScope unit="pp">113-126</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b561

### Block 562

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[71]`.

```xml
<biblStruct xml:id="SA-BIBL-1">
        <analytic>
          <author>
            <forename>William</forename>
            <forename>A.</forename>
            <surname>Gale</surname>
          </author>
          <author>
            <forename>Kenneth</forename>
            <forename>W.</forename>
            <surname>Church</surname>
          </author>
          <title level="a">Program for aligning sentences in bilingual corpora</title>
        </analytic>
        <monogr>
          <title level="j">Computational Linguistics</title>
          <imprint>
            <biblScope unit="vol">19</biblScope>
            <date>1993</date>
            <biblScope unit="pp">75-102</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b562

### Block 563

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[72]`.

```xml
<biblStruct xml:id="AI-BIBL-5">
        <analytic>
          <author>
            <forename>G.</forename>
            <forename>N.</forename>
            <surname>Leech</surname>
          </author>
          <author>
            <forename>R.</forename>
            <forename>G.</forename>
            <surname>Garside</surname>
          </author>
          <title level="a">Running a Grammar Factory</title>
        </analytic>
        <monogr>
          <editor>
            <forename>S.</forename>
            <surname>Johansson</surname>
          </editor>
          <editor>
            <forename>A.-B.</forename>
            <surname>Stenstrøm</surname>
          </editor>
          <title level="m">English Computer Corpora: Selected Papers and Research Guide</title>
          <imprint>
            <pubPlace>Berlin</pubPlace>
            <publisher>de Gruyter</publisher>
            <pubPlace>New York</pubPlace>
            <publisher>Mouton</publisher>
            <date>1991</date>
            <biblScope unit="pp">pp. 15-32.</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b563

### Block 564

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[73]`.

```xml
<biblStruct xml:id="AI-BIBL-6">
        <analytic>
          <author>
            <forename>I.</forename>
            <surname>Marshall</surname>
          </author>
          <title level="a">Choice of Grammatical Word Class without Global Syntactic Analysis:
            Tagging Words in the LOB Corpus</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <biblScope unit="vol">17</biblScope>
            <date>1983</date>
            <biblScope unit="pp">139-50</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b564

### Block 565

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[74]`.

```xml
<biblStruct xml:id="AI-BIBL-7">
        <monogr>
          <author>
            <forename>R.</forename>
            <forename>G.</forename>
            <surname>Garside</surname>
          </author>
          <author>
            <forename>G.</forename>
            <forename>N.</forename>
            <surname>Leech</surname>
          </author>
          <author>
            <forename>G.</forename>
            <forename>R.</forename>
            <surname>Sampson</surname>
          </author>
          <title level="m">The Computational Analysis of English: a Corpus-Based Approach</title>
          <imprint>
            <pubPlace>Oxford</pubPlace>
            <publisher>Oxford University Press</publisher>
            <date>1991</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b565

### Block 566

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[75]`.

```xml
<biblStruct xml:id="GD-BIBL-1">
        <monogr>
          <author>
            <forename>Gary</forename>
            <surname>Chartrand</surname>
          </author>
          <author>
            <forename>Linda</forename>
            <surname>Lesniak</surname>
          </author>
          <title level="m">Graphs and Digraphs</title>
          <imprint>
            <pubPlace>Menlo Park, CA</pubPlace>
            <publisher>Wadsworth</publisher>
            <date>1986</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b566

### Block 567

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[76]`.

```xml
<biblStruct xml:id="GD-BIBL-2">
        <analytic>
          <author>
            <forename>R.</forename>
            <surname>Jackendoff</surname>
          </author>
          <title level="a">X-Bar Syntax: A study of phrase structure</title>
        </analytic>
        <monogr>
          <title level="j">Linguistic Inquiry Monograph</title>
          <imprint>
            <biblScope unit="vol">2</biblScope>
            <date>1977</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b567

### Block 568

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[77]`.

```xml
<biblStruct xml:id="CC-BIBL-1">
        <analytic>
          <author>
            <forename>M.</forename>
            <surname>Kytö</surname>
          </author>
          <author>
            <forename>M.</forename>
            <surname>Rissanen</surname>
          </author>
          <title level="a">The Helsinki Corpus of English Texts</title>
        </analytic>
        <monogr>
          <editor>
            <forename>M.</forename>
            <surname>Kytö</surname>
          </editor>
          <editor>
            <forename>O.</forename>
            <surname>Ihalainen</surname>
          </editor>
          <editor>
            <forename>M.</forename>
            <surname>Rissanen</surname>
          </editor>
          <title level="m">Corpus Linguistics: hard and soft</title>
          <imprint>
            <pubPlace>Amsterdam</pubPlace>
            <publisher>Rodopi</publisher>
            <date>1988</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b568

### Block 569

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[78]`.

```xml
<biblStruct xml:id="NH-BIBL-1">
        <analytic>
          <author>
            <forename>Steven</forename>
            <surname>DeRose</surname>
          </author>
          <title level="a">Markup overlap: a review and a horse</title>
          <ptr target="http://www.mulberrytech.com/Extreme/Proceedings/html/2004/DeRose01/EML2004DeRose01.html"/>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2004</title>
          <imprint>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b569

### Block 570

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[79]`.

```xml
<biblStruct xml:id="NH-BIBL-01">
        <monogr>
          <author>
            <forename>Andreas</forename>
            <surname>Witt</surname>
          </author>
          <title level="m" xml:lang="de">Multiple Informationsstrukturierung mit
            Auszeichnungssprachen. XML-basierte Methoden und deren Nutzen für die
            Sprachtechnologie</title>
          <imprint>
            <date>2002</date>
          </imprint>
        </monogr>
        <note>Ph D thesis, Bielefeld University</note>
        <note>See also <ptr target="http://xml.coverpages.org/Witt-allc2002.html"/>
        </note>
      </biblStruct>
```

^b570

### Block 571

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[80]`.

```xml
<biblStruct xml:id="NH-BIBL-2">
        <analytic>
          <author>
            <forename>Mirco</forename>
            <surname>Hilbert</surname>
          </author>
          <author>
            <forename>Oliver</forename>
            <surname>Schonefeld</surname>
          </author>
          <author>
            <forename>Andreas</forename>
            <surname>Witt</surname>
          </author>
          <title level="a">Making CONCUR work</title>
          <ptr target="http://www.mulberrytech.com/Extreme/Proceedings/html/2005/Witt01/EML2005Witt01.xml"/>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2005</title>
          <imprint>
            <date>2005</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b571

### Block 572

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[81]`.

```xml
<biblStruct xml:id="NH-BIBL-3">
        <monogr>
          <author>
            <forename>Alex</forename>
            <surname>Dekhtyar</surname>
          </author>
          <author>
            <forename>Ionut</forename>
            <forename>E.</forename>
            <surname>Iacob</surname>
          </author>
          <title level="m">A framework for management of concurrent XML markup</title>
          <!-- MDH 2014-01-22 Note: This is a 404 and the website appears to be down. Replaced with another source.-->
          <!--<ptr target="http://www.eppt.org/~emil/publications/dke04-concurrent.pdf"/>-->
          <ptr target="http://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=1104&amp;context=csse_fac"/>
          <imprint>
            <date>2005</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b572

### Block 573

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[82]`.

```xml
<biblStruct xml:id="NH-BIBL-4">
        <monogr>
          <author>
            <forename>H.</forename>
            <forename>V.</forename>
            <surname>Jagadish</surname>
          </author>
          <author>
            <forename>Laks</forename>
            <forename>V.</forename>
            <forename>S.</forename>
            <surname>Lakshmanan</surname>
          </author>
          <author>
            <forename>Monica</forename>
            <surname>Scannapieco</surname>
          </author>
          <author>
            <forename>Divesh</forename>
            <surname>Srivastava</surname>
          </author>
          <author>
            <forename>Nuwee</forename>
            <surname>Wiwatwattana</surname>
          </author>
          <title level="m">Colorful XML: one hierarchy isn't enough</title>
          <!-- MDH 2014-01-22 Note: Old URL redirects to new location, so ptr updated.  -->
          <!-- MDH 2015-12-28 Note: New URL server disappeared from the web, so now linking to archive.org copy.  -->
          <!--<ptr target="http://www.research.att.com/~divesh/papers/jlssw2004-mct.pdf"/>-->
          <!--<ptr target="http://www2.research.att.com/~divesh/papers/jlssw2004-mct.pdf"/>-->
          <ptr target="http://web.archive.org/web/20150706093254/http://www2.research.att.com/~divesh/papers/jlssw2004-mct.pdf"/>
          <imprint>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b573

### Block 574

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[83]`.

```xml
<biblStruct xml:id="NH-BIBL-5">
        <analytic>
          <author>
            <forename>Noureddine</forename>
            <surname>Chatti</surname>
          </author>
          <author>
            <forename>Suha</forename>
            <surname>Kaouk</surname>
          </author>
          <author>
            <forename>Sylvie</forename>
            <surname>Calabretto</surname>
          </author>
          <author>
            <forename>Jean</forename>
            <forename>Marie</forename>
            <surname>Pinon</surname>
          </author>
          <title level="a">MultiX: an XML based formalism to encode multistructured
            documents</title>
          <!-- MDH 2014-01-22 Note: old URL was 404, replaced with new location.  -->
          <!--<ptr target="http://www.idealliance.org/papers/extreme/proceedings/html/2007/Chatti01/EML2007Chatti01.html"/>-->
          <ptr target="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.115.1525&amp;rep=rep1&amp;type=pdf"/>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2007</title>
          <imprint>
            <date>2007</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b574

### Block 575

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[84]`.

```xml
<biblStruct xml:id="NH-BIBL-6">
        <analytic>
          <author>
            <forename>Patrick</forename>
            <surname>Durusau</surname>
          </author>
          <author>
            <forename>Matthew</forename>
            <forename>Brook</forename>
            <surname>O'Donnell</surname>
          </author>
          <title level="a">Coming down from the trees: next step in the evolution of markup?</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages 2002</title>
          <imprint>
            <date>2002</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b575

### Block 576

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[85]`.

```xml
<biblStruct xml:id="NH-BIBL-7">
        <analytic>
          <author>
            <forename>Jeni</forename>
            <surname>Tennison</surname>
          </author>
          <author>
            <forename>Wendell</forename>
            <surname>Piez</surname>
          </author>
          <title level="a">The layered markup and annotation language</title>
        </analytic>
        <monogr>
          <title level="m">Proceedings of Extreme Markup Languages Conference</title>
          <imprint>
            <date>2002</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b576

### Block 577

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[86]`.

```xml
<biblStruct xml:id="NH-BIBL-8">
        <monogr>
          <author>
            <forename>Claus</forename>
            <surname>Huitfeldt</surname>
          </author>
          <author>
            <forename>C.</forename>
            <forename>Michael</forename>
            <surname>Sperberg-McQueen</surname>
          </author>
          <title level="m">TexMECS: An experimental markup meta-language for complex
            documents</title>
          <ptr target="http://mlcd.blackmesatech.com/mlcd/2003/Papers/texmecs.html"/>
          <imprint>
            <date>2001</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b577

### Block 578

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[87]`.

```xml
<biblStruct xml:id="FS-BIBL-01">
        <analytic>
          <author>
            <forename>D. Terence</forename>
            <surname>Langendoen</surname>
          </author>
          <author>
            <forename>Gary F. </forename>
            <surname>Simons</surname>
          </author>
          <title level="a">A rationale for the TEI recommendations for feature-structure
            markup,</title>
        </analytic>
        <monogr>
          <title level="j">Computers and the Humanities</title>
          <imprint>
            <biblScope unit="vol">29</biblScope>
            <date>1995</date>
            <biblScope unit="pp">167-195</biblScope>
          </imprint>
        </monogr>
      </biblStruct>
```

^b578

### Block 579

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[88]`.

```xml
<biblStruct xml:id="BS-5605">
        <monogr>
          <author>British Standards Institute</author>
          <title level="m">BS 5605:1990: Recommendations for Citing and Referencing Published
            Material</title>
          <imprint>
            <date>1990</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b579

### Block 580

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[89]`.

```xml
<biblStruct xml:id="BS-6371">
        <monogr>
          <author>British Standards Institute</author>
          <title level="m">BS 6371:1983: Recommendations for Citation of Unpublished
            Documents</title>
          <imprint>
            <date>1983</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b580

### Block 581

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[90]`.

```xml
<biblStruct xml:id="DIN-1505-2">
        <monogr>
          <author>Deutsches Institut für Normung</author>
          <title level="m">DIN 1505-2: Titelangaben von Dokumenten; Zitierregeln</title>
          <imprint>
            <date>1984</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b581

### Block 582

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[91]`.

```xml
<biblStruct xml:id="RAK">
        <monogr>
          <author>Die Deutsche Bibliothek</author>
          <title level="m">Regeln für die alphabetische Katalogisierung in wissenschaftlichen
            Bibliotheken RAK-WB</title>
          <imprint>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b582

### Block 583

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[92]`.

```xml
<biblStruct xml:id="ISO-690">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO 690:1987: Information and documentation – Bibliographic references – Content,
            form and structure</title>
          <imprint>
            <date>1987</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b583

### Block 584

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[93]`.

```xml
<biblStruct xml:id="ISO-8601">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO 8601:2004: Data elements and interchange formats — Information interchange —
            Representation of dates and times</title>
          <imprint>
            <date>2004</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b584

### Block 585

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[94]`.

```xml
<biblStruct xml:id="ISO-12620">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO 12620:2009: Terminology and other language and content resources –
            Specification of data categories and management of a Data Category Registry for language
            resources</title>
          <ptr target="http://www.iso.org/iso/catalogue_detail?csnumber=37243"/>
          <imprint>
            <date>2009</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b585

### Block 586

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[95]`.

```xml
<biblStruct xml:id="ISO-19136">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO 19136:2007: Geographic information — Geography Markup Language (GML)</title>
          <imprint>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b586

### Block 587

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[96]`.

```xml
<biblStruct xml:id="ISO-19757-3">
        <monogr>
          <author>International Organization for Standardization</author>
          <title>ISO/IEC 19757-3:2006: Information technology — Document Schema Definition Languages
            (DSDL) – Part 3: Rule-based validation – Schematron</title>
          <imprint>
            <date>2006</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b587

### Block 588

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[97]`.

```xml
<biblStruct xml:id="RICA">
        <monogr>
          <author>Istituto Centrale per il Catalogo Unico</author>
          <title level="m">Regole italiane di catalogazione per autori</title>
          <imprint>
            <date>1979</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b588

### Block 589

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[98]`.

```xml
<biblStruct xml:id="ANSI-NISO-Z39.29">
        <monogr>
          <author>National Information Standards Organization</author>
          <title>ANSI/NISO Z39.29 – 2005 (R2010) Bibliographic References</title>
          <imprint>
            <date>2010</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b589

### Block 590

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[99]`.

```xml
<biblStruct xml:id="ISBD">
        <monogr>
          <title level="m">ISBD: International Standard Bibliographic Description</title>
          <imprint>
            <pubPlace>Berlin, München</pubPlace>
            <pubPlace>De Gruyter Saur</pubPlace>
            <date>2011</date>
          </imprint>
        </monogr>
        <series>
          <title>IFLA Series on Bibliographic Control</title>
          <biblScope unit="vol">44</biblScope>
        </series>
      </biblStruct>
```

^b590

### Block 591

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[100]`.

```xml
<biblStruct xml:id="GOST-7.0.5">
        <monogr>
          <author>Федеральное агентство по техническому регулированию и метрологии
            (РОССТАНДАРТ)</author>
          <title level="m">ГОСТ Р 7.0.5-2008: Система стандартов по информации, библиотечному и
            издательскому делу. Библиографическая ссылка. Общие требования и правила
            составления</title>
          <imprint>
            <date>2008</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b591

### Block 592

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[101]`.

```xml
<biblStruct xml:id="GOST-7.1">
        <monogr>
          <author>Федеральное агентство по техническому регулированию и метрологии
            (РОССТАНДАРТ)</author>
          <title level="m">ГОСТ 7.1—2003. Система стандартов по информации, библиотечному и
            издательскому делу. Библиографическая запись. Библоиграфическое описание. Общие
            требования и правила составления</title>
          <imprint>
            <date>2003</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b592

### Block 593

XML location: `/div[1]/div[2]/listBibl[1]/biblStruct[102]`.

```xml
<biblStruct xml:id="CO-BIBL-2">
        <monogr>
          <author>DCMI Usage Board</author>
          <title>Dublin Core™ Metadata Element Set, Version 1.1: Reference Description</title>
          <ptr target="https://www.dublincore.org/specifications/dublin-core/dces/"/>
          <imprint>
            <date>2012-06-14</date>
          </imprint>
        </monogr>
      </biblStruct>
```

^b593

### Block 594

XML location: `/div[1]/div[3]/head[1]`.

```xml
<head>Reading List</head>
```

^b594

### Block 595

XML location: `/div[1]/div[3]/p[1]`.

```xml
<p rend="display">The following lists of readings in markup theory and the TEI derive from work
      originally prepared by Susan Schreibman and Kevin Hawkins for the TEI Education Special
      Interest Group, recoded in TEI P5 by Sabine Krott and Eva Radermacher. They should be regarded
      only as a snapshot of work in progress, to which further contributions and corrections are
      welcomed (see further <ptr target="http://www.tei-c.org/Support/Learn/tei_bibliography.xml"/>).</p>
```

^b595

### Block 596

XML location: `/div[1]/div[3]/div[1]/head[1]`.

```xml
<head>Theory of Markup and XML</head>
```

^b596

### Block 597

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[1]`.

```xml
<biblStruct xml:id="XX-1">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeld</surname>
            </author>
            <title level="a">Concurrent Document Hierarchies in MECS and SGML</title>
          </analytic>
          <monogr>
            <title level="j">Literary and Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">14</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1999</date>
              <biblScope unit="pp">29-42</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b597

### Block 598

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[2]`.

```xml
<biblStruct xml:id="XX-2">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Rabbit/duck grammars: a validation method for overlapping
              structures</title>
            <ptr target="http://conferences.idealliance.org/extreme/html/2006/SperbergMcQueen01/EML2006SperbergMcQueen01.html"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of Extreme Markup Languages 2006</title>
            <imprint>
              <date>2006</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b598

### Block 599

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[3]`.

```xml
<biblStruct xml:id="Barnardetal1995">
          <analytic>
            <author>
              <forename>David</forename>
              <forename>T.</forename>
              <surname>Barnard</surname>
            </author>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Jean-Pierre</forename>
              <surname>Gaspart</surname>
            </author>
            <author>
              <forename>Lynne</forename>
              <forename>A.</forename>
              <surname>Price</surname>
            </author>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Giovanni</forename>
              <forename>Battista</forename>
              <surname>Varile</surname>
            </author>
            <title level="a">Hierarchical Encoding of Text: Technical Problems and SGML
              Solutions</title>
            <idno type="DOI">10.1007/BF01830617</idno>
            <ptr target="http://www.tei-c.org/Vault/ML/mlw18.ps"/>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">29</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1995</date>
              <biblScope unit="pp">211–231</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b599

### Block 600

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[4]`.

```xml
<biblStruct xml:id="Barnardetal1996">
          <analytic>
            <author>
              <forename>David</forename>
              <forename>T.</forename>
              <surname>Barnard</surname>
            </author>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Lessons learned from using SGML in the Text Encoding Initiative</title>
            <idno type="DOI">10.1016/0920-5489(95)00035-6</idno>
          </analytic>
          <monogr>
            <title level="j">Computer Standards &amp; Interfaces</title>
            <imprint>
              <biblScope unit="vol">18</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1996</date>
              <biblScope unit="pp">3–10</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b600

### Block 601

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[5]`.

```xml
<biblStruct xml:id="Burnard1991">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">What is SGML and how does it help?</title>
            <ptr target="http://www.tei-c.org/Vault/ED/EDW25/"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Daniel</forename>
              <surname>Greenstein</surname>
            </editor>
            <title level="m">Modelling Historical Data: Towards a Standard for Encoding and
              Exchanging Machine-readable Texts</title>
            <imprint>
              <pubPlace>St Katherinen</pubPlace>
              <publisher>Max-Planck-Institut für Geschichte In Kommission bei Scripta Mercaturae
                Verlag</publisher>
              <date>1991</date>
              <biblScope unit="pp">81–91</biblScope>
            </imprint>
          </monogr>
          <series>
            <title level="s">Halbgraue Reihe zur Historischen Fachinformatik</title>
            <respStmt>
              <resp>Herausg. von</resp>
              <persName>
                <forename>Manfred</forename>
                <surname>Thaller</surname>
              </persName>
            </respStmt>
            <biblScope>serie A</biblScope>
            <biblScope unit="vol">11</biblScope>
          </series>
          <!--note>last accessed August 12, 2007</note-->
          <note>Revised version published as <ptr target="#Burnard1995a"/></note>
        </biblStruct>
```

^b601

### Block 602

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[6]`.

```xml
<biblStruct xml:id="Burnard1995a">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">SGML on the Web: Too Little Too Soon or Too Much Too Late?</title>
            <ptr target="http://users.ox.ac.uk/~lou/Belux/"/>
          </analytic>
          <monogr>
            <title level="j">Computers &amp; Texts</title>
            <imprint>
              <biblScope unit="vol">15</biblScope>
              <date>1995</date>
              <biblScope unit="pp">12–15</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b602

### Block 603

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[7]`.

```xml
<biblStruct xml:id="Burnard1995c">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">What is SGML and How Does It Help?</title>
            <idno type="DOI">10.1007/BF01830315</idno>
            <ptr target="http://xml.coverpages.org/burnardw25-index.html"/>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">29</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1995</date>
              <biblScope unit="pp">41–50</biblScope>
            </imprint>
          </monogr>
          <note>Reprinted in <ptr target="#Ide1995b"/>, pp. 41-50</note>
        </biblStruct>
```

^b603

### Block 604

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[8]`.

```xml
<biblStruct xml:id="Ide1995b">
          <monogr>
            <editor>
              <forename>Nancy</forename>
              <surname>Ide</surname>
            </editor>
            <editor>
              <forename>Jean</forename>
              <surname>Veronis</surname>
            </editor>
            <title level="m">The Text Encoding Initiative: Background and Contexts</title>
            <imprint>
              <pubPlace>Dordrecht</pubPlace>
              <pubPlace>Boston</pubPlace>
              <publisher>Kluwer Academic Publisher</publisher>
              <date>1995</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b604

### Block 605

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[9]`.

```xml
<biblStruct xml:id="Burnard1999a">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">Is Humanities Computing an Academic Discipline? or, Why Humanities
              Computing Matters</title>
            <ptr target="http://www.iath.virginia.edu/hcs/burnard.html"/>
            <ptr target="http://www.iath.virginia.edu/hcs/"/>
            <imprint>
              <date>1999</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 29, 2007</note-->
          <note>Presented at an interdisciplinary seminar at the Institute for Advanced Technology
            in the Humanities, University of Virginia, November 1999.</note>
        </biblStruct>
```

^b605

### Block 606

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[10]`.

```xml
<biblStruct xml:id="Burnard1999b">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Using SGML for Linguistic Analysis: The Case of the BNC</title>
            <ptr target="http://users.ox.ac.uk/~lou/papers/sgml96.sgm"/>
          </analytic>
          <monogr>
            <title level="j">Markup Languages Theory and Practice</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <date>1999</date>
              <pubPlace>Cambridge, Massachusettes</pubPlace>
              <publisher>MIT Press</publisher>
              <biblScope unit="pp">31–51</biblScope>
            </imprint>
          </monogr>
          <note>Also published in <ptr target="#Moser2001a"/>, pp. 53–72</note>
        </biblStruct>
```

^b606

### Block 607

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[11]`.

```xml
<biblStruct xml:id="Moser2001a">
          <monogr>
            <editor>
              <forename>Stephan</forename>
              <surname>Moser</surname>
            </editor>
            <editor>
              <forename>Peter</forename>
              <surname>Stahl</surname>
            </editor>
            <editor>
              <forename>Werner</forename>
              <surname>Wegstein</surname>
            </editor>
            <editor>
              <forename>Norbert</forename>
              <forename>Richard</forename>
              <surname>Wolf</surname>
            </editor>
            <title level="m">Maschinelle Verarbeitung Altdeutscher Texte V (Beiträge zum Fünften
              Internationalen Symposion, Würzburg, 4–6 März 1997)</title>
            <imprint>
              <pubPlace>Tübingen</pubPlace>
              <publisher>Niemeyer</publisher>
              <date>2001</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b607

### Block 608

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[12]`.

```xml
<biblStruct xml:id="Burnardetal1999">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Elizabeth</forename>
              <surname>Lalou</surname>
            </author>
            <author>
              <forename>Peter</forename>
              <surname>Robinson</surname>
            </author>
            <title level="a">Vers un Standard Européen de Description des Manuscrits: Le Projet
              Master</title>
          </analytic>
          <monogr>
            <title level="j" type="main">Documents Numeriques</title>
            <title level="j" type="sub">Les Documents Anciens</title>
            <imprint>
              <biblScope unit="vol">3</biblScope>
              <biblScope unit="issue">1–2</biblScope>
              <date>1999</date>
              <pubPlace>Paris</pubPlace>
              <publisher>Hermes Science Publications</publisher>
              <biblScope unit="pp">151-169</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b608

### Block 609

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[13]`.

```xml
<biblStruct xml:id="Burnard1999">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">XML: The Dream and the Reality</title>
            <ptr target="http://users.ox.ac.uk/~lou/papers/euro99.xml"/>
            <imprint>
              <date>1999</date>
            </imprint>
          </monogr>
          <note>Closing plenary address at the XML Europe Conference, Granada, May 1999</note>
        </biblStruct>
```

^b609

### Block 610

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[14]`.

```xml
<biblStruct xml:id="Burnardetal2000">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Claudia</forename>
              <surname>Claridge</surname>
            </author>
            <author>
              <forename>Josef</forename>
              <surname>Schmied</surname>
            </author>
            <author>
              <forename>Rainer</forename>
              <surname>Siemund</surname>
            </author>
            <title level="a">Encoding the Lampeter Corpus</title>
            <ptr target="http://users.ox.ac.uk/~lou/papers/glasgie.xml"/>
          </analytic>
          <monogr>
            <title level="m">DRH98: Selected Papers from Digital Resources for the
              Humanities</title>
            <imprint>
              <pubPlace>London</pubPlace>
              <publisher>Office for Humanities Communication</publisher>
              <date>2000</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b610

### Block 611

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[15]`.

```xml
<biblStruct xml:id="Burnard2000">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">From Two Cultures to Digital Culture: The Rise of the Digital
              Demotic</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/twocults.html"/>
            <imprint>
              <date>2000</date>
            </imprint>
          </monogr>
          <note>Presented at CLIP, Alicante</note>
          <!--note>last accessed on August 12, 2007</note-->
          <note> Published in Italian as <ptr target="#Burnard2001a"/>
          </note>
        </biblStruct>
```

^b611

### Block 612

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[16]`.

```xml
<biblStruct xml:id="Burnard2001a">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Dalle «Due Culture» Alla Cultura Digitale: La Nascita del Demotico
              Digitale</title>
            <respStmt>
              <resp>Translated by</resp>
              <persName>
                <forename>Federico</forename>
                <surname>Pellizi</surname>
              </persName>
            </respStmt>
          </analytic>
          <monogr>
            <title level="j" type="main">Il Verri</title>
            <title level="j" type="sub">Nella Rete</title>
            <imprint>
              <biblScope unit="vol">16</biblScope>
              <date>2001</date>
              <pubPlace>Milano</pubPlace>
              <publisher>Monogramma</publisher>
              <biblScope unit="pp">9–22</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b612

### Block 613

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[17]`.

```xml
<biblStruct xml:id="Burnard2001b">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">On the Hermeneutic Implications of Text Encoding</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/herman.htm"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Domenico</forename>
              <surname>Fiormonte</surname>
            </editor>
            <editor>
              <forename>Jonathan</forename>
              <surname>Usher</surname>
            </editor>
            <title level="m">New Media and the Humanities: Research and Applications</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Humanities Computing Unit</publisher>
              <date>2001</date>
              <biblScope unit="pp">31–38</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed on August 12, 2007</note-->
        </biblStruct>
```

^b613

### Block 614

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[18]`.

```xml
<biblStruct xml:id="Burnard2005a">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Encoding Standards for the Electronic Edition</title>
            <ptr target="http://nl.ijs.si/e-zrc/bib/eziss-Burnard.pdf"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Matija</forename>
              <surname>Ogrin</surname>
            </editor>
            <title level="m" xml:lang="sl" type="main">Znanstvene Izdaje in Elektronski
              Medij</title>
            <title level="m" xml:lang="en" type="sub">Scholarly Editions and the Digital
              Medium</title>
            <imprint>
              <pubPlace>Ljubljana</pubPlace>
              <publisher>Studia Litteraria ZRC ZAZU</publisher>
              <date>2005</date>
              <biblScope unit="pp">12–67</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b614

### Block 615

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[19]`.

```xml
<biblStruct xml:id="Burnard2005b">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Metadata for corpus work</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/metadata.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Martin</forename>
              <surname>Wynne</surname>
            </editor>
            <title level="m">Developing Linguistic Corpora: A Guide to Good Practice</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Oxbow Books</publisher>
              <date>2005</date>
              <biblScope unit="pp">30–46</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b615

### Block 616

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[20]`.

```xml
<biblStruct xml:id="Burnardetaleds2006">
          <monogr>
            <editor>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </editor>
            <editor>
              <forename>Katherine</forename>
              <forename>O'Brien</forename>
              <surname>O'Keefe</surname>
            </editor>
            <editor>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </editor>
            <title level="m">Electronic Textual Editing</title>
            <ptr target="http://www.tei-c.org/Vault/ETE/"/>
            <imprint>
              <pubPlace>New York</pubPlace>
              <publisher>Modern Languages Association</publisher>
              <date>2006</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b616

### Block 617

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[21]`.

```xml
<biblStruct xml:id="Buzzetti2002">
          <analytic>
            <author>
              <forename>Dino</forename>
              <surname>Buzzetti</surname>
            </author>
            <title level="a">Digital Representation and the Text Model</title>
            <ptr target="http://muse.jhu.edu/journals/new_literary_history/v033/33.1buzzetti.html"/>
          </analytic>
          <monogr>
            <title level="j">New Literary History</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2002</date>
              <biblScope unit="pp">61–88</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b617

### Block 618

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[22]`.

```xml
<biblStruct xml:id="Caton2001">
          <analytic>
            <author>
              <forename>Paul</forename>
              <surname>Caton</surname>
            </author>
            <title level="a">Markup's Current Imbalance</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory and Practice</title>
            <imprint>
              <biblScope unit="vol">3</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2001</date>
              <biblScope unit="pp">1–13</biblScope>
            </imprint>
          </monogr>
          <note>This paper was proceeded by reports at the Joint Annual Conference of the
            Association for Computers and the Humanities and the Association for Literary and
            Linguistic Computing in 1999 (Charlottesville, Virginia) and Extreme Markup Languages
            2000 (Montreal, Canada)</note>
        </biblStruct>
```

^b618

### Block 619

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[23]`.

```xml
<biblStruct xml:id="ChenandYu2003">
          <analytic>
            <author>
              <forename>Ruey-Shun</forename>
              <surname>Chen</surname>
            </author>
            <author>
              <forename>Shien-Chiang</forename>
              <surname>Yu</surname>
            </author>
            <title level="a">Developing an XML Framework for Metadata System</title>
            <ptr target="http://dl.acm.org/citation.cfm?id=963653"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of the 1st International Symposium on Information and
              Communication Technologies</title>
            <imprint>
              <pubPlace>Dublin</pubPlace>
              <date>2003</date>
              <biblScope unit="pp">267–272</biblScope>
            </imprint>
          </monogr>
          <series>
            <title level="s">ACM International Conference Proceeding Series</title>
            <biblScope unit="vol">49</biblScope>
          </series>
          <!--note>last accessed August 12, 2007</note-->
          <note>This paper was presented in a session entitled "Electronic Document
            Technology."</note>
        </biblStruct>
```

^b619

### Block 620

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[24]`.

```xml
<biblStruct xml:id="Coombs1986">
          <monogr>
            <author>
              <forename>James</forename>
              <forename>H.</forename>
              <surname>Coombs</surname>
            </author>
            <title level="m">Information Management System for Scholars</title>
            <idno>Technical Memorandum TM 69–2</idno>
            <imprint>
              <pubPlace>Providence</pubPlace>
              <publisher>Brown Computer Center</publisher>
              <date>1986</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b620

### Block 621

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[25]`.

```xml
<biblStruct xml:id="Coombsetal1987">
          <analytic>
            <author>
              <forename>James</forename>
              <forename>H.</forename>
              <surname>Coombs</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>Steven</forename>
              <forename>J.</forename>
              <surname>DeRose</surname>
            </author>
            <title level="a">Markup Systems and The Future of Scholarly Text Processing</title>
            <idno type="DOI">10.1145/32206.32209</idno>
            <ptr target="http://xml.coverpages.org/coombs-hallgren.html"/>
            <ptr target="http://xml.coverpages.org/coombs.html"/>
          </analytic>
          <monogr>
            <title level="j">Communications of the ACM</title>
            <imprint>
              <biblScope unit="vol">30</biblScope>
              <biblScope unit="issue">11</biblScope>
              <date>1987</date>
              <biblScope unit="pp">933–947</biblScope>
            </imprint>
          </monogr>
          <note>Reprinted with new commentary in <ptr target="#Landow1993a"/>, pp 85–118</note>
        </biblStruct>
```

^b621

### Block 622

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[26]`.

```xml
<biblStruct xml:id="Landow1993a">
          <monogr>
            <editor>
              <forename>George</forename>
              <forename>P.</forename>
              <surname>Landow</surname>
            </editor>
            <editor>
              <forename>Paul</forename>
              <surname>Delany</surname>
            </editor>
            <title level="m">The Digital Word: Text-based Computing in the Humanities</title>
            <imprint>
              <pubPlace>Cambridge, MA</pubPlace>
              <publisher>MIT Press</publisher>
              <date>1993</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b622

### Block 623

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[27]`.

```xml
<biblStruct xml:id="Cover2005">
          <monogr>
            <author>
              <forename>Robin</forename>
              <surname>Cover</surname>
            </author>
            <title level="m">Markup Languages and (Non-) Hierarchies</title>
            <ptr target="http://xml.coverpages.org/hierarchies.html"/>
            <imprint>
              <date>2005</date>
            </imprint>
          </monogr>
          <note>Technology report from the Cover Pages</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b623

### Block 624

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[28]`.

```xml
<biblStruct xml:id="DeRose1995">
          <monogr>
            <author>
              <forename>Steven</forename>
              <forename>J.</forename>
              <surname>DeRose</surname>
            </author>
            <title level="m">Structured Information: Navigation, Access, and Control</title>
            <ptr target="http://xml.coverpages.org/deroseStructure.html"/>
            <imprint>
              <date>1995</date>
            </imprint>
          </monogr>
          <note>Paper presented at the Berkeley Finding Aid Conference, April 4–6, 1995</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b624

### Block 625

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[29]`.

```xml
<biblStruct xml:id="DeRoseetal1990">
          <analytic>
            <author>
              <forename>Steven</forename>
              <forename>J.</forename>
              <surname>DeRose</surname>
            </author>
            <author>
              <forename>David</forename>
              <forename>G.</forename>
              <surname>Durand</surname>
            </author>
            <author>
              <forename>Elli</forename>
              <surname>Mylonas</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">What is Text, Really?</title>
          </analytic>
          <monogr>
            <title level="j">Journal of Computing in Higher Education</title>
            <imprint>
              <biblScope unit="vol">1</biblScope>
              <biblScope unit="issue">2</biblScope>
              <date>1990</date>
              <biblScope unit="pp">3–26</biblScope>
            </imprint>
          </monogr>
          <note>Republished (<ptr target="#DeRose1997a"/>) as a "classic reprint" with invited
            commentary and authors' replies in the ACM/SIGDOC</note>
        </biblStruct>
```

^b625

### Block 626

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[30]`.

```xml
<biblStruct xml:id="DeRose1997a">
          <analytic>
            <author>
              <forename>Steven</forename>
              <forename>J.</forename>
              <surname>DeRose</surname>
            </author>
            <author>
              <forename>David</forename>
              <forename>G.</forename>
              <surname>Durand</surname>
            </author>
            <author>
              <forename>Elli</forename>
              <surname>Mylonas</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">What is Text, Really?</title>
            <idno type="DOI">10.1145/264842.264843</idno>
          </analytic>
          <monogr>
            <title level="j">Journal of Computer Documentation</title>
            <imprint>
              <biblScope unit="vol">21</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1997</date>
              <biblScope unit="pp">1–24</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b626

### Block 627

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[31]`.

```xml
<biblStruct xml:id="Goldfarb1981">
          <analytic>
            <author>
              <forename>Charles</forename>
              <forename>F.</forename>
              <surname>Goldfarb</surname>
            </author>
            <title level="a">A Generalized Approach to Document Markup</title>
            <ptr target="http://users.nyct.net/~aray/notes/igm.html"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of the ACM SIGPLAN SIGOA Symposium on Text
              Manipulation</title>
            <imprint>
              <pubPlace>New York</pubPlace>
              <publisher>ACM</publisher>
              <date>1981</date>
              <biblScope>68–73</biblScope>
            </imprint>
          </monogr>
          <note>Adapted as "Annex A. Introduction to Generalized Markup" in ISO 8879</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b627

### Block 628

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[32]`.

```xml
<biblStruct xml:id="Graham1999">
          <analytic>
            <author>
              <forename>Tony</forename>
              <surname>Graham</surname>
            </author>
            <title level="a">Unicode: What Is It and How Do I Use It?</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory &amp; Practice</title>
            <imprint>
              <biblScope unit="vol">1</biblScope>
              <biblScope unit="issue">4</biblScope>
              <date>1999</date>
              <biblScope unit="pp">75</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b628

### Block 629

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[33]`.

```xml
<biblStruct xml:id="Hockey1996">
          <analytic>
            <author>
              <forename>Susan</forename>
              <surname>Hockey</surname>
            </author>
            <title level="a">Creating and Using Electronic Editions</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Richard</forename>
              <forename>J.</forename>
              <surname>Finneran</surname>
            </editor>
            <title level="m">The Literary Text in the Digital Age</title>
            <imprint>
              <pubPlace>Ann Arbor, MI</pubPlace>
              <publisher>University of Michigan Press</publisher>
              <date>1996</date>
              <biblScope unit="pp">1–22</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b629

### Block 630

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[34]`.

```xml
<biblStruct xml:id="Hockeyetal1999">
          <monogr>
            <author>
              <forename>Susan</forename>
              <surname>Hockey</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>Jerome</forename>
              <forename>J.</forename>
              <surname>McGann</surname>
            </author>
            <title level="m">What is Text? A Debate on the Philosophical and Epistemological Nature
              of Text in the Light of Humanities Computing Research</title>
            <ptr target="http://www2.iath.virginia.edu/ach-allc.99/proceedings/hockey-renear2.html"/>
            <imprint>
              <date>1999</date>
            </imprint>
          </monogr>
          <note>Panel presented at ACH/ALLC 1999</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b630

### Block 631

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[35]`.

```xml
<biblStruct xml:id="Hockey2000">
          <monogr>
            <author>
              <forename>Susan</forename>
              <surname>Hockey</surname>
            </author>
            <title level="m">Electronic Texts in the Humanities</title>
            <imprint>
              <pubPlace>New York, NY</pubPlace>
              <publisher>Oxford University Press</publisher>
              <date>2000</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b631

### Block 632

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[36]`.

```xml
<biblStruct xml:id="Huitfeldt1994a">
          <analytic>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <title level="a">Multi-dimensional Texts in a One-dimensional Medium</title>
            <idno type="DOI">10.1007/BF01830270</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">28</biblScope>
              <biblScope unit="issue">4/5</biblScope>
              <date>1994</date>
              <biblScope unit="pp">235–241</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b632

### Block 633

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[37]`.

```xml
<biblStruct xml:id="Huitfeldt1994b">
          <analytic>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <title level="a">Toward a Machine-Readable Version of Wittgenstein's Nachlaß: Some
              Editorial Problems</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Hans</forename>
              <forename>Gerhard</forename>
              <surname>Senger</surname>
            </editor>
            <title level="m">Philosophische Editionen. Erwartungen an sie — Wirkungen durch
              sie</title>
            <imprint>
              <pubPlace>Tübingen</pubPlace>
              <publisher>Max Niemeyer Verlag</publisher>
              <date>1994</date>
              <biblScope unit="pp">37–43</biblScope>
            </imprint>
          </monogr>
          <series>
            <title level="s">Beihefte zu editio</title>
            <biblScope unit="vol">6</biblScope>
          </series>
        </biblStruct>
```

^b633

### Block 634

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[38]`.

```xml
<biblStruct xml:id="Lamport1987">
          <analytic>
            <author>
              <forename>Leslie</forename>
              <surname>Lamport</surname>
            </author>
            <title level="a">Document Production: Visual or Logical?</title>
            <ptr target="http://research.microsoft.com/en-us/um/people/lamport/pubs/pubs.html#document-production"/>
          </analytic>
          <monogr>
            <title level="j">Notices of the American Mathematical Society</title>
            <imprint>
              <biblScope unit="vol">34</biblScope>
              <date>1987</date>
              <biblScope unit="pp">621–624</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <note>Republished as <ptr target="#Lamport1988a"/></note>
        </biblStruct>
```

^b634

### Block 635

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[39]`.

```xml
<biblStruct xml:id="Lamport1988a">
          <analytic>
            <author>
              <forename>Leslie</forename>
              <surname>Lamport</surname>
            </author>
            <title level="a">Document Production: Visual or Logical?</title>
            <ptr target="http://www.tug.org/TUGboat/Articles/tb09-1/tb20lamport.pdf"/>
          </analytic>
          <monogr>
            <title level="j">TUGboat</title>
            <imprint>
              <biblScope unit="vol">9</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1988</date>
              <biblScope unit="pp">8-10</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b635

### Block 636

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[40]`.

```xml
<biblStruct xml:id="Lavagnino1996">
          <analytic>
            <author>
              <forename>John</forename>
              <surname>Lavagnino</surname>
            </author>
            <title level="a">Completeness and Adequacy in Text Encoding</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Richard</forename>
              <forename>J.</forename>
              <surname>Finneran</surname>
            </editor>
            <title level="m">The Literary Text in the Digital Age</title>
            <imprint>
              <pubPlace>Ann Arbor, MI</pubPlace>
              <publisher>University of Michigan Press</publisher>
              <date>1996</date>
              <biblScope unit="pp">63–76</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b636

### Block 637

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[41]`.

```xml
<biblStruct xml:id="Lightfoot1979">
          <monogr>
            <author>
              <forename>Charles</forename>
              <surname>Lightfoot</surname>
            </author>
            <title level="m">Generic Textual Element Identification—A Primer</title>
            <imprint>
              <pubPlace>Arlington</pubPlace>
              <publisher>Graphic Communications Computer Association</publisher>
              <date>1979</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b637

### Block 638

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[42]`.

```xml
<biblStruct xml:id="Lubell1999">
          <analytic>
            <author>
              <forename>Joshua</forename>
              <surname>Lubell</surname>
            </author>
            <title level="a">Structured Markup on the Web: A Tale of Two Sites</title>
            <ptr target="http://www.mel.nist.gov/msidlibrary/doc/mlang/markuplang.htm"/>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory &amp; Practice</title>
            <imprint>
              <biblScope unit="vol">1</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1999</date>
              <biblScope unit="pp">7–22</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b638

### Block 639

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[43]`.

```xml
<biblStruct xml:id="McEneryetal1998">
          <monogr>
            <author>
              <forename>Tony</forename>
              <surname>McEnery</surname>
            </author>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Andrew</forename>
              <surname>Wilson</surname>
            </author>
            <author>
              <forename>Paul</forename>
              <surname>Baker</surname>
            </author>
            <title level="m">Validation of Linguistic Corpora</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/ELRA/WP3/"/>
            <imprint>
              <date>1998</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <note>Report commissioned by ELRA</note>
        </biblStruct>
```

^b639

### Block 640

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[44]`.

```xml
<biblStruct xml:id="McGann1997">
          <analytic>
            <author>
              <forename>Jerome</forename>
              <surname>McGann</surname>
            </author>
            <title level="a">The Rationale of Hypertext</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Kathryn</forename>
              <surname>Sutherland</surname>
            </editor>
            <title level="m">Electronic Text: Investigations in Method and Theory</title>
            <imprint>
              <pubPlace>New York, NY</pubPlace>
              <publisher>Clarendon Press Oxford</publisher>
              <date>1997</date>
              <biblScope unit="pp">19–46</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b640

### Block 641

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[45]`.

```xml
<biblStruct xml:id="McGann2001">
          <monogr>
            <author>
              <forename>Jerome</forename>
              <surname>McGann</surname>
            </author>
            <title level="m">Radiant Textuality: Literature After the World Wide Web</title>
            <imprint>
              <pubPlace>New York, NY</pubPlace>
              <publisher>Palgrave Macmillian</publisher>
              <date>2001</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b641

### Block 642

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[46]`.

```xml
<biblStruct xml:id="McGann2004">
          <analytic>
            <author>
              <forename>Jerome</forename>
              <surname>McGann</surname>
            </author>
            <title level="a">Marking Texts of Many Dimensions</title>
            <ptr target="http://www.digitalhumanities.org/companion/"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Susan</forename>
              <surname>Schreibman</surname>
            </editor>
            <editor>
              <forename>Ray</forename>
              <surname>Siemens</surname>
            </editor>
            <editor>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </editor>
            <title level="m">A Companion to Digital Humanities</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Blackwell</publisher>
              <date>2004</date>
              <biblScope unit="pp">198–217</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b642

### Block 643

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[47]`.

```xml
<biblStruct xml:id="Morrisonetalnodate">
          <monogr>
            <author>
              <forename>Alan</forename>
              <surname>Morrison</surname>
            </author>
            <author>
              <forename>Michael</forename>
              <surname>Popham</surname>
            </author>
            <author>
              <forename>Karen</forename>
              <surname>Wikander</surname>
            </author>
            <title level="m">Creating and Documenting Electronic Texts: A Guide to Good
              Practice</title>
            <ptr type="winita" target="http://ota.ox.ac.uk/documents/creating/cdet/"/>
            <imprint>
              <date>(no date)</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b643

### Block 644

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[48]`.

```xml
<biblStruct xml:id="Pichler1995">
          <analytic>
            <author>
              <forename>Alois</forename>
              <surname>Pichler</surname>
            </author>
            <title level="a">Advantages of a Machine-Readable Version of Wittgenstein's
              Nachlaß</title>
            <ptr type="winita" target="http://hdl.handle.net/1956/1875"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Kjell</forename>
              <forename>S.</forename>
              <surname>Johannessen</surname>
            </editor>
            <editor>
              <forename>Tore</forename>
              <surname>Nordenstam</surname>
            </editor>
            <title level="m">Culture and Value: Philosophy and the Cultural Sciences. Beiträge des
              18. Internationalen Wittgenstein Symposiums 13–20. August 1995 Kirchberg am
              Wechsel</title>
            <imprint>
              <pubPlace>Kirchberg am Wechsel</pubPlace>
              <publisher>Die Österreichische Ludwig Wittgenstein Gesellschaft</publisher>
              <date>1995</date>
              <biblScope unit="pp">770–776</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <!--idno type="handle">1956/1875</idno-->
        </biblStruct>
```

^b644

### Block 645

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[49]`.

```xml
<biblStruct xml:id="Piez2001">
          <analytic>
            <author>
              <forename>Wendell</forename>
              <surname>Piez</surname>
            </author>
            <title level="a">Beyond the 'Descriptive vs. Procedural' Distinction</title>
            <ptr target="http://conferences.idealliance.org/extreme/html/2001/Piez01/EML2001Piez01.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>B.</forename>
              <forename>Tommie</forename>
              <surname>Usdin</surname>
            </editor>
            <editor>
              <forename>Steven</forename>
              <forename>R.</forename>
              <surname>Newcomb</surname>
            </editor>
            <title level="m">Proceedings of Extreme Markup Languages 2001: Montreal, Canada</title>
            <imprint>
              <date>2001</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b645

### Block 646

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[50]`.

```xml
<biblStruct xml:id="Popham1996">
          <analytic>
            <author>
              <forename>Michael</forename>
              <surname>Popham</surname>
            </author>
            <title level="a">What Is Markup and Why Does It Matter</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Michael</forename>
              <surname>Popham</surname>
            </editor>
            <editor>
              <forename>Lorna</forename>
              <surname>Hughes</surname>
            </editor>
            <title level="m">Computers and Teaching in the Humanities: Selected Papers from the
              CATH94 Conference held in Glasgow University September 9th-12th 1994</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>CTI Centre for Textual Studies</publisher>
              <date>1996</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b646

### Block 647

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[51]`.

```xml
<biblStruct xml:id="Quin1996">
          <analytic>
            <author>
              <forename>Liam</forename>
              <surname>Quin</surname>
            </author>
            <title level="a">Suggestive Markup: Explicit Relationships in Descriptive and
              Prescriptive DTDs</title>
            <ptr target="https://www.holoweb.net/liam/papers/1996-sgml96-SuggestiveMarkup/"/>
          </analytic>
          <monogr>
            <editor>
              <forename>B.</forename>
              <forename>Tommie</forename>
              <surname>Usdin</surname>
            </editor>
            <editor>
              <forename>Deborah</forename>
              <forename>A.</forename>
              <surname>Lapeyre</surname>
            </editor>
            <title level="m">SGML'96 Conference Proceedings</title>
            <imprint>
              <pubPlace>Alexandria, VA</pubPlace>
              <publisher>Graphic Communications Association</publisher>
              <date>1996</date>
              <biblScope unit="pp">405–418</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b647

### Block 648

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[52]`.

```xml
<biblStruct xml:id="Raymondetal1996">
          <analytic>
            <author>
              <forename>Darrell</forename>
              <surname>Raymond</surname>
            </author>
            <author>
              <forename>Frank</forename>
              <surname>Tompa</surname>
            </author>
            <author>
              <forename>Derick</forename>
              <surname>Wood</surname>
            </author>
            <title level="a">From Data Representation to Data Model: Meta-Semantic Issues in the
              Evolution of SGML</title>
            <ptr target="https://cs.uwaterloo.ca/~fwtompa/.papers/sgml.ps                                                         http://www.sciencedirect.com/science/article/pii/0920548996000335                                                         http://dl.acm.org/citation.cfm?id=1648954"/>
          </analytic>
          <monogr>
            <title level="j">Computer Standards &amp; Interfaces</title>
            <imprint>
              <biblScope unit="vol">18</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1996</date>
              <biblScope unit="pp">25–36</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b648

### Block 649

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[53]`.

```xml
<biblStruct xml:id="Renearetal1996">
          <analytic>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Durand</surname>
            </author>
            <author>
              <forename>Elli</forename>
              <surname>Mylonas</surname>
            </author>
            <title level="a">Refining our Notion of What Text Really Is: The Problem of Overlapping
              Hierarchies</title>
            <ptr target="http://cds.library.brown.edu/resources/stg/monographs/ohco.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Susan</forename>
              <surname>Hockey</surname>
            </editor>
            <editor>
              <forename>Nancy</forename>
              <surname>Ide</surname>
            </editor>
            <title level="m">Research in Humanities Computing 4: Selected Papers from the 1992
              ALLC/ACH Conference</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Oxford University Press</publisher>
              <date>1996</date>
              <biblScope unit="pp">263–280</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b649

### Block 650

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[54]`.

```xml
<biblStruct xml:id="Renear1997">
          <analytic>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Out of Praxis: Three (Meta)Theories of Textuality</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Kathryn</forename>
              <surname>Sutherland</surname>
            </editor>
            <title level="m">Electronic Text: Investigations in Method and Theory</title>
            <imprint>
              <pubPlace>New York, NY</pubPlace>
              <publisher>Clarendon Press Oxford</publisher>
              <date>1997</date>
              <biblScope unit="pp">107–126</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b650

### Block 651

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[55]`.

```xml
<biblStruct xml:id="Renear2000">
          <analytic>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">The Descriptive/Procedural Distinction is Flawed</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory and Practice</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <biblScope unit="issue">4</biblScope>
              <date>2000</date>
              <biblScope unit="pp">411–420</biblScope>
            </imprint>
          </monogr>
          <!--<note>This is a slightly revised version of a paper presented at Extreme Markup
                                              Languages 2000 (Montreal, Canada). An earlier version was published in that
                                              conference's proceedings, and still earlier versions were presented in May
                                              1998 at the HIT Center at the University of Bergen and in July 1998 at the
                                              Oxford University Humanities Computing Unit.</note>-->
        </biblStruct>
```

^b651

### Block 652

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[56]`.

```xml
<biblStruct xml:id="Renearetal2002">
          <analytic>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Dubin</surname>
            </author>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Towards a Semantics for XML Markup</title>
            <idno type="DOI">10.1145/585058.585081</idno>
          </analytic>
          <monogr>
            <editor>
              <forename>Richard</forename>
              <surname>Furuta</surname>
            </editor>
            <editor>
              <forename>Jonathan</forename>
              <forename>I.</forename>
              <surname>Maletic</surname>
            </editor>
            <editor>
              <forename>Ethan</forename>
              <forename>V.</forename>
              <surname>Munson</surname>
            </editor>
            <title level="m">Proceedings of the 2002 ACM Symposium on Document Engineering</title>
            <imprint>
              <pubPlace>McLean, VA</pubPlace>
              <publisher>Association for Computing Machinery</publisher>
              <date>2002</date>
              <biblScope unit="pp">119–126</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b652

### Block 653

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[57]`.

```xml
<biblStruct xml:id="Renearetal2003a">
          <analytic>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>Christopher</forename>
              <surname>Phillippe</surname>
            </author>
            <author>
              <forename>Pat</forename>
              <surname>Lawton</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Dubin</surname>
            </author>
            <title level="a">An XML Document Corresponds to Which FRBR Group 1 Entity?</title>
            <!-- MDH 2014-01-22 Note: This had two ptrs. The first ptr was a 301, so I've updated it; second was 404, so I've deleted it.  -->
            <ptr target="http://conferences.idealliance.org/extreme/html/2003/Lawton01/EML2003Lawton01.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>B.</forename>
              <forename>Tommie</forename>
              <surname>Usdin</surname>
            </editor>
            <editor>
              <forename>Steven</forename>
              <forename>R.</forename>
              <surname>Newcomb</surname>
            </editor>
            <title level="m">Proceedings of Extreme Markup Languages 2003: Montreal, Canada</title>
            <imprint>
              <date>2003</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b653

### Block 654

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[58]`.

```xml
<biblStruct xml:id="Renearetal2003b">
          <analytic>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Dubin</surname>
            </author>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <title level="a">XML Semantics and Digital Libraries</title>
            <ptr target="http://dl.acm.org/citation.cfm?id=827192"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of the 3rd ACM/IEEE–CS Joint Conference on Digital
              Libraries</title>
            <imprint>
              <pubPlace>Los Alamitos, CA</pubPlace>
              <publisher>IEEE Computer Society</publisher>
              <date>2003</date>
              <biblScope unit="pp">303–305</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b654

### Block 655

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[59]`.

```xml
<biblStruct xml:id="Renear2004">
          <analytic>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Text Encoding</title>
            <ptr target="http://www.digitalhumanities.org/companion/"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Susan</forename>
              <surname>Schreibman</surname>
            </editor>
            <editor>
              <forename>Ray</forename>
              <surname>Siemans</surname>
            </editor>
            <editor>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </editor>
            <title level="m">A Companion to Digital Humanities</title>
            <imprint>
              <pubPlace>Oxford</pubPlace>
              <publisher>Blackwell</publisher>
              <date>2004</date>
              <biblScope unit="pp">218–239</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b655

### Block 656

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[60]`.

```xml
<biblStruct xml:id="SalmonAlt2006">
          <analytic>
            <author>
              <forename>Susanne</forename>
              <surname>Salmon-Alt</surname>
            </author>
            <title level="a">Data Structures for Etymology: Towards an Etymological Lexical
              Network</title>
            <ptr target="http://hal.archives-ouvertes.fr/docs/00/11/09/71/PDF/etymology_final_bulag.pdf"/>
          </analytic>
          <monogr>
            <title level="j" type="main">BULAG: revue internationale annuelle</title>
            <title level="j" type="sub">Numéro Etymologie</title>
            <imprint>
              <biblScope unit="vol">31</biblScope>
              <date>2006</date>
              <pubPlace>Besançon</pubPlace>
              <publisher>Presses Universitaires de Franche-Comté</publisher>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b656

### Block 657

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[61]`.

```xml
<biblStruct xml:id="Schreibman2002a">
          <analytic>
            <author>
              <forename>Susan</forename>
              <surname>Schreibman</surname>
            </author>
            <title level="a">Computer-mediated Texts and Textuality: Theory and Practice</title>
            <idno type="DOI">10.1023/A:1016178200469</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">36</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2002</date>
              <biblScope unit="pp">283–293</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b657

### Block 658

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[62]`.

```xml
<biblStruct xml:id="Schreibman2002b">
          <analytic>
            <author>
              <forename>Susan</forename>
              <surname>Schreibman</surname>
            </author>
            <title level="a">The Text Ported</title>
            <idno type="DOI">10.1093/llc/17.1.77</idno>
          </analytic>
          <monogr>
            <title level="j">Literary and Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">17</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2002</date>
              <biblScope unit="pp">77–87</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b658

### Block 659

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[63]`.

```xml
<biblStruct xml:id="SGMLUsersGroup1990">
          <monogr>
            <author>
              <orgName>SGML Users' Group</orgName>
            </author>
            <title level="m">A Brief History of the Development of SGML</title>
            <ptr target="http://www.sgmlsource.com/history/sgmlhist.htm"/>
            <imprint>
              <date>1990</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b659

### Block 660

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[64]`.

```xml
<biblStruct xml:id="ShipmanandMarshall1999">
          <analytic>
            <author>
              <forename>Frank</forename>
              <forename>M.</forename>
              <surname>Shipman</surname>
              <genName>III</genName>
            </author>
            <author>
              <forename>Catherine</forename>
              <forename>C.</forename>
              <surname>Marshall</surname>
            </author>
            <title level="a">Formality Considered Harmful: Experiences, Emerging Themes, and
              Directions on the Use of Formal Representations in Interactive Systems</title>
            <idno type="DOI">10.1023/A:1008716330212</idno>
            <ptr target="http://www.csdl.tamu.edu/~shipman/papers/cscw.pdf"/>
          </analytic>
          <monogr>
            <title level="j">Computer-Supported Cooperative Work</title>
            <imprint>
              <biblScope unit="vol">8</biblScope>
              <biblScope unit="issue">4</biblScope>
              <date>1999</date>
              <biblScope unit="pp">333–352</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b660

### Block 661

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[65]`.

```xml
<biblStruct xml:id="SperbergMcQueenandHuitfeldt1999">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <title level="a">Concurrent document hierarchies in MECS and SGML</title>
            <idno type="DOI">10.1093/llc/14.1.29</idno>
          </analytic>
          <monogr>
            <title level="j">Literary and Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">14</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1999</date>
              <biblScope unit="pp">29–42</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b661

### Block 662

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[66]`.

```xml
<biblStruct xml:id="SperbergMcQueenetal2000">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <forename>H.</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Meaning and Interpretation in Markup</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory and Practice</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2000</date>
              <biblScope unit="pp">215–234</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b662

### Block 663

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[67]`.

```xml
<biblStruct xml:id="SperbergMcQueenetal2002">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <author>
              <forename>David</forename>
              <surname>Dubin</surname>
            </author>
            <author>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Drawing Inferences on the Basis of Markup</title>
            <!--         MDH 2014-01-22 Note: There were two ptrs; the first was a 301 redirect, so I've updated it, and the second was a 404, so I've deleted it.   -->
            <ptr target="http://conferences.idealliance.org/extreme/html/2002/CMSMcQ01/EML2002CMSMcQ01.html"/>
          </analytic>
          <monogr>
            <editor>
              <forename>B.</forename>
              <forename>Tommie</forename>
              <surname>Usdin</surname>
            </editor>
            <editor>
              <forename>Steven</forename>
              <forename>R.</forename>
              <surname>Newcomb</surname>
            </editor>
            <title level="m">Proceedings of Extreme Markup Languages 2002: Montreal, Canada</title>
            <imprint>
              <date>2002</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b663

### Block 664

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[68]`.

```xml
<biblStruct xml:id="Sukovic2002">
          <analytic>
            <author>
              <forename>Suzana</forename>
              <surname>Sukovic</surname>
            </author>
            <title level="a">Beyond the Scriptorium: The Role of the Library in Text
              Encoding</title>
            <ptr target="http://www.dlib.org/dlib/january02/sukovic/01sukovic.html"/>
          </analytic>
          <monogr>
            <title level="j">D-Lib</title>
            <imprint>
              <biblScope unit="vol">8</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2002</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b664

### Block 665

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[69]`.

```xml
<biblStruct xml:id="UniversityofNebraskaLincolnLibraries2003">
          <monogr>
            <author>
              <orgName>University of Nebraska — Lincoln Libraries</orgName>
            </author>
            <title level="m">A Basic Guide to Text Encoding</title>
            <!--         MDH: 2014-01-22 Note: This is a 404 as of this date.    -->
            <!-- MDH: 2016-09-01 Note: Found an alternative URL, which I'll substitute
                                                 for now; I presume it's the same document. -->
            <!--<ptr target="http://libr.unl.edu:2000/guide_site/teien.html"/>-->
            <ptr target="http://cdrh.unl.edu/book/export/html/2428"/>
            <imprint>
              <date>2003</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b665

### Block 666

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[70]`.

```xml
<biblStruct xml:id="Unsworth2001">
          <monogr>
            <author>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </author>
            <title level="m">Knowledge Representation in Humanities Computing</title>
            <ptr target="http://people.brandeis.edu/~unsworth/KR/"/>
            <imprint>
              <date>2001</date>
            </imprint>
          </monogr>
          <note>Lecture I in the eHumanities NEH Lecture Series on Technology &amp; the Humanities,
            Washington, DC, April 3, 2001</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b666

### Block 667

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[71]`.

```xml
<biblStruct xml:id="Unsworth2000">
          <monogr>
            <author>
              <forename>John</forename>
              <surname>Unsworth</surname>
            </author>
            <title level="m">Scholarly Primitives: What Methods Do Humanities Researchers Have in
              Common, How Might Our Tools Reflect This?</title>
            <ptr target="http://people.brandeis.edu/~unsworth/Kings.5-00/primitives.html"/>
            <imprint>
              <date>2000</date>
            </imprint>
          </monogr>
          <note> Part of a Symposium on "Humanities Computing: Formal Methods, Experimental
            Practice" sponsored by King's College, London</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b667

### Block 668

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[72]`.

```xml
<biblStruct xml:id="Vitalietal2000">
          <analytic>
            <author>
              <forename>Fabio</forename>
              <surname>Vitali</surname>
            </author>
            <author>
              <forename>Luca</forename>
              <surname>Bompani</surname>
            </author>
            <author>
              <forename>Paolo</forename>
              <surname>Ciancarini</surname>
            </author>
            <title level="a">Hypertext Functionalities with XML</title>
          </analytic>
          <monogr>
            <title level="j">Markup Languages: Theory &amp; Practice</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <biblScope unit="issue">4</biblScope>
              <date>2000</date>
              <biblScope unit="pp">389</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b668

### Block 669

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[73]`.

```xml
<biblStruct xml:id="Watson1992">
          <monogr>
            <author>
              <forename>Dennis</forename>
              <forename>G.</forename>
              <surname>Watson</surname>
            </author>
            <title level="m">Brief History of Document Markup</title>
            <ptr target="http://chnm.gmu.edu/digitalhistory/links/pdf/chapter3/3.19a.pdf"/>
            <imprint>
              <date>1992</date>
            </imprint>
          </monogr>
          <note>Circular 1086. Florida Cooperative Extension Service, Institute of Food and
            Agricultural Sciences, University of Florida</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b669

### Block 670

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[74]`.

```xml
<biblStruct xml:id="Weelnodate">
          <analytic>
            <author>
              <forename>Adriaan</forename>
              <nameLink>van der</nameLink>
              <surname>Weel</surname>
            </author>
            <title level="a">The Concept of Markup</title>
            <ptr target="https://docmh.com/adriaan-van-der-weel-digital-text-and-the-gutenberg-heritage-pdf"/>
          </analytic>
          <monogr>
            <title level="m">Digital Text and the Gutenberg Heritage</title>
            <imprint>
              <date>(no date)</date>
              <biblScope unit="chap">3</biblScope>
            </imprint>
          </monogr>
          <note>in preparation; draft only</note>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b670

### Block 671

XML location: `/div[1]/div[3]/div[1]/listBibl[1]/biblStruct[75]`.

```xml
<biblStruct xml:id="WeltyandIde1999">
          <analytic>
            <author>
              <forename>Christopher</forename>
              <surname>Welty</surname>
            </author>
            <author>
              <forename>Nancy</forename>
              <surname>Ide</surname>
            </author>
            <title level="a">Using the Right Tools: Enhancing Retrieval from Marked-up
              Documents</title>
            <idno type="DOI">10.1023/A:1001800717376</idno>
            <ptr target="http://link.springer.com/article/10.1023/A%3A1001800717376"/>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1–2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">59–84</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b671

### Block 672

XML location: `/div[1]/div[3]/div[2]/head[1]`.

```xml
<head>TEI</head>
```

^b672

### Block 673

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[1]`.

```xml
<biblStruct xml:id="Bauman1996">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <title level="a">Keying NAMEs: the WWP Approach</title>
            <ptr target="http://www.wwp.brown.edu/about/history/archive/newsletter/vol02num03/nameKey-home.html"/>
          </analytic>
          <monogr>
            <title level="j">Brown University Women Writers Project Newsletter</title>
            <imprint>
              <biblScope unit="vol">2</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1996</date>
              <biblScope unit="pp">3–6</biblScope>
              <biblScope unit="pp">10–11</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b673

### Block 674

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[2]`.

```xml
<biblStruct xml:id="BaumanandFlanders2004">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <author>
              <forename>Julia</forename>
              <surname>Flanders</surname>
            </author>
            <title level="a">Odd Customizations</title>
            <ptr target="http://conferences.idealliance.org/extreme/html/2004/Bauman01/EML2004Bauman01.html"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of Extreme Markup Languages 2004</title>
            <imprint>
              <date>2004</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b674

### Block 675

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[3]`.

```xml
<biblStruct xml:id="Bauman1995">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <title level="a">Tables of Contents TEI-style</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </editor>
            <title level="j" type="main">TEXT Technology: The Journal of Computer Text
              Processing</title>
            <title level="j" type="sub">Electronic Texts and the Text Encoding Initiative. A Special
              Issue of TEXT Technology</title>
            <imprint>
              <biblScope unit="vol">5</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>1995</date>
              <pubPlace>Madison, SD</pubPlace>
              <publisher>College of Liberal Arts, Dakota State University</publisher>
              <biblScope unit="pp">235–247</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b675

### Block 676

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[4]`.

```xml
<biblStruct xml:id="BaumanandCatapano1999">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <author>
              <forename>Terry</forename>
              <surname>Catapano</surname>
            </author>
            <title level="a">TEI and the Encoding of the Physical Structure of Books</title>
            <idno type="DOI">10.1023/A:1001769103586</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1–2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">113–127</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b676

### Block 677

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[5]`.

```xml
<biblStruct xml:id="Bauman2005">
          <analytic>
            <author>
              <forename>Syd</forename>
              <surname>Bauman</surname>
            </author>
            <title level="a">TEI HORSEing Around</title>
            <ptr target="http://conferences.idealliance.org/extreme/html/2005/Bauman01/EML2005Bauman01.html"/>
          </analytic>
          <monogr>
            <title level="m">Proceedings of the Extreme Markup Languages 2005</title>
            <imprint>
              <date>2005</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b677

### Block 678

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[6]`.

```xml
<biblStruct xml:id="Brown1994">
          <analytic>
            <author>
              <forename>Malcolm</forename>
              <forename>B.</forename>
              <surname>Brown</surname>
            </author>
            <title level="a">What is the TEI?</title>
          </analytic>
          <monogr>
            <title level="j">Information Technology and Libraries</title>
            <imprint>
              <biblScope unit="vol">13</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1994</date>
              <biblScope unit="pp">8</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b678

### Block 679

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[7]`.

```xml
<biblStruct xml:id="Burnard1992">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">The Text Encoding Initiative: A Progress Report</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Gerhard</forename>
              <surname>Leitner</surname>
            </editor>
            <title level="m">New Directions in Corpus Linguistics</title>
            <imprint>
              <pubPlace>Berlin</pubPlace>
              <publisher>Mouton de Gruyter</publisher>
              <date>1992</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b679

### Block 680

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[8]`.

```xml
<biblStruct xml:id="Burnard1993">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">Rolling your own with the TEI</title>
          </analytic>
          <monogr>
            <title level="j">Information Services and Use</title>
            <imprint>
              <biblScope unit="vol">13</biblScope>
              <biblScope unit="issue">2</biblScope>
              <date>1993</date>
              <pubPlace>Amsterdam</pubPlace>
              <publisher>IOS Press</publisher>
              <biblScope unit="pp">141–154</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b680

### Block 681

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[9]`.

```xml
<biblStruct xml:id="Burnard1994">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">The TEI: Towards an Extensible Standard for the Encoding of
              Texts</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Seamus</forename>
              <surname>Ross</surname>
            </editor>
            <editor>
              <forename>Edward</forename>
              <surname>Higgs</surname>
            </editor>
            <title level="m">Electronic Information Resources and Historians</title>
            <imprint>
              <pubPlace>London</pubPlace>
              <publisher>British Academy</publisher>
              <date>1994</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b681

### Block 682

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[10]`.

```xml
<biblStruct xml:id="Burnard1995">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="a">The Text Encoding Initiative: An Overview</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Geoffrey</forename>
              <surname>Leech</surname>
            </editor>
            <editor>
              <forename>Greg</forename>
              <surname>Myers</surname>
            </editor>
            <editor>
              <forename>Jenny</forename>
              <surname>Thomas</surname>
            </editor>
            <title level="m">Spoken English on Computer: Transcription, Mark-up and
              Application</title>
            <imprint>
              <pubPlace>London</pubPlace>
              <publisher>Longman</publisher>
              <date>1995</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b682

### Block 683

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[11]`.

```xml
<biblStruct xml:id="Burnard1997">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">The Text Encoding Initiative's Recommendations for the Encoding of
              Language Corpora: Theory and Practice</title>
            <ptr target="http://users.ox.ac.uk/~lou/wip/Soria/"/>
            <imprint>
              <date>1997</date>
            </imprint>
          </monogr>
          <note>Prepared for a seminar on Etiquetación y extracción de información de grandes corpus
            textuales within the Curso Industrias de la Lengua (14–18 de Julio de 1997). Sponsored
            by the Fundacion Duques de Soria.</note>
        </biblStruct>
```

^b683

### Block 684

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[12]`.

```xml
<biblStruct xml:id="BurnardandPopham1999">
          <analytic>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <author>
              <forename>Michael</forename>
              <surname>Popham</surname>
            </author>
            <title level="a">Putting Our Headers Together: A Report on the TEI Header Meeting 12
              September 1997</title>
            <idno type="DOI">10.1023/A:1001710828622</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <pubPlace>Dordrecht, Boston</pubPlace>
              <publisher>Kluwer Academic Publishers</publisher>
              <biblScope unit="pp">39–47</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b684

### Block 685

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[13]`.

```xml
<biblStruct xml:id="AB-eg-02">
          <monogr>
            <title>An Agreement to Establish a Consortium for the Maintenance of the Text Encoding
              Initiative</title>
            <ptr target="http://www.tei-c.org/About/consortium.html"/>
            <imprint>
              <date>March 1999</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b685

### Block 686

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[14]`.

```xml
<biblStruct xml:id="AB-eg-03">
          <monogr>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">Text Encoding for Interchange: A New Consortium</title>
            <ptr target="http://www.ariadne.ac.uk/issue24/tei"/>
            <imprint>
              <date>2000</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b686

### Block 687

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[15]`.

```xml
<biblStruct xml:id="Ciottied2005">
          <monogr>
            <editor>
              <forename>Fabio</forename>
              <surname>Ciotti</surname>
            </editor>
            <title level="m">Il Manuale TEI Lite: Introduzione Alla Codifica Elettronica Dei Testi
              Letterari</title>
            <imprint>
              <pubPlace>Milano</pubPlace>
              <publisher>Sylvestre Bonnard</publisher>
              <date>2005</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b687

### Block 688

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[16]`.

```xml
<biblStruct xml:id="Chang2001">
          <analytic>
            <author>
              <forename>Sheau-Hwang</forename>
              <surname>Chang</surname>
            </author>
            <title level="a">The Implications of TEI</title>
          </analytic>
          <monogr>
            <title level="j">OCLC Systems and Services</title>
            <imprint>
              <biblScope unit="vol">17</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2001</date>
              <biblScope unit="pp">101–103</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b688

### Block 689

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[17]`.

```xml
<biblStruct xml:id="Cournane1997">
          <monogr>
            <author>
              <forename>Mavis</forename>
              <surname>Cournane</surname>
            </author>
            <title level="m">The Application of SGML/TEI to the Processing of Complex, Multi-lingual
              Text</title>
            <note>PhD Dissertation</note>
            <imprint>
              <pubPlace>Cork, Ireland</pubPlace>
              <publisher>University College Cork</publisher>
              <date>1997</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b689

### Block 690

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[18]`.

```xml
<biblStruct xml:id="DigitalLibraryFederation1998">
          <monogr>
            <author>
              <orgName>Digital Library Federation</orgName>
            </author>
            <title level="m">TEI and XML in Digital Libraries: Meeting June 30 and July 1, 1998,
              Library of Congress, Summary/Proceedings</title>
            <!-- MDH 2014-09-05: commented out the link because this document is not public any more.  -->
            <!--<ptr target="http://www.lib.umich.edu/digital-library-production-service-dlps/tei-and-xml-digital-libraries"/>-->
            <imprint>
              <date>1998</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b690

### Block 691

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[19]`.

```xml
<biblStruct xml:id="DigitalLibraryFederation2007">
          <monogr>
            <author>
              <orgName>Digital Library Federation</orgName>
            </author>
            <title level="m" type="main">TEI Text Encoding in Libraries: Guidelines for Best
              Encoding Practices</title>
            <title level="m" type="sub">Version 3.0 (October 2011)</title>
            <ptr target="http://www.tei-c.org/SIG/Libraries/teiinlibraries/main-driver.html"/>
            <imprint>
              <date>2011</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b691

### Block 692

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[20]`.

```xml
<biblStruct xml:id="Finney2006">
          <analytic>
            <author>
              <forename>Timothy</forename>
              <forename>J.</forename>
              <surname>Finney</surname>
            </author>
            <title level="a">Manuscript Markup</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Larry</forename>
              <forename>W.</forename>
              <surname>Hurtado</surname>
            </editor>
            <title level="m">The Freer Biblical Manuscripts: Fresh Studies of an American Treasure
              Trove</title>
            <imprint>
              <pubPlace>Atlanta, GA</pubPlace>
              <publisher>Society of Biblical Literature</publisher>
              <date>2006</date>
              <biblScope unit="pp">263-288</biblScope>
            </imprint>
          </monogr>
          <series>
            <title level="s">Text-critical studies</title>
            <biblScope unit="vol">6</biblScope>
          </series>
        </biblStruct>
```

^b692

### Block 693

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[21]`.

```xml
<biblStruct xml:id="GibsonandRuotolo2003">
          <analytic>
            <author>
              <forename>Matthew</forename>
              <surname>Gibson</surname>
            </author>
            <author>
              <forename>Christine</forename>
              <surname>Ruotolo</surname>
            </author>
            <title level="a">Beyond the Web: TEI, the Digital Library, and the Ebook
              Revolution</title>
            <idno type="DOI">10.1023/A:1021895322291</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">37</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2003</date>
              <biblScope unit="pp">57–63</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b693

### Block 694

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[22]`.

```xml
<biblStruct xml:id="Loiseaunodate">
          <monogr>
            <author>
              <forename>Sylvain</forename>
              <surname>Loiseau</surname>
            </author>
            <title level="m">Les standards : autour d'XML et de la TEI</title>
            <ptr target="http://www.revue-texto.net/Corpus/Manufacture/standards/sommaire.html"/>
            <imprint>
              <date>2002</date>
            </imprint>
          </monogr>
          <!--note>last accessed August 5, 2007</note-->
        </biblStruct>
```

^b694

### Block 695

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[23]`.

```xml
<biblStruct xml:id="MarkoandKelleher2001">
          <analytic>
            <author>
              <forename>Lynn</forename>
              <surname>Marko</surname>
            </author>
            <author>
              <forename>Christina</forename>
              <surname>Kelleher Powell</surname>
            </author>
            <title level="a">Descriptive Metadata Strategy for TEI Headers: A University of Michigan
              Library Case Study</title>
            <idno type="DOI">10.1108/10650750110402585</idno>
          </analytic>
          <monogr>
            <title level="j">OCLC Systems &amp; Services</title>
            <imprint>
              <biblScope unit="vol">17</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2001</date>
              <biblScope unit="pp">117-20</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b695

### Block 696

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[24]`.

```xml
<biblStruct xml:id="Mertz2003">
          <monogr>
            <author>
              <forename>David</forename>
              <surname>Mertz</surname>
            </author>
            <title level="m" type="main">XML Matters: TEI — the Text Encoding Initiative</title>
            <title level="m" type="sub"> An XML Dialect for Archival and Complex Documents</title>
            <ptr target="http://www.ibm.com/developerworks/xml/library/x-matters30/index.html"/>
            <imprint>
              <date>2003</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b696

### Block 697

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[25]`.

```xml
<biblStruct xml:id="Morrison1999">
          <analytic>
            <author>
              <forename>Alan</forename>
              <surname>Morrison</surname>
            </author>
            <title level="a">Delivering Electronic Texts Over the Web: The Current and Planned
              Practices of the Oxford Text Archive</title>
            <idno type="DOI">10.1023/A:1001726011322</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">193-198</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b697

### Block 698

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[26]`.

```xml
<biblStruct xml:id="MylonasandRenear1999">
          <analytic>
            <author>
              <forename>Elli</forename>
              <surname>Mylonas</surname>
            </author>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">The Text Encoding Initiative at 10: Not Just an Interchange Format
              Anymore — But a New Research Community</title>
            <idno type="DOI">10.1023/A:1001832310939</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">1-9</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b698

### Block 699

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[27]`.

```xml
<biblStruct xml:id="Nellhaus2001">
          <analytic>
            <author>
              <forename>Tobin</forename>
              <surname>Nellhaus</surname>
            </author>
            <title level="a">XML, TEI, Digital Libraries in the Humanities</title>
            <ptr target="http://muse.jhu.edu/journals/portal_libraries_and_the_academy/v001/1.3nellhaus.html"/>
          </analytic>
          <monogr>
            <title level="j">Portal: Libraries and the Academy</title>
            <imprint>
              <biblScope unit="vol">1</biblScope>
              <biblScope unit="issue">3</biblScope>
              <date>2001</date>
              <biblScope unit="pp">267-277</biblScope>
            </imprint>
          </monogr>
          <!--note>last accessed August 12, 2007</note-->
        </biblStruct>
```

^b699

### Block 700

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[28]`.

```xml
<biblStruct xml:id="Rahtz2003">
          <monogr>
            <author>
              <forename>Sebastian</forename>
              <surname>Rahtz</surname>
            </author>
            <title level="m">Building TEI DTDs and Schemas on demand</title>
            <!--     Original Oxford site now gone; Internet Archive source used instead.       -->
            <ptr target="https://web.archive.org/web/20150706100318/http://tei.oucs.ox.ac.uk/Talks/2003-05-06-xmleurope2003/xmleurope2003.pdf"/>
            <imprint>
              <date>2003</date>
            </imprint>
          </monogr>
          <note>Paper presented at XML Europe 2003, London, March 2003</note>
        </biblStruct>
```

^b700

### Block 701

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[29]`.

```xml
<biblStruct xml:id="Rahtzetal2004">
          <monogr>
            <author>
              <forename>Sebastian</forename>
              <surname>Rahtz</surname>
            </author>
            <author>
              <forename>Norman</forename>
              <surname>Walsh</surname>
            </author>
            <author>
              <forename>Lou</forename>
              <surname>Burnard</surname>
            </author>
            <title level="m">A unified model for text markup: TEI, Docbook, and beyond</title>
            <ptr target="http://www.tei-c.org/Activities/Workgroups/META/xmleurope2004.pdf"/>
            <imprint>
              <date>2004</date>
            </imprint>
          </monogr>
          <note>Paper presented at XML Europe 2004, Amsterdam, April 2004</note>
        </biblStruct>
```

^b701

### Block 702

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[30]`.

```xml
<biblStruct xml:id="Renear1995">
          <analytic>
            <author>
              <forename>Allen</forename>
              <surname>Renear</surname>
            </author>
            <title level="a">Theory and Metatheory in the Development of Text Encoding</title>
            <ptr target="http://uhra.herts.ac.uk/bitstream/handle/2299/7302/904841.pdf?sequence=2"/>
          </analytic>
          <monogr>
            <editor>
              <forename>Michael</forename>
              <forename>A.</forename>
              <forename>R.</forename>
              <surname>Biggs</surname>
            </editor>
            <editor>
              <forename>Claus</forename>
              <surname>Huitfeldt</surname>
            </editor>
            <title level="m">Philosophy and Electronic Publishing</title>
            <imprint>
              <date>1995</date>
            </imprint>
          </monogr>
          <note>Interactive seminar for the Monist</note>
          <!--note>last accessed December 19, 2006</note-->
        </biblStruct>
```

^b702

### Block 703

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[31]`.

```xml
<biblStruct xml:id="Robinsonnodate">
          <monogr>
            <author>
              <forename>Peter</forename>
              <surname>Robinson</surname>
            </author>
            <title level="m">Making a Digital Edition with TEI and Anastasia</title>
            <ptr target="http://sd-editions.com/AnaServer?teidoc+0+start.anv"/>
            <imprint>
              <date>(no date)</date>
            </imprint>
          </monogr>
          <!--note>last accessed January 26, 2005</note-->
        </biblStruct>
```

^b703

### Block 704

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[32]`.

```xml
<biblStruct xml:id="Seaman1995">
          <monogr>
            <author>
              <forename>David</forename>
              <surname>Seaman</surname>
            </author>
            <title level="m">The Electronic Text Center Introduction to TEI and Guide to Document
              Preparation</title>
            <ptr target="https://web.archive.org/web/20140804000849/etext.lib.virginia.edu/standards/tei/uvatei.html"/>
            <imprint>
              <date>1995</date>
            </imprint>
          </monogr>
        </biblStruct>
```

^b704

### Block 705

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[33]`.

```xml
<biblStruct xml:id="Simons1999">
          <analytic>
            <author>
              <forename>Gary</forename>
              <forename>F.</forename>
              <surname>Simons</surname>
            </author>
            <title level="a">Using Architectural Forms to Map TEI Data into an Object-Oriented
              Database</title>
            <idno type="DOI">10.1023/A:1001765030032</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">85-101</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b705

### Block 706

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[34]`.

```xml
<biblStruct xml:id="Smith1999">
          <analytic>
            <author>
              <forename>David</forename>
              <surname>Smith</surname>
            </author>
            <title level="a">Textual Variation and Version Control in the TEI</title>
            <idno type="DOI">10.1023/A:1001795210724</idno>
          </analytic>
          <monogr>
            <title level="j">Computers and the Humanities</title>
            <imprint>
              <biblScope unit="vol">33</biblScope>
              <biblScope unit="issue">1-2</biblScope>
              <date>1999</date>
              <biblScope unit="pp">103-112</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b706

### Block 707

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[35]`.

```xml
<biblStruct xml:id="SperbergMcQueen1991">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Text in the Electronic Age: Textual Study and Text Encoding, with
              Examples from Medieval Texts</title>
            <idno type="DOI">10.1093/llc/6.1.34</idno>
          </analytic>
          <monogr>
            <title level="j">Literary &amp; Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">6</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>1991</date>
              <biblScope unit="pp">34-46</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b707

### Block 708

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[36]`.

```xml
<biblStruct xml:id="SperbergMcQueen1994">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">The Text Encoding Initiative: Electronic Text Markup for
              Research</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Brett</forename>
              <surname>Sutton</surname>
            </editor>
            <title level="m">Literary Texts in an Electronic Age</title>
            <imprint>
              <pubPlace>Urbana-Champaign, IL</pubPlace>
              <publisher>University of Illinois at Urbana-Champaign, Graduate School of Library and
                Information Science</publisher>
              <date>1994</date>
              <biblScope unit="pp">35–55</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b708

### Block 709

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[37]`.

```xml
<biblStruct xml:id="SperbergMcQueen1996">
          <analytic>
            <author>
              <forename>C.</forename>
              <forename>Michael</forename>
              <surname>Sperberg-McQueen</surname>
            </author>
            <title level="a">Textual Criticism and the Text Encoding Initiative</title>
          </analytic>
          <monogr>
            <editor>
              <forename>Richard</forename>
              <forename>J.</forename>
              <surname>Finneran</surname>
            </editor>
            <title level="m">The Literary Text in the Digital Age</title>
            <imprint>
              <pubPlace>Ann Arbor, MI</pubPlace>
              <publisher>University of Michigan Press</publisher>
              <date>1996</date>
              <biblScope unit="pp">37–62</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b709

### Block 710

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[38]`.

```xml
<biblStruct xml:id="Vanhoutte2004">
          <analytic>
            <author>
              <forename>Edward</forename>
              <surname>Vanhoutte</surname>
            </author>
            <title level="a">An Introduction to the TEI and the TEI Consortium</title>
            <idno type="DOI">10.1093/llc/19.1.9</idno>
          </analytic>
          <monogr>
            <title level="j">Literary &amp; Linguistic Computing</title>
            <imprint>
              <biblScope unit="vol">19</biblScope>
              <biblScope unit="issue">1</biblScope>
              <date>2004</date>
              <biblScope unit="pp">9</biblScope>
            </imprint>
          </monogr>
        </biblStruct>
```

^b710

### Block 711

XML location: `/div[1]/div[3]/div[2]/listBibl[1]/biblStruct[39]`.

```xml
<biblStruct xml:id="RFC4151">
          <monogr>
            <editor>
              <forename>T.</forename>
              <surname>Kindberg</surname>
            </editor>
            <editor>
              <forename>S.</forename>
              <surname>Hawke</surname>
            </editor>
            <title level="m">The 'tag' URI Scheme</title>
            <ptr target="https://www.ietf.org/rfc/rfc4151.txt"/>
            <idno>RFC 4151</idno>
            <imprint>
              <date>2005</date>
              <publisher>IETF</publisher>
            </imprint>
          </monogr>
        </biblStruct>
```

^b711

