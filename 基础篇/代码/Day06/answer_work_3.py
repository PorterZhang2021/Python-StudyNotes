"""
实现判断一个数是不是素数的函数
"""


def is_prime(num):
    """判断一个数是不是素数"""
    # 用于判定是否会被其他数整除
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    # 这里说明如果不是1则继续返回False
    return True if num != 1 else False
