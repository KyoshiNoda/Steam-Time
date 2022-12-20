import requests
import json

api_key = "69165F7C2940B1D23B6A67783A944BAB"
steamid = "76561198871279330"

response = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steamid}&format=json')
response_dict = json.loads(response.text)
print(response_dict)


# print(response.text)