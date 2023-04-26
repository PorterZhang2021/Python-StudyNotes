from pymongo import MongoClient

# 连接数据库
client = MongoClient(host='localhost', port=27017)
# 指定数据库
db = client.test
# 指定集合
collection = db.students

# 查询小于20的数据
results = collection.find({'age': {'$lt': 20}})
# 生成器对象
print(results)
for result in results:
    print(result)
# 查询大于20的数据
results = collection.find({'age': {'$gt': 20}})
print(results)
for result in results:
    print(result)
# 查询小于等于20的数据
results = collection.find({'age': {'$lte': 20}})
print(results)
for result in results:
    print(result)
# 查询大于等于20的数据
results = collection.find({'age': {'$gte': 20}})
print(results)
for result in results:
    print(result)
# 查询不等于20的数据
results = collection.find({'age': {'$ne': 20}})
print(results)
for result in results:
    print(result)
# 查询在20到23范围的数据
results = collection.find({'age': {'$in': [20, 23]}})
print(results)
for result in results:
    print(result)
# 查询不在20到23范围内的数据
results = collection.find({'age': {'$nin': [20, 23]}})
print(results)
for result in results:
    print(result)
