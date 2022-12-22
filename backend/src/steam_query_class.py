import requests
import json

class Steam_WebAPI_Query:
    def __init__ (self, steam_id, api_key='69165F7C2940B1D23B6A67783A944BAB'):
        self.steam_id = steam_id
        self.api_key = api_key
    
    def get_owned_games(self):
        return self.query("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/")

    def get_total_playtime(self, appid):
        response_data = self.query("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/")
        for i in range(len(response_data['response']['games'])):
            if response_data['response']['games'][i]['appid'] == appid:
                return response_data['response']['games'][i]['playtime_forever']

    def appid_converter(self, appid):
        response_data = self.query("https://api.steampowered.com/ISteamApps/GetAppList/v2")
        for i in range(len(response_data['applist']['apps'])):
            if response_data['applist']['apps'][i]['appid'] == appid:
                return response_data['applist']['apps'][i]['name']

    def name_to_steamid_converter(self, name):
        response_data = json.loads(requests.get(f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={self.api_key}&vanityurl={name}').text)
        return list(response_data['response'].values())

    def get_profile(self):
        response_data = self.query("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/")
        return list(response_data['response']['players'][0].values())

    def query (self, url):
        if url.split("/")[4] in ("GetPlayerSummaries"):
            return json.loads(requests.get(f'{url}?key={self.api_key}&steamids={self.steam_id}').text)
        return json.loads(requests.get(f'{url}?key={self.api_key}&steamid={self.steam_id}').text)
        
    def get_app_img_url(self, appid):
        response_data = self.query("http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/")
        for i in range(len(response_data['response']['games'])):
            if response_data['response']['games'][i]['appid'] == appid:
                return f'http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/' + response_data['response']['games'][i]['img_icon_url'] + ".jpg"



def test():
    query = Steam_WebAPI_Query('76561198871279330')
    # print(query.get_owned_games())
    # print(query.get_total_playtime(824270))
    print(query.appid_converter(714010))
    # print(query.name_to_steamid_converter("Dilian1"))
    # print(query.get_profile())
    # print(query.query("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"))
    # print(query.get_app_img_url(1938090))

if __name__ == '__main__':
    test()
    
