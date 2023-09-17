import pymongo
import pprint

client = pymongo.MongoClient()
db = client.test

# 目標: 查詢音樂欣賞不及格的學生

# 錯誤做法:
# 查詢陣列內容時，各查詢條件獨立運作，
# 下方代碼會先過濾出含有元素音樂欣賞的資料，
# 再過濾出 score 低於 60 的資料。
cursor = db.course.find(
    {
        "courseList.title": "音樂欣賞",
        "courseList.score": {"$lt": 60}
    }
)
pprint.pprint(list(cursor))

# 正確做法 1: 透過 $elemMatch 運算子綑綁各個查詢條件
cursor = db.course.find({
    "courseList": {
        "$elemMatch": {
            "title": "音樂欣賞",
            "score": {"$lt": 60}
        }
    }
})
pprint.pprint(list(cursor))

# 正確做法 2: 僅列出音樂欣賞課程 (投影操作)
cursor = db.course.find({
    "courseList": {
        "$elemMatch": {
            "title": "音樂欣賞",
            "score": {"$lt": 60}
        }
    },
}, {"student": 1, "courseList.$": 1})
pprint.pprint(list(cursor))
