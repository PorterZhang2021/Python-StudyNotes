from requests import Request, Session

# 链接
url = 'https://www.httpbin.org/post'
# 数据
data = {
    'name': 'germey'
}
# 伪装请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
# session
s = Session()
# 构造Request请求对象
req = Request('POST', url, data=data, headers=headers)
# 将Request对象转换成Prepared Request对象
prepped = s.prepare_request(req)
# 发送
r = s.send(prepped)
# 获取信息
print(r.text)

# 这里将request的请求直接转化成了一个对象，对于一些需要请求调度操作的场景可能很有帮助