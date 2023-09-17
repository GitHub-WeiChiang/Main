import pymongo
import pprint

client = pymongo.MongoClient()
db = client.test

cursor = db.course.find({"courseList.title": "電子學"})
pprint.pprint(list(cursor))

# Projection 投影操作: {"student": 1, "courseList.$": 1}
# 解釋:
# 指定了在查詢結果中要返回的字段，
# 要求返回 "student" 字段和 "courseList" 陣列中滿足查詢條件的元素，
# 這裡的 "courseList.$" 是一個特殊的表示法，
# 表示只返回符合查詢條件的 "courseList" 陣列中的元素，而不是整個陣列。
cursor = db.course.find({"courseList.title": "電子學"}, {"student": 1, "courseList.$": 1})
pprint.pprint(list(cursor))
