from urllib.parse import urlunparse
# 构建url链接的数据
data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# 构建链接
print(urlunparse(data))