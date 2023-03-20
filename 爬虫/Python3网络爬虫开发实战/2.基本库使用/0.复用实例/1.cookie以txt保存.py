# 文本形式保存Cookie
import urllib.request, http.cookiejar

# 文件名
file_name = r'文件保存地址'
# cookie对象 这里分为Mozilla与LWP两种
cookie_Mozilla = http.cookiejar.MozillaCookieJar(file_name)
cookie_LWP = http.cookiejar.LWPCookieJar(file_name)
# cookie保存到http中的cookie处理器中
handler_Mozilla = urllib.request.HTTPCookieProcessor(cookie_Mozilla)
handler_LWP = urllib.request.HTTPCookieProcessor(cookie_LWP)
# 构建一个opener对象
opener_Mozilla = urllib.request.build_opener(handler_Mozilla)
opener_LWP = urllib.request.HTTPCookieProcessor(handler_LWP)
# 进行请求响应
response_Mozilla = opener_Mozilla.open('请求链接')
response_LWP = opener_LWP.open('请求链接')
# 保存cookie
cookie_Mozilla.save(ignore_discard=True, ignore_expires=True)
cookie_LWP.save(ignore_discard=True, ignore_expires=True)