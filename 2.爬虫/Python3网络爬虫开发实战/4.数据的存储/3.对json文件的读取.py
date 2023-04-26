import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1995-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
# 查看str的累心
print(type(str))
# 读取str
data = json.loads(str)
# 以json方式输出
print(data)
# 查看输出后的类型
print(type(data))
# 获取json格式的属性
print(data[0]['name'])
print(data[0].get('name'))
# 优先使用get方法，因为直接查找会报错
# get方法可以设置默认值
print(data[0].get('age'))
print(data[0].get('age', 25))

# json数据需要双引号数据包裹
str = '''
[{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
'''
# 这种情况下会报错
# data = json.loads(str)