import pymongo

client = pymongo.MongoClient()

db = client.test

db.member.drop()

db.member.insert_one({"name": "Karina"})

# 建立名為 "name" 的索引 (Index) 在 "member" 集合上，
# 索引是一種用來提高查詢效能的資料結構，
# 此處建立了一個升序 (1 表示升序，-1 表示降序) 的索引，
# 以便在 "name" 字段上進行快速查詢。
db.member.create_index([("name", 1)])
