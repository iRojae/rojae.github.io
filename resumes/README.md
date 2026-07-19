# Resumes

Use the Markdown to PDF workflow for resumes and cover letters.

## Current Files

| Situation | File |
|-----------|------|
| General ATS resume source | `Resumes/Rojae_Mighty_ATS_Resume.md` |
| General ATS resume PDF | `Resumes/Rojae_Mighty_ATS_Resume.pdf` |
| Quant resume source | `Resumes/Rojae_Mighty_Quant_Resume.md` |
| Quant resume PDF | `Resumes/Rojae_Mighty_Quant_Resume.pdf` |
| Grad-school resume source | `Resumes/Rojae_Mighty_Grad_School_Resume.md` |
| Grad-school resume PDF | `Resumes/Rojae_Mighty_Grad_School_Resume.pdf` |
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

When shared content changes, edit the master CV first, then pull the relevant bullets into the quant and grad-school one-page resumes.
