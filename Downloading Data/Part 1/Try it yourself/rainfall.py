import matplotlib.pyplot as plt
import csv
from datetime import datetime

with open("fsd_weather_24.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    precip, dates = [], []
    for row in reader:
        precip.append(float(row[10]))
        dates.append(datetime.strptime(row[1], '%Y-%m-%d'))

    fig = plt.figure(dpi=128, figsize=(14.23, 8))
    plt.title("Daily Rainfall data of Fsd-2024", fontsize=24)
    plt.xlabel("Dates", fontsize=14)
    plt.ylabel("Rainfall ", fontsize=14)
    plt.plot(dates, precip)

    plt.show()
