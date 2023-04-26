import requests

# get请求
r = requests.get('https://www.baidu.com')
# 查看cookies
print(r.cookies)
# 输出cookies
for key, value in r.cookies.items():
    print(key + '=' + value)