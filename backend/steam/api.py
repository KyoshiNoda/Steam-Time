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
        return None


def get_steam_id(url, api_key):
    if "/id/" in url:
        parts = url.split("/id/")
        if len(parts) >= 2:
            vanity_url = parts[1][:-1]
            steamid_response = get_steam_id_api(
                vanity_url, api_key)['response']
            if "success" in steamid_response:
                return steamid_response["steamid"]
            else:
                return steamid_response
    elif "/profiles/":
        parts = url.split("/profiles/")
        return parts[1]
    else:
        return None


def get_steam_id_api(url, api_key):
    steam_api_url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"
    params = {
        "key": api_key,
        "vanityurl": url
    }
    response = requests.get(url=steam_api_url, params=params)
    if response.status_code == 200:
        json_response = response.json()
        if json_response.get("response", {}).get("message") != "No match":
            return json_response
        else:
            return {'response': {'error': 'Incorrect Steam URL.'}}
    else:
        return {'response': {'error': 'Incorrect API KEY.'}}


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
