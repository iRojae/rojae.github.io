# Resumes

One folder per application. Create **tailored 1-page resumes** from the template for each role. Use **CVs/** for full academic CVs.

## Layout

```
resumes/
├── google-student-researcher/   # Tailored for Google Student Researcher
│   ├── Rojae_Mighty_Resume.tex
│   └── Rojae_Mighty_Resume.pdf
└── _template/                   # Starting point for new applications
    └── Rojae_Mighty_Resume.tex
```

## Add a new tailored resume

1. Copy `_template/` to a new folder named `company-role` (e.g. `jpmorgan-quant-research`).
2. Edit the `.tex` file — reorder bullets, emphasize relevant skills, trim to one page.
3. Compile and commit both `.tex` and `.pdf`:

   ```bash
   cd resumes/your-new-folder
   pdflatex Rojae_Mighty_Resume.tex
   ```

## Which file to use when

| Situation | File |
|-----------|------|
| Job / internship application (1 page) | `resumes/<company-role>/Rojae_Mighty_Resume.pdf` |
| Grad school, fellowships, full record | `CVs/master/Rojae_Mighty_CV.pdf` |

## Workflow tip

When you update shared content (new award, publication, project), edit **CVs/master** first, then pull the relevant bullets into active tailored resumes.
