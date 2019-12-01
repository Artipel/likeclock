import requests

def get_data():
    r = requests.request('GET', 'https://www.instagram.com/web/search/topsearch/?query=theflipdots')
    print(r.json()['users'][0]['user']['follower_count'])
