# Commit conventions

This repo follows [Conventional Commits](https://www.conventionalcommits.org/) with `type` and `scope` values adapted to report writing instead of software development. Commit messages are written in English.

## Format

```text
<type>(<scope>): <subject>

<body>
```

- `type`: required, pick one value from the table below.
- `scope`: optional, tells which part of the report changed.
- `subject`: a short description of the change, imperative mood (`add`, `fix`, `update`, not `added` or `adds`), lowercase first letter, no trailing period, whole first line at most 72 characters.
- `body`: optional, separated from the first line by a blank line, explains the motivation when the subject alone is not clear. Wrap lines at 72 characters.

## Type

| Type | Use when |
|---|---|
| `content` | Writing or editing report content: sections, subsections, paragraphs, tables, acknowledgements |
| `fix` | Fixing errors in content or compile errors: typos, wrong figures, broken `\ref`/`\cite`, LaTeX errors |
| `figure` | Adding or changing figures in `figures/` |
| `ref` | Adding, editing or removing references in `refs.bib` |
| `style` | Presentation-only changes that do not alter content: preamble, page layout, fonts, header/footer, heading format, title page |
| `build` | Changing how the report builds: `.latexmkrc`, `scripts/build.py` |
| `ci` | Changing the GitHub Actions workflows |
| `docs` | Changing repo documentation: `README.md`, `CONTRIBUTING.md` (not the report content) |
| `chore` | Everything else: `metadata.tex`, `.gitignore`, editor config, cleaning up files |
| `revert` | Reverting a previous commit; the subject is the title of the reverted commit |

If a commit falls under several types, split it into several commits. When that is not possible, pick the type of the main change.

## Scope

A scope is a section name (without the order prefix of the folder) or a fixed area of the repo:

| Scope | Covers |
|---|---|
| `introduction`, `business-problem`, `proposed-solution`, `application`, `evaluation`, `conclusion` | The matching section in `sections/<order>-<name>/` and its `figures/<name>/` folder |
| `frontmatter` | Title page, acknowledgements |
| `metadata` | `metadata.tex` |

A scope can be omitted when the change is not tied to a specific part, e.g. `ref`, `build`, `ci`, or when it spans several sections.

## Examples

```text
content(introduction): add the tourism phenomenon background
content(proposed-solution): compare the Inmon and Kimball approaches
fix(business-problem): correct the ADR definition
fix: resolve broken references after renaming section 3 labels
figure(proposed-solution): add the star schema diagram
ref: add the Kimball Data Toolkit book
style(frontmatter): align student names on the title page
chore(metadata): set phase 2 and the course code
build: fail the build on undefined citations
ci: attach the PDF to published releases
docs: explain the checkpoint workflow in README
```

Example commit with a body:

```text
content(proposed-solution): declare the four variable types of each model

Chapter 7 distinguishes decision, uncontrollable, intermediate and
result variables, so the model catalog now lists them for M1--M3.
```

## Pull requests and checkpoints

- `main` does not accept direct pushes. Every change is written on its own branch (e.g. `content/tourism-background`), a pull request is opened into `main` and can only be merged when the `build` check passes.
- When merging a pull request with **Squash and merge** (the only enabled merge method), the pull request title becomes the commit message on `main`. The pull request title therefore follows the same format.
- Once a subsection is written, delete its `guide` (writing guide) box in the same commit, see [README](README.md#writing-guide-boxes).
- Before creating a checkpoint for a phase, update `\reportphase` in `metadata.tex` in its own pull request, e.g. `chore(metadata): set phase 1`. Then create the release as described in [README](README.md#creating-a-checkpoint-for-a-phase).
