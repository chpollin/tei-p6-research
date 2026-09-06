---
type: glossary
term: "Entity identification"
created: 2026-09-06
updated: 2026-09-06
---

# Entity identification

Entity identification links a mention in a text, or a record about an entity, to the entity it
stands for or to an external authority, through a coded identifier or a URI. In TEI P5 4.12.0
the attributes `key` and `ref` of `att.canonical` serve this purpose on a name or referring
string.
[[10_markdown/documents/tei-p5-att.canonical-4.12.0#^r1]]

## Examples

<!-- examples:begin -->
- [[30_assertions/p5-att-canonical-associates-a-name-with-canonical-information-about-its-object]] — In TEI P5 4.12.0, att.canonical associates a representation such as a name or title with canonical information about the object being named or referenced
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s1]]
- [[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]] — In TEI P5 4.12.0, att.canonical provides no semantic basis and suggests no precedence when both key and ref are supplied
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s10]]
- [[30_assertions/p5-att-naming-describes-nymref-through-the-object-named]] — In TEI P5 4.12.0, att.naming describes nymRef as locating the canonical form of the names associated with the object named by the element bearing it
  - [[20_distillates/documents/tei-p5-att.naming-4.12.0#^s3]]
- [[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]] — In TEI P5 4.12.0, att.naming inherits key and ref from att.canonical as two ways of associating a name with its referent, and ref is to be used wherever a direct link to canonical information about the referent can be supplied
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s3]]
- [[30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named]] — In TEI P5 4.12.0, the Guidelines state that the association nymRef makes with a nym has nothing to do with any individual who might use the name
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s56]]
- [[30_assertions/p5-guidelines-distinguish-resolving-a-name-from-treating-it-as-an-object]] — In TEI P5 4.12.0, the Guidelines distinguish the resolution of a name or referring string to its referent through key or ref from the treatment of names as objects in their own right, for whose canonical or normalized form they use the term nym
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s55]]
- [[30_assertions/p5-guidelines-present-three-encodings-of-a-nationality-as-the-same-information]] — In TEI P5 4.12.0, the Guidelines present a generic state of type nationality, a nationality element with the same text and an empty nationality element carrying a key and the dating attribute as encodings of the same information
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s33]]
- [[30_assertions/p5-guidelines-state-that-interchange-is-improved-by-tag-uris-in-ref-instead-of-key]] — In TEI P5 4.12.0, the Guidelines state that interchange is improved by the use of tag URIs in ref instead of key, and point to another section of the Guidelines for the explanation
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s5]]
- [[30_assertions/p5-idno-serves-labels-that-identify-an-object-or-concept-in-a-cataloguing-system-or-a-distributed-system]] — In TEI P5 4.12.0, the English remarks on idno state that the element should be used for labels which identify an object or concept in a formal cataloguing system such as a database or an RDF store, or in a distributed system such as the World Wide Web
  - [[20_distillates/documents/tei-p5-idno-4.12.0#^s12]]
- [[30_assertions/p5-idno-supplies-any-form-of-identifier-used-to-identify-some-object-in-a-standardized-way]] — In TEI P5 4.12.0, the English description of idno states that the element supplies any form of identifier used to identify some object in a standardized way
  - [[20_distillates/documents/tei-p5-idno-4.12.0#^s1]]
- [[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]] — In TEI P5 4.12.0, the key attribute of att.canonical provides an externally defined means of identifying the entity or entities being named, using a coded value of some kind
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s2]]
- [[30_assertions/p5-key-remarks-propose-no-particular-syntax-because-its-form-depends-on-project-practice]] — In TEI P5 4.12.0, the English remarks on key propose no particular syntax for the values of the attribute, because its form will depend entirely on practice within a given project
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s4]]
- [[30_assertions/p5-key-requires-resolution-documentation-for-interchange]] — In TEI P5 4.12.0, the use of key in interchange requires that documentation about how the key is to be resolved be sent to the recipient
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s8]]
- [[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]] — In TEI P5 4.12.0, key serves cases where no direct link is required, because a local convention resolves the reference or because the encoder judges that no resolution is necessary
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s4]]
- [[30_assertions/p5-persname-is-synonymous-with-name-of-type-person]] — In TEI P5 4.12.0, the Guidelines hold persName synonymous with name of type person apart from its own type attribute and treat encodings of one name with rs, name or persName under the same ref as equivalent
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s8]]
- [[30_assertions/p5-prosopography-records-refer-to-external-authorities-through-idno]] — In TEI P5 4.12.0, the Guidelines state that a prosopography record of a named entity commonly refers explicitly to other resources such as name authority files, a gazetteer or a printed book, and follow that statement with a specList naming idno with its type attribute
  - [[20_distillates/documents/tei-p5-guidelines-nd-4.12.0#^s25]]
- [[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]] — In TEI P5 4.12.0, the ref attribute of att.canonical provides an explicit means of locating a full definition or identity for the entity being named by means of one or more URIs
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s5]]
- [[30_assertions/p5-ref-points-directly-to-xml-elements-or-other-resources]] — In TEI P5 4.12.0, the English remarks on the ref attribute require its value to point directly to one or more XML elements or other resources by means of one or more whitespace-separated URIs
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s6]]
- [[30_assertions/p5-simultaneous-key-and-ref-are-not-recommended-without-documentation]] — In TEI P5 4.12.0, the English remarks on att.canonical state that the simultaneous use of both key and ref is not recommended unless documentation explaining the use is provided for interchange, probably in an ODD customization
  - [[20_distillates/documents/tei-p5-att.canonical-4.12.0#^s11]]
- [[30_assertions/p5-testnames-name-of-type-person-in-a-note-carries-a-key-and-no-ref]] — In the TEI P5 4.12.0 test document testnames.xml, a record states a relation to another person inside a note and marks that other person with a name element that carries type person and a key holding an identifier and no ref, so the kind of referent is given by type and the identification of the referent by key
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s6]]
- [[30_assertions/p5-testnames-person-name-form-and-place-carry-three-separate-identifying-values]] — In the TEI P5 4.12.0 test document testnames.xml, a person record carries only an xml:id on the person element, gives its name form a key of its own beside a type value, and identifies the birthplace by a key on placeName that repeats the element text, so the person, the name form and the place carry three separate identifying values
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s14]]
- [[30_assertions/p5-testnames-places-in-birth-and-death-are-named-without-identification-while-a-nationality-is-identified-by-key]] — In the TEI P5 4.12.0 test document testnames.xml, the place names inside birth and death of one record consist of a settlement and a country carrying neither type nor key, so the places are named without being identified, while the same record identifies a nationality by a key on an empty nationality element
  - [[20_distillates/documents/tei-p5-test-testnames-4.12.0#^s18]]
- [[30_assertions/teic-tei-issue-1414-author-proposes-ref-and-key-on-person-and-place]] — In TEIC/TEI issue 1414, the issue author wrote that they thought the best way was to allow ref, and key for the web-impaired, on person and place
  - [[20_distillates/publications/teic-tei-issue-1414#^s3]]
- [[30_assertions/teic-tei-issue-1414-author-proposes-that-a-record-entry-refer-through-ref-or-key-to-further-information-about-the-same-entity]] — In TEIC/TEI issue 1414, the issue author wrote that an entry in a placeography, personography, bibliography or whatever should be able to refer, using ref or key, to some other data structure that has further information about the same entity
  - [[20_distillates/publications/teic-tei-issue-1414#^s1]]
- [[30_assertions/teic-tei-issue-1414-comment-of-2019-reports-that-person-place-org-and-bibl-allow-idno-while-event-and-nym-do-not]] — In TEIC/TEI issue 1414, a comment of 2019-05-07 stated that person, place, org and bibl allowed idno at that time and that event and nym did not
  - [[20_distillates/publications/teic-tei-issue-1414#^s15]]
- [[30_assertions/teic-tei-issue-1414-commenter-summarizes-idno-as-a-first-child-of-the-record-elements-as-the-short-term-solution]] — In TEIC/TEI issue 1414, a commenter summarized the discussion and named adding idno as a first child of the ogrophy elements as the short-term solution
  - [[20_distillates/publications/teic-tei-issue-1414#^s14]]
- [[30_assertions/teic-tei-issue-2739-commenter-states-att-personal-is-a-member-of-att-naming-and-att-naming-of-att-canonical]] — In TEIC/TEI issue 2739, a commenter stated that att.personal is a member of att.naming and that att.naming is a member of att.canonical
  - [[20_distillates/publications/teic-tei-issue-2739#^s4]]
- [[30_assertions/teic-tei-issue-337-author-announces-an-interim-guidelines-change-telling-people-to-switch-to-ref]] — In TEIC/TEI issue 337, the issue author wrote that as an interim measure the Guidelines would be modified to make the point that people should switch to ref wherever key is mentioned
  - [[20_distillates/publications/teic-tei-issue-337#^s5]]
- [[30_assertions/teic-tei-issue-337-author-reports-a-wish-to-deprecate-key-held-back-by-its-wide-use]] — In TEIC/TEI issue 337, the issue author reported a wish to deprecate key some day, held back by how widely the attribute was used at the time of writing
  - [[20_distillates/publications/teic-tei-issue-337#^s4]]
- [[30_assertions/teic-tei-issue-337-commenter-excepts-values-that-already-refer-to-an-external-vocabulary]] — In TEIC/TEI issue 337, a commenter excepted those like a country element with key FR, which already refer to a particular external vocabulary
  - [[20_distillates/publications/teic-tei-issue-337#^s21]]
<!-- examples:end -->
