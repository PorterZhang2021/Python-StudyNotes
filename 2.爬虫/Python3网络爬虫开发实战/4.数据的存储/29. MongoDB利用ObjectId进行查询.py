from pymongo import MongoClient
from bson.objectid import ObjectId

# 连接MongoDB
client = MongoClient(host='localhost', port=27017)
# 指定数据库
db = client.test
# 指定集合
collection = db['students']

# 利用id进行查询
result = collection.find_one({'_id': ObjectId('64463b587c95f1d54ab05160')})
# 获取查询到的值
print(result)