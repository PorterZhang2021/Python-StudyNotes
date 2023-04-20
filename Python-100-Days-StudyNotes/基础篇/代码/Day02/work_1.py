"""

    华式温度转换为摄氏温度
    C = (F-32) / 1.8
"""

# temp = input(int('请输入华式温度 = '))
# 这个写法是错误的，先输入后转换
temp = int(input('请输入华氏温度 = '))

convert_temp = (temp - 32) / 1.8

# print('%d℉转换后的温度为%d℃', (temp, convert_temp))
# 这里的写法也是错误的，正确写法如下
print('%d℉转换后的温度为%d℃' % (temp, convert_temp))
