import matplotlib.pyplot as plt

start, end = map(int, input("Enter two numbers separated by space(start and end) to define the range: ").split())
values = range(start, end + 1)
power = int(input("Enter the power to which each number should be raised: "))

squares = [i ** power for i in values]
plt.scatter(values, squares, c=squares, cmap=plt.cm.Blues, edgecolors='none', s=25)

# Set chart and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel('Squares', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
