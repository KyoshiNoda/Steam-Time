from pymongo import MongoClient
from dateutil import parser
from pandas import DataFrame
import bcrypt
from secret_settings import MONGO_DB_CONNECTION_STRING, MONGO_DB_DATABASE, MONGO_DB_COLLECTION, API_KEY

def get_database(database_name):
    client = MongoClient(MONGO_DB_CONNECTION_STRING)
    return client[database_name]

def create_account(email_hash, steam_name, password_hash, api_key_hash):
    database = get_database(MONGO_DB_DATABASE)
    collection = database[MONGO_DB_COLLECTION]

    item = {
        "email" : email_hash,
        "steam_name" : steam_name,
        "password" : password_hash,
        "api_key" : api_key_hash,
    }

    collection.insert_one(item)

def main():
    ### Data Already Used, edit data and the run
    
    create_account("test@example.com", "Dilian1", "examplepassword", "1")
    create_account("test2@example.com", "Dilian2", "examplepassword2", "1")

if __name__ == "__main__":
    main()