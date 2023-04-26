from urllib.parse import urlparse

# 解析百度页面
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
# 输出其实例对象类型
print(type(result))
# 输出解析结果
print(result)
# :// 前为scheme  / 前为netloc:域名 / path:访问路径 ; params 参数  ? query查询条件  # fragment 锚点
# ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
# scheme://netloc/path;params?query#fragment