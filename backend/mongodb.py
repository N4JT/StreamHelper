from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient('mongodb+srv://test:randomPassword@twitchkickdatabase.zt1iver.mongodb.net/')
    print(client)
    db = client['users']
    collection = db['User']
    return collection

