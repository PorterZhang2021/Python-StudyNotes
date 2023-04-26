import csv

with open('data.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'age']
    # 初始化一个字典写入对象
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 写入字典头
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
    