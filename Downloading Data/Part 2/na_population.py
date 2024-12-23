from pygal_maps_world.maps import World

wm = World()
wm.title = "Population of countries in North America."
wm.add("North America", {"ca": 39538223, 'us': 346174404, 'mx': 131299502})
wm.render_to_file("na_population.svg")
