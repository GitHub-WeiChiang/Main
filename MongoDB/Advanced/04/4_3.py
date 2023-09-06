import pymongo

from pprint import *

client = pymongo.MongoClient()
db = client.opendata

pipeline = [
    {
        '$addFields': {
            'iAQI': {
                '$toInt': '$AQI'
            }
        }
    }
]

cursor = db.AQI.aggregate(pipeline)
pprint(list(cursor))
