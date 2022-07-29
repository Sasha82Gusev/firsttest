import requests

max_intelligence = 0

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
response = requests.get(url)

for id in range(len(response.json())):
    if response.json()[id]['name'] == 'Thanos' or response.json()[id]['name'] == 'Hulk' or response.json()[id]['name'] == 'Captain America':
        if response.json()[id]['powerstats']['intelligence'] > max_intelligence:
            max_intelligence_name = response.json()[id]['name']


print("Самый умный супергерой это ",max_intelligence_name)