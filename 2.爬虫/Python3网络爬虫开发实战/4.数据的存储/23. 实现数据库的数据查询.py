import pymysql

# 进行数据库的数据连接
db = pymysql.connect(host='localhost', user='root', passwd='123456', db='spiders')
# 数据库游标
cursor = db.cursor()

# 进行数据的查询
sql = 'SELECT * FROM students WHERE age >= 20'

try:
    # 执行数据库语句
    cursor.execute(sql)
    # 输出条数
    print('Count:', cursor.rowcount)
    # 获取数据库的首个数据记录
    one = cursor.fetchone()
    # 输出记录的信息
    print('One:', one)
    # 获取所有记录 由于游标是指针形式，因此这里是从输出后的下一个开始输出
    results = cursor.fetchall()
    # 输出记录
    print('Results:', results)
    # 查询记录类型
    print('Results Type:', type(results))
    # 按行输出
    for row in results:
        print(row)
except:
    print('Error')