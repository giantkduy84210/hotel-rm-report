# Hotel RM Report

LaTeX source of the course report. Every push to `main` makes GitHub Actions rebuild the report and update the latest PDF at:

**Latest PDF:** https://github.com/giantkduy84210/hotel-rm-report/releases/download/latest/report.pdf

## Repository layout

```text
.
├── main.tex                  # root file, assembles the report sections in order
├── metadata.tex              # course name, course code, report title, advisor, students, year
├── refs.bib                  # references (biblatex + biber, IEEE style)
├── styles/
│   ├── preamble.tex          # packages, page layout, header/footer, heading format
│   ├── guide.tex             # "Writing guide" boxes in each subsection
│   └── diagrams.tex          # TikZ styles for the star schema and DSS architecture
├── frontmatter/              # title page, acknowledgements
├── sections/
│   ├── 1-introduction/       # Section 1: introduction
│   ├── 2-business-problem/   # Section 2: business problem definition
│   ├── 3-proposed-solution/  # Section 3: proposed solution (MMS covered in depth)
│   ├── 4-application/        # Section 4: application development
│   ├── 5-evaluation/         # Section 5: evaluation
│   └── 6-conclusion/         # Section 6: conclusion
├── figures/                  # figures, one folder per section
├── slides/                   # midterm + final presentations
├── docs/                     # research, decisions, assumptions, demo script
├── scripts/build.py          # build script
├── .latexmkrc                # build config shared by local, VS Code and CI
├── CONTRIBUTING.md           # commit conventions
└── .github/workflows/build.yml
```

Conventions (same as mobile-report):
- Each level-1 section is a folder `sections/<order>-<name>/`. The section's `main.tex` holds the `\section{}` command and `\input`s the subsections, one file per subsection.
- Figures live in `figures/<section name>/`. The preamble declares `\graphicspath{{figures/}}`.
- All `\input` and `\include` paths are relative to the repo root.
- Headings are sentence case. Familiar English terms (DSS, Star Schema, Revenue Management, MBMS, ...) stay as they are.

## Writing-guide boxes

Each subsection starts with a `guide` box listing what the subsection must contain and which questions it must answer. Delete the box in the same commit that finishes the subsection; set `\showguidesfalse` in `metadata.tex` to preview the report without any of them.

## Creating a checkpoint for a phase

1. Update `\reportphase` in `metadata.tex` in its own pull request, e.g. `chore(metadata): set phase 1`.
2. Publish a release with a tag such as `phase-1` on the commit to checkpoint.
3. CI builds that exact commit and attaches `report-<tag>.pdf` to the release (never expires). The `latest` prerelease always tracks `main`.

## Building

```bash
python3 scripts/build.py        # build once
python3 scripts/build.py watch  # watch mode
python3 scripts/build.py clean  # clean
```

Requires a TeX Live installation with vntex (T5), biber and latexmk.
