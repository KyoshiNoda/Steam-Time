import hash
from pymongo import MongoClient
from pandas import DataFrame
from secret_settings import MONGO_DB_CONNECTION_STRING, MONGO_DB_DATABASE, MONGO_DB_COLLECTION, API_KEY

def get_database(database_name):
    client = MongoClient(MONGO_DB_CONNECTION_STRING)
    return client[database_name]

def create_account(email, steam_name, password, api_key):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]

    item = {
        "email" : email,
        "steam_name" : steam_name,
        "password" : password,
        "api_key" : api_key,
    }
    collection.insert_one(item)

def get_account(email):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]
    # items_df = DataFrame(collection.find_one({"email": binary.Binary(email_hash)}))
    items_df = DataFrame(collection.find({"email": email}))
    if items_df.empty:
        return None
    return items_df

def get_password_hash(email):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]
    items_df = DataFrame(collection.find({"email": email}))
    if items_df.empty:
        return None
    elif items_df["password"][0] == "":
        return None
    else:
        return items_df["password"][0]

def get_api_key(email):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]
    items_df = DataFrame(collection.find({"email": email}))
    if items_df.empty:
        return None
    elif items_df["api_key"][0] == "":
        return None
    else:
        return items_df["api_key"][0]

def get_steam_name(email):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]
    items_df = DataFrame(collection.find({"email": email}))
    if items_df.empty:
        return None
    elif items_df["steam_name"][0] == "":
        return None
    else:
        return items_df["steam_name"][0]


def main():
    ### Data Already Used, edit data and run

    email = "email@example.com"
    steam_name_hash = hash.hash_string("example_hash")
    password_hash = hash.hash_string("hashed_password")
    api_key_hash = hash.hash_string("239047238")

    # create_account(email, steam_name_hash, password_hash, api_key_hash)
    # print(get_account(email))
    # print(get_password_hash(email))
    # print(get_api_key(email))
    # print(get_steam_name(email))

    print(hash.compare_hash("hashed_password".encode("utf8"), get_password_hash(email)))

if __name__ == "__main__":
    main()