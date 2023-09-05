import pymongo

client = pymongo.MongoClient()
db = client.opendata
db_test = client.test

# # 修改資料
# # 修改 SiteName 為淡水的 AQI 值
# db.AQI.update_one(
#     {"SiteName": "淡水"}, {"$set": {"AQI": "10"}}
# )
# # 修改 SiteName 為淡水的 AQI 與 Status 欄位值
# db.AQI.update_one(
#     {"SiteName": "淡水"},  {"$set": {"AQI": "60", "Status": "普通"}}
# )
# # 查看修改是否成功並顯示修改了幾筆資料
# result = db.AQI.update_many({"County": "新北市"}, {"$set": {"AQI": "10"}})
# if result.acknowledged:
#     print("update {} documents".format(result.modified_count))
#
# # 找不到修改對象就新增
# # 在 AQI 資料表中修改一比 County 為臺中市且 SiteName 為我的家的這筆資料，
# # 如果沒有這筆資料則透過 upsert 參數設定直接新增
# db.AQI.update_one(
#     {
#         "County": "臺中市",
#         "SiteName": "我的家"
#     },
#     {
#         "$set": {
#             "AQI": "10",
#             "Status": "良好"
#         }
#     },
#     upsert=True
# )
#
# # 新增與移除欄位
# # 新增
# db.AQI.update_one(
#     {
#         "County": "臺中市",
#         "SiteName": "我的家"
#     },
#     {
#         "$set": {
#             "Longitude": "120",
#             "Latitude": "24"
#         }
#     }
# )
# # 移除
# db.AQI.update_one(
#     {
#         "County": "臺中市",
#         "SiteName": "我的家"
#     },
#     {
#         "$unset": {
#             "Longitude": "",
#             "Latitude": ""
#         }
#     }
# )
