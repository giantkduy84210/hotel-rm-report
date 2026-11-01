# Quy ước commit

Repo sử dụng [Conventional Commits](https://www.conventionalcommits.org/), với tập `type` và `scope` được điều chỉnh cho việc viết report thay vì phát triển phần mềm. Commit message viết bằng tiếng Anh.

## Định dạng

```text
<type>(<scope>): <subject>

<body>
```

- `type`: bắt buộc, chọn một giá trị trong bảng bên dưới.
- `scope`: không bắt buộc, cho biết phần nào của report bị thay đổi.
- `subject`: mô tả ngắn thay đổi, viết ở thể mệnh lệnh (`add`, `fix`, `update`, không viết `added` hay `adds`), chữ thường ở đầu, không có dấu chấm cuối câu, tổng độ dài dòng đầu không quá 72 ký tự.
- `body`: không bắt buộc, cách dòng đầu một dòng trống, dùng để giải thích lý do thay đổi khi subject chưa đủ rõ. Mỗi dòng không quá 72 ký tự.

## Type

| Type | Dùng khi |
|---|---|
| `content` | Viết mới hoặc chỉnh sửa nội dung report: section, subsection, đoạn văn, bảng, lời cảm ơn |
| `fix` | Sửa lỗi trong nội dung hoặc lỗi compile: typo, số liệu sai, `\ref`/`\cite` hỏng, lỗi LaTeX |
| `figure` | Thêm hoặc sửa figure trong `figures/`, bao gồm cả file source trong `src/` |
| `ref` | Thêm, sửa hoặc xóa tài liệu tham khảo trong `refs.bib` |
| `style` | Thay đổi hình thức trình bày mà không đổi nội dung: preamble, layout trang, font, header/footer, định dạng heading, trang bìa |
| `build` | Thay đổi cách build: `.latexmkrc`, `scripts/build.py` |
| `ci` | Thay đổi workflow GitHub Actions |
| `docs` | Thay đổi tài liệu của repo: `README.md`, `CONTRIBUTING.md` (không phải nội dung report) |
| `chore` | Các việc còn lại: `metadata.tex`, `.gitignore`, config editor, dọn file |
| `revert` | Hoàn tác một commit trước đó, subject là tiêu đề của commit bị hoàn tác |

Nếu một commit rơi vào nhiều type, nên tách thành nhiều commit. Trường hợp không tách được, chọn type ứng với thay đổi chính.

## Scope

Scope dùng tên section (bỏ phần số thứ tự trong tên folder) hoặc tên một khu vực cố định của repo:

| Scope | Phạm vi |
|---|---|
| `project-overview`, `product-scope`, `ui-ux-design`, `technical-architecture` | Section tương ứng trong `sections/<order>-<name>/` và folder `figures/<name>/` |
| `frontmatter` | Trang bìa, lời cảm ơn |
| `metadata` | `metadata.tex` |

Scope có thể bỏ qua khi thay đổi không gắn với một phần cụ thể, ví dụ `ref`, `build`, `ci`, hoặc khi thay đổi trải trên nhiều section.

## Ví dụ

```text
content(project-overview): add personas from the user survey
content(technical-architecture): compare Flutter and React Native
fix(product-scope): correct acceptance criteria of US-VID-03
fix: resolve broken references after renaming section 3 labels
figure(ui-ux-design): add cross-module user flow diagram
ref: add Jetpack Compose documentation
style(frontmatter): align student names on the title page
chore(metadata): set phase 2 and course code
build: fail the build on undefined citations
ci: attach the PDF to published releases
docs: explain the checkpoint workflow in README
```

Ví dụ commit có body:

```text
content(technical-architecture): cache news and music for offline use

The phase 1 feedback asked for offline support, so section 4.3 now
describes the local cache and how it syncs with the backend.
```

## Pull request và checkpoint

- `main` không nhận push trực tiếp. Mọi thay đổi được viết trên một branch riêng (ví dụ `content/user-personas`), mở pull request vào `main` và chỉ merge được khi check `build` pass.
- Khi merge pull request bằng **Squash and merge** (cách merge duy nhất được bật), title của pull request trở thành commit message trên `main`. Vì vậy title của pull request cũng theo đúng định dạng trên.
- Viết xong một subsection thì xóa khung `guide` (Hướng dẫn viết) của subsection đó trong cùng commit, xem [README](README.md#khung-hướng-dẫn-viết).
- Trước khi tạo checkpoint cho một giai đoạn, cập nhật `\reportphase` trong `metadata.tex` bằng một pull request riêng, ví dụ `chore(metadata): set phase 1`. Sau đó mới tạo release theo hướng dẫn trong [README](README.md#tạo-checkpoint-cho-từng-giai-đoạn).
