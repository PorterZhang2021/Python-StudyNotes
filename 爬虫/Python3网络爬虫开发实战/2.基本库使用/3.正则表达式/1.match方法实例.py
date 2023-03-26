import re

# 文本内容
content = 'Hello 123 4567 World_This is a Regex Demo'
# 文本长度
print(len(content))
# 正则表达匹配式
# Hello 匹配任意空白字符串 匹配任意数字(3个) 匹配任意空白字符串 匹配任意数字{4} 匹配任意空白字符串 匹配字母、数字、下划线{10}
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content, re.S)
# 输出SRE_Match对象
print(result)
# 输出匹配到的内容
print(result.group())
# 输出匹配范围
print(result.span())