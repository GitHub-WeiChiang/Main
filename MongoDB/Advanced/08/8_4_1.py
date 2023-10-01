import pymongo

client = pymongo.MongoClient()

db = client.test

try:
    db.test.insert_one({'email': 'albert0425369@gmail.com'})
except pymongo.errors.DuplicateKeyError as error:
    print(error)
