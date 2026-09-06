"""Admit the three locked P5 pilot sources through the shared admission tool.

Run with ``python -m tools.ingest_text_identity``; ``--check`` is read-only and
also works without ignored originals, using the complete embedded XML. The
admission logic lives in ``tools.ingest_git_blobs``; this module carries the
pilot's admission list, which the representations it already wrote hold fixed.
"""

from __future__ import annotations

from tools.ingest_git_blobs import XML_LANG, Admission, Run, cli
from tools.ingest_git_blobs import embedded_source as _embedded_source

__all__ = ["PILOT", "XML_LANG", "embedded_source", "main"]

PILOT = Run(
    run_id="2026-09-05-text-identity-pilot-admission",
    date="2026-09-05",
    adapter="tools.ingest_text_identity",
    version=1,
    manifest="sources/manifests/2026-09-05-text-identity-pilot-admission.yaml",
    boundary=(
        "Exactly anchor.xml, span.xml, and annotation.xml from P5/Source/Specs "
        "at the locked release commit"
    ),
    status_applies_to=(
        "three selected complete Git blobs and their immutable representations "
        "only; not the source family"
    ),
    known_limits=(
        "No claim of complete P5 source-family acquisition; the published-HTML "
        "reconciliation remains separate.",
        "Selected sources do not establish general text-version identity or "
        "automatic cross-version anchoring.",
    ),
    admissions=(
        Admission(
            git_path="P5/Source/Specs/anchor.xml",
            blob="14fe6e40ab7f3684075d4861d88cdc164f3b143b",
            size=5444,
            slug="tei-p5-anchor-4.12.0",
            heading="anchor",
            title="TEI P5 4.12.0 anchor specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/span.xml",
            blob="7eef78bf21e96322e669fb86d7c0282e25a5d79b",
            size=6800,
            slug="tei-p5-span-4.12.0",
            heading="span",
            title="TEI P5 4.12.0 span specification",
            form="spec",
        ),
        Admission(
            git_path="P5/Source/Specs/annotation.xml",
            blob="9c98ca8590036df7de925753c7d65fb028c41d1b",
            size=6577,
            slug="tei-p5-annotation-4.12.0",
            heading="annotation",
            title="TEI P5 4.12.0 annotation specification",
            form="spec",
        ),
    ),
)


def embedded_source(name: str, rendered: bytes) -> bytes:
    """The complete XML of one pilot representation, addressed by its short name."""
    slug = f"tei-p5-{name}-4.12.0"
    for admission in PILOT.admissions:
        if admission.slug == slug:
            return _embedded_source(admission, rendered)
    raise KeyError(f"no pilot admission for {name}")


def main() -> int:
    return cli(PILOT, __doc__)


if __name__ == "__main__":
    raise SystemExit(main())
