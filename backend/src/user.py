import steam_query
from secret_settings import API_KEY


class User:
    def __init__ (self, email, steam_name, api_key=API_KEY):
        self.email = email
        self.steam_name = steam_name
        self.api_key = api_key
        self.steam_id = steam_query.get_steamid_from_name(steam_name, api_key)

    def get_steam_name (self):
        return self.steam_name

    def get_api_key (self):
        return self.api_key

    def get_steam_id (self):
        return self.steam_id

def test():
    user1 = User("test@example.com", "Dilian1")
    print(user1.get_steam_id())

if __name__ == '__main__':
    test()