#!/usr/bin/env python3
"""Create all remaining files for hotel-rm-report repo."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOBILE = Path("/Users/giantkd/WINDOWS/BKU/HK261/Mobile/mobile-report")

# ── Files to copy verbatim from mobile-report ──
COPY_VERBATIM = [
    (".latexmkrc", None),
    (".gitignore", None),
    (".vscode/settings.json", None),
    ("scripts/build.py", None),
    ("styles/guide.tex", None),
]

for rel, _ in COPY_VERBATIM:
    src = MOBILE / rel
    dst = ROOT / rel
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  copied {rel}")
    else:
        print(f"  SKIP (not found) {rel}")

# ── .github/workflows/build.yml (adapt URL) ──
ci = (MOBILE / ".github/workflows/build.yml").read_text()
(ROOT / ".github/workflows/build.yml").write_text(ci)
print("  copied .github/workflows/build.yml")

# ── frontmatter/titlepage.tex (adapt from mobile) ──
titlepage = r"""\begin{titlepage}
    \begin{tikzpicture}[remember picture, overlay, inner sep=0, outer sep=0]
        \draw[blue!70!black, line width=4pt]
            ([xshift=-1.5cm,yshift=-2cm]current page.north east) coordinate (A)
            -- ([xshift=1.5cm,yshift=-2cm]current page.north west) coordinate (B)
            -- ([xshift=1.5cm,yshift=2cm]current page.south west) coordinate (C)
            -- ([xshift=-1.5cm,yshift=2cm]current page.south east) coordinate (D) -- cycle;
        \draw ([yshift=0.5cm,xshift=-0.5cm]A) -- ([yshift=0.5cm,xshift=0.5cm]B)
            -- ([yshift=-0.5cm,xshift=0.5cm]B) -- ([yshift=-0.5cm,xshift=-0.5cm]B)
            -- ([yshift=0.5cm,xshift=-0.5cm]C) -- ([yshift=0.5cm,xshift=0.5cm]C)
            -- ([yshift=-0.5cm,xshift=0.5cm]C) -- ([yshift=-0.5cm,xshift=-0.5cm]D)
            -- ([yshift=0.5cm,xshift=-0.5cm]D) -- ([yshift=0.5cm,xshift=0.5cm]D)
            -- ([yshift=-0.5cm,xshift=0.5cm]A) -- ([yshift=-0.5cm,xshift=-0.5cm]A)
            -- ([yshift=0.5cm,xshift=-0.5cm]A);
        \draw ([yshift=-0.3cm,xshift=0.3cm]A) -- ([yshift=-0.3cm,xshift=-0.3cm]B)
            -- ([yshift=0.3cm,xshift=-0.3cm]B) -- ([yshift=0.3cm,xshift=0.3cm]B)
            -- ([yshift=-0.3cm,xshift=0.3cm]C) -- ([yshift=-0.3cm,xshift=-0.3cm]C)
            -- ([yshift=0.3cm,xshift=-0.3cm]C) -- ([yshift=0.3cm,xshift=0.3cm]D)
            -- ([yshift=-0.3cm,xshift=0.3cm]D) -- ([yshift=-0.3cm,xshift=-0.3cm]D)
            -- ([yshift=-0.3cm,xshift=-0.3cm]A) -- ([yshift=0.3cm,xshift=0.3cm]A)
            -- ([yshift=-0.3cm,xshift=0.3cm]A);
    \end{tikzpicture}
    \vspace{0.25cm}
    \begin{center}
        \textbf{ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH}\\
        \vspace{0.05cm}
        \textbf{TRƯỜNG ĐẠI HỌC BÁCH KHOA}\\
        \vspace{0.05cm}
        \textbf{KHOA KHOA HỌC VÀ KỸ THUẬT MÁY TÍNH} \\
    \end{center}
    \vspace{0.55cm}
    \begin{figure}[h!]
        \begin{center}
            \includegraphics[scale=0.5]{hcmut.png}
        \end{center}
    \end{figure}
    \vspace{0.55cm}
    \begin{center}
        \parbox{0.9\linewidth}{\centering
            {\Large \textbf{\coursename{} (\coursecode)}}\\[0.3cm]
            \rule{0.85\linewidth}{0.5pt}\\[0.4cm]
            {\Large \textbf{\reportkind\ifdefempty{\reportphase}{}{ -- \reportphase}}}\\[0.3cm]
            {\Large \textbf{\textit{``\reporttitle''}}}
            \\[0.4cm]
            \rule{0.85\linewidth}{0.5pt}
        }
        \vspace{1cm}
        \newcommand{\stackedlines}[1]{\begin{tabular}[t]{@{}l@{}}#1\end{tabular}}
        \begin{tabular}{r l}
            \textbf{GVHD:} & \stackedlines{\reportadvisors} \\
                                 &                                \\
            \textbf{Sinh viên:} & \stackedlines{\reportstudents} \\
        \end{tabular}
    \end{center}
    \vspace{4.25cm}
    \begin{center}
        \textbf{\reportplace{} $-$ \reportyear}
    \end{center}
\end{titlepage}"""
(ROOT / "frontmatter/titlepage.tex").write_text(titlepage)
print("  wrote frontmatter/titlepage.tex")

(ROOT / "frontmatter/acknowledgement.tex").write_text(
    "% TODO: Lời cảm ơn\n\\section*{Lời cảm ơn}\n\nChúng em xin gửi lời cảm ơn...\n")
print("  wrote frontmatter/acknowledgement.tex")

# ── styles/diagrams.tex ──
(ROOT / "styles/diagrams.tex").write_text(r"""% TikZ styles for diagrams (star schema, DSS architecture, influence diagrams)
\tikzset{
    factbox/.style={rectangle, draw=blue!70!black, fill=blue!10, thick, minimum width=3.2cm, minimum height=1.2cm, align=center},
    dimbox/.style={rectangle, draw=orange!80!black, fill=orange!10, thick, minimum width=2.6cm, minimum height=0.9cm, align=center},
    sysbox/.style={rectangle, draw=teal!70!black, fill=teal!10, thick, minimum width=3.5cm, minimum height=1.3cm, align=center, rounded corners=3pt},
    arrow/.style={-{Stealth[length=3mm]}, thick},
    dasharrow/.style={-{Stealth[length=3mm]}, thick, dashed},
    label/.style={font=\small\itshape, text=gray},
}
""")
print("  wrote styles/diagrams.tex")

# ── refs.bib ──
refs = r"""@book{kimball2013,
  author    = {Kimball, Ralph and Ross, Margy},
  title     = {The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling},
  edition   = {3},
  publisher = {Wiley},
  year      = {2013},
  address   = {Indianapolis, IN}
}

@book{goeldner2009,
  author    = {Goeldner, Charles R. and Ritchie, J. R. Brent},
  title     = {Tourism: Principles, Practices, Philosophies},
  edition   = {11},
  publisher = {Wiley},
  year      = {2009},
  address   = {Hoboken, NJ}
}

@article{antonio2019,
  author  = {Antonio, Nuno and Almeida, Ana and Nunes, Lu{\'i}s},
  title   = {Hotel booking demand datasets},
  journal = {Data in Brief},
  volume  = {22},
  pages   = {41--49},
  year    = {2019},
  doi     = {10.1016/j.dib.2018.11.126}
}

@book{turban2011,
  author    = {Turban, Efraim and Sharda, Ramesh and Delen, Dursun},
  title     = {Decision Support and Business Intelligence Systems},
  edition   = {9},
  publisher = {Prentice Hall},
  year      = {2011}
}

@book{hoffer2016,
  author    = {Hoffer, Jeffrey A. and Ramesh, V. and Topi, Heikki},
  title     = {Modern Database Management},
  edition   = {12},
  publisher = {Pearson},
  year      = {2016}
}

@book{inmon2005,
  author    = {Inmon, William H.},
  title     = {Building the Data Warehouse},
  edition   = {4},
  publisher = {Wiley},
  year      = {2005}
}

@article{weatherford2003,
  author  = {Weatherford, Lawrence R. and Kimes, Sheryl E.},
  title   = {A comparison of forecasting methods for hotel revenue management},
  journal = {International Journal of Forecasting},
  volume  = {19},
  number  = {3},
  pages   = {401--415},
  year    = {2003}
}

@article{rothstein1971,
  author  = {Rothstein, Marvin},
  title   = {An Airline Overbooking Model},
  journal = {Transportation Science},
  volume  = {5},
  number  = {2},
  pages   = {180--192},
  year    = {1971}
}

@book{talluri2004,
  author    = {Talluri, Kalyan T. and van Ryzin, Garrett J.},
  title     = {The Theory and Practice of Revenue Management},
  publisher = {Kluwer Academic Publishers},
  year      = {2004}
}

@article{song2008,
  author  = {Song, Haiyan and Li, Gang},
  title   = {Tourism demand modelling and forecasting --- {A} review of recent research},
  journal = {Tourism Management},
  volume  = {29},
  number  = {2},
  pages   = {203--220},
  year    = {2008}
}

@article{peng2014,
  author  = {Peng, Bao and Song, Haiyan and Crouch, Geoffrey I.},
  title   = {A meta-analysis of international tourism demand forecasting and implications for practice},
  journal = {Tourism Management},
  volume  = {45},
  pages   = {181--193},
  year    = {2014}
}
"""
(ROOT / "refs.bib").write_text(refs)
print("  wrote refs.bib")

# ── Section files ──
sections = {
    "1-introduction": {
        "main.tex": r"""\section{Introduction}
\input{sections/1-introduction/background}
\input{sections/1-introduction/objectives}""",
        "background.tex": r"""\subsection{Background and Motivation}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Tourism phenomenon là gì (Goeldner \& Ritchie, 2009, tr.~14)
    \item Vì sao chọn domain Tourism $\to$ Hotel Revenue Management
    \item Dataset: Antonio et al.\ (2019), 119{,}390 bookings, 2 hotels Bồ Đào Nha
  \end{itemize}
  \guidepart{Câu hỏi cần trả lời}
  \begin{itemize}
    \item Vì sao tourism là domain quan trọng?
    \item Trong tourism, vì sao chọn accommodation/lodging?
    \item Trong lodging, vì sao cần revenue management?
  \end{itemize}
\end{guide}""",
        "objectives.tex": r"""\subsection{Objectives}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Mục tiêu: xây dựng DSS cho quản lý doanh thu khách sạn
    \item Ba quyết định hỗ trợ: định giá, phân bổ, overbooking
    \item Output: RevPAR, ADR, occupancy
  \end{itemize}
\end{guide}""",
    },
    "2-business-problem": {
        "main.tex": r"""\section{Business Problem Definition}
\input{sections/2-business-problem/tourism-components}
\input{sections/2-business-problem/lodging-industry}
\input{sections/2-business-problem/problem-statement}
\input{sections/2-business-problem/goals}""",
        "tourism-components.tex": r"""\subsection{Tourism Components}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Goeldner Figure 1.2: 4 components (Tourist, Natural Resources, Built Environment, Operating Sectors)
    \item Trích: ``The very heart of the tourism phenomenon model is unequivocally the tourist'' (tr.~15)
    \item Trích: ``hotels, restaurants, conference centers'' $\subset$ tourism superstructure (tr.~17)
    \item Trích: ``increased use of central reservation systems, emphasis on service, and the use of yield management techniques'' (tr.~190)
  \end{itemize}
\end{guide}""",
        "lodging-industry.tex": r"""\subsection{Lodging Industry}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Số liệu AH\&LA: 47,135 properties, 4.4M rooms, \$133.4B sales, 63.3\% occupancy (tr.~156)
    \item 3 chỉ số: ADR, occupancy, RevPAR (glossary tr.~186)
    \item 2 segments: business (44\%, \$112/night) vs leisure (56\%, \$103/night)
    \item Hàng dễ hỏng (perishable inventory) + mùa vụ + sức chứa cố định
  \end{itemize}
\end{guide}""",
        "problem-statement.tex": r"""\subsection{Problem Statement}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Decision makers: revenue manager (cô Lan) + giám đốc vận hành
    \item 3 quyết định: (1) giá theo hạng/ngày, (2) phân bổ đoàn/lẻ, (3) overbooking
    \item Vì sao semistructured: máy tính làm được phần số, người phán đoán phần còn lại
    \item Dataset: 119,390 bookings, 32 columns, 2015--2017
  \end{itemize}
\end{guide}""",
        "goals.tex": r"""\subsection{Expected Goals}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Mục tiêu chính: tối đa RevPAR
    \item Mục tiêu phụ: giảm phòng trống mùa thấp
    \item Ràng buộc: số walk $\leq$ ngưỡng
  \end{itemize}
\end{guide}""",
    },
    "3-proposed-solution": {
        "main.tex": r"""\section{Proposed Solution}
\input{sections/3-proposed-solution/architecture}
\input{sections/3-proposed-solution/star-schema}
\input{sections/3-proposed-solution/models}
\input{sections/3-proposed-solution/mbms}""",
        "architecture.tex": r"""\subsection{DSS Architecture}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item 4 phân hệ DSS (Ch6 slide): data management, model management, UI, knowledge-based
    \item Sơ đồ kiến trúc tổng thể (TikZ hoặc figure)
    \item Stack: DuckDB + statsmodels + PuLP + Streamlit
  \end{itemize}
\end{guide}""",
        "star-schema.tex": r"""\subsection{Star Schema Design}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Kimball 4 bước: business process $\to$ grain $\to$ dimensions $\to$ facts
    \item Grain: booking-night (1 dòng = 1 đêm $\times$ 1 booking)
    \item Goeldner tr.~419: ``Hotel and other accommodations people want data on visitor-nights''
    \item fact\_room\_night + fact\_daily\_occupancy + 7 dims
    \item Sơ đồ star schema (figure)
  \end{itemize}
\end{guide}""",
        "models.tex": r"""\subsection{Model Catalog}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item M1 Forecasting (Holt-Winters): dự báo nhu cầu theo mùa
    \item M2 Optimization (LP/PuLP): phân bổ phòng đoàn/lẻ
    \item M3 Overbooking (cost model): mức bán vượt tối ưu
    \item Mỗi model khai báo 4 loại biến (decision, uncontrollable, intermediate, result)
    \item Mỗi model khai báo static/dynamic + certainty/risk/uncertainty + cấp quản lý
  \end{itemize}
\end{guide}""",
        "mbms.tex": r"""\subsection{Model Base Management Subsystem}
\begin{guide}
  \guidepart{Nội dung cần có — ĐỀ TÀI NHÓM, TRÌNH BÀY SÂU}
  \begin{itemize}
    \item Định nghĩa MBMS (Ch7 slide 61): ``capabilities similar to those of a DBMS''
    \item ``No standard MBMS'' (Ch7 slide 63): vì sao nhóm tự thiết kế
    \item 6 năng lực MBMS (Ch7 slide 62): Control, Flexibility, Feedback, Interface, Redundancy reduction, Increased consistency
    \item Model registry: metadata từng model + versioning
    \item Sơ đồ MBMS trong kiến trúc tổng thể
  \end{itemize}
\end{guide}""",
    },
    "4-application": {
        "main.tex": r"""\section{Application Development}
\input{sections/4-application/etl}
\input{sections/4-application/model-implementation}
\input{sections/4-application/ui}
\input{sections/4-application/tech-stack}""",
        "etl.tex": r"""\subsection{ETL Pipeline}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Extract: đọc CSV (pandas)
    \item Transform: ghép 4 cột arrival $\to$ date, tách booking-night, mã hóa surrogate keys
    \item Load: nạp vào DuckDB star schema
    \item Sơ đồ pipeline + screenshot DuckDB
  \end{itemize}
\end{guide}""",
        "model-implementation.tex": r"""\subsection{Model Implementation}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item M1: statsmodels ExponentialSmoothing, train 2015--2016, test 2017
    \item M2: PuLP LP, biến + ràng buộc + objective function
    \item M3: cost model, công thức break-even $p \geq C/(ADR + C)$
    \item Registry: JSON + run(model\_id, params)
    \item Code snippets quan trọng
  \end{itemize}
\end{guide}""",
        "ui.tex": r"""\subsection{Streamlit User Interface}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item 4 màn: Dashboard (OLAP), Model Catalog (MBMS), What-if/Goal-seeking, Tracking
    \item Screenshots từng màn
    \item Mô tả luồng người dùng theo 4 pha Simon
  \end{itemize}
\end{guide}""",
        "tech-stack.tex": r"""\subsection{Technology Stack}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Bảng: công cụ $\times$ vai trò $\times$ lý do chọn
    \item Python + DuckDB + statsmodels + PuLP + Streamlit + Plotly
    \item Trade-off: vì sao không dùng Excel/Power BI
  \end{itemize}
\end{guide}""",
    },
    "5-evaluation": {
        "main.tex": r"""\section{Evaluation}
\input{sections/5-evaluation/model-performance}
\input{sections/5-evaluation/whatif-demo}
\input{sections/5-evaluation/limitations}""",
        "model-performance.tex": r"""\subsection{Model Performance}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item M1: MAPE, RMSE, so sánh baseline (naive seasonal)
    \item M2: LP solution (số phòng đoàn tối ưu, doanh thu)
    \item M3: mức overbooking khuyến nghị theo kịch bản
    \item Biểu đồ forecast vs actual
  \end{itemize}
\end{guide}""",
        "whatif-demo.tex": r"""\subsection{What-if Demonstration}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Kịch bản demo theo 4 pha Simon
    \item Screenshot what-if (slider $\to$ chart update)
    \item Screenshot goal-seeking (nhập RevPAR target $\to$ calculate price)
  \end{itemize}
\end{guide}""",
        "limitations.tex": r"""\subsection{Limitations and Assumptions}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Total rooms không có sẵn $\to$ estimate từ max(rooms\_sold)
    \item adr = 0 $\to$ complimentary rooms, cần filter
    \item Revenue = room revenue only (không gồm F\&B)
    \item 2 khách sạn khác phân khúc $\to$ chạy model riêng
    \item Booking hủy: demand vs revenue phân biệt
  \end{itemize}
\end{guide}""",
    },
    "6-conclusion": {
        "main.tex": r"""\section{Conclusion}
\input{sections/6-conclusion/summary}
\input{sections/6-conclusion/future-work}""",
        "summary.tex": r"""\subsection{Summary}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Tóm tắt: đã xây dựng gì, đạt được gì
    \item Điểm mạnh: DW + MBMS + 3 models + interactive UI
  \end{itemize}
\end{guide}""",
        "future-work.tex": r"""\subsection{Future Work}
\begin{guide}
  \guidepart{Nội dung cần có}
  \begin{itemize}
    \item Mở rộng: thêm model ML, thêm mảng (Spa, F\&B), SCD Type 2
    \item Kết nối real-time data source
  \end{itemize}
\end{guide}""",
    },
}

for dirname, files in sections.items():
    for fname, content in files.items():
        fpath = ROOT / "sections" / dirname / fname
        fpath.parent.mkdir(parents=True, exist_ok=True)
        fpath.write_text(content)
        print(f"  wrote sections/{dirname}/{fname}")

# ── docs files ──
docs = {
    "decisions.md": """# Design Decisions Log

| # | Date | Decision | Rationale |
|---|------|----------|-----------|
| 1 | 2026-10-29 | Grain = booking-night | Goeldner tr.419: "Hotel and other accommodations people want data on visitor-nights" |
| 2 | 2026-10-29 | DuckDB cho DW | Data nhỏ (119K), không cần server, SQL analytic nhanh |
| 3 | 2026-10-29 | Kimball bottom-up | Scope 1 học kỳ, 1 business process, 1 star schema |
| 4 | 2026-10-31 | Filter is_canceled=0 khi tính revenue | Booking hủy không thu tiền |
| 5 | 2026-10-31 | Estimate total_rooms từ max(rooms_sold) | Dataset không có total_rooms |
| 6 | 2026-10-31 | Chạy model riêng cho H1/H2 | Resort vs City khác demand pattern |
""",
    "assumptions.md": """# Assumptions and Limitations

## Assumptions
1. Total rooms: estimated from max(rooms_sold_per_day) in data (dataset does not include this)
2. adr = 0 bookings are complimentary rooms (filtered or noted)
3. Revenue = adr × nights = room revenue only (no F&B, parking, spa)
4. Season definition derived from data (GROUP BY month → observe ADR/occupancy)
5. Walk cost estimated by domain expert (parameter in UI, not from data)

## Limitations
1. Dataset is static (2015-2017), no real-time feeds
2. Two hotels are in different segments (resort vs city) — modeled separately
3. M1 (Holt-Winters) projects pattern but does not explain causality (Goeldner tr.422)
4. M3 uses simplified expected-value model, not full no-show distribution
5. No channel profitability modeling (commission rates by OTA vs Direct)
""",
    "demo-script.md": """# Demo Video Script (20-30 minutes)

## Pha 1: Intelligence (5 phút)
1. Mở Dashboard → chỉ thấy occupancy tuần tới dự báo 55% vs mọi năm 75%
2. Drill-down: mùa → tháng → tuần, slice theo H1/H2
3. Dice: chỉ khách lẻ + mùa cao → thấy ADR đang thấp

## Pha 2: Design (8 phút)
1. Mở tab What-if
2. Kéo slider giá hạng A từ $120 lên $132
3. M1 chạy lại → dự báo khách lẻ giảm → M2 giải lại → RevPAR thay đổi
4. Thử phương án 2: nhập đoàn 40 phòng $80 → M2 khuyến nghị 30 phòng

## Pha 3: Choice (5 phút)
1. Bảng so sánh các kịch bản cạnh nhau
2. Goal-seeking: "muốn RevPAR $85 thì giá hạng A phải là bao nhiêu?"
3. Chọn phương án + ghi chú lý do

## Pha 4: Implementation (5 phút)
1. Mở tab Tracking → so sánh thực tế vs kế hoạch
2. Quay về Dashboard → vòng lặp đóng

## Model Catalog (5 phút)
1. Mở tab Model Catalog
2. Hiển thị registry: M1, M2, M3 + metadata + version
3. Chỉ ra 6 năng lực MBMS tương ứng trong app
""",
}
for fname, content in docs.items():
    (ROOT / "docs" / fname).write_text(content)
    print(f"  wrote docs/{fname}")

# ── README.md ──
readme = """# Hotel RM Report

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
- Mỗi section cấp 1 là một thư mục `sections/<order>-<name>/`. File `main.tex` của section chứa lệnh `\\section{}` và `\\input` các subsection, mỗi subsection nằm trong một file riêng.
- Hình minh họa đặt trong `figures/<section name>/`. Preamble đã khai báo `\\graphicspath{{figures/}}`.
- Mọi đường dẫn trong `\\input` và `\\include` đều tính từ thư mục gốc của repo.
- Tiêu đề viết hoa chữ cái đầu như một câu bình thường. Thuật ngữ quen dùng bằng tiếng Anh (DSS, Star Schema, Revenue Management, MBMS, ...) giữ nguyên.

## Cách build

```bash
python3 scripts/build.py        # build once
python3 scripts/build.py watch  # watch mode
python3 scripts/build.py clean  # clean
```

Yêu cầu: TeX Live với vntex (T5), biber, latexmk.
"""
(ROOT / "README.md").write_text(readme)
print("  wrote README.md")

# ── CONTRIBUTING.md (adapted) ──
contrib = (MOBILE / "CONTRIBUTING.md").read_text()
(ROOT / "CONTRIBUTING.md").write_text(contrib)
print("  wrote CONTRIBUTING.md")

print("\n✅ All files created.")
