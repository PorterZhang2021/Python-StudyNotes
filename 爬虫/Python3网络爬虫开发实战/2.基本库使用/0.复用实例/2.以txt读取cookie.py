import urllib.request, http.cookiejar

# 读取文件
file_name = r'cookie存储地址'
# 构建一个cookie对象
cookie_Mozilla = http.cookiejar.MozillaCookieJar()
cookie_LWP = http.cookiejar.LWPCookieJar()
# 读取此文件
cookie_Mozilla.load(file_name, ignore_discard=True, ignore_expires=True)
cookie_LWP.load(file_name, ignore_discard=True, ignore_expires=True)
# 构建cookie的handler
handler_Mozilla = urllib.request.HTTPCookieProcessor(cookie_Mozilla)
handler_LWP = urllib.request.HTTPCookieProcessor(cookie_LWP)
# 构建一个opener对象
opener_Mozilla = urllib.request.build_opener(handler_Mozilla)
opener_LWP = urllib.request.build_opener(handler_LWP)
# 进行请求响应 这里需要使用http的链接而不是https链接
response_Mozilla = opener_Mozilla.open('请求链接')
response_LWP = opener_LWP.open('请求链接')
# 输出响应信息
print(response_Mozilla.read().decode('utf-8'))
print(response_LWP.read().decode('utf-8'))
                                                                                                                                                                   

