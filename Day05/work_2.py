"""
找出10000以内的完美数
说明：完美数又称为完全数或完备数，
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）
恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
完美数有很多神奇的特性，有兴趣的可以自行了解。

10000以内拿到一个数 -> 循环
求出其因子 -> 循环
因子求和得出结果与数比较 -> 判断
"""
import math

# 10000以内的数
for i in range(1, 10001):
    # 用于因子求和
    number = 0

    # 求出因子
    for j in range(1, i):
        # 判断是否是因子
        if i % j == 0:
            # 因子求和
            number += j

    # 判断是否是完美数
    if number == i:
        print(number)

"""
完美数
# 输出2到9999之间的数
for num in range(2, 10000):
    # 
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor = 0:
            result += factor
            # 暂时不能理解这个
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
"""