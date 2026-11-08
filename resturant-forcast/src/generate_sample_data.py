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
print(df["rained"].mean())
print(df["rained"].sum())
# D: menu items and their normal daily sales

# E: generate sales for every day x every item

# F: save to CSV files
