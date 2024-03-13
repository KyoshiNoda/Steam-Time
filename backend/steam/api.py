import requests
import os
from flask import request


def get_player_summary(steam_id, api_key):
    steam_api_url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params = {
        "key": api_key,
        "steamids": steam_id,
        "format": "json"
    }
    response = requests.get(url=steam_api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Failure to get steam id. Error: HTTP {}, {}'.format(response.status_code)


def get_steam_id(url):
    if "/id/" in url:
        parts = url.split("/id/")
        if len(parts) >= 2:
            steamid_response = get_steam_id_api(parts[1][:-1])["response"]
            if steamid_response["success"] == 1:
                return steamid_response["steamid"]
            else:
                return parts[1][:-1]
    else:
        return None


def get_steam_id_api(url):
    steam_api_url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"
    params = {
        "key": os.getenv('API_KEY'),
        "vanityurl": url
    }
    response = requests.get(url=steam_api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Failure to get steam id. Error: HTTP {}, {}'.format(response.status_code)


def get_owned_games():
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    data = request.values
    if "steamid" in data.keys():
        params = {
            "key": os.getenv('API_KEY'),
            "steamid": data['steamid']
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failure to get owned games. Error: HTTP {}'.format(response.status_code)
    else:
        return 'invalid steamid'


def get_recently_played_games():
    url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1"
    data = request.values
    if "steamid" in data.keys():
        params = {
            "key": os.getenv('API_KEY'),
            "steamid": data['steamid']
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failure to get recently played games. Error: HTTP {}'.format(response.status_code)
    else:
        return "invalid steamid"


def get_steam_level():
    url = "https://api.steampowered.com/IPlayerService/GetSteamLevel/v1"
    data = request.values
    if "steamid" in data.keys():
        params = {
            "key": os.getenv('API_KEY'),
            "steamid": data['steamid']
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failure to get steam level games. Error: HTTP {}'.format(response.status_code)
    else:
        return "invalid steamid"
