import matplotlib.pyplot as plt

values = range(1, 5001)
cubes = [i ** 3 for i in values]
plt.scatter(values, cubes, c=cubes, cmap=plt.cm.Blues)

plt.title("The cube-points of 1st '5000' numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
# plt.ticklabel_format(style='plain', axis='y')  # Force plain formatting on the y-axis instead of scientific.

plt.show()
