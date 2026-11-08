import numpy as np
import pandas as pd

rng = np.random.default_rng(42)


# A: list of dates
dates = pd.date_range("2025-11-01", "2026-10-31")

# B: Calendar table(date, day of week), remove the closed day
df = pd.DataFrame({"date": dates, "day_of_week": dates.day_name()})
df = df[df["day_of_week"] != "Monday"]
df = df.reset_index(drop=True)

# C: fake weather per day (tempature, rain)
avg_temp_by_month = {
    1: 35,
    2: 36,
    3: 45,
    4: 57,
    5: 67,
    6: 79,
    7: 80,
    8: 79,
    9: 72,
    10: 62,
    11: 50,
    12: 38,
}
df["month"] = df["date"].dt.month
df["day_temp_f"] = rng.normal(df["month"].map(avg_temp_by_month), 5).round().astype(int)
df["rained"] = rng.random(size=len(df)) < 0.3

# D: menu items and their normal daily sales
menu = {
    "salmon_roll": 30,
    "spicy_tuna_roll": 25,
    "shrimp_tempura_roll": 23,
    "California Roll": 32,
}

# E: generate sales for every day x every item
day_multiplier = {"Friday": 1.4, "Saturday": 1.6, "Sunday": 1.2}

rows = []
for i, row in df.iterrows():
    for item, base_sale in menu.items():
        multiplier = day_multiplier.get(row["day_of_week"], 1.0)
        rain_multiplier = 0.8 if row["rained"] else 1.0
        expected = multiplier * base_sale * rain_multiplier
        units = max(round(rng.normal(expected, expected * 0.1)), 0)
        rows.append({"date": row["date"], "item": item, "units_sold": units})

sales = pd.DataFrame(rows)


# F: save to CSV files
df = df[["date", "day_temp_f", "rained"]]
print(df)

sales.to_csv("data/sample_sales.csv", index=False)
df.to_csv("data/sample_weather.csv", index=False)
