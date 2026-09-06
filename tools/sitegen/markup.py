"""Escape values and build the links shared by every generated page.

One escaping function, one URL policy, one repository-link form. Page modules
interpolate nothing that has not passed through here.
"""
from __future__ import annotations

import html
import re
from pathlib import PurePosixPath
from urllib.parse import quote, urlsplit


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def safe_url(value: str) -> str:
    """Accept the absolute HTTP(S) URL of an external source, nothing else."""
    if not isinstance(value, str) or value != value.strip() or any(ord(c) < 32 for c in value) or "\\" in value:
        raise ValueError("Unsafe URL")
    parsed = urlsplit(value)
    if parsed.scheme not in ("https", "http") or not parsed.netloc or parsed.username or parsed.password:
        raise ValueError("Source URLs must be absolute HTTP(S) URLs")
    return value


def link_href(value: str) -> str:
    """Accept a relative target inside the published site, or a source URL."""
    if not isinstance(value, str) or value != value.strip() or any(ord(c) < 32 for c in value) or "\\" in value:
        raise ValueError("Unsafe URL")
    if urlsplit(value).scheme or value.startswith("//"):
        return safe_url(value)
    return value


def deployment_base(value: str | None) -> str | None:
    """Normalize the HTTPS base that a deployed page resolves file links against."""
    if not value:
        return None
    safe_url(value)
    parsed = urlsplit(value)
    if parsed.scheme != "https" or parsed.query or parsed.fragment:
        raise ValueError("repository_base must be an HTTPS repository path")
    return value.rstrip("/") + "/"


def repository_link(path: str, base: str | None) -> str:
    """Link a public repository file, locally relative or under a deployment base."""
    target, _, anchor = path.partition("#")
    if target.startswith(("/", "00_sources/")) or ".." in PurePosixPath(target).parts or "\\" in path:
        raise ValueError("Unsafe or non-public repository path")
    href = (base or "../") + quote(target, safe="/")
    # GitHub renders Obsidian block markers as text, not addressable IDs.
    # Link to the actual file and preserve the precise anchor in the label.
    if anchor and not anchor.startswith("^"):
        href += "#" + quote(anchor, safe="-")
    return href


def doc_id(path: str) -> str:
    """Public artifact anchor, shared by the knowledge page and its citations."""
    return "doc-" + re.sub(r"[^a-z0-9]+", "-", path.removesuffix(".md").lower()).strip("-")
