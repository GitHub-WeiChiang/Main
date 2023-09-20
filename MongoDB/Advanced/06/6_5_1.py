import pymongo

from datetime import *

# 可以直接儲存至資料庫後透過 MongoDB 的日期函數 $toDate 轉換
date_str = "2022/3/1 13:20:0"
# 沒有加上時區符號
formatter = "%Y/%m/%d %H:%M:%S"

client = pymongo.MongoClient()

db = client.test

# 也可以先用 Python 的函數預先轉換
d = datetime.strptime(date_str, formatter)
db.test.insert_one({"date": d})

# 加上時區符號
d_1 = datetime.strptime("2022/3/1 13:20:0+0800", "%Y/%m/%d %H:%M:%S%z")
d_2 = datetime.strptime("2022/3/1 13:20:0CST", "%Y/%m/%d %H:%M:%S%Z")
