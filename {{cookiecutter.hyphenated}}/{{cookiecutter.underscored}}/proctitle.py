from __future__ import annotations

import os
import sys
from pathlib import Path

try:
    from setproctitle import setproctitle
except Exception:
    setproctitle = None


def _base_name() -> str:
    return (
        os.environ.get("PROC_TITLE_BASE")
        or os.environ.get("DJANGO_SETTINGS_MODULE", "django").split(".")[0]
    )


def compute_title(mode: str, extra: str | None = None) -> str:
    base = _base_name()
    if extra:
        return f"{base} [{mode}] {extra}"
    return f"{base} [{mode}]"


def apply_title(title: str) -> None:
    if setproctitle is None:
        return
    setproctitle(title)


def title_for_manage_py(argv: list[str] | None = None) -> str:
    argv = argv or sys.argv
    cmd = argv[1] if len(argv) > 1 else "help"
    detail = cmd
    if cmd in {"runserver", "shell", "dbshell"}:
        detail = " ".join(argv[1:])
    return compute_title("manage", detail)


def title_for_wsgi(server_hint: str | None = None) -> str:
    hint = server_hint
    if not hint:
        exe = Path(sys.argv[0]).name.lower()
        if "gunicorn" in exe:
            hint = "gunicorn"
        elif "uwsgi" in exe:
            hint = "uwsgi"
    return compute_title("wsgi", hint)


def title_for_asgi(server_hint: str | None = None) -> str:
    hint = server_hint
    if not hint:
        exe = Path(sys.argv[0]).name.lower()
        if "granian" in exe:
            hint = "granian"
        elif "uvicorn" in exe:
            hint = "uvicorn"
        elif "daphne" in exe:
            hint = "daphne"
    return compute_title("asgi", hint)
