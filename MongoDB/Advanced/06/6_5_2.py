import pymongo

from datetime import *

client = pymongo.MongoClient()

db = client.test

doc = db.test.find_one()
date = doc["date"]

# 方法一: 透過 strftime() 函數加上 % 符號格式化出所需字串形式
year = datetime.strftime(date, "%Y")
print(year)

# 方法二: 直接利用 datetime 物件的各個屬性
print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)
print(date.microsecond)
