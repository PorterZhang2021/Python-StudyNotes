from urllib.parse import urlsplit

# urlsplit方法
result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# 通过属性或者索引获得输出
print(result.scheme, result[0])
