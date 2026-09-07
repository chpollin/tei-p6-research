"""Admit the pinned overlap test for the Text and Document Structures run.

The nine Guidelines sources reuse the complete reference intake. The two
discussion threads enter separately as citation-only sources. Run this module
to materialize the single test source, or use --check without a Git mirror.
"""

from tools.ingest_git_blobs import Admission, Run, cli

RUN = Run(
    run_id="2026-09-07-text-structures-admission",
    date="2026-09-07",
    adapter="tools.ingest_text_structures",
    version=1,
    manifest="sources/manifests/2026-09-07-text-structures-admission.yaml",
    boundary="Exactly P5/Test/testoverlap.xml at the locked P5 4.12.0 release commit",
    status_applies_to="one test document and its immutable representation only",
    known_limits=(
        "The nine selected Guidelines sources reuse the complete reference admission.",
        "GitHub issues 1400 and 1505 enter separately as citation-only publications.",
        "A repository test demonstrates encoded practice, not a normative rule or a passed validation run.",
        "The test is an extract of A Christmas Carol, not an independent editorial corpus.",
    ),
    admissions=(
        Admission(
            git_path="P5/Test/testoverlap.xml",
            blob="740ff7a95c2a0399aab87e1c919f0db7931d9d4c",
            size=3329,
            slug="tei-p5-test-testoverlap-4.12.0",
            heading="testoverlap",
            title="TEI P5 4.12.0 overlap test document",
            form="test-document",
            rights_note=(
                "Per-file review on 2026-09-07: no separate rights notice in this file; "
                "the pinned TEI release licence covers its encoding. The literary extract "
                "is from Charles Dickens, A Christmas Carol (1843). Preserve the original "
                "text and TEI attribution; no modern edition or facsimile is included."
            ),
        ),
    ),
)


if __name__ == "__main__":
    raise SystemExit(cli(RUN, __doc__))
