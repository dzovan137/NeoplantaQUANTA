# Introduction to Quantum Information

An interactive course built with **[Jupyter Book 2](https://next.jupyterbook.org) / [MyST](https://mystmd.org)**.
Prose, LaTeX, figures, and Python snippets that students copy into their own notebooks
(code is shown for reading, it is **not** executed in the page).

## Read the course

Once deployed, the site lives at:
**https://dzovan137.github.io/NeoplantaQUANTA/**

## Build it locally

You need [Node.js](https://nodejs.org) (v18+). Then:

```bash
npm install -g mystmd     # install the MyST CLI (once)
myst start                # live preview at http://localhost:3000
myst build --html         # build the static site into _build/html
```

## Project layout

```
myst.yml                    # site + project configuration (title, TOC, math macros)
intro.md                    # landing page
content/01-qubits.md        # Lesson 1 — image, LaTeX, and copy-paste Python
content/02-feature-gallery.md  # reference page showing every MyST feature used here
images/                     # figures
references.bib              # bibliography
.github/workflows/deploy.yml   # auto-deploy to GitHub Pages on push to main
```

## How the course is published

Pushing to `main` triggers the GitHub Action in `.github/workflows/deploy.yml`,
which builds the site and publishes it to GitHub Pages. Enable it once under
**Settings → Pages → Source: GitHub Actions**.

## License

Content is licensed CC-BY-4.0 and code MIT (see `myst.yml`).
