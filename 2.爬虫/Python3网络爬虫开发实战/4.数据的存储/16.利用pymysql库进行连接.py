import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
# 数据库游标
cursor = db.cursor()
# 查询数据库版本
cursor.execute('SELECT VERSION()')
# 获取第一条输出
data = cursor.fetchone()
# 输出查询到的数据
print('Database version:', data)
# 构建一个叫spiders的数据库
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4")
# 关闭数据库连接
db.close()