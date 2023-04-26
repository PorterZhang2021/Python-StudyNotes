import urllib.parse
import urllib.request

# 将其以二进制代码的形式保存 这里传递的是以form表单的形式
data = bytes(urllib.parse.urlencode({'name':'germey'}), encoding='utf-8')
# 获取httpbin网址的响应 data传递的是数据请求参数
response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# 将响应信息以utf-8的形式输出
print(response.read().decode('utf-8'))