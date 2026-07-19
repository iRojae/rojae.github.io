from pathlib import Path
import os

import markdown


ROOT = Path(__file__).resolve().parents[1]
RESUME_MD = ROOT / "Resumes" / "Rojae_Mighty_ATS_Resume.md"
RESUME_PDF = ROOT / "Resumes" / "Rojae_Mighty_ATS_Resume.pdf"
CACHE_DIR = ROOT / ".cache"

CACHE_DIR.mkdir(exist_ok=True)
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE_DIR))

from weasyprint import HTML


def main() -> None:
    md_text = RESUME_MD.read_text(encoding="utf-8")
    body = markdown.markdown(md_text, extensions=["extra"])
    html = (
        '<!doctype html><html><head><meta charset="utf-8"></head>'
        f"<body>{body}</body></html>"
    )
    HTML(string=html, base_url=str(ROOT)).write_pdf(RESUME_PDF)
    print(f"Updated {RESUME_PDF.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
