import pymongo
from pymongo import MongoClient

# 连接client
client = MongoClient('mongodb://localhost:27017')

# 指定数据库
db = client.test
# 指定集合
collection = db.students

# 数据统计
count = collection.count_documents({'age':20})
print(count)

# 数据排序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 元素偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

# 指定获取元素的个数
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

# 数据更新
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)

# 数据更新2
condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

# 多条数据更新
condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

# 删除数据
result = collection.delete_one({'name': 'Kevin'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)