import pprint
import pymongo

from datetime import *

# 本地時間 (台灣為例: UTC + 8)
local_time = datetime.now()
# UTC 時間
utc_time = datetime.utcnow()

# 2023-09-18 19:11:02.412960
print(local_time)
# 2023-09-18 11:11:02.412965
print(utc_time)

# MongoDB 儲存的日期不包含時區資訊，
# 若 Python 中的日期包含時區資訊，
# 儲存到 MongoDB 後會被自動轉成 UTC 時區。

# Python 的 now() 所回傳的本地時間並不包含時區，
# 也就是說其預設是 UTC 時區。

# 時區資訊 (以台灣為例)
tz = timezone(timedelta(hours=8))

# 本地時間
local_time = datetime.now()
# 本地時間 + 時區訊息
tz_time = datetime.now(tz)

# 兩者 "時間相同" 但 "時區不同"
# 2023-09-18 19:19:13.454403
print(local_time)
# 2023-09-18 19:19:13.454404+08:00
print(tz_time)

# --------------------------------------------------

client = pymongo.MongoClient()
db = client.test

db.test.drop()

# 把 "時間相同" 但 "時區不同" 的資料儲存至資料庫，
# local_time 預設是 UTC 時區，不會被改動，
# tz_time 被自動轉換成 UTC 時區，也就是自動減去 8 小時。
db.test.insert_one({"local_time": local_time})
db.test.insert_one({"tz_time": tz_time})

cursor = db.test.find({}, {"_id": 0})
pprint.pprint(list(cursor))

# 改善方法:
# 儲存至 MondoDB 前將所有日期都轉換成 UTC 時區，
# 同時額外增加欄位儲存時區資訊。
db.test.insert_one({"local_time": local_time, "tz": local_time.tzname()})
db.test.insert_one({"tz_time": tz_time, "tz": tz_time.tzname()})

cursor = db.test.find({}, {"_id": 0})
pprint.pprint(list(cursor))
