from urllib.parse import urlparse

# 这里url直接带了http
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https:')
print(result)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
# 这里可以发现传入的scheme失效了，直接使用的url的方案