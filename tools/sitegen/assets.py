"""Load checked-in frontend source assets for deterministic inline rendering."""

from pathlib import Path, PurePath


ASSET_ROOT = Path(__file__).with_name("assets")


def read_asset(name: str) -> str:
    """Return one named asset without allowing path traversal."""
    if not name or PurePath(name).name != name:
        raise ValueError(f"unsafe site asset name: {name!r}")
    path = ASSET_ROOT / name
    if not path.is_file():
        raise FileNotFoundError(f"site asset missing: {path}")
    return path.read_text(encoding="utf-8")
