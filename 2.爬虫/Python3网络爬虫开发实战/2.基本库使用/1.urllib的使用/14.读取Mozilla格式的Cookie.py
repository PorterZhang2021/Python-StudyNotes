import urllib.request, http.cookiejar

# 读取文件
file_name = r'E:\Project\PythonProject\Python-100-Days\爬虫\Python3网络爬虫开发实战\2.基本库使用\cookie_Netscape.txt'
# 构建一个cookie对象
cookie = http.cookiejar.MozillaCookieJar()
# 读取此文件
cookie.load(file_name, ignore_discard=True, ignore_expires=True)
# 构建cookie的handler
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建一个opener对象
opener = urllib.request.build_opener(handler)
# 进行请求响应 这里需要使用http的链接而不是https链接
response = opener.open('http://www.baidu.com')
# 输出响应信息
print(response.read().decode('utf-8'))