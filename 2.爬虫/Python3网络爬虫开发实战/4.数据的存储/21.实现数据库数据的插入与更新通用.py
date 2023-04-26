import pymysql

db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '20120004',
    'name': 'Nancy',
    'age': 23
}

# 表名
table = 'students'
# 键名
keys = ','.join(data.keys())
# 值名
values = ','.join(['%s'] * len(data))
# sql语句
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table,  
    keys=keys, values=values)
# 更新语句
update = ','.join(["{key} = %s".format(key=key) for key in data])
# 构建插入或者更新语句
sql += update

# 进行尝试
try:
    # 如果语句能够执行
    if cursor.execute(sql, tuple(data.values())*2):
        # 输出成功
        print('Successful')
        # 数据库内执行操作
        db.commit()
    else:
        # 输出没有修改
        print('No change')
except:
    # 失败
    print('Failed')
    # 进行操作回滚
    db.rollback()
# 关闭数据库
db.close()