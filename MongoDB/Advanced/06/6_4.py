import pymongo

from datetime import datetime

client = pymongo.MongoClient()

db = client.test

db.product.drop()

db.product.insert_one({"price": 100, "date":  datetime(2021, 1, 5, 0, 0, 0)})
db.product.insert_one({"price": 200, "date":  datetime(2021, 2, 5, 0, 0, 0)})
db.product.insert_one({"price": 200, "date":  datetime(2021, 3, 5, 0, 0, 0)})
db.product.insert_one({"price": 600, "date":  datetime(2021, 7, 5, 0, 0, 0)})
db.product.insert_one({"price": 200, "date":  datetime(2021, 9, 5, 0, 0, 0)})
db.product.insert_one({"price": 400, "date":  datetime(2021, 11, 5, 0, 0, 0)})
