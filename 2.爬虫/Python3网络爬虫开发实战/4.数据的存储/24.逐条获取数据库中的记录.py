import pymysql

db = pymysql.connect(host='localhost', user='root', passwd='123456', db='spiders')
cursor = db.cursor()

# 逐条获取数据
sql = 'SELECT * FROM students WHERE age >= 20'
# 获取查询的记录
try:
    # 进行sql语句的执行
    cursor.execute(sql)
    # 输出行数
    print('Count:', cursor.rowcount)
    # 输出记录
    row = cursor.fetchone()
    # 逐条输出记录
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
