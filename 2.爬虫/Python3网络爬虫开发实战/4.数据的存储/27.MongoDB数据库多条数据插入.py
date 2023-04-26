from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# 指定集合
collection = db.students

# 多条数据插入
student1 = {
    'id': '20170103',
    'name': 'Kevin',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170204',
    'name': 'Mark',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])

print(result)
print(result.inserted_ids)