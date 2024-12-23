import pygal
from pygal.style import Style
from die import Die

custom_style = Style(
    title_font_size=30,
    x_title_font_size=14,
    y_title_font_size=14,
    label_font_size=14,
    major_label_font_size=18
)

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(8)

# Make some rolls and store result in a list.
results = []
for i in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for i in range(1, max_results + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

hist = pygal.Bar(style=custom_style, show_y_guides=False, show_legend=True, legend_at_bottom=True)

hist.title = "Result of rolling two D6 and one D8 1000 times"
hist.x_labels = [i for i in range(1, max_results+1)]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add('2D6 + D8', frequencies)
hist.render_to_file('die_visual.svg')
