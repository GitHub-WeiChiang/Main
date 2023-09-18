import pprint
import pymongo

client = pymongo.MongoClient()
db = client.test

db.test.drop()

db.test.insert_one({"name": "Karina"})
db.test.insert_one({"name": "Winter"})

# Stage - $set: Adds new fields to documents.
# $set outputs documents that contain all existing fields from the input documents and newly added fields.
# {
#   "createDate": {
#     "$toDate": "$_id"
#   }
# }

pipeline = [
    {
        '$set': {
            'createDate': {
                '$toDate': '$_id'
            }
        }
    }
]

cursor = db.test.aggregate(pipeline)
pprint.pprint(list(cursor))
