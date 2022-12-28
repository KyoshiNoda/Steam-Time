import steam_query


class User:
    def __init__ (self, steam_name, api_key='69165F7C2940B1D23B6A67783A944BAB'):
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
    user1 = User("Dilian1")
    print(user1.get_steam_id())

if __name__ == '__main__':
    test()