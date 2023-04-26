import http.cookiejar, urllib.request

# 这个是利用虚假身份登入百度后获取cookie

# 声明一个CookieJar对象 
cookie = http.cookiejar.CookieJar()
# 构建Handler
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建一个opener类
opener = urllib.request.build_opener(handler)
# 利用其访问百度
response = opener.open('https://www.baidu.com')
# 输出cookie中的信息
for item in cookie:
    print(item.name + "=" + item.value)