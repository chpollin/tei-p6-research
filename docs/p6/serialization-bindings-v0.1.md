# Abstract Text Model 0.1 reference bindings

These independent project bindings encode the
[Abstract Text Model 0.1](abstract-text-model-v0.1.md). They are neither official
TEI P6 syntax nor converters from TEI P5. Their vocabulary and preservation
contract are project posits.

## 1. Model and encoding

An instance is the same package of agents, concepts, texts, versions,
continuity claims, selections, readings, annotations, and relations in all
three bindings. Selecting XML, JSON, or YAML changes its notation. It does not
change object identities, responsibility, selector resolution, or model rules.
The XML binding represents objects explicitly. It does not infer a
primary textual hierarchy or place annotation boundaries inside version text.

The reference API in `tools/models/bindings.py` provides two operations.

```python
encode_model(package, binding) -> str
decode_model(text, binding) -> dict
```

The binding name is exactly `json`, `xml`, or `yaml`. Both operations validate
the package against the core model. Invalid syntax, unknown fields, invalid
references, incorrect hashes, and other structural errors raise `ValueError`.
Ambiguous or absent quote selections remain valid when allowed by the core.
Successful decoding does not mean that every selection resolves. Operations
do not mutate their inputs and perform no external retrieval.

Let `E_b` encode and `D_b` decode binding `b`. For every valid package `p`, the
required preservation laws are the following.

```text
D_b(E_b(p)) = p
canonical_bytes(D_c(E_c(D_b(E_b(p))))) = canonical_bytes(p)
```

The first equality is exact data equality, including array order, optional
field presence, scalar types, and every string code point. Object-key order is
irrelevant. The second expresses the model's R11 equivalence after a binding
change. Registry order need not be significant under R11, but the bindings
preserve it nevertheless. XML root collection order is emitted consistently
with the core collection order. Segments are never merged or reordered.

These laws concern decoded data. An arbitrary input document need not retain
its original indentation, quotation style, namespace prefix, or other lexical
choices after re-encoding. The API accepts Unicode strings. Callers writing
files must use UTF-8 without automatic newline conversion.

## 2. JSON binding

JSON directly represents the existing reference package. Object keys must be
unique strings, and no unknown model fields are accepted. Arrays, strings,
integers, and `null` retain their types. Non-finite numbers, floating-point
values, booleans, and lone Unicode surrogates are outside the model. The
encoder uses readable indentation and JSON escapes where required. It does
not normalize whitespace, line endings, Unicode, or identifiers inside data.

## 3. XML binding

The root is `model` in namespace
`urn:tei-p6-research:abstract-text:0.1`. Its required unqualified attributes are
`binding_version="0.1"` and `model_version="0.1"`. All nine collections must
appear exactly once, including empty collections. No other root attributes or
collections are permitted. Every element belongs to the model namespace.

| Collection | Child record name |
|---|---|
| `agents` | `agent` |
| `concepts` | `concept` |
| `texts` | `text` |
| `versions` | `version` |
| `continuities` | `continuity` |
| `selections` | `selection` |
| `readings` | `reading` |
| `annotations` | `annotation` |
| `relations` | `relation` |

Record and field names match the model. Each record or field has an explicit
`type` of `object`, `array`, `string`, `integer`, or `null`. An object contains
one element per field, with no duplicate field names. Arrays preserve child
order. The `nodes` array uses `node` children, `segments` uses `segment`
children, and other arrays use `item`. A null field has neither text nor
children. An empty array is distinct from null and from an absent field.
Integers use decimal JSON notation without a leading plus sign or leading
zeroes. Strings are element text, not attribute values.

This complete minimal package contains a single version of `abc`.

```xml
<model xmlns="urn:tei-p6-research:abstract-text:0.1"
       binding_version="0.1" model_version="0.1">
  <agents />
  <concepts />
  <texts />
  <versions>
    <version type="object">
      <id type="string">v1</id>
      <content type="string">abc</content>
      <sha256 type="string">ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad</sha256>
      <parents type="array" />
    </version>
  </versions>
  <continuities />
  <selections />
  <readings />
  <annotations />
  <relations />
</model>
```

Readable literal text is used whenever XML 1.0 can preserve it. An individual
string containing a carriage return or an XML-incompatible character instead
uses `encoding="json-string"`. Its element text is one complete JSON string
literal, with XML escaping applied as necessary.

```xml
<content type="string" encoding="json-string">"A\r\nB\u0000"</content>
```

This field decodes to `A`, carriage return, line feed, `B`, and U+0000.
Encoding applies to that string only. Records and relationships remain
explicit XML elements. Literal carriage returns anywhere in an XML input
are rejected to avoid silent XML line-ending normalization. A character
reference such as `&#13;` in an ordinary string is also accepted and preserved.
Strings containing only spaces, tabs, or line feeds retain those characters.

XML declarations are optional. When present they must specify XML 1.0 and,
if an encoding is named, UTF-8. DTD declarations, custom entities, comments,
processing instructions, mixed content between fields, unknown types,
unknown attributes, and foreign-namespace elements are rejected. Predefined
XML escaping and valid character references remain ordinary XML syntax.
The decoder and core validator implement conformance. There is no separate
XSD, Relax NG schema, or Schematron schema.

## 4. YAML binding

YAML represents the same nested mappings and sequences as JSON. The encoder
quotes every string, including keys, and emits no anchors or aliases. Quoting
prevents values such as `null`, `true`, `01`, `yes`, and dates from changing
type under readers with different YAML scalar conventions. Escapes preserve
controls, carriage returns, and other characters requiring special spelling.

The decoder uses a restricted safe-loader contract.

- Mapping keys are unique strings. Merge-key processing is not performed.
- Implicit integers use decimal JSON notation. The null spelling is `null`.
- JSON boolean and non-integer number spellings are recognized and rejected.
  The core model has no corresponding fields.
- Other unquoted scalars are strings. In particular, YAML's legacy boolean,
  timestamp, hexadecimal, and octal conventions are not inferred.
- Explicit tags are limited to mappings, sequences, strings, decimal integers,
  and `null`. Object construction, binary data, timestamps, sets, anchors,
  aliases, and multiple documents are rejected.

YAML quotation and block-scalar choices determine the decoded string. The reference
encoder always emits the quoted form that preserves the existing model value.
The YAML dependency is PyYAML, already used by repository tools.

## 5. Validation and limits

`tests/models/test_bindings.py` runs every valid existing core case, every
valid existing editorial-profile fixture, and both standalone model examples
through all three bindings and across binding changes. Invalid model fixtures
must fail encoding. Additional cases exercise controls, carriage returns,
Unicode combining sequences, supplementary characters, whitespace-only
strings, duplicate keys, malformed structures, unsafe syntax, incorrect
references, and incorrect version hashes.

The bindings preserve profile relation records as ordinary core data. Callers
using the editorial provenance profile must separately invoke its validator
and revision operation.
Neither round-trip equality nor core validation establishes an annotation's
truth, historical derivation, the adequacy of a concept definition, TEI P5
conformance, or successful migration from an external edition.

The decoder imposes a nesting guard beyond the depth of any valid core
package, but no general document-size or resource quota. Applications accepting
large untrusted uploads must set their own resource limits. RDF, JSON-LD,
database layouts, and other bindings remain separate design work. A new
format requires an explicit mapping and the same preservation checks.
