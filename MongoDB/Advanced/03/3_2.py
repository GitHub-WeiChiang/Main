import pymongo
import pprint

client = pymongo.MongoClient()
db = client.opendata

# 函數 find() 會回傳一個 Cursor 類別的實例，
# 可以透過 list() 方法將其轉型為陣列。
for doc in db.AQI.find():
    pprint.pprint('{County}{SiteName}: {AQI}'.format(**doc))

# 取得第一筆資料
first_doc = db.AQI.find()[0]
pprint.pprint('{County}{SiteName}: {AQI}'.format(**first_doc))

# 將 Cursor 類別實例轉型為陣列並取得最後三筆資料
for doc in list(db.AQI.find())[-3:]:
    pprint.pprint('{County}{SiteName}: {AQI}'.format(**doc))

# 只查詢一筆資料
info = db.AQI.find_one()
if info is None:
    print("no document found !")
else:
    pprint.pprint('{County}{SiteName}: {AQI}'.format(**info))

# 顯示特定欄位
# projection 參數:
# 若 value 為 1 表示該欄位要顯示，為 0 表示該欄位不顯示。
# 除 "_id" 欄位外，其它欄位 1 與 0 為互斥設定，亦即只可全部為 0 或 1，不可混合共存 (僅可列出要或不要顯示的欄位)。
# 第一個參數若為空字典，表示沒有搜尋條件，要查詢所有資料。
# 可以透過 True 與 False 表示 1 與 0。
cursor = db.AQI.find({}, projection={"County": 1, "SiteName": 1, "AQI": 1, "_id": 0})
pprint.pprint(list(cursor))
