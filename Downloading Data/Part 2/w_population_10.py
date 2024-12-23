import json
from country_code import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

with open('population_data.json') as f:
    pop_data = json.load(f)

    # Build a dictionary of population data.
    cc_population = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_population[code] = population
            else:
                print(f"Error: \"{country_name}\"")

    # Group the countries into population levels.
    cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
    for cc, pop in cc_population.items():
        if pop < 10000000:
            cc_pop_1[cc] = pop
        elif pop < 100000000:
            cc_pop_2[cc] = pop
        else:
            cc_pop_3[cc] = pop

    print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = "World Population in 2010, by Country."
wm.add('0-10M', cc_pop_1)
wm.add('10M-100M', cc_pop_2)
wm.add('> 100M', cc_pop_3)

wm.render_to_file('w_population_10.svg')
