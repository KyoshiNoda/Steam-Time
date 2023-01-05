from pymongo import MongoClient
from dateutil import parser
from pandas import DataFrame
import bcrypt
from secret_settings import MONGO_DB_CONNECTION_STRING, MONGO_DB_DATABASE, MONGO_DB_COLLECTION, API_KEY

def get_database(database_name):
    client = MongoClient(MONGO_DB_CONNECTION_STRING)
    return client[database_name]

def create_account(email_hash, steam_name_hash, password_hash, api_key_hash):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]

    item = {
        "email" : email_hash,
        "steam_name" : steam_name_hash,
        "password" : password_hash,
        "api_key" : api_key_hash,
    }
    collection.insert_one(item)

def get_password_hash(email_hash):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]
    items_df = DataFrame(collection.find({"email": email_hash}))
    if items_df.empty:
        return None
    elif items_df["password"][0] == "":
        return None
    else:
        return items_df["password"][0]

def get_api_key(email_hash):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]
    items_df = DataFrame(collection.find({"email": email_hash}))
    if items_df.empty:
        return None
    elif items_df["api_key"][0] == "":
        return None
    else:
        return items_df["api_key"][0]

def get_steam_name(email_hash):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]
    items_df = DataFrame(collection.find({"email": email_hash}))
    if items_df.empty:
        return None
    elif items_df["steam_name"][0] == "":
        return None
    else:
        return items_df["steam_name"][0]


def main():
    ### Data Already Used, edit data and run
    
    # create_account("test1@example.com", "example_name1", "examplepassword1", "1")
    # create_account("test2@example.com", "example_name2", "examplepassword2", "2")
    
    # print(get_password_hash("test1@example.com"))
    # get_password_hash("asfasfd")

if __name__ == "__main__":
    main()