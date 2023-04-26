import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='spiders')
# 数据库游标 
cursor = db.cursor()

# 更新数据语句
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    # 执行更新操作
    cursor.execute(sql, (25, 'Bob'))
    # 数据库执行操作
    db.commit()
except:
    # 操作回滚
    db.rollback()
# 关闭数据库
db.close()