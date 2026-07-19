from pathlib import Path
import os

import markdown


ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / ".cache"
CV_TARGETS = [
    (
        ROOT / "CVs" / "master" / "Rojae_Mighty_CV.md",
        ROOT / "CVs" / "master" / "Rojae_Mighty_CV.pdf",
    )
]


CACHE_DIR.mkdir(exist_ok=True)
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE_DIR))

from weasyprint import HTML


def render_pdf(source: Path, output: Path) -> None:
    md_text = source.read_text(encoding="utf-8")
    body = markdown.markdown(md_text, extensions=["extra"])
    html = (
        '<!doctype html><html><head><meta charset="utf-8"></head>'
        f"<body>{body}</body></html>"
    )
    HTML(string=html, base_url=str(ROOT)).write_pdf(output)
    print(f"Updated {output.relative_to(ROOT)}")


def main() -> None:
    for source, output in CV_TARGETS:
        render_pdf(source, output)


if __name__ == "__main__":
    main()
