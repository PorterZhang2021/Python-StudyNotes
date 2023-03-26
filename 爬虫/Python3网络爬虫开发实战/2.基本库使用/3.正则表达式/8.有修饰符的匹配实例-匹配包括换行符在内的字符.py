import re

# 内容
content = '''Hello 1234567 World_This
is a Regex Demo
'''
# 结果 这里的修饰符为匹配内容包括re.S的匹配
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# 分组
print(result.group(1))

# 相关的匹配修饰符
# 修饰符 描述
# re.I 使匹配对大小写不敏感
# re.L 实现本地化识别-(local-aware)匹配
# re.M 多行匹配，影响^和$
# re.S 使匹配内容包括换行符在内的所有字符
# re.U 根据Unicode字符集解析字符，这个标志会影响\w、\W、\b和\B
# re.X 该标志能够给予你更灵活的格式，以便将正则表达式书写得更易于理解