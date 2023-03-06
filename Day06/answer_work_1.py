"""
实现计算求最大公约数和最小公倍数的函数
"""


def gcd(x, y):
    """
    用于求最大公约数的函数
    :param x: 一个数
    :param y: 另一个数
    :return: 最大公约数
    """
    # 这里有交换操作
    # 主要是判定两个数哪个大然后进行交换
    (x, y) = (y, x) if x > y else (x, y)

    # 求解最大公约数 这里是倒序获取结果
    for factor in range(x, 0, -1):
        # 如果满足两者都能整除则成立
        if x % factor == 0 and y % factor == 0:
            # 返回结果
            return factor


def lcm(x, y):
    """
    求最小公倍数
    :param x: 一个数
    :param y: 另一个数
    :return: 最小公倍数
    """

    # 此部分主要返回的是最小公倍数
    return x * y // gcd(x, y)
