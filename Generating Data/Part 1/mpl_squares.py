import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(values, squares, linewidth=5)

# Set chart and label axis.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squares", fontsize=14)
plt.tick_params(axis='both', labelsize=30)

plt.show()
