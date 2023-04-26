import httpx

# 链接
url = 'https://www.httpbin.org/'
# 请求数据
data = {
    'name': 'germey'
}

# get方法
r = httpx.get(url+'get', params=data)
# post方法
r = httpx.post(url+'post', data=data)
# put方法
r = httpx.put(url+'put')
# delete方法
r = httpx.delete(url+'delete')
# patch方法
r = httpx.patch(url+'patch')