import matplotlib.pyplot as plt
from random_w import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.figure(dpi=96, figsize=(14.23, 8.0))
    num_points = list(range(rw.num_points))

    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.plot(0, 0, c='green', marker='o', markersize=10)  # Overwriting the first point.
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', marker='o', markersize=10)  # Overwriting the last point.

    # Removing the axes.
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break
