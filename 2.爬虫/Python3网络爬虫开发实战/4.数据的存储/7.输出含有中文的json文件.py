import json

data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w', encoding='utf-8') as file:
    # 此情况下输出的中文字符会变成Unicode字符
    # file.write(json.dumps(data, indent=2))
    # 输出中文指定一下参数 将ascii关闭
    file.write(json.dumps(data, indent=2, ensure_ascii=False))

# 简化写法
json.dump(data, open('data.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)