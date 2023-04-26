from urllib.parse import parse_qs

# get请求query
query = 'name=germy&age=25'
# 反序列化 URL参数转回字典类型
print(parse_qs(query))