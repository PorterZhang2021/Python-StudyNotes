from urllib import request, parse

# 请求链接url
url = 'https://www.httpbin.org/post'
# 数据
dict = {'name': 'germey'}
# 将数据转化成bytes类型
data = bytes(parse.urlencode(dict), encoding='utf-8')
# 构建request类 传入 url，data以及method的属性
req = request.Request(url=url, data=data, method='POST')
# 添加请求头
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# 构建响应请求
response = request.urlopen(req)
# 输出获得的响应请求
print(response.read().decode('utf-8'))