import hash
from pymongo import MongoClient, errors
from pandas import DataFrame
from secret_settings import MONGO_DB_CONNECTION_STRING, MONGO_DB_DATABASE, MONGO_DB_COLLECTION, API_KEY


def get_database(database_name):
    """
    Returns the database connection
    Returns None if connection fails
    """
    try:
        conn = MongoClient(MONGO_DB_CONNECTION_STRING)
    except errors.ConnectionFailure:
        print("Cannot connect to database!")
        return None
    finally:
        return conn[database_name]

def create_account(email, steam_name, password, api_key):
    """
    Creates a document within Accounts collection of database
    """
    database = get_database(MONGO_DB_DATABASE)
    if database == None:
        print("Cannot connect to database!")
        return 0
    collection = database[MONGO_DB_COLLECTION]

    if get_account(email) != None:
        print("Account already exists!")
        return 0

    collection.insert_one({
            "email" : email,
            "steam_name" : steam_name,
            "password" : password,
            "api_key" : api_key,
        })

def get_account(email):
    database = get_database(MONGO_DB_DATABASE)
    if database == None:
        print("Cannot connect to database!")
        return 0
    collection = database[MONGO_DB_COLLECTION]

    items_df = DataFrame(collection.find({"email": email}))
    if items_df.empty:
        return 0
    return items_df

def get_password_hash(email):
    database = get_database(MONGO_DB_DATABASE)
    if database == None:
        print("Cannot connect to database!")
        return 0
    collection = database[MONGO_DB_COLLECTION]

    items_df = DataFrame(collection.find({"email": email}))
    if items_df.empty:
        return 0
    elif items_df["password"][0] == "":
        return 0
    else:
        return items_df["password"][0]

def get_api_key(email):
    database = get_database(MONGO_DB_DATABASE)
    if database == None:
        print("Cannot connect to database!")
        return 0
    collection = database[MONGO_DB_COLLECTION]

    items_df = DataFrame(collection.find({"email": email}))
    if items_df.empty:
        return 0
    elif items_df["api_key"][0] == "":
        return 0
    else:
        return items_df["api_key"][0]

def get_steam_name(email):
    database = get_database(MONGO_DB_DATABASE)
    if database == None:
        print("Cannot connect to database!")
        return 0
    collection = database[MONGO_DB_COLLECTION]

    items_df = DataFrame(collection.find({"email": email}))
    if items_df.empty:
        return 
    elif items_df["steam_name"][0] == "":
        return 0
    else:
        return items_df["steam_name"][0]

def compare_passwords(email, password):
    if get_password_hash(email) == 0:
        return False
    return hash.compare_hash(password.encode("utf8"), get_password_hash(email))

def change_password(email, new_password):
    database = get_database(MONGO_DB_DATABASE)
    if database == None:
        print("Cannot connect to database!")
        return 0
    collection = database[MONGO_DB_COLLECTION]

    filter = {"email": email}
    new_values = {"$set": {"password": new_password}}
    try:
        collection.update_one(filter, new_values)
    except:
        print("Could not update password")
        return 0
    return 1


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

    change_password(email, "meow")

    # print(hash.compare_hash("hashed_password".encode("utf8"), get_password_hash(email)))

if __name__ == "__main__":
    main()