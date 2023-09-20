# 透過 MongoDB 的 $currentDate 運算子取得伺服器時間，
# 但需注意 $currentDate 不可用於新增資料指令中 (只能用於更新資料指令)，
# 所以要藉由 upsert 參數實現新增資料功能。

import pymongo

client = pymongo.MongoClient()

db = client.test

db.member.drop()

# 因 $type 預設為 date 故「"signUpDate": {"$type": "date"}」可以改為「"signUpDate": True」

# 若希望所存的日期是 Timestamp 型態時可將「"signUpDate": {"$type": "date"}」改為「"signUpDate": {"$type": "timestamp"}」

db.member.update_one(
    {
        "_id": "Tom"
    },
    {
        "$currentDate": {
            "signUpDate": {"$type": "date"}
        }
    },
    upsert=True
)
