import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_14.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.seek(0)

    header_row = next(reader)
    print(header_row)

    next_row = next(reader)
    for index, columns in enumerate(next_row):
        print(index, columns)

    # Get high temperature from file.
    highs, dates, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)
        highs.append(int(row[1]))
        lows.append(int(row[2]))

    # Plot the data.
    fig = plt.figure(dpi=96, figsize=(14.23, 8))

    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.title("Daily high Temperature - 2014 Sitka", fontsize=24)
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize='14')
    fig.autofmt_xdate()

    plt.show()
