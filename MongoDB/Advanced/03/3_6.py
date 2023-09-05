import pymongo
import gridfs

client = pymongo.MongoClient()
db_test = client.test

# # 儲存檔案
# file_name = "avatar_winter.JPG"
# fs = gridfs.GridFS(db_test)
# with open(file_name, "rb") as f:
#     fs.put(f, filename=file_name)
# # 取出檔案
# file_name = "avatar_winter.JPG"
# fs = gridfs.GridFS(db_test)
# file = fs.find_one({"filename": file_name})
# with open(file.filename, "wb") as f:
#     f.write(file.read())
# # 刪除檔案
# file_name = "avatar_winter.JPG"
# fs = gridfs.GridFS(db_test)
# file = fs.find_one({"filename": file_name})
# if file is not None:
#     fs.delete(file.id)
# else:
#     print("{} not found".format(file_name))
# # 列出儲存的檔案
# fs = gridfs.GridFS(db_test)
# for filename in fs.list():
#     print(filename)
# # 列出檔案的詳細資訊
# fs = gridfs.GridFS(db_test)
# for file in fs.find():
#     print("file name: {}".format(file.filename))
#     print("upload date: {}".format(file.uploadDate))
#     print("length: {}".format(file.length))
#
# # 對儲存的檔案加上額外資訊
# file_name = "avatar_winter.JPG"
# fs = gridfs.GridFS(db_test)
# with open(file_name, "rb") as f:
#     fs.put(f, filename=file_name, version=2.0)
# # 取出 2.0 版本的老婆
# file_name = "avatar_winter.JPG"
# fs = gridfs.GridFS(db_test)
# file = fs.find_one({"filename": file_name, "version": 2.0})
# with open(file.filename, "wb") as f:
#     f.write(file.read())
# # 使用 get_last_version() 函数取得最新版本的檔案
# file_name = "avatar_winter.JPG"
# fs = gridfs.GridFS(db_test)
# file = fs.get_last_version(file_name)
# with open(file.filename, "wb") as f:
#     f.write(file.read())
