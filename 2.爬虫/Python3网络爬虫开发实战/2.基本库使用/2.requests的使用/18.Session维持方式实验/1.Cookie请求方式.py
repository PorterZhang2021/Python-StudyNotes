import requests
# 进行get请求
requests.get('https://www.httpbin.org/cookies/set/number/123456789')
# 进行get请求
r = requests.get('https://www.httpbin.org/cookies')
# 输出响应信息
print(r.text)