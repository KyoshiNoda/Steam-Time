import requests
import json

class Steam_WebAPI_Query:
    def __init__ (self, steam_id, api_key='69165F7C2940B1D23B6A67783A944BAB'):
        self.steam_id = steam_id
        self.api_key = api_key
    
    def get_owned_games(self):
        return json.loads(requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={self.steam_id}&format=json').text)

    def get_total_playtime(self, appid):
        response_data = json.loads(requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={self.steam_id}&format=json').text)
        for i in range(len(response_data['response']['games'])):
            if response_data['response']['games'][i]['appid'] == appid:
                return response_data['response']['games'][i]['playtime_forever']

    def appid_converter(self, appid):
        app_list_data = json.loads(requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2").text)
        for i in range(len(app_list_data['applist']['apps'])):
            if app_list_data['applist']['apps'][i]['appid'] == appid:
                return app_list_data['applist']['apps'][i]['name']

    def name_to_steamid_converter(self, name):
        response_data = json.loads(requests.get(f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={self.api_key}&vanityurl={name}').text)
        return response_data['response']['steamid']

def test():
    query = Steam_WebAPI_Query('76561198871279330')
    print(query.get_owned_games())
    print(query.get_total_playtime(824270))
    print(query.appid_converter(1591520))
    print(query.name_to_steamid_converter("Dilian1"))

if __name__ == '__main__':
    test()
    

    