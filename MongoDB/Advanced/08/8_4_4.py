import pymongo

client = pymongo.MongoClient()
db = client.test
db.test.drop()

db.test.insert_many([
    {"_id": "Karina", "score": 100},
    {"_id": "Giselle"},
    {"_id": "Winter", "score": 90},
    {"_id": "Ningning", "score": None}
])

# 創建 "normal" 索引，該索引基於 "score" 欄位的升序排列 (1 表示升序)。
db.test.create_index([("score", 1)], name="normal")
# 創建 "sparse" 稀疏索引，稀疏索引僅包含那些具有索引欄位的文檔，
# 對於缺少索引欄位的文檔不會建立索引，在這種情況下只有具有 "score" 欄位的文檔才會被索引，
# 而缺少 "score" 欄位的文檔將不會被包括在索引中。
db.test.create_index([("score", 1)], name="sparse", sparse=True)

# 定義部分過濾器表達式，用於確定哪些文檔應該包含在索引中，
# 具體來說這個過濾器表示只有那些具有 "score" 欄位的文檔將包含在索引中。
partial_filter = {"score": {"$exists": True}}
# 只有符合過濾器條件的文檔 (具有 "score" 欄位) 才會包含在這個索引中。
db.test.create_index([("score", 1)], name="partial", partialFilterExpression=partial_filter)

# 指定使用 normal 索引: 會顯示所有資料
result = db.test.find().sort("score").hint("normal")
for document in result:
    print(document)

# 分隔線 4 我
print("----------")

# 指定使用 sparse 索引: 僅顯示被放入 sparse 索引中的資料
result = db.test.find().sort("score").hint("sparse")
for document in result:
    print(document)

# 分隔線 4 我
print("----------")

# 指定使用 partial 索引: 僅顯示被放入 sparse 索引中的資料
result = db.test.find().sort("score").hint("partial")
for document in result:
    print(document)
