import requests
import json

api_key = "69165F7C2940B1D23B6A67783A944BAB"
steam_id = "76561198871279330"

# response = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steamid}&format=json')
# response_data = json.loads(requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steamid}&format=json').text)
# # print(response_data['response']['games'][0])
# # print(response_data)
# for i in range(len(response_data['response']['games'])):
#     if response_data['response']['games'][i]['appid'] == 550:
#         print(response_data['response']['games'][i]['playtime_forever'])

# app_list = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2")
# app_list_data = json.loads(requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2").text)
# for i in range(len(app_list_data['applist']['apps'])):
#     if app_list_data['applist']['apps'][i]['appid'] == 1648300:
#         print(app_list_data['applist']['apps'][i]['name'])
#         break
# print(app_list_data['applist']['apps'][0]['appid'])

result = json.loads(requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json').text)
print(result)