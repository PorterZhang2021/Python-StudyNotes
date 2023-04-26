import re
# 内容
content = '54aK54yr5oiR54ix5L2g'
# 替换输出
content = re.sub('\d+', '', content)
# 输出替换后的内容
print(content)