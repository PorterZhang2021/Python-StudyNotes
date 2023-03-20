import urllib.request, http.cookiejar

# 构建LWP模式的cookie对象
cookie = http.cookiejar.LWPCookieJar()
# 读取文件
file_name = r'E:\Project\PythonProject\Python-100-Days\爬虫\Python3网络爬虫开发实战\2.基本库使用\cookie_LWP.txt'
# 读取对应的cookie对象文件
cookie.load(file_name, ignore_discard=True, ignore_expires=True)
# 构建链接对象
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
# 获取响应信息
response = opener.open('https://www.baidu.com')
# 输出响应信息                                                                                                                                                                    
print(response.read().decode('utf-8'))