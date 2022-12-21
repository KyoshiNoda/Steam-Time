import requests
import json

api_key = "69165F7C2940B1D23B6A67783A944BAB"
steamid = "76561198871279330"

# response = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steamid}&format=json')
# response_data = json.loads(response.text)
# print(response_data['response']['games'][0])
# print(response_data)

app_list = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2")
app_list_data = json.loads(app_list.text)
# for x in app_list_data['applist']['apps']:
#     if x == 41:
#         print(app_list_data['applist']['apps'][x])
#         break
print(app_list_data['applist']['apps'][41])
