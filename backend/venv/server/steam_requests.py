import requests

api_key = "69165F7C2940B1D23B6A67783A944BAB"
steamid = "76561198871279330"

response = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steamid}&format=json')
print(response.text)