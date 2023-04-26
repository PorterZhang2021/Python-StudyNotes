import json

# 这种方式直接快速读取了我们需要的文件
data = json.load(open('data.json', encoding='utf-8'))
print(data)