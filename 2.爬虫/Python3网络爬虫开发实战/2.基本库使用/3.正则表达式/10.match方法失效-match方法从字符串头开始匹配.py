import re
# 内容
content = 'Extra stings Hello 1234567 Worl_This is a Regex Demo Extra    stings'
# match匹配方法 Hello .*? 非贪婪匹配-匹配任意数量的字符-最少 (\d+)-分组-匹配任意数量的数字 
# .*? 非贪婪匹配-匹配任意数量的字符-最少 Demo
result = re.match('Hello.*?(\d+).*?Demo', content)
# 输出匹配后的对象
print(result)