import requests
import json
    
def get_owned_games(steam_id, api_key):
    """
    Returns the owned games of the player
    """
    return query("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/", steam_id, api_key)

def get_total_playtime(app_id, steam_id, api_key):
    """
    Returns the total playtime of the player
    """
    response_data = query("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/", steam_id, api_key)
    for i in range(len(response_data['response']['games'])):
        if response_data['response']['games'][i]['appid'] == app_id:
            return response_data['response']['games'][i]['playtime_forever']

def appid_to_name_converter(app_id):
    """
    Returns the steam appid of a game
    """
    response_data = json.loads(requests.get(f'https://store.steampowered.com/api/appdetails/?appids={app_id}').text)
    return response_data[f'{app_id}']['data']['name']


def get_steamid_from_name(steam_name, api_key):
    """
    Returns the steamid of the object's name
    """
    response_data = json.loads(requests.get(f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={steam_name}').text)
    if response_data['response']['success'] == 1:
        return response_data['response']['steamid']
    return None

def get_profile(steam_id, api_key):
    """
    Returns the steam summary of a player
    """
    response_data = query("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", steam_id, api_key)
    if response_data['response']['players'] == []:
        return None
    return response_data['response']['players'][0]


def get_app_img_url(app_id):
    """
    Returns the image url of a steam application
    """
    response_data = json.loads(requests.get(f'https://store.steampowered.com/api/appdetails/?appids={app_id}').text)
    try:
        if response_data[f'{app_id}']['data']['steam_appid'] == app_id:
            url = response_data[f'{app_id}']['data']['header_image'].split("?")
            return url[0]
    except KeyError:
        return None

def query (url, steam_id, api_key):
    if url.split("/")[4] in ("GetPlayerSummaries"):
        return json.loads(requests.get(f'{url}?key={api_key}&steamids={steam_id}').text)
    return json.loads(requests.get(f'{url}?key={api_key}&steamid={steam_id}').text)