import requests

# get请求
r = requests.get('https://www.httpbin.org/get')
# post请求
r = requests.post('https://www.httpbin.org/post')
# put请求
r = requests.put('https://www.httpbin.org/put')
# delete请求
r = requests.delete('https://www.httpbin.org/delete')
# patch请求
r = requests.patch('https://www.httpbin.org/patch')