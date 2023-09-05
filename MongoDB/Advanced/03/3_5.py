import pymongo

client = pymongo.MongoClient()
db = client.opendata

# # 把 SiteName 為淡水的資料換成新的 JSON 格式
# db.AQI.replace_one({"SiteName": "淡水"}, {"weather": "下雨"})
# # 將 SiteName 為日月潭的資料換成水社馬頭 (找不到則新增)
# db.AQI.replace_one(
#     {"SiteName": "日月潭"},
#     {"SiteName": "水社馬頭", "weather": "晴天"},
#     upsert=True
# )
# # 由傳回值得知取代狀態
# result = db.AQI.replace_one({"SiteName": "水社馬頭"}, {"weather": "下雨"})
# if result.acknowledged:
#     print("successful")
