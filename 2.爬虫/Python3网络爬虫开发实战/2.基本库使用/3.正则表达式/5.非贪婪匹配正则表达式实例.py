import re

# 内容
content = 'Hello 1234567 World_This is a Regex Demo'
# 进行匹配 这里的匹配 开始 He .*? 匹配任意字符-非贪婪匹配 (\d+) 匹配任意数量的数字 .*匹配任意数量的字符 Demo $结尾
result = re.match('^He.*?(\d+).*Demo$', content)
# 输出匹配结果
print(result)
# 分组
print(result.group(1))
