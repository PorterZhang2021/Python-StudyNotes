from urllib.parse import urlparse

# url解析 这里将允许解析锚点关闭了
result = urlparse('https://www.baidu.com/index.html#comment', allow_fragments=False)
# 利用属性输出或者利用数组索引形式输出
print(result.scheme, result[0], result.netloc, result[1], sep='\n')