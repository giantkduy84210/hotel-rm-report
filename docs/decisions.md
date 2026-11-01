# Design Decisions Log

| # | Date | Decision | Rationale |
|---|------|----------|-----------|
| 1 | 2026-10-29 | Grain = booking-night | Goeldner tr.419: "Hotel and other accommodations people want data on visitor-nights" |
| 2 | 2026-10-29 | DuckDB cho DW | Data nhỏ (119K), không cần server, SQL analytic nhanh |
| 3 | 2026-10-29 | Kimball bottom-up | Scope 1 học kỳ, 1 business process, 1 star schema |
| 4 | 2026-10-31 | Filter is_canceled=0 khi tính revenue | Booking hủy không thu tiền |
| 5 | 2026-10-31 | Estimate total_rooms từ max(rooms_sold) | Dataset không có total_rooms |
| 6 | 2026-10-31 | Chạy model riêng cho H1/H2 | Resort vs City khác demand pattern |
