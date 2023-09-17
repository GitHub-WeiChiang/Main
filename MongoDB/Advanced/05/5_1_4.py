import pymongo
import pprint

client = pymongo.MongoClient()
db = client.test

# 差集: 兩個集合相減 ($setDifference)
# s1 - s2
cursor = db.set.aggregate([{
    "$project": {
        "result": {
            "$setDifference": ["$s1", "$s2"]
        },
        "_id": 0
    }
}])
pprint.pprint(list(cursor))
# s2 - s1
cursor = db.set.aggregate([{
    "$project": {
        "result": {
            "$setDifference": ["$s2", "$s1"]
        },
        "_id": 0
    }
}])
pprint.pprint(list(cursor))

# 是否相等: 兩個集合中的元素是否一樣 ($setEquals)
cursor = db.set.aggregate([{
    "$project": {
        "result": {
            "$setEquals": ["$s3", "$s4"]
        },
        "_id": 0
    }
}])
pprint.pprint(list(cursor))

# 是否為子集合: 某集合中的元素是否全部存在於另一個集合 ($setIsSubset)
# s3 是否為 s1 的子集合
cursor = db.set.aggregate([{
    "$project": {
        "result": {
            "$setIsSubset": ["$s3", "$s1"]
        },
        "_id": 0
    }
}])
pprint.pprint(list(cursor))

# 交集: 傳回兩個集合中都有的元素 ($setIntersection)
cursor = db.set.aggregate([{
    "$project": {
        "result": {
            "$setIntersection": ["$s2", "$s3"]
        },
        "_id": 0
    }
}])
pprint.pprint(list(cursor))

# 聯集: 傳回兩個集合相加後的結果 (去重)($setUnion)。
cursor = db.set.aggregate([{
    "$project": {
        "result": {
            "$setUnion": ["$s1", "$s2"]
        },
        "_id": 0
    }
}])
pprint.pprint(list(cursor))
