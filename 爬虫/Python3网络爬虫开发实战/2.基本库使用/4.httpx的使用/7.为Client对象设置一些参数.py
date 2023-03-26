import httpx

url = 'http://www.httpbin.org/headers'
# 请求头
headers = {'User-Agent': 'my-app/0.0.1'}
# 对client对象设置请求头
with httpx.Client(headers=headers) as client:
    r = client.get(url)
    print(r.json()['headers']['User-Agent'])