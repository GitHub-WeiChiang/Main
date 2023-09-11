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
    }, {
        '$group': {
            '_id': '$County',
            'averageAQI': {
                '$avg': '$iAQI'
            }
        }
    }, {
        '$project': {
            'averageAQI': {
                '$round': [
                    '$averageAQI', 0
                ]
            }
        }
    }, {
        '$sort': {
            'averageAQI': 1
        }
    }
]

# 使用 Pipeline 讀取 Collection
cursor = db.AQI.aggregate(pipeline)
pprint(list(cursor))

# 讀取 View
cursor = db.vw_average_aqi.find()
pprint(list(cursor))
