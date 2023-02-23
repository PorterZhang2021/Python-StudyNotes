"""
    正整数的反转
"""

# 每次取一位
# 将取得的位数重新添加回去

num = int(input('num = '))
reversed_num = 0
# 判断是否有需要转换的数
while num > 0:
    # 将初始值提升一个位数加上获得的个位
    reversed_num = reversed_num * 10 + num % 10
    # 消去个位
    num //= 10
# 输出反转数
print(reversed_num)
