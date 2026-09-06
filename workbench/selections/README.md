# Selection records

A selection record holds the dated tables of one topic run of milestone 6,
produced under the selection procedure in [the plan](../../knowledge/plan.md).
It carries the snapshot of the streams the run queried, with the declared
query of every family and its hit count, and the selection table that gives
every candidate its disposition and the reason for it. A disposition row is
an audit trail. It shows what the run saw on its date and what it did with
each hit, so that a reader can retrace an admission, a deferral or a
rejection without repeating the queries.

The counts hold for the manifests, locks and pinned commit the record names
and for no later state of them. A record is written once, when the run has
made its selection, and stays as it was written when the streams grow or a
deferred candidate is admitted later. A further run of the same topic writes
its own record.

These files are records and navigation aids, never sources or grounding
targets. The evidence questions of a run, the summary of what it admits and
the procedure that produced the record stand in
[the plan](../../knowledge/plan.md). The admission manifest under
`sources/manifests/` is the audit record of ingestion, and the review audit
records of a run live under `workbench/reviews/<run-id>/`.

The folder holds the record of
[run 2 of Metadata and Entities](2026-09-06-metadata-and-entities-run2.md)
and the record of
[run 1 of Text and Document Structures](2026-09-06-text-and-document-structures-run1.md).
