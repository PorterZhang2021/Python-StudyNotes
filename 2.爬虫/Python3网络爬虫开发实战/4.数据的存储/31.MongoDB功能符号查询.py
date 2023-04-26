from pymongo import MongoClient

# 连接数据库
client = MongoClient('mongodb://localhost:27017')

# 指定数据库
db = client.test
# 指定集合
collection = db.students

# 获取正则匹配查询的结果
results = collection.find({'name': {'$regex': '^M.*'}})
print(results)
for result in results:
    print(result)
# 查看属性是否存在
results = collection.find({'name': {'$exists': True}})
print(results)
for result in results:
    print(result)
# 进行类型判断 - 这几个操作需要看mongodb文档
results = collection.find({'name': {'$type': 'int'}})
print(results)
# 数字模操作 age的模5余0
results = collection.find({'age': {'$mode': [5, 0]}})
print(results)
# 文本查询操作 查询Mike字符串
results = collection.find({'$text': {'$search': 'Mike'}})
print(results)

# 高级条件查询 自身粉丝数等于关注数
# results = collection.find({'$where': 'obj.fans_count == obj.follows_count'})
# print(results)
# for result in results:
#     print(result)