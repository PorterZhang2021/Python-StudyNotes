import re

# 从头部以外的位置进行字符串的匹配
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra   stings'
# match匹配需要从字符串的开始进行匹配 所以不成功
# 这里再字符串中间进行匹配 使用的是search方法
result = re.search('Hello.*?(\d+).*?Demo', content)
# 输出匹配后的对象
print(result)