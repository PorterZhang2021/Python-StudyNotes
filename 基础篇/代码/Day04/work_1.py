"""
输入一个正整数判断是不是素数
素数指的是只能被1和自身整除的大于1的数
"""
# 平方根
from math import sqrt

# 输入一个数
number = int(input('请输入一个数（大于1）:'))

# + 可以利用平方根来缩减规模效率
end = int(sqrt(number))

# 循环1到这个数的值 -> 每个都可以被1和其自身整除
# 那么我只需要验证范围(2, number)即可了
flag = 0
# for i in range(2, number):
# 规模缩减
for i in range(2, end + 1):
    # 求余运算如果出现相等
    if number % i == 0:
        # 那么就将flag标记为1
        flag = 1
        # + 直接跳出循环 再次缩减规模
        break

# 如果flag为1 不是素数
if flag == 1 or number == 1:
    print('这个数不是素数')
# 如果flag为0 是素数
else:
    print('这个数是素数')
