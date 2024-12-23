import pygal
import requests
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

r = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars')
response_dicts = r.json()
print(response_dicts.keys())

repo_dicts = response_dicts['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'], 'label': repo_dict['description'], 'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# Make Visualization.
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most starred python projects on Github"
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repo_visual.svg')
