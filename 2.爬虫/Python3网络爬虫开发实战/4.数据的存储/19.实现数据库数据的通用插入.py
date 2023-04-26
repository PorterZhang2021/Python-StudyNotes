import pymysql

# 创建数据库
db = pymysql.connect(host='localhost', user='root', passwd='123456', db='spiders')
# 获取数据游标
cursor = db.cursor()

# 数据
data = {
    'id': '20120001', 
    'name': 'Bob',
    'age': 20
}

# 表名
table = 'students'
# 键值名
keys = ','.join(data.keys())
# 值名
values = ','.join(['%s'] * len(data))
# 需要创建的sql语句
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# 进行创建
try:
    # 如果满足要求
    if cursor.execute(sql, tuple(data.values())):
        # 输出成功
        print('Successful')
        # 执行插入操作
        db.commit()
except:
    # 输出失败
    print('Failed')
    # 进行回滚
    db.rollback()
# 关闭数据库
db.close()
