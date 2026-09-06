---
type: chapter
status: grounded
checked:
  validation: 2026-09-06
assertions:
  - "[[30_assertions/p5-rs-contains-a-general-purpose-name-or-referring-string]]"
  - "[[30_assertions/p5-persname-contains-a-proper-noun-referring-to-a-person]]"
  - "[[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]]"
  - "[[30_assertions/p5-persname-is-synonymous-with-name-of-type-person]]"
  - "[[30_assertions/p5-placename-abbreviates-typed-name-or-rs-at-the-cost-of-their-distinction]]"
  - "[[30_assertions/p5-role-on-a-naming-element-carries-information-about-the-entity-referenced]]"
  - "[[30_assertions/p5-rolename-excludes-the-role-a-person-has-in-a-context]]"
  - "[[30_assertions/p5-rs-and-name-cannot-mark-the-components-of-a-name]]"
  - "[[30_assertions/p5-name-component-markup-does-not-cover-every-name]]"
  - "[[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]]"
  - "[[30_assertions/p5-guidelines-distinguish-resolving-a-name-from-treating-it-as-an-object]]"
  - "[[30_assertions/p5-nym-contains-the-definition-of-a-canonical-name-or-name-component]]"
  - "[[30_assertions/p5-person-holds-variant-name-forms-without-prioritization]]"
  - "[[30_assertions/p5-person-description-elements-are-datable]]"
  - "[[30_assertions/p5-att-naming-describes-nymref-through-the-object-named]]"
  - "[[30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named]]"
  - "[[30_assertions/p5-person-provides-information-about-an-identifiable-individual]]"
  - "[[30_assertions/p5-guidelines-separate-the-entity-record-from-references-to-the-entity]]"
  - "[[30_assertions/p5-prosopography-records-refer-to-external-authorities-through-idno]]"
  - "[[30_assertions/p5-guidelines-let-an-encoder-regard-a-city-and-its-predecessor-as-one-place]]"
  - "[[30_assertions/p5-entity-information-comprises-statements-about-traits-states-and-events]]"
  - "[[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]]"
  - "[[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]]"
  - "[[30_assertions/p5-guidelines-present-three-encodings-of-a-nationality-as-the-same-information]]"
  - "[[30_assertions/p5-relation-describes-a-relationship-amongst-places-events-persons-or-objects]]"
  - "[[30_assertions/p5-guidelines-admit-persons-places-and-organizations-as-relationship-participants]]"
  - "[[30_assertions/p5-att-canonical-associates-a-name-with-canonical-information-about-its-object]]"
  - "[[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]]"
  - "[[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]]"
  - "[[30_assertions/p5-key-requires-resolution-documentation-for-interchange]]"
  - "[[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]]"
  - "[[30_assertions/p5-ref-points-directly-to-xml-elements-or-other-resources]]"
  - "[[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]]"
  - "[[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]]"
  - "[[30_assertions/p5-simultaneous-key-and-ref-are-not-recommended-without-documentation]]"
posits: 13
topics: ["[[Metadata and Entities]]"]
created: 2026-09-06
updated: 2026-09-06
---

# Metadata and Entities: mention, name, record, statement and identification in TEI P5 4.12.0

The entity extension of the abstract model has to keep five things apart, the
mention of an entity in a text, the name as a linguistic object, the record
about the entity, the statements made about it and the identification of the
entity meant. This chapter asks how TEI P5 4.12.0 treats the five and where it
gives two of them one construct. Its evidence consists of nine admitted P5
sources of one release, two attribute class specifications, six element
specifications and the Guidelines chapter on names, dates, people and places.
No encoded material and no official P6 record enter the argument.[^boundary]

## 1. The mention in the text

`rs` contains a general purpose name or referring string,[^rs] and the English
description of `persName` states that the element contains a proper noun or
proper-noun phrase referring to a person.[^persname] The Guidelines describe
the core elements as marking a text segment as a proper noun or a referring
string and as stating the kind of object named only through a value of
`type`.[^type] They hold `persName` synonymous with `name` of type person
apart from its own `type` attribute and treat four encodings of one name,
with `rs`, with `name` inside `rs`, with `name` and with `persName`, as
equivalent once each carries the same `ref` value.[^synonym] They state that
`placeName` may be regarded as an abbreviation for `name` or `rs` of type
place and add in a footnote that strictly a value such as figurative should be
given to the periphrastic place names in the `placeName` version of their
example to preserve the distinction that the choice of `rs` had indicated.[^placename] The `role` attribute of
`att.naming` may specify further information about the entity referenced,
such as the occupation of a person.[^role] The Guidelines reserve `roleName`
for roles that function as part of a name, place a person's roles and
occupations within `person`, and admit that the line between an associated
title and the rest of a name is not always clear.[^rolename]

The mention therefore carries the kind of its referent as a `type` value and
can carry properties of the referent as `role` values, and in the Guidelines'
own example the specialized element drops the difference between a proper
noun and a referring string unless a `type` value restores it. Under the
equivalence of the four encodings, shared identification is what makes two
mentions the same.[^mention]

## 2. The name as a linguistic object

`rs` and `name` are insufficiently powerful to mark the internal components
or structure of names, and `persName`, `surname`, `forename`, `roleName`,
`addName`, `nameLink` and `genName` are provided for distinguishing a family
name, a forename and an honorary title, which matters for nominal record
linkage and for a sorted list of personal names.[^components] The Guidelines
admit that their mechanisms for marking personal name components will not
cater for every personal name or every processing need and recommend feature
structures where the structure is highly complex or the components
particularly ambiguous.[^coverage] They state that the module of the chapter
provides elements to represent the person, place or organization a name
refers to and the name itself independently of its application, so that it
can represent a personal name, the person being named and the canonical name
being used.[^module] The chapter summarizes the resolution of a name or
referring string as a matter of the object it refers to, effected through
`key` or `ref`, and then treats names as objects in their own right
irrespective of the objects they are attached to, using the term nym for the
canonical or normalized form of a name so regarded and providing `listNym`
and `nym`.[^nymdist] `nym` contains the definition for a canonical name or
name component of any kind.[^nym] Inside `person`, any number of variant name
forms may be given with their language and kind and with no prioritization
among them, in contrast with the library practice of taking an authority-file
form as the base form.[^variants] The specific and generic elements under
discussion at that point of the chapter are members of `att.datable`, and the
example dates two name forms of a person who changed name in a given
year.[^datable]

The first open disagreement concerns where the canonical form is reached
from. By its description in `att.naming`, `nymRef` provides a means of
locating the canonical form of the names associated with the object named by
the element bearing it.[^nymrefclass] The Guidelines chapter lets any member
of `att.naming` use `nymRef` to indicate the nym with which it corresponds,
illustrates this with a forename holding a familiar short form whose `nymRef`
points to the nym of the full name, and notes that this association has
nothing to do with any individual who might use the name.[^nymrefchapter]
Its account of the class relation describes `nymRef` as associating the name
itself with a base or canonical form.[^inherit] The class specification
reaches the canonical form through the object named, the chapter detaches
the association from any individual who might use the name and says nothing
there about places or organizations, and none of the admitted sources
resolves the pair.[^name] Because the account of the class relation speaks of
the name itself for any sort of name, this chapter reads the detachment as
holding for place and organization names as well.[^individuals]

## 3. The entity record

`person` provides information about an identifiable individual.[^person] The
Guidelines describe `org`, in a way they call analogous to `place` and
`person`, as a unique wrapper for information about an entity distinct from
the references to that entity, which a naming element such as `orgName`
typically encodes, so that the content of a naming element represents the way
an organization is named in a given context while the content of `org`
represents what the encoder knows about it, gathered in a single place and
independent of its textual realization.[^record] They state that a
prosopography record of a named entity commonly refers explicitly to other
resources such as name authority files, a gazetteer or a printed book, and
follow that statement with a specList naming `idno` with its `type`
attribute.[^idno] The modern city of Lyon and the Roman Lugdunum, which
overlap significantly without being physically co-extensive, are their
example of what an encoder may wish to regard as the same place while
supplying both names with the period during which each was current.[^lyon]

The separation of record and reference is stated for organizations and
called analogous to `place` and `person`, and this chapter reads it as
holding for the three records.[^separation] That `idno` is the element for
the references a record makes is read here from the specList that follows
the described practice, since the prose states no purpose for
it.[^idnoread] The record so read holds the entity together with its name
forms and the statements about it. Its identity in the Lyon case follows the
encoder's wish without a stated criterion, the dating of that decision sits
on the names, and the record's link to the outside runs through `idno` while
the mention's link runs through `key` and `ref`.[^entity]

## 4. Statements about the entity

The Guidelines describe information about people, places, organizations and
events as statements about traits, states, events and external
resources.[^statements] Because any statement about the changes of state in
a person's life, such as birth, marriage or appointment to office, rests on
some source, possibly several and possibly contradictory, each such statement
needs to be documentable, put into a time frame and relatable to other
statements.[^documentable] The generic elements are members of
`att.global.responsibility` and `att.editLike`, which make available `cert`,
`resp`, `evidence` and `source`, so that conflicting sources can yield more
than one view of what happened, as with two birth events by different
agents.[^responsibility] The specific and generic elements under discussion
can be limited in time through `att.datable`.[^datable] A generic state of
type nationality, a `nationality` element with the same text and an empty
`nationality` element carrying a `key` and the dating attribute are presented
as encodings of the same information.[^nationality]

The second open disagreement concerns the participants of a relationship.
The description of `relation` has the relationship hold amongst a specified
group of places, events, persons, objects or other items.[^relationelement]
The Guidelines chapter uses `listRelation` and `relation` to document
relationships amongst the persons, places or organizations identified and
defines a relationship as a describable link between specified participants,
where a participant might be a person, a place or an
organization.[^relationchapter]

For a statement about a change of state in a person's life, P5 thus states
what a claim record needs, a responsible agency, a certainty, a source, a
time frame and the coexistence of conflicting views, and this chapter
extends the requirement to every statement about an entity.[^extension] The
sources state neither how a statement is withdrawn nor how two conflicting
views relate beyond standing side by side, and in the third nationality
encoding a `key` value stands in for the textual content of the statement,
so the identification mechanism of the mention reappears inside a
statement.[^claims]

## 5. Identification

`att.canonical` provides attributes that associate a representation such as a
name or title with canonical information about the object being named or
referenced.[^canonical] Its `key` attribute provides an externally defined
means of identifying the entity or entities being named, using a coded value
of some kind.[^key] The Guidelines provide `key` for the cases where no direct
link is required, because a local convention resolves the reference or
because the encoder judges that no resolution is necessary.[^keycases] The
remarks on the class state that the use of `key` in interchange requires that
documentation about how it is to be resolved be sent to the
recipient.[^keydoc] The `ref` attribute of the class provides an explicit
means of locating a full definition or identity for the entity being named by
one or more URIs,[^ref] and the English remarks require its value to point
directly to one or more XML elements or other resources by
whitespace-separated URIs.[^refvalue] `att.naming` inherits both attributes
as two ways of associating any sort of name with its referent, and `ref` is
to be used wherever a direct link can be supplied, which requires that a
`person` element with that identifier exist somewhere, possibly in another
document, with more than one URI where the name refers to more than one
person.[^inherit] When both attributes are supplied on one element, the
remarks on `att.canonical` state that the Guidelines provide no semantic
basis and no suggested precedence,[^noprecedence] and the English remarks do
not recommend the simultaneous use unless documentation explaining it is
provided for interchange, probably in an ODD customization.[^simultaneous]

These rules are stated for `att.canonical` and its remarks, and this chapter
reads the inheritance of `key` and `ref` into `att.naming` as carrying the
documentation obligation, the missing precedence and the recommendation to
every naming element.[^inheritance] Identification is thus a property of the
name in the text, and what the sources attach to it is a coded value or a
URI, a documentation obligation and the absence of a precedence rule. None of
the admitted sources names an agent, a date or a certainty for the act of
identifying, whereas an agency and a certainty are stated for the generic
description elements and a time limit for the elements under discussion
there, and the construct that resolves a name to a `person` element in
another document is the construct that points to a resource outside any TEI
document.[^denotation]

## 6. From the findings to the record kinds

P5 4.12.0 gives the mention and the kind of its referent one construct,
gives the mention and its identification one construct without an agent or a
date, and reaches the canonical form of a name through the entity in one
text and through the name in another. The
[record kinds of the entity extension](../knowledge/text-model.md#record-kinds-of-the-entity-extension),
entity, name, mention, denotation claim and alignment claim, separate what
these constructs join, and the findings above state what each kind has to
preserve.[^questions]

An entity record with an identity, a display label and nothing about the
world keeps of `person`, `place` and `org` only the identity that the Lyon
example leaves to the encoder, while the statements, name forms and `idno`
values the record gathers become claims carried by it.[^entity] A name claim,
that an entity bears a form with a language and a validity scope, takes over
the typed, language-tagged, dated and unprioritized forms inside `person`,
whereas a nym and the correspondence between a short form and a full form
are claims about a name and have no kind among the five.[^name]

A mention, as a reading node or an annotation, keeps the difference between
a proper noun and a referring string as a concept, while the kind of the
referent and the properties that `type` and `role` place on it belong to the
entity and to claims about it once a denotation exists.[^mention] A
denotation claim gives the `key` and `ref` pair an agent, an instant, a
status and a certainty, turns a `ref` with several URIs into several claims
and replaces the missing precedence rule with coexisting claims, whereas a
`ref` to a `person` element in another document is neither a denotation
within one package nor an alignment to an external vocabulary.[^denotation]
An alignment claim carried by the entity record takes over `idno` on the
record and `ref` to a resource outside any TEI document, so a mention that
P5 identifies directly by an external URI needs a local entity minted between
the mention and the alignment.[^alignment]

These posits answer three open evidence questions of the
[P6 design chapter](12-p6-design.md) in part. The additional object its
[second section](12-p6-design.md#2-text-projections-and-occurrence-identity)
asks for is the entity record, the retained responsibility marker of its
[third section](12-p6-design.md#3-structure-as-an-attributed-reading)
becomes the agent of a denotation claim, and the withdrawal and cross-agent
disagreement of its
[fifth section](12-p6-design.md#5-version-identity-and-revision-of-claims)
are what P5 states for description elements only as coexistence and leaves
unstated for the identification of a mention. The entity extension has to be
tested against the constructs named here before any of them is called a
defect of P5.[^questions]

[^rs]: Grounded in [[30_assertions/p5-rs-contains-a-general-purpose-name-or-referring-string]].
[^persname]: Grounded in [[30_assertions/p5-persname-contains-a-proper-noun-referring-to-a-person]].
[^type]: Grounded in [[30_assertions/p5-core-elements-state-the-kind-of-referent-only-through-type]].
[^synonym]: Grounded in [[30_assertions/p5-persname-is-synonymous-with-name-of-type-person]].
[^placename]: Grounded in [[30_assertions/p5-placename-abbreviates-typed-name-or-rs-at-the-cost-of-their-distinction]].
[^role]: Grounded in [[30_assertions/p5-role-on-a-naming-element-carries-information-about-the-entity-referenced]].
[^rolename]: Grounded in [[30_assertions/p5-rolename-excludes-the-role-a-person-has-in-a-context]].
[^components]: Grounded in [[30_assertions/p5-rs-and-name-cannot-mark-the-components-of-a-name]].
[^coverage]: Grounded in [[30_assertions/p5-name-component-markup-does-not-cover-every-name]].
[^module]: Grounded in [[30_assertions/p5-namesdates-represents-the-referent-and-the-name-independently]].
[^nymdist]: Grounded in [[30_assertions/p5-guidelines-distinguish-resolving-a-name-from-treating-it-as-an-object]].
[^nym]: Grounded in [[30_assertions/p5-nym-contains-the-definition-of-a-canonical-name-or-name-component]].
[^variants]: Grounded in [[30_assertions/p5-person-holds-variant-name-forms-without-prioritization]].
[^datable]: Grounded in [[30_assertions/p5-person-description-elements-are-datable]].
[^nymrefclass]: Grounded in [[30_assertions/p5-att-naming-describes-nymref-through-the-object-named]].
[^nymrefchapter]: Grounded in [[30_assertions/p5-guidelines-detach-the-nymref-association-from-the-entity-named]].
[^person]: Grounded in [[30_assertions/p5-person-provides-information-about-an-identifiable-individual]].
[^record]: Grounded in [[30_assertions/p5-guidelines-separate-the-entity-record-from-references-to-the-entity]].
[^idno]: Grounded in [[30_assertions/p5-prosopography-records-refer-to-external-authorities-through-idno]].
[^lyon]: Grounded in [[30_assertions/p5-guidelines-let-an-encoder-regard-a-city-and-its-predecessor-as-one-place]].
[^statements]: Grounded in [[30_assertions/p5-entity-information-comprises-statements-about-traits-states-and-events]].
[^documentable]: Grounded in [[30_assertions/p5-each-statement-about-a-life-must-be-documentable-and-time-framed]].
[^responsibility]: Grounded in [[30_assertions/p5-generic-description-elements-carry-certainty-and-responsibility]].
[^nationality]: Grounded in [[30_assertions/p5-guidelines-present-three-encodings-of-a-nationality-as-the-same-information]].
[^relationelement]: Grounded in [[30_assertions/p5-relation-describes-a-relationship-amongst-places-events-persons-or-objects]].
[^relationchapter]: Grounded in [[30_assertions/p5-guidelines-admit-persons-places-and-organizations-as-relationship-participants]].
[^canonical]: Grounded in [[30_assertions/p5-att-canonical-associates-a-name-with-canonical-information-about-its-object]].
[^key]: Grounded in [[30_assertions/p5-key-identifies-the-entity-named-through-an-externally-defined-coded-value]].
[^keycases]: Grounded in [[30_assertions/p5-key-serves-cases-where-no-direct-link-is-required]].
[^keydoc]: Grounded in [[30_assertions/p5-key-requires-resolution-documentation-for-interchange]].
[^ref]: Grounded in [[30_assertions/p5-ref-locates-a-definition-or-identity-for-the-entity-named-by-uris]].
[^refvalue]: Grounded in [[30_assertions/p5-ref-points-directly-to-xml-elements-or-other-resources]].
[^inherit]: Grounded in [[30_assertions/p5-att-naming-inherits-key-and-ref-and-prefers-a-direct-link]].
[^noprecedence]: Grounded in [[30_assertions/p5-att-canonical-gives-no-precedence-when-key-and-ref-co-occur]].
[^simultaneous]: Grounded in [[30_assertions/p5-simultaneous-key-and-ref-are-not-recommended-without-documentation]].
[^boundary]: Posit: the five-way division is the analytic frame of the entity extension and no admitted source states it, so the chapter reads two class specifications, six element specifications and one Guidelines chapter of one release against a frame they did not choose. Open evidence question: which class specifications the naming elements depend on, above all `att.global.responsibility`, `att.datable` and the member lists of `att.naming`, and which encoded material must be admitted before a finding here can become a design requirement?
[^mention]: Posit: a mention kind that is a reading node or an annotation keeps the difference between a proper noun and a referring string as a concept, which the Guidelines' place-name example shows the specialized element losing, while the kind of the referent and the `role` properties belong to the entity and to claims about it once a denotation exists. Open evidence question: which encoding workflows need the kind of referent or a role on a mention that denotes no identified entity, so that the mention would have to carry them itself?
[^name]: Posit: a name claim with form, language and validity scope covers the forms inside `person`, whereas a nym and the correspondence between a short form and a full form are claims about a name with no kind among the five, and the disagreement over `nymRef`, stated by the class for the object named and by the chapter for individuals, is that gap in P5's own terms. Open evidence question: which editions with an onomastic practice relate name forms to one another independently of any bearer, so that a name-as-object kind would be missing from the extension?
[^individuals]: Posit: the Guidelines detach the `nymRef` association from individuals only, and this chapter extends the detachment to place and organization names because the same chapter's account of the class relation speaks of associating the name itself with a base or canonical form for any sort of name. Open evidence question: which passage of the Guidelines or of the class specification states the `nymRef` association for place and organization names, and does encoded onomastic material use it on them?
[^separation]: Posit: the Guidelines state the separation of record and reference for organizations and call it analogous to `place` and `person`, and this chapter reads the separation as holding for the person and place records too, because the definition of `person` and the Lyon example are consistent with it without stating it. Open evidence question: which passages of the chapter on person and place records, once distilled and reviewed, state the separation for those records themselves, and which encoded prosopographies keep or blur it?
[^idnoread]: Posit: the specList naming `idno` that follows the described practice is read as assigning the element to the references a record makes to external resources, which the prose does not state. Open evidence question: which passage of the Guidelines or which part of the specification of `idno` states that purpose, and how do encoded records carry such references?
[^entity]: Posit: an identity record keeps of the P5 record only its identity, while the statements, name forms and `idno` links it gathers become claims about it, and the Lyon example shows an identity that follows the encoder's wish without a stated criterion and is dated through the names, which needs a name claim with validity because a bare identity record has no field for it. Open evidence question: which independently selected editions record why two things count as one entity, and whether that reason is a claim kind of its own or content of the name and alignment claims?
[^extension]: Posit: the Guidelines require documentation, a time frame and relatability for statements about changes of state in a person's life, and this chapter extends the requirement to every statement about an entity, because the generic elements that carry certainty and responsibility serve traits and states as well as events. Open evidence question: which passages state the requirement for traits, for states, for places and for organizations, and which encoded records date and source such statements?
[^claims]: Posit: documentation, time frame and relatability together with `cert`, `resp`, `evidence` and `source` correspond to the agent, certainty and validity fields of the claim pattern and to the coexistence of claims by different agents, while evidence and source have no pattern field, withdrawal is unstated in the sources, and the participant set of a relation record stays open between the element description and the Guidelines chapter. Open evidence question: which recorded disagreements from real prosopographies show whether a source pointer and an evidence kind belong on the claim, and which participant kinds their relations take?
[^inheritance]: Posit: the identification rules are stated for `att.canonical` and its English remarks, and this chapter reads the inheritance of `key` and `ref` into `att.naming` as carrying the documentation obligation, the absence of precedence and the recommendation against simultaneous use to every naming element, which the sources state for the class alone. Open evidence question: which class specification of `att.naming` and which member declarations at the pinned release state that the remarks travel with the attributes, and which elements are members of the two classes?
[^denotation]: Posit: a denotation claim with agent, instant, status and certainty gives the `key` and `ref` pair what the sources leave unstated, turns several URIs into several claims and replaces the missing precedence rule with coexisting claims, whereas a `ref` to a `person` element in another document is neither a denotation within one package nor an alignment to an external vocabulary, and the identifier policy does not yet cover it. Open evidence question: how editions distribute records and texts across files, and whether the retained responsibility marker of the P6 design chapter's third section is the agent of such a claim or a value the claim reports?
[^alignment]: Posit: `idno` on the record, read as the element for its external references, and `ref` to a resource outside any TEI document both become alignment claims carried by the entity record, so a mention identified directly by an external URI needs a minted local entity, and the documentation obligation of `key` becomes the agent of the claim and the base of the package. Open evidence question: which editions identify mentions by external URIs without a local record, and whether they accept a minted local entity or need a denotation claim that targets an IRI?
[^questions]: Posit: the findings answer the P6 design chapter's questions about additional objects, the responsibility marker and the revision of claims in part, because the entity record is the additional object, the marker is the agent of a denotation claim, and P5 states revision as coexistence for description elements and leaves it unstated for identification, so the entity extension is tested against the constructs named here before any of them counts as a defect of P5. Open evidence question: which official P6 records, once admitted, address the naming attributes and the description elements, and which encoded practice shows the folds identified here to be costs?
