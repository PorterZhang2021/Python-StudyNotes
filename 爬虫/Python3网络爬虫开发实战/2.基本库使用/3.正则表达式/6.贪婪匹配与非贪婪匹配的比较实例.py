import re

content = 'http://weibo.com/comment/kEraCN'
# 这个为非贪婪匹配 http .*? 非贪婪匹配 匹配任意数量字符串 尽量匹配最少 comment/ (分组.*?) 这里也是匹配任意数量字符串 尽可能匹配最少
result1 = re.match('http.*?comment/(.*?)', content)
# 这个为贪婪匹配 http .*? 非贪婪匹配 匹配任意数量字符串 尽量匹配最少  comment/ (分组.*) 这里也是匹配任意数量字符串 尽可能匹配最多
result2 = re.match('http.*?comment/(.*)', content)
print('result1:', result1.group(1))
print('result2:', result2.group(1))