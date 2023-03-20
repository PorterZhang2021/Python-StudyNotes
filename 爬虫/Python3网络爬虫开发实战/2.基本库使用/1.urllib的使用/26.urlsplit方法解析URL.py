from urllib.parse import urlsplit

# 同urlparse相似的方法
result = urlsplit('https://www.baidu.com/index.html/;user?id=5#comment')
# 输出结果
print(result)
# SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html/;user', query='id=5', fragment='comment')
# 其与urlparese的区别可能时是并不解析params参数