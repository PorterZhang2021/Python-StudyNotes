from urllib import request, parse

# url用于请求的url
url = 'https://www.httpbin.org/post'
# 请求头 这里是模拟伪装自己是个浏览器
headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'www.httpbin.org'
}
# 字典 用于后续传入data中的数据
dict = {'name': 'germey'}
# data 传输数据 传输必须是bytes类型
data = bytes(parse.urlencode(dict), encoding='utf-8')
# 构建一个request类对象，方法为POST
req = request.Request(url=url, data=data, headers=headers, method='POST')
# 响应信息 这里直接传入一个request对象
response = request.urlopen(req)
# 输出响应后的信息以utf-8的格式
print(response.read().decode('utf-8'))