#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESUME_MD="$ROOT/Resumes/Rojae_Mighty_ATS_Resume.md"
PYTHON="$ROOT/.venv/bin/python"

if ! command -v fswatch >/dev/null 2>&1; then
  echo "fswatch is not installed. Install it with: brew install fswatch" >&2
  exit 1
fi

if [ ! -x "$PYTHON" ]; then
  echo "Missing Python environment at .venv. Create it and install dependencies first." >&2
  exit 1
fi

"$PYTHON" "$ROOT/scripts/render_resume_pdf.py"
echo "Watching $RESUME_MD"

fswatch -o "$RESUME_MD" | while read -r _; do
  "$PYTHON" "$ROOT/scripts/render_resume_pdf.py"
done
