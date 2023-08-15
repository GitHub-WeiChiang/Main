import urllib.request as urllib
import json
import pymongo
import ssl

# 访问的网站若為 https 會需要 SSL 认证，
# 而直接使用 urllib 会导致本地验证失败，
# 需透過 ssl._create_unverified_context 关闭认证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://raw.githubusercontent.com/kirkchu/mongodb/main/aqi.json'

# 下載 JSON 資料並解析
response = urllib.urlopen(url)
text = response.read().decode('utf-8')

print(text)

text = text.replace('PM2.5', 'PM2_5')
text = text.replace('"AQI": ""', '"AQI": "-1"')

jsonObj = json.loads(text)

# 將資料存進 opendata 資料庫中的 AQI 資料表
client = pymongo.MongoClient()
db = client.opendata
db.AQI.insert_many(jsonObj['records'])
