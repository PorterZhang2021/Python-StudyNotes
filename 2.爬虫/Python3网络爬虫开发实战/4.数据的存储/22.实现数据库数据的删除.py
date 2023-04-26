import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='spiders')
# 数据库游标
cursor = db.cursor()
# 数据表
table = 'students'
# 条件
condition = 'age > 20'
# sql语句
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
# try except语句
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交语句给数据库
    db.commit()
except:
    # 数据库回滚
    db.rollback()
# 关闭数据库
db.close()