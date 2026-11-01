# Design Decisions Log

| # | Date | Decision | Rationale |
|---|------|----------|-----------|
| 1 | 2026-10-29 | Grain = booking-night | Goeldner p. 419: "Hotel and other accommodations people want data on visitor-nights" |
| 2 | 2026-10-29 | DuckDB for the DW | Small data (119K rows), no server needed, fast analytic SQL |
| 3 | 2026-10-29 | Kimball bottom-up | One-semester scope, 1 business process, 1 star schema |
| 4 | 2026-10-31 | Filter is_canceled = 0 when computing revenue | Canceled bookings generate no revenue |
| 5 | 2026-10-31 | Estimate total_rooms from max(rooms_sold) | The dataset has no total_rooms column |
| 6 | 2026-10-31 | Run models separately for H1/H2 | Resort and city hotels have different demand patterns |
| 7 | 2026-11-01 | Two fact tables: fact_room_night (booking-night) + fact_daily_occupancy (dense daily snapshot, hotel × date × room type) | Segment-level questions need booking-nights; occupancy needs a dense snapshot so empty nights count in the denominator |
| 8 | 2026-11-01 | KPIs computed as ratio-of-sums (SUM(revenue)/SUM(nights)), never AVG(rate) | Room rate is semi-additive; AVG weights bookings instead of room-nights |
| 9 | 2026-11-01 | Five models: M1 forecast, M2 Littlewood, M3 LP allocation, M4 overbooking, M5 pricing goal-seek | Covers all three decisions; Littlewood handles the single group request, LP the multi-night version |
| 10 | 2026-11-01 | MBMS implemented as database tables: model_catalog + run_model() registry + fact_scenario_run | "No standard MBMS" → take the DBMS analogy literally: catalog (schema), registry (query processor), run log (transaction log) |
| 11 | 2026-11-01 | Overbooking show-up probability p measured at cut-off h days before arrival (bookings still on the books), not from final status | Most cancellations happen early; the final show rate overstates no-show risk and over-recommends overbooking |
| 12 | 2026-11-01 | M1 compared against seasonal-naive baselines on the same backtest; the winner is used, not assumed | Honest evaluation discipline (a smoothing method can lose to a naive baseline) |
| 13 | 2026-11-01 | Overbooking evaluated by replaying historical bookings under different booking limits, with capacity stress (100/90/80%) | True overbooking never observed in data (censored); report honestly if the claim is not supported |

