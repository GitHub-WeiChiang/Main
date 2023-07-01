import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/?authMechanism=DEFAULT")

    all_db = client.list_database_names()
    print(all_db)

    collections = client["admin"]["main"]

    collections.insert_one({
        "name": "Albert",
        "age": 26
    })

    for rec in collections.find():
        print(rec)

    collections.delete_one({
        "name": "Albert"
    })

    for rec in collections.find():
        print(rec)
