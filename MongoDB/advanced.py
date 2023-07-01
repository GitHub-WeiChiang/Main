import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/?authMechanism=DEFAULT")

    # 创建一个数据库:
    # 数据库只有在内容插入后才会创建，
    # 亦即数据库创建后要创建集合 (数据表) 并插入一个文档 (记录)，
    # 数据库才会真正创建。
    db = client["mongo_db"]

    # # 判断数据库是否已存在
    # if "mongo_db" in client.list_database_names():
    #     print("数据库已存在 !")
    # else:
    #     print("数据库不存在 !")

    # 创建一个集合
    collection = db["collection"]

    # # 判断集合是否已存在
    # if "collection" in db.list_collection_names():
    #     print("集合已存在 !")
    # else:
    #     print("集合不存在 !")

    # # 插入集合並返回 "_id" 字段
    # data = {"name": "Albert", "age": "26"}
    # print(collection.insert_one(data).inserted_id)

    # # 插入指定 "_id" 的多个文档
    # data_list = [
    #     {"_id": 1, "name": "Albert1", "age": "26"},
    #     {"_id": 2, "name": "Albert2", "age": "26"},
    #     {"_id": 3, "name": "Albert3", "age": "26"},
    # ]
    # print(collection.insert_many(data_list).inserted_ids)

    # # 查询集合中所有数据
    # for data in collection.find():
    #     print(data)

    # # 查询指定字段的数据
    # for x in collection.find({}, {"_id": 0, "name": 1, "age": 1}):
    #     print(x)

    # # 根据指定条件查询
    # for x in collection.find({"_id": 1}):
    #     print(x)

    # # 返回指定条数记录
    # for x in collection.find({}).limit(1):
    #     print(x)

    # # 修改文档
    # collection.update_many({"_id": 1}, {"$set": {"name": "Wei"}})
    # print(collection.find_one({"_id": 1}))

    # # 排序
    # for data in collection.find().sort("name"):
    #     print(data)
    # for data in collection.find().sort("name", -1):
    #     print(data)

    # # 删除数据
    # collection.delete_one({"_id": 1})
    # for data in collection.find():
    #     print(data)
    #
    # collection.delete_many({"_id": {"$gt": 1}})
    # for data in collection.find():
    #     print(data)

    # # 删除集合中的所有文档
    # collection.delete_many({})

    # # 删除集合
    # collection.drop()
    # if "collection" in db.list_collection_names():
    #     print("集合已存在 !")
    # else:
    #     print("集合不存在 !")
