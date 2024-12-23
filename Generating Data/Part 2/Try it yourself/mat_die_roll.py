import matplotlib.pyplot as plt
from die import Die

die = Die()

results = []
for i in range(1000):
    results.append(die.roll())

frequencies = []
for i in range(1, die.num_sides + 1):
    frequencies.append(results.count(i))

x_values = list(range(1, die.num_sides + 1))
# Make Visualization.
plt.scatter(x_values, frequencies)
plt.show()
