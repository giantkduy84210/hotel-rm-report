# Hotel RM Report

Repo chứa source LaTeX của report môn học. Mỗi khi branch `main` thay đổi, GitHub Actions compile lại report và cập nhật bản PDF mới nhất tại:

**PDF mới nhất:** https://github.com/giantkduy84210/hotel-rm-report/releases/download/latest/report.pdf

## Cấu trúc repo

```text
.
├── main.tex                  # file gốc, ghép các phần của report theo thứ tự
├── metadata.tex              # tên môn học, mã môn, tên đề tài, giảng viên, sinh viên, năm
├── refs.bib                  # tài liệu tham khảo (biblatex + biber, style IEEE)
├── styles/
│   ├── preamble.tex          # khai báo package, layout trang, header/footer, định dạng heading
│   ├── guide.tex             # khung "Hướng dẫn viết" trong mỗi subsection
│   └── diagrams.tex         # TikZ styles cho star schema, DSS architecture
├── frontmatter/              # trang bìa, lời cảm ơn
├── sections/
│   ├── 1-introduction/       # Phần 1: giới thiệu
│   ├── 2-business-problem/   # Phần 2: business problem definition
│   ├── 3-proposed-solution/  # Phần 3: proposed solution (MMS deep)
│   ├── 4-application/        # Phần 4: application development
│   ├── 5-evaluation/         # Phần 5: evaluation
│   └── 6-conclusion/         # Phần 6: conclusion
├── figures/                  # hình minh họa, chia folder theo section
├── slides/                    # midterm + final presentation
├── docs/                      # research, decisions, assumptions, demo script
├── scripts/build.py          # script compile
├── .latexmkrc                # cấu hình build dùng chung cho local, VS Code và CI
├── CONTRIBUTING.md           # quy ước commit
└── .github/workflows/build.yml
```

Convention (giống mobile-report):
- Mỗi section cấp 1 là một thư mục `sections/<order>-<name>/`. File `main.tex` của section chứa lệnh `\section{}` và `\input` các subsection, mỗi subsection nằm trong một file riêng.
- Hình minh họa đặt trong `figures/<section name>/`. Preamble đã khai báo `\graphicspath{{figures/}}`.
- Mọi đường dẫn trong `\input` và `\include` đều tính từ thư mục gốc của repo.
- Tiêu đề viết hoa chữ cái đầu như một câu bình thường. Thuật ngữ quen dùng bằng tiếng Anh (DSS, Star Schema, Revenue Management, MBMS, ...) giữ nguyên.

## Cách build

```bash
python3 scripts/build.py        # build once
python3 scripts/build.py watch  # watch mode
python3 scripts/build.py clean  # clean
```

Yêu cầu: TeX Live với vntex (T5), biber, latexmk.
