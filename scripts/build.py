"""Compile the report. Works on Windows, macOS and Linux with no extra Python packages.

    python3 scripts/build.py            build once, producing main.pdf at the repo root
    python3 scripts/build.py watch      rebuild on every file save, press Ctrl+C to stop
    python3 scripts/build.py clean      remove build/ and main.pdf

Build settings (engine, output directories, biber) live in .latexmkrc; this script only calls latexmk.
Options the script does not recognize are passed through to latexmk, e.g. `python3 scripts/build.py build -g`
to force a full rebuild.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = ROOT / "build"
PDF = ROOT / "main.pdf"
LOG = BUILD_DIR / "main.log"


def check_tools() -> None:
    missing = [tool for tool in ("latexmk", "perl", "biber") if shutil.which(tool) is None]
    if missing:
        sys.exit(
            f"Could not find {', '.join(missing)} in PATH. "
            "See the 'Install compiler' section in README.md."
        )


def create_build_tree() -> None:
    """Mirror the source directory tree inside build/ so \\include can write .aux files."""
    import os
    for dirpath, dirnames, filenames in os.walk(ROOT, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in ("build", ".git", ".zcode", "__pycache__", ".vscode")]
        rel = Path(dirpath).relative_to(ROOT)
        target = BUILD_DIR / rel
        target.mkdir(parents=True, exist_ok=True)


def manual_compile() -> int:
    """Run the correct 4-pass sequence: pdflatex → biber → pdflatex → pdflatex.

    This bypasses latexmk's emulate_aux mode which doesn't always trigger biber properly
    on TinyTeX / TeX Live installations.
    """
    check_tools()
    create_build_tree()

    env = {**__import__("os").environ}

    passes = [
        ("pass 1 (gen .bcf)", ["pdflatex", "-interaction=nonstopmode", "-output-directory=build", "main.tex"]),
        ("biber", ["biber", "build/main.bcf"]),
        ("pass 2", ["pdflatex", "-interaction=nonstopmode", "-output-directory=build", "main.tex"]),
        ("pass 3", ["pdflatex", "-interaction=nonstopmode", "-output-directory=build", "main.tex"]),
    ]

    for label, cmd in passes:
        if label == "biber":
            result = subprocess.run(cmd, cwd=ROOT, capture_output=True, env=env)
            print(f"  {label}: {'OK' if result.returncode == 0 else 'WARN'}")
            if result.returncode != 0:
                stderr = result.stderr.decode("utf-8", errors="replace")[:200]
                print(f"    biber error: {stderr}")
        else:
            # pdflatex output may contain T5-encoded bytes; don't decode with text=True
            result = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=env)
            print(f"  {label}: {'OK' if result.returncode == 0 else 'WARN'}")

    pdf_out = BUILD_DIR / "main.pdf"
    if pdf_out.exists():
        shutil.copy(pdf_out, PDF)
        print(f"\nPDF: {PDF.relative_to(ROOT).as_posix()}")
        _print_errors()
        return 0
    else:
        _print_errors()
        return 1


def _print_errors() -> None:
    """Print error lines from the log file."""
    if not LOG.exists():
        return
    lines = LOG.read_text(encoding="utf-8", errors="replace").splitlines()
    error_line = re.compile(
        r"^(?:[A-Za-z]:)?[^:\s]+:\d+: |^! "
        r"|Warning: (Reference|Citation) .* undefined|multiply defined|Missing character"
    )
    errors = []
    for i, line in enumerate(lines):
        if error_line.search(line):
            errors.append(line)
    if errors:
        print(f"\nWarnings in build/main.log ({len(errors)} lines):", file=sys.stderr)
        for line in errors[:20]:
            print(f"  {line}", file=sys.stderr)


def latexmk(extra: list[str]) -> int:
    check_tools()
    create_build_tree()
    result = subprocess.run(["latexmk", *extra], cwd=ROOT)
    return result.returncode


def build(extra: list[str]) -> int:
    # Use manual 4-pass compile which properly runs biber
    return manual_compile()


def watch(extra: list[str]) -> int:
    # -pvc: watch source files and rebuild on change. -view=none: do not open a PDF viewer.
    create_build_tree()
    try:
        return latexmk(["-pvc", "-view=none", *extra])
    except KeyboardInterrupt:
        return 0


def clean(_: list[str]) -> int:
    shutil.rmtree(BUILD_DIR, ignore_errors=True)
    for f in (PDF, PDF.with_suffix(".synctex.gz")):
        f.unlink(missing_ok=True)
    print("Removed build/ and main.pdf")
    return 0


def main() -> int:
    # Windows consoles fall back to cp1252 when output is piped; force UTF-8 so non-ASCII text in the log prints correctly.
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    commands = {"build": build, "watch": watch, "clean": clean}
    parser = argparse.ArgumentParser(description="Compile the report with latexmk.")
    parser.add_argument("command", nargs="?", default="build", choices=commands)
    args, extra = parser.parse_known_args()
    return commands[args.command](extra)


if __name__ == "__main__":
    sys.exit(main())
