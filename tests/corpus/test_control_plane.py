from pathlib import Path

from tools.corpus.validate_control_plane import validate


def test_repository_source_control_plane_is_consistent() -> None:
    root = Path(__file__).resolve().parents[2]
    assert validate(root) == []
