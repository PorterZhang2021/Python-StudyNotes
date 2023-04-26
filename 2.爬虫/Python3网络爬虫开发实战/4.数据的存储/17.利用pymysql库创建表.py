import pymysql

# 创建数据库后，在连接时需要额外指定一个参数db
db = pymysql.connect(host='localhost', user='root', passwd='123456', db='spiders')
# 获取数据库游标
cursor = db.cursor()
# 创建一个表
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL,' + \
      'age INT NOT NULL, PRIMARY KEY(id))'
# 执行数据库语句
cursor.execute(sql)
# 关闭数据库
db.close()