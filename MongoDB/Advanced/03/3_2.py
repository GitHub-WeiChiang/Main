import pymongo
import pprint

client = pymongo.MongoClient()
db = client.opendata
db_test = client.test

# # 函數 find() 會回傳一個 Cursor 類別的實例，
# # 可以透過 list() 方法將其轉型為陣列。
# for doc in db.AQI.find():
#     pprint.pprint('{County}{SiteName}: {AQI}'.format(**doc))
#
# # 取得第一筆資料
# first_doc = db.AQI.find()[0]
# pprint.pprint('{County}{SiteName}: {AQI}'.format(**first_doc))
#
# # 將 Cursor 類別實例轉型為陣列並取得最後三筆資料
# for doc in list(db.AQI.find())[-3:]:
#     pprint.pprint('{County}{SiteName}: {AQI}'.format(**doc))
#
# # 只查詢一筆資料
# info = db.AQI.find_one()
# if info is None:
#     print("no document found !")
# else:
#     pprint.pprint('{County}{SiteName}: {AQI}'.format(**info))
#
# # 顯示特定欄位
# # projection 參數:
# # 若 value 為 1 表示該欄位要顯示，為 0 表示該欄位不顯示。
# # 除 "_id" 欄位外，其它欄位 1 與 0 為互斥設定，亦即只可全部為 0 或 1，不可混合共存 (僅可列出要或不要顯示的欄位)。
# # 第一個參數若為空字典，表示沒有搜尋條件，要查詢所有資料。
# # 可以透過 True 與 False 表示 1 與 0。
# cursor = db.AQI.find({}, projection={"County": 1, "SiteName": 1, "AQI": 1, "_id": 0})
# pprint.pprint(list(cursor))
#
# # 單一條件查詢
# cursor = db.AQI.find({"SiteName": "淡水"})
# pprint.pprint(list(cursor))
# cursor = db.AQI.find_one({"SiteName": "淡水"})
# pprint.pprint(cursor)
#
# # 多重條件查詢
# # AND
# cursor = db.AQI.find({"County": "新北市", "SiteName": "板橋"})
# pprint.pprint(list(cursor))
# # OR
# cursor = db.AQI.find({
#     "$or": [
#         {"SiteName": "淡水"},
#         {"SiteName": "板橋"}
#     ]
# })
# pprint.pprint(list(cursor))
#
# # 比較運算子
# # 相等
# cursor = db.AQI.find({
#     "SiteName": {"$eq": "板橋"}
# })
# pprint.pprint(list(cursor))
# # 包含
# cursor = db.AQI.find({
#     "SiteName": {"$in": ["板橋", "淡水"]}
# })
# pprint.pprint(list(cursor))
# # 不包含
# cursor = db.AQI.find({
#     "SiteName": {"$nin": ["板橋", "淡水"]}
# })
# pprint.pprint(list(cursor))
#
# # 刪除 Collection
# db.AQI.drop()
#
# # 新增資料
# db_test.weather.drop()
# db_test.weather.insert_many([
#     {"humidity": 50, "temperature": 22},
#     {"humidity": 55, "temperature": 28},
#     {"humidity": 65, "temperature": 19},
# ])
#
# # 查詢溫度低於 20 度的資料
# cursor = db_test.weather.find({
#     "temperature": {"$lt": 20}
# })
# pprint.pprint(list(cursor))
# # 查詢溫度高於 20 度且低於 30 度的資料
# cursor = db_test.weather.find({
#     "temperature": {"$gte": 20, "$lt": 30}
# })
# pprint.pprint(list(cursor))
#
# # 存在運算子 (具有被指定為 True 的那個欄位)
# db.AQI.insert_one({"weather": "晴天"})
# cursor = db.AQI.find({
#     "weather": {"$exists": True}
# })
# pprint.pprint(list(cursor))
#
# # 模糊查詢
# # County 中有北字
# cursor = db.AQI.find({
#     "County": {"$regex": "北"}
# })
# pprint.pprint(list(cursor))
# # County 中第一個字為新字
# cursor = db.AQI.find({
#     "County": {"$regex": "^新"}
# })
# pprint.pprint(list(cursor))
# # County 中最後一個字為縣字
# cursor = db.AQI.find({
#     "County": {"$regex": "縣$"}
# })
# pprint.pprint(list(cursor))
# # AQI 在 15 (含) 以上的所有縣市資料
# cursor = db.AQI.find({
#     "AQI": {"$regex": "1[5-9].|[2-9]."}
# })
# pprint.pprint(list(cursor))
#
# # 運用 where 語句
# # 查詢 AQI 超過 100 的資料
# cursor = db.AQI.find().where("parseInt(this.AQI) > 10")
# pprint.pprint(list(cursor))
# # 查詢 AQI 大於 20 小於 25 的資料
# cursor = db.AQI.find().where("parseInt(this.AQI) > 20 && parseInt(this.AQI) < 25")
# pprint.pprint(list(cursor))
#
# # 查詢結果排序
# # 將 test 資料庫中 weather 資料表的溫度做遞增排序
# cursor = db_test.weather.find().sort("temperature")
# pprint.pprint(list(cursor))
# # 將 test 資料庫中 weather 資料表的溫度做遞減排序
# cursor = db_test.weather.find().sort("temperature", -1)
# pprint.pprint(list(cursor))
# # 將 test 資料庫 weather 資料表中的資料先按照 humidity 遞增排序，再按照 temperature 遞增排序
# cursor = db_test.weather.find().sort("humidity", 1).sort("temperature", 1)
# pprint.pprint(list(cursor))
# # 將 test 資料庫 weather 資料表中的資料先按照 humidity 遞增排序，若相同則按照 temperature 遞增排序
# cursor = db_test.weather.find().sort([
#     ("humidity", 1), ("temperature", 1)
# ])
# pprint.pprint(list(cursor))
#
# # 中文排序
# # 按筆畫排序
# cursor = db.AQI.find(
#     {}, {"SiteName": 1, "_id": 0}
# ).collation({"locale": "zh_Hant"}).sort("SiteName")
# pprint.pprint(list(cursor))
# # 按照注音符號排序
# cursor = db.AQI.find(
#     {}, {"SiteName": 1, "_id": 0}
# ).collation({"locale": "zh@collation=zhuyin"}).sort("SiteName")
# pprint.pprint(list(cursor))
# # 按照拼音排序
# cursor = db.AQI.find(
#     {}, {"SiteName": 1, "_id": 0}
# ).collation({"locale": "zh"}).sort("SiteName")
# pprint.pprint(list(cursor))
#
# # 若覺得每次排序中文都要修改語系很麻煩:
# # 1. 建立特定語系的資料表後再輸入資料
# #     step 1. Create Collection
# #     step 2. Use Custom Collation
# #     step 3. locale: zh_Hant - Chinese (Traditional)
# # 2. 建立特定語系的 View
#
# # 計算查詢筆數
# # 可以設定查詢條件
# n1 = db.AQI.count_documents({"County": "臺北市"})
# # 快速估算整個資料表且無法設定查詢條件
# n2 = db.AQI.estimated_document_count()
# print((n1, n2))
#
# # 去除重複資料
# cursor = db.AQI.distinct("County")
# pprint.pprint(list(cursor))
# # 幫 distinct 加上查詢條件
# cursor = db.AQI.distinct("County", {"County": {"$regex": "北"}})
# pprint.pprint(list(cursor))
#
# # 限制與忽略
# # 只列出一筆資料
# cursor = db.AQI.find(limit=1)
# pprint.pprint(list(cursor))
# # 列出從第三筆開始的連續五筆資料
# cursor = db.AQI.find(skip=2,  limit=5)
# pprint.pprint(list(cursor))
# # 先將資料排序後再取最後兩筆資料
# cursor = db.AQI.find().collation({"locale": "zh_Hant"}).sort("SiteName", -1).limit(2)
# pprint.pprint(list(cursor))
#
# # 查詢子文件
# # 輸入兩筆資料
# db_test.course.drop()
# db_test.course.insert_many([
#     {
#         "student": "S1",
#         "course": {
#             "機率": 80,
#             "音樂欣賞": 70
#         }
#     },
#     {
#         "student": "S2",
#         "course": {
#             "物理": 85,
#             "機率": 70,
#             "音樂欣賞": 50
#         }
#     },
# ])
# # 查詢音樂欣賞課程不及格的學生
# cursor = db_test.course.find(
#     {"course.音樂欣賞": {"$lt": 60}}, {"student": 1, "course.音樂欣賞": 1}
# )
# pprint.pprint(list(cursor))
# # 查詢哪些學生修了物理課程
# cursor = db_test.course.find({"course.物理": {"$exists": True}})
# pprint.pprint(list(cursor))
