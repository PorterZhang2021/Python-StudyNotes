from urllib.parse import parse_qsl

# 查询
query = 'name=germey&age=25'
# 以元组的形式输出URL参数
print(parse_qsl(query))
