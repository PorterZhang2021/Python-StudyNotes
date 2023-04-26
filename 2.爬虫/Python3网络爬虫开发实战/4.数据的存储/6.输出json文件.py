import json

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w', encoding='utf-8') as file:
    # 此方式只是直接输出
    # file.write(json.dumps(data))
    # 按json的缩进格式进行输出
    file.write(json.dumps(data, indent=2))