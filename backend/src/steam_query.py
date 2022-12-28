import requests
import json
import user

    
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
    return response_data['response']['steamid']

def get_profile(steam_id, api_key):
    """
    Returns the steam summary of a player
    """
    response_data = query("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", steam_id, api_key)
    return list(response_data['response']['players'][0].values())


def get_app_img_url(app_id, steam_id, api_key):
    """
    Returns the image url of a steam application
    """
    response_data = query("http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/", steam_id, api_key)
    for i in range(len(response_data['response']['games'])):
        if response_data['response']['games'][i]['appid'] == app_id:
            return f'http://media.steampowered.com/steamcommunity/public/images/apps/{app_id}/' + response_data['response']['games'][i]['img_icon_url'] + ".jpg"

def query (url, steam_id, api_key):
    if url.split("/")[4] in ("GetPlayerSummaries"):
        return json.loads(requests.get(f'{url}?key={api_key}&steamids={steam_id}').text)
    return json.loads(requests.get(f'{url}?key={api_key}&steamid={steam_id}').text)
    


def test():
    api_key = '69165F7C2940B1D23B6A67783A944BAB'
    steam_id = get_steamid_from_name("Dilian1", api_key)

    #TEST: AppID -> Name
    print(appid_to_name_converter(714010))

    #TEST: Get Owned Games of Player
    print(get_owned_games(steam_id, api_key))

    #TEST: Get total playtime of a game
    print(get_total_playtime(824270, steam_id, api_key))

    #TEST: Get SteamID from username
    print(get_steamid_from_name("Dilian1", api_key))

    #TEST: Get Steam profile from SteamID
    print(get_profile(steam_id, api_key))

    #TEST: Get the image url from an appID
    print(get_app_img_url(1938090, steam_id, api_key))

    #TEST: Test query() function
    print(query("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", steam_id, api_key))


if __name__ == '__main__':
    test()
    
