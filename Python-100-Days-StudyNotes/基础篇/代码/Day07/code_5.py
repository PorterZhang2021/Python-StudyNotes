# * 运算符用来实现重复一个字符串的内容
s1 = 'hello' * 3
# 打印结果
print(s1)

s2 = 'world'
# 字符串的拼接
s1 += s2
print(s1)

# in 判断是否包含此字符串 返回布尔值
print('ll' in s1)
print('good' in s1)

# 新字符串
str2 = 'abc123456'

# 指定下标的字符
print(str2[2])
# 指定下标的字符 开始:结束
print(str2[2:5])
# 指定下标的字符 开始: -> 一直到结束
print(str2[2:])
# 逆序输出
print(str2[::-1])
# 反向截取 倒数第三位到倒数第一位
print(str2[-3:-1])
