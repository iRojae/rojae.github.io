# CVs

One folder per application. Keep the **master CV** as your full academic record; create **tailored CVs** from the template for each role or program.

## Layout

```
CVs/
├── master/                      # Full CV (grad school, conferences, leadership)
│   ├── Rojae_Mighty_CV.tex
│   └── Rojae_Mighty_CV.pdf
├── google-student-researcher/   # Tailored for Google Student Researcher
│   ├── Rojae_Mighty_CV.tex
│   └── Rojae_Mighty_CV.pdf
└── _template/                   # Starting point for new applications
    └── Rojae_Mighty_CV.tex
```

## Add a new tailored CV

1. Copy `_template/` to a new folder named `company-role` (e.g. `mit-grad-admissions`).
2. Edit the `.tex` file — emphasize relevant research, awards, and skills for that audience.
3. Compile and commit both `.tex` and `.pdf`:

   ```bash
   cd CVs/your-new-folder
   pdflatex Rojae_Mighty_CV.tex
   ```

## Which file to use when

| Situation | File |
|-----------|------|
| Grad school, fellowships, research programs | `CVs/<company-role>/Rojae_Mighty_CV.pdf` or `CVs/master/Rojae_Mighty_CV.pdf` |
| Website download link | `CVs/master/Rojae_Mighty_CV.pdf` |

## Workflow tip

When you update shared content (new award, publication, project), edit **master** first, then pull the relevant sections into any active tailored CVs.
