from urllib.parse import urlparse

# 这里将scheme://netloc/path;params?query#fragment 拆分开
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# 输出结果
print(result)
# ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=5', fragment='comment')
# 这个部分对netloc解析具有错误