# CVs

Keep one public **master CV** as the full academic record for the website. Use tailored resumes, not extra public CVs, for specific applications.

## Layout

```
CVs/
└── master/                      # Full CV: research, conferences, leadership, service
    ├── Rojae_Mighty_CV.md
    └── Rojae_Mighty_CV.pdf
```

## Markdown to PDF workflow

1. Edit the relevant `Rojae_Mighty_CV.md`.
2. Render PDFs from the repo root:

   ```bash
   make cv-pdf
   ```

## Which file to use when

| Situation | File |
|-----------|------|
| Grad school, fellowships, research programs | `CVs/master/Rojae_Mighty_CV.pdf` |
| Website download link | `CVs/master/Rojae_Mighty_CV.pdf` |

## Workflow tip

When shared content changes, edit **CVs/master/Rojae_Mighty_CV.md** first, render the PDF, then pull relevant bullets into the tailored resume Markdown files.
