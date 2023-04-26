import pymysql

id = '20120001'
user = 'Bob'
age = 20

# 数据库获取
db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='spiders')
# 数据库游标
cursor = db.cursor()
# 插入数据语句
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# 进行数据的插入执行
try:
    # 进行语句的执行
    cursor.execute(sql, (id, user, age))
    # 实现数据插入
    db.commit()
except:
    # 如果有问题那么进行回滚
    db.rollback()
# 关闭数据库连接
db.close()