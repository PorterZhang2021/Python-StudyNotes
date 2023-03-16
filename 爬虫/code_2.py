"""
# 添加请求头信息
urllib.request.Request(url, data=None, headers={}, method=None)
url: 请求连接
data: 数据
headers: 请求头信息
method: 请求方法
"""
from urllib import request, parse
import ssl

# ssl未经验证的上下文
context = ssl._create_unverified_context()

# 请求url
url = 'https://biihu.cc//account/ajax/login_process'
# 请求header
headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
# 请求参数
dict = {
    'return_url': 'https://biihu.cc/',
    'user_name':'xiaoshuaib@gmail.com',
    'password':'123456789',
    '_post_type': 'ajax',
}

# 请求参数转化为byte
data = bytes(parse.urlencode(dict), 'utf-8')
# 封装request
req = request.Request(url, data=data, headers=headers, method='POST')
# 进行请求
response = request.urlopen(req, context=context)
print(response.read().decode('utf-8'))
