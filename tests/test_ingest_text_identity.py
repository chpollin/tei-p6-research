"""The pilot admission list against the representations it already wrote.

The pilot is now a list handed to `tools.ingest_git_blobs`, so what has to hold
is that the list still reproduces the three committed representations and their
manifest byte for byte. The converter's own boundaries are checked in
`test_ingest_git_blobs.py`.
"""

from pathlib import Path

import pytest

from tools.ingest_git_blobs import admit, blob_id
from tools.ingest_text_identity import PILOT, embedded_source

ROOT = Path(__file__).resolve().parents[1]


def test_the_pilot_list_reproduces_the_committed_admission() -> None:
    admit(ROOT, PILOT, check=True)


@pytest.mark.parametrize("admission", PILOT.admissions, ids=lambda a: a.slug)
def test_every_pilot_representation_carries_its_admitted_blob(admission) -> None:
    rendered = (ROOT / admission.rendered).read_bytes()
    name = admission.slug.removeprefix("tei-p5-").removesuffix("-4.12.0")
    assert blob_id(embedded_source(name, rendered)) == admission.blob


def test_an_unadmitted_short_name_resolves_to_no_source() -> None:
    with pytest.raises(KeyError, match="no pilot admission"):
        embedded_source("persname", b"")
