from pymongo import MongoClient
from dateutil import parser
from pandas import DataFrame
from secret_settings import MONGO_DB_CONNECTION_STRING

def get_database():

    client = MongoClient(MONGO_DB_CONNECTION_STRING)

    return client['user_shopping_list']

def main():
    dbname = get_database()
    collection_name = dbname["user_1_items"]
    
    # item_1 = {
    # "_id" : "U1IT00001",
    # "item_name" : "Blender",
    # "max_discount" : "10%",
    # "batch_number" : "RR450020FRG",
    # "price" : 340,
    # "category" : "kitchen appliance"
    # }

    # item_2 = {
    # "_id" : "U1IT00002",
    # "item_name" : "Egg",
    # "category" : "food",
    # "quantity" : 12,
    # "price" : 36,
    # "item_description" : "brown country eggs"
    # }

    # collection_name.insert_many([item_1, item_2])

    # expiry_date = '2021-07-13T00:00:00.000Z'
    # expiry = parser.parse(expiry_date)

    # item_3 = {
    #     "item_name" : "Bread",
    #     "quantity" : 2,
    #     "ingredients" : "all-purpose flour",
    #     "expiry_date" : expiry
    # }

    # collection_name.insert_one(item_3)

    item_details = collection_name.find()
    for item in item_details:
        items_df = DataFrame(item_details)
        print(items_df)

    item_details = collection_name.find({"category" : "food"})
    print(item_details)

    category_index = collection_name.create_index("category")
    print(category_index)
    

if __name__ == "__main__":
    main()