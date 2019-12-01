import requests

r = requests.request('GET', 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCLd5Q9pD22qEndut3uaoglQ&key=AIzaSyBXpfee6eEHPEwmhkGzNBlCIQfF0d5upgQ')
print(r.json()['items'][0]['statistics']['subscriberCount'])