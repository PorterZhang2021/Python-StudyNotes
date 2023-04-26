import re

# 内容
content = '(百度)www.baidu.com'
# 转义字符的匹配
result = re.match('\(百度\)www\.baidu\.com', content)
# 输出匹配的转义字符
print(result)