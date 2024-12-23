import matplotlib.pyplot as plt
from random_w import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(dpi=96, figsize=(14.23, 8.0))
    num_points = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=num_points, cmap=plt.cm.Blues, edgecolors='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)  # Overwriting the first point.
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)  # Overwriting the last point.

    # Removing the axes.
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break
