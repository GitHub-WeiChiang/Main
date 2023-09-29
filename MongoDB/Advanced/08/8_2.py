import pymongo

client = pymongo.MongoClient()

db = client.test

db.member.drop()

db.member.insert_one({"name": "Karina"})

db.member.create_index([("name", 1)])
