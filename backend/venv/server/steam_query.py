import requests
import json

class Steam_Query:
    # Returns a string format of json objects
    def steam_request_get_owned_games(self, api_key, steam_id):
        return requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json').text

    def appid_converter(self, appid):
        return 0