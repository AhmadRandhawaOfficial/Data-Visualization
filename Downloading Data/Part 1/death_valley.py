import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)

    # Print all rows for debugging (optional)
    for row in reader:
        print(row)
    f.seek(0)

    # Read and print the header row
    header_row = next(reader)
    print(header_row)

    # Print the second row with column indexes
    next_row = next(reader)
    for index, column in enumerate(next_row):
        print(index, column)

    # Initialize lists for highs, lows, and dates
    highs, dates, lows = [], [], []

    # Process each row
    for row in reader:
        try:
            # Parse date and temperature values
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            # Handle rows with missing or invalid data
            print(f"Missing or invalid data in row: {row}")
        else:
            # Add valid data to lists
            dates.append(date)
            highs.append(high)
            lows.append(low)

    # Plot the data
    fig = plt.figure(dpi=96, figsize=(14.23, 8))

    plt.plot(dates, highs, c='red', alpha=0.5, label='Highs')
    plt.plot(dates, lows, c='blue', alpha=0.5, label='Lows')
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Add titles and labels
    plt.title("Daily High and Low Temperatures - 2014\nDeath Valley", fontsize=24)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.legend()

    # Rotate the date labels for better readability
    fig.autofmt_xdate()

    # Display the plot
    plt.show()
