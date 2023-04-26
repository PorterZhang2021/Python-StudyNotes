import urllib.request

# request类 这里request的是python官网
request = urllib.request.Request('https://python.org')
# 响应 这里用的依然是urlopen 但是直接传入了一个request类作为请求
response = urllib.request.urlopen(request)
# 打印响应信息 
print(response.read().decode('utf-8'))