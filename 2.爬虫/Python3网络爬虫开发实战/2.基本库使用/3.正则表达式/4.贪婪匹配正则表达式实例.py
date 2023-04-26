import re

# 内容
content = 'Hello 1234567 World_This is a Regex Demo'
# 正则匹配式 开始 He 匹配任意字符 (分组 匹配任意数量数字) 匹配任意字符 Demo 结束
# 这里的.*默认是使用的贪婪匹配，因此在这种情况下，我们的分组中只匹配到了一个7
result = re.match('^He.*(\d+).*Demo$', content)
# 输出正则匹配结果
print(result)
# 输出分组匹配结果
print(result.group(1))