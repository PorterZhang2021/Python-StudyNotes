import requests

# timeout超时响应请求 这里传入元组 前面为请求连接connect 后面是读出时间read
r = requests.get('https://www.httpbin.org/get', timeout=(5, 30))
# 状态码
print(r.status_code)
# 不限制等待时间 当然不写效果同理
r = requests.get('https://www.httpbin.org/get', timeout=None)
print(r.status_code)
