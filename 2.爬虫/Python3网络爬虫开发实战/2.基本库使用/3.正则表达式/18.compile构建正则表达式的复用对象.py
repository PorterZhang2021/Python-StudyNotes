import re

# 内容1
content1 = '2019-12-15 12:00'
# 内容2
content2 = '2019-12-17 12:55'
# 内容3
content3 = '2019-12-22 13:21'
# 此方法将正则表达式编辑成正则表达式对象，以便后面的匹配与复用
pattern = re.compile('\d{2}:\d{2}')
# 查看由compile构建后的pattern对象是什么
print(type(pattern))
# 复用方案1
result1 = re.sub(pattern, '', content1)
# 复用方案2
result2 = re.sub(pattern, '', content2)
# 复用方案3
result3 = re.sub(pattern, '', content3)
# 输出复用后的结果
print(result1, result2, result3)