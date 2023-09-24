import pymongo
import pprint

client = pymongo.MongoClient()

db = client.test

cursor = db.taiwan.find(
    {
        "geometry": {
            # 此運算子僅支援 Polygon 與 MultiPolygon 型態
            "$geoWithin": {
                "$geometry": {
                    "coordinates": [
                        [
                            [
                                120.82906600165273,
                                25.441831200418775
                            ],
                            [
                                120.82906600165273,
                                24.604512235502085
                            ],
                            [
                                122.10533665976197,
                                24.604512235502085
                            ],
                            [
                                122.10533665976197,
                                25.441831200418775
                            ],
                            [
                                120.82906600165273,
                                25.441831200418775
                            ]
                        ]
                    ],
                    "type": "Polygon"
                }
            }
        }
    },
    {
        "County": 1,
        "_id": 0
    }
)

pprint.pprint(list(cursor))
