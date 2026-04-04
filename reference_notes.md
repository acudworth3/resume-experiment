# References

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
