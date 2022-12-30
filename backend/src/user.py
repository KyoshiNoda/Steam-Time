import steam_query
import bcrypt
from secret_settings import API_KEY


class User:
    def __init__ (self, steam_name, api_key='API_KEY'):
        self.steam_name = steam_name
        self.api_key = api_key
        self.steam_id = steam_query.get_steamid_from_name(steam_name, api_key)

    def get_steam_name (self):
        return self.steam_name

    def get_api_key (self):
        return self.api_key

    def get_steam_id (self):
        return self.steam_id

def hash_string(string):
    """
    Returns a salted hash of the string using bcrypt
    """
    return bcrypt.hashpw(string.encode('utf8'), bcrypt.gensalt())

def compare_hash(hash_a, hash_b):
    """
    Compare two hashes and returns the result\n
    Both Hash Strings must be encoded with utf8
    """
    return bcrypt.checkpw(hash_a, hash_b)



def test():
    user1 = User("Dilian1")
    print(user1.get_steam_id())

if __name__ == '__main__':
    test()