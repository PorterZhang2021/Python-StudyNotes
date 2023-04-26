import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
# 这里可以发现匹配式子和之前一致
# ^开始 He .*? 匹配任意数量字符-最少-非贪婪匹配 (\d+) 匹配任意数量数字 .*? 匹配任意数量字符-最少-非贪婪匹配 Demo $结束
result = re.match('^He.*?(\d+).*?Demo$', content)
# 这里由于出现了换行，导致上面的match方法无法匹配到对应的对象，所以没有分组
print(result.group(1))