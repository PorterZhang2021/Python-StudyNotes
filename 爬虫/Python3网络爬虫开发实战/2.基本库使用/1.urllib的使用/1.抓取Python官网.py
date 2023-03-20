import urllib.request

# 打开python官网
response = urllib.request.urlopen('https://www.python.org')
# 将pyhton官网的数据解析
# print(response.read().decode('utf-8'))

# 查看响应类型
print(type(response))
# 状态 响应的状态码
print(response.status)
# 头部信息 响应的头信息
print(response.getheaders())
# 头部信息中服务信息 响应头中的Server值 服务器利用Nginx搭建
print(response.getheader('Server'))