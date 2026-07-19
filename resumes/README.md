# Resumes

Use the Markdown to PDF workflow for resumes and cover letters.

## Current Files

| Situation | File |
|-----------|------|
| ATS resume source | `Resumes/Rojae_Mighty_ATS_Resume.md` |
| ATS resume PDF | `Resumes/Rojae_Mighty_ATS_Resume.pdf` |
| Full academic CV | `CVs/master/Rojae_Mighty_CV.pdf` |

## Render

Edit the Markdown source, then render the PDF from the repo root:

```bash
make resume-pdf
```

For all current Markdown document PDFs:

```bash
make docs-pdf
```

## Workflow Tip

When shared content changes, edit the master CV first, then pull the relevant bullets into the active one-page resume.
