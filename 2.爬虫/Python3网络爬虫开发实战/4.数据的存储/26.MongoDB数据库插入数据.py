from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# 指定集合
collection = db.students

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

# 调用collection类的insert方法插入数据
result = collection.insert_one(student)
print(type(result))
# 获取id对象
print(result.inserted_id)