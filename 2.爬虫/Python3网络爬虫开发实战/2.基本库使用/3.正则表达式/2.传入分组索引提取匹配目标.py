import re
# 内容
content = 'Hello 1234567 World_This is a Regex Demo'
# 进行匹配 起始头Hello 匹配任意字符串 这里用括号构建了分组(匹配任意数量的数字) 匹配任意字符串 World
result = re.match('^Hello\s(\d+)\sWorld', content)
# 匹配成功的SRE_Match对象
print(result)
# 匹配结果
print(result.group())
# 提取1号分组匹配的结果
print(result.group(1))
# 输出匹配的范围
print(result.span())