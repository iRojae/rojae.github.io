.PHONY: resume-pdf cv-pdf docs-pdf resume-watch

resume-pdf:
	.venv/bin/python scripts/render_resume_pdf.py

cv-pdf:
	.venv/bin/python scripts/render_cv_pdf.py

docs-pdf: resume-pdf cv-pdf

resume-watch:
	scripts/watch_resume_pdf.sh
