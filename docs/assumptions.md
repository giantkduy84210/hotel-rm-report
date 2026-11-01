# Assumptions and Limitations

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
