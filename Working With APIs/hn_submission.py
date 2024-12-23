import requests
from operator import itemgetter

# Make an API call and store the response
r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')

submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    submission_r = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link: ", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

