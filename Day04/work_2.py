"""
 输入两个正整数，计算它们的最大公约数和最小公倍数

 两个数的最大公约数是两个数的公共因子中最大的那个数
 两个数的最小公倍数是能够同时被两个数整除的最小的那个数
"""

# 输入两个正整数
number1 = int(input('请输入一个正整数:'))
number2 = int(input('请输入另一个正整数:'))

# 拿最大的那个数作为循环的末尾
if number1 > number2:
    for_number = number1
else:
    for_number = number2

# - 这一部分可以直接进行交换
# if number1 > number2:
#     number1, number2 = number2, number1

# 两个数的最大公约数是两个数的公共因子中最大的那个数
# greatest_common_divisor = 0
# 求出最大公共因子
for i in range(1, for_number):
    # 公共因子 -> 满足 number1 % i == 0 and number2 % i == 0
    if number1 % i == 0 and number2 % i == 0:
        greatest_common_divisor = i

# 两个数的最小公倍数是能够同时被两个数整除的最小的那个数
# 为什么最大公约数和最小公倍数的题会联系
# 这是因为最小公倍数 = 两个数的乘积 / 最大公约数
# 所以求解最大公约数是求解最小公倍数的题目的一部分
least_common_multiple = (number1 * number2) / greatest_common_divisor

# 输出
print('数:%d和%d的最大公约数是%d，最小公倍数是:%d' %
      (number1, number2, greatest_common_divisor, least_common_multiple))
