# 文本形式保存Cookie
import urllib.request, http.cookiejar

# 文件名
file_name = r'E:\Project\PythonProject\Python-100-Days\爬虫\Python3网络爬虫开发实战\2.基本库使用\cookie_Netscape.txt'
# cookie对象
cookie = http.cookiejar.MozillaCookieJar(file_name)
# cookie保存进程
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建一个链接
opener = urllib.request.build_opener(handler)
# 响应 这里需要使用http的链接而不是https链接
response = opener.open('http://www.baidu.com')
# 将其保存进cookie
cookie.save(ignore_discard=True, ignore_expires=True)