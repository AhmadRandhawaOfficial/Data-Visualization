import pygal
from random_w import RandomWalk

rw = RandomWalk()
rw.fill_walk()

hist = pygal.XY()
hist.title = "Random Walk Visualization"
hist.x_title = "X-Position"
hist.y_title = "Y-Position"

walk_data = list(zip(rw.x_values, rw.y_values))
hist.add('', walk_data)

hist.render_to_file('random_w_visual.svg')
