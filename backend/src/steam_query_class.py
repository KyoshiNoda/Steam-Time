import requests
import json

class Steam_WebAPI_Query:
    def __init__ (self, steam_name, api_key='69165F7C2940B1D23B6A67783A944BAB'):
        self.steam_name = steam_name
        self.api_key = api_key
        self.steam_id = self.get_steamid_from_name()
    
    def get_owned_games(self):
        """
        Returns the owned games of the player
        """
        return self.query("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/")

    def get_total_playtime(self, appid):
        """
        Returns the total playtime of the player
        """
        response_data = self.query("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/")
        for i in range(len(response_data['response']['games'])):
            if response_data['response']['games'][i]['appid'] == appid:
                return response_data['response']['games'][i]['playtime_forever']

    def appid_to_name_converter(self, appid):
        """
        Returns the steam appid of a game
        """
        response_data = json.loads(requests.get(f'https://store.steampowered.com/api/appdetails/?appids={appid}').text)
        return response_data[f'{appid}']['data']['name']


    def get_steamid_from_name(self):
        """
        Returns the steamid of the object's name
        """
        response_data = json.loads(requests.get(f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={self.api_key}&vanityurl={self.steam_name}').text)
        return response_data['response']['steamid']

    def get_profile(self):
        """
        Returns the steam summary of a player
        """
        response_data = self.query("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/")
        return list(response_data['response']['players'][0].values())

    
    def get_app_img_url(self, appid):
        """
        Returns the image url of a steam application
        """
        response_data = self.query("http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/")
        for i in range(len(response_data['response']['games'])):
            if response_data['response']['games'][i]['appid'] == appid:
                return f'http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/' + response_data['response']['games'][i]['img_icon_url'] + ".jpg"

    def query (self, url):
        if url.split("/")[4] in ("GetPlayerSummaries"):
            return json.loads(requests.get(f'{url}?key={self.api_key}&steamids={self.steam_id}').text)
        return json.loads(requests.get(f'{url}?key={self.api_key}&steamid={self.steam_id}').text)
    


def test():
    query = Steam_WebAPI_Query("Dilian1")
    # print(query.steam_id)
    print(query.appid_to_name_converter(714010))
    # print(query.get_owned_games())
    # print(query.get_total_playtime(824270))
    # print(query.appid_to_name_converter(714010))
    # print(query.name_to_steamid_converter("Dilian1"))
    # print(query.get_profile())
    # print(query.query("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"))
    # print(query.get_app_img_url(1938090))

if __name__ == '__main__':
    test()
    
