import re

# 内容
content = 'Hello 123 4567 World_This is a Regex Demo'
# match方法 ^开始头 Hello 匹配任意字符数 $匹配结尾
result = re.match('^Hello.*Demo$', content)
# SRE_Match对象
print(result)
# 输出匹配目标
print(result.group())
# 输出匹配的范围         
print(result.span())