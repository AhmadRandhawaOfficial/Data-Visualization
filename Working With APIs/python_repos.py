import pygal
import requests
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code', r.status_code)

response_dict = r.json()
print(response_dict.keys())
print(response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"Keys: {len(repo_dict)}")
for key in sorted(repo_dict):
    print(key)

print(f"\nSelected information about first repository.")
print(f"Full name: {repo_dict['full_name']}")
print(f"Description: {repo_dict['description']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Clone URL: {repo_dict['clone_url']}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nFull name: {repo_dict['full_name']}")
    print(f"Description: {repo_dict['description']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Clone URL: {repo_dict['clone_url']}")

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make Visualization.
my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most Starred Python Projects on GitHub"
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')