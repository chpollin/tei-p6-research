---
title: Verification
project:
  name: "TEI P6 Research"
  repository: "tei-p6-research"
method:
  name: Promptotyping
  url: https://dhcraft.org/Promptotyping/
status: draft
language: en
created: "2026-09-06"
updated: "2026-09-11"
related: [INDEX, operations, schema, testing, governance, state, journal]
---

# Verification

This document holds the adversarial checking of the project's own claims.
Validation in [[knowledge/operations]] establishes deterministic
conformance. Everything beyond that, the machine review of source support,
its independence, the human verification, the premise rule for proposals
and the counterevidence search, is defined here. Together with validation,
machine review permits `validated`. Only human verification permits
`verified`.

## What the checks establish

Three checks divide the work, and each answers one question under its own
authority.

| Check | Question | Authority |
|---|---|---|
| Validation | Does the artifact satisfy its formal contract and do its anchors resolve? | records deterministic conformance |
| Machine review | Does the cited passage support the statement? | with validation, permits `validated` |
| Verification | Does this grounding hold as evidence? | the designated human expert may establish `verified` |

Agents prepare the files and the review pairs, and their agreement establishes
no truth. Evidence is relative to a claim rather than an intrinsic property of
a document. Grounding is the structural relation, evidence is the grounding
relation that passed human verification, and a posit is an authorial conclusion
with an explicit rationale and an open evidence question. The intended result
is an inspectable research record whose check outcomes carry their dates, so an
unfinished vault stays useful because the review state of each artifact is
explicit.

## Machine review

Machine review judges source support for each passage and statement pair.
Its fixed verdicts are **fully supports**, **partially supports**,
**overreaches**, **contradicts** and **not in the text**. Only *fully
supports* passes. Together with validation, this permits `validated` status
and no higher.

Anti-anchoring is mandatory. The reviewer sees the source location and the
bare statement, without the producing agent's reasoning, its Support prose or
its anchors. A document pair contains the anchored block and heading path, a
publication pair the quotation, a data pair the computation and its result.
Each is paired only with the statement being judged. `tools/review.py` cuts
these pairs deterministically and builds one prompt per pair from the
skeleton below.

> You are an adversarial reviewer. Below are a source passage and a statement
> that claims to be supported by it. Your task is to refute the statement.
> Judge only whether this passage supports this statement. Answer with exactly
> one verdict: fully supports | partially supports | overreaches | contradicts
> | not in the text. Then give one sentence of justification.
>
> PASSAGE: {source location, with its heading path}
> STATEMENT: {statement}

The reviewer must add a line when the statement displaces the passage's
subject. For a self-report, *fully supports* applies when the statement
attributes the claim to the source, while asserting the claimed achievement
itself is *overreaches*. For a state report, the statement must retain the
state and date shown by the source, while extending that observation into an
unqualified property of the object is *overreaches*. Examples include
restored objects, dated inventories and plans. The assertion review prompt
in [[knowledge/operations]] applies the same verdicts to an assertion and the
distillate statement it claims as support.

Record `checked.machine-review: <date>` on a document only when every one of
its pairs came back *fully supports*. A failed verdict requires rework.
Narrow the assertion or replace the unsupported anchor with one that carries
the claim, then review the changed pair again. Record systematic failure
patterns in [[knowledge/journal]].

## Review protocol and audit records

A review runs in a fresh context. The prompts are emitted unmodified by
`tools/review.py` or by the pilot runner, each prompt carries its SHA-256,
and every verdict is bound to that hash together with reviewer attribution,
the verdict from the fixed vocabulary and one sentence of reasoning. The
audit records of one run live under `workbench/reviews/<run-id>/` as
`pairs.jsonl` and `verdicts.jsonl` with a README that names the scope. They
are records and never sources or grounding targets.

A changed passage, a changed claim or a reused verdict invalidates the
review. `check_review_records` in `tools/review.py` holds the stored pairs
against the pairs the vault cuts today and the verdicts against both. An
acceptance runner rejects changed prompts, incomplete coverage, duplicate or
unknown verdicts, missing reasoning and any verdict other than *fully
supports*. Earlier rounds, including non-passing ones, stay in the run
directory as `*-round1.jsonl` so that a correction remains inspectable.
Completing the prompt context with mechanically recovered source identity,
locator or XML ancestor labels is legitimate, because it changes neither the
immutable representation nor the claim. A changed claim needs new prompts
and a fresh review, and old verdicts do not apply to it.

A change of the review instrument itself invalidates recorded source reviews
in the same way as a changed passage. When the pair cutter began to show the
source title, the heading path and the locator line with each block, and when
a representation form gained identified locators, every stored source pair
changed its prompt, so the affected runs were re-judged in fresh contexts and
the superseded records stayed in the run directory as `*-cutter1.jsonl`.
Assertion pairs are unaffected by such a change, because their prompts hold
only the distillate statement and the assertion. A runner that enriches its
prompts beyond the cutter, as the pilot runner does, must be judged from its
stored pairs rather than from freshly cut ones, since a verdict binds to the
prompt the reviewer saw.
`python tools/check_wave1_sources.py . --review-only` and
`python tools/check_text_identity_pilot.py` check the current scope, the
unmodified canonical prompts and the passing verdict hashes of the recorded
runs without local raw data.

## Independence

A review is independent when three conditions hold. The reviewer comes from
a different model family than the producer, it works in a fresh context, and
it has no access to the author's rationale. A review that meets the second
and third condition with the same model family is recorded as a limitation
in the run's README and in [[knowledge/state]], because independence of
context does not imply independence of model errors. [[knowledge/governance]]
assigns adversarial reading to Fable, and where the producer was Fable the
reviewer comes from another family. Where only one family is available in a
session, the producer and the reviewer are different models of that family
(the entity run of 2026-09-06 paired Opus authors with a Fable reviewer and a
Fable author with an Opus reviewer), the pairing is named in the verdict record
itself, and the same-family limitation is recorded as above.

## Vollprüfung

Diese Methode gilt für den eigens beauftragten Meilenstein in [[knowledge/plan]]. Sie erweitert die bisherigen begrenzten Prüfläufe um eine vollständige Bestandsprüfung. Der Integrator friert die Dateien, ihre Prüfsummen, den Stand des Prüfinstruments und die vollständige Dokumentliste ein. Ein uncommitteter Stand wird durch seine Datei- und Prompthashes bezeichnet; ein Commit ist keine Voraussetzung für die Prüfung.

Die Arbeit wird auf getrennte Reviewer verteilt:

| Prüfauftrag | Vollständiger Umfang und Frage |
|---|---|
| Original und Kontext | Für jedes Destillat Identität, Version und Quellenrolle prüfen; XML/Markdown-Treue oder Zitat gegen das Original prüfen. Den umgebenden Abschnitt auf Bedingungen, Gegenbeispiele und Sprecherzuordnung lesen. Fehlende Originale ausdrücklich als nicht erneut geprüfte Zitattreue führen. |
| Destillierte Aussagen | Jede Core statement gegen ihren Beleg und den gesondert bereitgestellten Quellenkontext beurteilen. Tatsachenbehauptungen in Terms und Appraisal zusätzlich erfassen; Fragen und Wertungen als solche ausweisen. |
| Assertions | Jede Grounding-Beziehung beurteilen und den vollständigen Statement-Abschnitt gegen alle angegebenen Belege prüfen. H1, Statement und Support müssen denselben Geltungsbereich haben. Mehrere Anker erhalten zusätzlich ein Urteil über ihren gemeinsamen Schluss. |
| Widerspruch und Verwendung | Beide Positionen jedes `contested`-Paars mit ihren Quellen und Geltungsbereichen vergleichen. Alle quellenbezogenen Kapitelaussagen gegen ihre Assertions prüfen; Posits, Fremdaussagen und eigene Vorschläge auseinanderhalten. |
| Zweitprüfung | Sämtliche Abweichungen und Konflikte von einem anderen Reviewer beurteilen lassen. Eine vorab festgelegte Stichprobe bestandener Urteile kontrolliert systematische Fehler; bei einem systematischen Befund den betroffenen Aussagentyp vollständig erneut prüfen. |

Die Blindprüfung erhält keine Produzentenbegründung, keine bisherigen Urteile und keinen Zugriff auf den übrigen Projektbestand. Ein frischer Modellaufruf allein belegt diese Grenze nicht. `tools/review_execution.py` erzeugt dafür ein leeres temporäres Arbeitsverzeichnis außerhalb des Repositorys und sperrt Projektinstruktionen, Werkzeuge, Plugins, Browser und externe Kontextdienste durch die protokollierten CLI-Flags und eine explizit leere MCP-Konfiguration. `tools/full_review.py` und der historische Einzelpaar-Runner verwenden diese gemeinsame Ausführungsgrenze. Alte Reviews erwerben dadurch keine nachträgliche Isolation.

Das ergänzende Instrument `tools/full_review.py` erzeugt Quellenpaare mit benachbartem Kontext, Assertion-Paare mit vollständigem Statement sowie eigene Gesamttext-, Kapitel- und Konfliktprüfungen. Quellen- und Assertion-Paare werden getrennt von Gesamttextprüfungen gebündelt; dadurch gelangen Support-Begründungen aus einem Konsistenzpaket nicht in einen Belegdurchgang. Bei Dokumentrepräsentationen über 240.000 Zeichen erhält die Gesamttextprüfung den Vorspann und sämtliche zitierten Kontextfenster. Diese Auswahlgrenze steht im Prompt. Für Aussagen, die weitere Passagen benötigen, muss der Reviewer eine Lücke melden. Publikationskontexte werden mit URL, Version, Locator und Texthash explizit zugeliefert; fehlender Kontext und nicht darin enthaltene Zitate sperren den Gesamt-Pass.

Bei einer Assertion mit mehreren Quellen prüft jedes Einzelpaar den Beitrag seines Belegs zum vollständigen Statement. Der gesonderte Gesamtdurchgang prüft, ob alle Belege gemeinsam den Schluss tragen. Das verlangt eine erkennbare Zuschreibung der Teilbefunde; eine Quelle muss nicht zusätzlich die ausdrücklich einer anderen Quelle zugeschriebenen Beobachtungen belegen. Maschinenlesbare Kontextgrenzen benennen ausgewählte Passagen. Ein Pass gilt für die geprüften Behauptungen innerhalb dieses Kontexts und behauptet keine Lektüre des gesamten Quellendokuments.

`emit` schreibt einen unveränderlichen Prüfauftrag; `run --model opus` führt ihn aus. `check` gleicht den aktuellen Inhalt, sämtliche Prompthashes, die Instrumentfassung, Abdeckung und protokollierte Isolation ab. Der Materialhash bindet Text und beweisrelevante Metadaten; die spätere Buchung eines tatsächlich durchgeführten Checks verändert ihn nicht. `sample` zieht nach vollständiger Erstprüfung die vorab definierte Zweitstichprobe. `emit --ids` kennzeichnet einen eingeschränkten Prüfauftrag ausdrücklich. `reuse` übernimmt vollständig passende, isoliert erzeugte Pakete. Nach einer Instrumentänderung verlangt `--equivalent-prompts` identische vollständige Pakete einschließlich Systemanweisung, Einheiten, Materialhashes, JSON-Urteilsformat und Ausführungsgrenze; die Herkunft wird protokolliert. Geänderte Prompts werden nie übernommen. `run --retry-failed` erhält fehlgeschlagene Versuche in eindeutig benannten Verzeichnissen und versucht ausschließlich offene Einheiten erneut. Vollständige Drittquellenkontexte und Prompts bleiben im ignorierten Rohbereich; `seal` exportiert Prüfsummen, Einheiten, Reviewerzuordnung und Urteile ohne Quellenkörper. Keines dieser Kommandos vergibt einen wissenschaftlichen Status.

Die Quellenidentität aus Metadaten, Präambel, Destillattitel und Zitatlocator
begleitet den Beleg, ohne eine zusätzliche Interpretation zu begründen. Der
Originalwortlaut einer Publikationsquote wird der Assertion-Prüfung dabei
nicht als weiterer Beleg geliefert. XML-Leseblöcke erhalten ihre Vorfahren
und Attribute aus dem unveränderten Original. Bei großen Repräsentationen
werden auch die ausdrücklich außerhalb der Core statements zitierten Blöcke
geliefert. Für die neun mit `tools.ingest_practice_v1` aufgenommenen Dokumente
erhält auch die Einzelclaim-Prüfung die vollständige Repräsentation:
Gesamtzahlen und Elementzuordnungen brauchen den Zusammenhang über einzelne
Byteintervalle hinaus. P6-Kontexte umfassen den extrahierten Seitentext.

`python -m tools.current_review .` ist der zusätzliche aktuelle Gesamtcheck.
Er verlangt einen Erstlauf über sämtliche Wissensdokumente und exakt die
prospektiv bestimmte Zweitstichprobe. Zweiturteile müssen dieselben Prompts
prüfen, separat erzeugte Antworten haben und ohne Wiederverwendung entstanden
sein. Beide Siegel müssen vollständig bestehen. Die öffentlichen Siegel
erlauben einen Abgleich von Material, Instrument, Abdeckung und Urteilsbindung;
die Originalantworten und privaten Kontexte prüft der lokale `check`-Lauf.

Der bestehende Cutter liefert Quellenpaare aus Core statements und Assertion-Paare aus deren H1. Er erfasst weder den gesamten Statement-Abschnitt noch jede Tatsachenbehauptung in den übrigen Abschnitten oder den Kapiteln. Die Vollprüfung braucht deshalb ergänzende, gespeicherte Kontext- und Gesamttextpaare. Diese erhalten eine eigene Instrumentfassung und Prompthashes; die bisherigen Prompts bleiben erhalten. Alle Reviewer sehen den Wortlaut der zu prüfenden Aussage, während die Bewertungsbegründung des Produzenten ausschließlich Gegenstand des gesonderten Konsistenzdurchgangs ist.

Für jedes Urteil werden ID, Prompthash, Reviewer, konkretes Modell, Prüftag, festes Verdict und Begründung erfasst. Auftragsbrief, Antwort und Prüfumgebung bleiben zuordenbar. Die Abdeckung wird für jede Prüfebene separat gezählt; hundert Prozent beim bisherigen Cutter decken dessen ausgelassene Abschnitte nicht ab. Historische Sonderprompts des Piloten werden durch dessen eigenen Checker geprüft und gelten nicht automatisch für neu erzeugte Prompts.

Die Opus-Vorgabe für Subagents bleibt bestehen. Mehrere Opus-Kontexte teilen Fehlermöglichkeiten ihrer Modellfamilie. Für von derselben Familie produzierte Aussagen wird diese Einschränkung pro Dokument ausgewiesen; familienfremde oder menschliche Gegenprüfung bleibt gesondert zu belegen. Eine unbekannte Produzentenzuordnung begründet keinen Unabhängigkeitsanspruch.

Ein Pass setzt vollständige Abdeckung des eingefrorenen Umfangs, passende Hashes, eindeutige Reviewerzuordnung und abgeschlossene Behandlung aller Abweichungen voraus. Ein offener Quellenzugang, ein ungeklärter Konflikt oder eine nicht gestützte Aussage bleibt sichtbar und trägt keine freigegebene Schlussfolgerung. Nacharbeit verändert niemals die unveränderliche Quellenrepräsentation. Geänderte Destillate und Assertions benötigen neue Paare und neue Urteile; alte Reviews bleiben nachvollziehbar. Die Vollprüfung verleiht kein menschliches `verified` und keine Zusicherung absoluter Wahrheit.

## Human verification

The human verification role named in [[knowledge/specification]], the
project owner or an explicitly designated TEI domain expert, judges whether
grounding holds as evidence. Only this role may establish `verified`. Machine
checks prepare the material without replacing that judgment.

Verification runs as a stratified sample per chapter. The strata are the
assertions the chapter cites, grouped by source type and by topic, and the
quota per stratum is recorded in [[knowledge/journal]] before the sample is
drawn. The role verifies the prepared pairs of the sample passage by passage
and records `checked.verification: <date>` by or on behalf of the verifying
role. A failed pair returns its assertion to rework and voids the sample of
its stratum. Human acceptance of an experiment, recorded through the items in
[[knowledge/experiments]], is a separate decision from the verification of a
grounding relation.

## Premises of a proposal

A premise of the Proposal for TEI P6, and of any design requirement, rests on
`validated` assertions. A `grounded` assertion may be cited while a chapter
is being written, but the chapter cannot reach `validated` and no design
requirement can be derived from the assertion until it has passed machine
review. A recommendation remains a posit even when its premises are
verified.

## Counterevidence search

Before an assertion supports a design requirement, a counterevidence search
runs and is recorded. The search names the topic map, the sources or queries
consulted and the result. A source that contradicts the assertion produces a
second assertion, both marked `contested` and linked reciprocally through
`contested-with`. A search without a finding is recorded with its date under
the open questions of the topic map, so that a later reader can see what was
looked for. A requirement that rests on an assertion without a recorded
counterevidence search enters output as a posit.

## Status discipline

`grounded` → (validation and machine review passed) → `validated` →
(verification passed) → `verified`. Assertion building or review may set
`contested` when sources conflict, and only verification resolves it. An
artifact's status is the minimum of its anchors' states, and no check may
assign a status above its authority.
