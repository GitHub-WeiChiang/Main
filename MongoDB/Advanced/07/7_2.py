import pymongo
import pprint

client = pymongo.MongoClient()

db = client.test

cursor = db.taiwan.find_one(
    {
        "geometry": {
            # 用於找出哪個範圍的資料包含了所給的做標點
            "$geoIntersects": {
                # 要搜尋的座標資料
                "$geometry": {
                    # 透過點座標搜尋
                    "type": "Point",
                    # 以新竹市立動物園為例
                    "coordinates": [120.97993, 24.79998]
                }
            }
        }
    },
    {
        "County": 1,
        "_id": 0
    }
)

pprint.pprint(cursor)


cursor = db.taiwan.find(
    {
        "geometry": {
            # 用於找出哪個範圍的資料包含了所給的做標點
            "$geoIntersects": {
                # 要搜尋的座標資料
                "$geometry": {
                    "coordinates": [
                        [
                            [
                                121.51325797531257,
                                25.023078838658336
                            ],
                            [
                                121.51325797531257,
                                25.017826090305462
                            ],
                            [
                                121.5201686698191,
                                25.017826090305462
                            ],
                            [
                                121.5201686698191,
                                25.023078838658336
                            ],
                            [
                                121.51325797531257,
                                25.023078838658336
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
