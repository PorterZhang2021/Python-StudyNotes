import requests

# Session维持
s = requests.Session()
# 设置cookies
s.get('https://www.httpbin.org/cookies/set/number/123456789')
# 进行请求
r = s.get('https://www.httpbin.org/cookies')
# 获取请求后的响应信息
print(r.text)