import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

# A: list of dates
dates = pd.date_range("2025-11-01", "2026-10-31")

# B: Calendar table(date, day of week), remove the closed day
df = pd.DataFrame({"date": dates, "day_of_week": dates.day_name()})
df = df[df["day_of_week"] != "Monday"]
df = df.reset_index(drop=True)
print(df)

# C: fake weather per day (tempature, rain)

# D: menu items and their normal daily sales

# E: generate sales for every day x every item

# F: save to CSV files
