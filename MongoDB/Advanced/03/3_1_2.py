import pymongo

# 負責與 Server 端連線，無帶參數預設為 "localhost:27017"
client = pymongo.MongoClient()
# 選擇 test 資料庫
db = client.test

# 新增一筆資料
result = db["weather"].insert_one({
    'humidity': 68,
    'temperature': 26,
    'date': '2022/3/1 6:0:0'
})

# 判斷結果
if result.acknowledged:
    print("成功:", result.inserted_id)
else:
    print("失敗")

# 新增多筆資料
result = db.weather.insert_many([
 {
    'humidity': 65,
    'temperature': 26,
    'date': '2022/3/1 7:0:0'
  },
  {
    'humidity': 65,
    'temperature': 27,
    'date': '2022/3/1 8:0:0'
  }  
])

# 判斷結果
if result.acknowledged:
    print("成功:", result.inserted_ids)
else:
    print("失敗")

# 關閉連線
client.close()
