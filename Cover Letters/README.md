# Cover Letters

One folder per application. Create tailored cover letters from the template for each role.

## Layout

```
Cover Letters/
├── Chase Invest/
│   ├── Chase_Invest.tex
│   └── Chase_Invest.pdf
├── Two Sigma/
│   ├── Two_Sigma.tex
│   └── Two_Sigma.pdf
├── voloridge-quantitative-developer-intern-2027/
│   ├── Cover_Letter.tex
│   └── Cover_Letter.pdf
└── _template/
    └── Cover_Letter.tex
```

## Add a new cover letter

1. Copy `_template/` to a new folder named `company-role`.
2. Edit the `.tex` file for that application.
3. Compile and commit both `.tex` and `.pdf`:

   ```bash
   cd "Cover Letters/your-new-folder"
   pdflatex Cover_Letter.tex
   ```

## Workflow tip

Pair each cover letter with the matching tailored resume in `resumes/<company-role>/` when available.
