from urllib.parse import urlparse

# 这里将fragments进行了忽略
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# 输出时没有framents而是直接和之前的params和query组合了
print(result)
# ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5#comment', fragment='')