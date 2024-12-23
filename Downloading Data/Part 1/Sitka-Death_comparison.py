import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Parsing Sitka data
dates_s, highs_s, lows_s = [], [], []
with open('sitka_weather_14.csv') as s:
    reader = csv.reader(s)
    header_row = next(reader)

    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print(f"Missing or invalid data in Sitka row: {row}")
        else:
            dates_s.append(date)
            highs_s.append(high)
            lows_s.append(low)

# Parsing Death Valley data
dates_d, highs_d, lows_d = [], [], []
with open('death_valley_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing or invalid data in Death Valley row: {row}")
        else:
            dates_d.append(date)
            highs_d.append(high)
            lows_d.append(low)

# Plotting Sitka and Death Valley data
fig, ax = plt.subplots(dpi=96, figsize=(14.23, 8))

# Sitka data
ax.plot(dates_s, highs_s, c='blue', alpha=0.5, label='Sitka Highs')
ax.plot(dates_s, lows_s, c='blue', alpha=0.3, label='Sitka Lows')
ax.fill_between(dates_s, lows_s, highs_s, facecolor='blue', alpha=0.1)

# Death Valley data
ax.plot(dates_d, highs_d, c='red', alpha=0.5, label='Death Valley Highs')
ax.plot(dates_d, lows_d, c='red', alpha=0.3, label='Death Valley Lows')
ax.fill_between(dates_d, lows_d, highs_d, facecolor='red', alpha=0.1)

# Customizing the plot
ax.set_title("Daily High and Low Temperatures\nSitka vs Death Valley - 2014", fontsize=24)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.legend()

fig.autofmt_xdate()
plt.show()
