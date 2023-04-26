from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)

# 指定数据库
db = client.test
# 指定集合
collection = db.students

# 查询数据
result = collection.find_one({'name': 'Mike'})
# 查看其类型
print(type(result))
# 输出查询到的对象
print(result)
