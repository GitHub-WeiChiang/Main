import pymongo

hosts = [
    "localhost:20000",
    "localhost:20001",
    "localhost:20002"
]

client = pymongo.MongoClient(hosts)
