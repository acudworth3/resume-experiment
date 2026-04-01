# Plan

> Use this as the basis for resume updates

## Tasking

- [ ] Read -> 📖 All files
- [x] Read -> 📖 Readme.md
- [x] Read -> 📖 watch video again https://www.youtube.com/watch?v=S2gpOr-mbf4
- [x] Task -> 🗒️ run it locally
- [x] Task -> 🗒️ ~update github action to use a release branch?~
- [x] Task -> 🗒️ ATS isn't being generated?

- [ ] Task -> 🗒️ setup treesitter for LaTeX

### New Tools

#### LaTeX

- [ ] Learn -> ❔ learn the basics

#### pdfinfo

- [x] Parse -> 📚 parse the command lines

```sh
pdfinfo your_cv.pdf | grep "Pages:" | awk '{print $2}'
```

#### pdflatex

#### pdftotext

### Resume

- [ ] Task -> 🗒️ figure out website display/removal
- [ ] Task -> 🗒️ in general need to adjust for multi line issues

- [ ] Task -> 🗒️ update certifications.yaml
- [ ] Task -> 🗒️ update experience.yaml
- [ ] Task -> 🗒️ update skills.yaml
- [ ] Task -> 🗒️ update strength.yaml

#### Extending this

- [ ] Task -> 🗒️ how to include meta data
- [ ] Task -> 🗒️ write a test to detect > 1 page `pdfinfo your_cv.pdf | grep "Pages:" | awk '{print $2}'`

- [ ] Task -> 🗒️ extend the make file
- [ ] Task -> 🗒️ host cvs with github pages

- `generate.py` is where you would add templates

### Files Parsing

- [x] Read -> 📖 MAKEFILE
- [x] Read -> 📖 generate.py
- [x] Read -> 📖 test_data_completeness.py
- [x] Read -> 📖 generate_ats.py
- [x] Read -> 📖 read the scripts
- [x] Read -> 📖 cv-build.yml

- [ ] Learn -> ❔ understand the tempaltes
- [ ] Read -> 📖 https://github.com/acudworth3/resume-experiment/blob/main/docs/CONTENT_GUIDE.md

## AI Integration

- [ ] Task -> 🗒️ develop strategy
- [x] Task -> 🗒️ fix github cli issue
- [ ] Task -> 🗒️ fix atuin

## Issues + Updates

- need to call `make ats-all` to get ATS locally
- to run locally also requires `sudo apt install texlive-fonts-extra texlive-full`

# Completed
