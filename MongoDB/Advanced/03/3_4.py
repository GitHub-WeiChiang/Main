import pymongo

client = pymongo.MongoClient()
db = client.opendata

# # 刪除資料
# # 將欄位 SiteName 為我的家的一筆資料刪除
# db.AQI.delete_one({"SiteName": "我的家"})
# # 查看刪除的狀態
# result = db.AQI.delete_many({"County": "新北市"})
# if result.acknowledged:
#     print("delete {} documents".format(result.deleted_count))
