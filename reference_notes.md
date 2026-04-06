# References

## Deployment

- run `gh workflow run publish-resumes  -r $(git branch --show-current)` to generate

## Template Notes

- [ ] Task -> 🗒️ understand altacv

- columnratio is important
- work in overleaf https://www.overleaf.com/latex/templates/altacv-template/trgqjpwnmtgv
- work in overleaf https://www.overleaf.com/project/69d089f40e7e3ce53a7d739c
- seems like fontawesome symbols are available

- might be cool to add this

```latex
\cvsection{Languages}

\cvskill{{\faHeartbeat} Python }{5}
\divider

\cvskill{Spanish}{4}
\divider

\cvskill{German}{3.5} %% Supports X.5 values.

%% Yeah I didn't spend too much time making all the
%% spacing consistent... sorry. Use \smallskip, \medskip,
%% \bigskip, \vspace etc to make adjustments.
\medskip

```

## New Tools

### LaTeX

### pdfinfo

```sh
pdfinfo your_cv.pdf | grep "Pages:" | awk '{print $2}'
```

### pdflatex

### pdftotext

## Issues + Updates

- need to call `make ats-all` to get ATS locally
- to run locally also requires `sudo apt install texlive-fonts-extra texlive-full`

## Misc

## Keep

[![CV Pipeline as Code: LaTeX, YAML, and GitHub Actions](https://img.youtube.com/vi/S2gpOr-mbf4/maxresdefault.jpg)](https://youtu.be/S2gpOr-mbf4)

**CV Pipeline as Code: LaTeX, YAML, and GitHub Actions** - Learn how to use this template to automate your CV generation workflow.

## Customization

### Add New Variants

1. Create template directory: `templates/new-variant/`
2. Add template file: `templates/new-variant/template.tex.j2`
3. Add tagline to `data/personal.yaml`
4. Tag relevant experience in `data/experience.yaml`
5. Update `Makefile` VARIANTS list
6. Update `.github/workflows/cv-build.yml` matrix

### Modify Colors/Design

Edit templates in `templates/*/template.tex.j2` - each uses AltaCV LaTeX class with customizable colors.

**Current color schemes** (based on color psychology research):

- **Software Developer**: Purple (#7C3AED) - Innovation, creativity, problem-solving
- **DevOps Engineer**: Orange (#FF6B35) - Energy, collaboration, developer enablement
- **Cloud Engineer**: Steel Blue (#4682B4) - Trust, reliability, professionalism

- [ ] Task -> 🗒️ rewrite this

## Troubleshooting

### PDFs not generating locally?

Check dependencies:

```bash
# Python packages
pip list | grep PyYAML

# LaTeX
pdflatex --version

# PDF utilities
pdftotext -v
```

### Tests failing?

Run verbose test output:

```bash
python scripts/test_data_completeness.py
```

Common issues:

- Missing data in YAML files
- Special characters in LaTeX (use `\&` for `&`, `\%` for `%`)
- Tags not matching template filters

## Troubleshooting

### PDFs not generating locally?

Check dependencies:

```bash
# Python packages
pip list | grep PyYAML

# LaTeX
pdflatex --version

# PDF utilities
pdftotext -v
```

### Tests failing?

Run verbose test output:

```bash
python scripts/test_data_completeness.py
```

Common issues:

- Missing data in YAML files
- Special characters in LaTeX (use `\&` for `&`, `\%` for `%`)
- Tags not matching template filters
