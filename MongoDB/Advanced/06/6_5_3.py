import pymongo
import time

# 導入 MongoDB BSON (Binary JSON) 庫中的 Timestamp 類別，
# 用於表示 MongoDB 中的時間戳 (timestamp)。
from bson.timestamp import Timestamp

client = pymongo.MongoClient()
db = client.test

# 使用 time 模組的 time() 函數獲取當前的 Unix 時間戳 (以秒為單位)，
# 後將其轉換為整數型別以便存儲在 timestamp 變數中。
timestamp = int(time.time())

# 插入一個新文件 (包含一個鍵值對)，
# 其中鍵為 ts，值是一個 MongoDB 的 Timestamp 物件，
# 物件的時間戳是剛剛獲取的 Unix 時間戳，且時間戳的增量值設置為 1。
db.test.insert_one({"ts": Timestamp(timestamp, 1)})

# --------------------------------------------------

# 取得一個 Timestamp 物件後轉成 Python 可處理型態的方法

doc = db.test.find_one()

# 轉換成 datetime 類別
date = doc["ts"].as_datetime()
print(date)
# 轉換成常見的 timestamp
timestamp = doc["ts"].time
print(timestamp)
# 轉換成 BSON Timestamp 物件中的第二個參數值 (时间戳增量)
inc = doc["ts"].inc
print(inc)
