"""The isolation boundary of a blind review call through the local Claude CLI.

knowledge/verification.md § Vollprüfung requires a runner that works in a
directory without project instructions, with every tool and every external
context service switched off, and that records its invocation conditions. A
fresh `claude -p` alone does not establish that boundary. This module holds the
boundary in one place, apart from the V1 instrument in tools/full_review.py,
because the per-pair path of tools/review.py uses it as well and must not import
the instrument.

The flag contract follows the `claude --help` of the installed CLI:

- `--safe-mode` switches off CLAUDE.md, skills, plugins, hooks, MCP servers,
  custom commands and agents while authentication keeps working. `--bare` is
  not used, because it never reads the OAuth login.
- `--tools ""` removes every built-in tool.
- `--strict-mcp-config` with an explicitly empty `--mcp-config` file loads no
  MCP server from any other configuration.
- `--disable-slash-commands`, `--no-chrome`, `--no-session-persistence` and
  `--permission-mode dontAsk` remove skills, the browser integration, the saved
  session and every permission prompt.

Every call runs in a fresh, empty temporary working directory outside the
repository, and the MCP configuration lives in a second temporary directory so
that the working directory stays empty. The prompt goes in on stdin, because a
Windows command line caps out around 32k characters. The environment is
inherited, since authentication may depend on it, and no value of it is ever
recorded.
"""

from __future__ import annotations

import contextlib
import json
import os
import shutil
import subprocess
import tempfile
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[1]
EMPTY_MCP_CONFIG = {"mcpServers": {}}
ISOLATION_FLAGS = (
    "--safe-mode",
    "--tools",
    "",
    "--strict-mcp-config",
    "--disable-slash-commands",
    "--no-chrome",
    "--no-session-persistence",
    "--permission-mode",
    "dontAsk",
)
# A batch file shim hands its arguments to cmd.exe, which reads these characters
# as syntax; the native executable behind the npm shim takes them verbatim.
CMD_METACHARACTERS = frozenset('&|<>^%!\r\n')
NPM_NATIVE = Path("node_modules/@anthropic-ai/claude-code/bin/claude.exe")


@dataclass
class Workdir:
    """The temporary directories of one call and what was observed about them."""

    cwd: Path
    mcp_config: Path
    empty_before: bool = False
    outside_repository: bool = False
    empty_after: bool | None = None

    def conditions(self) -> dict[str, object]:
        return {
            "cwd": "fresh temporary directory, removed after the call",
            "cwd_empty_before": self.empty_before,
            "cwd_outside_repository": self.outside_repository,
            "cwd_empty_after": self.empty_after,
            "mcp_config": json.dumps(EMPTY_MCP_CONFIG, separators=(",", ":")),
        }


def resolve_claude() -> str:
    """The Claude CLI executable, preferring the native binary behind an npm shim."""
    found = shutil.which("claude")
    if not found:
        raise RuntimeError("claude executable not found on PATH")
    path = Path(found)
    if path.suffix.lower() in {".cmd", ".bat"}:
        native = path.parent / NPM_NATIVE
        if native.is_file():
            return str(native)
    return found


def _inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError:
        return False
    return True


@contextlib.contextmanager
def isolated_workdir(repository: Path = REPOSITORY) -> Iterator[Workdir]:
    """An empty working directory outside the repository, removed afterwards.

    Refuses to yield a directory that is not empty or lies inside the
    repository, so a misconfigured TMP cannot put the project back into reach.
    """
    cwd = Path(tempfile.mkdtemp(prefix="review-cwd-"))
    config_dir = Path(tempfile.mkdtemp(prefix="review-mcp-"))
    workdir = Workdir(cwd=cwd, mcp_config=config_dir / "mcp.json")
    try:
        workdir.mcp_config.write_text(json.dumps(EMPTY_MCP_CONFIG), encoding="utf-8")
        workdir.empty_before = not any(cwd.iterdir())
        workdir.outside_repository = not _inside(cwd, repository) and not _inside(
            repository, cwd
        )
        if not workdir.empty_before or not workdir.outside_repository:
            raise RuntimeError(
                f"review working directory is not empty or not outside the repository: {cwd}"
            )
        yield workdir
    finally:
        with contextlib.suppress(OSError):
            workdir.empty_after = not any(cwd.iterdir())
        shutil.rmtree(cwd, ignore_errors=True)
        shutil.rmtree(config_dir, ignore_errors=True)


def isolated_command(
    executable: str,
    model: str | None,
    mcp_config: Path,
    *,
    json_schema: str | None = None,
) -> list[str]:
    """The argv of one isolated print-mode call; the prompt is never part of it."""
    command = [executable, "-p"]
    if model:
        command += ["--model", model]
    if json_schema is not None:
        command += ["--output-format", "json", "--json-schema", json_schema]
    command += [*ISOLATION_FLAGS, "--mcp-config", str(mcp_config)]
    if Path(executable).suffix.lower() in {".cmd", ".bat"} and any(
        char in CMD_METACHARACTERS for part in command[1:] for char in part
    ):
        raise RuntimeError("an argument would be reinterpreted by the cmd.exe shim")
    return command


def recorded_argv(command: list[str], mcp_config: Path) -> list[str]:
    """The argv as recorded: executable by name, temporary paths by role."""
    recorded = [Path(command[0]).name, *command[1:]]
    return ["<empty MCP config file>" if part == str(mcp_config) else part for part in recorded]


def cli_version(executable: str, repository: Path = REPOSITORY, timeout: int = 60) -> str:
    """The version string the installed CLI reports, read in an isolated directory."""
    with isolated_workdir(repository) as workdir:
        result = subprocess.run(
            [executable, "--version"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=workdir.cwd,
            timeout=timeout,
            check=False,
        )
    if result.returncode != 0 or not result.stdout.strip():
        raise RuntimeError(f"claude --version failed: {result.stderr.strip()[:200]}")
    return result.stdout.strip()


def call_claude(
    executable: str,
    model: str,
    json_schema: str,
    prompt: str,
    *,
    timeout: int,
    repository: Path = REPOSITORY,
) -> dict[str, object]:
    """One isolated structured-output call; returns the raw outcome and its conditions."""
    with isolated_workdir(repository) as workdir:
        command = isolated_command(
            executable, model, workdir.mcp_config, json_schema=json_schema
        )
        outcome: dict[str, object] = {
            "argv": recorded_argv(command, workdir.mcp_config),
            "stdin": "package prompt",
            "timeout_seconds": timeout,
            "environment": "inherited from the caller; no value recorded",
        }
        try:
            result = subprocess.run(
                command,
                input=prompt,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                cwd=workdir.cwd,
                timeout=timeout,
                check=False,
                env=os.environ.copy(),
            )
        except subprocess.TimeoutExpired:
            outcome.update(returncode=None, stdout="", stderr="", timed_out=True)
        else:
            outcome.update(
                returncode=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr,
                timed_out=False,
            )
    outcome["workdir"] = workdir.conditions()
    return outcome
