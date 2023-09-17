import pymongo
import pprint

client = pymongo.MongoClient()
db = client.test

# 同時修物理與音樂欣賞的學生: 使用 $all 運算子
cursor = db.course.find({"courseList": {"$all": ["音樂欣賞", "物理"]}})
pprint.pprint(list(cursor))

# 同時修物理與音樂欣賞的學生: 使用 $and 運算子
cursor = db.course.find(
    {
        "$and": [
            {"courseList": "物理"},
            {"courseList": "音樂欣賞"}
        ]
    }
)
pprint.pprint(list(cursor))

# 僅需修物理或音樂欣賞的學生: 使用 $or 運算子
cursor = db.course.find(
    {
        "$or": [
            {"courseList": "物理"},
            {"courseList": "音樂欣賞"}
        ]
    }
)
pprint.pprint(list(cursor))
