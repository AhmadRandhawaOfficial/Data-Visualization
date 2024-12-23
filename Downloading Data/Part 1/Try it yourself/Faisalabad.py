import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('fsd_weather_24.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lows, highs, dates = [], [], []
    for row in reader:
        lows.append(float(row[3]))
        highs.append(float(row[2]))
        date = datetime.strptime(row[1], '%Y-%m-%d')
        dates.append(date)

    # Add Visualization.
    fig = plt.figure(dpi=96, figsize=(14.23, 8))
    plt.plot(dates, lows, c='blue', label='lows')
    plt.plot(dates, highs, c='red', label='highs')
    plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

    plt.title("Daily high-low temperature of Faisalabad 2024", fontsize=24)
    plt.xlabel("Dates", fontsize=14)
    plt.ylabel("Temperature (F)", fontsize=14)
    fig.autofmt_xdate()

    plt.show()

