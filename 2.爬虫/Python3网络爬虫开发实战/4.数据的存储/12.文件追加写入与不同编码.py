import csv

with open('data.csv', 'a', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})
    # 新追加为中文 如果open函数没有指定编码会输出乱码
    writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})