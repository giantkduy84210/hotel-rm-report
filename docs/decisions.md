# Design Decisions Log

| # | Date | Decision | Rationale |
|---|------|----------|-----------|
| 1 | 2026-10-29 | Grain = booking-night | Goeldner p. 419: "Hotel and other accommodations people want data on visitor-nights" |
| 2 | 2026-10-29 | DuckDB for the DW | Small data (119K rows), no server needed, fast analytic SQL |
| 3 | 2026-10-29 | Kimball bottom-up | One-semester scope, 1 business process, 1 star schema |
| 4 | 2026-10-31 | Filter is_canceled = 0 when computing revenue | Canceled bookings generate no revenue |
| 5 | 2026-10-31 | Estimate total_rooms from max(rooms_sold) | The dataset has no total_rooms column |
| 6 | 2026-10-31 | Run models separately for H1/H2 | Resort and city hotels have different demand patterns |
