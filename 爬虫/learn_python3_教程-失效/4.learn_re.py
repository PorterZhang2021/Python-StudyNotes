import re
# 拿出数字
content = 'Xiaoshuaib has 100 bananas'
# 贪婪匹配
res = re.match('^Xi.*(\d+).*s$', content)
print(res.group(1))

content = 'Xiaoshuaib has 100 bananas'
# 非贪婪匹配
res = re.match('^Xi.*?(\d+).*s$', content)
print(res.group(1))

content = """Xiaoshuaib has 100
bananas"""
# 字符串有换行 利用re.S进行匹配
res = re.match('^Xi.*?(\d+).*s$', content, re.S)
print(res.group(1))

# 匹配返回第一个结果
res = re.match('Xi.*?(\d+).*s', content, re.S)
print(res.group(1))

# 获取所有的100
content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""

# 轻松获取所有匹配内容
res = re.findall('Xi.*?(\d+).*?s;', content, re.S)
print(res)

# 100直接替换成250
content = re.sub('\d+', '250', content)
print(content)

# 将匹配符封装
# 通过这种方式可以帮助复用
pattern = re.compile('Xi.*?(\d+).*s', re.S)
res = re.match(pattern, content)

print(res.group(1))