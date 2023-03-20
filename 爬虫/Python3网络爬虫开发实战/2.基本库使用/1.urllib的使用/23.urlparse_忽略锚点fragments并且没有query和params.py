from urllib.parse import urlparse

# 这里没有参数;params和查询?query
result = urlparse('https://www.baidu.com/index.html#comment', allow_fragments=False)
# 输出结果
print(result)
# ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html#comment', params='', query='', fragment='')
# 这里忽略了锚点的部分