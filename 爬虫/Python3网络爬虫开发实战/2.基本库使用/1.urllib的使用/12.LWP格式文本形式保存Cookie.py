import urllib.request, http.cookiejar

file_name = r'E:\Project\PythonProject\Python-100-Days\爬虫\Python3网络爬虫开发实战\2.基本库使用\cookie_LWP.txt'
# 利用LWP格式
cookie = http.cookiejar.LWPCookieJar(file_name)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)