import pymongo
import pprint

client = pymongo.MongoClient()
db = client.test

cursor = db.course.find({"courseList": "機率"})
pprint.pprint(list(cursor))
