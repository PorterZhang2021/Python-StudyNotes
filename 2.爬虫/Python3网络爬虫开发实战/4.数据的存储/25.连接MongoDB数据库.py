import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
# 另一种连接方式
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# 另一种指定方式
# db = client['test']

# 指定集合
collection = db.students
# 另一种指定方式
# collection = db['students']

