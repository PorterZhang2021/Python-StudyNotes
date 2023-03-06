"""
 输入两个正整数，计算它们的最大公约数和最小公倍数

 两个数的最大公约数是两个数的公共因子中最大的那个数
 两个数的最小公倍数是能够同时被两个数整除的最小的那个数
"""


# 输入两个正整数
number1 = int(input('请输入一个正整数:'))
number2 = int(input('请输入另一个正整数:'))



# 两个数的最大公约数是两个数的公共因子中最大的那个数
# greatest_common_divisor = 0
# 求出最大公共因子
def gdc(number_1, number_2):
    for i in range(1, max(number_1, number_2)):
        # 公共因子 -> 满足 number1 % i == 0 and number2 % i == 0
        if number1 % i == 0 and number2 % i == 0:
            greatest_common_divisor = i
    return greatest_common_divisor

# 两个数的最小公倍数是能够同时被两个数整除的最小的那个数
# 为什么最大公约数和最小公倍数的题会联系
# 这是因为最小公倍数 = 两个数的乘积 / 最大公约数
# 所以求解最大公约数是求解最小公倍数的题目的一部分
def lcm(number_1, number_2):
    greatest_common_divisor = gdc(number_1, number_2)
    least_common_multiple = (number1 * number2) / greatest_common_divisor
    return least_common_multiple

# 获取最大公共因子
greatest_common_divisor = gdc(number1, number2)
# 获取最小公倍数
least_common_multiple = lcm(number1, number2)
# 输出
print('数:%d和%d的最大公约数是%d，最小公倍数是:%d' % (number1, number2, greatest_common_divisor, least_common_multiple))